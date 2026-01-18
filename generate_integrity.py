#!/usr/bin/env python3
"""
Generate SHA-384 integrity hashes for all markdown files in skills directory
Author: EvanChuan
Date: 2026-01-16
"""

import hashlib
import json
from pathlib import Path
from datetime import datetime

def calculate_sha384(file_path):
    """Calculate SHA-384 hash of a file"""
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
        print("Expected location: investor_skill/")
        return

    # Find all markdown files
    markdown_files = sorted(skills_dir.rglob('*.md'))

    print(f"{'='*80}")
    print(f"Generating SHA-384 Integrity Hashes")
    print(f"{'='*80}")
    print(f"Found {len(markdown_files)} markdown files\n")

    integrity_data = {
        "version": "1.0.0",
        "generated_at": datetime.now().isoformat(),
        "algorithm": "sha384",
        "repository": "EvanChuan/investor_skill",
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
        print(f"  Hash: {sha384_hash[:32]}...")

    # Save integrity.json
    output_file = 'integrity.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(integrity_data, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*80}")
    print(f"✅ Successfully generated {output_file}")
    print(f"✅ Total files protected: {len(integrity_data['files'])}")
    print(f"📅 Generated at: {integrity_data['generated_at']}")
    print(f"{'='*80}")
    print(f"\n💡 Next step: Run 'python verify_integrity.py' to test verification")

if __name__ == '__main__':
    generate_integrity()
