#!/usr/bin/env python3
"""
Verify file integrity against integrity.json
Author: EvanChuan
Date: 2026-01-16
"""

import hashlib
import json
from pathlib import Path
import sys

def calculate_sha384(file_path):
    """Calculate SHA-384 hash of a file"""
    sha384 = hashlib.sha384()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha384.update(chunk)
    return sha384.hexdigest()

def verify():
    """Verify file integrity against integrity.json"""

    integrity_file = 'integrity.json'

    if not Path(integrity_file).exists():
        print(f"❌ Error: {integrity_file} not found!")
        print("Please run 'python generate_integrity.py' first.")
        return 1

    with open(integrity_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"{'='*80}")
    print(f"Skill Files Integrity Verification")
    print(f"{'='*80}")
    print(f"Algorithm: {data['algorithm'].upper()}")
    print(f"Total files: {len(data['files'])}")
    print(f"Generated: {data.get('generated_at', 'N/A')}")
    print(f"{'='*80}\n")

    passed = 0
    failed = []
    missing = []

    for file_info in data['files']:
        path = Path(file_info['path'])
        expected = file_info['sha384']

        if not path.exists():
            print(f"✗ MISSING: {path}")
            missing.append(str(path))
            continue

        actual = calculate_sha384(path)

        if actual == expected:
            print(f"✓ PASS: {path}")
            passed += 1
        else:
            print(f"✗ FAIL: {path}")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")
            failed.append({
                'path': str(path),
                'expected': expected,
                'actual': actual
            })

    # Summary
    print(f"\n{'='*80}")
    print(f"VERIFICATION SUMMARY")
    print(f"{'='*80}")
    print(f"✓ Passed:  {passed}")
    print(f"✗ Failed:  {len(failed)}")
    print(f"? Missing: {len(missing)}")

    if failed:
        print(f"\n⚠️  WARNING: {len(failed)} file(s) have been modified!")
        print(f"These files may have been tampered with or updated.")
        print(f"\nModified files:")
        for fail in failed:
            print(f"  - {fail['path']}")

    if missing:
        print(f"\n⚠️  WARNING: {len(missing)} file(s) are missing!")
        print(f"Missing files:")
        for miss in missing:
            print(f"  - {miss}")

    if not failed and not missing:
        print(f"\n✅ All files verified successfully! No tampering detected.")
        print(f"{'='*80}")
        return 0
    else:
        print(f"\n❌ Verification failed!")
        print(f"{'='*80}")
        return 1

if __name__ == '__main__':
    sys.exit(verify())
