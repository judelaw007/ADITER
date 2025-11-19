#!/usr/bin/env python3
"""
Convert markdown files in generated_notes/08_Leasing/quality_checked to DOCX
Uses the create_enhanced_docx.py functions
"""

import os
import sys
from pathlib import Path
from create_enhanced_docx import create_enhanced_document

def convert_markdown_files():
    """Convert all markdown files in the leasing directory"""

    # Define the source directory
    source_dir = Path('generated_notes/08_Leasing/quality_checked')

    # Check if directory exists
    if not source_dir.exists():
        print(f"❌ Error: Directory {source_dir} does not exist")
        return False

    # Find all markdown files
    md_files = sorted(source_dir.glob('*.md'))

    if not md_files:
        print(f"❌ No markdown files found in {source_dir}")
        return False

    print(f"📁 Found {len(md_files)} markdown files to convert:\n")

    converted_count = 0

    for md_file in md_files:
        try:
            # Read markdown content
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract title from filename
            title = md_file.stem.replace('_', ' ')

            # Create output filename
            docx_filename = str(source_dir / f"{md_file.stem}.docx")

            # Create enhanced document
            create_enhanced_document(content, title, docx_filename)
            converted_count += 1

        except Exception as e:
            print(f"❌ Error converting {md_file.name}: {str(e)}")
            continue

    print(f"\n✅ Successfully converted {converted_count}/{len(md_files)} files")
    return converted_count > 0

if __name__ == '__main__':
    success = convert_markdown_files()
    sys.exit(0 if success else 1)
