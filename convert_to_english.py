#!/usr/bin/env python3
"""
Add bilingual headers to SKILL.md files
This prepares files for English translation while maintaining Chinese output
Author: EvanChuan
Date: 2026-01-16
"""

from pathlib import Path
import shutil
from datetime import datetime

def add_bilingual_header(content, file_path):
    """Add bilingual instruction header to markdown"""

    # Skip if already has the header
    if 'output_language: zh-TW' in content:
        print(f"  ⚠️  Already has bilingual header, skipping...")
        return None

    header = """---
language: en
output_language: zh-TW
last_updated: """ + datetime.now().strftime('%Y-%m-%d') + """
---

<!-- ⚠️ CRITICAL INSTRUCTION ⚠️ -->
**When using this skill, you MUST generate ALL responses in Traditional Chinese (繁體中文).**

This English documentation is designed for AI model comprehension.
All analysis, reports, and outputs should be written in Chinese for end users.
<!-- END INSTRUCTION -->

"""

    # Remove existing front matter if present
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = '---'.join(parts[2:]).lstrip()

    return header + content

def process_skill_file(file_path):
    """Add bilingual header to a skill markdown file"""

    print(f"\nProcessing: {file_path}")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        updated_content = add_bilingual_header(original_content, file_path)

        if updated_content is None:
            return False

        # Create backup
        backup_dir = file_path.parent / '.backup'
        backup_dir.mkdir(exist_ok=True)
        backup_path = backup_dir / f"{file_path.stem}.backup.md"

        shutil.copy2(file_path, backup_path)
        print(f"  ✓ Backup created: {backup_path}")

        # Save updated file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"  ✓ Added bilingual header")

        return True

    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    """Process all SKILL.md files in skills directory"""

    skills_dir = Path('skills')

    if not skills_dir.exists():
        print("❌ Error: 'skills' directory not found!")
        print("Please run this script from the repository root.")
        return

    # Find all SKILL.md files
    skill_files = sorted(skills_dir.rglob('*.md'))

    print(f"{'='*80}")
    print(f"Adding Bilingual Headers to SKILL.md Files")
    print(f"{'='*80}")
    print(f"Found {len(skill_files)} SKILL.md files")

    processed = 0
    for skill_file in skill_files:
        if process_skill_file(skill_file):
            processed += 1

    print(f"\n{'='*80}")
    print(f"✅ Completed! {processed}/{len(skill_files)} files updated")
    print(f"{'='*80}")
    print(f"\n📝 IMPORTANT NEXT STEPS:")
    print(f"1. Review the updated files")
    print(f"2. Manually translate section headers and instructions to English")
    print(f"3. Keep examples and case studies in Chinese")
    print(f"4. Test with Claude to ensure output is still in Chinese")
    print(f"5. Run 'python generate_integrity.py' to update hashes")
    print(f"\n💡 Tip: Backups are saved in skills/*/.backup/ directories")
    print(f"{'='*80}")

if __name__ == '__main__':
    main()
