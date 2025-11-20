#!/usr/bin/env python3
"""
Script to convert all markdown files in the Arbitration_of_disputes quality_checked folder to DOCX
"""

import os
import sys
from pathlib import Path

# Add the ADITER directory to the path to import the create_enhanced_docx module
sys.path.insert(0, '/home/user/ADITER')

from create_enhanced_docx import create_enhanced_document

def convert_arbitration_files():
    """Convert all markdown files in the quality_checked directory"""

    # Define paths
    source_dir = Path('/home/user/ADITER/generated_notes/14_Arbitration_of_disputes/quality_checked')
    word_docs_dir = source_dir / 'word_docs'

    # Create word_docs directory if it doesn't exist
    word_docs_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ Created/verified directory: {word_docs_dir}")

    # Find all markdown files
    md_files = sorted(source_dir.glob('*.md'))

    if not md_files:
        print("❌ No markdown files found in the quality_checked directory")
        return False

    print(f"\n📋 Found {len(md_files)} markdown file(s) to convert\n")

    # Convert each markdown file
    for md_file in md_files:
        try:
            print(f"📄 Processing: {md_file.name}")

            # Read markdown content
            with open(md_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()

            # Extract title from filename (remove number prefix and .md)
            filename_without_ext = md_file.stem  # e.g., "67_The_use_of_arbitration_by_natural_energy_resource_companies"
            title = filename_without_ext.split('_', 1)[1].replace('_', ' ')  # Remove number prefix and convert underscores to spaces

            # Define output path
            docx_filename = word_docs_dir / f"{md_file.stem}.docx"

            # Create the enhanced document
            create_enhanced_document(markdown_content, title, str(docx_filename))

        except Exception as e:
            print(f"❌ Error converting {md_file.name}: {str(e)}")
            return False

    print(f"\n✅ All files converted successfully!")
    print(f"📁 DOCX files saved to: {word_docs_dir}")

    # List created files
    docx_files = sorted(word_docs_dir.glob('*.docx'))
    print(f"\n📊 Summary - Created {len(docx_files)} DOCX file(s):")
    for docx_file in docx_files:
        print(f"   ✓ {docx_file.name}")

    return True

if __name__ == '__main__':
    success = convert_arbitration_files()
    sys.exit(0 if success else 1)
