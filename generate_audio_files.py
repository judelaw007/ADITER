#!/usr/bin/env python3
"""
Generate TTS Audio Files for Presentation Voice-Overs
Supports Google Cloud TTS API and Gemini API
"""

import os
import sys
import json
import base64
import requests
from pathlib import Path
import re


class TTSAudioGenerator:
    """Generate audio files from voice-over scripts"""

    def __init__(self, api_key: str, use_gemini: bool = False):
        self.api_key = api_key
        self.use_gemini = use_gemini

        if use_gemini:
            # Gemini API endpoint (for future compatibility)
            self.tts_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent"
        else:
            # Google Cloud Text-to-Speech API
            self.tts_url = "https://texttospeech.googleapis.com/v1/text:synthesize"

        self.voice_config = {
            'languageCode': 'en-US',
            'name': 'en-US-Neural2-D',  # Professional, warm voice
            'ssmlGender': 'NEUTRAL'
        }

        self.audio_config = {
            'audioEncoding': 'MP3',
            'pitch': 0.0,
            'speakingRate': 0.95,  # Slightly slower for educational content
            'volumeGainDb': 0.0
        }

    def extract_script_text(self, script_file: Path) -> dict:
        """Extract title and script text from script file"""
        content = script_file.read_text(encoding='utf-8')

        # Extract slide title
        title_match = re.search(r'Slide: (.+)', content)
        title = title_match.group(1) if title_match else "Untitled"

        # Extract main script (between title and character count)
        lines = content.split('\n')
        script_lines = []
        capturing = False

        for line in lines:
            if line.startswith('Slide:'):
                capturing = True
                continue
            elif line.startswith('Character Count:') or line.startswith('Estimated Duration:'):
                break
            elif capturing and line.strip():
                script_lines.append(line)

        script_text = '\n\n'.join(script_lines).strip()

        return {
            'title': title,
            'text': script_text,
            'char_count': len(script_text)
        }

    def generate_audio_google_tts(self, text: str, output_file: Path) -> bool:
        """Generate audio using Google Cloud Text-to-Speech"""
        print(f"  Generating audio: {output_file.name}...")

        try:
            # Prepare request
            data = {
                'input': {'text': text},
                'voice': self.voice_config,
                'audioConfig': self.audio_config
            }

            response = requests.post(
                self.tts_url,
                params={'key': self.api_key},
                headers={'Content-Type': 'application/json'},
                json=data,
                timeout=60
            )

            if response.status_code == 200:
                result = response.json()
                audio_content = base64.b64decode(result['audioContent'])

                with open(output_file, 'wb') as f:
                    f.write(audio_content)

                file_size = os.path.getsize(output_file)
                print(f"    ✓ Generated: {file_size/1024:.1f}KB")
                return True
            else:
                print(f"    ✗ Error: {response.status_code}")
                print(f"    Response: {response.text[:200]}")
                return False

        except Exception as e:
            print(f"    ✗ Error: {e}")
            return False

    def generate_audio_gemini(self, text: str, output_file: Path) -> bool:
        """Generate audio using Gemini API (if TTS is supported)"""
        print(f"  Generating audio with Gemini: {output_file.name}...")

        try:
            # Gemini API request format (may need adjustment based on actual API)
            data = {
                "contents": [{
                    "parts": [{
                        "text": f"Convert this to speech: {text}"
                    }]
                }],
                "generationConfig": {
                    "temperature": 0.7,
                }
            }

            response = requests.post(
                self.tts_url,
                params={'key': self.api_key},
                headers={'Content-Type': 'application/json'},
                json=data,
                timeout=60
            )

            if response.status_code == 200:
                # This is placeholder - actual Gemini TTS response format unknown
                print(f"    ⚠ Gemini TTS not yet fully supported, using Google Cloud TTS instead")
                return self.generate_audio_google_tts(text, output_file)
            else:
                print(f"    ✗ Gemini Error: {response.status_code}")
                print(f"    Falling back to Google Cloud TTS...")
                return self.generate_audio_google_tts(text, output_file)

        except Exception as e:
            print(f"    ✗ Gemini Error: {e}")
            print(f"    Falling back to Google Cloud TTS...")
            return self.generate_audio_google_tts(text, output_file)

    def process_all_scripts(self, scripts_dir: Path, audio_dir: Path):
        """Process all voice-over scripts and generate audio"""

        # Get all script files
        script_files = sorted([f for f in scripts_dir.glob("ch*_sec*.txt") if f.is_file()])

        if not script_files:
            print(f"❌ No script files found in {scripts_dir}")
            return

        print(f"\n🎙️  Generating Audio Files")
        print("=" * 70)
        print(f"Scripts found: {len(script_files)}")
        print(f"Output directory: {audio_dir}")
        print(f"API: {'Gemini' if self.use_gemini else 'Google Cloud TTS'}")
        print()

        audio_dir.mkdir(exist_ok=True)

        successful = 0
        failed = 0

        for script_file in script_files:
            # Extract script data
            script_data = self.extract_script_text(script_file)

            print(f"\n📝 {script_file.stem}")
            print(f"   Title: {script_data['title']}")
            print(f"   Length: {script_data['char_count']:,} characters")

            # Generate audio filename
            audio_filename = script_file.stem + ".mp3"
            audio_file = audio_dir / audio_filename

            # Generate audio
            if self.use_gemini:
                success = self.generate_audio_gemini(script_data['text'], audio_file)
            else:
                success = self.generate_audio_google_tts(script_data['text'], audio_file)

            if success:
                successful += 1
            else:
                failed += 1

        # Summary
        print("\n" + "=" * 70)
        print(f"📊 Summary:")
        print(f"   ✓ Successful: {successful}")
        print(f"   ✗ Failed: {failed}")
        print(f"   📁 Audio directory: {audio_dir}")
        print()


def main():
    """Main execution"""

    # Check for API key
    api_key = os.environ.get('GOOGLE_API_KEY') or os.environ.get('GEMINI_API_KEY')

    if not api_key:
        print("❌ No API key found!")
        print()
        print("Please set your Google API key:")
        print("  export GOOGLE_API_KEY='your-api-key-here'")
        print()
        print("Or run with:")
        print("  GOOGLE_API_KEY='your-key' python3 generate_audio_files.py")
        print()
        print("Get your API key from:")
        print("  - Google Cloud TTS: https://console.cloud.google.com/apis/credentials")
        print("  - Gemini API: https://makersuite.google.com/app/apikey")
        sys.exit(1)

    # Determine which API to use
    use_gemini = '--gemini' in sys.argv

    # Set up paths
    scripts_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations/voiceover_scripts")
    audio_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations/audio")

    if not scripts_dir.exists():
        print(f"❌ Scripts directory not found: {scripts_dir}")
        sys.exit(1)

    # Generate audio
    generator = TTSAudioGenerator(api_key, use_gemini=use_gemini)
    generator.process_all_scripts(scripts_dir, audio_dir)

    print("✅ Audio generation complete!")
    print()
    print("Next steps:")
    print("  1. Review audio files in the audio directory")
    print("  2. Integrate audio into presentation HTML files")
    print()


if __name__ == "__main__":
    main()
