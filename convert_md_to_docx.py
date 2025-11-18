#!/usr/bin/env python3
"""
Script to batch convert markdown files to DOCX format
using the create_enhanced_docx module
"""

import os
import sys
from pathlib import Path

# Add the project root to the path to import create_enhanced_docx
sys.path.insert(0, '/home/user/ADITER')

from create_enhanced_docx import create_enhanced_document

def convert_markdown_files(source_dir, output_dir):
    """
    Convert all markdown files in source_dir to DOCX format in output_dir

    Args:
        source_dir: Directory containing markdown files
        output_dir: Directory to save DOCX files
    """
    source_path = Path(source_dir)
    output_path = Path(output_dir)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    # Find all markdown files
    md_files = sorted(source_path.glob('*.md'))

    if not md_files:
        print(f"❌ No markdown files found in {source_dir}")
        return False

    print(f"Found {len(md_files)} markdown files to convert\n")

    success_count = 0

    for md_file in md_files:
        try:
            # Read markdown content
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract title from filename
            # Remove the .md extension and clean up the name
            title = md_file.stem.replace('_', ' ')

            # Create output filename
            output_filename = str(output_path / f"{md_file.stem}.docx")

            # Convert to DOCX
            print(f"Converting: {md_file.name}")
            create_enhanced_document(content, title, output_filename)
            success_count += 1

        except Exception as e:
            print(f"❌ Error converting {md_file.name}: {str(e)}")
            continue

    print(f"\n✅ Successfully converted {success_count}/{len(md_files)} files")
    return success_count == len(md_files)

if __name__ == '__main__':
    source_directory = '/home/user/ADITER/generated_notes/05_Technical_services/quality_checked'
    output_directory = '/home/user/ADITER/generated_notes/05_Technical_services/quality_checked/word_docs'

    print("Markdown to DOCX Converter")
    print("=" * 50)
    print(f"Source: {source_directory}")
    print(f"Output: {output_directory}\n")

    convert_markdown_files(source_directory, output_directory)
