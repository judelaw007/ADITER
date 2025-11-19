#!/usr/bin/env python3
"""
Quick test of Gemini TTS with one script file
"""

import os
import sys
from pathlib import Path

# Load API key from .env
env_file = Path('.env')
if env_file.exists():
    for line in env_file.read_text().splitlines():
        if line.startswith('GOOGLE_API_KEY='):
            api_key = line.split('=', 1)[1].strip().strip('"\'')
            os.environ['GOOGLE_API_KEY'] = api_key
            break

# Import after setting env
from generate_audio_gemini_tts import GeminiTTSGenerator

# Test with first script
scripts_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations/voiceover_scripts")
audio_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations/audio_test")
audio_dir.mkdir(exist_ok=True)

# Get first script
script_files = sorted([f for f in scripts_dir.glob("ch01_sec01*.txt") if f.is_file()])

if not script_files:
    print("No test script found!")
    sys.exit(1)

test_script = script_files[0]

print(f"🧪 Testing Gemini TTS with: {test_script.name}\n")

# Initialize generator
generator = GeminiTTSGenerator(os.environ['GOOGLE_API_KEY'], use_pro=False)

# Extract and generate
script_data = generator.extract_script_text(test_script)

print(f"Title: {script_data['title']}")
print(f"Length: {script_data['char_count']:,} characters\n")

# Generate audio
output_file = audio_dir / (test_script.stem + ".mp3")
success = generator.generate_audio_tts(script_data['text'], output_file)

if success:
    if output_file.exists():
        size = os.path.getsize(output_file)
        print(f"\n✅ Test successful!")
        print(f"   Output: {output_file}")
        print(f"   Size: {size/1024:.1f}KB")
    elif output_file.with_suffix('.wav').exists():
        size = os.path.getsize(output_file.with_suffix('.wav'))
        print(f"\n✅ Test successful (WAV format)!")
        print(f"   Output: {output_file.with_suffix('.wav')}")
        print(f"   Size: {size/1024:.1f}KB")
else:
    print(f"\n❌ Test failed!")
    sys.exit(1)
