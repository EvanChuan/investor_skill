# investor_skill — 每日市場日報自動化系統

每日 15:00 後執行，自動整合國際股市、美股、板塊強弱、加密黃金、總經數據，產出完整 Markdown 日報。

---

## 每日操作（兩步完成）

### Step 1｜執行腳本（終端機，約 3–5 分鐘）

```bash
bash /home/evan/Desktop/investor_skill/run_daily.sh
```

自動依序完成：
- 下載 Google Sheets Watchlist（板塊 Rank 數據）
- 生成 19 張 TradingView 風格技術線圖
- 整合 yfinance 指數數據，產出預填日報

### Step 2｜補齊 WebSearch 數據（Claude Code，約 2 分鐘）

開啟 VS Code，對 Claude Code 說：

```
幫我補齊今天的日報
```

Claude Code 會搜尋並填入：
- 區塊四：BTC 現價、CMC 恐懼貪婪、BTC ETF 資金流
- 區塊五：美股成交額前 40 名
- 區塊六：US10Y 殖利率、WTI 油價、DXY、重要總經事件
- 區塊七：CNN 恐懼貪婪、VIX、期貨盤前（NQ1/ES1/YM1/RTY1）

---

## 首次設定

### 1. 初始化 Python 環境

```bash
cd /home/evan/Desktop/investor_skill/scripts
python3 -m venv .venv
.venv/bin/pip install yfinance mplfinance matplotlib pandas numpy \
  openpyxl google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 2. Google Sheets 認證（只需做一次）

```bash
python3 /home/evan/Desktop/investor_skill/scripts/google_auth.py
```

瀏覽器會開啟 Google 登入頁，授權後自動儲存 `config/token.json`。後續執行無需重複操作，token 過期時會自動刷新。

> ⚠️ `config/token.json` 與 `config/credentials.json` 已列入 `.gitignore`，不會上傳至 GitHub。

---

## 專案結構

```
investor_skill/
├── run_daily.sh                    # 每日一鍵執行腳本
├── CLAUDE.md                       # Claude Code 行為指令（日報 SOP）
│
├── scripts/                        # 自動化腳本
│   ├── download_watchlist.py       # Step 1：下載 Google Sheets Watchlist
│   ├── generate_charts.py          # Step 2：生成技術線圖（yfinance + mplfinance）
│   ├── build_daily_report.py       # Step 3：整合預填日報
│   ├── parse_watchlist.py          # 輔助：解析 xlsx 板塊數據
│   ├── google_auth.py              # Google OAuth2 認證（首次使用）
│   └── .venv/                      # Python 虛擬環境（本機）
│
├── config/                         # 憑證（不上傳 GitHub）
│   ├── credentials.json            # Google OAuth2 用戶端 ID
│   └── token.json                  # 自動更新的存取 token
│
├── data/
│   └── watchlist/                  # 每日下載的 Watchlist xlsx
│       └── Market WatchlistMMDD.xlsx
│
├── reports/                        # 日報輸出
│   ├── YYYY-MM-DD_daily_market_report.md   # 每日完整日報
│   ├── YYYY-MM-DD_watchlist.md             # Watchlist 解析摘要
│   └── charts/
│       └── YYYY-MM-DD/             # 技術線圖（19 張 PNG）
│           ├── TAIEX.png
│           ├── NDX.png
│           ├── NVDA.png
│           └── ...
│
└── skills/                         # 投資分析技能模組
    ├── FRAMEWORK.md                # 七階段投資框架總覽
    ├── macro-market-analysis/      # 總體經濟分析
    ├── industry-research/          # 產業研究與輪動
    ├── market-sentiment-tracking/  # 市場情緒追蹤
    ├── equity-fundamental-analysis/
    ├── valuation-analysis/
    ├── technical-analysis/
    └── risk-management/
```

---

## 日報區塊說明

| 區塊 | 內容 | 來源 |
|------|------|------|
| 一｜國際股市 | TAIEX / NI225 / HSI / KOSPI / SXXP | yfinance + 線圖 |
| 二｜美國股市 | DJI / NDX / SPX / RUT / SOX | yfinance + 線圖 |
| 三｜強弱板塊 | Industry Rank Top10 + XL 系列 + 七巨頭 | Watchlist + yfinance |
| 四｜加密黃金 | BTC / 黃金 + ETF 資金流 | yfinance + WebSearch |
| 五｜成交額排行 | 美股前 40 名 | WebSearch |
| 六｜總經議題 | US10Y / WTI / DXY / 重要事件 | Watchlist + WebSearch |
| 七｜盤前情緒 | CNN F&G / VIX / 期貨盤前 | WebSearch |

**自動填充（腳本）：** 區塊一、二、三、四部分、六部分
**WebSearch 補充（Claude Code）：** 區塊四 ETF 流量、五、六殖利率油價、七全部

---

## 技術線圖說明

- **資料期間：** 近 1 年（約 252 個交易日）
- **指標：** EMA 10（黃）/ EMA 50（藍）/ EMA 200（橘紅，牛熊線）+ MACD
- **趨勢判斷：** 創新高 / 高點震盪 / 震盪 / 測試牛熊線
- **風格：** TradingView 暗色主題

---

## Watchlist 資料來源

Google Sheets「TheMarketMemo」試算表，包含三個工作表：
- `Assets`：ETF、個股 Rank 數據
- `Structure`：市值板塊輪動（XL 系列）
- `Industry`：概念板塊 Rank 排行

---

*版本：v2.3.0 ｜ 維護者：Evan *
