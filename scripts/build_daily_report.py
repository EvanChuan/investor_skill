#!/usr/bin/env python3
"""
build_daily_report.py — 每日市場日報自動建構器

整合三個本地資料來源，生成預填充日報：
  1. yfinance      → 指數收盤價 + 趨勢階段（與 generate_charts 共用邏輯）
  2. Watchlist xlsx → 板塊 Rank、ETF 強弱排行、商品/黃金/BTC ETF 數據
  3. reports/charts/ → 技術線圖（generate_charts.py 產出）

Routines 執行順序：
  Step 1: python3 scripts/download_watchlist.py     # 下載最新 watchlist
  Step 2: scripts/.venv/bin/python scripts/generate_charts.py  # 生成線圖
  Step 3: scripts/.venv/bin/python scripts/build_daily_report.py  # 整合日報

Routine 最後補充 WebSearch 數據（VIX、CNN 恐懼貪婪、期貨盤前、成交額前40）

用法：
  scripts/.venv/bin/python scripts/build_daily_report.py
  scripts/.venv/bin/python scripts/build_daily_report.py --date 2026-05-19
"""

import argparse
import glob
import os
import re
import sys
import warnings
from datetime import date, datetime, timedelta
from pathlib import Path

warnings.filterwarnings("ignore")

import openpyxl
import pandas as pd
import yfinance as yf

PROJECT_ROOT   = Path(__file__).parent.parent
REPORTS_DIR    = PROJECT_ROOT / "reports"
CHARTS_BASE    = REPORTS_DIR / "charts"
WATCHLIST_DIR  = PROJECT_ROOT / "data" / "watchlist"

# ============================================================================
# 指數設定（yfinance）
# ============================================================================

INTL_INDICES = [
    {"name": "TAIEX",  "ticker": "^TWII",     "display": "台灣加權指數（TAIEX）"},
    {"name": "NI225",  "ticker": "^N225",     "display": "日經平均指數（NI225）"},
    {"name": "HSI",    "ticker": "^HSI",      "display": "香港恆生指數（HSI）"},
    {"name": "KOSPI",  "ticker": "^KS11",     "display": "韓國綜合指數（KOSPI）"},
    {"name": "SXXP",   "ticker": "^STOXX50E", "display": "歐洲 STOXX 50（SXXP）"},
]

US_INDICES = [
    {"name": "DJI",   "ticker": "^DJI",  "display": "道瓊工業指數（DJI）"},
    {"name": "NDX",   "ticker": "^NDX",  "display": "納斯達克 100（NDX）"},
    {"name": "SPX",   "ticker": "^GSPC", "display": "標普 500（SPX）"},
    {"name": "RUT",   "ticker": "^RUT",  "display": "羅素 2000（RUT）"},
    {"name": "SOX",   "ticker": "^SOX",  "display": "費城半導體（SOX）"},
]

# 七巨頭（Magnificent 7）追蹤
AI_TICKERS = [
    {"name": "AAPL",  "display": "蘋果（AAPL）"},
    {"name": "MSFT",  "display": "微軟（MSFT）"},
    {"name": "AMZN",  "display": "亞馬遜（AMZN）"},
    {"name": "GOOGL", "display": "Alphabet（GOOGL）"},
    {"name": "META",  "display": "Meta（META）"},
    {"name": "NVDA",  "display": "輝達（NVDA）"},
    {"name": "TSLA",  "display": "特斯拉（TSLA）"},
]

# ============================================================================
# yfinance 工具函數（與 generate_charts.py 共用邏輯）
# ============================================================================

def calc_ema(series, period):
    return series.ewm(span=period, adjust=False).mean()

def detect_trend(df, ema200):
    close    = df["Close"].iloc[-1]
    high_252 = df["High"].rolling(252, min_periods=1).max().iloc[-1]
    high_60  = df["High"].rolling(60,  min_periods=1).max().iloc[-1]
    ema200_v = ema200.iloc[-1]
    if close >= high_252 * 0.995:
        return "創新高"
    elif abs(close - ema200_v) / ema200_v <= 0.02:
        return "測試牛熊線"
    elif close >= high_60 * 0.94:
        return "高點震盪"
    else:
        return "震盪"

def get_index_data(ticker: str) -> dict | None:
    try:
        df = yf.download(ticker, period="2y", auto_adjust=True, progress=False)
        if df.empty or len(df) < 5:
            return None
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel(1)
        df = df[["Open", "High", "Low", "Close", "Volume"]].dropna()
        close   = df["Close"].iloc[-1]
        prev    = df["Close"].iloc[-2]
        pct     = (close / prev - 1) * 100
        ema200  = calc_ema(df["Close"], 200)
        trend   = detect_trend(df, ema200)
        return {
            "close": close,
            "pct":   pct,
            "trend": trend,
        }
    except Exception:
        return None

def get_stock_data(ticker: str) -> dict | None:
    return get_index_data(ticker)

# ============================================================================
# Watchlist Excel 解析（精簡版，專注取出 Rank 數據）
# ============================================================================

def find_watchlist_xlsx(target_date: date) -> Path | None:
    mmdd = target_date.strftime("%m%d")
    # 優先找 data/watchlist/，再 fallback 到舊的 PROJECT_ROOT
    patterns = [
        WATCHLIST_DIR / f"Market Watchlist{mmdd}.xlsx",
        WATCHLIST_DIR / f"Market Watchlist {mmdd}.xlsx",
        PROJECT_ROOT  / f"Market Watchlist{mmdd}.xlsx",
        PROJECT_ROOT  / f"Market Watchlist {mmdd}.xlsx",
    ]
    for p in patterns:
        if p.exists():
            return p
    # fallback: 最新的 xlsx（先找 data/watchlist/，再找 root）
    files = list(WATCHLIST_DIR.glob("Market Watchlist*.xlsx")) + \
            list(PROJECT_ROOT.glob("Market Watchlist*.xlsx"))
    if files:
        return max(files, key=lambda f: f.stat().st_mtime)
    return None

def _to_num(v):
    """字串數字轉 float；非數字原樣返回。"""
    if isinstance(v, (int, float)):
        return v
    if isinstance(v, str):
        try:
            return float(v.replace(",", "").replace("%", "").strip())
        except (ValueError, TypeError):
            pass
    return v


def parse_xlsx_sections(xlsx_path: Path, sheet_name: str) -> list[dict]:
    """解析指定工作表，回傳 sections 清單，每個 section 含 name + rows。"""
    try:
        wb = openpyxl.load_workbook(xlsx_path, data_only=True)
        ws = wb[sheet_name]
    except Exception:
        return []

    sections = []
    current  = None
    header   = False

    for row in ws.iter_rows(min_row=1, values_only=True):
        vals  = list(row)
        c_val = vals[2] if len(vals) > 2 else None
        d_val = vals[3] if len(vals) > 3 else None
        e_val = _to_num(vals[4]) if len(vals) > 4 else None

        if c_val == "Ticker":
            header = True
            continue
        if not header or c_val is None:
            continue

        # Section header
        if not isinstance(e_val, (int, float)):
            if d_val is None and c_val:
                current = {"name": str(c_val), "rows": []}
                sections.append(current)
            continue

        ticker = str(c_val).replace("BATS:", "").strip()
        price  = e_val
        d1     = _to_num(vals[5]) if len(vals) > 5 else None

        # 尋找 Rank（最後一個有數值的欄位）
        rank = None
        for v in reversed(vals[6:14]):
            num_v = _to_num(v)
            if isinstance(num_v, (int, float)) and 0 <= num_v <= 100:
                rank = float(num_v)
                break

        if current is None:
            current = {"name": "其他", "rows": []}
            sections.append(current)

        current["rows"].append({
            "ticker": ticker,
            "name":   str(d_val) if d_val else "",
            "price":  price,
            "d1":     d1,
            "rank":   rank,
        })

    return sections

def get_watchlist_data(xlsx_path: Path) -> dict:
    """提取日報所需的關鍵 watchlist 數據。"""
    assets    = parse_xlsx_sections(xlsx_path, "Assets")
    structure = parse_xlsx_sections(xlsx_path, "Structure")
    industry  = parse_xlsx_sections(xlsx_path, "Industry")

    # 所有 rows 攤平，方便查找
    def flat(sections):
        out = {}
        for s in sections:
            for r in s["rows"]:
                out[r["ticker"]] = r
        return out

    all_assets    = flat(assets)
    all_structure = flat(structure)
    all_industry  = flat(industry)

    # 全體 Rank 排行（Industry）
    all_industry_rows = [r for s in industry for r in s["rows"] if r["rank"] is not None]
    top_by_rank = sorted(all_industry_rows, key=lambda x: x["rank"], reverse=True)

    # Market Cap Weighted Sectors（板塊輪動）
    sector_rows = []
    for s in structure:
        if "Sector" in s["name"] or "Market Cap" in s["name"]:
            sector_rows.extend(s["rows"])

    return {
        "assets":        all_assets,
        "structure":     all_structure,
        "industry":      all_industry,
        "top_by_rank":   top_by_rank,
        "sector_rows":   sector_rows,
    }

# ============================================================================
# 日期工具
# ============================================================================

def prev_trading_day(d: date) -> date:
    """回傳上一個交易日（跳過週末，不處理假日）。"""
    delta = 1
    prev = d - timedelta(days=delta)
    while prev.weekday() >= 5:  # 5=Saturday, 6=Sunday
        delta += 1
        prev = d - timedelta(days=delta)
    return prev

# ============================================================================
# 格式化工具
# ============================================================================

def fmt_pct(val, plus=True) -> str:
    if val is None:
        return "—"
    arrow = "↑" if val >= 0 else "↓"
    sign  = "+" if (val >= 0 and plus) else ""
    return f"{arrow} {sign}{val*100:.2f}%" if abs(val) < 1 else f"{arrow} {sign}{val:.2f}%"

def fmt_pct_raw(pct_float) -> str:
    """pct_float 已是百分比值（如 1.23）"""
    if pct_float is None:
        return "—"
    arrow = "↑" if pct_float >= 0 else "↓"
    sign  = "+" if pct_float >= 0 else ""
    return f"{arrow} {sign}{pct_float:.2f}%"

def rank_icon(rank) -> str:
    if rank is None:
        return ""
    if rank >= 80:
        return "🔥"
    if rank >= 60:
        return "↑"
    if rank >= 40:
        return "→"
    return "↓"

def chart_img(name: str, date_str: str) -> str:
    rel = f"charts/{date_str}/{name}.png"
    full = REPORTS_DIR / rel
    if full.exists():
        return f"![{name}]({rel})\n"
    return f"> ⚠️ 圖表未生成，請執行：`scripts/.venv/bin/python scripts/generate_charts.py --date {date_str}`\n"

# ============================================================================
# 日報建構
# ============================================================================

def build_report(target_date: date, xlsx_path: Path | None) -> str:
    date_str = target_date.strftime("%Y-%m-%d")
    mmdd     = target_date.strftime("%m/%d")  # 亞股：今日

    us_date     = prev_trading_day(target_date)
    us_date_str = us_date.strftime("%Y-%m-%d")
    us_mmdd     = us_date.strftime("%m/%d")   # 美股：昨日（前一交易日）

    print(f"\n📋 建構日報：{date_str}")

    # ── 取得 watchlist 數據 ───────────────────────────────────────────────────
    wl = None
    if xlsx_path:
        print(f"  讀取 Watchlist：{xlsx_path.name}")
        wl = get_watchlist_data(xlsx_path)
    else:
        print("  ⚠️ 找不到 Watchlist xlsx，板塊 Rank 數據將為空")

    lines = []

    # ── Header ───────────────────────────────────────────────────────────────
    lines += [
        f"# 每日市場日報 — {date_str}",
        f"",
        f"**產出時間：** {date_str}（台灣時間）",
        f"**資料截止：** 美股 {us_date_str} 收盤 ／ 亞股 {date_str} 收盤",
        f"**自動化模組：** macro-market-analysis ｜ industry-research ｜ market-sentiment-tracking",
        f"",
        f"---",
        f"",
    ]

    # ====================================================================
    # 區塊一：國際股市
    # ====================================================================
    print("  [1/7] 國際股市... ", end="", flush=True)
    lines += [f"## 一、{mmdd} 國際股市概況（↑ 漲，↓ 跌）", ""]

    for idx in INTL_INDICES:
        d = get_index_data(idx["ticker"])
        if d:
            chg_str  = fmt_pct_raw(d["pct"])
            lines += [
                f"### {mmdd} {idx['display']} {chg_str}",
                f"- 收盤：{d['close']:,.2f}",
                f"- 趨勢階段：**{d['trend']}**",
                "",
                chart_img(idx["name"], date_str),
            ]
        else:
            lines += [f"### {mmdd} {idx['display']}", "> 數據取得失敗，請手動補充", ""]

    # Watchlist 補充：區域 ETF Rank
    if wl:
        lines += ["### 區域 ETF 相對強弱（Watchlist Rank）", ""]
        region_map = [
            ("全球", ["VT", "ACWI"]),
            ("美國", ["SPY", "QQQ", "VTI"]),
            ("已開發市場", ["EFA", "EWJ", "EWG", "EWU"]),
            ("新興市場", ["EEM", "EMXC", "EWT", "EWY"]),
            ("中國", ["MCHI", "FXI", "KWEB", "ASHR"]),
        ]
        lines += ["| 地區 | 代號 | 價格 | 1D% | Rank |", "|------|------|------|-----|------|"]
        for region, tickers in region_map:
            for t in tickers:
                r = wl["assets"].get(t) or wl["structure"].get(t)
                if r and r["rank"] is not None:
                    d1 = fmt_pct(r["d1"])
                    lines.append(
                        f"| {region} | {t} | ${r['price']:.2f} | {d1} | "
                        f"{r['rank']:.1f} {rank_icon(r['rank'])} |"
                    )
    lines += ["", "---", ""]
    print("✅")

    # ====================================================================
    # 區塊二：美國股市
    # ====================================================================
    print("  [2/7] 美國股市... ", end="", flush=True)
    lines += [f"## 二、{us_mmdd} 美國股市概況（昨日收盤）", ""]

    for idx in US_INDICES:
        d = get_index_data(idx["ticker"])
        if d:
            chg_str = fmt_pct_raw(d["pct"])
            # Watchlist Rank 補充
            rank_str = ""
            if wl:
                r = wl["structure"].get(idx["name"]) or wl["assets"].get(
                    {"DJI": "DIA", "NDX": "QQQ", "SPX": "SPY", "RUT": "IWM", "SOX": "SOXX"}.get(idx["name"], "")
                )
                if r and r["rank"] is not None:
                    rank_str = f"（Watchlist Rank：{r['rank']:.1f} {rank_icon(r['rank'])}）"
            lines += [
                f"### {us_mmdd} {idx['display']} {chg_str}",
                f"- 收盤：{d['close']:,.2f} {rank_str}",
                f"- 趨勢階段：**{d['trend']}**",
                "",
                chart_img(idx["name"], date_str),
            ]
        else:
            lines += [f"### {us_mmdd} {idx['display']}", "> 數據取得失敗", ""]

    lines += ["---", ""]
    print("✅")

    # ====================================================================
    # 區塊三：強弱板塊 + AI 龍頭
    # ====================================================================
    print("  [3/7] 強弱板塊... ", end="", flush=True)
    lines += [f"## 三、{us_mmdd} 美股強弱勢板塊（昨日收盤）", ""]

    # 3-1 板塊強弱（Watchlist Industry Rank）
    lines += [
        "> **#概念板塊排行，關注哪個族群才是一直排在前面。**",
        "",
    ]
    if wl and wl["top_by_rank"]:
        top10 = wl["top_by_rank"][:10]
        lines += ["#### 強勢板塊 Top 10（Industry Rank 排行）", ""]
        lines += ["| 排名 | 代號 | 板塊/名稱 | 價格 | 1D% | Rank |",
                  "|------|------|---------|------|-----|------|"]
        for i, r in enumerate(top10, 1):
            d1 = fmt_pct(r["d1"])
            lines.append(
                f"| {i} | **{r['ticker']}** | {r['name'] or '—'} | "
                f"${r['price']:.2f} | {d1} | {r['rank']:.1f} 🔥 |"
            )
        lines.append("")

        # 市值板塊 XL 系列
        if wl["sector_rows"]:
            xl_rows = [r for r in wl["sector_rows"] if r["ticker"].startswith("X") and r["rank"] is not None]
            xl_sorted = sorted(xl_rows, key=lambda x: x["rank"], reverse=True)
            if xl_sorted:
                lines += ["#### 市值板塊 Rank 排行（XL 系列）", ""]
                lines += ["| 代號 | 名稱 | 1D% | Rank |", "|------|------|-----|------|"]
                for r in xl_sorted:
                    d1 = fmt_pct(r["d1"])
                    icon = rank_icon(r["rank"])
                    lines.append(f"| {r['ticker']} | {r['name']} | {d1} | {r['rank']:.1f} {icon} |")
                lines.append("")
    else:
        lines += ["> ⚠️ Watchlist 未載入，板塊排行請手動補充", ""]

    # 3-2 AI 龍頭
    lines += [
        "",
        "> **#七巨頭（Magnificent 7）追蹤**",
        "> 國際趨勢（題材）＋ 有客戶（需求）＋ 賣超好 ＋ 贏超多 ＝ 會持續上漲的股票。",
        "",
    ]
    for ai in AI_TICKERS:
        t = ai["name"]
        d = get_stock_data(t)
        # 嘗試從 watchlist 取 Rank
        rank_info = ""
        if wl:
            r = wl["industry"].get(t) or wl["assets"].get(t)
            if r and r["rank"] is not None:
                rank_info = f"｜Rank {r['rank']:.1f} {rank_icon(r['rank'])}"

        if d:
            chg_str = fmt_pct_raw(d["pct"])
            lines += [
                f"#### {ai['display']}",
                f"- 收盤：${d['close']:.2f}　{chg_str}　趨勢：**{d['trend']}** {rank_info}",
                "",
                chart_img(t, date_str),
            ]
        else:
            lines += [f"#### {ai['display']}", "> 數據取得失敗", ""]

    lines += ["---", ""]
    print("✅")

    # ====================================================================
    # 區塊四：黃金與加密貨幣
    # ====================================================================
    print("  [4/7] 黃金/加密... ", end="", flush=True)
    lines += [f"## 四、{mmdd} 黃金、加密貨幣", ""]

    # BTC（from watchlist IBIT + yfinance BTC-USD）
    lines += ["> **#BTC：[趨勢描述待 WebSearch 補充]**", ""]
    btc_d = get_stock_data("BTC-USD")
    if btc_d:
        lines += [
            "### 比特幣（BTC/USD）",
            f"- 現價：${btc_d['close']:,.2f} USD",
            f"- 24H 漲跌：{fmt_pct_raw(btc_d['pct'])}",
            f"- 趨勢階段：**{btc_d['trend']}**",
            "",
            chart_img("BTC", date_str),
        ]
    if wl:
        ibit = wl["assets"].get("IBIT")
        if ibit:
            lines += [
                "**IBIT（BTC 現貨 ETF）**",
                f"| 代號 | 價格 | 1D% | Rank |",
                f"|------|------|-----|------|",
                f"| IBIT | ${ibit['price']:.2f} | {fmt_pct(ibit['d1'])} | "
                f"{ibit['rank']:.1f} {rank_icon(ibit['rank'])} |" if ibit['rank'] else
                f"| IBIT | ${ibit['price']:.2f} | {fmt_pct(ibit['d1'])} | — |",
                "",
            ]

    lines += [
        "### CMC Crypto 恐懼與貪婪指數",
        "> ⚠️ 待 WebSearch 補充（來源：coinmarketcap.com 或 alternative.me）",
        "",
        "### BTC 現貨 ETF 資金流（Farside）",
        "> ⚠️ 待 WebSearch 補充（來源：coinglass.com/etf/bitcoin）",
        "",
    ]

    # 黃金（from watchlist GLD + yfinance GC=F）
    lines += ["> **#黃金：[趨勢描述待補充]**", ""]
    gold_d = get_stock_data("GC=F")
    if gold_d:
        lines += [
            "### 黃金（XAU/USD）",
            f"- 現價：${gold_d['close']:,.2f} USD/oz",
            f"- 24H 漲跌：{fmt_pct_raw(gold_d['pct'])}",
            f"- 趨勢階段：**{gold_d['trend']}**",
            "",
            chart_img("GOLD", date_str),
        ]
    if wl:
        gld = wl["assets"].get("GLD")
        if gld:
            lines += [
                "**GLD（黃金 ETF）Watchlist 數據**",
                f"| 代號 | 價格 | 1D% | Rank |",
                f"|------|------|-----|------|",
                f"| GLD | ${gld['price']:.2f} | {fmt_pct(gld['d1'])} | "
                f"{gld['rank']:.1f} {rank_icon(gld['rank'])} |" if gld['rank'] else
                f"| GLD | ${gld['price']:.2f} | {fmt_pct(gld['d1'])} | — |",
                "",
            ]

    lines += ["---", ""]
    print("✅")

    # ====================================================================
    # 區塊五：成交額前 40
    # ====================================================================
    lines += [
        f"## 五、美股成交額前四十名排行",
        "",
        "> **#觀察哪些公司持續在前段班，符合策略才建倉（後半是 AI 硬體公司）。**",
        "> ⚠️ 此區塊需 WebSearch 補充（建議搜尋：Barchart most active stocks 或 Finviz screener）",
        "",
        "| 排名 | 代號 | 公司名稱 | 成交額 | 漲跌% |",
        "|------|------|---------|--------|-------|",
        "| 1-40 | — | 待 WebSearch 補充 | — | — |",
        "",
        "---",
        "",
    ]

    # ====================================================================
    # 區塊六：總經議題
    # ====================================================================
    print("  [6/7] 總經議題... ", end="", flush=True)
    lines += [f"## 六、市場資訊 / 總經議題", ""]

    # 美債（from watchlist Treasury Bonds）
    if wl:
        tlt = wl["assets"].get("TLT")
        ief = wl["assets"].get("IEF")
        shy = wl["assets"].get("SHY")

        lines += [
            "> **#債券市場：殖利率環境判讀（美債 ETF 代理）**",
            "",
            "| 美債 ETF | 代號 | 價格 | 1D% | 5D% | Rank | 意義 |",
            "|---------|------|------|-----|-----|------|------|",
        ]
        bond_map = [
            (tlt, "TLT", "20Y+ 長期債（利率敏感）"),
            (ief, "IEF", "7-10Y 中期債"),
            (shy, "SHY", "1-3Y 短期債（Fed 政策代理）"),
        ]
        for r, code, desc in bond_map:
            if r:
                d1 = fmt_pct(r["d1"])
                rank = f"{r['rank']:.1f} {rank_icon(r['rank'])}" if r["rank"] else "—"
                lines.append(f"| {desc} | {code} | ${r['price']:.2f} | {d1} | — | {rank} | {desc} |")

        lines += [
            "",
            "**債券解讀：**",
            f"- TLT 趨勢：{'下跌（殖利率上升）' if tlt and tlt['d1'] and tlt['d1'] < 0 else '上漲（殖利率下降）' if tlt and tlt['d1'] and tlt['d1'] > 0 else '待確認'}",
            "- 具體殖利率數值（US10Y）：⚠️ 待 WebSearch 補充",
            "",
        ]

    # 原油（from watchlist USO + PDBC）
    if wl:
        uso  = wl["assets"].get("USO")
        pdbc = wl["assets"].get("PDBC")
        lines += [
            "> **#商品市場：原油 + 大宗商品**",
            "",
            "| 代號 | 名稱 | 價格 | 1D% | 20D% | Rank |",
            "|------|------|------|-----|------|------|",
        ]
        for r, code, desc in [(uso, "USO", "WTI 原油 ETF"), (pdbc, "PDBC", "大宗商品 ETF")]:
            if r:
                d1 = fmt_pct(r["d1"])
                rank = f"{r['rank']:.1f} {rank_icon(r['rank'])}" if r["rank"] else "—"
                lines.append(f"| {code} | {desc} | ${r['price']:.2f} | {d1} | — | {rank} |")
        lines += [
            "",
            "- WTI 原油現貨價格（USD/桶）：⚠️ 待 WebSearch 補充",
            "- DXY 美元指數：⚠️ 待 WebSearch 補充",
            "",
        ]

    lines += [
        "### 近期重要事件（⚠️ 待 WebSearch 補充）",
        "",
        "| 日期 | 事件 | 重要程度 | 預期/前值 |",
        "|------|------|---------|---------|",
        "| — | FOMC 會議紀要 | ⭐⭐⭐ | 待補充 |",
        "| — | CPI / PCE | ⭐⭐⭐ | 待補充 |",
        "| — | 非農就業 | ⭐⭐⭐ | 待補充 |",
        "",
        "---",
        "",
    ]
    print("✅")

    # ====================================================================
    # 區塊七：盤前（全部 WebSearch）
    # ====================================================================
    lines += [
        f"## 七、{mmdd} 美股盤前與關注機會",
        "",
        "> **#美股情緒指數（⚠️ 待 WebSearch 補充）**",
        "",
        "### CNN 恐懼貪婪指數",
        "| 今日 | 昨日 | 上週 | 上月 |",
        "|------|------|------|------|",
        "| ⚠️ 待補充 | — | — | — |",
        "",
        "> **#.VIX 波動率指數（⚠️ 待 WebSearch 補充）**",
        "",
        "### 期貨指數盤前（⚠️ 待 WebSearch 補充）",
        "| 商品 | 代號 | 最新價 | 漲跌% |",
        "|------|------|--------|-------|",
        "| 道瓊期貨 | YM1 | — | — |",
        "| 納指期貨 | NQ1 | — | — |",
        "| 標普期貨 | ES1 | — | — |",
        "| 羅素期貨 | RTY1 | — | — |",
        "",
        "---",
        "",
    ]

    # ====================================================================
    # 附錄：Watchlist 完整強弱總覽
    # ====================================================================
    if wl and wl["top_by_rank"]:
        lines += [
            "## 附錄｜Watchlist 強弱總覽（Industry Rank Top 15）",
            "",
            "| 排名 | 代號 | 板塊 | 價格 | 1D% | Rank |",
            "|------|------|------|------|-----|------|",
        ]
        for i, r in enumerate(wl["top_by_rank"][:15], 1):
            d1 = fmt_pct(r["d1"])
            lines.append(
                f"| {i} | **{r['ticker']}** | {r.get('_section', '—')} | "
                f"${r['price']:.2f} | {d1} | {r['rank']:.1f} {rank_icon(r['rank'])} |"
            )
        lines += ["", "---", ""]

    # Footer
    lines += [
        "*本報告由 build_daily_report.py 自動產出 ｜ investor_skill v1.3.0*",
        "*資料來源：yfinance（指數）｜ TheMarketMemo Watchlist（板塊 Rank）｜ 技術線圖（generate_charts.py）*",
        "*⚠️ 標示欄位需 Routine WebSearch 補充完成*",
        "*免責聲明：本報告僅供參考，不構成投資建議。*",
    ]

    return "\n".join(lines)

# ============================================================================
# 主程式
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="每日市場日報建構器")
    parser.add_argument("--date", default=date.today().strftime("%Y-%m-%d"),
                        help="報告日期 YYYY-MM-DD（預設今日）")
    args = parser.parse_args()

    target_date = datetime.strptime(args.date, "%Y-%m-%d").date()
    date_str    = target_date.strftime("%Y-%m-%d")

    # 找 watchlist xlsx
    xlsx_path = find_watchlist_xlsx(target_date)
    if xlsx_path:
        print(f"✅ Watchlist：{xlsx_path.name}")
    else:
        print("⚠️  找不到 Watchlist xlsx，板塊數據將跳過")

    # 建構日報
    report = build_report(target_date, xlsx_path)

    # 輸出
    REPORTS_DIR.mkdir(exist_ok=True)
    out_path = REPORTS_DIR / f"{date_str}_daily_market_report.md"
    out_path.write_text(report, encoding="utf-8")

    print(f"\n✅ 日報已產出：{out_path}")
    print(f"   ⚠️  請讓 Routine 補充 WebSearch 數據（VIX、CNN 恐懼貪婪、成交額前40、期貨盤前）")


if __name__ == "__main__":
    main()
