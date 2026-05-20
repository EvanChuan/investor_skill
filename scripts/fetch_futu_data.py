#!/usr/bin/env python3
"""
fetch_futu_data.py — 富途 OpenAPI 資料抓取模組

提供兩個核心功能供 build_daily_report.py 呼叫：
  1. get_sector_rank()    → 美股板塊類股漲跌排行（前 50）
  2. get_turnover_rank()  → 美股成交額排行（前 50）

前置需求：
  - 富途牛牛帳號（免費帳戶即可）
  - 本機需運行 OpenD Gateway（下載：https://openapi.futunn.com/futu-api-doc/intro/openD.html）
  - 安裝 SDK：pip install moomoo-api

用法（獨立測試）：
  python scripts/fetch_futu_data.py

整合方式：
  from scripts.fetch_futu_data import get_sector_rank, get_turnover_rank
  sector_df   = get_sector_rank(top_n=50)
  turnover_df = get_turnover_rank(top_n=50)
"""

import time
import sys
from datetime import date
from pathlib import Path
from typing import Optional

try:
    import moomoo as ft
    import pandas as pd
except ImportError:
    print("❌ 請先安裝 moomoo SDK：pip install moomoo-api")
    sys.exit(1)

# ============================================================================
# 設定
# ============================================================================

OPEND_HOST = "127.0.0.1"
OPEND_PORT = 11111

# S&P 500 成分股代碼（用於成交額排行掃描，無需掃全市場）
# 涵蓋高流動性大型股，確保排行榜前50基本不會遺漏
SP500_SAMPLE = [
    # Mega Cap 核心（一定入榜）
    "US.AAPL", "US.NVDA", "US.MSFT", "US.AMZN", "US.GOOGL",
    "US.GOOG", "US.META", "US.TSLA", "US.AVGO", "US.BRK-B",
    # 金融
    "US.JPM", "US.V", "US.MA", "US.BAC", "US.WFC", "US.GS",
    "US.MS", "US.C", "US.AXP", "US.BLK",
    # 科技/半導體
    "US.AMD", "US.INTC", "US.QCOM", "US.MU", "US.ARM",
    "US.AMAT", "US.LRCX", "US.KLAC", "US.MRVL", "US.ORCL",
    "US.CRM", "US.ADBE", "US.NOW", "US.PLTR", "US.SNOW",
    # 醫療/消費
    "US.LLY", "US.UNH", "US.JNJ", "US.ABBV", "US.MRK",
    "US.PFE", "US.AMGN", "US.TMO", "US.DHR", "US.ISRG",
    "US.WMT", "US.COST", "US.HD", "US.MCD", "US.NKE",
    "US.SBUX", "US.TGT", "US.LOW", "US.PG", "US.KO",
    "US.PEP", "US.PM", "US.MO", "US.CL", "US.MDLZ",
    # 能源/工業/通訊
    "US.XOM", "US.CVX", "US.COP", "US.SLB", "US.OXY",
    "US.GE", "US.CAT", "US.HON", "US.RTX", "US.LMT",
    "US.T", "US.VZ", "US.CMCSA", "US.DIS", "US.NFLX",
    "US.SPOT", "US.UBER", "US.LYFT", "US.DASH", "US.ABNB",
    # 高人氣/高波動（常入成交額榜）
    "US.MSTR", "US.GME", "US.AMC", "US.RIVN", "US.LCID",
    "US.SOFI", "US.HOOD", "US.COIN", "US.RIOT", "US.MARA",
    "US.SMCI", "US.DELL", "US.HPQ", "US.IBM", "US.CSCO",
    "US.NET", "US.DDOG", "US.CRWD", "US.ZS", "US.PANW",
    "US.GTLB", "US.TTD", "US.SHOP", "US.SE", "US.BIDU",
    "US.PDD", "US.JD", "US.BABA", "US.NIO", "US.XPEV",
    "US.LI", "US.BILI", "US.FUTU", "US.TIGR", "US.VALE",
    "US.TSM", "US.ASML", "US.SAP", "US.TM", "US.SONY",
    "US.SPY", "US.QQQ", "US.IWM", "US.TQQQ", "US.SQQQ",
    "US.UVXY", "US.VXX",
]

# ============================================================================
# 工具函數
# ============================================================================

def _fmt_turnover(val) -> str:
    """將成交額（USD）格式化為易讀字串。"""
    if val is None or (isinstance(val, float) and val != val):  # NaN check
        return "—"
    val = float(val)
    if val >= 1e9:
        return f"${val/1e9:.2f}B"
    elif val >= 1e6:
        return f"${val/1e6:.1f}M"
    else:
        return f"${val/1e3:.0f}K"


def _fmt_change(val) -> str:
    """格式化漲跌幅。"""
    if val is None or (isinstance(val, float) and val != val):
        return "—"
    val = float(val)
    arrow = "↑" if val >= 0 else "↓"
    sign  = "+" if val >= 0 else ""
    return f"{arrow} {sign}{val:.2f}%"


# ============================================================================
# 核心功能 1：板塊類股漲跌排行
# ============================================================================

def get_sector_rank(
    top_n: int = 50,
    host: str = OPEND_HOST,
    port: int = OPEND_PORT,
) -> Optional[pd.DataFrame]:
    """
    取得美股板塊漲跌排行，回傳 DataFrame。

    回傳欄位：
        plate_code   板塊代碼（如 US.BK1032）
        plate_name   板塊名稱（如 Semiconductors）
        change_rate  板塊整體漲跌幅（%），以板塊內股票平均值估算
        top_stock    板塊漲幅最大的標的代號
        top_stock_chg 板塊漲幅最大標的的漲跌幅（%）

    策略：
        富途 OpenAPI 無法直接取得「板塊指數」漲跌幅，
        因此改為取每個板塊內漲幅最大（Top1）的個股代表板塊強弱，
        並以 Top5 個股的平均漲跌幅估算板塊整體動能。
    """
    ctx = None
    try:
        ctx = ft.OpenQuoteContext(host=host, port=port)

        # Step 1：取得美股所有行業板塊清單
        ret, plates_df = ctx.get_plate_list(ft.Market.US, ft.Plate.INDUSTRY)
        if ret != ft.RET_OK:
            print(f"❌ get_plate_list 失敗：{plates_df}")
            return None

        print(f"  📊 掃描 {len(plates_df)} 個板塊中...")

        results = []
        for idx, row in plates_df.iterrows():
            plate_code = row["code"]
            plate_name = row["plate_name"]

            # Step 2：取板塊內股票（依漲跌幅降序，取前5）
            ret2, stock_df = ctx.get_plate_stock(
                plate_code,
                sort_field=ft.SortField.CHANGE_RATE,
                ascend=False,
            )
            if ret2 != ft.RET_OK or stock_df.empty:
                continue

            top5 = stock_df.head(5)
            avg_chg = top5["change_rate"].mean() if "change_rate" in top5.columns else None
            top1    = top5.iloc[0]

            results.append({
                "plate_code":    plate_code,
                "plate_name":    plate_name,
                "avg_change":    round(avg_chg, 2) if avg_chg is not None else None,
                "top_stock":     top1["code"].replace("US.", ""),
                "top_stock_name": top1.get("stock_name", ""),
                "top_stock_chg": round(top1["change_rate"], 2) if "change_rate" in top1 else None,
            })

            # 限流：每個板塊請求之間稍作停頓
            time.sleep(0.05)

        if not results:
            print("⚠️ 未取得任何板塊資料")
            return None

        df = pd.DataFrame(results)
        df = df.sort_values("avg_change", ascending=False).reset_index(drop=True)
        df.index += 1  # 排名從 1 開始

        return df.head(top_n)

    except Exception as e:
        print(f"❌ get_sector_rank 發生錯誤：{e}")
        return None
    finally:
        if ctx:
            ctx.close()


# ============================================================================
# 核心功能 2：成交額排行
# ============================================================================

def get_turnover_rank(
    top_n: int = 50,
    code_list: Optional[list] = None,
    host: str = OPEND_HOST,
    port: int = OPEND_PORT,
) -> Optional[pd.DataFrame]:
    """
    取得美股成交額排行，回傳 DataFrame。

    參數：
        top_n      回傳前 N 名（預設 50）
        code_list  自訂掃描標的清單（預設使用 SP500_SAMPLE）

    回傳欄位：
        rank        排名
        code        股票代號
        name        公司名稱
        cur_price   最新收盤價
        change_rate 漲跌幅（%）
        turnover    成交額（USD）
        turnover_fmt 成交額（格式化，如 $5.23B）
        volume      成交量
    """
    codes = code_list or SP500_SAMPLE
    ctx   = None
    try:
        ctx = ft.OpenQuoteContext(host=host, port=port)
        all_snaps = []

        print(f"  💰 掃描 {len(codes)} 支標的中（分批快照）...")

        # 每批最多 200 支，批次間隔 1 秒（保守限流）
        for i in range(0, len(codes), 200):
            batch = codes[i:i + 200]
            ret, snap_df = ctx.get_market_snapshot(batch)
            if ret == ft.RET_OK and not snap_df.empty:
                all_snaps.append(snap_df)
            elif ret != ft.RET_OK:
                print(f"  ⚠️ 第 {i//200+1} 批快照失敗：{snap_df}")
            time.sleep(1)

        if not all_snaps:
            print("❌ 無法取得任何快照資料")
            return None

        full_df = pd.concat(all_snaps, ignore_index=True)

        # 標準化欄位名稱（moomoo SDK 版本差異）
        col_map = {
            "stock_name": "name",
            "last_price": "cur_price",
        }
        full_df = full_df.rename(columns={k: v for k, v in col_map.items() if k in full_df.columns})

        # 過濾無效資料
        full_df = full_df[full_df["turnover"].notna() & (full_df["turnover"] > 0)]

        # 排序並取前 N 名
        result_df = (
            full_df[["code", "name", "cur_price", "change_rate", "turnover", "volume"]]
            .sort_values("turnover", ascending=False)
            .head(top_n)
            .reset_index(drop=True)
        )
        result_df.index += 1  # 排名從 1 開始
        result_df["rank"]         = result_df.index
        result_df["code"]         = result_df["code"].str.replace("US.", "", regex=False)
        result_df["turnover_fmt"] = result_df["turnover"].apply(_fmt_turnover)
        result_df["change_fmt"]   = result_df["change_rate"].apply(_fmt_change)

        return result_df

    except Exception as e:
        print(f"❌ get_turnover_rank 發生錯誤：{e}")
        return None
    finally:
        if ctx:
            ctx.close()


# ============================================================================
# Markdown 格式化輸出（供 build_daily_report.py 直接嵌入）
# ============================================================================

def format_sector_rank_md(df: pd.DataFrame, top_n: int = 20) -> str:
    """
    將板塊排行 DataFrame 轉為 Markdown 表格字串。
    回傳的字串可直接插入日報 Markdown。
    """
    if df is None or df.empty:
        return "> ⚠️ 富途 OpenAPI 板塊資料未能取得，請確認 OpenD 是否運行"

    lines = [
        "| 排名 | 板塊名稱 | 板塊均漲跌 | 最強個股 | 個股漲跌% |",
        "|------|---------|-----------|---------|----------|",
    ]
    for rank, row in df.head(top_n).iterrows():
        avg_chg = _fmt_change(row["avg_change"])
        top_chg = _fmt_change(row["top_stock_chg"])
        lines.append(
            f"| {rank} | {row['plate_name']} | {avg_chg} "
            f"| {row['top_stock']}（{row['top_stock_name']}） | {top_chg} |"
        )
    return "\n".join(lines)


def format_turnover_rank_md(df: pd.DataFrame, top_n: int = 50) -> str:
    """
    將成交額排行 DataFrame 轉為 Markdown 表格字串。
    回傳的字串可直接插入日報 Markdown。
    """
    if df is None or df.empty:
        return "> ⚠️ 富途 OpenAPI 成交額資料未能取得，請確認 OpenD 是否運行"

    lines = [
        "| 排名 | 代號 | 公司名稱 | 收盤價 | 漲跌% | 成交額 |",
        "|------|------|---------|--------|-------|--------|",
    ]
    for _, row in df.head(top_n).iterrows():
        price = f"${float(row['cur_price']):.2f}" if row["cur_price"] else "—"
        lines.append(
            f"| {row['rank']} | **{row['code']}** | {row['name']} "
            f"| {price} | {row['change_fmt']} | {row['turnover_fmt']} |"
        )
    return "\n".join(lines)


# ============================================================================
# 主程式（獨立測試）
# ============================================================================

if __name__ == "__main__":
    print("\n=====================================")
    print(" 富途 OpenAPI 資料抓取測試")
    print("=====================================")
    print(f" 日期：{date.today()}")
    print(f" OpenD：{OPEND_HOST}:{OPEND_PORT}")
    print("")

    # --- 測試成交額排行（僅掃 SP500_SAMPLE，速度快）---
    print("[1/2] 抓取成交額排行前 50...")
    turnover_df = get_turnover_rank(top_n=50)
    if turnover_df is not None:
        print(f"✅ 成交額排行取得 {len(turnover_df)} 筆")
        print(turnover_df[["rank", "code", "name", "turnover_fmt", "change_fmt"]].head(10).to_string())
    else:
        print("❌ 成交額排行抓取失敗")

    print("")

    # --- 測試板塊漲跌排行 ---
    print("[2/2] 抓取板塊漲跌排行前 20...")
    sector_df = get_sector_rank(top_n=20)
    if sector_df is not None:
        print(f"✅ 板塊排行取得 {len(sector_df)} 個板塊")
        print(sector_df[["plate_name", "avg_change", "top_stock", "top_stock_chg"]].to_string())
    else:
        print("❌ 板塊排行抓取失敗")

    print("\n✅ 測試完成")
