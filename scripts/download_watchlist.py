#!/usr/bin/env python3
"""
download_watchlist.py — 自動從 Google Sheets 下載 Watchlist 並解析成日報

Claude Code Routines 執行入口。每日執行一次：
  1. 用 token.json 靜默認證（無需人工操作）
  2. 下載試算表為 .xlsx
  3. 呼叫 parse_watchlist.py 解析並輸出 Markdown

用法：
    python3 scripts/download_watchlist.py

環境需求：
    config/token.json（執行 google_auth.py 後自動生成）
"""

import io
import os
import sys
import subprocess
from datetime import date

import openpyxl
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# 把 scripts/ 加入 path，才能 import google_auth
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from google_auth import get_credentials

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR  = os.path.join(PROJECT_ROOT, "reports")
SCRIPTS_DIR  = os.path.join(PROJECT_ROOT, "scripts")

# TheMarketMemo 試算表 ID（從 URL 取得）
SHEET_ID = "1HlM-6fb9Hg2oEnqMWtWjcn6KNB5-mgt8oOrxKdv8O_Y"

# 試算表中要讀取的工作表
TARGET_SHEETS = ["Assets", "Structure", "Industry"]


def download_via_sheets_api(creds, sheet_id, out_path):
    """
    用 Sheets API v4 讀取試算表數據，存成 .xlsx。
    只需要 spreadsheets.readonly scope，不依賴 Drive API 或 export URL。
    """
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    service = build("sheets", "v4", credentials=creds)
    spreadsheet = service.spreadsheets()

    # 取得所有工作表名稱
    meta = spreadsheet.get(spreadsheetId=sheet_id).execute()
    all_sheet_names = [s["properties"]["title"] for s in meta.get("sheets", [])]

    # 只讀 TARGET_SHEETS（跳過不需要的）
    sheets_to_read = [s for s in all_sheet_names if s in TARGET_SHEETS]
    if not sheets_to_read:
        sheets_to_read = all_sheet_names  # fallback：讀全部

    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # 移除預設空白工作表

    for sheet_name in sheets_to_read:
        result = spreadsheet.values().get(
            spreadsheetId=sheet_id,
            range=sheet_name,
        ).execute()
        values = result.get("values", [])

        ws = wb.create_sheet(title=sheet_name)
        for row in values:
            ws.append(row)

    wb.save(out_path)
    return True


def main():
    today = date.today()
    date_str = today.strftime("%Y-%m-%d")
    mmdd = today.strftime("%m%d")

    os.makedirs(REPORTS_DIR, exist_ok=True)

    # ── 步驟 1：取得憑證（自動刷新，無頭執行）──
    print(f"[{date_str}] 取得 Google 認證...")
    creds = get_credentials()
    print("認證成功")

    # ── 步驟 2：用 Sheets API 讀取試算表 ──
    xlsx_path = os.path.join(PROJECT_ROOT, f"Market Watchlist{mmdd}.xlsx")
    print(f"讀取試算表至 {xlsx_path}...")
    try:
        ok = download_via_sheets_api(creds, SHEET_ID, xlsx_path)
    except Exception as e:
        print(f"[錯誤] Sheets API 失敗：{e}")
        sys.exit(1)
    if not ok:
        sys.exit(1)
    print(f"完成（{os.path.getsize(xlsx_path) / 1024:.1f} KB）")

    # ── 步驟 3：解析並輸出 Markdown ──
    print("解析 Watchlist...")
    parse_script = os.path.join(SCRIPTS_DIR, "parse_watchlist.py")
    result = subprocess.run(
        [sys.executable, parse_script, xlsx_path],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        print(result.stdout.strip())
        print(f"\n完成：reports/{date_str}_watchlist.md")
    else:
        print("[錯誤] 解析失敗：")
        print(result.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
