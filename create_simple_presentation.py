#!/usr/bin/env python3
"""
Simplified ADIT Presentation Builder (No Encryption Dependency)
Creates interactive HTML5 presentations with OpenAI TTS
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import List, Dict

try:
    from openai import OpenAI
except ImportError:
    print("Installing OpenAI library...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "openai"], check=True)
    from openai import OpenAI

try:
    from docx import Document
except ImportError:
    print("Installing python-docx library...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "python-docx"], check=True)
    from docx import Document


class SimplePresentationBuilder:
    """Build presentations without encryption"""

    def __init__(self, openai_api_key: str, output_dir: str = "presentation_output"):
        self.client = OpenAI(api_key=openai_api_key)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.audio_dir = self.output_dir / "audio"
        self.audio_dir.mkdir(exist_ok=True)

    def parse_docx_to_slides(self, docx_path: str, max_slides: int = 10) -> List[Dict]:
        """Parse DOCX file into presentation slides"""
        doc = Document(docx_path)
        slides = []
        current_slide = {"title": "", "content": [], "narration": ""}

        for para in doc.paragraphs:
            text = para.text.strip()
            if not text:
                continue

            # Check if it's a heading (new slide)
            if para.style.name.startswith('Heading 1'):
                if current_slide["title"] and len(slides) < max_slides:
                    slides.append(current_slide)
                current_slide = {"title": text, "content": [], "narration": text}
            elif para.style.name.startswith('Heading 2'):
                if current_slide["title"] and len(slides) < max_slides:
                    slides.append(current_slide)
                current_slide = {"title": text, "content": [], "narration": text}
            else:
                # Regular content
                if len(current_slide["content"]) < 5:  # Limit content per slide
                    current_slide["content"].append(text[:200])  # Limit text length
                    current_slide["narration"] += " " + text[:500]

            if len(slides) >= max_slides:
                break

        # Add last slide
        if current_slide["title"] and len(slides) < max_slides:
            slides.append(current_slide)

        return slides[:max_slides]  # Ensure we don't exceed max

    def create_narration_script(self, slide: Dict) -> str:
        """Create a narration script from slide content"""
        # Limit narration to avoid long audio
        narration = slide["narration"][:800]

        # Clean up for better TTS
        narration = re.sub(r'\[.*?\]', '', narration)  # Remove citations
        narration = re.sub(r'\s+', ' ', narration)  # Normalize whitespace
        narration = re.sub(r'[•\-]\s*', '', narration)  # Remove bullets

        return narration.strip()

    def generate_voice(self, text: str, slide_index: int, voice: str = "alloy") -> str:
        """Generate voice narration using OpenAI TTS"""
        print(f"  Generating voice for slide {slide_index + 1}...")

        audio_file = self.audio_dir / f"slide_{slide_index:03d}.mp3"

        try:
            response = self.client.audio.speech.create(
                model="tts-1-hd",
                voice=voice,
                input=text,
                speed=1.0
            )

            response.stream_to_file(str(audio_file))
            file_size = os.path.getsize(audio_file)
            print(f"    ✓ Generated: {audio_file.name} ({file_size/1024:.1f}KB)")
            return audio_file.name

        except Exception as e:
            print(f"    ✗ Error generating voice: {e}")
            return None

    def generate_html_presentation(self, slides: List[Dict], title: str,
                                   audio_files: List[str]) -> str:
        """Generate interactive HTML5 presentation"""

        # Read the template from demo_presentation.html and adapt it
        slides_html = ""
        for i, slide in enumerate(slides):
            content_html = ""
            for item in slide["content"]:
                content_html += f"<p>{item}</p>"

            slides_html += f'''
            <div class="slide {'active' if i == 0 else ''}">
                <h1>{slide["title"]}</h1>
                <div class="slide-content">
                    {content_html}
                </div>
            </div>
            '''

        audio_files_json = json.dumps(audio_files)

        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            overflow: hidden;
        }}
        .presentation-container {{
            max-width: 1200px;
            height: 100vh;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            padding: 20px;
        }}
        .slide-container {{
            flex: 1;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 60px;
            overflow-y: auto;
            position: relative;
        }}
        .slide {{
            display: none;
            animation: slideIn 0.5s ease-in-out;
        }}
        .slide.active {{ display: block; }}
        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateX(50px); }}
            to {{ opacity: 1; transform: translateX(0); }}
        }}
        .slide h1 {{
            color: #1F4E78;
            font-size: 2.5em;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 4px solid #667eea;
        }}
        .slide-content {{
            font-size: 1.2em;
            line-height: 1.8;
            color: #333;
        }}
        .slide-content p {{ margin-bottom: 15px; }}
        .controls {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 20px;
            padding: 20px;
            background: rgba(255,255,255,0.2);
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }}
        button {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.1em;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }}
        button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        }}
        button:disabled {{
            opacity: 0.5;
            cursor: not-allowed;
            transform: none;
        }}
        .progress-bar {{
            flex: 1;
            margin: 0 30px;
            height: 8px;
            background: rgba(255,255,255,0.3);
            border-radius: 10px;
            overflow: hidden;
        }}
        .progress-fill {{
            height: 100%;
            background: white;
            border-radius: 10px;
            transition: width 0.3s ease;
        }}
        .slide-counter {{
            color: white;
            font-size: 1.1em;
            font-weight: bold;
        }}
        .audio-indicator {{
            position: absolute;
            top: 20px;
            right: 20px;
            background: #667eea;
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 0.9em;
            display: none;
        }}
        .audio-indicator.playing {{
            display: block;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.6; }}
        }}
        .audio-controls {{
            display: flex;
            align-items: center;
            gap: 15px;
        }}
        .audio-toggle {{
            background: rgba(255,255,255,0.3);
            border: 2px solid white;
            padding: 10px 20px;
            font-size: 1em;
        }}
    </style>
</head>
<body>
    <div class="presentation-container">
        <div class="slide-container">
            <div class="audio-indicator" id="audioIndicator">🔊 Audio Playing</div>
            {slides_html}
        </div>

        <div class="controls">
            <button id="prevBtn" onclick="navigateSlide(-1)">← Previous</button>

            <div style="flex: 1; display: flex; align-items: center; gap: 20px;">
                <div class="progress-bar">
                    <div class="progress-fill" id="progressFill"></div>
                </div>
                <div class="slide-counter" id="slideCounter">1 / {len(slides)}</div>
            </div>

            <div class="audio-controls">
                <button class="audio-toggle" id="audioToggle" onclick="toggleAudio()">🔊 Audio On</button>
                <button id="nextBtn" onclick="navigateSlide(1)">Next →</button>
            </div>
        </div>
    </div>

    <audio id="audioPlayer"></audio>

    <script>
        let currentSlide = 0;
        const totalSlides = {len(slides)};
        let audioEnabled = true;
        const audioFiles = {audio_files_json};

        const slides = document.querySelectorAll('.slide');
        const audioPlayer = document.getElementById('audioPlayer');
        const audioIndicator = document.getElementById('audioIndicator');
        const audioToggle = document.getElementById('audioToggle');

        function showSlide(index) {{
            slides.forEach(slide => slide.classList.remove('active'));
            slides[index].classList.add('active');

            currentSlide = index;
            updateControls();
            updateProgress();

            if (audioEnabled && audioFiles[index]) {{
                playSlideAudio(index);
            }} else {{
                stopAudio();
            }}
        }}

        function playSlideAudio(index) {{
            const audioFile = audioFiles[index];
            if (audioFile) {{
                audioPlayer.src = 'audio/' + audioFile;
                audioPlayer.play().then(() => {{
                    audioIndicator.classList.add('playing');
                }}).catch(err => {{
                    console.log('Audio play failed:', err);
                }});

                audioPlayer.onended = () => {{
                    audioIndicator.classList.remove('playing');
                }};
            }}
        }}

        function stopAudio() {{
            audioPlayer.pause();
            audioPlayer.currentTime = 0;
            audioIndicator.classList.remove('playing');
        }}

        function navigateSlide(direction) {{
            stopAudio();
            const newIndex = currentSlide + direction;
            if (newIndex >= 0 && newIndex < totalSlides) {{
                showSlide(newIndex);
            }}
        }}

        function updateControls() {{
            document.getElementById('prevBtn').disabled = currentSlide === 0;
            document.getElementById('nextBtn').disabled = currentSlide === totalSlides - 1;
            document.getElementById('slideCounter').textContent = `${{currentSlide + 1}} / ${{totalSlides}}`;
        }}

        function updateProgress() {{
            const progress = ((currentSlide + 1) / totalSlides) * 100;
            document.getElementById('progressFill').style.width = progress + '%';
        }}

        function toggleAudio() {{
            audioEnabled = !audioEnabled;
            audioToggle.textContent = audioEnabled ? '🔊 Audio On' : '🔇 Audio Off';

            if (audioEnabled) {{
                playSlideAudio(currentSlide);
            }} else {{
                stopAudio();
            }}
        }}

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowRight' || e.key === ' ') {{
                e.preventDefault();
                navigateSlide(1);
            }} else if (e.key === 'ArrowLeft') {{
                e.preventDefault();
                navigateSlide(-1);
            }} else if (e.key === 'm' || e.key === 'M') {{
                toggleAudio();
            }}
        }});

        // Touch support
        let touchStartX = 0;
        document.addEventListener('touchstart', (e) => {{
            touchStartX = e.touches[0].clientX;
        }});

        document.addEventListener('touchend', (e) => {{
            const touchEndX = e.changedTouches[0].clientX;
            const diff = touchStartX - touchEndX;

            if (Math.abs(diff) > 50) {{
                navigateSlide(diff > 0 ? 1 : -1);
            }}
        }});

        // Initialize
        showSlide(0);
    </script>
</body>
</html>'''

        return html_content

    def build_presentation(self, docx_path: str, title: str, voice: str = "onyx", max_slides: int = 10):
        """Build complete presentation"""

        print(f"\n{'='*60}")
        print(f"Building: {title}")
        print(f"{'='*60}\n")

        # Step 1: Parse content
        print(f"Step 1: Parsing DOCX content (max {max_slides} slides)...")
        slides = self.parse_docx_to_slides(docx_path, max_slides)
        print(f"  ✓ Created {len(slides)} slides\n")

        # Step 2: Generate voice
        print(f"Step 2: Generating voice narration (voice: {voice})...")
        audio_files = []
        for i, slide in enumerate(slides):
            script = self.create_narration_script(slide)
            if script:
                audio_file = self.generate_voice(script, i, voice)
                audio_files.append(audio_file if audio_file else "")
            else:
                audio_files.append("")
        print(f"  ✓ Generated {len([a for a in audio_files if a])} audio files\n")

        # Step 3: Generate HTML
        print("Step 3: Creating interactive HTML presentation...")
        html_content = self.generate_html_presentation(slides, title, audio_files)

        html_file = self.output_dir / "presentation.html"
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"  ✓ Created: {html_file}\n")

        return str(html_file)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Create ADIT voice presentations')
    parser.add_argument('topic', nargs='?', help='Topic number (e.g., 01, 02)')
    parser.add_argument('--voice', default='onyx', choices=['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'])
    parser.add_argument('--max-slides', type=int, default=10, help='Maximum slides (default: 10 for demo)')
    args = parser.parse_args()

    # Get API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("ERROR: OPENAI_API_KEY not set!")
        sys.exit(1)

    # Find DOCX file
    topic = args.topic or "02"
    notes_dir = Path("generated_notes")
    topic_dirs = list(notes_dir.glob(f"{topic}_*"))

    if not topic_dirs:
        print(f"No topic found for: {topic}")
        sys.exit(1)

    docx_files = list(topic_dirs[0].glob("**/*.docx"))
    if not docx_files:
        print("No DOCX files found!")
        sys.exit(1)

    docx_file = docx_files[0]
    title = docx_file.stem.replace("_", " ")

    print(f"\n✓ API Key: {api_key[:20]}...")
    print(f"✓ Voice: {args.voice}")
    print(f"✓ Max slides: {args.max_slides}")
    print(f"✓ Processing: {docx_file.name}\n")

    # Build
    builder = SimplePresentationBuilder(api_key)
    output = builder.build_presentation(docx_file, title, args.voice, args.max_slides)

    print("="*60)
    print("✅ SUCCESS!")
    print("="*60)
    print(f"\nOutput: {output}")
    print("\nTo view:")
    print("  cd presentation_output && python -m http.server 8000")
    print("  Open: http://localhost:8000/presentation.html")
    print("\nNavigation: ← → arrows, or click Next/Previous")
    print("Audio toggle: M key or click audio button")
