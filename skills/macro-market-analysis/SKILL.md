---
name: macro-market-analysis
description: >
  總體經濟市場趨勢分析，模擬 30 年經驗資深投資人視角，解讀經濟數據、央行政策與跨資產資金流向，判斷市場週期位置與資產配置方向。整合 risk-radar 宏觀風險雷達子模組，支援月度/季度定期風險掃描。

  當使用者詢問以下問題時，請使用本 skill：市場現在適合投資嗎？現在是牛市還是熊市？Fed 升降息對市場的影響是什麼？CPI/通膨/GDP/PMI/非農就業數據怎麼解讀？資金正在流向哪些資產類別？股票債券現金如何配置？哪些產業值得現在佈局？需要地緣政治風險評估？需要月報或季報形式的宏觀風險掃描？支援完整數據指標總表（短期/中期/長期、領先/同步/落後），涵蓋流動性指標（TGA、RRP、M2、淨流動性公式）、週度就業數據、PMI 採購經理人指數等超過 80 項關鍵指標。Step 5 跨資產輪動分析直接讀取全市場觀察 Google 試算表（涵蓋全球股票/固定收益/商品/比特幣共 100+ ETF 的趨勢、相對強弱排名與輪動訊號）。
version: 2.4.0
author: Evan
license: Proprietary
tags:
  - macroeconomics
  - market-trends
  - economic-indicators
  - policy-analysis
  - investment-strategy
  - asset-allocation
  - fund-flow-tracking
  - risk-radar
  - liquidity-cycle
---

# 總體經濟市場趨勢分析（Macro Market Analysis）

## 概述

本技能模擬擁有超過 30 年實戰經驗的資深投資人角色，透過系統化解讀經濟數據、央行政策、地緣政治事件、產業發展週期與**跨資產資金流動追蹤**，協助掌握市場大方向，做出理性的資產配置與產業選擇決策。

### 核心理念

- 在空頭市場中，再好的股票也難逃下跌命運
- 在多頭市場中，選對產業比選對個股更重要
- **資產配置決定 80% 的報酬，選股只決定 20%**
- 理解經濟週期與資金流向，才能「該積極時積極，該保守時保守」

### 子模組：Risk Radar 宏觀風險雷達

整合 **risk-radar** 作為定期檢查子模組：
- **使用時機：** 月度/季度例行風險掃描，或重大事件後（FOMC、黑天鵝、信用事件）臨時啟動
- **核心框架：** 流動性週期 ＋ 壓力型去通膨 ＋ AI 資本支出週期
- **與常規分析的差異：** 常規分析回應即時問題；Risk Radar 是固定指標的週期性掃描，輸出結構化月報/季報
- **詳細執行邏輯：** 參考 `references/risk-radar-sop.md`

---

### 核心能力

1. **經濟數據深度解讀** — GDP、CPI/PPI/PCE、就業市場、PMI、殖利率曲線
2. **央行政策影響評估** — Fed 政策立場、利率路徑、QE/QT 傳導機制
3. **跨資產資金流追蹤** — ETF 資金流、CFTC COT 大戶持倉、機構評級、16 大資產類別溫度評分
4. **市場週期位置判斷** — 復甦/擴張/高峰/衰退，牛市/熊市/盤整
5. **產業趨勢與輪動策略** — 週期對應產業特性，輪動時機識別
6. **地緣政治風險評估** — 中美關係、貿易政策、能源供應風險
7. **歷史情境比較** — 相似歷史週期尋找、路徑推演、機率評估

---

## 適用場景

### 觸發關鍵詞

**經濟面：** 通膨、CPI、PPI、PCE、GDP、景氣、升息、降息、利率、Fed、就業、失業率、非農、衰退、軟著陸、硬著陸

**市場面：** 大盤走勢、S&P 500、加權指數、牛市、熊市、市場情緒、股債配置、資產配置

**資金流向：** 資金流、ETF 資金流、機構持倉、大戶動向、COT 報告、資產輪動、避險資產、風險資產

**產業面：** 產業趨勢、產業週期、半導體、AI、電動車、綠能、產業輪動、類股表現

**風險面：** 地緣政治、中美關係、黑天鵝、系統性風險

**風險雷達（子模組）：** 風險雷達、風險掃描、宏觀風險檢查、流動性週期、壓力型去通膨、去槓桿、月報更新、季報更新、定期檢查

### 不適用情境

- 單一公司深度分析 → 使用 `equity-fundamental-analysis`
- 具體技術進出場時機 → 使用 `technical-analysis`
- 產業層面深度研究 → 優先考慮 `industry-research`

---

## 執行流程

```
第一階段：總體經濟分析（三大支柱）
├── Step 1: 情境識別與分析範圍確定
├── Step 2: 資料蒐集與驗證
├── Step 3: 經濟數據深度解讀
├── Step 4: 央行政策環境評估
└── Step 5: 跨資產資金流追蹤分析 ⭐
     ↓
第二階段：市場研判
├── Step 6: 市場週期位置判斷
├── Step 7: 產業趨勢分析（如適用）
└── Step 8: 投資策略建議
     ↓
[若觸發 Risk Radar 關鍵詞]
└── Step 10: 宏觀風險雷達掃描（輸出月報/季報）
     ↓
Step 9: 產出報告
```

---

### Step 1: 情境識別與需求分析

識別問題類型，確定分析重點：

- **總經環境評估** → 需要完整經濟數據 + 資金流分析
- **特定指標解讀** → 聚焦該指標 + 相關連動指標
- **資產配置建議** → 優先執行資金流追蹤模組
- **產業趨勢分析** → 需要產業數據 + 總經背景
- **投資策略建議** → 需要完整分析鏈

確定分析範圍：
- **地理：** 全球 / 美國 / 中國 / 台灣 / 歐洲
- **時間：** 最新值 / 近 3 個月 / 近 1 年 / 近 5 年
- **關注重點：** 成長 / 通膨 / 就業 / 利率 / 資金流向

**1.3 分析檢查清單（按需勾選）**

```
□ 【經濟成長】GDP (Real GDP Growth, YoY/QoQ) / GDPNow 即時估計
□ 【通膨指標】CPI、Core CPI、PPI、PCE（物價）、Core PCE、通膨預期(T5YIE, T10YIE)
□ 【就業市場】Unemployment Rate、Nonfarm Payrolls、Wage Growth
□ 【週度就業】Initial Jobless Claims（初領）、Continuing Jobless Claims（續領）⭐ 每週四
□ 【消費動能】Real PCE Spending、Retail Sales（名目+實質）
□ 【利率環境】Fed Funds Rate、2Y/10Y/30Y Treasury Yield、殖利率曲線(10Y-2Y, 10Y-3M)、實質利率(TIPS)
□ 【信用利差】High Yield OAS、Investment Grade OAS
□ 【領先指標】Conference Board LEI、ISM 製造業 PMI、ISM 服務業 PMI、ISM 新訂單 ⭐
□ 【區域 PMI】費城聯儲製造業指數、紐約帝國州製造業指數、Chicago Fed CFNAI
□ 【消費信心】Conference Board Consumer Confidence、U of Michigan Consumer Sentiment
□ 【房市指標】Housing Starts、Building Permits、NAHB 指數、30Y 房貸利率
□ 【貨幣供給】M2 Money Supply (YoY) ⭐ 流動性核心
□ 【信貸狀況】Senior Loan Officer Survey (SLOOS)、C&I Loans、Consumer Credit、信用卡違約率
□ 【市場流動性】Fed Total Assets、TGA（財政部現金餘額）、RRP（逆回購餘額）、Bank Reserves ⭐
□ 【淨流動性】Net Liquidity = Fed Assets - TGA - RRP（自行計算）⭐
□ 【銀行間壓力】FRA-OIS Spread、TED Spread ⭐ 危機預警
□ 【市場估值】S&P 500 Forward P/E、Shiller CAPE、Equity Risk Premium (ERP)
□ 【市場情緒】VIX、Put/Call Ratio、AAII 散戶情緒、NAAIM 機構曝險度
□ 【資金流向】ETF Fund Flows、CFTC COT 大戶持倉、機構評級(OW/N/UW) ⭐
□ 【亞洲指標】中國製造業 PMI（官方+財新）、台灣出口訂單、南韓出口、USD/CNY
□ 【能源/商品】WTI/Brent 原油、天然氣、美國原油庫存（週三）、波羅的海乾散貨指數(BDI)
□ 【美元流動性】DXY 美元指數、SOFR、EFFR
□ 【政策動態】Fed Meeting Minutes、FOMC Statement、點陣圖利率路徑
□ 【產業數據】（根據關注產業而定，參考 industry-research 模組）
```

---

### Step 2: 資料蒐集與驗證

**首選官方來源：**
- FRED (fred.stlouisfed.org) — 聯準會經濟數據庫
- BLS / BEA — 美國勞工與經濟分析局
- 各國央行官網、統計局

**次選整合平台：**
- Trading Economics — 全球數據整合
- Investing.com — 經濟日曆

**資金流數據：**
- 🔗 **全市場觀察表（Google 試算表）** — 跨資產/板塊/類股即時趨勢與輪動（Step 5 主要工具）
  `https://docs.google.com/spreadsheets/d/1OMbg5nPRELu7cpkVrGR9CppMyUhjebpShk17n4wyhZA/edit?usp=sharing`
- ETFdb.com、Morningstar Fund Flows — ETF 資金流查詢（補充驗證）
- CFTC 官網 — COT 大戶持倉報告（每週五發布）
- PIMCO、JP Morgan、BlackRock 季度報告 — 機構資產配置評級

**閱讀內部參考文件（依需求載入）：**
- `references/economic-indicators.md` — 指標定義與解讀標準
- `references/fed-policy-framework.md` — Fed 政策決策邏輯
- `references/cross-asset-fund-flow.md` — 跨資產資金流完整 SOP
- `references/industry-cycles.md` — 產業景氣循環特性
- `references/historical-scenarios.md` — 歷史情境比對資料庫

---

### Step 3: 經濟數據深度解讀

對每項指標進行三維分析：
1. **絕對值** — 當前數值的歷史位置（高/中/低）
2. **趨勢** — 方向變化（改善/惡化/持平）
3. **超預期程度** — 相較市場共識的落差

跨指標交叉驗證：領先指標（PMI、LEI、消費者信心）→ 同步指標（GDP、工業生產）→ 落後指標（失業率）

詳細解讀框架請參考 `references/economic-indicators.md`

---

### Step 4: 央行政策環境評估

**Fed 三步驟分析：**
1. 確認當前政策立場（鴿派 / 中性 / 鷹派）
2. 評估未來利率路徑（升息 / 暫停 / 降息）
3. 分析政策傳導機制對各資產類別的影響

同步評估財政政策（預算赤字規模、政府支出方向）對市場流動性的疊加影響。

詳細框架請參考 `references/fed-policy-framework.md`

---

### Step 5: 跨資產資金流追蹤分析

**目標：** 觀察各類資產、板塊、類股的趨勢與輪動方向，識別資金正在流入/流出的資產類別。

---

#### 5.1 全市場觀察表（主要工具）⭐

**直接讀取以下 Google 試算表，取得即時全市場輪動數據：**

🔗 **全市場觀察表：** `https://docs.google.com/spreadsheets/d/1OMbg5nPRELu7cpkVrGR9CppMyUhjebpShk17n4wyhZA/edit?usp=sharing`

> 每次執行 Step 5 時，請直接透過上方連結讀取最新數據。

**表格涵蓋資產類別：**

| 類別 | 子類 | 主要 Ticker |
|------|------|------------|
| **股票** | 全球市場 | VT、ACWI、ACWX |
| | 美股市場 | VTI、SPY、QQQ |
| | 已開發市場 | EFA、EZU、EWJ、EWG、EWU 等 11 支 |
| | 新興市場 | EEM、EWT（台灣）、EWY（韓國）、EWZ（巴西）等 14 支 |
| | 中國市場 | MCHI、FXI、KWEB、ASHR |
| | 房地產 | REET、VNQI、VNQ、REM、MBB |
| | 高股息 | DVY、SCHD、IDV、AMLP、PFF |
| | 優先收益 | JEPI、JEPQ、QQQI、DIVO、QYLD 等 |
| **固定收益** | 廣泛市場 | BND、AGG、BNDX、TIP、VTIP |
| | 國債 | TLT（長債）、IEF（中債）、SHY（短債）、SGOV、BIL |
| | 公司債 | LQD、HYG、BINC、JAAA、JBBB |
| | 新興市場債 | EMB、EMHY |
| **商品** | — | GLD、SLV、USO、UNG、CPER、DBB、DBA、PDBC |
| **比特幣** | — | IBIT |

**欄位解讀指南：**

| 欄位 | 含義 | 解讀方式 |
|------|------|---------|
| `1D% / 5D%` | 短期價格動能 | 識別近期急漲/急跌 |
| `20D% / 60D%` | 中期價格動能 | 確認趨勢強度與持續性 |
| `60-Day Trend` | 60 日趨勢方向 | Up/Down/Flat |
| `20R / 60R / 120R` | 相對強弱排名（20/60/120 日）| 數字越小排名越前，資金偏好越高 |
| `Rank` | 綜合排名 | 整體資金吸引力排序 |
| `REL5/20/60/120` | 相對大盤表現 | 正值=跑贏市場，負值=跑輸市場 |
| `From 2025-12-31` | YTD 年初至今報酬 | 年度資金輪動全貌 |

**輪動判讀邏輯：**
- **Rank 前段 + 60D% 持續正 + 60-Day Trend = Up** → 資金持續流入，強勢資產
- **Rank 後段 + 60D% 持續負 + REL60 負值** → 資金流出，迴避
- **20R 突然大幅上升（排名躍升）+ 1D/5D% 明顯正** → 資金開始輪入，觀察是否持續
- **比較 EWT（台灣）vs EWY（韓國）vs QQQ** → 半導體/科技輪動方向

---

#### 5.2 深度驗證（可選）

若需進一步確認資金流方向，可補充以下四重驗證：

1. **ETF 資金流** — ETFdb.com 或 Morningstar 查詢近 1 週/1 月淨申購/贖回金額
2. **CFTC COT 大戶持倉** — 追蹤主要商品/指數期貨的大戶淨多單變化（每週五發布）
3. **機構評級** — PIMCO/JP Morgan/BlackRock 的 OW/N/UW 資產配置評級
4. **信用利差驗證** — HY OAS 收窄=風險偏好上升；擴大=避險情緒升溫

**四重驗證結論範例：**
```
全市場觀察表：TLT Rank 前段 + 60D% 正 + REL60 正（債券跑贏）
+ 債券 ETF 淨申購連續 2 週正值
+ COT 大戶增持公債期貨淨多單
+ 機構評級一致 Overweight 債券
= 四重確認 → 高信度看多債券
```

完整 SOP 請參考 `references/cross-asset-fund-flow.md`

---

### Step 6: 市場週期位置判斷

整合前述分析，綜合判斷：

1. **經濟週期階段：** 復甦 → 擴張 → 高峰 → 衰退
2. **市場情緒與估值：** S&P 500 P/E 歷史分位數、VIX 水準
3. **風險偏好：** Risk-On（進攻）vs Risk-Off（防禦）
4. **資金流驗證：** Step 5 資金流方向是否與週期判斷一致

若資金流與週期判斷不一致，降低倉位信心，等待信號趨於一致再行動。

---

### Step 7: 產業趨勢分析（如適用）

基於週期位置，識別受益產業板塊。

不同週期的產業偏好，詳見 `references/industry-cycles.md`。若需深度產業研究，啟動 `industry-research` 模組。

---

### Step 8: 投資策略建議

基於「經濟指標 + 央行政策 + 資金流分析 + 週期判斷」，輸出：

- **資產配置比例**（股票 / 債券 / 現金 / 黃金）
- **產業配置方向**（超配 / 標配 / 低配）
- **動態調整觸發條件**（何時改變配置的條件）

輸出範例：

```markdown
## 資產配置建議（YYYY-MM-DD）

| 資產類別 | 目標比例 | 調整幅度 | 理由 |
|---------|---------|---------|------|
| 股票    | 40%     | -20%    | 資金流確認避險情緒 |
| 債券    | 40%     | +15%    | 三重驗證顯示資金湧入 |
| 黃金    | 10%     | +5%     | 避險需求強勁 |
| 現金    | 10%     | 持平    | 保留流動性 |

### 動態調整觸發點
增加股票倉位至 60%（需滿足以下條件之一）：
- 股票 ETF 連續 2 週淨流入 > $5B
- COT 大戶淨多單連續 3 週增加
- 機構評級轉為 OW（3 家以上一致）
```

---

### Step 10: Risk Radar 宏觀風險雷達掃描（子模組）

**觸發條件（滿足任一即啟動）：**
- 使用者明確要求「風險雷達」「風險掃描」「月報/季報更新」
- 重大事件後臨時啟動（FOMC 意外決策、信用事件、黑天鵝）

**四大週期判斷（詳細執行參考 `references/risk-radar-sop.md`）：**

- **Step 10A：** 判斷「壓力型去通膨 vs 健康去通膨」（CPI + 實質零售銷售 + 信貸成長）
- **Step 10B：** 檢查「資產價格 vs 通膨預期背離」（T5YIE vs S&P 500）
- **Step 10C：** 定位「流動性週期」（修復期 / 擴張期 / 擴張末期 / 去槓桿期）
- **Step 10D：** AI/半導體資本週期交叉驗證（Capex 指引 vs 營收成長）

**標準輸出格式（月報/季報）：**

```markdown
## 宏觀風險雷達更新（YYYY-QY）

### 1. 總體與流動性摘要（5-10 行）
### 2. 風險雷達表（8-12 個關鍵指標 + 🟢🟡🔴 燈號）
### 3. 週期判斷（修復/早期擴張/擴張末期/去槓桿）
### 4. 資產配置與產業權重指引
### 5. 風險提示（未來 3-12 個月關鍵觸發點）
```

> Risk Radar 不提供個股建議，僅提供資產類別/產業層級的方向指引。

---

### Step 9: 產出報告

選擇報告格式：
- **每日快評** — 單一事件即時解讀（1-2 頁）
- **週度報告** — 整合資金流週報
- **月度深度** — 完整分析鏈
- **季度策略** — 中期資產配置方向

標準報告結構請參考 `references/analysis-report-template.md`

---

## 數據調用指南

完整 80+ 項指標的定義、時效性與數據來源，請載入：
`references/economic-indicators-reference.md`

以下依分析目的列出應優先調用的指標群組：

### 快速市場方向掃描（5 分鐘）
調用：VIX、10Y 殖利率 + 實質利率（TIPS）、淨流動性（Fed Assets - TGA - RRP）、FRA-OIS / TED Spread（危機預警）

### 通膨與 Fed 政策分析
調用：CPI + Core CPI + PCE + **Core PCE**（Fed 偏好）、T5YIE 通膨預期、密西根通膨預期、PPI（領先通膨 1-2 個月）、TIPS 實質利率

### 就業市場健康度
調用：**初領 + 續領失業救濟金**（每週四，高頻領先）、非農就業 + 失業率（月度同步）、JOLTS 職位空缺 + 離職率（領先景氣轉折）、薪資成長（工資通膨傳導）

### 景氣循環位置判斷
調用：Conference Board LEI、**ISM 製造業 + 服務業 PMI**（新訂單子指標最重要）、GDPNow 即時估計（Atlanta Fed）、CFNAI（芝加哥聯儲活動指數）

### 流動性環境與資金條件 ⭐
調用：**M2 (YoY)**、**TGA + RRP → 計算淨流動性**、Fed 資產負債表規模（QT 追蹤）、SLOOS 銀行放貸標準、C&I 貸款成長、HY OAS + IG OAS（信用利差）

### 信用壓力與系統風險預警
調用：**FRA-OIS Spread + TED Spread**（銀行間壓力，危機早期信號）、HY OAS 高收益債利差、信用卡違約率、商業地產空置率

### 資產配置方向
調用：殖利率曲線（10Y-2Y 倒掛程度）、S&P 500 Forward P/E + Shiller CAPE + ERP、AAII 散戶情緒 + NAAIM 機構曝險度、ETF 資金流 + CFTC COT 大戶持倉

### 亞洲 / 台灣聚焦
調用：**台灣出口訂單**（領先半導體景氣 1-2 個月）、**南韓出口**（領先全球貿易）、中國官方 + 財新 PMI、USD/CNY 離岸匯率

### 能源 / 商品通膨風險
調用：WTI / Brent 原油 + **美國原油庫存**（每週三 EIA）、銅價（景氣溫度計）、BDI 波羅的海乾散貨指數

---

## 參考資料

**核心框架（必讀）：**
- `references/interpretation-framework.md` — 數據解讀與決策框架（核心方法論）
- `references/analysis-report-template.md` — 標準化報告範本
- `references/cross-asset-fund-flow.md` — 跨資產資金流追蹤完整 SOP
- `references/risk-radar-sop.md` — Risk Radar 宏觀風險雷達掃描 SOP

**數據與指標：**
- `references/economic-indicators-reference.md` — **完整數據指標總表**（10 大類、80+ 指標，含時效性/領先落後屬性）⭐
- `references/data-sources.md` — 權威數據來源指引
- `references/economic-indicators.md` — 經濟指標定義與解讀標準
- `references/fed-policy-framework.md` — Fed 政策決策邏輯與解讀框架

**產業與風險：**
- `references/industry-cycles.md` — 各產業景氣循環特性與輪動策略
- `references/geopolitical-risks.md` — 地緣政治風險評估清單
- `references/historical-scenarios.md` — 歷史情境資料庫與類比分析

**實用工具：**
- 🔗 **全市場觀察表** — `https://docs.google.com/spreadsheets/d/1OMbg5nPRELu7cpkVrGR9CppMyUhjebpShk17n4wyhZA/edit?usp=sharing`（Step 5 跨資產輪動主要工具）
- `assets/investment-decision-checklist.md` — 投資決策檢查清單
- `assets/2025_macro-economics-guide.pdf` — 總體經濟分析實戰指引

---

## 版本歷史

### v2.4.0 (2026-03-18) ⭐ NEW

**重大更新：**
- ✅ Step 5 整合「全市場觀察表」Google 試算表作為跨資產輪動主要工具
- ✅ 新增欄位解讀指南（Rank、REL、60-Day Trend、20R/60R/120R）
- ✅ Step 5 重構為 5.1 主工具（直接讀表）+ 5.2 深度驗證（補充四重確認）
- ✅ Step 2 資金流數據來源新增試算表連結
- ✅ 參考資料新增全市場觀察表入口

### v2.3.0 (2026-03-18)

**重大更新：**
- ✅ 新增「完整數據指標總表」章節（10 大類、80+ 指標）
- ✅ 所有指標標註時效性（短期/中期/長期）與領先/同步/落後屬性
- ✅ 新增初領/續領失業救濟金（Initial / Continuing Jobless Claims）
- ✅ 新增 ISM 製造業 / 服務業 PMI 明確條目
- ✅ 新增 M2 貨幣供給量（流動性核心指標）
- ✅ 新增「流動性指標」獨立章節：TGA、RRP、Bank Reserves、SOFR、EFFR
- ✅ 新增美元淨流動性公式（Fed Assets - TGA - RRP）
- ✅ 新增 FRA-OIS Spread、TED Spread（金融壓力預警）
- ✅ 新增人民幣匯率追蹤（USD/CNY 離岸 CNH）
- ✅ 新增 PCE 消費支出量（與 PCE 物價分開列示）
- ✅ 新增 GDPNow 即時估計（Atlanta Fed）
- ✅ 新增房市指標（Housing Starts, NAHB, Case-Shiller, 房貸利率）
- ✅ 更新 Step 1.3 分析檢查清單為完整版（24 項）
- ✅ 建立「快速執行節奏建議」（每日/每週/每月/每季）

### v2.2.0 (2026-02-19)

**重大更新：**
- ✅ 整合 `risk-radar` 作為本模組的子模組（Step 10）
- ✅ 新增觸發關鍵詞：風險雷達、流動性週期、壓力型去通膨、月報/季報
- ✅ 建立四大週期判斷邏輯（Step 10A-D）
- ✅ 新增 Risk Radar 月報/季報標準輸出格式

### v2.1.0 (2026-01-18)

**重大更新：**
- ✅ 新增「跨資產資金流追蹤分析」模組（Step 5）
- ✅ 整合 ETF 資金流 + CFTC COT + 機構評級三重驗證機制
- ✅ 新增 16 大資產類別追蹤體系
- ✅ 建立資金溫度評分系統（-2 ~ +2）
