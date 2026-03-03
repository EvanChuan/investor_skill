# SKILL.md 文件大小優化建議

## 現狀分析（2026-Q1）

| 模組 | 行數 | 大小 | 狀態 |
|---|---|---|---|
| macro-market-analysis | 761 | 24 KB | ⚠️ 選先優化 |
| equity-fundamental-analysis | 536 | 15.3 KB | ⚠️ 選先優化 |
| industry-research | 514 | 14.6 KB | ⚠️ 建議精簡 |
| valuation-analysis | - | - | 待查 |
| market-sentiment-tracking | - | - | 待查 |
| technical-analysis | - | - | 待查 |
| risk-management | 88 | 2.1 KB | ✅ 理想大小 |

**目標：** 每個 SKILL.md 目標大小 **5-8 KB 以內**（對應 150-250 行）

---

## 優化原則

> **SKILL.md 的定位是 AI 執行送代碼，不是完整知識庫。**
> 內容應聚焦於「做什麼」和「怎麼做」，詳細知識實例放到 references/。

### 原則 1：移出詳細參考資料
- 大型資料表格（如 16 大資產類別）→ `references/` 目錄
- 完整範例輸出（markdown 範例內容）→ `references/` 目錄
- 外部資源連結清單 → `references/data-sources.md`

### 原則 2：移出版本歷史
- 完整版本記錄 → `CHANGELOG.md`（每個模組內）
- SKILL.md 只保留最新版本號和日期

### 原則 3：精簡 Step 說明
- 每個 Step 以 2-5 行說明核心行動
- 詳細分析方法參考對應 `references/` 文件
- 避免在 SKILL.md 中嵌入大型代碼塊

### 原則 4：移出 FAQ
- FAQ 移至 `docs/faq.md` 或各模組的 `references/` 目錄

### 原則 5：移出使用指南
- 新手/進階/專家分級內容 → `docs/getting-started.md`

---

## macro-market-analysis/SKILL.md 具體優化方案

**目前 24 KB → 目標 8 KB**

### 可移除內容（約 -12 KB）

| 內容區塊 | 目前大小 | 方案 |
|---|---|---|
| Step 5.1 　16 大資產表格、ETF/CFTC 對映表 | ~2 KB | 移至 `references/cross-asset-fund-flow.md` |
| Step 8.2 資產配置議完整輸出範例 | ~2 KB | 移至 `references/analysis-report-template.md` |
| Step 10 Risk Radar 完整月報輸出格式 | ~1.5 KB | 移至 `references/risk-radar-sop.md` |
| 版本歷史 v1.0 ~ v2.1 | ~2 KB | 移至 `CHANGELOG.md` |
| FAQ 完整內容 + 三點範例 | ~2 KB | 移至 `references/faq-macro.md` |
| 使用指南三階段 | ~1 KB | 移至 `docs/getting-started.md` |

### 保留在 SKILL.md 的內容
- frontmatter（name, description, version, tags）
- 模組概述 + 核心理念
- 適用場景 + 觸發關鍵詞
- 執行流程概要（每 Step 2-5 行）
- 參考資料出口清單（不含外部連結）
- 最新版本號

---

## equity-fundamental-analysis/SKILL.md 優化建議

**目前 15.3 KB → 目標 6-7 KB**

### 可移除內容
- 財務比率完整公式表格 → `references/financial-ratios.md`
- SWOT 分析範例輸出 → `references/analysis-templates.md`
- 版本歷史 → `CHANGELOG.md`
- 婉極分類詳細說明 → `references/moat-framework.md`

---

## industry-research/SKILL.md 優化建議

**目前 14.6 KB → 目標 6-7 KB**

### 可移除內容
- 產業景氣循環詳細對照表 → `references/industry-cycles.md`
- 全球產業分布地圖 → `references/sector-map.md`
- 版本歷史 → `CHANGELOG.md`

---

## 優化執行順序

1. **P0** macro-market-analysis （-16 KB 效益最大）
2. **P1** equity-fundamental-analysis （-8 KB）
3. **P2** industry-research （-8 KB）
4. **P3** 其餘模組（按需優化）

---

*最後更新：2026-03-03*
