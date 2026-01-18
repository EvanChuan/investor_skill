# 🚀 快速開始指南

## 第一步：準備工作（5 分鐘）

### 1. 開啟終端機（Terminal）

**Mac/Linux:**
- 按 `Cmd + Space`，輸入 "Terminal"

**Windows:**
- 按 `Win + R`，輸入 "cmd" 或 "powershell"

### 2. 進入您的 repository 目錄

```bash
# 如果還沒 clone，先 clone
git clone https://github.com/EvanChuan/investor_skill.git

# 進入目錄
cd investor_skill

# 確認位置正確（應該看到 skills 資料夾）
ls
```

---

## 第二步：下載並放置腳本（2 分鐘）

從這個對話中下載以下 4 個檔案，放到 `investor_skill/` 根目錄：

1. ✅ `generate_integrity.py`
2. ✅ `verify_integrity.py`
3. ✅ `convert_to_english.py`
4. ✅ `LOCAL_SETUP_GUIDE.md`

放置後，您的目錄結構應該像這樣：

```
investor_skill/
├── skills/
│   ├── macro-market-analysis/
│   ├── industry-research/
│   ├── equity-fundamental-analysis/
│   └── valuation-analysis/
├── generate_integrity.py          ← 新增
├── verify_integrity.py             ← 新增
├── convert_to_english.py           ← 新增
└── LOCAL_SETUP_GUIDE.md            ← 新增
```

---

## 第三步：生成 SHA-384 雜湊值（1 分鐘）

在終端機中執行：

```bash
# 生成 integrity.json
python generate_integrity.py
```

**預期輸出：**
```
================================================================================
Generating SHA-384 Integrity Hashes
================================================================================
Found 42 markdown files

✓ skills/macro-market-analysis/SKILL.md
  Hash: 223f41dff49e03b2541c9e111e53fe3c...
✓ skills/industry-research/SKILL.md
  Hash: bb14b971c1675326327106758ccfb5b9...
...

================================================================================
✅ Successfully generated integrity.json
✅ Total files protected: 42
================================================================================
```

**結果：**會在根目錄生成 `integrity.json` 檔案。

---

## 第四步：驗證功能（30 秒）

測試驗證腳本是否正常工作：

```bash
python verify_integrity.py
```

**預期輸出：**
```
================================================================================
Skill Files Integrity Verification
================================================================================
Algorithm: SHA384
Total files: 42
================================================================================

✓ PASS: skills/macro-market-analysis/SKILL.md
✓ PASS: skills/industry-research/SKILL.md
...

================================================================================
✓ Passed: 42 | ✗ Failed: 0 | ? Missing: 0
✅ All files verified successfully! No tampering detected.
```

---

## 第五步：添加雙語指令（2 分鐘）

為所有 SKILL.md 加入雙語指令區塊：

```bash
python convert_to_english.py
```

**預期輸出：**
```
================================================================================
Adding Bilingual Headers to SKILL.md Files
================================================================================
Found 4 SKILL.md files

Processing: skills/macro-market-analysis/SKILL.md
  ✓ Backup created: skills/macro-market-analysis/.backup/SKILL.backup.md
  ✓ Added bilingual header

Processing: skills/industry-research/SKILL.md
  ✓ Backup created: skills/industry-research/.backup/SKILL.backup.md
  ✓ Added bilingual header
...

✅ Completed! 4/4 files updated
```

**結果：**
- 每個 SKILL.md 前面會加入英文指令區塊
- 原始檔案會備份到 `.backup/` 目錄

---

## 第六步：手動翻譯（需要時間）

現在您需要將 SKILL.md 的內容翻譯成英文。建議流程：

### 選項 A：使用 Claude 協助翻譯（推薦）

1. 開啟 `skills/macro-market-analysis/SKILL.md`
2. 複製**雙語指令之後**的所有中文內容
3. 貼給 Claude（我），請求翻譯：

```
請幫我將以下投資分析 Skill 翻譯成英文：

要求：
1. 保留檔案開頭的 YAML front matter 和 CRITICAL INSTRUCTION
2. 標題和說明翻譯成英文
3. 範例（Example）保持中文
4. 專有名詞第一次出現時用括號加中文，如 "GDP (國內生產總值)"

[貼上您的中文內容]
```

4. 將翻譯結果貼回檔案
5. 儲存

### 選項 B：分批處理

如果時間有限，可以先翻譯最重要的檔案：

**優先順序：**
1. `skills/macro-market-analysis/SKILL.md` ⭐⭐⭐
2. `skills/industry-research/SKILL.md` ⭐⭐⭐
3. `skills/equity-fundamental-analysis/SKILL.md` ⭐⭐
4. `skills/valuation-analysis/SKILL.md` ⭐⭐

其他 `references/*.md` 可以之後再翻譯。

---

## 第七步：更新雜湊值（30 秒）

翻譯完成後，重新生成 integrity.json：

```bash
# 重新生成（包含更新後的檔案）
python generate_integrity.py

# 驗證新的雜湊值
python verify_integrity.py
```

---

## 第八步：提交到 GitHub（2 分鐘）

```bash
# 查看變更
git status

# 加入所有檔案
git add .

# 提交
git commit -m "feat: Add SHA-384 protection and bilingual documentation

- Add integrity.json with SHA-384 hashes
- Add integrity management scripts
- Add bilingual headers to SKILL.md files
- Prepare for English translation"

# 推送
git push origin main
```

---

## 第九步：測試 Claude 輸出（1 分鐘）

在 Claude 中上傳您更新後的 SKILL.md，測試：

```
請使用 macro-market-analysis skill 分析當前美國經濟狀況
```

**預期：** Claude 應該輸出中文分析報告。

如果輸出英文，檢查 SKILL.md 頂端的指令是否正確。

---

## ✅ 完成檢查清單

完成以下項目即算完成基礎保護：

- [ ] 下載 4 個腳本檔案到本地
- [ ] 執行 `generate_integrity.py` 生成雜湊值
- [ ] 執行 `verify_integrity.py` 驗證成功
- [ ] 執行 `convert_to_english.py` 添加雙語指令
- [ ] 翻譯至少 1 個 SKILL.md 為英文
- [ ] 重新生成 integrity.json
- [ ] 提交到 GitHub
- [ ] 測試 Claude 輸出仍為中文

---

## 🆘 遇到問題？

### 問題 1: "python: command not found"

**解決：**
```bash
# 改用 python3
python3 generate_integrity.py
```

### 問題 2: "找不到 skills 目錄"

**解決：**
```bash
# 確認當前目錄
pwd

# 應該在 investor_skill/ 根目錄
# 如果不是，cd 到正確位置
cd /path/to/investor_skill
```

### 問題 3: Claude 還是輸出英文

**解決：**檢查 SKILL.md 頂端是否有：
```markdown
---
output_language: zh-TW
---

<!-- ⚠️ CRITICAL INSTRUCTION ⚠️ -->
**When using this skill, you MUST generate ALL responses in Traditional Chinese (繁體中文).**
```

---

## 📞 需要協助？

如果需要我幫您翻譯特定的 SKILL.md，請直接貼上內容！

---

**預估總時間：** 
- 基礎設定：15 分鐘
- 翻譯 1 個 SKILL.md：30 分鐘
- 翻譯全部：2-3 小時（可分批進行）

**現在就開始第一步吧！** 🎯
