---
name: market-sentiment-tracking
description: >
  市場情緒追蹤與逆向投資機會識別，追蹤恐慌貪婪指標（VIX、Fear & Greed Index、Put/Call Ratio）、籌碼面（融資融券、法人動向、GEX）、分析師共識與社群媒體情緒，整合為 0-100 綜合情緒評分，識別極端情緒反轉機會與投機過熱警訊。

  當使用者詢問以下問題時請使用本 skill：市場現在是貪婪還是恐慌？VIX 飆升代表什麼？現在有逆向投資機會嗎？融資融券比率正常嗎？法人（外資/投信）在買還是賣？這支股票的籌碼健康嗎？社群媒體對這支股票的看法如何？現在是散戶追高的警訊嗎？Put/Call Ratio 顯示什麼信號？GEX 是正還是負？
version: 1.0.0
author: Evan
license: Proprietary
tags:
  - market-sentiment
  - fear-greed-index
  - contrarian-investing
  - behavioral-finance
  - crowd-psychology
  - social-sentiment
  - positioning-analysis
---

# Market Sentiment Tracking（市場情緒追蹤）

## 概述

本技能系統化追蹤市場情緒與投資人行為，透過量化情緒指標、籌碼面分析、資金流向監測、分析師共識與社群媒體情緒挖掘，整合為綜合情緒評分（0-100），識別極端情緒帶來的逆向投資機會與投機過熱警訊。

### 核心理念

**「在別人貪婪時恐懼，在別人恐慌時貪婪」**

- 基本面告訴你「應該值多少」，情緒面告訴你「市場認為值多少」
- 兩者差距 = 投資機會
- 情緒極端時（< 20 或 > 80），往往是最佳進場或退場時機

### 與其他階段的關係

```
第一階段（總經） → 判斷「應該」做什麼（理性面）
第二階段（產業） → 判斷「該佈局」哪些板塊
第三階段（個股） → 判斷「這家公司」值不值得投資
第四階段（估值） → 判斷「價格」是否合理
第五階段（情緒） → 判斷「市場」在做什麼（行為面）⭐ 當前階段
第六階段（技術） → 判斷「時機」何時進場
第七階段（風險） → 判斷「如何」管理風險
```

### 七大核心能力

1. **恐慌與貪婪指標** — VIX、CNN Fear & Greed Index、Put/Call Ratio
2. **籌碼面與大戶持倉** — 融資融券、法人買賣超、Institutional Ownership、Short Interest、GEX
3. **資金流向與避險情緒** — ETF 資金流、黃金流入、DXY 變動、國債殖利率
4. **分析師共識追蹤** — 評級分布、評級變化速度、目標價共識
5. **社群與媒體情緒** — 新聞 NLP 分析、Reddit/PTT 熱度、Meme Stock 偵測
6. **散戶行為監測** — 新開戶數、零股交易量、選擇權未平倉
7. **情緒預測與位階判斷** — 歷史分位數、情緒-價格背離偵測、轉折點預測

---

## 適用場景

### 觸發關鍵詞

**情緒指標：** VIX、恐慌指數、Fear & Greed、Put/Call Ratio、市場情緒、貪婪、恐慌、投機、過熱

**籌碼面：** 融資融券、券資比、法人買賣超、外資動向、散戶、主力、大戶、放空比例、GEX、暴力盤、軋空

**資金流向：** 避險資產、黃金、美元、ETF 資金流、風險偏好、資金撤退

**社群情緒：** 社群媒體、新聞情緒、Reddit、Twitter、PTT、熱度、討論度、Meme Stock

**逆向投資：** 逆向機會、極端情緒、反市場、反轉、恐慌性殺盤

### 不適用情境

- 公司基本面深度分析 → 使用 `equity-fundamental-analysis`
- 總體經濟環境評估 → 使用 `macro-market-analysis`
- 估值與目標價計算 → 使用 `valuation-analysis`

---

## 執行流程

### Step 1: 情境識別與分析範圍

識別問題類型：
- 市場整體情緒 → 需要 VIX、Fear & Greed、Put/Call 等宏觀情緒指標
- 個股籌碼分析 → 需要融資融券、法人動向、Short Interest
- 短線情緒轉折 → 需要即時指標（VIX、GEX、避險資產流向）
- 社群情緒監測 → 需要新聞與社群媒體分析
- 逆向投資機會 → 需要情緒極端值與歷史比對

確定分析範圍（市場 / 板塊 / 個股，台股 / 美股 / 全球）

---

### Step 2: 恐慌與貪婪指標追蹤

**目標：** 量化市場整體情緒，識別極端恐慌或貪婪

**VIX 恐慌指數**（來源：CBOE）
- < 12 極度自滿 → 過度樂觀警訊
- 15-20 正常波動
- 20-30 緊張升溫
- 30-40 恐慌模式 → 可能逆向佈局機會
- > 40 極度恐慌 → 強烈逆向信號

詳細解讀 → `references/market-indicators/vix-interpretation-guide.md`

**CNN Fear & Greed Index**（來源：CNN）
- 0-20 極度恐慌 🟢 | 21-40 恐慌 🟡 | 41-60 中性 | 61-80 貪婪 🔴 | 81-100 極度貪婪 🔴

極端點反轉策略 → `references/market-indicators/fear-greed-reversal-strategy.md`

**Put/Call Ratio**（來源：CBOE）
- > 1.2 極度悲觀（逆向信號）| 0.7-1.0 中性 | < 0.5 極度樂觀（警訊）

詳細解讀 → `references/market-indicators/put-call-ratio-guide.md`

---

### Step 3: 籌碼面與大戶持倉分析

**目標：** 追蹤散戶、法人與大戶持倉，判斷籌碼健康度

**融資融券（台股）** — 健康特徵：股價上漲 + 融資減少 + 法人買超
- 券資比 < 10% 過度樂觀；> 30% 可能軋空機會
- 詳見 `references/institutional-flows/margin-trading-analysis.md`

**法人買賣超（台股）** — 外資方向最重要；投信連續買超代表籌碼集中
- 詳見 `references/institutional-flows/institutional-flow-taiwan.md`

**Institutional Ownership（美股）** — > 70% 高度機構化（穩定）；< 30% 散戶主導（高波動）
- Insider Buying 為正面信號；大量 Insider Selling 需判斷
- 詳見 `references/institutional-flows/institutional-ownership-analysis.md`

**Short Interest（放空比例）** — > 20% 極度看空，但結合正面消息可能觸發軋空
- 軋空識別 → `references/institutional-flows/short-squeeze-detection.md`

**GEX（Gamma Exposure）** — Positive GEX 壓制波動（區間盤）；Negative GEX 加劇波動（暴力盤）
- Zero Gamma Level 為關鍵支撐/壓力位
- 詳見 `references/options-analysis/gex-gamma-exposure-guide.md`

---

### Step 4: 資金流向與避險情緒

**目標：** 追蹤資金在風險與避險資產間的快速轉換

- **ETF 資金流** — 引用 `macro-market-analysis` Step 8B（真實資金流）結果；觀察股票 ETF 大幅流出 + 債券/黃金流入
- **黃金短線避險** — GLD ETF 單日流入 > $500M = 強烈避險需求；詳見 `references/market-indicators/gold-safe-haven-flow.md`
- **DXY 美元指數** — 單日漲 > 1% 代表資金撤離風險資產；詳見 `references/market-indicators/dxy-risk-sentiment.md`
- **國債殖利率** — 10 年期美債殖利率快速下降 = 避險需求（債券價格上漲）

---

### Step 5: 分析師共識追蹤

**目標：** 追蹤專業分析師評級變化，識別共識轉向

評級分布（來源：TipRanks、Yahoo Finance）：
- 看多比例 > 80% → 一致看多（可能過度樂觀，警訊）
- 看多比例 < 20% → 一致看空（可能逆向機會）
- 近 1 週快速升/降評 > 5 次 → 評級動態異常

安全邊際 = (平均目標價 - 當前價) / 當前價，若 < 0 代表股價已超越目標價

詳細方法 → `references/sentiment-analysis/analyst-consensus-tracking.md`

---

### Step 6: 社群與媒體情緒挖掘

**目標：** NLP 量化新聞與社群情緒，偵測極端值

**執行步驟（簡版）：**
1. 搜尋近 7/30 天相關新聞標題，評分正面(+1)/中性(0)/負面(-1)
2. 搜尋 Reddit WSB、StockTwits（美股）或 PTT Stock 板（台股）的討論熱度與情緒傾向
3. 計算看多/看空比例，偵測極端值（> 90% 一致 = 過度情緒）
4. Meme Stock 偵測：討論量 > 平均 5 倍 + 散戶一致看多 = 投機炒作警訊

詳細 NLP 方法 → `references/sentiment-analysis/news-sentiment-nlp.md`
社群分析方法 → `references/sentiment-analysis/social-sentiment-analysis.md`

---

### Step 7: 散戶行為監測

**目標：** 追蹤散戶進場與投機氛圍

- **台股：** 新開戶數激增 + 零股交易量暴增 + 選擇權 OI 創新高 = 散戶狂熱（警訊）
- **警訊信號：** 新開戶數創歷史新高 + 市場已連續上漲數月 = 散戶追高可能見頂

詳細指標 → `references/sentiment-analysis/retail-investor-behavior.md`

---

### Step 8: 情緒預測與位階判斷

**目標：** 判斷當前情緒歷史位置，預測轉折點

**情緒歷史分位數：**
- < 10% → 極度恐慌（歷史低檔，強烈逆向信號）
- 30-70% → 正常範圍
- > 90% → 極度貪婪（歷史高檔，警訊）

**情緒-價格背離偵測：**
- 頂背離：價格創新高 + 情緒分數不再創新高 → 潛在頂部警訊
- 底背離：價格創新低 + 情緒分數不再創新低 → 潛在底部機會
- 連續 2 週以上背離 = 背離確認

**轉折點觸發條件：** 情緒分數到達極端值（< 20 或 > 80）+ 連續 3 天不再創新極端值 + 初步反轉信號

預測框架 → `references/frameworks/sentiment-prediction-framework.md`

---

### Step 9: 綜合情緒評分與操作建議

**情緒評分系統（0-100 分）：**

| 維度 | 權重 | 評分標準 | 數據來源 |
|------|------|---------|---------|
| 恐慌指標 | 25% | 0（極度恐慌）~ 100（極度貪婪）| VIX、Fear & Greed、Put/Call |
| 籌碼面 | 25% | 0（極度悲觀）~ 100（極度樂觀）| 融資融券、法人動向、Short Interest、GEX |
| 分析師共識 | 20% | 0（一致看空）~ 100（一致看多）| 評級分布、評級變化 |
| 社群/媒體情緒 | 15% | 0（極度負面）~ 100（極度正面）| 新聞 NLP、社群情緒 |
| 散戶行為 | 15% | 0（散戶恐慌）~ 100（散戶狂熱）| 新開戶數、零股、選擇權 OI |

**評分計算：**
```
綜合情緒分數 =
(恐慌指標 × 0.25) + (籌碼面 × 0.25) +
(分析師共識 × 0.20) + (社群情緒 × 0.15) + (散戶行為 × 0.15)
```

**綜合情緒分數解讀：**

| 分數 | 情緒狀態 | 建議 |
|------|---------|------|
| 0-20 | 極度恐慌 😱 | 🟢 逆向投資機會（分批進場）|
| 21-40 | 偏向恐慌 😟 | 🟡 謹慎佈局（基本面好的標的）|
| 41-60 | 中性 😐 | 🟡 正常持有，按計畫執行 |
| 61-80 | 偏向貪婪 😊 | 🔴 謹慎追高，考慮部分獲利了結 |
| 81-100 | 極度貪婪 🤑 | 🔴 高風險區，建議減碼 |

**操作建議矩陣（情緒面 × 基本面）：**

| 情緒面 | 基本面優 | 基本面中 | 基本面差 |
|--------|---------|---------|---------|
| 極度恐慌（0-20） | 🟢 積極買進 | 🟡 逢低佈局 | 🔴 避免（可能基本面惡化）|
| 偏向恐慌（20-40） | 🟢 分批買進 | 🟡 小額試單 | 🔴 觀望 |
| 中性（40-60） | 🟢 持有 | 🟡 持有 | 🔴 減碼 |
| 偏向貪婪（60-80） | 🟡 持有/部分獲利 | 🔴 獲利了結 | 🔴 賣出 |
| 極度貪婪（80-100） | 🔴 獲利了結 | 🔴 賣出 | 🔴 賣出 |

**黃金法則：** 當「情緒極端（< 20 或 > 80）+ 基本面未惡化」→ 最佳逆向投資機會

評分細節 → `references/frameworks/sentiment-scoring-methodology.md`
逆向投資策略 → `references/frameworks/contrarian-investing-framework.md`

---

## 輸出格式

```markdown
## 市場情緒分析摘要

**分析日期：** YYYY-MM-DD
**分析標的：** [市場整體 / 特定產業 / 個股代碼]

### 📊 綜合情緒評分：XX/100（情緒狀態）

| 維度 | 評分 | 狀態 | 關鍵發現 |
|------|------|------|---------|
| 恐慌指標 | XX/100 | 😊/😐/😟 | VIX XX，Fear & Greed XX |
| 籌碼面 | XX/100 | 😊/😐/😟 | 融資 XX 億，法人買超 XX 億 |
| 分析師共識 | XX/100 | 😊/😐/😟 | 看多比例 XX% |
| 社群情緒 | XX/100 | 😊/😐/😟 | 正面新聞 XX%，社群熱度 XX |
| 散戶行為 | XX/100 | 😊/😐/😟 | 新開戶數 XX，零股交易 XX |

### 🎯 操作建議

🟢/🟡/🔴 **[積極買進 / 分批買進 / 持有 / 獲利了結 / 賣出]**

**理由（3-5 句話）：** [整合情緒分析結果]

### 🔥 反市場機會

✅ 發現逆向投資機會 / ❌ 目前無明顯逆向機會

### 📈 情緒位階與預測

- **歷史分位數：** XX%（過去 3 年）
- **情緒-價格背離：** ✅ 偵測到 / ❌ 無背離
- **轉折點預測：** [1-2 週內可能反轉 / 情緒仍將持續]

### ⚠️ 風險提示

[2-3 項關鍵風險或警訊]

**下一步追蹤重點：**
- [追蹤項目 1]
- [追蹤項目 2]
```

完整詳細報告範本 → `references/tools/sentiment-report-template.md`

---

## 參考資料

**情緒指標：**
- `references/market-indicators/vix-interpretation-guide.md`
- `references/market-indicators/fear-greed-reversal-strategy.md`
- `references/market-indicators/put-call-ratio-guide.md`
- `references/market-indicators/gold-safe-haven-flow.md`
- `references/market-indicators/dxy-risk-sentiment.md`

**籌碼面分析：**
- `references/institutional-flows/margin-trading-analysis.md`
- `references/institutional-flows/institutional-flow-taiwan.md`
- `references/institutional-flows/institutional-ownership-analysis.md`
- `references/institutional-flows/short-squeeze-detection.md`
- `references/options-analysis/gex-gamma-exposure-guide.md`

**分析師與社群：**
- `references/sentiment-analysis/analyst-consensus-tracking.md`
- `references/sentiment-analysis/news-sentiment-nlp.md`
- `references/sentiment-analysis/social-sentiment-analysis.md`
- `references/sentiment-analysis/retail-investor-behavior.md`

**情緒預測與框架：**
- `references/frameworks/sentiment-prediction-framework.md`
- `references/frameworks/sentiment-scoring-methodology.md`
- `references/frameworks/contrarian-investing-framework.md`
- `references/frameworks/behavioral-finance-principles.md`

**工具與範本：**
- `references/tools/data-sources.md`
- `references/tools/sentiment-dashboard-template.md`
- `references/tools/contrarian-opportunity-checklist.md`
- `references/tools/sentiment-report-template.md`

---

**免責聲明：** 本技能提供的情緒分析與操作建議僅供參考，不構成投資建議。市場情緒瞬息萬變，歷史模式不代表未來表現。投資決策應基於個人風險承受能力、完整研究與專業諮詢。
