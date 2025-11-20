#!/usr/bin/env python3
"""
Convert all MD files in quality_checked directory to DOCX format
"""
import os
from pathlib import Path
from create_enhanced_docx import create_enhanced_document

# Target directory
target_dir = "/home/user/ADITER/generated_notes/13_Governance_of_natural_energy_resources/quality_checked"

# Find all MD files
md_files = sorted(Path(target_dir).glob("*.md"))

print(f"Found {len(md_files)} markdown files to convert:")
for md_file in md_files:
    print(f"  - {md_file.name}")

print("\nStarting conversion...\n")

for md_file in md_files:
    # Read markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Extract title from filename (remove number prefix and .md)
    filename = md_file.stem
    # Remove leading numbers and underscore: "63_Definition_..." -> "Definition_..."
    title = '_'.join(filename.split('_')[1:]).replace('_', ' ')

    # Create output filename
    output_filename = md_file.with_suffix('.docx')

    try:
        create_enhanced_document(markdown_content, title, str(output_filename))
    except Exception as e:
        print(f"❌ Error converting {md_file.name}: {str(e)}")

print("\n✅ All conversions complete!")
