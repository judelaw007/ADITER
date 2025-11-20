#!/usr/bin/env python3
"""
Script to convert markdown files to DOCX with improved performance
"""

import os
import sys
from pathlib import Path

# Add the ADITER directory to the path to import the create_enhanced_docx module
sys.path.insert(0, '/home/user/ADITER')

from create_enhanced_docx import create_enhanced_document

def convert_file(source_file, output_dir):
    """Convert a single markdown file to DOCX"""
    try:
        print(f"📄 Processing: {source_file.name}...", flush=True)

        # Read markdown content
        with open(source_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Extract title from filename (remove number prefix and .md)
        filename_without_ext = source_file.stem
        title = filename_without_ext.split('_', 1)[1].replace('_', ' ')

        # Define output path
        docx_filename = output_dir / f"{source_file.stem}.docx"

        # Create the enhanced document
        create_enhanced_document(markdown_content, title, str(docx_filename))
        print(f"✅ Created: {docx_filename.name}\n", flush=True)
        return True

    except Exception as e:
        print(f"❌ Error converting {source_file.name}: {str(e)}\n", flush=True)
        return False

def main():
    """Convert all markdown files in the quality_checked directory"""

    # Define paths
    source_dir = Path('/home/user/ADITER/generated_notes/14_Arbitration_of_disputes/quality_checked')
    word_docs_dir = source_dir / 'word_docs'

    # Create word_docs directory if it doesn't exist
    word_docs_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ Created/verified directory: {word_docs_dir}\n")

    # Find all markdown files
    md_files = sorted(source_dir.glob('*.md'))

    if not md_files:
        print("❌ No markdown files found in the quality_checked directory")
        return False

    print(f"📋 Found {len(md_files)} markdown file(s) to convert\n")

    # Convert each markdown file
    successful = 0
    failed = 0

    for md_file in md_files:
        if convert_file(md_file, word_docs_dir):
            successful += 1
        else:
            failed += 1

    # Summary
    print("\n" + "="*50)
    print(f"✅ Successfully converted: {successful}/{len(md_files)} files")
    if failed > 0:
        print(f"❌ Failed conversions: {failed}")

    # List created files
    docx_files = sorted(word_docs_dir.glob('*.docx'))
    print(f"\n📊 DOCX files in word_docs directory ({len(docx_files)}):")
    for docx_file in docx_files:
        size_kb = docx_file.stat().st_size / 1024
        print(f"   ✓ {docx_file.name} ({size_kb:.1f} KB)")

    return failed == 0

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
