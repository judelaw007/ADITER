#!/usr/bin/env python3
"""
Batch convert markdown files to DOCX using create_enhanced_docx.py
"""

import os
import sys
from pathlib import Path

# Import the create_enhanced_document function
from create_enhanced_docx import create_enhanced_document

def extract_title_from_md(md_content):
    """Extract title from markdown content (first # heading)"""
    lines = md_content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return "Untitled Document"

def convert_md_to_docx(md_file_path, output_dir=None):
    """Convert a single markdown file to DOCX"""
    md_path = Path(md_file_path)

    # Read markdown content
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Extract title
    title = extract_title_from_md(md_content)

    # Determine output path
    if output_dir:
        output_path = Path(output_dir) / f"{md_path.stem}.docx"
    else:
        output_path = md_path.with_suffix('.docx')

    # Convert to DOCX
    create_enhanced_document(md_content, title, str(output_path))

    return output_path

def main():
    # Define source directory
    source_dir = Path("generated_notes/05_Technical_services/quality_checked")

    if not source_dir.exists():
        print(f"❌ Error: Directory not found: {source_dir}")
        sys.exit(1)

    # Find all .md files
    md_files = list(source_dir.glob("*.md"))

    if not md_files:
        print(f"❌ No markdown files found in {source_dir}")
        sys.exit(1)

    print(f"Found {len(md_files)} markdown file(s) to convert:")
    for md_file in md_files:
        print(f"  - {md_file.name}")

    print("\n" + "="*60)
    print("Starting conversion...")
    print("="*60 + "\n")

    # Convert each file
    converted_files = []
    for md_file in md_files:
        try:
            output_path = convert_md_to_docx(md_file, source_dir)
            converted_files.append(output_path)
            print(f"✅ Converted: {md_file.name} → {output_path.name}")
        except Exception as e:
            print(f"❌ Error converting {md_file.name}: {str(e)}")

    print("\n" + "="*60)
    print(f"Conversion complete! {len(converted_files)} file(s) converted.")
    print("="*60)

    return converted_files

if __name__ == "__main__":
    main()
