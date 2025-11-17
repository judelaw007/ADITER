#!/usr/bin/env python3
"""
Script to convert all MD files in the Tax and Fiscal Regimes quality_checked directory to DOCX
"""

import os
import sys
from pathlib import Path
from create_enhanced_docx import create_enhanced_document

# Define the source directory
SOURCE_DIR = Path("generated_notes/02_Tax_and_fiscal_regimes/quality_checked")
WORD_DOCS_DIR = SOURCE_DIR / "word_docs"

def get_title_from_filename(filename):
    """Extract a clean title from the markdown filename"""
    # Remove .md extension and replace underscores with spaces
    name = filename.replace('.md', '')
    # Clean up the name for use as a title
    return name.replace('_', ' ')

def convert_md_files():
    """Convert all MD files in the source directory to DOCX"""

    # Ensure source directory exists
    if not SOURCE_DIR.exists():
        print(f"❌ Source directory not found: {SOURCE_DIR}")
        return False

    # Create word_docs directory if it doesn't exist
    WORD_DOCS_DIR.mkdir(exist_ok=True)
    print(f"📁 Created/verified word_docs directory: {WORD_DOCS_DIR}")

    # Find all MD files
    md_files = sorted(SOURCE_DIR.glob("*.md"))

    if not md_files:
        print("❌ No MD files found in the source directory")
        return False

    print(f"\n📝 Found {len(md_files)} MD files to convert:\n")

    converted_count = 0
    for md_file in md_files:
        try:
            print(f"Converting: {md_file.name}")

            # Read the markdown file
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Get title from filename
            title = get_title_from_filename(md_file.name)

            # Create output filename
            output_filename = str(WORD_DOCS_DIR / md_file.stem) + ".docx"

            # Create the document
            create_enhanced_document(content, title, output_filename)
            converted_count += 1

        except Exception as e:
            print(f"❌ Error converting {md_file.name}: {str(e)}")
            continue

    print(f"\n✅ Successfully converted {converted_count}/{len(md_files)} files")
    return converted_count == len(md_files)

if __name__ == '__main__':
    success = convert_md_files()
    sys.exit(0 if success else 1)
