# 跨資產價格輪動（Cross-Asset Price Rotation）

> 本文件為 `macro-market-analysis` **Step 8A：Cross-Asset Price Rotation** 的執行參考。
> **真實資金流**（ETF 申贖、COT 持倉、機構評級）請見 `cross-asset-fund-flow.md`。
> 核心原則：**價格輪動不等於真實資金流。兩者必須分開命名、分開驗證。**

---

## 一、定位與命名紀律

本模組觀察的是**價格的相對表現與排名變化**，而非資金的實際進出。

### ✅ 正確命名

> **Price Rotation / Relative Strength（價格輪動 / 相對強弱）**

### ❌ 不得直接稱為「資金流入」

以下現象**都只是價格證據**，不足以宣稱資金流入：

- Rank 前進
- 60D% 上升
- REL60 轉為正值
- 60-Day Trend 轉為 Up

要宣稱「資金流入」，必須由 `cross-asset-fund-flow.md` 的 ETF 淨申購、COT 淨部位或機構評級變化佐證。

> **為什麼重要：** 價格上漲可能來自空單回補、流動性不足下的少量買盤、或指數再平衡，與真實資金配置無關。混用兩者會造成錯誤的高信度判斷。

---

## 二、主要工具：全市場觀察表 ⭐

🔗 **全市場觀察表（Google 試算表）：**
`https://docs.google.com/spreadsheets/d/1OMbg5nPRELu7cpkVrGR9CppMyUhjebpShk17n4wyhZA/edit?usp=sharing`

> 每次執行 Step 8A 時，直接透過上方連結讀取最新數據。

---

## 三、表格涵蓋資產類別（100+ ETF）

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

---

## 四、欄位解讀指南 ⭐

| 欄位 | 含義 | 解讀方式 |
|------|------|---------|
| `1D% / 5D%` | 短期價格動能 | 識別近期急漲/急跌 |
| `20D% / 60D%` | 中期價格動能 | 確認趨勢強度與持續性 |
| `60-Day Trend` | 60 日趨勢方向 | Up / Down / Flat |
| `20R / 60R / 120R` | 相對強弱排名（20/60/120 日） | 數字越小排名越前，價格表現越強 |
| `Rank` | 綜合排名 | 整體相對強弱排序 |
| `REL5/20/60/120` | 相對大盤表現 | 正值＝跑贏市場，負值＝跑輸市場 |
| `From 2025-12-31` | YTD 年初至今報酬 | 年度輪動全貌 |

---

## 五、輪動判讀邏輯 ⭐

| 訊號組合 | 判讀 |
|---------|------|
| Rank 前段 ＋ 60D% 持續正 ＋ 60-Day Trend = Up | **強勢資產**，價格輪動確認（仍需資金流佐證） |
| Rank 後段 ＋ 60D% 持續負 ＋ REL60 負值 | **弱勢資產**，相對表現落後，迴避 |
| 20R 突然大幅上升（排名躍升）＋ 1D/5D% 明顯正 | **輪動起步**，觀察是否持續 2-3 週再確認 |
| REL60 由負轉正且連續 4 週維持 | 中期相對強弱翻轉，信度較高 |
| 比較 EWT（台灣）vs EWY（韓國）vs QQQ | 半導體 / 科技的區域輪動方向 |

### 判讀順序

1. 先看 `Rank` 與 `60-Day Trend` 定位**中期趨勢**
2. 再看 `REL60 / REL120` 確認**是否真的跑贏大盤**（避免把大盤 Beta 誤認為個別強勢）
3. 最後看 `1D/5D% + 20R` 找**剛啟動的輪動**
4. 交叉比對 `cross-asset-fund-flow.md`，確認是否有真實資金支持

---

## 六、核心輪動觀察組

以下配對用於判讀市場風險偏好與循環位置：

| 觀察組 | 意涵 |
|-------|------|
| **SPY vs QQQ vs RSP vs IWM** | 大型 vs 科技 vs 等權重 vs 小型 — RSP/IWM 落後代表市場寬度惡化 |
| **Cyclical vs Defensive** | 週期（XLI/XLB/XLF）vs 防禦（XLU/XLP/XLV）— 景氣預期的價格投射 |
| **Growth vs Value** | 成長 vs 價值 — 對利率與久期的敏感度 |
| **High Beta vs Low Volatility** | SPHB vs SPLV — 最直接的風險偏好溫度計 |
| **HYG vs LQD vs TLT** | 高收益 vs 投資級 vs 公債 — 信用循環的即時價格投射 |
| **EWT vs EWY vs QQQ** | 台灣 vs 韓國 vs 那斯達克 — 半導體區域輪動 |
| **GLD vs DXY vs 10Y 實質利率** | 黃金的三角驗證 — 黃金漲但實質利率也漲＝去美元化敘事 |
| **BTC vs QQQ vs 淨流動性** | 比特幣作為流動性的高 Beta 代理 |

---

## 七、標準輸出範本

```markdown
### 跨資產價格輪動（Step 8A）

| 資產 | Rank | 60D% | REL60 | 60D Trend | 價格輪動判讀 |
|------|-----:|-----:|------:|-----------|------------|
| | | | | | |

**輪動觀察組：**
- 風險偏好（High Beta vs Low Vol）：
- 市場寬度（SPY vs RSP vs IWM）：
- 信用價格投射（HYG vs LQD vs TLT）：
- 半導體區域（EWT vs EWY vs QQQ）：

**本期最明顯的輪動方向：** [由 A 輪向 B]
**待資金流驗證項目：** [列出需 cross-asset-fund-flow.md 佐證的標的]
```

---

## 八、與 `cross-asset-fund-flow.md` 的分工

| 項目 | 本文件（Step 8A） | cross-asset-fund-flow.md（Step 8B） |
|------|-----------------|----------------------------------|
| 觀察對象 | 價格、排名、相對強弱 | ETF 淨申贖、COT 持倉、機構評級 |
| 資料頻率 | 每日 | 每週（COT 週五）／每月（機構） |
| 時效 | 即時 | 落後 3-7 天 |
| 用途 | 發現輪動、排序強弱 | 驗證輪動是否有真實資金支持 |
| 單獨使用 | ❌ 不可宣稱資金流 | ✅ 可宣稱資金流 |

### 交叉驗證矩陣

| 價格輪動 | 真實資金流 | 判讀 |
|---------|-----------|------|
| 強 | 流入 | ✅ 高信度趨勢 |
| 強 | 流出 | ⚠️ 軋空、供給不足或追價風險 |
| 弱 | 流入 | ⚠️ 可能在吸收賣壓，等待轉折 |
| 弱 | 流出 | 🔴 高信度弱勢 |

---

## 九、分析紀律

1. 價格輪動**永遠不可單獨宣稱為資金流入/流出**。
2. 單日排名跳動不具意義，至少觀察 5-10 個交易日。
3. 低流動性 ETF（成交量小）的排名變化雜訊高，需降權處理。
4. REL 為相對大盤，大盤本身大跌時「跑贏」不等於絕對報酬為正，須同時報 60D% 絕對值。
5. 商品 ETF（USO、UNG）存在換倉損耗（contango），長期報酬與現貨價格會顯著偏離，不可直接當商品價格看。

---

## 十、關聯文件

- `../SKILL.md` — macro-market-analysis 主技能（Step 8A 觸發點）
- `cross-asset-fund-flow.md` — 真實資金流追蹤完整 SOP（Step 8B）
- `narrative-vs-reality.md` — 市場確認（Market Confirmation）章節使用本表輸出
- `credit-cycle.md` — HYG/LQD/TLT 的信用循環意涵
- `industry-cycles.md` — 產業輪動與循環對應
