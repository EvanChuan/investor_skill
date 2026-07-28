---
name: macro-market-analysis
description: >
  總體經濟市場趨勢分析與投資決策引擎。以「市場交易預期 → 總經因果鏈 → 八大循環 → 政策反應函數 →
  流動性與信用 → 製造業與全球貿易傳導 → 跨資產價格輪動 → 真實資金流 → 敘事與市場驗證」為核心，
  將總經資料轉化為市場環境評級、資產曝險、產業權重、風險條件與部位調整觸發點。
  整合 Risk Radar 宏觀風險雷達子模組（Step 11），支援每日快評、週報、月報、季報與重大事件後掃描。

  當使用者詢問下列問題時使用本 skill：市場現在適合投資嗎？現在是牛市還是熊市？景氣循環在哪個位置？
  Fed 升降息與 QE/QT 對市場的影響？CPI/PCE/GDP/PMI/非農就業數據怎麼解讀？市場已經 Price-in 多少？
  流動性是擴張還是收縮（TGA/RRP/準備金/M2）？信用條件是否惡化（SLOOS/HY OAS）？
  資金正在流向哪些資產類別？股票債券現金黃金如何配置？哪些產業值得佈局？
  中國信用與台韓出口對半導體的傳導？AI/半導體資本支出週期是否過熱？地緣政治風險評估？
  需要月報或季報形式的宏觀風險掃描？
  支援 Tier 1/2/3 指標分層（80+ 指標）、Macro Score 與 Confidence Score 雙分數輸出。
  Step 8A 跨資產價格輪動直接讀取全市場觀察 Google 試算表（100+ ETF 的趨勢、相對強弱排名與輪動訊號）。
version: 3.0.0
author: Evan
license: Proprietary
tags:
  - macroeconomics
  - market-expectations
  - causal-analysis
  - market-regime
  - liquidity-cycle
  - credit-cycle
  - manufacturing-cycle
  - asset-rotation
  - fund-flow-tracking
  - narrative-analysis
  - investment-strategy
  - risk-radar
---

# 總體經濟市場分析與投資決策引擎
## Macro Market Analysis v3.0

---

## 1. 定位

本技能不是經濟數據百科，也不以單一指標預測市場。

核心任務：

> **總經資料 → 因果推理 → 預期差 → 政策反應 → 市場驗證 → 投資決策**

分析時必須回答：

1. 經濟現在如何？
2. 經濟正在往哪裡變？
3. 市場原本預期什麼？
4. 資產價格已反映多少？
5. Fed、財政與信用條件如何演變？
6. 資金與價格是否確認該敘事？
7. 哪些條件會推翻目前判斷？

### 核心理念

- 空頭市場中，再好的股票也難逃下跌
- 多頭市場中，選對產業比選對個股更重要
- **資產配置決定 80% 的報酬，選股只決定 20%**
- 股票與債券交易的是**預期**，不是已公布的數據

---

## 2. 核心投資思維

### 2.1 市場交易的是預期

- 數據「好或壞」不等於市場「漲或跌」
- 必須比較：原值 / 修正值 / 共識 / 實際值 / 公布後市場反應
- 利多已被 Price-in 時，數據優於預期也可能利多出盡
- 市場極度悲觀時，數據只要不再惡化，價格就可能反轉

### 2.2 五維資料變數（每項數據都要跑一次）

| 維度 | 說明 |
|------|------|
| **Level** | 絕對值與歷史位置 |
| **Trend** | 近 1/3/6/12 個月方向 |
| **Rate of Change** | 改善或惡化的速度 |
| **Surprise** | 實際值相對市場共識 |
| **Revision** | 前期資料是否遭重大上修/下修 |

> ❌ 禁止只因 PMI > 50、失業率低或 GDP 正成長就直接判定市場多空。

### 2.3 數據必須放進因果鏈

每項資料必須標示：原因 → 傳導節點 → 結果 → 領先/同步/落後屬性。

### 2.4 敘事必須由價格、信用與資金驗證

新聞、政策語言與社群情緒是市場敘事的一部分，但不是交易指令。
詳見 `references/narrative-vs-reality.md`。

---

## 3. 適用與不適用情境

### 觸發關鍵詞

**經濟面：** 通膨、CPI、PPI、PCE、GDP、景氣、升息、降息、利率、Fed、就業、失業率、非農、衰退、軟著陸、硬著陸、預期差、Price-in

**市場面：** 大盤走勢、S&P 500、加權指數、牛市、熊市、市場情緒、股債配置、資產配置、市場體制

**流動性/信用：** 流動性、淨流動性、TGA、RRP、準備金、M2、QT、SLOOS、信用利差、HY OAS、去槓桿

**資金流：** 資金流、ETF 資金流、機構持倉、COT 報告、資產輪動、相對強弱、避險資產

**製造與貿易：** ISM、PMI、新訂單、庫存、中國信用、社會融資、南韓出口、台灣外銷訂單、半導體循環

**產業面：** 產業趨勢、產業週期、AI 資本支出、半導體、電動車、綠能、產業輪動

**風險面：** 地緣政治、中美關係、黑天鵝、系統性風險、風險雷達、風險掃描、月報更新、季報更新

### 不適用

| 需求 | 改用模組 |
|------|---------|
| 單一公司完整基本面 | `equity-fundamental-analysis` |
| 精確技術進出場 | `technical-analysis` |
| 深度產業供應鏈研究 | `industry-research` |
| 個股合理價與安全邊際 | `valuation-analysis` |
| 倉位大小與停損 | `risk-management` |

---

## 4. 執行總流程

| Step | 名稱 | 目的 | 主要參考文件 |
|:----:|------|------|------------|
| 0 | 問題界定 | 地區、時間尺度、資產範圍 | — |
| 1 | **Market Pricing** | 市場目前在交易什麼、已 Price-in 多少 | `fed-policy-framework.md` |
| 2 | Data Integrity | 資料來源、時效與修正驗證 | `data-sources.md` |
| 3 | Economic Causal Chain | 成長、就業、收入、消費 | `economic-indicators.md` |
| 4 | Inflation + Fed Reaction | 通膨成因與 Fed 反應函數 | `fed-policy-framework.md` |
| 5 | **Liquidity Cycle** | 五大流動性來源交叉驗證 | `liquidity-cycle.md` ⭐ |
| 6 | **Credit Cycle** | 銀行放貸、違約、信用利差 | `credit-cycle.md` ⭐ |
| 7 | Manufacturing + Trade | 訂單鏈與全球傳導 | `manufacturing-cycle.md`／`global-trade-transmission.md` ⭐ |
| 8A | **Price Rotation** | 跨資產價格輪動與相對強弱 | `cross-asset-price-rotation.md` ⭐ |
| 8B | **Actual Capital Flow** | ETF 申贖、COT、機構評級 | `cross-asset-fund-flow.md` |
| 9 | Narrative vs Reality | 敘事、部位、資料、價格四層檢驗 | `narrative-vs-reality.md` ⭐ |
| 10 | Regime Classification | 八大循環同步定位 | `policy-regime-classification.md`／`industry-cycles.md` |
| 11 | **Scenario & Risk Radar** | 三情境 + 12 項風險雷達（子模組） | `risk-radar-sop.md` |
| 12 | Investment Implications | Macro Score、曝險與產業權重 | `analysis-report-template.md` |
| 13 | Trigger Conditions | 確認、推翻與部位觸發條件 | — |

> ⭐ = v3.0 新增或重構模組。
> **Step 8A 與 8B 必須分開輸出，不可合併** —— 價格輪動不等於真實資金流。

---

## 5. Step 0｜問題界定

確認四項後才開始分析：

- **地區：** 全球 / 美國 / 中國 / 台灣 / 歐洲 / 日本
- **時間尺度：** 即時事件（1 日-2 週）/ 波段（1-3 月）/ 中期（3-12 月）/ 長期（1-5 年）
- **決策範圍：** 市場環境 / 資產配置 / 產業輪動 / 事件解讀 / 風險偵測
- **主要資產：** 股票、公債、信用債、黃金、商品、美元、比特幣、現金

未指定時，預設為：**美國經濟 + 全球風險資產 + 1-3 個月波段視角**。

---

## 6. Step 1｜Market Pricing（市場預期層）

**在讀任何經濟數據前先回答：**

1. 市場正在交易哪個主要敘事？
2. FedWatch / Fed Funds Futures 已 Price-in 多少次升降息？
3. 2Y、10Y、實質利率在交易什麼成長與通膨組合？
4. 信用利差是否確認 Risk-On？
5. 美元、黃金、原油、比特幣是否產生背離？
6. 市場交易的是未來 1-2 個月，還是 6-12 個月？

### 預期差表（每逢重大數據必填）

| 欄位 | 說明 |
|------|------|
| Previous | 原值 |
| Revised Previous | 修正後原值 |
| Consensus | 市場預期 |
| Actual | 實際值 |
| Surprise | Actual − Consensus |
| Pre-pricing | 公布前價格已反映程度 |
| Immediate Reaction | 公布後股/債/匯即時反應 |
| Follow-through | 1-5 日是否延續 |

### Policy Expectation Gap

比較 **Fed 聲明與點陣圖 vs Fed Funds Futures vs 2Y 殖利率**。
若 Fed 與市場定價明顯不一致，列為重大波動來源，並寫入 Step 11 情境。

---

## 7. Step 2｜資料來源與可信度

**優先順序：** 官方原始資料 > 交易所與市場原始來源 > 整合平台

整合平台（Trading Economics、Investing.com、MacroMicro、ETFdb、Morningstar）僅作輔助，
與官方資料不符時**以官方為準**，並註明發布日期。

每項資料必須標示：發布日期、所屬期間、原值/修正值/終值、下次更新日。

**重大修正警戒清單**（不可只引用 Headline）：非農就業、GDP、Retail Sales、Industrial Production、Payroll Benchmark Revisions、生產力與單位勞動成本。

完整來源清單見 `references/data-sources.md`。

---

## 8. Step 3｜經濟因果鏈

```text
企業訂單與獲利 → 招聘與裁員 → 工資與家庭收入
→ 消費與信貸使用 → 企業營收與庫存 → 生產與投資 → GDP
```

> 有工作與收入，才有可持續消費；有訂單與融資，企業才擴產與僱用。

**四大模組必看：**

| 模組 | 核心指標 |
|------|---------|
| 成長 | Real GDP、GDPNow、Real Final Sales、Business Fixed Investment、Industrial Production、CFNAI、LEI |
| 就業（依領先→落後） | Initial Claims → Continuing Claims → JOLTS Openings/Quits → ISM Employment → 非農 → 失業率 → 薪資成長 |
| 消費 | Real PCE Spending、Retail Sales Control Group、Real Disposable Income、Consumer Credit、信用卡違約率、儲蓄率 |
| 品質判別 | 健康降溫（招聘減少）vs 惡化降溫（大規模裁員 + 續領攀升 + 信貸緊縮） |

> ❌ 禁止把 PCE Price Index 誤當作 PCE Spending。
> ❌ GDP 必須拆解結構，不可只報總數。

詳見 `references/economic-indicators.md`。

---

## 9. Step 4｜通膨與 Fed 反應函數

**通膨成因分類：** 需求拉動 / 成本推動 / 貨幣信用擴張 / 供給衝擊 / 預期自我強化 / 住房與服務黏性

**核心資料：** CPI、Core CPI、PPI、PCE Price、Core PCE、Supercore Services、Shelter、薪資成長、單位勞動成本、T5YIE/T10YIE、密西根通膨預期、原油與運價

### Fed Reaction Function

```text
通膨 + 就業 + 金融穩定 + 成長 + 通膨預期 → Fed 政策立場
```

輸出必含：當前立場（鷹/中性/鴿）、下一步（升息/暫停/降息）、政策限制程度、市場定價差、對 2Y/10Y/美元/黃金/成長股與銀行股的傳導。

詳見 `references/fed-policy-framework.md`。

---

## 10. Step 5｜流動性循環 ⭐

五大來源交叉驗證：**Fed Assets、TGA、ON RRP、Bank Reserves、M2**。

```text
Liquidity Proxy = Fed Assets − TGA − ON RRP
```

> ⚠️ 此公式**僅為代理指標**，輸出時必須標示，不得視為市場流動性精確總量。
> ⚠️ **RRP 下降不必然是利多**，須先判斷資金流向準備金或被財政部吸收。

**輸出必含四項：** 方向、速度、主要驅動因子、對高 Beta / 長久期 / 信用市場的影響。

完整判讀規則、五階段定義與觀察節奏見 `references/liquidity-cycle.md`。

---

## 11. Step 6｜信用循環 ⭐

**信用通常比 GDP 更早反映惡化。**

核心資料：SLOOS 放貸標準與貸款需求、C&I Loans、Consumer Credit、信用卡/車貸違約率、HY OAS、IG OAS、FRA-OIS、商業地產違約率。

**最高優先警訊：** 股市創新高但 HY OAS 快速擴大 → 重大背離，**優先相信信用市場**。

五階段（放寬 / 穩定 / 收緊 / 惡化 / 危機）、傳導鏈與量化門檻見 `references/credit-cycle.md`。

---

## 12. Step 7｜製造業與全球貿易 ⭐

### 美國端

```text
New Orders → Production → Employment → Inventories → Supplier Deliveries → Prices
```

```text
Manufacturing Impulse = New Orders − Inventories
```

> **PMI 看方向與變化率，不看 50 這個水位。** PMI < 50 但連續改善可能是復甦；> 50 但連續下滑可能是趨緩。

服務業（ISM Services）佔美國 GDP 比重更高，需同步判讀。詳見 `references/manufacturing-cycle.md`。

### 全球傳導鏈

```text
中國信用（Credit Impulse / TSF）→ 中國 PMI → 全球貿易
→ 南韓出口與半導體出口 → 台灣外銷訂單 → 台灣電子暨光學 PMI → 半導體營收與資本支出
```

> ⚠️ AI 時代必須拆解出口的產品結構 —— 傳統電子與 AI 資本支出已出現脫鉤。

詳見 `references/global-trade-transmission.md`。

---

## 13. Step 8A｜跨資產價格輪動 ⭐

**主要工具：全市場觀察表（Google 試算表）**
`https://docs.google.com/spreadsheets/d/1OMbg5nPRELu7cpkVrGR9CppMyUhjebpShk17n4wyhZA/edit?usp=sharing`

觀察 1D/5D/20D/60D 報酬、Rank、REL、60-Day Trend、YTD。

### ⚠️ 命名紀律

此步驟的正確名稱是 **Price Rotation / Relative Strength**。
Rank 前進、60D% 上升、REL60 轉正、Trend 轉 Up —— **都只是價格證據，不得直接稱為資金流入**。

欄位解讀指南、100+ ETF 資產分類表、輪動判讀邏輯與核心觀察組見
`references/cross-asset-price-rotation.md`。

---

## 14. Step 8B｜真實資金流

用以下證據驗證 Step 8A 的價格輪動：
ETF 淨申購/贖回、共同基金流量、CFTC COT、Dealer/Asset Manager 部位、NAAIM、13F、機構 OW/N/UW 評級。

| 價格輪動 | 真實資金流 | 判讀 |
|---|---|---|
| 強 | 流入 | ✅ 高信度趨勢 |
| 強 | 流出 | ⚠️ 軋空、供給不足或追價風險 |
| 弱 | 流入 | ⚠️ 可能在吸收賣壓，等待轉折 |
| 弱 | 流出 | 🔴 高信度弱勢 |

完整 SOP（16 大資產類別、資金溫度分數、COT 判讀）見 `references/cross-asset-fund-flow.md`。

---

## 15. Step 9｜敘事與真實

四層依序檢驗：**Dominant Narrative → Consensus Positioning → Data Reality → Market Confirmation**

結論必須從五個標籤擇一：敘事與資料一致 / 敘事領先資料 / 價格領先資料 / 敘事過度延伸 / 敘事與信用市場背離。

> ⚠️ **不得以陰謀論取代證據。** 每個對敘事的質疑都必須指出具體是哪項資料、信用指標或價格不支持，
> 且結論必須可被未來資料證偽（寫入 Step 13）。

詳見 `references/narrative-vs-reality.md`。

---

## 16. Step 10｜八大循環體制分類

不可用單一景氣階段概括整個市場。八大循環須同步定位：

| 循環 | 狀態選項 |
|---|---|
| Economic | 復甦 / 擴張 / 趨緩 / 衰退 |
| Inflation | 上升 / 高檔 / 降溫 / 通縮 |
| Monetary | 緊縮 / 暫停 / 寬鬆 |
| Yield | 倒掛加深 / 陡峭化 / 平坦化 / 正常化 |
| Liquidity | 修復 / 擴張 / 中性 / 收縮 / 去槓桿 |
| Credit | 放寬 / 穩定 / 收緊 / 惡化 / 危機 |
| Manufacturing | 去庫存 / 補庫存 / 擴張 / 過熱 |
| Asset Rotation | Risk-On / Rotation / Defensive / Risk-Off |

**另加：** Productivity / Capex Cycle、AI / Semiconductor Capex Cycle。

**時間軸輸出：** Nowcast（現在）、1-3M（波段）、3-12M（中期），並標示市場主要在交易哪一層。

> Monetary 與 Liquidity 兩個循環的定位，需搭配 `references/policy-regime-classification.md`
> 判斷「誰在主導資金成本」（央行獨立性、財政與貨幣互動），而非只看升降息方向。

---

## 17. Step 11｜情境與 Risk Radar（子模組）

### 17.1 三情境

Base / Bull / Bear 各須含：機率、因果路徑、需觀察的資料、失效條件、受惠與受害資產。

### 17.2 Risk Radar 固定掃描 12 項

1. 健康去通膨 vs 壓力型去通膨
2. 股市 vs 通膨預期背離
3. 流動性週期定位
4. 信用惡化
5. 殖利率與期限溢酬衝擊
6. 財政赤字與發債壓力
7. 美元急升/急貶
8. 銀行與商業地產
9. 地緣政治與能源供應
10. AI / 半導體 Capex vs Revenue
11. 槓桿與衍生工具、擁擠交易
12. 重大政策、選舉、關稅與行政命令

**觸發時機：** 月度/季度例行掃描，或重大事件後臨時啟動（FOMC 意外、信用事件、黑天鵝）。

**22 項指標清單、燈號規則與月報/季報標準輸出格式見 `references/risk-radar-sop.md`。**

> Risk Radar 不提供個股建議，僅提供資產類別/產業層級方向指引。

---

## 18. Step 12｜投資決策輸出

### 18.1 Macro Score（100 分）

| 模組 | 權重 |
|---|---:|
| Growth / Consumption | 15 |
| Inflation | 10 |
| Fed / Rates | 15 |
| Liquidity | 20 |
| Credit | 15 |
| Manufacturing / Global Trade | 10 |
| Market Confirmation | 10 |
| System Risk | 5 |
| **Total** | **100** |

每個模組依 Level、Trend、Rate of Change、Surprise、Revision、Cross-confirmation 評分。

| 分數 | 判讀 |
|---|---|
| 80-100 | 強 Risk-On |
| 65-79 | 偏多 |
| 50-64 | 中性 / 輪動 |
| 35-49 | 偏空 |
| 0-34 | 強 Risk-Off |

### 18.2 Confidence Score（100 分）

衡量資料一致性、資料新鮮度、指標背離程度、市場是否確認、重大事件是否尚未公布。

> ⚠️ **不得只給單一 Macro Score**，必須同時輸出 Confidence，避免假精確。

### 18.3 曝險建議

輸出股票曝險方向、高/低 Beta、債券久期、信用債、現金、黃金、商品、比特幣、產業超配/標配/低配。

> ⚠️ 資產比例必須是**情境建議**（對應 Base/Bull/Bear），不得預設適用所有投資者。
> 實際倉位大小與停損由 `risk-management` 模組決定。

### 18.4 與選股流程的銜接

總經分析完成後依序進入：趨勢產業（`industry-research`）→ 個股基本面（`equity-fundamental-analysis`）
→ 估值（`valuation-analysis`）→ 情緒與籌碼（`market-sentiment-tracking`）→ 技術面（`technical-analysis`）
→ 倉位與風控（`risk-management`）。

若 SPY/QQQ 趨勢不支持、流動性與信用轉差、或重大事件風險過高 → **降低個股進場強度與槓桿**。

---

## 19. Step 13｜觸發條件

每份報告必須列出三組：

- **Confirming Triggers** — 哪些資料出現後可提高目前判斷的信心
- **Invalidating Triggers** — 哪些資料會推翻目前結論
- **Position Triggers** — 在什麼條件下提高/降低股票曝險、調整久期、增持現金或黃金、降低選擇權槓桿

> 避免使用無根據的固定金額門檻，應以趨勢、歷史分位數與多重指標確認為準。

---

## 20. 指標分層（80+ 指標不得全部等權）

### Tier 1｜核心決策指標（每次完整分析必更新）

GDPNow、Real PCE / Retail Sales Control Group、Core PCE、Initial / Continuing Claims、非農、
ISM New Orders、FedWatch / 2Y、10Y 實質利率、Fed Assets、TGA、ON RRP、Bank Reserves、
M2 YoY、HY OAS、SLOOS、DXY、VIX、市場寬度

### Tier 2｜驗證指標（Tier 1 轉折或矛盾時調用）

LEI、CFNAI、JOLTS、消費者信心、IG OAS、房市、PPI、單位勞動成本、C&I Loans、區域聯儲調查

### Tier 3｜診斷指標（出現異常才深入）

CPI 細項、信用卡/車貸違約、商業地產、FRA-OIS、航運/BDI、各產業庫存、區域銀行壓力、特定國家政治風險

完整定義、時效性與領先/落後屬性見 `references/economic-indicators-reference.md`。

---

## 21. 快速執行模式

| 模式 | 執行範圍 | 適用 |
|------|---------|------|
| **每日日報** ⭐ | Step 1 + Step 12 摘要（指數收盤、US10Y/DXY/WTI、事件表） | 對應專案 `CLAUDE.md` 區塊一、二、六，**不跑完整 14 步** |
| 每日快評 | Step 1 + Step 3/4 相關項 + Step 9 | 單一事件即時解讀 |
| 週度更新 | Step 1、2、5、6、8A、8B + 重大事件日程 | Claims、Fed 資產、TGA/RRP、HY OAS、輪動 |
| 月度深度 | Step 0-13 完整 + Risk Radar 月報 | 就業、CPI/PCE、ISM、M2、中國 PMI、台韓出口 |
| 季度策略 | Step 0-13 完整 + GDP + SLOOS + 財報/Capex + 八大循環 + 三情境 | 中期資產配置 |

---

## 22. 標準輸出格式

```markdown
# Macro Dashboard｜YYYY-MM-DD

## 一句話結論
市場主要交易 ______，總經處於 ______，流動性 ______，信用 ______。策略上 ______，但需防範 ______。

## 1. Regime Dashboard（八大循環：狀態 / 趨勢 / 信心）
## 2. Market Pricing（敘事、已 Price-in、Fed vs Market Gap、最擁擠交易）
## 3. 核心因果鏈（資料 A → 傳導 B → 結果 C → 市場影響 D）
## 4. 最新數據表（原值/修正 | 預期 | 實際 | 趨勢 | 解讀）
## 5. 最大矛盾與背離
## 6. Price Rotation vs Actual Flow（分列，不可合併）
## 7. 三情境（機率 / 因果路徑 / 受惠資產 / 失效條件）
## 8. Macro Score __/100｜Confidence __/100
## 9. 投資含義（股票曝險、產業偏好、債券、黃金/商品、現金、槓桿）
## 10. Trigger Conditions（Confirming / Invalidating / Position）
```

完整報告範本見 `references/analysis-report-template.md`。

---

## 23. 分析紀律（12 條）

1. 不用單一指標決定多空。
2. 不混淆價格輪動與真實資金流。
3. 不把 Net Liquidity 當作精確流動性總量。
4. 不忽略前值修正。
5. 不只看 Headline，必須看結構。
6. 不只看絕對值，必須看方向與速度。
7. 不把通膨數據自動解讀成利多/利空。
8. 不把降息自動解讀成利多 —— 須先判斷降息成因。
9. 不因官方資料或新聞敘事就跳過市場驗證。
10. 不用陰謀論取代證據 —— 敘事分析必須由資料、信用與價格確認。
11. 不提供無條件適用所有人的精確配置比例。
12. 重大 FOMC、CPI、非農、GDP、財報或政策事件前，降低過度槓桿。

---

## 24. 參考文件

**核心方法論**
- `references/interpretation-framework.md` — 數據解讀與決策框架
- `references/analysis-report-template.md` — 標準化報告範本
- `references/data-sources.md` — 權威數據來源指引

**循環模組（Step 5-9）** ⭐
- `references/liquidity-cycle.md` — 流動性循環（Step 5）
- `references/credit-cycle.md` — 信用循環（Step 6）
- `references/manufacturing-cycle.md` — 製造業循環（Step 7 美國端）
- `references/global-trade-transmission.md` — 全球製造與貿易傳導鏈（Step 7 全球端）
- `references/cross-asset-price-rotation.md` — 跨資產價格輪動（Step 8A）
- `references/cross-asset-fund-flow.md` — 真實資金流追蹤 SOP（Step 8B）
- `references/narrative-vs-reality.md` — 敘事與真實檢驗（Step 9）

**指標與政策**
- `references/economic-indicators-reference.md` — 完整指標總表（10 大類、80+ 指標）
- `references/economic-indicators.md` — 經濟指標定義與解讀標準
- `references/fed-policy-framework.md` — Fed 政策決策邏輯與反應函數
- `references/policy-regime-classification.md` — 政策 Regime 分類與市場含義（Step 4／Step 10）

**產業與風險**
- `references/risk-radar-sop.md` — Risk Radar 宏觀風險雷達掃描 SOP（Step 11）
- `references/industry-cycles.md` — 各產業景氣循環特性與輪動策略
- `references/geopolitical-risks.md` — 地緣政治風險評估清單
- `references/historical-scenarios.md` — 歷史情境資料庫與類比分析

**實用工具**
- 🔗 **全市場觀察表** — `https://docs.google.com/spreadsheets/d/1OMbg5nPRELu7cpkVrGR9CppMyUhjebpShk17n4wyhZA/edit?usp=sharing`（Step 8A 主要工具）
- `assets/investment-decision-checklist.md` — 投資決策檢查清單
- `assets/2025_macro-economics-guide.pdf` — 總體經濟分析實戰指引

---

## 25. 版本歷史

### v3.0.0 (2026-07-28) ⭐ NEW

**框架重構：**
- ✅ 將框架由「指標蒐集」升級為「投資決策引擎」：市場預期 → 因果鏈 → 政策反應 → 市場驗證 → 投資決策
- ✅ 流程由 Step 1-10 重編為 **Step 0-13**（Risk Radar 由 Step 10 → **Step 11**；資金流由 Step 5 → **Step 8A/8B**）
- ✅ 新增 Market Pricing 與 Policy Expectation Gap（Step 1）
- ✅ 新增五維資料變數：Level、Trend、Rate of Change、Surprise、Revision
- ✅ 新增經濟因果鏈：企業訂單 → 就業 → 收入 → 消費 → 生產 → GDP
- ✅ 單一景氣週期擴充為**八大循環**同步定位
- ✅ Fed 分析升級為 Fed Reaction Function + Policy Expectation Gap

**新增模組（含對應 references）：**
- ✅ 重構流動性模組：Fed Assets / TGA / RRP / Bank Reserves / M2 五層交叉驗證，明確標示 Net Liquidity 僅為代理指標
- ✅ 新增完整信用循環（SLOOS、HY/IG OAS、五階段、股信背離警訊）
- ✅ 新增製造業訂單鏈與 Manufacturing Impulse（New Orders − Inventories）
- ✅ 新增中國信用 → 中國 PMI → 南韓出口 → 台灣外銷訂單 → 半導體傳導鏈，補入 China Credit Impulse
- ✅ 將「價格輪動」與「真實資金流」正式拆為 Step 8A / 8B，禁止混用命名
- ✅ 新增 Narrative vs Reality 四層檢驗與反陰謀論紀律

**決策輸出：**
- ✅ 新增 Macro Score（100 分）與 Confidence Score 雙分數
- ✅ 新增 Base / Bull / Bear 三情境
- ✅ 新增 Confirming / Invalidating / Position 三組觸發條件
- ✅ 新增 Tier 1/2/3 指標分層（取代原 24 項平面檢查清單）
- ✅ 新增與 industry-research / equity-fundamental / valuation / sentiment / technical / risk-management 的銜接邏輯
- ✅ 新增「每日日報模式」，對應專案 CLAUDE.md 區塊一、二、六（不跑完整流程）

**結構調整：**
- ✅ 依 `docs/skill-optimization.md` 原則，深度內容下放 references，SKILL.md 保留執行骨架
- ✅ 保留 v2.4.0 全市場觀察表欄位解讀指南（移至 `references/cross-asset-price-rotation.md`）
- ✅ 保留 v2.4.0 之 Risk Radar、官方數據來源與 80+ 指標能力

### v2.4.0 (2026-03-18)
- Step 5 整合全市場觀察表 Google 試算表；新增欄位解讀指南（Rank、REL、20R/60R/120R）

### v2.3.0 (2026-03-18)
- 新增完整數據指標總表（10 大類、80+ 指標）、流動性指標章節與淨流動性公式

### v2.2.0 (2026-02-19)
- 整合 risk-radar 為子模組，建立四大週期判斷與月報/季報格式

### v2.1.0 (2026-01-18)
- 新增跨資產資金流追蹤模組、ETF/COT/機構評級三重驗證、16 大資產類別追蹤體系
