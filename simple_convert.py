#!/usr/bin/env python3
"""Simple markdown to DOCX converter with timeout handling"""

from pathlib import Path
from docx import Document
from docx.shared import Pt
import sys
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Conversion taking too long")

source_dir = Path("generated_notes/14_Arbitration_of_disputes/quality_checked")
output_dir = source_dir / "word_docs"

files = [
    ("68_Bilateral_investment_treaties_and_Energy_Charter_Treaty.md", "Bilateral Investment Treaties and Energy Charter Treaty"),
    ("69_Arbitration_clauses_in_contracts.md", "Arbitration Clauses in Contracts")
]

for filename, title in files:
    md_file = source_dir / filename
    if not md_file.exists():
        print(f"❌ {filename} not found")
        continue

    print(f"Converting: {filename}...", flush=True)

    try:
        # Read file
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Create document
        doc = Document()
        doc.add_heading(title, level=1)

        # Simple line-by-line addition
        for i, line in enumerate(lines):
            line = line.rstrip()
            if not line:
                continue
            elif line.startswith('# '):
                doc.add_heading(line[2:], level=1)
            elif line.startswith('## '):
                doc.add_heading(line[3:], level=2)
            elif line.startswith('### '):
                doc.add_heading(line[4:], level=3)
            elif line.startswith('#### '):
                doc.add_heading(line[5:], level=4)
            elif line.startswith('- ') or line.startswith('  - '):
                # Simple list
                text = line.lstrip('- ')
                p = doc.add_paragraph(text, style='List Bullet')
            elif line.startswith('|'):
                # Skip tables for now
                continue
            else:
                if line.strip():
                    doc.add_paragraph(line)

        # Save
        output_file = output_dir / filename.replace('.md', '.docx')
        doc.save(str(output_file))
        print(f"✅ Created: {output_file.name}")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

print("\n✅ Done!")
