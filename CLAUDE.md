# CLAUDE.md — 每日市場日報 Routine 指令核心

本文件定義 Claude Code Routines 每次執行的自動化範圍與 SOP。

---

## 自動化範圍說明

Claude Code Routines 只負責以下三個可自動搜尋的模組：

| 模組 | 對應日報區塊 | 執行方式 |
|------|-----------|---------|
| `macro-market-analysis` | 區塊一（國際股市）、區塊二（美股概況）、區塊六（總經/Fed/油價/殖利率） | 🤖 自動 |
| `industry-research`（市場資金流向） | 區塊三（強弱板塊排行）、區塊五（成交額前 40 名） | 🤖 自動 |
| `market-sentiment-tracking` | 區塊四（BTC/黃金/加密情緒）、區塊七（VIX/恐懼貪婪/期貨盤前） | 🤖 自動 |

以下區塊**不在自動化範圍**，由人工手動補充：

| 區塊 | 原因 |
|------|------|
| 個股基本面 / 技術分析 | 需人工判讀圖表趨勢、建倉條件 |
| 個股短線換算（盤前換單清單） | 需人工決策，不適合自動輸出 |
| 估值分析 / 風險管理 | 完全人工操作 |

---

## Routine 執行順序（三段式自動化）

每日 Routine 依序執行以下三步，再由 Routine 補充 WebSearch 數據：

```bash
# 步驟 1｜下載 Watchlist 試算表（Google Sheets → xlsx → watchlist.md）
python3 /home/evan/Desktop/investor_skill/scripts/download_watchlist.py

# 步驟 2｜生成技術線圖（yfinance → PNG，存入 reports/charts/YYYY-MM-DD/）
/home/evan/Desktop/investor_skill/scripts/.venv/bin/python \
  /home/evan/Desktop/investor_skill/scripts/generate_charts.py

# 步驟 3｜整合日報（yfinance 指數 + Watchlist Rank + 線圖路徑 → 預填日報）
/home/evan/Desktop/investor_skill/scripts/.venv/bin/python \
  /home/evan/Desktop/investor_skill/scripts/build_daily_report.py
```

步驟 3 完成後，Routine 讀取預填日報並用 WebSearch 補充以下欄位：
- 區塊五：美股成交額前 40 名
- 區塊七：VIX 波動率指數、CNN 恐懼貪婪指數、期貨盤前數據
- 區塊六：US10Y 實際殖利率、DXY 美元指數、WTI 現貨油價
- 近期重要總經事件

---

## 執行規則

- **輸出路徑：** `reports/YYYY-MM-DD_daily_market_report.md`
- **若 `reports/` 資料夾不存在，自動建立**
- 資料來源：Python 腳本（yfinance + Watchlist）＋ WebSearch 補充
- 語言：繁體中文
- **趨勢階段標注規則：**
  - `創新高（N）` — 突破前高，N = 連續第幾次
  - `高點震盪（N）` — 高點附近盤整
  - `震盪（N）` — 中段震盪，未突破
  - `測試牛熊線（N）` — 測試 EMA 200 分界
- 漲用 ↑，跌用 ↓

---

## 日報 Header

```markdown
# 每日市場日報 — YYYY-MM-DD

**產出時間：** YYYY-MM-DD（台灣時間）
**資料截止：** 美股 YYYY-MM-DD 收盤 ／ 亞股 YYYY-MM-DD 收盤
**自動化模組：** macro-market-analysis ｜ industry-research ｜ market-sentiment-tracking
```

---

## 🤖 區塊一｜國際股市概況

**對應模組：** `macro-market-analysis`
**搜尋目標：** TAIEX、NI225、HSI、KOSPI、SXXP 最新收盤

```markdown
## 一、MM/DD 國際股市概況（↑ 漲，↓ 跌）

### MM/DD 台灣加權指數（TAIEX）↑/↓ X.XX%
- 收盤：XX,XXX 點
- 趨勢階段：**高點震盪（N）**
- 簡評：[1-2 句趨勢判讀]

### MM/DD 日經平均指數（NI225）↑/↓ X.XX%
- 收盤：XX,XXX 點
- 趨勢階段：**高點震盪（N）**
- 簡評：

### MM/DD 香港恆生指數（HSI）↑/↓ X.XX%
- 收盤：XX,XXX 點
- 趨勢階段：**震盪（N）**
- 簡評：

### MM/DD 韓國綜合指數（KOSPI）↑/↓ X.XX%
- 收盤：X,XXX 點
- 趨勢階段：**高點震盪（N）**
- 簡評：

### MM/DD 歐洲 STOXX 600（SXXP）↑/↓ X.XX%
- 收盤：XXX 點
- 趨勢階段：**震盪（N）**
- 簡評：
```

---

## 🤖 區塊二｜美國股市概況

**對應模組：** `macro-market-analysis`
**搜尋目標：** DJI、NDX、SPX、RUT、SOX 最新收盤

```markdown
## 二、MM/DD 美國股市概況

### MM/DD 道瓊工業指數（DJI）↑/↓ X.XX%
- 收盤：XX,XXX 點
- 趨勢階段：**震盪（N）**（前次：高點震盪）
- 簡評：

### MM/DD 納斯達克 100 指數（NDX）↑/↓ X.XX%
- 收盤：XX,XXX 點
- 趨勢階段：**創新高（N）**
- 簡評：

### MM/DD 標普 500 指數（SPX）↑/↓ X.XX%
- 收盤：X,XXX 點
- 趨勢階段：**創新高（N）**
- 簡評：

### MM/DD 羅素 2000 指數（RUT）↑/↓ X.XX%
- 收盤：X,XXX 點
- 趨勢階段：**高點震盪（N）**
- 簡評：

### MM/DD 費城半導體指數（SOX）↑/↓ X.XX%
- 收盤：X,XXX 點
- 趨勢階段：**高點震盪（N）**
- 簡評：
```

---

## 🤖 區塊三｜美股強弱勢板塊

**對應模組：** `industry-research`（市場資金流向）
**搜尋目標：** 昨日各概念板塊漲跌排行、七巨頭個股收盤價

```markdown
## 三、MM/DD 美股強弱勢板塊（昨日收盤）

> **#概念板塊排行，關注哪個族群才是一直排在前面。**

#### 強勢板塊 Top 10（Industry Rank 排行）

| 排名 | 代號 | 板塊/名稱 | 價格 | 1D% | Rank |
|------|------|---------|------|-----|------|
| 1 | | | | | 🔥 |
| ... | | | | | |

#### 市值板塊 Rank 排行（XL 系列）

| 代號 | 名稱 | 1D% | Rank |
|------|------|-----|------|
| XLK | 科技 | | |
| XLE | 能源 | | |
| ... | | | |

---

> **#七巨頭（Magnificent 7）追蹤**
> 國際趨勢（題材）＋ 有客戶（需求）＋ 賣超好 ＋ 贏超多 ＝ 會持續上漲的股票。

| 個股 | 代號 | 收盤價 | 趨勢階段 |
|------|------|--------|---------|
| 蘋果 | AAPL | $XXX | |
| 微軟 | MSFT | $XXX | |
| 亞馬遜 | AMZN | $XXX | |
| Alphabet | GOOGL | $XXX | |
| Meta | META | $XXX | |
| 輝達 | NVDA | $XXX | |
| 特斯拉 | TSLA | $XXX | |
```

> ⚠️ 個股建倉條件（AI 硬體 ＋ 進交額排行 ＋ EMA200 ＋ MACD 綠柱）為**人工判讀**，不在自動輸出範圍。

---

## 🤖 區塊四｜黃金與加密貨幣

**對應模組：** `market-sentiment-tracking`
**搜尋目標：** BTC 現價、CMC 恐懼貪婪指數、BTC ETF 資金流（Farside）、黃金現價

```markdown
## 四、MM/DD 黃金、加密貨幣

> **#BTC：[本日趨勢描述]**

### 比特幣（BTC/USDT）
- 現價：$XXX,XXX USD
- 24H 漲跌：↑/↓ X.XX%
- 趨勢階段：**測試牛熊線（N）/ 震盪（N）**

### CMC Crypto 恐懼與貪婪指數
| 今日 | 昨日 | 上週 | 上月 |
|------|------|------|------|
| **XX（中立 / 貪婪 / 恐懼）** | XX | XX | XX |

### BTC 現貨 ETF 資金流（Farside）
| 日期 | IBIT | FBTC | BITB | ARKB | 其他 | 合計 |
|------|------|------|------|------|------|------|
| MM/DD | | | | | | **+/-$XXXM** |
| MM/DD | | | | | | **+/-$XXXM** |
| MM/DD | | | | | | **+/-$XXXM** |
- 近一週累計：**+/-$X,XXXM**

---

> **#黃金：[本日趨勢描述]**

### 黃金（XAU/USD）
- 現價：$X,XXX USD/oz
- 24H 漲跌：↑/↓ X.XX%
- 趨勢階段：**第三隻腳（N）/ 高點震盪（N）**
- 簡評：三條 EMA 若持續糾纏，切勿頻繁進出，長線持股。
```

---

## 🤖 區塊五｜美股成交額前 40 名排行

**對應模組：** `industry-research`（市場資金流向）
**搜尋目標：** 昨日美股成交額前 40 名（Finviz / Barchart Most Active）

```markdown
## 五、美股成交額前四十名排行

> **#觀察哪些公司持續在前段班，符合策略才建倉（後半是 AI 硬體公司）。**

目前市場最強的四大族群（AI 晶片、記憶體、光通訊、加密貨幣）。
如果平常不會進來排行榜，但這幾天突然出現的，都視為短線，同時觀察有沒有整個族群都上榜。

| 排名 | 代號 | 公司名稱 | 最新成交（萬） | 漲跌 | 漲跌% | 成交量（億）|
|------|------|---------|-------------|------|-------|-----------|
| 1 | NVDA | 輝達 | | | | |
| 2 | SPY | 標普 500 ETF | | | | |
| 3 | | | | | | |
| ... | | | | | | |
| 40 | | | | | | |

**榜單觀察：**
- 持續上榜 AI 硬體族群：[代號列表]
- 今日異常進榜（短線注意）：[代號＋原因]
```

---

## 🤖 區塊六｜市場資訊 / 總經議題

**對應模組：** `macro-market-analysis`
**搜尋目標：** US10Y 殖利率、WTI 油價、DXY、Fed 最新動態、重要經濟事件

```markdown
## 六、市場資訊 / 總經議題

> **#市場資訊：[本週最重要總經標題]**

### 美國 10 年期公債殖利率（US10Y）
- 現值：X.XX%（↑/↓）
- 關鍵水位：4.5%（超過代表財政壓力）
- 解讀：[2-3 句影響分析]

### WTI 國際原油
- 現價：$XXX/桶（↑/↓）
- 趨勢階段：**震盪（N）**
- 關鍵水位：$60-70 正常；$100 以上地緣風險溢價偏高

### DXY 美元指數
- 現值：XXX（↑/↓）
- 解讀：[強弱分析對股市影響]

### 近期重要事件
| 日期 | 事件 | 重要程度 | 預期/前值 |
|------|------|---------|---------|
| | FOMC 會議紀要 | ⭐⭐⭐ | |
| | CPI / PCE | ⭐⭐⭐ | |
| | 非農就業 | ⭐⭐⭐ | |
| | NVDA 財報 | ⭐⭐⭐ | |

---

> **#（宣告）市場資訊：[深度產業主題]**

[本週 AI 基建 / 能源 / 地緣政治等深度主題整理，2-4 段文字]
```

---

## 🤖 區塊七｜美股盤前與關注機會

**對應模組：** `market-sentiment-tracking`
**搜尋目標：** CNN 恐懼貪婪指數、VIX、期貨盤前（NQ1/ES1/YM1/RTY1）

```markdown
## 七、MM/DD 美股盤前與關注機會

> **#美股情緒指數 XX（[極度恐懼/恐懼/中立/貪婪/極度貪婪]）。**

### CNN 恐懼貪婪指數
| 今日 | 昨日 | 上週 | 上月 |
|------|------|------|------|
| **XX（貪婪）** | XX | XX | XX |

---

> **#.VIX 波動率指數 XX（[過股情緒稍降溫 / 恐慌升溫]）。**

### CBOE VIX
- 現值：**XX**
- 解讀：< 15 市場平靜｜15-25 正常波動｜> 25 恐慌

---

> **#美股期貨指數盤前（大於 1% 波動為盤前高不確定性警示）。**

### 期貨指數盤前
| 商品 | 代號 | 最新價 | 漲跌 | 漲跌% |
|------|------|--------|------|-------|
| 道瓊期貨 | YM1 | | | |
| 納指期貨 | NQ1 | | | |
| 標普期貨 | ES1 | | | |
| 羅素期貨 | RTY1 | | | |
| 日經期貨 | NKD1 | | | |
| 恆生期貨 | HSI1 | | | |
```

> ⚠️ 盤前換單清單（個股短線換算）為**人工填寫**，Routine 不自動輸出。

---

## ✍️ 人工補充區塊（Routine 不執行）

以下欄位由人工在日報中手動補充：

```markdown
## 八、個股短線換算（人工）

> 符合建倉條件：AI 硬體 ＋ 進交額排行 ＋ EMA 200 線上 ＋ 日 MACD 綠柱 ＋ 過 MACD 綠線

| 代號 | 公司 | 觀察原因 | 趨勢階段 | 備註 |
|------|------|---------|---------|------|
| | | | | |

---

## 九、結語（人工）

[今日操作心得、市場觀察、投資紀律提醒]
```

---

## 資料來源對照

| 搜尋項目 | 建議來源 |
|---------|---------|
| 指數收盤 | Yahoo Finance、Investing.com |
| 板塊排行 | Finviz Heatmap、Barchart Sector |
| AI 個股 | Yahoo Finance、CNBC |
| BTC 價格 | CoinGecko |
| CMC 恐懼貪婪 | CoinMarketCap Fear & Greed |
| BTC ETF 流量 | Farside Investors、Coinglass |
| 黃金 | Investing.com XAU/USD |
| 成交額排行 | Finviz Most Active、Barchart |
| US10Y / WTI / DXY | CNBC、Investing.com |
| CNN 恐懼貪婪 | CNN Business Fear & Greed |
| VIX | CBOE、Yahoo Finance |
| 期貨盤前 | CME Group、CNBC Pre-Market |

---

## 關聯技能模組

- `skills/macro-market-analysis/SKILL.md` — 區塊一、二、六（v3.0.0：日報請走**日報模式** = Step 1 + Step 12 摘要，勿執行完整 Step 0-13）
- `skills/macro-market-analysis/references/cross-asset-price-rotation.md` — 價格輪動與相對強弱（Step 8A）
- `skills/macro-market-analysis/references/cross-asset-fund-flow.md` — 真實資金流輔助（Step 8B）
- `skills/industry-research/SKILL.md` — 區塊三、五
- `skills/market-sentiment-tracking/SKILL.md` — 區塊四、七
- `skills/FRAMEWORK.md` — 整體投資框架參考

---

*版本：v2.3.0 ｜ 更新：2026-05-19 ｜ 維護者：Evan*
*格式參考：Unlimited Capital 操盤日報*
