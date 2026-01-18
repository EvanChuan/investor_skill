# 本地端執行指南：SHA-384 保護 + 中文轉英文

## 📋 前置準備

### 1. 確認您的環境

開啟終端機（Terminal）並執行：

```bash
# 檢查 Python 版本（需要 3.6 或以上）
python --version
# 或
python3 --version

# 檢查 Git
git --version
```

### 2. Clone Repository 到本地

```bash
# 如果還沒 clone
git clone https://github.com/EvanChuan/investor_skill.git
cd investor_skill

# 如果已經 clone，確保是最新版本
git pull origin main
```

---

## 🔧 步驟一：生成 SHA-384 雜湊值

### 1.1 建立完整性管理腳本

在 `investor_skill/` 根目錄建立 `generate_integrity.py`：

```python
#!/usr/bin/env python3
"""
Generate SHA-384 integrity hashes for all markdown files
"""

import hashlib
import json
from pathlib import Path
from datetime import datetime

def calculate_sha384(file_path):
    """Calculate SHA-384 hash"""
    sha384 = hashlib.sha384()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha384.update(chunk)
    return sha384.hexdigest()

def generate_integrity():
    """Generate integrity.json for all markdown files in skills/"""

    skills_dir = Path('skills')

    if not skills_dir.exists():
        print("❌ Error: 'skills' directory not found!")
        print("Please run this script from the repository root.")
        return

    # Find all markdown files
    markdown_files = sorted(skills_dir.rglob('*.md'))

    print(f"Found {len(markdown_files)} markdown files\n")

    integrity_data = {
        "version": "1.0.0",
        "generated_at": datetime.now().isoformat(),
        "algorithm": "sha384",
        "files": []
    }

    for md_file in markdown_files:
        file_path = str(md_file).replace('\\', '/')
        file_size = md_file.stat().st_size
        sha384_hash = calculate_sha384(md_file)

        integrity_data['files'].append({
            "path": file_path,
            "sha384": sha384_hash,
            "size": file_size
        })

        print(f"✓ {file_path}")
        print(f"  SHA-384: {sha384_hash}\n")

    # Save integrity.json
    with open('integrity.json', 'w', encoding='utf-8') as f:
        json.dump(integrity_data, f, indent=2, ensure_ascii=False)

    print(f"{'='*80}")
    print(f"✅ Successfully generated integrity.json")
    print(f"✅ Total files protected: {len(integrity_data['files'])}")
    print(f"{'='*80}")

if __name__ == '__main__':
    generate_integrity()
```

### 1.2 執行腳本生成 integrity.json

```bash
# 在 investor_skill/ 根目錄執行
python generate_integrity.py
# 或
python3 generate_integrity.py
```

執行成功後，會在根目錄生成 `integrity.json` 檔案。

---

## 📝 步驟二：中文轉英文（保持輸出中文）

### 2.1 建立轉換輔助腳本

建立 `convert_to_english.py`：

```python
#!/usr/bin/env python3
"""
Helper script to convert Chinese markdown to English while maintaining Chinese output
"""

from pathlib import Path

def add_bilingual_header(content, file_path):
    """Add bilingual instruction header to markdown"""

    # Skip if already has the header
    if 'output_language: zh-TW' in content:
        return content

    header = '''---
language: en
output_language: zh-TW
---

<!-- ⚠️ CRITICAL INSTRUCTION ⚠️ -->
**When using this skill, you MUST generate ALL responses in Traditional Chinese (繁體中文).**

This English documentation is designed for AI model comprehension.
All analysis, reports, and outputs should be written in Chinese for end users.
<!-- END INSTRUCTION -->

'''

    # Remove existing front matter if present
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = '---'.join(parts[2:]).lstrip()

    return header + content

def process_skill_file(file_path):
    """Add bilingual header to a skill markdown file"""

    print(f"Processing: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    updated_content = add_bilingual_header(content, file_path)

    # Create backup
    backup_path = file_path.parent / f"{file_path.stem}.backup{file_path.suffix}"
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✓ Backup created: {backup_path}")

    # Save updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"  ✓ Updated with bilingual header\n")

def main():
    """Process all SKILL.md files in skills directory"""

    skills_dir = Path('skills')

    if not skills_dir.exists():
        print("❌ Error: 'skills' directory not found!")
        return

    # Find all SKILL.md files
    skill_files = sorted(skills_dir.rglob('SKILL.md'))

    print(f"{'='*80}")
    print(f"Found {len(skill_files)} SKILL.md files")
    print(f"{'='*80}\n")

    for skill_file in skill_files:
        process_skill_file(skill_file)

    print(f"{'='*80}")
    print(f"✅ Completed! {len(skill_files)} files processed")
    print(f"\n⚠️  IMPORTANT NEXT STEPS:")
    print(f"1. Review the updated files")
    print(f"2. Manually translate section headers and instructions to English")
    print(f"3. Keep examples and case studies in Chinese")
    print(f"4. Test with Claude to ensure output is still in Chinese")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
```

### 2.2 執行轉換（添加雙語指令）

```bash
python convert_to_english.py
```

這會為所有 `SKILL.md` 檔案加入雙語指令區塊。

### 2.3 手動翻譯內容

現在您需要**手動**將各個 SKILL.md 的內容翻譯成英文。我建議使用 Claude 協助：

**範例流程：**

```bash
# 1. 開啟第一個檔案
code skills/macro-market-analysis/SKILL.md
# 或用任何文字編輯器

# 2. 將中文內容貼給 Claude，請求翻譯：
"請將以下 Skill 說明翻譯成英文，但保留：
1. 前面的 YAML front matter 和 CRITICAL INSTRUCTION
2. 所有範例（Examples）保持中文
3. 專有名詞第一次出現時加中文註解

[貼上您的中文內容]"

# 3. 將翻譯結果貼回檔案
```

---

## ✅ 步驟三：驗證完整性

### 3.1 建立驗證腳本

建立 `verify_integrity.py`：

```python
#!/usr/bin/env python3
"""Verify file integrity against integrity.json"""

import hashlib
import json
from pathlib import Path

def calculate_sha384(file_path):
    sha384 = hashlib.sha384()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha384.update(chunk)
    return sha384.hexdigest()

def verify():
    if not Path('integrity.json').exists():
        print("❌ integrity.json not found!")
        return 1

    with open('integrity.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"{'='*80}")
    print(f"Skill Files Integrity Verification")
    print(f"Algorithm: {data['algorithm'].upper()}")
    print(f"Total files: {len(data['files'])}")
    print(f"{'='*80}\n")

    passed = failed = missing = 0

    for file_info in data['files']:
        path = Path(file_info['path'])
        expected = file_info['sha384']

        if not path.exists():
            print(f"✗ MISSING: {path}")
            missing += 1
            continue

        actual = calculate_sha384(path)

        if actual == expected:
            print(f"✓ PASS: {path}")
            passed += 1
        else:
            print(f"✗ FAIL: {path}")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")
            failed += 1

    print(f"\n{'='*80}")
    print(f"✓ Passed: {passed} | ✗ Failed: {failed} | ? Missing: {missing}")
    print(f"{'='*80}")

    return 0 if (failed == 0 and missing == 0) else 1

if __name__ == '__main__':
    exit(verify())
```

### 3.2 執行驗證

```bash
# 驗證檔案完整性
python verify_integrity.py
```

---

## 🔄 步驟四：更新 integrity.json

翻譯完成後，需要重新生成雜湊值：

```bash
# 重新生成 integrity.json（包含更新後的檔案）
python generate_integrity.py

# 驗證新的雜湊值
python verify_integrity.py
```

---

## 📤 步驟五：提交到 GitHub

### 5.1 檢查變更

```bash
# 查看修改了哪些檔案
git status

# 查看具體變更內容
git diff skills/
```

### 5.2 提交變更

```bash
# 加入所有變更
git add integrity.json
git add generate_integrity.py
git add verify_integrity.py
git add convert_to_english.py
git add skills/

# 提交
git commit -m "feat: Add SHA-384 integrity protection and English documentation

- Add integrity.json with SHA-384 hashes for all markdown files
- Add generate_integrity.py for hash generation
- Add verify_integrity.py for integrity verification
- Convert skill documentation to English while maintaining Chinese output
- Add bilingual headers to all SKILL.md files"

# 推送到 GitHub
git push origin main
```

---

## 🧪 步驟六：測試 Claude 輸出

### 6.1 在 Claude 中測試

上傳更新後的 SKILL.md 到 Claude，測試：

```
請使用 macro-market-analysis skill 分析當前美國經濟狀況
```

**預期結果：** Claude 應該輸出中文分析報告，即使 Skill 內容是英文。

### 6.2 驗證雙語功能

如果 Claude 輸出英文，檢查：
1. SKILL.md 頂端是否有 `output_language: zh-TW`
2. CRITICAL INSTRUCTION 是否明確說明要用中文輸出

---

## 📊 完整操作檢查清單

- [ ] Clone repository 到本地
- [ ] 建立 `generate_integrity.py`
- [ ] 執行生成 `integrity.json`
- [ ] 建立 `convert_to_english.py`
- [ ] 執行添加雙語指令
- [ ] 手動翻譯 4 個主要 SKILL.md 為英文
- [ ] 翻譯 references 目錄下的重要檔案
- [ ] 重新生成 `integrity.json`
- [ ] 執行 `verify_integrity.py` 確認無誤
- [ ] 提交到 GitHub
- [ ] 測試 Claude 輸出仍為中文

---

## ⚠️ 常見問題

### Q: Python 版本錯誤？
```bash
# 如果 python 指向 Python 2.x，改用：
python3 generate_integrity.py
python3 verify_integrity.py
```

### Q: 找不到 skills 目錄？
確保您在 `investor_skill/` 根目錄執行腳本：
```bash
pwd  # 應該顯示 .../investor_skill
ls   # 應該看到 skills/ 目錄
```

### Q: 如何只翻譯部分檔案？
可以先翻譯最重要的 4 個 SKILL.md：
```bash
skills/macro-market-analysis/SKILL.md
skills/industry-research/SKILL.md
skills/equity-fundamental-analysis/SKILL.md
skills/valuation-analysis/SKILL.md
```

其他 references 可以分批處理。

---

## 🎯 建議順序

### Day 1: 基礎保護
1. 生成 integrity.json ✅
2. 提交到 GitHub

### Day 2-3: 主要檔案翻譯
3. 翻譯 4 個主要 SKILL.md
4. 測試 Claude 輸出

### Week 2: 完整翻譯
5. 翻譯所有 references/*.md
6. 更新 integrity.json
7. 設定 GitHub Branch Protection

---

**準備好了嗎？從建立第一個腳本開始！** 🚀
