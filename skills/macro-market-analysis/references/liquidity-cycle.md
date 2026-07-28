# 流動性循環（Liquidity Cycle）

> 本文件為 `macro-market-analysis` **Step 5：Liquidity Cycle** 的執行參考。
> 核心原則：**流動性不是單一數字，必須由五個來源交叉驗證方向與速度。**

---

## 一、五大流動性來源

| # | 來源 | 核心指標 | 發布頻率 | 資料來源 |
|---|------|---------|---------|---------|
| 1 | **央行流動性** | Fed Total Assets（WALCL）、QE / QT 每月縮減速度 | 每週四 | FRED `WALCL` |
| 2 | **財政流動性** | TGA 財政部一般帳戶餘額 | 每日 | FRED `WTREGEN`／Treasury Daily Statement |
| 3 | **貨幣市場緩衝** | ON RRP 隔夜逆回購餘額 | 每日 | FRED `RRPONTSYD`／NY Fed |
| 4 | **銀行體系流動性** | Bank Reserves 準備金、SOFR、EFFR | 每週／每日 | FRED `WRESBAL`、`SOFR`、`EFFR` |
| 5 | **廣義貨幣** | M2 YoY（M1 僅作佐證） | 月度 | FRED `M2SL` |

**閱讀順序：** 先看 (1) 決定總量方向 → 再看 (2)(3) 決定資金被吸走或釋出 → 最後看 (4)(5) 確認是否真的抵達實體與市場。

---

## 二、Net Liquidity 代理指標

```text
Liquidity Proxy = Fed Assets − TGA − ON RRP
```

### ⚠️ 使用限制（必讀）

此公式**只是代理指標（proxy）**，不是市場流動性的精確總量。輸出報告時必須明確標示為「代理指標」。

不能代表的部分：

- 未涵蓋銀行體系的信用創造（放貸才是流動性的主力）
- 未涵蓋境外美元（Eurodollar）與離岸融資市場
- 未涵蓋券商 / 交易商的資產負債表擴張能力
- 未涵蓋外國央行的美債持有變化與 FIMA 回購

**正確用法：** 看它的**方向與變化速度**，不看絕對數值；且必須與 Bank Reserves 同步驗證。

---

## 三、ON RRP 特別判讀規則

**RRP 下降不必然是利多。** 必須先判斷資金流向：

| RRP 變化 | 同時觀察 | 判讀 |
|---------|---------|------|
| RRP ↓ + Bank Reserves ↑ | 準備金上升 | ✅ 真正的流動性釋放，偏正面 |
| RRP ↓ + TGA ↑ | 財政部發債吸金 | ⚠️ 資金被財政部吸收，中性偏空 |
| RRP ↓ + Bank Reserves 同步 ↓ | 兩者齊跌 | 🔴 流動性實質收縮，**不可判定為擴張** |
| RRP 已接近 0 | 緩衝耗盡 | 🔴 後續 QT 將直接侵蝕準備金，壓力顯著上升 |

**關鍵水位參考：** Bank Reserves 佔 GDP 比重跌破約 10-11% 時，通常視為準備金稀缺區（historic scarcity zone），貨幣市場利率易出現尖刺（SOFR − EFFR 利差走闊）。

---

## 四、流動性週期五階段

| 階段 | 特徵 | 典型組合 | 對資產的影響 |
|------|------|---------|------------|
| **修復期** | 危機後央行擴表、準備金回補 | Fed Assets ↑、RRP 低、Reserves ↑ | 高 Beta、長久期資產領漲 |
| **擴張期** | 流動性穩定增加，信用同步放寬 | Net Liquidity ↑、HY OAS 收窄 | 全面 Risk-On，小型股/新興市場跟上 |
| **中性期** | 總量持平，內部結構搬移 | Fed Assets 持平、TGA/RRP 互換 | 輪動為主，指數區間震盪 |
| **收縮期** | QT 持續 + TGA 回補 | Net Liquidity ↓、Reserves ↓ | 高 Beta 走弱，資金集中大型權值 |
| **去槓桿期** | 準備金稀缺 + 融資市場失靈 | SOFR 尖刺、FRA-OIS 擴大 | Risk-Off，現金/短債/黃金相對強勢 |

---

## 五、標準輸出要求

每次執行 Step 5 必須輸出以下四項，缺一不可：

1. **方向** — 擴張 / 中性 / 收縮
2. **速度** — 加速 / 平穩 / 減速（用 4 週與 13 週變化率比較）
3. **主要驅動因子** — 是 Fed 擴縮表？TGA 回補？還是 RRP 耗盡？
4. **傳導影響** — 分別說明對「高 Beta 股票」「長久期資產（長債/成長股）」「信用市場」的預期影響

### 輸出範本

```markdown
### 流動性循環判斷

- **階段：** 收縮期（第 N 個月）
- **方向：** 收縮｜**速度：** 減速中（QT 步伐已放緩）
- **主要驅動因子：** TGA 季底回補 $XXXB 為本期最大吸金來源，QT 為次要
- **Net Liquidity（代理）：** $X.XXT（4 週 −$XXB／13 週 −$XXXB）
- **Bank Reserves：** $X.XXT（佔 GDP XX%）— 尚未進入稀缺區
- **RRP：** $XXB（已接近耗盡，緩衝功能大致喪失）
- **傳導影響：**
  - 高 Beta：承壓，羅素 2000 相對弱勢
  - 長久期：對 10Y 實質利率敏感度上升
  - 信用市場：HY OAS 尚未反映，為主要背離點
```

---

## 六、觀察節奏

| 頻率 | 觀察項目 |
|------|---------|
| **每日** | TGA、ON RRP |
| **每週四** | Fed Total Assets（H.4.1 報表）、Bank Reserves |
| **每日** | SOFR、EFFR、SOFR−EFFR 利差 |
| **月度** | M2 YoY |
| **季度** | 財政部再融資會議（QRA）— 預告未來季度發債節奏與 TGA 目標 |

> **QRA 是季度必看事件：** 發債結構（短債 vs 長債比重）直接決定下一季 TGA 與 RRP 的互動路徑。

---

## 七、常見判讀陷阱

1. ❌ 只看 Net Liquidity 曲線就宣告多空 — 必須同時看 Bank Reserves 是否同向。
2. ❌ 把 RRP 下降一律當利多 — 見第三節。
3. ❌ 把 M2 YoY 轉正當成流動性擴張 — M2 是落後指標，需以 SLOOS 與 C&I Loans 佐證信用是否真的擴張。
4. ❌ 忽略季節性 — TGA 在 4 月報稅季與季底會有規律性大幅波動，非政策訊號。
5. ❌ 把流動性當成唯一多空決定因子 — 流動性在 Macro Score 中權重 20，仍需與信用循環（15）交叉。

---

## 八、關聯文件

- `../SKILL.md` — macro-market-analysis 主技能（Step 5 觸發點）
- `credit-cycle.md` — 信用循環（流動性的下游驗證）
- `fed-policy-framework.md` — Fed 政策決策邏輯與 QE/QT 傳導
- `risk-radar-sop.md` — Risk Radar 定期掃描（含流動性週期定位）
- `economic-indicators-reference.md` — 完整指標總表
