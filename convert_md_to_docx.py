#!/usr/bin/env python3
"""
Batch converter script to convert all markdown files to DOCX format
Using the create_enhanced_docx module
"""

import os
import sys
from pathlib import Path
from create_enhanced_docx import create_enhanced_document

def convert_directory_md_to_docx(source_dir, output_dir=None):
    """
    Convert all markdown files in a directory to DOCX format

    Args:
        source_dir: Directory containing markdown files
        output_dir: Directory to save DOCX files (defaults to source_dir)
    """

    if output_dir is None:
        output_dir = source_dir

    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Find all markdown files
    source_path = Path(source_dir)
    md_files = list(source_path.glob('*.md'))

    if not md_files:
        print(f"⚠️  No markdown files found in {source_dir}")
        return 0

    print(f"Found {len(md_files)} markdown file(s) to convert")
    print("-" * 50)

    converted_count = 0

    for md_file in sorted(md_files):
        try:
            # Read markdown file
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()

            # Generate output filename
            output_path = Path(output_dir)
            output_filename = str(output_path / (md_file.stem + '.docx'))

            # Extract title from filename (remove prefix and underscores)
            title = md_file.stem.replace('_', ' ')

            # Convert to DOCX
            print(f"\n📄 Converting: {md_file.name}")
            create_enhanced_document(md_content, title, output_filename)
            converted_count += 1

        except Exception as e:
            print(f"❌ Error converting {md_file.name}: {str(e)}")
            continue

    print("\n" + "=" * 50)
    print(f"✅ Successfully converted {converted_count}/{len(md_files)} files")
    return converted_count

if __name__ == '__main__':
    # Directory containing markdown files
    source_directory = '/home/user/ADITER/generated_notes/04_Permanent_establishments/quality_checked'

    print("Markdown to DOCX Batch Converter")
    print("=" * 50)
    print(f"Source directory: {source_directory}")

    # Convert all files in the source directory
    convert_directory_md_to_docx(source_directory)
