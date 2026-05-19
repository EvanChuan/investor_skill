#!/usr/bin/env python3
"""
每日技術線圖生成腳本 — Daily Technical Chart Generator

功能：
  1. 自動下載市場數據（via yfinance）
  2. 計算 EMA 10 / EMA 50 / EMA 200（牛熊線）與 MACD 指標
  3. 生成暗色主題技術線圖（TradingView 風格）
  4. 自動判斷趨勢階段：創新高 / 高點震盪 / 震盪 / 測試牛熊線
  5. 輸出至 reports/charts/YYYY-MM-DD/

使用方式：
  python scripts/generate_charts.py
  python scripts/generate_charts.py --date 2026-05-19
  python scripts/generate_charts.py --group 美國股市

依賴套件（使用 scripts/.venv）：
  scripts/.venv/bin/pip install yfinance mplfinance matplotlib pandas numpy
"""

import argparse
import sys
import warnings
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # 非互動模式，適合 Routine 無頭執行

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 設定中文字體（優先順序：Noto Sans CJK TC → AR PL UMing → fallback）
_CJK_CANDIDATES = [
    "Noto Sans CJK JP", "Noto Sans CJK SC", "Noto Serif CJK JP",
    "AR PL UMing CN", "AR PL UKai CN", "AR PL UMing TW MBE",
]
_available = {f.name for f in fm.fontManager.ttflist}
_cjk_font  = next((f for f in _CJK_CANDIDATES if f in _available), None)
if _cjk_font:
    matplotlib.rcParams["font.family"]        = _cjk_font
    matplotlib.rcParams["axes.unicode_minus"] = False

# FontProperties 物件，用於每個 text() 呼叫確保中文正確渲染
_FP_NORMAL = fm.FontProperties(family=_cjk_font) if _cjk_font else None
_FP_BOLD   = fm.FontProperties(family=_cjk_font, weight="bold") if _cjk_font else None
import matplotlib.patches as mpatches
import mplfinance as mpf
import numpy as np
import pandas as pd
import yfinance as yf

warnings.filterwarnings("ignore")

# ============================================================================
# 觀察清單設定
# ============================================================================

CHART_GROUPS = {
    "國際股市": [
        {"name": "TAIEX",  "ticker": "^TWII",    "display": "台灣加權指數（TAIEX）"},
        {"name": "NI225",  "ticker": "^N225",    "display": "日經平均指數（NI225）"},
        {"name": "HSI",    "ticker": "^HSI",     "display": "香港恆生指數（HSI）"},
        {"name": "KOSPI",  "ticker": "^KS11",    "display": "韓國綜合指數（KOSPI）"},
        {"name": "SXXP",   "ticker": "^STOXX50E","display": "歐洲 STOXX 50（SXXP）"},
    ],
    "美國股市": [
        {"name": "DJI",    "ticker": "^DJI",     "display": "道瓊工業指數（DJI）"},
        {"name": "NDX",    "ticker": "^NDX",     "display": "納斯達克 100（NDX）"},
        {"name": "SPX",    "ticker": "^GSPC",    "display": "標普 500（SPX）"},
        {"name": "RUT",    "ticker": "^RUT",     "display": "羅素 2000（RUT）"},
        {"name": "SOX",    "ticker": "^SOX",     "display": "費城半導體（SOX）"},
    ],
    "AI龍頭": [
        {"name": "NVDA",   "ticker": "NVDA",     "display": "輝達（NVDA）"},
        {"name": "AVGO",   "ticker": "AVGO",     "display": "博通（AVGO）"},
        {"name": "TSM",    "ticker": "TSM",      "display": "台積電 ADR（TSM）"},
        {"name": "MRVL",   "ticker": "MRVL",     "display": "邁威爾科技（MRVL）"},
        {"name": "UFO",    "ticker": "UFO",      "display": "太空衛星 ETF（UFO）"},
    ],
    "加密黃金": [
        {"name": "BTC",    "ticker": "BTC-USD",  "display": "比特幣（BTC/USD）"},
        {"name": "GOLD",   "ticker": "GC=F",     "display": "黃金期貨（GOLD）"},
    ],
}

ALL_GROUPS = list(CHART_GROUPS.keys())

# ============================================================================
# EMA / MACD 計算
# ============================================================================

def calc_ema(series: pd.Series, period: int) -> pd.Series:
    return series.ewm(span=period, adjust=False).mean()

def calc_macd(close: pd.Series, fast=12, slow=26, signal=9):
    macd_line   = calc_ema(close, fast) - calc_ema(close, slow)
    signal_line = calc_ema(macd_line, signal)
    histogram   = macd_line - signal_line
    return macd_line, signal_line, histogram

# ============================================================================
# 趨勢階段自動判斷
# ============================================================================

def detect_trend_stage(df: pd.DataFrame, ema200: pd.Series) -> str:
    """
    回傳趨勢標籤：創新高 / 高點震盪 / 震盪 / 測試牛熊線
    判斷邏輯：
      - 創新高：收盤價突破過去 252 天（約 1 年）最高點
      - 測試牛熊線：收盤價在 EMA200 ±2% 以內
      - 高點震盪：收盤價在過去 60 天高點的 95% 以上
      - 震盪：其餘情況
    """
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

# ============================================================================
# TradingView 暗色主題
# ============================================================================

TV_STYLE = mpf.make_mpf_style(
    base_mpf_style="nightclouds",
    marketcolors=mpf.make_marketcolors(
        up="#26a69a", down="#ef5350",
        edge="inherit", wick="inherit",
        volume={"up": "#26a69a66", "down": "#ef535066"},
    ),
    facecolor="#131722",
    figcolor="#131722",
    gridstyle="--",
    gridcolor="#2a2e39",
    y_on_right=True,
    rc={
        "axes.labelcolor": "#d1d4dc",
        "xtick.color":     "#787b86",
        "ytick.color":     "#787b86",
        "axes.edgecolor":  "#2a2e39",
    },
)

EMA_COLORS = {
    "ema10":  "#ffeb3b",   # 黃：短期
    "ema50":  "#2196f3",   # 藍：中期
    "ema200": "#ff5722",   # 橘紅：牛熊線
}

TREND_COLORS = {
    "創新高":     "#26a69a",
    "高點震盪":   "#ffeb3b",
    "震盪":       "#90a4ae",
    "測試牛熊線": "#ef5350",
}

# ============================================================================
# 單張圖表生成
# ============================================================================

def generate_chart(ticker_info: dict, output_dir: Path, period: str = "1y") -> Path | None:
    name    = ticker_info["name"]
    ticker  = ticker_info["ticker"]
    display = ticker_info["display"]

    print(f"  [{name}] 下載數據中... ", end="", flush=True)
    try:
        df = yf.download(ticker, period=period, auto_adjust=True, progress=False)
        if df.empty or len(df) < 60:
            print("❌ 數據不足，跳過")
            return None
        # 統一欄位名稱（yfinance 1.x 可能回傳 MultiIndex）
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel(1)
        df = df[["Open", "High", "Low", "Close", "Volume"]].dropna()
    except Exception as e:
        print(f"❌ 下載失敗：{e}")
        return None

    # ── 計算指標 ────────────────────────────────────────────────────────────
    ema10  = calc_ema(df["Close"], 10)
    ema50  = calc_ema(df["Close"], 50)
    ema200 = calc_ema(df["Close"], 200)
    macd_line, signal_line, histogram = calc_macd(df["Close"])

    trend = detect_trend_stage(df, ema200)

    # MACD 直方圖顏色（綠漲紅跌）
    hist_colors = ["#26a69a" if v >= 0 else "#ef5350" for v in histogram]

    # ── 建立 addplots ────────────────────────────────────────────────────────
    addplots = [
        mpf.make_addplot(ema10,       panel=0, color=EMA_COLORS["ema10"],  width=1.0, linestyle="-"),
        mpf.make_addplot(ema50,       panel=0, color=EMA_COLORS["ema50"],  width=1.2, linestyle="-"),
        mpf.make_addplot(ema200,      panel=0, color=EMA_COLORS["ema200"], width=1.5, linestyle="-"),
        mpf.make_addplot(macd_line,   panel=2, color="#2196f3", width=1.0, ylabel="MACD"),
        mpf.make_addplot(signal_line, panel=2, color="#ff9800", width=1.0),
        mpf.make_addplot(histogram,   panel=2, type="bar", color=hist_colors, width=0.7),
    ]

    # ── 輸出路徑 ────────────────────────────────────────────────────────────
    output_path = output_dir / f"{name}.png"

    # ── 繪圖 ────────────────────────────────────────────────────────────────
    fig, axes = mpf.plot(
        df,
        type="candle",
        style=TV_STYLE,
        addplot=addplots,
        volume=True,
        panel_ratios=(4, 1, 2),
        figsize=(14, 9),
        title="",
        returnfig=True,
        tight_layout=False,
    )

    # ── 標題與趨勢標注 ───────────────────────────────────────────────────────
    trend_color = TREND_COLORS.get(trend, "#ffffff")
    close_price = df["Close"].iloc[-1]
    pct_change  = (df["Close"].iloc[-1] / df["Close"].iloc[-2] - 1) * 100
    chg_sign    = "+" if pct_change >= 0 else ""
    chg_color   = "#26a69a" if pct_change >= 0 else "#ef5350"

    # 主 K 線區 axes[0]
    ax_main = axes[0]
    ax_main.set_facecolor("#131722")

    # 左上：名稱（用 FontProperties 確保中文渲染）
    ax_main.text(
        0.01, 0.97, display,
        transform=ax_main.transAxes,
        color="#d1d4dc", fontsize=12,
        va="top", ha="left",
        fontproperties=_FP_BOLD,
    )
    # 左上次行：價格 + 漲跌幅（ASCII，不需要 CJK）
    ax_main.text(
        0.01, 0.90,
        f"{close_price:,.2f}  {chg_sign}{pct_change:.2f}%",
        transform=ax_main.transAxes,
        color=chg_color, fontsize=10,
        va="top", ha="left",
    )
    # 圖例：EMA
    legend_handles = [
        mpatches.Patch(color=EMA_COLORS["ema10"],  label="EMA 10"),
        mpatches.Patch(color=EMA_COLORS["ema50"],  label="EMA 50"),
        mpatches.Patch(color=EMA_COLORS["ema200"], label="EMA 200  牛熊線"),
    ]
    legend = ax_main.legend(
        handles=legend_handles, loc="upper left",
        bbox_to_anchor=(0.01, 0.85),
        framealpha=0.2, fontsize=8, labelcolor="#d1d4dc",
        facecolor="#131722",
    )
    if _FP_NORMAL:
        for text in legend.get_texts():
            text.set_fontproperties(_FP_NORMAL)

    fig.patch.set_facecolor("#131722")
    fig.savefig(output_path, dpi=150, bbox_inches="tight",
                facecolor="#131722", edgecolor="none")
    plt.close(fig)

    print(f"✅ {trend}")
    return output_path

# ============================================================================
# 主流程
# ============================================================================

def main():
    parser = argparse.ArgumentParser(description="每日技術線圖生成器")
    parser.add_argument("--date",  default=datetime.today().strftime("%Y-%m-%d"),
                        help="報告日期，格式 YYYY-MM-DD（預設今日）")
    parser.add_argument("--group", default="all",
                        choices=["all"] + ALL_GROUPS,
                        help="只生成指定群組的圖表")
    parser.add_argument("--period", default="1y",
                        help="K 線資料期間，如 1y / 2y / 6mo（預設 1y）")
    args = parser.parse_args()

    # ── 輸出目錄 ────────────────────────────────────────────────────────────
    repo_root  = Path(__file__).parent.parent
    output_dir = repo_root / "reports" / "charts" / args.date
    output_dir.mkdir(parents=True, exist_ok=True)

    target_groups = ALL_GROUPS if args.group == "all" else [args.group]

    # ── 生成圖表 ─────────────────────────────────────────────────────────────
    results = {}
    total, success = 0, 0

    for group in target_groups:
        print(f"\n📊 {group}")
        results[group] = []
        for item in CHART_GROUPS[group]:
            total += 1
            path = generate_chart(item, output_dir, period=args.period)
            if path:
                success += 1
                results[group].append({
                    "name":    item["name"],
                    "display": item["display"],
                    "path":    str(path.relative_to(repo_root)),
                })

    # ── 輸出 Markdown 嵌入片段 ───────────────────────────────────────────────
    md_snippet_path = output_dir / "chart_embeds.md"
    with open(md_snippet_path, "w", encoding="utf-8") as f:
        f.write(f"<!-- 技術線圖自動嵌入片段 — {args.date} -->\n\n")
        for group, charts in results.items():
            if not charts:
                continue
            f.write(f"### {group}\n\n")
            for c in charts:
                rel = c["path"].replace("\\", "/")
                f.write(f"#### {c['display']}\n")
                f.write(f"![{c['name']}]({rel})\n\n")

    # ── 統計 ────────────────────────────────────────────────────────────────
    print(f"\n{'─'*50}")
    print(f"✅ 完成：{success}/{total} 張圖表")
    print(f"📁 輸出目錄：{output_dir}")
    print(f"📝 嵌入片段：{md_snippet_path}")
    print(f"\n在日報中引用：")
    print(f"  ![]({output_dir.relative_to(repo_root)}/NVDA.png)")


if __name__ == "__main__":
    main()
