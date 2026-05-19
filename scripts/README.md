# scripts/ 使用說明

## generate_charts.py — 每日技術線圖生成器

### 功能
自動下載市場數據，生成暗色主題技術線圖（TradingView 風格），包含：
- K 線圖 + 成交量
- EMA 10（黃）/ EMA 50（藍）/ EMA 200 牛熊線（橘紅）
- MACD 指標（含直方圖）
- 趨勢階段自動標注：創新高 / 高點震盪 / 震盪 / 測試牛熊線

### 觀察清單
| 群組 | 標的 |
|------|------|
| 國際股市 | TAIEX、NI225、HSI、KOSPI、SXXP |
| 美國股市 | DJI、NDX、SPX、RUT、SOX |
| AI龍頭 | NVDA、AVGO、TSM、MRVL、UFO |
| 加密黃金 | BTC、GOLD |

### 安裝依賴
```bash
# 首次設定（建立虛擬環境）
python3 -m venv scripts/.venv
scripts/.venv/bin/pip install yfinance mplfinance matplotlib pandas numpy
```

### 執行方式
```bash
# 生成今日所有圖表
scripts/.venv/bin/python scripts/generate_charts.py

# 指定日期
scripts/.venv/bin/python scripts/generate_charts.py --date 2026-05-19

# 只生成特定群組
scripts/.venv/bin/python scripts/generate_charts.py --group 美國股市
scripts/.venv/bin/python scripts/generate_charts.py --group AI龍頭

# 調整 K 線期間（預設 2y）
scripts/.venv/bin/python scripts/generate_charts.py --period 1y
```

### 輸出結構
```
reports/
  charts/
    YYYY-MM-DD/
      TAIEX.png        ← 各標的技術線圖
      NI225.png
      SPX.png
      NVDA.png
      BTC.png
      ...
      chart_embeds.md  ← 自動生成的 Markdown 嵌入片段
```

### 在日報中引用
```markdown
![NVDA](reports/charts/2026-05-19/NVDA.png)
```

或將 `chart_embeds.md` 的內容直接貼入日報對應區塊。

### Claude Code Routines 整合
在 Routine 執行日報前，先執行此腳本生成圖表：
```
scripts/.venv/bin/python scripts/generate_charts.py --date {today}
```
圖表生成後，日報 Markdown 引用對應路徑即可。

---

## fetch_macro_data.py — 總經數據抓取腳本

從 FRED API 獲取美國總體經濟指標（GDP、CPI、就業、利率等）。
詳見 `skills/macro-market-analysis/scripts/README.md`。
