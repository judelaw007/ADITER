#!/usr/bin/env python3
"""
ADIT Fundamental Tax Issues - Single Presentation Generator
Creates ONE comprehensive HTML5 presentation using HTML5_Templates design
"""

import sys
from pathlib import Path
import docx


class FundamentalTaxPresentationBuilder:
    """Build single comprehensive presentation for Fundamental Tax Issues"""

    def __init__(self):
        self.topics_data = []

    def extract_docx_content(self, docx_path: str):
        """Extract content from DOCX file"""
        doc = docx.Document(docx_path)

        topic_data = {
            'title': '',
            'sections': []
        }

        current_section = None

        for para in doc.paragraphs:
            text = para.text.strip()
            if not text:
                continue

            # Extract topic title from first heading
            if not topic_data['title'] and para.style.name == 'Heading 1':
                topic_data['title'] = text
                continue

            # Check if it's a heading (section)
            if para.style.name.startswith('Heading'):
                # Save previous section
                if current_section and current_section['points']:
                    topic_data['sections'].append(current_section)

                # Start new section
                current_section = {
                    'title': text,
                    'points': []
                }
            else:
                # Add content point
                if current_section:
                    current_section['points'].append(text)

        # Add last section
        if current_section and current_section['points']:
            topic_data['sections'].append(current_section)

        return topic_data

    def generate_html_presentation(self):
        """Generate single comprehensive HTML5 presentation"""

        # Build curriculum cards HTML
        curriculum_cards = ""
        for idx, topic in enumerate(self.topics_data, 1):
            section_count = len(topic['sections'])
            curriculum_cards += f'''
            <div class="module-card">
                <div class="module-header">
                    <div class="module-number">{idx}</div>
                    <div class="module-title">{topic['title']}</div>
                </div>
                <div class="module-body">
                    <p class="module-description">
                        Comprehensive coverage of {topic['title'].lower()} principles and applications.
                    </p>
                    <div class="module-meta">
                        <span>📚 {section_count} sections</span>
                    </div>
                    <a href="#topic-{idx}" class="module-link">View Topic</a>
                </div>
            </div>
'''

        # Build topic content sections HTML
        topic_sections = ""
        for topic_idx, topic in enumerate(self.topics_data, 1):
            topic_sections += f'''
        <div class="topic-section" id="topic-{topic_idx}">
            <div class="topic-header">
                <h2 class="topic-title">{topic_idx}. {topic['title']}</h2>
            </div>
'''

            for section in topic['sections'][:10]:  # Limit sections
                points_html = ""
                for point in section['points'][:8]:  # Limit points per section
                    clean_point = point.replace('<', '&lt;').replace('>', '&gt;')
                    points_html += f"                    <li>{clean_point}</li>\n"

                topic_sections += f'''
            <div class="content-section">
                <h3 class="section-title">{section['title']}</h3>
                <ul class="bullet-points">
{points_html}                </ul>
            </div>
'''

            topic_sections += '''        </div>
'''

        # Generate complete HTML
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fundamental Tax Issues - ADIT</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --primary: #003F87;
            --secondary: #0066CC;
            --accent: #FF6B35;
            --light-bg: #F8F9FA;
            --dark-text: #1A1F36;
            --light-text: #FFFFFF;
            --success: #27AE60;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: var(--light-bg);
            color: var(--dark-text);
            line-height: 1.6;
        }}

        /* Welcome Section */
        .welcome-section {{
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
        }}

        .welcome-section::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 600px;
            height: 600px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 50%;
        }}

        .welcome-content {{
            max-width: 800px;
            position: relative;
            z-index: 1;
        }}

        .logo-circle {{
            width: 120px;
            height: 120px;
            margin: 0 auto 30px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 60px;
        }}

        .welcome-content h1 {{
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 20px;
            letter-spacing: -0.5px;
        }}

        .welcome-content .tagline {{
            font-size: 20px;
            opacity: 0.95;
            margin-bottom: 30px;
        }}

        .welcome-content .description {{
            font-size: 16px;
            line-height: 1.8;
            opacity: 0.9;
            margin-bottom: 40px;
        }}

        .cta-button {{
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
        }}

        .cta-button:hover {{
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
        }}

        /* Curriculum Section */
        .curriculum-section {{
            padding: 80px 40px;
        }}

        .curriculum-section header {{
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--light-text);
            padding: 50px 40px;
            text-align: center;
            margin-bottom: 60px;
            border-radius: 12px;
        }}

        .curriculum-section header h2 {{
            font-size: 42px;
            font-weight: 700;
            margin-bottom: 10px;
        }}

        .curriculum-section header p {{
            font-size: 16px;
            opacity: 0.95;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .modules-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
        }}

        .module-card {{
            background: white;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
            border-left: 4px solid var(--accent);
        }}

        .module-card:hover {{
            transform: translateY(-12px);
            box-shadow: 0 15px 35px rgba(0, 63, 135, 0.15);
        }}

        .module-header {{
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--light-text);
            padding: 30px 25px;
            display: flex;
            align-items: center;
            gap: 15px;
        }}

        .module-number {{
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
        }}

        .module-title {{
            font-size: 18px;
            font-weight: 600;
        }}

        .module-body {{
            padding: 25px;
        }}

        .module-description {{
            font-size: 14px;
            color: #666;
            line-height: 1.7;
            margin-bottom: 15px;
        }}

        .module-meta {{
            display: flex;
            gap: 15px;
            font-size: 13px;
            color: #888;
            padding-top: 15px;
            border-top: 1px solid #eee;
            margin-bottom: 15px;
        }}

        .module-link {{
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
        }}

        .module-link:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(0, 63, 135, 0.3);
        }}

        /* Topic Sections */
        .topic-section {{
            padding: 60px 40px;
            max-width: 1000px;
            margin: 0 auto;
        }}

        .topic-header {{
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: var(--light-text);
            padding: 40px;
            border-radius: 12px;
            margin-bottom: 40px;
        }}

        .topic-title {{
            font-size: 36px;
            font-weight: 700;
        }}

        .content-section {{
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
            margin-bottom: 30px;
        }}

        .section-title {{
            color: var(--primary);
            font-size: 22px;
            font-weight: 700;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid var(--light-bg);
            position: relative;
        }}

        .section-title::before {{
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 50px;
            height: 2px;
            background: linear-gradient(90deg, var(--accent), var(--secondary));
        }}

        .bullet-points {{
            list-style: none;
            margin: 0;
            padding: 0;
        }}

        .bullet-points li {{
            display: flex;
            gap: 15px;
            margin-bottom: 16px;
            line-height: 1.7;
            color: #555;
            font-size: 15px;
        }}

        .bullet-points li::before {{
            content: '▸';
            color: var(--accent);
            font-weight: bold;
            flex-shrink: 0;
            font-size: 18px;
        }}

        /* Back to Top */
        .back-to-top {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            font-size: 24px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
            opacity: 0;
            pointer-events: none;
        }}

        .back-to-top.visible {{
            opacity: 1;
            pointer-events: auto;
        }}

        .back-to-top:hover {{
            transform: translateY(-4px);
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.3);
        }}

        @media (max-width: 768px) {{
            .welcome-content h1 {{
                font-size: 32px;
            }}

            .curriculum-section {{
                padding: 40px 20px;
            }}

            .curriculum-section header h2 {{
                font-size: 32px;
            }}

            .modules-grid {{
                grid-template-columns: 1fr;
            }}

            .topic-section {{
                padding: 40px 20px;
            }}

            .topic-title {{
                font-size: 28px;
            }}

            .content-section {{
                padding: 25px;
            }}
        }}
    </style>
</head>
<body>
    <!-- Welcome Section -->
    <section class="welcome-section" id="welcome">
        <div class="welcome-content">
            <div class="logo-circle">🏛️</div>
            <h1>Fundamental Tax Issues</h1>
            <p class="tagline">ADIT Module - Advanced International Taxation</p>
            <p class="description">
                Master the core principles of international taxation including income flows, investment structures,
                tax treaties, and transfer pricing methodologies essential for global tax professionals.
            </p>
            <a href="#curriculum" class="cta-button">Begin Learning</a>
        </div>
    </section>

    <!-- Curriculum Section -->
    <section class="curriculum-section" id="curriculum">
        <header>
            <h2>Course Curriculum</h2>
            <p>Four Core Topics in International Tax Fundamentals</p>
        </header>

        <div class="container">
            <div class="modules-grid">
{curriculum_cards}            </div>
        </div>
    </section>

    <!-- Topic Content Sections -->
{topic_sections}
    <!-- Back to Top Button -->
    <a href="#welcome" class="back-to-top" id="backToTop">↑</a>

    <script>
        // Back to top button visibility
        window.addEventListener('scroll', function() {{
            const backToTop = document.getElementById('backToTop');
            if (window.scrollY > 500) {{
                backToTop.classList.add('visible');
            }} else {{
                backToTop.classList.remove('visible');
            }}
        }});
    </script>
</body>
</html>'''

        return html


def main():
    """Main execution"""

    # Find DOCX files
    source_dir = Path("generated_notes/01_Fundamental_tax_issues/quality_checked")
    if not source_dir.exists():
        print(f"❌ ERROR: Directory not found: {source_dir}")
        sys.exit(1)

    docx_files = sorted(source_dir.glob("*_Enhanced_*.docx"))
    if not docx_files:
        print(f"❌ ERROR: No DOCX files found in {source_dir}")
        sys.exit(1)

    print("📚 Fundamental Tax Issues - Single Presentation Generator")
    print("=" * 60)

    # Initialize builder
    builder = FundamentalTaxPresentationBuilder()

    # Extract content from all DOCX files
    print(f"\n📖 Extracting content from {len(docx_files)} DOCX files...\n")
    for docx_path in docx_files:
        filename = docx_path.stem
        topic_name = filename.replace("Fundamental_tax_issues_", "").replace("_Enhanced_2025-11-14", "").replace("_", " ")

        print(f"  ✓ {topic_name}")
        topic_data = builder.extract_docx_content(str(docx_path))
        topic_data['title'] = topic_name.title()
        builder.topics_data.append(topic_data)

    # Generate HTML presentation
    print(f"\n🎨 Creating single comprehensive HTML5 presentation...")
    html_content = builder.generate_html_presentation()

    # Save presentation
    output_dir = Path("generated_notes/01_Fundamental_tax_issues/presentations")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✅ Presentation created successfully!")
    print("=" * 60)
    print(f"\n📍 Location: {output_file}")
    print(f"📊 Topics included: {len(builder.topics_data)}")
    print(f"📄 File size: {output_file.stat().st_size / 1024:.1f}KB")
    print(f"\n🌐 To view:")
    print(f"   cd {output_dir}")
    print("   python3 -m http.server 8000")
    print("   Open: http://localhost:8000")


if __name__ == "__main__":
    main()
