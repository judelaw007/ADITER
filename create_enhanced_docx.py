#!/usr/bin/env python3
"""
Script to create enhanced Word documents from markdown content
Following QA Enhancement Protocol formatting standards
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import re

def create_enhanced_document(markdown_content, title, output_filename):
    """
    Create a professionally formatted Word document from markdown content

    Args:
        markdown_content: The enhanced markdown content
        title: Document title
        output_filename: Output .docx filename
    """
    doc = Document()

    # Set up styles
    setup_styles(doc)

    # Parse and add content
    parse_markdown_to_docx(doc, markdown_content, title)

    # Save document
    doc.save(output_filename)
    print(f"✅ Created: {output_filename}")

def setup_styles(doc):
    """Configure document styles per QA Enhancement Protocol"""
    styles = doc.styles

    # Configure Heading 1 (Document title)
    h1 = styles['Heading 1']
    h1.font.size = Pt(16)
    h1.font.bold = True
    h1.font.name = 'Calibri'

    # Configure Heading 2 (Main sections)
    h2 = styles['Heading 2']
    h2.font.size = Pt(14)
    h2.font.bold = True
    h2.font.name = 'Calibri'

    # Configure Heading 3 (Subsections)
    h3 = styles['Heading 3']
    h3.font.size = Pt(12)
    h3.font.bold = True
    h3.font.name = 'Calibri'

    # Configure Heading 4 (Sub-subsections)
    h4 = styles['Heading 4']
    h4.font.size = Pt(11)
    h4.font.bold = True
    h4.font.name = 'Calibri'

    # Configure Normal style
    normal = styles['Normal']
    normal.font.size = Pt(11)
    normal.font.name = 'Calibri'
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.15

def parse_markdown_to_docx(doc, content, title):
    """Parse markdown and add to document with proper formatting"""

    # Add title
    doc.add_heading(title, level=1)

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i].rstrip()

        # Skip empty lines at start
        if not line and i == 0:
            i += 1
            continue

        # Skip title line if it matches our title
        if line.startswith('# ') and title in line:
            i += 1
            continue

        # Headers
        if line.startswith('#### '):
            doc.add_heading(line[5:], level=4)
        elif line.startswith('### '):
            doc.add_heading(line[4:], level=3)
        elif line.startswith('## '):
            doc.add_heading(line[3:], level=2)
        elif line.startswith('# '):
            doc.add_heading(line[2:], level=1)

        # Tables
        elif line.startswith('|') and i + 1 < len(lines) and lines[i+1].startswith('|'):
            i = add_table(doc, lines, i)

        # Lists
        elif line.startswith('- ') or re.match(r'^\d+\.\s', line):
            i = add_list(doc, lines, i)

        # Code blocks
        elif line.startswith('```'):
            i = add_code_block(doc, lines, i)

        # Regular paragraphs
        elif line:
            p = doc.add_paragraph()
            add_formatted_text(p, line)

        i += 1

def add_table(doc, lines, start_idx):
    """Parse and add a markdown table"""
    table_lines = []
    i = start_idx

    # Collect table lines
    while i < len(lines) and lines[i].startswith('|'):
        table_lines.append(lines[i])
        i += 1

    if len(table_lines) < 2:
        return i

    # Parse table
    headers = [cell.strip() for cell in table_lines[0].split('|')[1:-1]]
    rows = []

    for line in table_lines[2:]:  # Skip header separator
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        if cells:
            rows.append(cells)

    # Create table
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.style = 'Light Grid Accent 1'

    # Add headers
    for idx, header in enumerate(headers):
        cell = table.rows[0].cells[idx]
        cell.text = header
        cell.paragraphs[0].runs[0].font.bold = True

    # Add rows
    for row_idx, row_data in enumerate(rows):
        for col_idx, cell_data in enumerate(row_data):
            table.rows[row_idx + 1].cells[col_idx].text = cell_data

    doc.add_paragraph()  # Space after table
    return i

def add_list(doc, lines, start_idx):
    """Parse and add a list"""
    i = start_idx

    while i < len(lines):
        line = lines[i].rstrip()

        if not line:
            break

        if line.startswith('- '):
            p = doc.add_paragraph(line[2:], style='List Bullet')
        elif re.match(r'^\d+\.\s', line):
            match = re.match(r'^\d+\.\s(.+)', line)
            if match:
                p = doc.add_paragraph(match.group(1), style='List Number')
        else:
            break

        i += 1

    return i

def add_code_block(doc, lines, start_idx):
    """Add a code block or example"""
    i = start_idx + 1
    code_lines = []

    while i < len(lines) and not lines[i].startswith('```'):
        code_lines.append(lines[i])
        i += 1

    # Add as shaded paragraph
    for code_line in code_lines:
        p = doc.add_paragraph(code_line)
        p.style = 'Normal'
        # Add shading would require more complex formatting

    return i + 1 if i < len(lines) else i

def add_formatted_text(paragraph, text):
    """Add text with bold and italic formatting"""
    # Simple bold detection with **text**
    parts = re.split(r'(\*\*[^*]+\*\*)', text)

    for part in parts:
        if part.startswith('**') and part.endswith('**'):
            run = paragraph.add_run(part[2:-2])
            run.font.bold = True
        else:
            # Check for italic
            italic_parts = re.split(r'(\*[^*]+\*)', part)
            for ipart in italic_parts:
                if ipart.startswith('*') and ipart.endswith('*') and not ipart.startswith('**'):
                    run = paragraph.add_run(ipart[1:-1])
                    run.font.italic = True
                else:
                    paragraph.add_run(ipart)


if __name__ == '__main__':
    print("Enhanced Word Document Creator")
    print("=" * 50)
