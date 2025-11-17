#!/usr/bin/env python3
"""
Simple script to create ADIT presentations with voice
Usage: python create_presentation.py <topic_number>
Example: python create_presentation.py 01
"""

import os
import sys
from pathlib import Path
from presentation_builder import PresentationBuilder


def find_docx_files(topic_number: str = None):
    """Find available DOCX files in generated_notes"""
    notes_dir = Path("generated_notes")

    if topic_number:
        # Find specific topic
        topic_dirs = list(notes_dir.glob(f"{topic_number}_*"))
        if topic_dirs:
            docx_files = list(topic_dirs[0].glob("*.docx"))
            return docx_files
    else:
        # Find all DOCX files
        return list(notes_dir.glob("**/*.docx"))

    return []


def main():
    # Check for OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not set!")
        print("\nTo use this tool, you need an OpenAI API key.")
        print("\nSteps:")
        print("1. Get your API key from: https://platform.openai.com/api-keys")
        print("2. Set it as an environment variable:")
        print("   export OPENAI_API_KEY='sk-...'")
        print("\nAlternatively, create a .env file with:")
        print("   OPENAI_API_KEY=sk-...")
        sys.exit(1)

    # Parse arguments
    topic_number = sys.argv[1] if len(sys.argv) > 1 else None

    # Find DOCX files
    print("\n" + "="*60)
    print("ADIT Interactive Presentation Builder")
    print("="*60 + "\n")

    docx_files = find_docx_files(topic_number)

    if not docx_files:
        print("No DOCX files found!")
        print("\nAvailable topics in generated_notes:")
        notes_dir = Path("generated_notes")
        for topic_dir in sorted(notes_dir.glob("[0-9]*")):
            print(f"  - {topic_dir.name}")
        print("\nUsage: python create_presentation.py <topic_number>")
        print("Example: python create_presentation.py 01")
        sys.exit(1)

    # Display available files
    print(f"Found {len(docx_files)} DOCX file(s):\n")
    for i, docx_file in enumerate(docx_files, 1):
        print(f"{i}. {docx_file.name}")

    # Configuration
    print("\n" + "-"*60)
    print("Configuration:")
    print("-"*60)

    # Voice selection
    voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
    print("\nAvailable voices:")
    print("  alloy   - Neutral, balanced")
    print("  echo    - Clear, professional")
    print("  fable   - Warm, expressive")
    print("  onyx    - Deep, authoritative")
    print("  nova    - Energetic, friendly")
    print("  shimmer - Smooth, calm")

    voice = input("\nSelect voice (default: alloy): ").strip().lower() or "alloy"
    if voice not in voices:
        print(f"Invalid voice. Using 'alloy'")
        voice = "alloy"

    # Password
    use_encryption = input("\nEncrypt presentation? (y/n, default: y): ").strip().lower()
    password = None

    if use_encryption != 'n':
        password = input("Enter password (default: ADIT2025): ").strip() or "ADIT2025"
        print(f"✓ Encryption enabled with password: {password}")
    else:
        print("✓ No encryption (presentation will be publicly accessible)")

    # Build presentation
    print("\n" + "="*60)
    print("Building Presentation...")
    print("="*60 + "\n")

    builder = PresentationBuilder(
        openai_api_key=api_key,
        output_dir="presentation_output"
    )

    # Process first DOCX file
    docx_file = docx_files[0]
    title = docx_file.stem.replace("_", " ")

    try:
        output_file = builder.build_presentation(
            docx_path=str(docx_file),
            title=title,
            voice=voice,
            password=password
        )

        print("="*60)
        print("✓ SUCCESS! Presentation created!")
        print("="*60)
        print(f"\nOutput: {output_file}")
        print(f"\nTo view:")
        print(f"  1. Open in browser: file://{Path(output_file).absolute()}")
        print(f"  2. Or run: python -m http.server 8000")
        print(f"     Then visit: http://localhost:8000/presentation_output/")

        if password:
            print(f"\nPassword: {password}")

        print("\n" + "="*60)
        print("Navigation Controls:")
        print("="*60)
        print("  • Click 'Next' / 'Previous' buttons")
        print("  • Use arrow keys (← →)")
        print("  • Swipe on touch devices")
        print("  • Press 'M' to mute/unmute audio")
        print("  • Audio auto-plays with each slide")

    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
