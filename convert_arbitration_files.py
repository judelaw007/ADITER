#!/usr/bin/env python3
"""
Script to convert markdown files in 14_Arbitration_of_disputes/quality_checked to DOCX format
"""

import os
import sys
from pathlib import Path
from create_enhanced_docx import create_enhanced_document

# Define source and output directories
source_dir = Path("generated_notes/14_Arbitration_of_disputes/quality_checked")
output_dir = source_dir / "word_docs"

# Create output directory if it doesn't exist
output_dir.mkdir(parents=True, exist_ok=True)
print(f"✅ Created/verified output directory: {output_dir}")

# Find all markdown files
md_files = sorted(source_dir.glob("*.md"))

if not md_files:
    print("❌ No markdown files found!")
    sys.exit(1)

print(f"\n📄 Found {len(md_files)} markdown file(s) to convert:")
for md_file in md_files:
    print(f"   - {md_file.name}")

print("\n" + "=" * 60)
print("Starting conversion...")
print("=" * 60 + "\n")

# Convert each markdown file
for md_file in md_files:
    try:
        # Read markdown content
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title from filename (remove number and .md extension)
        filename_without_ext = md_file.stem  # Remove .md
        # Remove leading number and underscore if present
        title = filename_without_ext
        if title[0].isdigit():
            # Remove leading digits and underscores
            title = title.lstrip('0123456789_')
        # Replace underscores with spaces
        title = title.replace('_', ' ')

        # Generate output filename
        output_filename = output_dir / md_file.name.replace('.md', '.docx')

        print(f"Converting: {md_file.name}")
        print(f"  Title: {title}")
        print(f"  Output: {output_filename.name}")

        # Create the enhanced document
        create_enhanced_document(content, title, str(output_filename))
        print()

    except Exception as e:
        print(f"❌ Error processing {md_file.name}: {str(e)}")
        print()

print("=" * 60)
print("✅ Conversion complete!")
print(f"📁 All DOCX files saved to: {output_dir}")
