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

import os
import sys
import subprocess
from datetime import date

import requests
from google.auth.transport.requests import Request

# 把 scripts/ 加入 path，才能 import google_auth
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from google_auth import get_credentials

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR  = os.path.join(PROJECT_ROOT, "reports")
SCRIPTS_DIR  = os.path.join(PROJECT_ROOT, "scripts")

# TheMarketMemo 試算表 ID（從 URL 取得）
SHEET_ID = "1HlM-6fb9Hg2oEnqMWtWjcn6KNB5-mgt8oOrxKdv8O_Y"


def download_xlsx(creds, sheet_id, out_path):
    """用 OAuth2 token 下載 Google Sheets 為 .xlsx 檔案。"""
    # 確保 token 是有效的
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # Drive API v3 export endpoint — 正確接受 OAuth2 Bearer token
    # docs.google.com/export 是 browser-cookie 導向，不適合 API 呼叫
    export_url = (
        f"https://www.googleapis.com/drive/v3/files/{sheet_id}/export"
        f"?mimeType=application%2Fvnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    headers = {"Authorization": f"Bearer {creds.token}"}
    response = requests.get(export_url, headers=headers, timeout=30)

    if response.status_code == 200:
        with open(out_path, "wb") as f:
            f.write(response.content)
        return True
    elif response.status_code == 401:
        print("[錯誤] 認證失敗，請重新執行 python3 scripts/google_auth.py")
        return False
    elif response.status_code == 403:
        print("[錯誤] 沒有存取權限。請確認 Google 帳號有這份試算表的查看權限")
        return False
    else:
        print(f"[錯誤] 下載失敗，HTTP {response.status_code}")
        print(f"回應內容：{response.text[:200]}")
        return False


def main():
    today = date.today()
    date_str = today.strftime("%Y-%m-%d")
    mmdd = today.strftime("%m%d")

    os.makedirs(REPORTS_DIR, exist_ok=True)

    # ── 步驟 1：取得憑證（自動刷新，無頭執行）──
    print(f"[{date_str}] 取得 Google 認證...")
    creds = get_credentials()
    print("認證成功")

    # ── 步驟 2：下載試算表 ──
    xlsx_path = os.path.join(PROJECT_ROOT, f"Market Watchlist{mmdd}.xlsx")
    print(f"下載試算表至 {xlsx_path}...")
    ok = download_xlsx(creds, SHEET_ID, xlsx_path)
    if not ok:
        sys.exit(1)
    print(f"下載完成（{os.path.getsize(xlsx_path) / 1024:.1f} KB）")

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
