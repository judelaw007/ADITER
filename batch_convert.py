#!/usr/bin/env python3
"""
Batch conversion script for markdown to DOCX files
"""
import os
import sys
from create_enhanced_docx import create_enhanced_document

def convert_all_md_files(input_dir):
    """Convert all markdown files in directory to DOCX"""
    md_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.md')])

    if not md_files:
        print("No markdown files found")
        return

    print(f"Found {len(md_files)} markdown files to convert\n")

    converted = 0
    failed = 0

    for idx, md_file in enumerate(md_files, 1):
        input_path = os.path.join(input_dir, md_file)
        output_filename = md_file.replace('.md', '.docx')
        output_path = os.path.join(input_dir, output_filename)

        print(f"[{idx}/{len(md_files)}] Converting: {md_file}...", end='', flush=True)

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            title = output_filename.replace('.docx', '').split('_', 1)[1].replace('_', ' ') if '_' in output_filename else output_filename

            create_enhanced_document(content, title, output_path)
            print(" ✅ Done")
            converted += 1

        except Exception as e:
            print(f" ❌ Error: {str(e)}")
            failed += 1

    print("\n" + "="*60)
    print(f"Conversion Summary:")
    print(f"  Successfully converted: {converted}/{len(md_files)}")
    if failed > 0:
        print(f"  Failed: {failed}")
    print("="*60)

if __name__ == '__main__':
    input_dir = "/home/user/ADITER/generated_notes/12_Transfer_pricing/quality_checked"
    convert_all_md_files(input_dir)
