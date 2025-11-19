#!/usr/bin/env python3
"""
ADIT Presentation Suite Generator
Follows Prompts/PresentationSlides architecture exactly
Creates proper subject-level and per-chapter files with HTML5_Templates design
"""

import sys
import re
from pathlib import Path
import docx


class PresentationSuiteBuilder:
    """Build complete presentation suite following prompt architecture"""

    def __init__(self, subject_title: str, output_dir: str):
        self.subject_title = subject_title
        self.output_dir = Path(output_dir)
        self.chapters = []

    def extract_chapter_structure(self, docx_path: str):
        """Extract chapter structure from DOCX"""
        doc = docx.Document(docx_path)

        chapter = {
            'title': '',
            'sections': [],
            'all_content': []
        }

        current_section = None

        for para in doc.paragraphs:
            text = para.text.strip()
            if not text:
                continue

            # Get chapter title from first Heading 1
            if para.style.name == 'Heading 1' and not chapter['title']:
                chapter['title'] = text
                continue

            # Main sections (Heading 2 with numbers)
            if para.style.name == 'Heading 2':
                if re.match(r'^\d+\.', text):
                    # Save previous section
                    if current_section and current_section['content']:
                        chapter['sections'].append(current_section)

                    # Start new section
                    current_section = {
                        'title': text,
                        'content': [],
                        'number': int(text.split('.')[0])
                    }
            else:
                # Add content to current section
                if current_section:
                    current_section['content'].append(text)

        # Add last section
        if current_section and current_section['content']:
            chapter['sections'].append(current_section)

        return chapter

    def generate_index_html(self):
        """Generate subject welcome page (index.html)"""
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.subject_title} - ADIT</title>
    {self._get_common_styles()}
</head>
<body>
    <section class="welcome-section">
        <div class="welcome-content">
            <div class="logo-circle">🏛️</div>
            <h1>{self.subject_title}</h1>
            <p class="tagline">ADIT Module - Advanced International Taxation</p>
            <p class="description">
                Master the core principles of international taxation including income flows, investment structures,
                tax treaties, and transfer pricing methodologies essential for global tax professionals.
            </p>
            <a href="curriculum.html" class="cta-button">Begin Learning</a>
        </div>
    </section>
</body>
</html>'''
        return html

    def generate_curriculum_html(self):
        """Generate curriculum page listing all chapters"""
        cards_html = ""
        for idx, chapter in enumerate(self.chapters, 1):
            slug = self._slugify(chapter['title'])
            section_count = len(chapter['sections'])

            cards_html += f'''
            <div class="module-card">
                <div class="module-header">
                    <div class="module-number">{idx:02d}</div>
                    <div class="module-title">{chapter['title']}</div>
                </div>
                <div class="module-body">
                    <p class="module-description">
                        Comprehensive coverage of {chapter['title'].lower()} principles and applications.
                    </p>
                    <div class="module-meta">
                        <span>📚 {section_count} sections</span>
                    </div>
                    <a href="{idx:02d}-{slug}-topic.html" class="module-link">Start Chapter</a>
                </div>
            </div>
'''

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Curriculum - {self.subject_title}</title>
    {self._get_common_styles()}
</head>
<body>
    <header>
        <h1>Course Curriculum</h1>
        <p>{self.subject_title} - All Chapters</p>
    </header>

    <div class="container">
        <div class="modules-grid">
{cards_html}        </div>
    </div>

    <div class="back-link">
        <a href="index.html">← Back to Welcome</a>
    </div>
</body>
</html>'''
        return html

    def generate_topic_html(self, chapter_idx: int, chapter: dict):
        """Generate chapter topic page"""
        slug = self._slugify(chapter['title'])

        # Extract learning objectives from first section or create from sections
        objectives = ""
        for idx, section in enumerate(chapter['sections'][:6], 1):
            clean_title = re.sub(r'^\d+\.\s*', '', section['title'])
            objectives += f'                    <li>{clean_title}</li>\n'

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{chapter['title']} - {self.subject_title}</title>
    {self._get_common_styles()}
</head>
<body>
    <div class="progress-bar" style="width: 5%;"></div>

    <header>
        <h1>{chapter['title']}</h1>
        <div class="breadcrumb">{self.subject_title} → Chapter {chapter_idx}</div>
    </header>

    <div class="container">
        <div class="content-section">
            <h2 class="section-title">Chapter Overview</h2>
            <p class="content-text">
                This chapter provides comprehensive coverage of {chapter['title'].lower()},
                essential for understanding international tax principles in the energy resources sector.
            </p>

            <h3 class="subsection-title">Learning Objectives</h3>
            <ul class="objectives-list">
{objectives}            </ul>
        </div>

        <div class="navigation">
            <a href="curriculum.html" class="nav-button prev">← Back to Curriculum</a>
            <a href="{chapter_idx:02d}-{slug}-1-content.html" class="nav-button next">Begin Chapter →</a>
        </div>
    </div>
</body>
</html>'''
        return html

    def generate_content_html(self, chapter_idx: int, chapter: dict, section_idx: int):
        """Generate content page for a specific section"""
        slug = self._slugify(chapter['title'])
        section = chapter['sections'][section_idx - 1]

        # Clean section title (remove number)
        clean_title = re.sub(r'^\d+\.\s*', '', section['title'])

        # Generate bullets (4-6 per section, integrating subsections)
        bullets = ""
        for content in section['content'][:6]:
            clean_content = content.replace('<', '&lt;').replace('>', '&gt;')
            bullets += f'                    <li>{clean_content}</li>\n'

        # Determine next page
        if section_idx < len(chapter['sections']):
            next_page = f"{chapter_idx:02d}-{slug}-{section_idx + 1}-content.html"
            next_label = "Next Section →"
        else:
            next_page = f"{chapter_idx:02d}-{slug}-assessment.html"
            next_label = "Continue to Assessment →"

        # Previous page
        if section_idx > 1:
            prev_page = f"{chapter_idx:02d}-{slug}-{section_idx - 1}-content.html"
        else:
            prev_page = f"{chapter_idx:02d}-{slug}-topic.html"

        # Calculate progress
        progress = int(((section_idx + 1) / (len(chapter['sections']) + 3)) * 100)

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{clean_title} - {self.subject_title}</title>
    {self._get_common_styles()}
</head>
<body>
    <div class="progress-bar" style="width: {progress}%;"></div>

    <header>
        <h1>{clean_title}</h1>
        <div class="breadcrumb">{self.subject_title} → Chapter {chapter_idx} → Section {section_idx}</div>
    </header>

    <div class="container">
        <div class="content-section">
            <h2 class="section-title">{clean_title}</h2>
            <ul class="bullet-points">
{bullets}            </ul>
        </div>

        <div class="navigation">
            <a href="{prev_page}" class="nav-button prev">← Previous</a>
            <a href="{next_page}" class="nav-button next">{next_label}</a>
        </div>
    </div>
</body>
</html>'''
        return html

    def generate_assessment_html(self, chapter_idx: int, chapter: dict):
        """Generate chapter assessment"""
        slug = self._slugify(chapter['title'])
        progress = int(((len(chapter['sections']) + 2) / (len(chapter['sections']) + 3)) * 100)

        # Generate N questions (one per main section)
        questions = ""
        for idx, section in enumerate(chapter['sections'], 1):
            clean_title = re.sub(r'^\d+\.\s*', '', section['title'])
            questions += f'''
            <div class="question-card">
                <div class="question-number">Question {idx}</div>
                <div class="question-text">
                    Which of the following best describes {clean_title.lower()}?
                </div>
                <ul class="options">
                    <li class="option">
                        <input type="radio" id="q{idx}a" name="question{idx}">
                        <label for="q{idx}a">
                            <span class="custom-radio"></span>
                            Option A
                        </label>
                    </li>
                    <li class="option">
                        <input type="radio" id="q{idx}b" name="question{idx}">
                        <label for="q{idx}b">
                            <span class="custom-radio"></span>
                            Option B
                        </label>
                    </li>
                </ul>
            </div>
'''

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assessment - {chapter['title']}</title>
    {self._get_common_styles()}
</head>
<body>
    <div class="progress-bar" style="width: {progress}%;"></div>

    <header>
        <h1>Chapter Assessment</h1>
        <div class="breadcrumb">{self.subject_title} → Chapter {chapter_idx} → Assessment</div>
    </header>

    <div class="container">
        <div class="assessment-intro">
            <h2>Test Your Knowledge</h2>
            <p>Answer the following questions to complete this chapter.</p>
        </div>

{questions}
        <div class="navigation">
            <a href="{chapter_idx:02d}-{slug}-{len(chapter['sections'])}-content.html" class="nav-button prev">← Previous Section</a>
            <a href="{chapter_idx:02d}-{slug}-completion.html" class="nav-button next">Complete Chapter →</a>
        </div>
    </div>
</body>
</html>'''
        return html

    def generate_completion_html(self, chapter_idx: int, chapter: dict):
        """Generate chapter completion page"""
        slug = self._slugify(chapter['title'])

        # Determine next chapter or curriculum
        if chapter_idx < len(self.chapters):
            next_slug = self._slugify(self.chapters[chapter_idx]['title'])
            next_link = f"{chapter_idx + 1:02d}-{next_slug}-topic.html"
            next_label = "Next Chapter →"
        else:
            next_link = "curriculum.html"
            next_label = "Back to Curriculum"

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Completion - {chapter['title']}</title>
    {self._get_common_styles()}
</head>
<body>
    <div class="progress-bar" style="width: 100%;"></div>

    <header>
        <h1>Chapter Complete!</h1>
        <div class="breadcrumb">{self.subject_title} → Chapter {chapter_idx} → Completion</div>
    </header>

    <div class="container">
        <div class="completion-section">
            <div class="completion-icon">✓</div>
            <h2>Congratulations!</h2>
            <p>You've completed <strong>{chapter['title']}</strong></p>

            <div class="stats">
                <div class="stat">
                    <div class="stat-number">{len(chapter['sections'])}</div>
                    <div class="stat-label">Sections Completed</div>
                </div>
            </div>
        </div>

        <div class="navigation">
            <a href="curriculum.html" class="nav-button prev">← Back to Curriculum</a>
            <a href="{next_link}" class="nav-button next">{next_label}</a>
        </div>
    </div>
</body>
</html>'''
        return html

    def _slugify(self, text: str) -> str:
        """Convert text to URL-friendly slug"""
        # Remove common prefixes
        text = re.sub(r'^(Tax |International |Transfer )', '', text, flags=re.IGNORECASE)
        # Convert to lowercase and replace spaces/special chars
        slug = text.lower()
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[-\s]+', '-', slug)
        return slug.strip('-')[:50]

    def _get_common_styles(self) -> str:
        """Get common CSS styles for all pages"""
        return '''<style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #003F87;
            --secondary: #0066CC;
            --accent: #FF6B35;
            --light-bg: #F8F9FA;
            --dark-text: #1A1F36;
            --light-text: #FFFFFF;
            --success: #27AE60;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: var(--light-bg);
            color: var(--dark-text);
            line-height: 1.6;
        }

        /* Progress Bar */
        .progress-bar {
            position: fixed;
            top: 0;
            left: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--accent), var(--secondary));
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        /* Welcome Section */
        .welcome-section {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--light-text);
            text-align: center;
            padding: 60px 40px;
            position: relative;
            overflow: hidden;
        }

        .welcome-section::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 600px;
            height: 600px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 50%;
        }

        .welcome-content {
            max-width: 800px;
            position: relative;
            z-index: 1;
        }

        .logo-circle {
            width: 120px;
            height: 120px;
            margin: 0 auto 30px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 60px;
        }

        .welcome-content h1 {
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 20px;
            letter-spacing: -0.5px;
        }

        .welcome-content .tagline {
            font-size: 20px;
            opacity: 0.95;
            margin-bottom: 30px;
        }

        .welcome-content .description {
            font-size: 16px;
            line-height: 1.8;
            opacity: 0.9;
            margin-bottom: 40px;
        }

        .cta-button {
            display: inline-block;
            background: white;
            color: var(--primary);
            padding: 16px 50px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            font-size: 16px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
            transition: all 0.3s ease;
        }

        .cta-button:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
        }

        /* Header */
        header {
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--light-text);
            padding: 35px 40px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        header::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 300px;
            height: 300px;
            background: rgba(255, 255, 255, 0.08);
            border-radius: 50%;
        }

        header h1 {
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 8px;
            letter-spacing: -0.5px;
            position: relative;
            z-index: 1;
        }

        header p, header .breadcrumb {
            font-size: 14px;
            opacity: 0.9;
            position: relative;
            z-index: 1;
        }

        /* Container */
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 50px 40px;
        }

        /* Module Grid */
        .modules-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin: 50px 0;
        }

        .module-card {
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            border-left: 4px solid var(--accent);
        }

        .module-card:hover {
            transform: translateY(-12px);
            box-shadow: 0 15px 35px rgba(0, 63, 135, 0.15);
        }

        .module-header {
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--light-text);
            padding: 30px 25px;
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .module-number {
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: 700;
            flex-shrink: 0;
        }

        .module-title {
            font-size: 18px;
            font-weight: 600;
        }

        .module-body {
            padding: 25px;
        }

        .module-description {
            font-size: 14px;
            color: #666;
            line-height: 1.7;
            margin-bottom: 15px;
        }

        .module-meta {
            display: flex;
            gap: 15px;
            font-size: 13px;
            color: #888;
            padding-top: 15px;
            border-top: 1px solid #eee;
            margin-bottom: 15px;
        }

        .module-link {
            display: inline-block;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: var(--light-text);
            padding: 12px 24px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(0, 63, 135, 0.2);
        }

        .module-link:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(0, 63, 135, 0.3);
        }

        /* Content Section */
        .content-section {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            margin-bottom: 30px;
        }

        .section-title {
            color: var(--primary);
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid var(--light-bg);
            position: relative;
        }

        .section-title::before {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 50px;
            height: 2px;
            background: linear-gradient(90deg, var(--accent), var(--secondary));
        }

        .subsection-title {
            color: var(--secondary);
            font-size: 18px;
            font-weight: 600;
            margin: 25px 0 15px 0;
        }

        .content-text {
            color: #555;
            line-height: 1.8;
            font-size: 15px;
            margin-bottom: 20px;
        }

        /* Bullet Points */
        .bullet-points, .objectives-list {
            list-style: none;
            margin: 0;
            padding: 0;
        }

        .bullet-points li, .objectives-list li {
            display: flex;
            gap: 15px;
            margin-bottom: 16px;
            line-height: 1.7;
            color: #555;
            font-size: 15px;
        }

        .bullet-points li::before {
            content: '▸';
            color: var(--accent);
            font-weight: bold;
            flex-shrink: 0;
            font-size: 18px;
        }

        .objectives-list li::before {
            content: '✓';
            color: var(--success);
            font-weight: bold;
            flex-shrink: 0;
            font-size: 16px;
        }

        /* Navigation */
        .navigation {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 50px;
        }

        .nav-button {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 18px 30px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            font-size: 15px;
            transition: all 0.3s ease;
        }

        .nav-button.prev {
            background: white;
            color: var(--primary);
            border: 2px solid var(--primary);
        }

        .nav-button.prev:hover {
            background: var(--light-bg);
        }

        .nav-button.next {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: var(--light-text);
            box-shadow: 0 4px 12px rgba(0, 63, 135, 0.2);
        }

        .nav-button.next:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(0, 63, 135, 0.3);
        }

        /* Assessment */
        .assessment-intro {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            margin-bottom: 30px;
            text-align: center;
        }

        .assessment-intro h2 {
            color: var(--primary);
            margin-bottom: 10px;
        }

        .question-card {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            margin-bottom: 20px;
        }

        .question-number {
            color: var(--secondary);
            font-weight: 600;
            font-size: 14px;
            margin-bottom: 10px;
        }

        .question-text {
            color: var(--dark-text);
            font-size: 16px;
            font-weight: 500;
            margin-bottom: 20px;
        }

        .options {
            list-style: none;
            padding: 0;
        }

        .option {
            margin-bottom: 12px;
        }

        .option label {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.2s;
        }

        .option label:hover {
            background: var(--light-bg);
        }

        .custom-radio {
            width: 20px;
            height: 20px;
            border: 2px solid var(--secondary);
            border-radius: 50%;
            flex-shrink: 0;
        }

        /* Completion */
        .completion-section {
            background: white;
            padding: 50px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            text-align: center;
        }

        .completion-icon {
            width: 100px;
            height: 100px;
            margin: 0 auto 20px;
            background: linear-gradient(135deg, var(--success), #2ECC71);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 60px;
            color: white;
        }

        .completion-section h2 {
            color: var(--primary);
            margin-bottom: 15px;
        }

        .stats {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-top: 30px;
        }

        .stat {
            text-align: center;
        }

        .stat-number {
            font-size: 36px;
            font-weight: 700;
            color: var(--secondary);
        }

        .stat-label {
            font-size: 14px;
            color: #666;
        }

        /* Back Link */
        .back-link {
            text-align: center;
            margin-top: 40px;
        }

        .back-link a {
            color: var(--secondary);
            text-decoration: none;
            font-weight: 600;
        }

        .back-link a:hover {
            text-decoration: underline;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .welcome-content h1 {
                font-size: 32px;
            }

            header h1 {
                font-size: 26px;
            }

            .container {
                padding: 30px 20px;
            }

            .content-section {
                padding: 25px;
            }

            .modules-grid {
                grid-template-columns: 1fr;
            }

            .navigation {
                grid-template-columns: 1fr;
            }
        }
    </style>'''

    def build_suite(self):
        """Build complete presentation suite"""
        self.output_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n🎨 Building Presentation Suite: {self.subject_title}")
        print("=" * 70)

        # Generate subject-level files
        print("\n📄 Creating subject-level files...")

        index_html = self.generate_index_html()
        (self.output_dir / "index.html").write_text(index_html, encoding='utf-8')
        print("  ✓ index.html")

        curriculum_html = self.generate_curriculum_html()
        (self.output_dir / "curriculum.html").write_text(curriculum_html, encoding='utf-8')
        print("  ✓ curriculum.html")

        # Generate per-chapter files
        for chapter_idx, chapter in enumerate(self.chapters, 1):
            slug = self._slugify(chapter['title'])
            section_count = len(chapter['sections'])

            print(f"\n📘 Chapter {chapter_idx}: {chapter['title']}")
            print(f"   Sections: {section_count}")

            # Topic page
            topic_html = self.generate_topic_html(chapter_idx, chapter)
            (self.output_dir / f"{chapter_idx:02d}-{slug}-topic.html").write_text(topic_html, encoding='utf-8')
            print(f"  ✓ {chapter_idx:02d}-{slug}-topic.html")

            # Content pages (one per main section)
            for section_idx in range(1, section_count + 1):
                content_html = self.generate_content_html(chapter_idx, chapter, section_idx)
                (self.output_dir / f"{chapter_idx:02d}-{slug}-{section_idx}-content.html").write_text(content_html, encoding='utf-8')
                print(f"  ✓ {chapter_idx:02d}-{slug}-{section_idx}-content.html")

            # Assessment
            assessment_html = self.generate_assessment_html(chapter_idx, chapter)
            (self.output_dir / f"{chapter_idx:02d}-{slug}-assessment.html").write_text(assessment_html, encoding='utf-8')
            print(f"  ✓ {chapter_idx:02d}-{slug}-assessment.html")

            # Completion
            completion_html = self.generate_completion_html(chapter_idx, chapter)
            (self.output_dir / f"{chapter_idx:02d}-{slug}-completion.html").write_text(completion_html, encoding='utf-8')
            print(f"  ✓ {chapter_idx:02d}-{slug}-completion.html")

        print("\n" + "=" * 70)
        print("✅ Presentation Suite Complete!")
        print(f"\n📂 Output directory: {self.output_dir}")
        print(f"📊 Total files created: {len(list(self.output_dir.glob('*.html')))}")


def main():
    """Main execution"""

    # Configuration
    subject_title = "Fundamental Tax Issues"
    source_dir = Path("generated_notes/01_Fundamental_tax_issues/quality_checked")
    output_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations")

    if not source_dir.exists():
        print(f"❌ ERROR: Source directory not found: {source_dir}")
        sys.exit(1)

    # Find DOCX files
    docx_files = sorted(source_dir.glob("*_Enhanced_*.docx"))
    if not docx_files:
        print(f"❌ ERROR: No DOCX files found in {source_dir}")
        sys.exit(1)

    # Initialize builder
    builder = PresentationSuiteBuilder(subject_title, str(output_dir))

    # Extract all chapters
    print(f"\n📖 Extracting content from {len(docx_files)} chapters...")
    for docx_path in docx_files:
        chapter = builder.extract_chapter_structure(str(docx_path))
        builder.chapters.append(chapter)
        print(f"  ✓ {chapter['title']} ({len(chapter['sections'])} sections)")

    # Build suite
    builder.build_suite()

    print(f"\n🌐 To view:")
    print(f"   cd {output_dir}")
    print("   python3 -m http.server 8000")
    print("   Open: http://localhost:8000")


if __name__ == "__main__":
    main()
