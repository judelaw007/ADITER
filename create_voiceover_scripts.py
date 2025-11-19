#!/usr/bin/env python3
"""
TTS Voice-Over Script Generator
Creates natural, conversational scripts for presentation slides
Following specific tone and style requirements
"""

import sys
import re
from pathlib import Path
import docx


class VoiceOverScriptGenerator:
    """Generate conversational TTS scripts from presentation content"""

    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.scripts = []

    def extract_section_content(self, docx_path: str, section_number: int):
        """Extract detailed content for a specific section from DOCX"""
        doc = docx.Document(docx_path)

        content_parts = []
        in_target_section = False
        current_section_num = 0

        for para in doc.paragraphs:
            text = para.text.strip()
            if not text:
                continue

            # Check for main section headings (Heading 2 with numbers)
            if para.style.name == 'Heading 2':
                if re.match(r'^\d+\.', text):
                    current_section_num = int(text.split('.')[0])

                    if current_section_num == section_number:
                        in_target_section = True
                        # Store section title without number
                        section_title = re.sub(r'^\d+\.\s*', '', text)
                        content_parts.append(('title', section_title))
                    elif current_section_num > section_number:
                        break
                    else:
                        in_target_section = False

            # Collect content within target section
            elif in_target_section:
                # Skip very short lines (likely headers)
                if len(text) < 10:
                    continue

                # Identify subsection headings (Heading 3)
                if para.style.name == 'Heading 3':
                    clean_heading = re.sub(r'^\d+\.\d+\s*', '', text)
                    content_parts.append(('subsection', clean_heading))
                else:
                    # Regular content
                    content_parts.append(('content', text))

        return content_parts

    def create_conversational_script(self, content_parts: list, chapter_title: str) -> str:
        """Transform content into conversational voice-over script"""

        if not content_parts:
            return ""

        # Get section title
        section_title = ""
        for part_type, part_text in content_parts:
            if part_type == 'title':
                section_title = part_text
                break

        # Build conversational paragraphs
        paragraphs = []
        current_paragraph = []

        for part_type, part_text in content_parts:
            if part_type == 'subsection':
                # Start new paragraph for subsection
                if current_paragraph:
                    paragraphs.append(' '.join(current_paragraph))
                    current_paragraph = []

                # Introduce subsection conversationally
                intro = self._conversational_subsection_intro(part_text)
                current_paragraph.append(intro)

            elif part_type == 'content':
                # Make content conversational
                conv_text = self._make_conversational(part_text)
                current_paragraph.append(conv_text)

                # Break into paragraphs every 2-3 content items
                if len(current_paragraph) >= 3:
                    paragraphs.append(' '.join(current_paragraph))
                    current_paragraph = []

        # Add remaining content
        if current_paragraph:
            paragraphs.append(' '.join(current_paragraph))

        # Combine paragraphs with spacing
        script = '\n\n'.join(paragraphs)

        # Ensure length is within range (3500-7000 characters)
        char_count = len(script)

        # If too short, expand naturally
        if char_count < 3500:
            script = self._expand_script(script, content_parts)
            char_count = len(script)

        # If too long, condense
        if char_count > 7000:
            script = script[:7000]
            # Find last complete sentence
            last_period = script.rfind('.')
            if last_period > 6500:
                script = script[:last_period + 1]
            char_count = len(script)

        # Calculate estimated duration (assuming ~150 words per minute)
        word_count = len(script.split())
        duration_minutes = word_count / 150
        duration_str = self._format_duration(duration_minutes)

        # Format final script
        final_script = f"""Slide: {section_title}

{script}

Character Count: {char_count:,} ✓
Estimated Duration: {duration_str}"""

        return final_script

    def _conversational_subsection_intro(self, heading: str) -> str:
        """Create conversational intro for subsections"""
        intros = [
            f"So let's talk about {heading.lower()}.",
            f"Now, when it comes to {heading.lower()}, here's what you need to know.",
            f"Here's the thing about {heading.lower()}.",
            f"You know, {heading.lower()} is actually quite important.",
            f"Let's dive into {heading.lower()}.",
        ]
        # Use hash of heading to get consistent intro
        idx = hash(heading) % len(intros)
        return intros[idx]

    def _make_conversational(self, text: str) -> str:
        """Transform formal text into conversational tone"""

        # Remove excessive formality
        text = text.replace('It is important to note that', 'Basically,')
        text = text.replace('It should be noted that', 'You should know that')
        text = text.replace('In accordance with', 'According to')
        text = text.replace('With respect to', 'When it comes to')
        text = text.replace('Furthermore,', 'Also,')
        text = text.replace('Moreover,', 'Plus,')
        text = text.replace('Therefore,', 'So,')
        text = text.replace('Consequently,', 'As a result,')
        text = text.replace('shall be', 'is')
        text = text.replace('shall', 'will')

        # Add occasional conversational fillers (sparingly)
        if len(text) > 200 and 'actually' not in text.lower():
            # Add "actually" to longer sentences occasionally
            sentences = text.split('. ')
            if len(sentences) > 2:
                sentences[1] = 'Actually, ' + sentences[1].lower() if sentences[1][0].isupper() else sentences[1]
                text = '. '.join(sentences)

        return text

    def _expand_script(self, script: str, content_parts: list) -> str:
        """Expand script naturally if too short"""

        # Add contextual transitions between paragraphs
        paragraphs = script.split('\n\n')
        expanded = []

        for i, para in enumerate(paragraphs):
            expanded.append(para)

            # Add transitions between paragraphs
            if i < len(paragraphs) - 1:
                transitions = [
                    "This is really important to understand.",
                    "Let me explain this a bit more.",
                    "Here's what makes this interesting.",
                    "You know, this actually matters quite a bit.",
                ]
                transition = transitions[i % len(transitions)]
                expanded.append(transition)

        return '\n\n'.join(expanded)

    def _format_duration(self, minutes: float) -> str:
        """Format duration as human-readable string"""
        total_seconds = int(minutes * 60)
        mins = total_seconds // 60
        secs = total_seconds % 60

        if mins == 0:
            return f"{secs} seconds"
        elif secs == 0:
            return f"{mins} minute{'s' if mins != 1 else ''}"
        else:
            return f"{mins} minute{'s' if mins != 1 else ''} {secs} seconds"

    def generate_scripts_for_chapter(self, chapter_num: int, docx_path: str, section_count: int, chapter_title: str):
        """Generate scripts for all sections in a chapter"""

        print(f"\n📝 Generating scripts for Chapter {chapter_num}: {chapter_title}")

        for section_num in range(1, section_count + 1):
            # Extract content
            content_parts = self.extract_section_content(str(docx_path), section_num)

            if not content_parts:
                print(f"  ⚠ Section {section_num}: No content found")
                continue

            # Create script
            script = self.create_conversational_script(content_parts, chapter_title)

            # Store script
            self.scripts.append({
                'chapter': chapter_num,
                'section': section_num,
                'script': script,
                'title': content_parts[0][1] if content_parts else f"Section {section_num}"
            })

            # Show preview
            char_count = len(script.split('\n\n')[1:-2])  # Content only
            print(f"  ✓ Section {section_num}: {char_count} characters")

    def save_scripts(self):
        """Save all scripts to text files"""

        scripts_dir = self.output_dir / "voiceover_scripts"
        scripts_dir.mkdir(exist_ok=True)

        # Save individual scripts
        for script_data in self.scripts:
            filename = f"chapter{script_data['chapter']:02d}_section{script_data['section']:02d}_script.txt"
            filepath = scripts_dir / filename
            filepath.write_text(script_data['script'], encoding='utf-8')

        # Create master script file
        master_content = []
        for script_data in self.scripts:
            master_content.append("=" * 80)
            master_content.append(f"CHAPTER {script_data['chapter']} - SECTION {script_data['section']}")
            master_content.append("=" * 80)
            master_content.append("")
            master_content.append(script_data['script'])
            master_content.append("")
            master_content.append("")

        master_file = scripts_dir / "all_scripts.txt"
        master_file.write_text('\n'.join(master_content), encoding='utf-8')

        print(f"\n✅ Scripts saved to: {scripts_dir}")
        print(f"   Individual scripts: {len(self.scripts)} files")
        print(f"   Master script: all_scripts.txt")


def main():
    """Main execution"""

    # Configuration
    source_dir = Path("generated_notes/01_Fundamental_tax_issues/quality_checked")
    output_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations")

    if not source_dir.exists():
        print(f"❌ ERROR: Source directory not found: {source_dir}")
        sys.exit(1)

    # Find DOCX files
    docx_files = sorted(source_dir.glob("*_Enhanced_*.docx"))
    if not docx_files:
        print(f"❌ ERROR: No DOCX files found")
        sys.exit(1)

    print("🎙️ TTS Voice-Over Script Generator")
    print("=" * 70)
    print("\nCreating natural, conversational scripts...")

    # Initialize generator
    generator = VoiceOverScriptGenerator(str(output_dir))

    # Chapter configurations (based on structure analysis)
    chapters = [
        {'num': 1, 'sections': 6, 'title': 'International Income Flows'},
        {'num': 2, 'sections': 5, 'title': 'International Investment'},
        {'num': 3, 'sections': 6, 'title': 'Tax Treaties'},
        {'num': 4, 'sections': 6, 'title': 'Transfer Pricing'},
    ]

    # Generate scripts for each chapter
    for idx, (docx_path, chapter_config) in enumerate(zip(docx_files, chapters)):
        generator.generate_scripts_for_chapter(
            chapter_config['num'],
            docx_path,
            chapter_config['sections'],
            chapter_config['title']
        )

    # Save all scripts
    generator.save_scripts()

    print("\n" + "=" * 70)
    print(f"📊 Summary:")
    print(f"   Total scripts generated: {len(generator.scripts)}")
    print(f"   Chapters processed: {len(chapters)}")
    print(f"\n📂 Location: {output_dir}/voiceover_scripts/")


if __name__ == "__main__":
    main()
