#!/usr/bin/env python3
"""
Integrate TTS Audio into HTML5 Presentations
Embeds audio players and enables auto-play narration
"""

import os
import re
import base64
from pathlib import Path


class AudioIntegrator:
    """Integrate audio files into presentation HTML pages"""

    def __init__(self, presentations_dir: str):
        self.presentations_dir = Path(presentations_dir)
        self.audio_dir = self.presentations_dir / "audio"

        # Mapping of chapter/section to audio files
        self.audio_mapping = self._build_audio_mapping()

    def _build_audio_mapping(self) -> dict:
        """Build mapping between HTML content files and audio files"""
        mapping = {}

        # Pattern: ch{chapter}_sec{section}_{title}.mp3
        for audio_file in self.audio_dir.glob("*.mp3"):
            match = re.match(r'ch(\d+)_sec(\d+)_.*\.mp3', audio_file.name)
            if match:
                chapter = int(match.group(1))
                section = int(match.group(2))
                key = (chapter, section)
                mapping[key] = audio_file.name

        return mapping

    def get_audio_for_content_file(self, html_file: Path) -> str:
        """Get corresponding audio file for a content HTML file"""
        # Pattern: 01-income-flows-...-1-content.html -> chapter 1, section 1
        # The section number is the last number before '-content.html'
        match = re.match(r'(\d+)-.*?-(\d+)-content\.html$', html_file.name)
        if match:
            chapter = int(match.group(1))
            section = int(match.group(2))
            return self.audio_mapping.get((chapter, section))
        return None

    def embed_audio(self, html_file: Path, audio_file: str) -> bool:
        """Embed audio player into HTML file"""
        try:
            # Read HTML content
            content = html_file.read_text(encoding='utf-8')

            # Check if audio is already embedded
            if 'class="audio-player"' in content or '<audio' in content:
                print(f"    ⚠ Audio already embedded in {html_file.name}")
                return False

            # Create audio player HTML
            audio_html = f'''
        <!-- Voice-Over Audio Player -->
        <div class="audio-player" style="margin: 2rem 0; padding: 1.5rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="flex: 1;">
                    <div style="font-size: 0.9rem; color: rgba(255,255,255,0.9); margin-bottom: 0.5rem;">
                        <strong>🎧 Professional Voice-Over Narration</strong>
                    </div>
                    <audio id="narration-audio" controls autoplay style="width: 100%; border-radius: 8px;">
                        <source src="audio/{audio_file}" type="audio/mpeg">
                        Your browser does not support the audio element.
                    </audio>
                </div>
                <button onclick="toggleAudio()" style="padding: 0.75rem 1.5rem; background: rgba(255,255,255,0.2); border: 2px solid rgba(255,255,255,0.4); border-radius: 8px; color: white; cursor: pointer; font-weight: bold; transition: all 0.3s;">
                    <span id="audio-toggle">⏸️ Pause</span>
                </button>
            </div>
        </div>

        <script>
            const audio = document.getElementById('narration-audio');
            const toggleBtn = document.getElementById('audio-toggle');

            function toggleAudio() {{
                if (audio.paused) {{
                    audio.play();
                    toggleBtn.textContent = '⏸️ Pause';
                }} else {{
                    audio.pause();
                    toggleBtn.textContent = '▶️ Play';
                }}
            }}

            // Update button state when audio ends
            audio.addEventListener('ended', () => {{
                toggleBtn.textContent = '🔄 Replay';
            }});

            // Auto-play on page load (with user interaction fallback)
            document.addEventListener('DOMContentLoaded', () => {{
                audio.play().catch(err => {{
                    console.log('Auto-play prevented - user interaction required');
                    toggleBtn.textContent = '▶️ Play';
                }});
            }});
        </script>
'''

            # Find the content container and insert audio player after the title
            # Look for the first <h1> or main content div
            if '<h1' in content:
                content = content.replace('<h1', audio_html + '\n        <h1', 1)
            elif '<div class="content' in content:
                content = re.sub(
                    r'(<div class="content[^"]*">)',
                    r'\1' + audio_html,
                    content,
                    count=1
                )
            else:
                # Fallback: insert after <body>
                content = content.replace('<body>', '<body>\n' + audio_html, 1)

            # Write updated content
            html_file.write_text(content, encoding='utf-8')
            return True

        except Exception as e:
            print(f"    ✗ Error embedding audio: {e}")
            return False

    def process_all_content_files(self):
        """Process all content HTML files and embed audio"""
        print("\n🎬 Integrating Audio into Presentations")
        print("=" * 70)
        print(f"Presentations directory: {self.presentations_dir}")
        print(f"Audio files found: {len(self.audio_mapping)}")
        print()

        # Find all content HTML files
        content_files = sorted(self.presentations_dir.glob("*-content.html"))

        if not content_files:
            print("❌ No content HTML files found!")
            return

        successful = 0
        skipped = 0
        failed = 0

        for html_file in content_files:
            audio_file = self.get_audio_for_content_file(html_file)

            if audio_file:
                print(f"📝 {html_file.name}")
                print(f"   Audio: {audio_file}")

                if self.embed_audio(html_file, audio_file):
                    print(f"   ✓ Audio embedded successfully")
                    successful += 1
                else:
                    skipped += 1
            else:
                print(f"⚠ {html_file.name}")
                print(f"   No matching audio file found")
                failed += 1
            print()

        # Summary
        print("=" * 70)
        print(f"📊 Summary:")
        print(f"   ✓ Successfully embedded: {successful}")
        print(f"   ⚠ Skipped (already embedded): {skipped}")
        print(f"   ✗ No audio found: {failed}")
        print()
        print(f"✅ Audio integration complete!")
        print()


def main():
    """Main execution"""
    presentations_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations")

    if not presentations_dir.exists():
        print(f"❌ Presentations directory not found: {presentations_dir}")
        return

    integrator = AudioIntegrator(str(presentations_dir))
    integrator.process_all_content_files()


if __name__ == "__main__":
    main()
