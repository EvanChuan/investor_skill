#!/usr/bin/env python3
"""
fetch_futu_data.py — 富途 OpenAPI 資料抓取模組

提供兩個核心功能供 build_daily_report.py 呼叫：
  1. get_sector_rank()    → 美股板塊類股漲跌排行（前 20）
  2. get_turnover_rank()  → 美股成交額排行（前 50）

前置需求：
  - 富途牛牛帳號（免貪責帳戶即可）
  - 本機需運行 OpenD Gateway（下載：https://openapi.futunn.com/futu-api-doc/intro/openD.html）
  - 安裝 SDK：pip install moomoo-api

用法（獨立測試）：
  python scripts/fetch_futu_data.py
"""

import socket
import time
import sys
from datetime import date
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

# S&P 500 成分股 + 高波動個股（用於成交額排行掃描，無需掃全市場）
SP500_SAMPLE = [
    # Mega Cap 核心
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
# OpenD 連線前預檢（關鍵修復：避免偏等 30 秒）
# ============================================================================

def is_opend_running(host: str = OPEND_HOST, port: int = OPEND_PORT, timeout: float = 2.0) -> bool:
    """
    利用 socket 快速檢查 OpenD 是否在接受連線。
    在 moomoo SDK 嘗試連接之前先呼叫，2 秒內無回應則判定未啟動。
    """
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (ConnectionRefusedError, socket.timeout, OSError):
        return False


# ============================================================================
# 工具函數
# ============================================================================

def _fmt_turnover(val) -> str:
    """\u5c07\u6210\u4ea4\u984d\uff08USD\uff09\u683c\u5f0f\u5316\u70ba\u6613\u8b80\u5b57\u4e32\u3002"""
    if val is None or (isinstance(val, float) and val != val):
        return "—"
    val = float(val)
    if val >= 1e9:
        return f"${val/1e9:.2f}B"
    elif val >= 1e6:
        return f"${val/1e6:.1f}M"
    else:
        return f"${val/1e3:.0f}K"


def _fmt_change(val) -> str:
    """\u683c\u5f0f\u5316\u6f32\u8dcc\u5e45\u3002"""
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
    top_n: int = 20,
    host: str = OPEND_HOST,
    port: int = OPEND_PORT,
) -> Optional[pd.DataFrame]:
    """
    取得美股板塊漲跌排行。

    回傳欄位：
        plate_code     板塊代碼
        plate_name     板塊名稱
        avg_change     板塊前5強股平均漲跌幅（%）
        top_stock      最強個股代號
        top_stock_name 最強個股名稱
        top_stock_chg  最強個股漲跌幅（%）
    """
    # 預檢：OpenD 未啟動則立即回傳
    if not is_opend_running(host, port):
        print(f"  ⚠️  OpenD 未在 {host}:{port} 運行，跳過板塊排行")
        return None

    ctx = None
    try:
        ctx = ft.OpenQuoteContext(host=host, port=port)

        ret, plates_df = ctx.get_plate_list(ft.Market.US, ft.Plate.INDUSTRY)
        if ret != ft.RET_OK:
            print(f"  ❌ get_plate_list 失敗：{plates_df}")
            return None

        print(f"  📊 掃描 {len(plates_df)} 個板塊中...")
        results = []

        for _, row in plates_df.iterrows():
            ret2, stock_df = ctx.get_plate_stock(
                row["code"],
                sort_field=ft.SortField.CHANGE_RATE,
                ascend=False,
            )
            if ret2 != ft.RET_OK or stock_df.empty:
                continue

            top5    = stock_df.head(5)
            avg_chg = top5["change_rate"].mean() if "change_rate" in top5.columns else None
            top1    = top5.iloc[0]

            results.append({
                "plate_code":     row["code"],
                "plate_name":     row["plate_name"],
                "avg_change":     round(avg_chg, 2) if avg_chg is not None else None,
                "top_stock":      top1["code"].replace("US.", ""),
                "top_stock_name": top1.get("stock_name", ""),
                "top_stock_chg":  round(top1["change_rate"], 2) if "change_rate" in top1 else None,
            })
            time.sleep(0.05)  # 輕度限流

        if not results:
            print("  ⚠️ 未取得任何板塊資料")
            return None

        df = pd.DataFrame(results).sort_values("avg_change", ascending=False).reset_index(drop=True)
        df.index += 1
        return df.head(top_n)

    except Exception as e:
        print(f"  ❌ get_sector_rank 發生錯誤：{e}")
        return None
    finally:
        if ctx:
            try:
                ctx.close()
            except Exception:
                pass


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
    取得美股成交額排行。

    參數：
        top_n      回傳前 N 名（預設 50）
        code_list  自訂掃描標的清單（預設 SP500_SAMPLE）

    回傳欄位：
        rank, code, name, cur_price, change_rate,
        turnover, turnover_fmt, volume, change_fmt
    """
    # 預檢：OpenD 未啟動則立即回傳
    if not is_opend_running(host, port):
        print(f"  ⚠️  OpenD 未在 {host}:{port} 運行，跳過成交額排行")
        return None

    codes = code_list or SP500_SAMPLE
    ctx   = None
    try:
        ctx = ft.OpenQuoteContext(host=host, port=port)
        all_snaps = []

        print(f"  💰 掃描 {len(codes)} 支標的中（分批快照）...")

        for i in range(0, len(codes), 200):
            batch = codes[i:i + 200]
            ret, snap_df = ctx.get_market_snapshot(batch)
            if ret == ft.RET_OK and not snap_df.empty:
                all_snaps.append(snap_df)
            elif ret != ft.RET_OK:
                print(f"  ⚠️ 第 {i//200+1} 批快照失敗：{snap_df}")
            time.sleep(1)

        if not all_snaps:
            print("  ❌ 無法取得任何快照資料")
            return None

        full_df = pd.concat(all_snaps, ignore_index=True)

        # 標準化欄位名稱（SDK 版本差異適配）
        col_map = {"stock_name": "name", "last_price": "cur_price"}
        full_df = full_df.rename(columns={k: v for k, v in col_map.items() if k in full_df.columns})
        full_df = full_df[full_df["turnover"].notna() & (full_df["turnover"] > 0)]

        result_df = (
            full_df[["code", "name", "cur_price", "change_rate", "turnover", "volume"]]
            .sort_values("turnover", ascending=False)
            .head(top_n)
            .reset_index(drop=True)
        )
        result_df.index += 1
        result_df["rank"]         = result_df.index
        result_df["code"]         = result_df["code"].str.replace("US.", "", regex=False)
        result_df["turnover_fmt"] = result_df["turnover"].apply(_fmt_turnover)
        result_df["change_fmt"]   = result_df["change_rate"].apply(_fmt_change)

        return result_df

    except Exception as e:
        print(f"  ❌ get_turnover_rank 發生錯誤：{e}")
        return None
    finally:
        if ctx:
            try:
                ctx.close()
            except Exception:
                pass


# ============================================================================
# Markdown 格式化輸出
# ============================================================================

def format_sector_rank_md(df: pd.DataFrame, top_n: int = 20) -> str:
    """\u5c07\u677f\u584a\u6392\u884c DataFrame \u8f49\u70ba Markdown \u8868\u683c\u5b57\u4e32\u3002"""
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
    """\u5c07\u6210\u4ea4\u984d\u6392\u884c DataFrame \u8f49\u70ba Markdown \u8868\u683c\u5b57\u4e32\u3002"""
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

    # 先預檢
    if not is_opend_running():
        print("❌ OpenD 未在執行中！")
        print("")
        print("請先啟動 OpenD Gateway：")
        print("  1. 下載：https://openapi.futunn.com/futu-api-doc/intro/openD.html")
        print("  2. 登入富途牛牛帳號後啟動")
        print("  3. 確認 OpenD 監聽於 127.0.0.1:11111")
        print("  4. 重新執行此測試")
        sys.exit(1)

    print("✅ OpenD 連線檢查通過")
    print("")

    print("[1/2] 抓取成交額排行前 50...")
    turnover_df = get_turnover_rank(top_n=50)
    if turnover_df is not None:
        print(f"✅ 成交額排行取得 {len(turnover_df)} 筆")
        print(turnover_df[["rank", "code", "name", "turnover_fmt", "change_fmt"]].head(10).to_string())
    else:
        print("❌ 成交額排行抓取失敗")

    print("")

    print("[2/2] 抓取板塊漲跌排行前 20...")
    sector_df = get_sector_rank(top_n=20)
    if sector_df is not None:
        print(f"✅ 板塊排行取得 {len(sector_df)} 個板塊")
        print(sector_df[["plate_name", "avg_change", "top_stock", "top_stock_chg"]].to_string())
    else:
        print("❌ 板塊排行抓取失敗")

    print("\n✅ 測試完成")
