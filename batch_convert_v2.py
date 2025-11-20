#!/usr/bin/env python3
"""
Batch conversion script with timeout handling
"""
import os
import sys
import signal
from create_enhanced_docx import create_enhanced_document

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Conversion timeout")

def convert_file_with_timeout(input_path, output_path, title, timeout_sec=60):
    """Convert a single file with timeout"""
    # Set the signal handler and alarm
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_sec)

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        create_enhanced_document(content, title, output_path)
        signal.alarm(0)  # Cancel alarm
        return True, None
    except TimeoutException:
        signal.alarm(0)  # Cancel alarm
        return False, "Timeout"
    except Exception as e:
        signal.alarm(0)  # Cancel alarm
        return False, str(e)

def convert_all_md_files(input_dir):
    """Convert all markdown files in directory to DOCX"""
    md_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.md')])

    if not md_files:
        print("No markdown files found")
        return

    print(f"Found {len(md_files)} markdown files to convert\n")

    converted = 0
    failed = 0
    failed_files = []

    for idx, md_file in enumerate(md_files, 1):
        input_path = os.path.join(input_dir, md_file)
        output_filename = md_file.replace('.md', '.docx')
        output_path = os.path.join(input_dir, output_filename)

        # Skip if already exists
        if os.path.exists(output_path):
            print(f"[{idx}/{len(md_files)}] {md_file} - Already exists, skipping")
            continue

        print(f"[{idx}/{len(md_files)}] Converting: {md_file}...", end='', flush=True)

        title = output_filename.replace('.docx', '').split('_', 1)[1].replace('_', ' ') if '_' in output_filename else output_filename

        success, error = convert_file_with_timeout(input_path, output_path, title, timeout_sec=120)

        if success:
            print(" ✅ Done")
            converted += 1
        else:
            print(f" ❌ Error: {error}")
            failed += 1
            failed_files.append(md_file)

    print("\n" + "="*60)
    print(f"Conversion Summary:")
    print(f"  Successfully converted: {converted}/{len(md_files)}")
    if failed > 0:
        print(f"  Failed: {failed}")
        print(f"  Failed files: {', '.join(failed_files)}")
    print("="*60)

if __name__ == '__main__':
    input_dir = "/home/user/ADITER/generated_notes/12_Transfer_pricing/quality_checked"
    convert_all_md_files(input_dir)
