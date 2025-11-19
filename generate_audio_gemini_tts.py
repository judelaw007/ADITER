#!/usr/bin/env python3
"""
Generate TTS Audio Files using Gemini 2.5 Pro/Flash TTS
Professional voice-over generation for ADIT presentations
"""

import os
import sys
import wave
import subprocess
from pathlib import Path
import re
from google import genai
from google.genai import types


class GeminiTTSGenerator:
    """Generate audio files using Gemini 2.5 TTS API"""

    def __init__(self, api_key: str, use_pro: bool = False):
        """
        Initialize Gemini TTS Generator

        Args:
            api_key: Google API key
            use_pro: Use gemini-2.5-pro-preview-tts instead of flash (higher quality, slower)
        """
        self.api_key = api_key

        # Initialize Gemini client
        self.client = genai.Client(api_key=api_key)

        # Model selection
        self.model = "gemini-2.5-pro-preview-tts" if use_pro else "gemini-2.5-flash-preview-tts"

        # Voice configuration
        # Available voices: Kore, Puck, Charon, Aoede
        # Puck - Professional, warm, clear voice (good for educational content)
        self.voice_name = "Puck"

        print(f"✓ Initialized Gemini TTS")
        print(f"  Model: {self.model}")
        print(f"  Voice: {self.voice_name}")

    def save_wave_file(self, filename: str, pcm_data: bytes, channels: int = 1,
                       rate: int = 24000, sample_width: int = 2):
        """Save PCM data to WAV file"""
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(rate)
            wf.writeframes(pcm_data)

    def convert_wav_to_mp3(self, wav_file: Path, mp3_file: Path) -> bool:
        """Convert WAV to MP3 using ffmpeg"""
        try:
            cmd = [
                'ffmpeg', '-y', '-i', str(wav_file),
                '-codec:a', 'libmp3lame', '-qscale:a', '2',
                str(mp3_file)
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

            if result.returncode == 0:
                return True
            else:
                print(f"    ✗ FFmpeg error: {result.stderr[:200]}")
                return False

        except FileNotFoundError:
            print(f"    ✗ ffmpeg not found - keeping WAV format")
            return False
        except Exception as e:
            print(f"    ✗ Conversion error: {e}")
            return False

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

    def generate_audio_tts(self, text: str, output_file: Path) -> bool:
        """
        Generate audio using Gemini 2.5 TTS

        Args:
            text: Script text to convert to speech
            output_file: Output MP3 file path

        Returns:
            bool: True if successful
        """
        print(f"  Generating with Gemini TTS: {output_file.name}...")

        try:
            # Create TTS prompt with style instructions
            # Gemini TTS allows natural language prompts for voice styling
            tts_prompt = f"""Speak in a warm, professional, conversational tone suitable for educational content.
Use a slightly slower pace for clarity. The speaker is an experienced tax educator explaining complex concepts
in an approachable way.

{text}"""

            # Generate audio with Gemini TTS
            response = self.client.models.generate_content(
                model=self.model,
                contents=tts_prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["AUDIO"],
                    speech_config=types.SpeechConfig(
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name=self.voice_name,
                            )
                        )
                    ),
                )
            )

            # Extract audio data
            if not response.candidates:
                print(f"    ✗ No audio generated")
                return False

            audio_data = response.candidates[0].content.parts[0].inline_data.data

            # Save as WAV temporarily
            wav_file = output_file.with_suffix('.wav')
            self.save_wave_file(str(wav_file), audio_data)

            wav_size = os.path.getsize(wav_file)
            print(f"    ✓ Generated WAV: {wav_size/1024:.1f}KB")

            # Convert to MP3
            if self.convert_wav_to_mp3(wav_file, output_file):
                mp3_size = os.path.getsize(output_file)
                print(f"    ✓ Converted to MP3: {mp3_size/1024:.1f}KB")
                # Remove WAV file
                wav_file.unlink()
                return True
            else:
                # Keep WAV if conversion fails
                print(f"    ⚠ Keeping WAV format")
                wav_file.rename(output_file.with_suffix('.wav'))
                return True

        except Exception as e:
            print(f"    ✗ Error: {e}")
            # Print more details if available
            if hasattr(e, 'message'):
                print(f"    Details: {e.message}")
            return False

    def process_all_scripts(self, scripts_dir: Path, audio_dir: Path):
        """Process all voice-over scripts and generate audio"""

        # Get all script files
        script_files = sorted([f for f in scripts_dir.glob("ch*_sec*.txt") if f.is_file()])

        if not script_files:
            print(f"❌ No script files found in {scripts_dir}")
            return

        print(f"\n🎙️  Generating Audio with Gemini 2.5 TTS")
        print("=" * 70)
        print(f"Scripts found: {len(script_files)}")
        print(f"Output directory: {audio_dir}")
        print(f"Model: {self.model}")
        print(f"Voice: {self.voice_name}")
        print()

        audio_dir.mkdir(exist_ok=True)

        successful = 0
        failed = 0
        total_size = 0

        for i, script_file in enumerate(script_files, 1):
            # Extract script data
            script_data = self.extract_script_text(script_file)

            print(f"\n[{i}/{len(script_files)}] 📝 {script_file.stem}")
            print(f"   Title: {script_data['title']}")
            print(f"   Length: {script_data['char_count']:,} characters")

            # Generate audio filename
            audio_filename = script_file.stem + ".mp3"
            audio_file = audio_dir / audio_filename

            # Generate audio
            if self.generate_audio_tts(script_data['text'], audio_file):
                successful += 1
                if audio_file.exists():
                    total_size += os.path.getsize(audio_file)
                elif audio_file.with_suffix('.wav').exists():
                    total_size += os.path.getsize(audio_file.with_suffix('.wav'))
            else:
                failed += 1

        # Summary
        print("\n" + "=" * 70)
        print(f"📊 Summary:")
        print(f"   ✓ Successful: {successful}")
        print(f"   ✗ Failed: {failed}")
        print(f"   📦 Total size: {total_size/1024/1024:.1f} MB")
        print(f"   📁 Audio directory: {audio_dir}")
        print()


def main():
    """Main execution"""

    # Check for API key
    api_key = os.environ.get('GOOGLE_API_KEY')

    if not api_key:
        print("❌ No API key found!")
        print()
        print("Please set your Google API key:")
        print("  export GOOGLE_API_KEY='your-api-key-here'")
        print()
        print("Or load from .env file")
        sys.exit(1)

    # Determine which model to use
    use_pro = '--pro' in sys.argv

    # Set up paths
    scripts_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations/voiceover_scripts")
    audio_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations/audio")

    if not scripts_dir.exists():
        print(f"❌ Scripts directory not found: {scripts_dir}")
        sys.exit(1)

    print("\n🎬 ADIT Fundamental Tax Issues - Gemini TTS Audio Generation")
    print("=" * 70)

    # Generate audio
    generator = GeminiTTSGenerator(api_key, use_pro=use_pro)
    generator.process_all_scripts(scripts_dir, audio_dir)

    print("✅ Audio generation complete!")
    print()
    print("Next steps:")
    print("  1. Review audio files in the audio directory")
    print("  2. Test audio quality and clarity")
    print("  3. Audio is already integrated into presentation HTML files")
    print()


if __name__ == "__main__":
    main()
