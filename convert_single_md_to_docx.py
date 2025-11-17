#!/usr/bin/env python3
"""
Script to convert a single markdown file to docx using create_enhanced_docx.py
"""

import sys
import os
from create_enhanced_docx import create_enhanced_document

def convert_md_to_docx(md_file_path, output_dir):
    """
    Convert a markdown file to docx

    Args:
        md_file_path: Path to the markdown file
        output_dir: Directory to save the docx file
    """
    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Extract title from first heading
    title = ""
    for line in markdown_content.split('\n'):
        if line.startswith('# '):
            title = line[2:].strip()
            break

    if not title:
        # Use filename as title
        title = os.path.basename(md_file_path).replace('.md', '').replace('_', ' ')

    # Create output filename
    base_name = os.path.basename(md_file_path).replace('.md', '')
    output_filename = os.path.join(output_dir, f"{base_name}.docx")

    # Create the document
    create_enhanced_document(markdown_content, title, output_filename)

    return output_filename

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python convert_single_md_to_docx.py <md_file_path> <output_dir>")
        sys.exit(1)

    md_file = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.exists(md_file):
        print(f"Error: Markdown file not found: {md_file}")
        sys.exit(1)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = convert_md_to_docx(md_file, output_dir)
    print(f"✅ Conversion complete: {output_file}")
