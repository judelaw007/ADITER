#!/usr/bin/env python3
"""
ADIT Presentation Creator - Version with API key input
Usage:
  python create_presentation_with_key.py --api-key sk-xxx [topic_number]
  python create_presentation_with_key.py [topic_number]  # Uses OPENAI_API_KEY env var
"""

import os
import sys
import argparse
from pathlib import Path
from presentation_builder import PresentationBuilder


def find_docx_files(topic_number: str = None):
    """Find available DOCX files in generated_notes"""
    notes_dir = Path("generated_notes")

    if topic_number:
        # Find specific topic
        topic_dirs = list(notes_dir.glob(f"{topic_number}_*"))
        if topic_dirs:
            docx_files = list(topic_dirs[0].glob("**/*.docx"))
            return docx_files
    else:
        # Find all DOCX files
        return list(notes_dir.glob("**/*.docx"))

    return []


def main():
    parser = argparse.ArgumentParser(
        description='Create ADIT presentations with voice narration'
    )
    parser.add_argument(
        '--api-key',
        help='OpenAI API key (or set OPENAI_API_KEY environment variable)',
        default=None
    )
    parser.add_argument(
        '--voice',
        choices=['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'],
        default='onyx',
        help='Voice for narration (default: onyx)'
    )
    parser.add_argument(
        '--password',
        default='ADIT2025',
        help='Encryption password (default: ADIT2025)'
    )
    parser.add_argument(
        '--no-encryption',
        action='store_true',
        help='Disable encryption'
    )
    parser.add_argument(
        'topic',
        nargs='?',
        help='Topic number (e.g., 01, 03, etc.)'
    )

    args = parser.parse_args()

    # Get API key
    api_key = args.api_key or os.getenv('OPENAI_API_KEY')

    if not api_key:
        print("\n❌ ERROR: No OpenAI API key provided!")
        print("\nOptions:")
        print("  1. Use --api-key flag:")
        print("     python create_presentation_with_key.py --api-key sk-...")
        print("\n  2. Set environment variable:")
        print("     export OPENAI_API_KEY='sk-...'")
        print("     python create_presentation_with_key.py")
        print("\n  3. Get an API key from:")
        print("     https://platform.openai.com/api-keys")
        sys.exit(1)

    # Verify API key format
    if not api_key.startswith('sk-'):
        print(f"\n⚠️  WARNING: API key doesn't start with 'sk-'")
        print(f"Key starts with: {api_key[:10]}...")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)

    print("\n" + "="*60)
    print("ADIT Interactive Presentation Builder")
    print("="*60 + "\n")
    print(f"✓ API Key: {api_key[:15]}...{api_key[-4:]}")
    print(f"✓ Voice: {args.voice}")
    print(f"✓ Encryption: {'Disabled' if args.no_encryption else f'Enabled (password: {args.password})'}")
    print()

    # Find DOCX files
    docx_files = find_docx_files(args.topic)

    if not docx_files:
        print("❌ No DOCX files found!")
        print("\nAvailable topics in generated_notes:")
        notes_dir = Path("generated_notes")
        for topic_dir in sorted(notes_dir.glob("[0-9]*")):
            print(f"  - {topic_dir.name}")
        print("\nUsage:")
        print("  python create_presentation_with_key.py --api-key sk-... 03")
        sys.exit(1)

    # Display available files
    print(f"Found {len(docx_files)} DOCX file(s):\n")
    for i, docx_file in enumerate(docx_files[:5], 1):  # Show first 5
        print(f"  {i}. {docx_file.name}")

    if len(docx_files) > 5:
        print(f"  ... and {len(docx_files) - 5} more")

    # Select first file
    docx_file = docx_files[0]
    print(f"\nProcessing: {docx_file.name}")
    print()

    # Build presentation
    print("="*60)
    print("Building Presentation...")
    print("="*60 + "\n")

    builder = PresentationBuilder(
        openai_api_key=api_key,
        output_dir="presentation_output"
    )

    title = docx_file.stem.replace("_", " ")
    password = None if args.no_encryption else args.password

    try:
        output_file = builder.build_presentation(
            docx_path=str(docx_file),
            title=title,
            voice=args.voice,
            password=password
        )

        print("\n" + "="*60)
        print("✅ SUCCESS! Presentation Created!")
        print("="*60)
        print(f"\nOutput: {output_file}")
        print(f"\nTo view:")
        print(f"  1. Start local server:")
        print(f"     cd presentation_output && python -m http.server 8000")
        print(f"\n  2. Open in browser:")
        print(f"     http://localhost:8000/{'index.html' if password else 'presentation.html'}")

        if password:
            print(f"\n  3. Enter password: {password}")

        print("\n" + "="*60)
        print("Navigation Controls:")
        print("="*60)
        print("  • Arrow keys (← →) or click Next/Previous")
        print("  • Press 'M' to toggle audio")
        print("  • Swipe on touch devices")
        print("  • Audio auto-plays with each slide")
        print("\n" + "="*60)

        # Show file sizes
        import os
        total_size = sum(
            os.path.getsize(f)
            for f in Path("presentation_output").rglob("*")
            if f.is_file()
        )
        print(f"\nTotal size: {total_size / 1024:.1f} KB")

        audio_files = list(Path("presentation_output/audio").glob("*.mp3"))
        if audio_files:
            audio_size = sum(os.path.getsize(f) for f in audio_files)
            print(f"Audio files: {len(audio_files)} files, {audio_size / 1024:.1f} KB")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
