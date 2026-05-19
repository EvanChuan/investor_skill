#!/bin/bash
# 每日市場日報 — 本機一鍵執行
# 用法：bash run_daily.sh
# 建議每日 15:00 後執行（亞股今日收盤 + 美股昨日收盤）

set -e
PROJ="$(cd "$(dirname "$0")" && pwd)"
VENV="$PROJ/scripts/.venv/bin/python"
DATE=$(date +%Y-%m-%d)

echo "=========================================="
echo " 每日市場日報 — $DATE"
echo "=========================================="

# ── venv 檢查 ──────────────────────────────────
if [ ! -f "$VENV" ]; then
  echo ""
  echo "[錯誤] 找不到 scripts/.venv，請先初始化環境："
  echo "  cd $PROJ/scripts"
  echo "  python3 -m venv .venv"
  echo "  .venv/bin/pip install yfinance mplfinance matplotlib pandas numpy \\"
  echo "    openpyxl google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client"
  exit 1
fi

cd "$PROJ"

# ── 步驟 1｜Watchlist ──────────────────────────
echo ""
echo "步驟 1｜下載 Watchlist（Google Sheets）..."
python3 scripts/download_watchlist.py

# ── 步驟 2｜技術線圖 ───────────────────────────
echo ""
echo "步驟 2｜生成技術線圖（19 張）..."
"$VENV" scripts/generate_charts.py

# ── 步驟 3｜整合日報 ───────────────────────────
echo ""
echo "步驟 3｜建構預填日報..."
"$VENV" scripts/build_daily_report.py

echo ""
echo "=========================================="
echo " 完成！預填日報位置："
echo " reports/${DATE}_daily_market_report.md"
echo ""
echo " 下一步：開啟 VS Code，對 Claude Code 說："
echo " 「幫我補齊今天的日報」"
echo "=========================================="
