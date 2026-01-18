---
name: market-sentiment-tracking
description: |
  第五階段：市場情緒追蹤與逆向投資機會識別。追蹤恐慌與貪婪指標（VIX、Fear & Greed Index、Put/Call Ratio）、籌碼面（融資融券、法人動向、GEX）、資金流向（ETF、避險資產）、分析師共識與社群媒體情緒，整合為 0-100 綜合情緒評分，識別極端情緒反轉機會與投機過熱警訊。
  
  使用時機：(1) 判斷市場整體情緒是貪婪還是恐慌 (2) 評估個股籌碼健康度與投機氛圍 (3) 識別逆向投資機會 (4) 追蹤散戶與法人行為 (5) 監測社群與媒體情緒變化 (6) 預測短期情緒轉折點。適用於承接前四階段分析後的進場時機判斷，或獨立執行市場情緒檢測。
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

# Market Sentiment Tracking (市場情緒追蹤)

## 概述

本技能模擬資深投資人對市場情緒與投資人行為的系統化追蹤，透過量化情緒指標、籌碼面分析、資金流向監測、分析師共識與社群媒體情緒挖掘，整合為綜合情緒評分（0-100），識別極端情緒帶來的逆向投資機會與投機過熱警訊。

### 核心理念

**「理解市場先生的情緒波動，在別人貪婪時恐懼，在別人恐慌時貪婪」**

- **基本面告訴你「應該值多少」，情緒面告訴你「市場認為值多少」**
- 兩者差距 = 投資機會
- 情緒極端時（< 20 或 > 80），往往是最佳進場或退場時機
- 行為金融學核心：過度反應、羊群效應、確認偏誤

### 與其他階段的關係

```
第一階段（總經）→ 判斷「應該」做什麼（理性面）
第二階段（產業）→ 判斷「該佈局」哪些板塊（策略面）
第三階段（個股）→ 判斷「這家公司」值不值得投資（基本面）
第四階段（估值）→ 判斷「價格」是否合理（價值面）
第五階段（情緒）→ 判斷「市場」在做什麼（行為面）⭐ 當前階段
第六階段（技術）→ 判斷「時機」何時進場（執行面）
第七階段（風險）→ 判斷「如何」管理風險與執行紀律（管理面）
```

### 核心能力

1. **恐慌與貪婪指標追蹤**
   - VIX 恐慌指數（瞬間波動情緒變化）
   - CNN Fear & Greed Index（極端點短線反轉）
   - Put/Call Ratio（選擇權偏多偏空過熱訊號）

2. **籌碼面與大戶持倉分析**
   - 融資融券餘額（台股散戶情緒）
   - 法人買賣超（外資、投信、自營商動向）
   - Institutional Ownership（美股機構持倉）
   - Short Interest（放空比例）
   - GEX（Gamma Exposure，暴力盤與軋空觀察）

3. **資金流向與避險情緒**
   - ETF 資金流向（引用第一階段，觀察資金風格快速轉換）
   - 黃金短線避險流入（風險迴避立即反應）
   - 美元指數 DXY 快速變動（風險偏好/撤退）
   - 國債殖利率與價格（避險需求）

4. **分析師共識追蹤**
   - 評級分布（Buy/Hold/Sell 比例）
   - 評級變化速度（升評 vs 降評趨勢）
   - 目標價共識（分析師平均目標價 vs 當前價）

5. **社群與媒體情緒挖掘**（深度分析）
   - 新聞情緒 NLP 分析（正面/中性/負面比例）
   - 社群熱度追蹤（Reddit、Twitter/X、PTT Stock）
   - 關鍵字頻率與情緒極端值偵測

6. **散戶行為監測**
   - 新開戶數（散戶進場高峰）
   - 零股交易量（台股散戶指標）
   - 選擇權未平倉量（投機氣氛）
   - Meme Stock 熱度（投機炒作跡象）

7. **情緒預測與位階判斷**
   - 情緒歷史分位數（當前情緒在過去 1 年/3 年/5 年的位置）
   - 情緒-價格背離偵測（情緒與價格走勢不一致）
   - 情緒轉折點預測（基於歷史模式）

---

## 適用場景

### 應使用本模組的情境

**市場整體情緒評估：**
- 「市場現在是貪婪還是恐慌？」
- 「是否有極端情緒可以做逆向投資？」
- 「散戶與法人在做什麼？」

**個股籌碼與情緒分析：**
- 「這支股票的籌碼健康嗎？」
- 「融資融券比率異常嗎？」
- 「法人持續買超還是賣超？」
- 「是否有過度投機跡象？」

**短線情緒轉折判斷：**
- 「VIX 突然飆升，是恐慌性殺盤嗎？」
- 「Fear & Greed Index 到達極端值了嗎？」
- 「Put/Call Ratio 是否顯示過度悲觀？」

**社群與媒體情緒監測：**
- 「市場對這支股票的評價如何？」
- 「社群是否出現過度樂觀？」
- 「新聞情緒是正面還是負面？」

**資金流向與避險需求：**
- 「資金是否快速流向避險資產？」
- 「黃金與美元是否同步上漲（風險迴避）？」
- 「ETF 資金流是否顯示風格轉換？」

### 觸發關鍵詞範例

**情緒指標：**
- VIX、恐慌指數、Fear & Greed、Put/Call Ratio
- 市場情緒、貪婪、恐慌、投機、過熱

**籌碼面：**
- 融資融券、券資比、法人買賣超、外資動向
- 散戶、主力、大戶、內部人交易、放空比例
- GEX、暴力盤、軋空

**資金流向：**
- 避險資產、黃金、美元、ETF 資金流
- 風險偏好、風險迴避、資金撤退

**社群情緒：**
- 社群媒體、新聞情緒、Reddit、Twitter、PTT
- 熱度、討論度、Meme Stock

**逆向投資：**
- 逆向機會、極端情緒、反市場、反轉

### 不適用情境

- 公司基本面深度分析 → 使用 `equity-fundamental-analysis`
- 總體經濟環境評估 → 使用 `macro-market-analysis`
- 產業趨勢研判 → 使用 `industry-research`
- 估值與目標價計算 → 使用 `valuation-analysis`

---

## 執行流程

### Step 1: 情境識別與分析範圍確定

**1.1 解析使用者問題**

識別問題類型：

- 市場整體情緒？→ 需要宏觀情緒指標（VIX、Fear & Greed、Put/Call）
- 個股籌碼分析？→ 需要融資融券、法人動向、Short Interest
- 短線情緒轉折？→ 需要即時指標（VIX、GEX、避險資產流向）
- 社群情緒監測？→ 需要新聞與社群媒體分析
- 逆向投資機會？→ 需要情緒極端值與歷史比對

**1.2 確定分析範圍**

- **地理範圍：** 全球市場 / 美股 / 台股 / 特定市場
- **時間範圍：** 即時（當日）/ 近 1 週 / 近 1 月 / 近 3 月
- **分析層級：** 市場整體 / 產業板塊 / 個股
- **關注重點：** 恐慌情緒 / 投機過熱 / 籌碼健康 / 社群情緒

**1.3 建立數據蒐集檢查清單**

根據問題類型，確定需要蒐集的數據：

```
□ 恐慌指標：VIX、Fear & Greed Index、Put/Call Ratio
□ 籌碼面：融資融券、法人買賣超、Institutional Ownership、Short Interest、GEX
□ 資金流向：ETF 資金流、黃金、美元 DXY、國債
□ 分析師共識：評級分布、評級變化、目標價共識
□ 社群媒體：新聞情緒、Reddit/Twitter 熱度、PTT Stock
□ 散戶行為：新開戶數、零股交易量、選擇權未平倉
□ 歷史對比：情緒分位數、歷史極端值、情緒-價格背離
```

---

### Step 2: 恐慌與貪婪指標追蹤

**目標：** 量化市場整體情緒，識別極端恐慌或貪婪

#### 2.1 VIX 恐慌指數

**數據來源：** [CBOE VIX Index](https://www.cboe.com/tradable_products/vix/)

**解讀標準：**
- VIX < 12：極度自滿（歷史低檔，過度樂觀）
- VIX 12-15：低波動（市場平穩）
- VIX 15-20：正常波動
- VIX 20-30：緊張情緒升溫（警戒）
- VIX 30-40：恐慌模式（可能是逢低佈局機會）
- VIX > 40：極度恐慌（歷史級恐慌，強烈逆向信號）

**進階分析：**
- 計算當前 VIX 在過去 1 年/3 年/5 年的歷史分位數
- 觀察 VIX 快速變化（單日漲幅 > 20% = 恐慌性拋售）
- VIX 期貨溢價/逆價（Contango/Backwardation）

**詳細解讀：** 參考 `references/sentiment/vix-interpretation-guide.md`

#### 2.2 CNN Fear & Greed Index

**數據來源：** [CNN Fear & Greed Index](https://edition.cnn.com/markets/fear-and-greed)

**七大子指標：**
1. 市場動能（S&P 500 vs 125 日均線）
2. 股價強度（52 週新高 vs 新低數量）
3. 股價廣度（上漲股票數量）
4. Put/Call Ratio
5. VIX
6. 市場需求（避險資產 vs 風險資產）
7. 垃圾債利差

**評分標準：**
- 0-20：極度恐慌 → 🟢 逆向投資機會
- 21-40：恐慌 → 🟡 謹慎佈局
- 41-60：中性 → 🟡 正常持有
- 61-80：貪婪 → 🔴 謹慎追高
- 81-100：極度貪婪 → 🔴 高風險區，考慮減碼

**極端點短線反轉策略：**
- 當 Fear & Greed < 20 且連續 3 天不再下降 → 可能形成短線底部
- 當 Fear & Greed > 80 且開始回落 → 可能形成短線頂部

**詳細策略：** 參考 `references/sentiment/fear-greed-reversal-strategy.md`

#### 2.3 Put/Call Ratio

**數據來源：** [CBOE Total Put/Call Ratio](https://www.cboe.com/tradable_products/vix/)

**解讀標準：**
- Ratio > 1.2：極度悲觀（買 Put 避險需求極高，逆向信號）
- Ratio 1.0-1.2：偏向悲觀
- Ratio 0.7-1.0：中性
- Ratio 0.5-0.7：偏向樂觀
- Ratio < 0.5：極度樂觀（投機氛圍過熱，警訊）

**選擇權偏多偏空過熱訊號：**
- Equity Put/Call Ratio（股票選擇權）：更反映個股情緒
- Index Put/Call Ratio（指數選擇權）：更反映市場整體情緒

**進階分析：**
- 觀察 Put/Call Ratio 與股價背離（Ratio 上升但股價上漲 = 警訊）
- 比較近 1 週 vs 近 1 月 vs 歷史平均

**詳細解讀：** 參考 `references/sentiment/put-call-ratio-guide.md`

---

### Step 3: 籌碼面與大戶持倉分析

**目標：** 追蹤散戶、法人與大戶的持倉變化，判斷籌碼健康度

#### 3.1 融資融券分析（台股專用）

**數據來源：** [證交所融資融券餘額](https://www.twse.com.tw/)

**關鍵指標：**
- **融資餘額：** 散戶樂觀指標（融資增加 = 散戶看多）
- **融券餘額：** 散戶悲觀指標（融券增加 = 散戶看空）
- **券資比：** 融券餘額 / 融資餘額
  - < 10%：過度樂觀（散戶一面倒看多，警訊）
  - 10-30%：正常範圍
  - > 30%：過度悲觀（可能軋空，逆向機會）

**健康籌碼特徵：**
- 股價上漲 + 融資減少 + 法人買超 = 健康上漲
- 股價下跌 + 融資增加 + 法人賣超 = 不健康下跌（散戶接刀）

**警訊籌碼特徵：**
- 股價上漲 + 融資暴增 + 法人賣超 = 散戶追高，可能見頂
- 融資餘額創新高但股價不再創新高 = 背離，警訊

**詳細分析：** 參考 `references/sentiment/margin-trading-analysis.md`

#### 3.2 法人買賣超（台股專用）

**數據來源：** [證交所法人買賣超](https://www.twse.com.tw/)

**三大法人：**
1. **外資：** 資金最大，方向最重要
2. **投信：** 較長期持有，關注連續買超
3. **自營商：** 短線操作，參考價值較低

**健康訊號：**
- 外資連續 5 日以上買超 + 股價上漲
- 投信連續買超（籌碼集中，較不易被洗出）

**警訊：**
- 外資連續賣超但股價仍上漲（散戶撐盤，不持久）
- 外資與投信同步大量賣超（機構一致看空）

**進階追蹤：**
- 外資持股比例變化趨勢（持續增加 vs 持續減少）
- 投信持股集中度（前十大投信持股佔比）

**詳細分析：** 參考 `references/sentiment/institutional-flow-taiwan.md`

#### 3.3 Institutional Ownership（美股專用）

**數據來源：** [Finviz](https://finviz.com/)、[Yahoo Finance](https://finance.yahoo.com/)、[WhaleWisdom](https://whalewisdom.com/)

**關鍵指標：**
- **Institutional Ownership %：** 機構持股比例
  - > 70%：高度機構化（波動較小，穩定）
  - 30-70%：正常範圍
  - < 30%：散戶為主（波動較大）

**Insider Trading（內部人交易）：**
- Insider Buying（內部人買進）：看好公司前景（正面信號）
- Insider Selling（內部人賣出）：需判斷是例行性賣出還是大量拋售

**詳細解讀：** 參考 `references/sentiment/institutional-ownership-analysis.md`

#### 3.4 Short Interest（放空比例）

**數據來源：** [Finviz](https://finviz.com/)、[MarketBeat](https://www.marketbeat.com/)

**解讀標準：**
- Short Interest < 5%：低度懷疑（正常）
- Short Interest 5-10%：中度放空
- Short Interest 10-20%：高度看空
- Short Interest > 20%：極度看空（但可能軋空）

**軋空機會識別：**
- Short Interest > 20% + 正面消息/業績超預期 = 可能軋空
- Days to Cover > 5 天（放空回補需要時間，軋空力道更強）

**詳細策略：** 參考 `references/sentiment/short-squeeze-detection.md`

#### 3.5 GEX（Gamma Exposure）

**數據來源：** [SqueezeMetrics](https://squeezemetrics.com/)、[SpotGamma](https://spotgamma.com/)

**核心概念：**
- GEX 衡量選擇權市場對標的價格的「推動力」或「壓制力」
- Positive GEX：造市商需要對沖，壓制波動（區間盤）
- Negative GEX：造市商加劇波動（暴力盤、單邊走勢）

**暴力盤與軋空觀察：**
- Negative GEX + 大量 Call OI（未平倉量）= 可能暴力上漲
- Negative GEX + 大量 Put OI = 可能暴力下跌
- Zero Gamma Level：GEX 由正轉負的臨界點，容易形成支撐或壓力

**進階應用：**
- 結合 VIX 與 Put/Call Ratio 判斷暴力盤方向
- 觀察主力選擇權部位變化（Call/Put OI 變化）

**詳細解讀：** 參考 `references/sentiment/gex-gamma-exposure-guide.md`

---

### Step 4: 資金流向與避險情緒

**目標：** 追蹤資金在風險資產與避險資產間的快速轉換

#### 4.1 ETF 資金流向（引用第一階段）

**數據來源：** 引用第一階段「跨資產資金流追蹤」結果

**觀察重點：**
- 股票 ETF 大幅淨流出 + 債券/黃金 ETF 淨流入 = 風險迴避
- 科技股 ETF 流出 + 價值股 ETF 流入 = 風格快速轉換
- 單日或單週資金流異常變化（> 平均值 2 倍標準差）

**資金風格快速轉換觀察：**
- Growth vs Value ETF 資金流對比
- Small Cap vs Large Cap ETF 資金流對比

**詳細解讀：** 參考第一階段 `references/cross-asset-fund-flow.md`

#### 4.2 黃金短線避險流入

**數據來源：** [GLD ETF 資金流](https://www.etfdb.com/etf/GLD/)、[COMEX Gold Futures](https://www.cmegroup.com/)

**風險迴避立即反應指標：**
- GLD ETF 單日淨流入 > $500M = 強烈避險需求
- COMEX Gold 期貨未平倉量快速增加 = 機構避險
- 黃金價格 + 美元 DXY 同步上漲 = 極度風險迴避（罕見）

**進階判斷：**
- 黃金 vs 實質利率（TIPS）的背離
- 黃金 vs 比特幣（新型避險資產）資金流對比

**詳細分析：** 參考 `references/sentiment/gold-safe-haven-flow.md`

#### 4.3 美元指數 DXY 快速變動

**數據來源：** [Investing.com DXY](https://www.investing.com/indices/usdollar)

**風險偏好/撤退訊號：**
- DXY 單日上漲 > 1%：資金撤退新興市場/風險資產
- DXY 快速下跌：資金流向風險資產（新興市場、股市）
- DXY 與 S&P 500 負相關性增強 = 避險需求升溫

**進階觀察：**
- DXY vs 日圓（JPY）vs 瑞士法郎（CHF）三大避險貨幣對比
- DXY 與 EM ETF（新興市場 ETF）資金流反向驗證

**詳細解讀：** 參考 `references/sentiment/dxy-risk-sentiment.md`

#### 4.4 國債殖利率與價格

**數據來源：** [US Treasury Yield Curve](https://www.treasury.gov/)

**避險需求指標：**
- 10 年期美債殖利率快速下降 = 避險需求（債券價格上漲）
- 2 年期 vs 10 年期利差（Yield Curve）倒掛加深 = 衰退恐慌

---

### Step 5: 分析師共識追蹤

**目標：** 追蹤專業分析師的評級變化，識別共識轉向

#### 5.1 評級分布與變化

**數據來源：** [TipRanks](https://www.tipranks.com/)、[Yahoo Finance](https://finance.yahoo.com/)、[Seeking Alpha](https://seekingalpha.com/)

**評級分布：**
- Strong Buy / Buy / Hold / Sell / Strong Sell 比例
- 計算「看多比例」：(Strong Buy + Buy) / 總評級數

**共識評分：**
- 看多比例 > 80%：一致看多（可能過度樂觀，警訊）
- 看多比例 60-80%：偏多共識
- 看多比例 40-60%：中性分歧
- 看多比例 20-40%：偏空共識
- 看多比例 < 20%：一致看空（可能過度悲觀，逆向機會）

#### 5.2 評級變化速度

**警訊信號：**
- 近 1 週快速升評 > 5 次：可能追高
- 近 1 週快速降評 > 5 次：可能恐慌性降評

**健康信號：**
- 穩定升評（每月 1-2 次，持續 3 個月以上）
- 評級穩定（無大幅波動）

#### 5.3 目標價共識

**數據分析：**
- 分析師平均目標價 vs 當前價
- 安全邊際 = (平均目標價 - 當前價) / 當前價

**解讀：**
- 安全邊際 > 30%：分析師一致看好（但需警惕過度樂觀）
- 安全邊際 10-30%：合理上漲空間
- 安全邊際 < 10%：上漲空間有限
- 安全邊際 < 0：當前價已超越目標價（過熱）

**詳細分析：** 參考 `references/sentiment/analyst-consensus-tracking.md`

---

### Step 6: 社群與媒體情緒挖掘（深度分析）

**目標：** 透過 NLP 分析新聞與社群媒體，量化市場情緒極端值

#### 6.1 新聞情緒 NLP 分析

**數據來源：**
- Google News API / Bing News API
- 財經媒體：CNBC、Bloomberg、Reuters、Yahoo Finance
- 台灣媒體：鉅亨網、經濟日報、工商時報

**執行步驟：**

1. **搜尋近 7 天/30 天新聞**
   - 搜尋關鍵字：公司名稱 / 產業關鍵字
   - 蒐集標題與摘要（節省 token）

2. **NLP 情緒評分**
   - 使用情緒分析工具（如 Claude 內建能力）
   - 對每篇新聞評分：正面（+1）、中性（0）、負面（-1）
   - 計算整體情緒分數：(正面新聞數 - 負面新聞數) / 總新聞數

3. **關鍵字頻率分析**
   - 正面關鍵字：「看好」「突破」「創新高」「強勁」「超預期」
   - 負面關鍵字：「危機」「暴跌」「警告」「下修」「虧損」
   - 中性關鍵字：「持平」「觀望」「整理」

4. **情緒極端值偵測**
   - 正面新聞比例 > 80%：媒體一致看好（可能過度樂觀）
   - 負面新聞比例 > 80%：媒體一致看壞（可能過度悲觀，逆向機會）

**詳細方法：** 參考 `references/sentiment/news-sentiment-nlp.md`

#### 6.2 社群媒體情緒追蹤

**數據來源：**

**美股：**
- [Reddit WallStreetBets](https://www.reddit.com/r/wallstreetbets/)
- [StockTwits](https://stocktwits.com/)
- Twitter/X（搜尋 $TICKER）

**台股：**
- [PTT Stock 板](https://www.ptt.cc/bbs/Stock/)
- [Mobile01 投資理財](https://www.mobile01.com/)

**執行步驟：**

1. **搜尋標的討論熱度**
   - 關鍵字搜尋（公司名稱、股票代號）
   - 計算討論量（近 7 天 vs 近 30 天平均）

2. **情緒分類與評分**
   - 看多貼文（含「買進」「看好」「YOLO」「to the moon」）
   - 看空貼文（含「放空」「看衰」「崩盤」「泡沫」）
   - 中性貼文
   - 計算看多比例：看多貼文數 / 總貼文數

3. **Meme Stock 炒作偵測**
   - 討論量暴增（> 平均值 5 倍）+ 散戶一致看多 = 投機炒作警訊
   - 使用情緒極端值 + 基本面背離判斷泡沫風險

4. **情緒極端值警訊**
   - 社群看多比例 > 90%：過度樂觀（散戶 FOMO，可能見頂）
   - 社群看空比例 > 90%：過度悲觀（可能是逆向機會）

**進階分析：**
- 區分「散戶」vs「專業投資人」發言（根據帳號歷史與發言品質）
- 追蹤「意見領袖」（KOL）的觀點變化

**詳細方法：** 參考 `references/sentiment/social-media-sentiment-analysis.md`

---

### Step 7: 散戶行為監測

**目標：** 追蹤散戶進場與投機氛圍

#### 7.1 散戶狂熱指標

**台股：**
- **新開戶數：** 券商新開戶數激增 = 散戶進場高峰（警訊）
- **零股交易量：** 零股交易量暴增 = 散戶積極參與
- **選擇權未平倉量：** 選擇權 OI 創新高 = 投機氛圍過熱

**美股：**
- **Robinhood 持倉變化：** 散戶平台持倉集中度
- **零股交易量（Fractional Shares）：** 散戶參與度

**警訊信號：**
- 新開戶數創歷史新高 + 市場已連續上漲數月 = 散戶追高（可能見頂）
- 選擇權 OI 暴增 + 高槓桿投機 = 過度投機

**詳細分析：** 參考 `references/sentiment/retail-investor-behavior.md`

---

### Step 8: 情緒預測與位階判斷

**目標：** 預測情緒轉折點，判斷當前情緒歷史位置

#### 8.1 情緒歷史分位數

**計算方法：**
- 蒐集過去 1 年/3 年/5 年的情緒分數歷史數據
- 計算當前情緒分數在歷史數據中的分位數

**解讀：**
- 歷史分位數 < 10%：極度恐慌（歷史低檔，強烈逆向信號）
- 歷史分位數 10-30%：偏向恐慌
- 歷史分位數 30-70%：正常範圍
- 歷史分位數 70-90%：偏向貪婪
- 歷史分位數 > 90%：極度貪婪（歷史高檔，警訊）

#### 8.2 情緒-價格背離偵測

**背離類型：**

**頂背離（警訊）：**
- 價格創新高 + 情緒分數不再創新高
- VIX 上升 + 股價上漲

**底背離（逆向機會）：**
- 價格創新低 + 情緒分數不再創新低
- VIX 下降 + 股價下跌

**背離確認：**
- 連續 2 週以上背離 = 背離確認
- 背離 + 成交量萎縮 = 反轉信號增強

#### 8.3 情緒轉折點預測

**基於歷史模式：**
- 尋找歷史上相似的情緒模式（極端情緒 → 反轉）
- 計算平均反轉時間（極端情緒後多久反轉）

**轉折點觸發條件：**
- 情緒分數到達極端值（< 20 或 > 80）
- 連續 3 天不再創新極端值
- 出現初步反轉信號（價格止跌/止漲、成交量放大）

**預測輸出：**
- 反轉機率（基於歷史相似情境）
- 預估反轉時間範圍（1-2 週內 / 2-4 週內）

**詳細方法：** 參考 `references/sentiment/sentiment-prediction-framework.md`

---

### Step 9: 綜合情緒評分與操作建議

**目標：** 整合所有情緒指標，產出 0-100 綜合情緒評分與具體操作建議

#### 9.1 情緒評分系統（0-100 分）

**評分維度與權重：**

| 維度 | 權重 | 評分標準 | 數據來源 |
|------|------|---------|---------|
| 恐慌指標 | 25% | 0（極度恐慌）~ 100（極度貪婪）| VIX、Fear & Greed、Put/Call |
| 籌碼面 | 25% | 0（極度悲觀）~ 100（極度樂觀）| 融資融券、法人動向、Short Interest、GEX |
| 分析師共識 | 20% | 0（一致看空）~ 100（一致看多）| 評級分布、評級變化 |
| 社群/媒體情緒 | 15% | 0（極度負面）~ 100（極度正面）| 新聞 NLP、社群情緒 |
| 散戶行為 | 15% | 0（散戶恐慌）~ 100（散戶狂熱）| 新開戶數、零股交易、選擇權 OI |

**綜合情緒分數計算：**

```
綜合情緒分數 = 
(恐慌指標分數 × 0.25) + 
(籌碼面分數 × 0.25) + 
(分析師共識分數 × 0.20) + 
(社群/媒體情緒分數 × 0.15) + 
(散戶行為分數 × 0.15)

最終分數範圍：0 ~ 100
```

**評分細節：** 參考 `references/sentiment/sentiment-scoring-methodology.md`

#### 9.2 綜合情緒分數解讀

| 分數範圍 | 情緒狀態 | 市場特徵 | 建議 |
|---------|---------|---------|------|
| 0-20 | 極度恐慌 😱 | VIX 飆升、資金撤退、媒體一致看空 | 🟢 逆向投資機會（分批進場）|
| 21-40 | 偏向恐慌 😟 | 情緒悲觀、籌碼鬆動、避險需求升溫 | 🟡 謹慎佈局（基本面好的標的）|
| 41-60 | 中性 😐 | 情緒平穩、籌碼健康、無明顯極端 | 🟡 正常持有，按計畫執行 |
| 61-80 | 偏向貪婪 😊 | 情緒樂觀、散戶積極、分析師看多 | 🔴 謹慎追高，考慮部分獲利了結 |
| 81-100 | 極度貪婪 🤑 | 媒體一致看多、散戶狂熱、投機過熱 | 🔴 高風險區，建議減碼 |

#### 9.3 操作建議矩陣

**結合情緒面與基本面：**

| 情緒面 | 基本面優 | 基本面中 | 基本面差 |
|--------|---------|---------|---------|
| 極度恐慌（0-20） | 🟢 **積極買進** | 🟡 逢低佈局 | 🔴 避免（可能有基本面惡化）|
| 偏向恐慌（20-40） | 🟢 **分批買進** | 🟡 小額試單 | 🔴 觀望 |
| 中性（40-60） | 🟢 持有 | 🟡 持有 | 🔴 減碼 |
| 偏向貪婪（60-80） | 🟡 持有/部分獲利 | 🔴 獲利了結 | 🔴 **賣出** |
| 極度貪婪（80-100） | 🔴 **獲利了結** | 🔴 **賣出** | 🔴 **賣出** |

**黃金法則：**
- 當「情緒極端（< 20 或 > 80）+ 基本面未惡化」→ 最佳逆向投資機會
- 當「情緒與價格背離」→ 潛在反轉信號，密切追蹤

#### 9.4 反市場操作機會提示

**逆向投資機會識別（需滿足以下條件之一）：**

1. **極度恐慌 + 基本面優質**
   - 綜合情緒分數 < 20
   - 第三階段基本面評分 > 7/10
   - 第四階段估值顯示低估（安全邊際 > 30%）
   - → 🟢 **強烈買進信號**

2. **情緒-價格底背離**
   - 價格創新低，但情緒分數不再創新低
   - VIX 開始下降但股價尚未反彈
   - → 🟢 **潛在底部，謹慎佈局**

3. **媒體與社群一致看空**
   - 新聞負面比例 > 80%
   - 社群看空比例 > 80%
   - 但基本面與估值無明顯惡化
   - → 🟢 **過度悲觀，逆向機會**

**投機過熱警訊（需滿足以下條件之一）：**

1. **極度貪婪 + 估值過高**
   - 綜合情緒分數 > 80
   - 第四階段估值顯示高估（當前價 > 樂觀目標價）
   - → 🔴 **強烈賣出信號**

2. **散戶狂熱 + Meme Stock 炒作**
   - 社群討論量暴增（> 平均值 5 倍）
   - 散戶一致看多（> 90%）
   - 基本面無明顯支撐
   - → 🔴 **投機泡沫，遠離**

3. **情緒-價格頂背離**
   - 價格創新高，但情緒分數不再創新高
   - VIX 上升但股價仍上漲
   - → 🔴 **潛在頂部，考慮減碼**

**詳細策略：** 參考 `references/sentiment/contrarian-investing-framework.md`

---

## 輸出格式

### 簡要結論（Summary）

```markdown
## 市場情緒分析摘要

**分析日期：** YYYY-MM-DD  
**分析標的：** [市場整體 / 特定產業 / 個股代碼]

---

### 📊 綜合情緒評分：XX/100（情緒狀態）

| 維度 | 評分 | 狀態 | 關鍵發現 |
|------|------|------|---------|
| 恐慌指標 | XX/100 | 😊/😐/😟 | VIX XX，Fear & Greed XX |
| 籌碼面 | XX/100 | 😊/😐/😟 | 融資 XX 億，法人買超 XX 億 |
| 分析師共識 | XX/100 | 😊/😐/😟 | 看多比例 XX% |
| 社群情緒 | XX/100 | 😊/😐/😟 | 正面新聞 XX%，社群熱度 XX |
| 散戶行為 | XX/100 | 😊/😐/😟 | 新開戶數 XX，零股交易 XX |

---

### 🎯 操作建議

🟢/🟡/🔴 **[積極買進 / 分批買進 / 持有 / 獲利了結 / 賣出]**

**理由（3-5 句話）：**
[整合情緒分析結果，說明當前市場情緒特徵與建議理由]

---

### 🔥 反市場機會

✅ **發現逆向投資機會**（或 ❌ 目前無明顯逆向投資機會）

[若有逆向機會，說明條件與建議]

---

### 📈 情緒位階與預測

- **歷史分位數：** XX%（過去 3 年）
- **情緒-價格背離：** ✅ 偵測到 / ❌ 無背離
- **轉折點預測：** [1-2 週內可能反轉 / 情緒仍將持續]

---

### ⚠️ 風險提示

[列出 2-3 項關鍵風險或警訊]

---

**下一步追蹤重點：**
- [追蹤項目 1]
- [追蹤項目 2]
- [追蹤項目 3]
```

### 詳細報告（Detail）

當使用者需要更詳細的分析時，產出完整報告：

**完整報告結構：**

1. **市場層面情緒儀表板**
   - VIX、Fear & Greed、Put/Call Ratio 詳細解讀
   - 資金流向與避險資產動態

2. **產業層面情緒分布**
   - 各產業情緒評分對比
   - 產業輪動情緒變化

3. **個股籌碼與分析師追蹤**
   - 融資融券詳細數據
   - 法人買賣超趨勢
   - Short Interest 與 GEX 分析
   - 分析師評級變化

4. **社群與媒體情緒摘要**
   - 新聞情緒 NLP 分析結果
   - 社群熱度與情緒分類
   - Meme Stock 炒作偵測

5. **歷史情緒與價格對比**
   - 情緒歷史分位數
   - 情緒-價格背離分析
   - 歷史相似情境比對

6. **情緒預測與轉折點判斷**
   - 情緒轉折點預測
   - 反轉機率與時間範圍

7. **操作建議與風險管理**
   - 具體進場點位與倉位建議
   - 停損與停利設定
   - 動態調整觸發條件

**詳細報告範本：** 參考 `references/sentiment/sentiment-report-template.md`

---

## 參考資料體系

### 核心方法論（必讀）

**情緒指標解讀：**
- `references/sentiment/vix-interpretation-guide.md` - VIX 恐慌指數完整解讀
- `references/sentiment/fear-greed-reversal-strategy.md` - Fear & Greed 極端點反轉策略
- `references/sentiment/put-call-ratio-guide.md` - Put/Call Ratio 詳細解讀

**籌碼面分析：**
- `references/sentiment/margin-trading-analysis.md` - 融資融券分析方法（台股）
- `references/sentiment/institutional-flow-taiwan.md` - 法人買賣超分析（台股）
- `references/sentiment/institutional-ownership-analysis.md` - 機構持倉分析（美股）
- `references/sentiment/short-squeeze-detection.md` - 軋空機會識別
- `references/sentiment/gex-gamma-exposure-guide.md` - GEX 與暴力盤分析

**資金流向：**
- `references/sentiment/gold-safe-haven-flow.md` - 黃金避險資金流分析
- `references/sentiment/dxy-risk-sentiment.md` - 美元指數風險情緒解讀

**分析師與社群：**
- `references/sentiment/analyst-consensus-tracking.md` - 分析師共識追蹤方法
- `references/sentiment/news-sentiment-nlp.md` - 新聞情緒 NLP 分析
- `references/sentiment/social-media-sentiment-analysis.md` - 社群媒體情緒挖掘

**散戶行為：**
- `references/sentiment/retail-investor-behavior.md` - 散戶行為監測指標

**情緒預測：**
- `references/sentiment/sentiment-prediction-framework.md` - 情緒預測與轉折點判斷
- `references/sentiment/sentiment-scoring-methodology.md` - 情緒評分計算方法

**逆向投資：**
- `references/sentiment/contrarian-investing-framework.md` - 逆向投資框架
- `references/sentiment/behavioral-finance-principles.md` - 行為金融學應用

### 數據來源與工具

**數據來源清單：**
- `references/sentiment/data-sources.md` - 完整數據來源與 API 指引

**實用工具：**
- `references/sentiment/sentiment-dashboard-template.md` - 情緒儀表板範本
- `references/sentiment/contrarian-opportunity-checklist.md` - 逆向機會檢查清單
- `references/sentiment/sentiment-report-template.md` - 完整報告範本

---

## 外部資源（精選）

### 情緒指標數據源

**恐慌與貪婪：**
- [CBOE VIX Index](https://www.cboe.com/tradable_products/vix/)
- [CNN Fear & Greed Index](https://edition.cnn.com/markets/fear-and-greed)
- [CBOE Put/Call Ratio](https://www.cboe.com/tradable_products/vix/)

**籌碼面（台股）：**
- [證交所融資融券](https://www.twse.com.tw/)
- [證交所法人買賣超](https://www.twse.com.tw/)

**籌碼面（美股）：**
- [Finviz](https://finviz.com/)
- [Yahoo Finance](https://finance.yahoo.com/)
- [WhaleWisdom 13F](https://whalewisdom.com/)
- [SqueezeMetrics GEX](https://squeezemetrics.com/)

**資金流向：**
- [ETFdb 資金流](https://www.etfdb.com/)
- [Investing.com DXY](https://www.investing.com/indices/usdollar)

**分析師共識：**
- [TipRanks](https://www.tipranks.com/)
- [Seeking Alpha](https://seekingalpha.com/)

**社群媒體：**
- [Reddit WallStreetBets](https://www.reddit.com/r/wallstreetbets/)
- [StockTwits](https://stocktwits.com/)
- [PTT Stock 板](https://www.ptt.cc/bbs/Stock/)

---

## 常見問題

**Q1: 情緒分析與技術分析有什麼不同？**

情緒分析聚焦「投資人行為與心理」，技術分析聚焦「價格與成交量」。兩者互補：
- 情緒極端時（< 20 或 > 80），技術分析容易失效
- 技術指標超買/超賣 + 情緒極端 = 更強的反轉信號

**Q2: 何時應該使用逆向投資策略？**

當滿足以下條件時：
1. 情緒分數到達極端值（< 20 或 > 80）
2. 基本面與估值未明顯惡化（第三、四階段確認）
3. 出現情緒-價格背離
4. 媒體與社群一致看多/看空

**Q3: 社群情緒分析會不會太主觀？**

本模組採用量化方法：
- 新聞情緒：NLP 自動評分，計算正負面比例
- 社群情緒：計算看多/看空貼文比例，而非主觀判斷
- 最終整合多個客觀指標，降低單一來源偏誤

**Q4: 如何處理情緒分析與基本面矛盾？**

優先順序：基本面 > 估值 > 情緒

- 基本面惡化 + 情緒極度恐慌 → 避免接刀（可能繼續下跌）
- 基本面優質 + 情緒極度恐慌 → 逆向投資機會
- 基本面惡化 + 情緒極度貪婪 → 強烈賣出信號

**Q5: 多久更新一次情緒分析？**

建議頻率：
- 短線交易：每日更新（關注 VIX、Put/Call、GEX）
- 中線投資：每週更新（關注法人動向、分析師共識）
- 長線投資：每月更新（關注整體情緒趨勢）

**Q6: GEX 如何影響短線操作？**

- **Positive GEX：** 造市商壓制波動，適合區間操作（低買高賣）
- **Negative GEX：** 造市商加劇波動，適合趨勢追蹤（順勢操作）
- **Zero Gamma Level：** 關鍵支撐/壓力位，突破後容易加速

---

## 版本記錄

### v1.0.0 (2026-01-18)

**初版功能：**
- ✅ 建立五大核心分析模組（恐慌指標、籌碼面、資金流向、分析師共識、社群情緒）
- ✅ 整合 0-100 綜合情緒評分系統
- ✅ 深度社群情緒 NLP 分析
- ✅ 情緒預測與歷史分位數判斷
- ✅ 情緒-價格背離偵測
- ✅ 逆向投資機會識別框架
- ✅ GEX（Gamma Exposure）暴力盤分析
- ✅ 完整參考文檔體系（15+ 文檔）
- ✅ 混合模式數據取得（官方免費數據 + 手動搜尋補充）

**核心特色：**
- 短線情緒追蹤（VIX、Fear & Greed、Put/Call、GEX、避險資產流向）
- 台股與美股雙市場支援
- 漸進式揭露設計（核心流程在 SKILL.md，細節在 references）
- AI agent 自主選擇最佳分析路徑

---

**免責聲明：**

本技能提供的情緒分析與操作建議僅供參考，不構成投資建議。市場情緒瞬息萬變，歷史模式不代表未來表現。投資決策應基於個人風險承受能力、完整研究與專業諮詢。情緒極端時往往伴隨高波動與不確定性，請謹慎管理風險。
