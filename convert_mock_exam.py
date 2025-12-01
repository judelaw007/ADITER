#!/usr/bin/env python3
"""
Script to convert Energy Resources Mock Exam to DOCX format
"""
from create_enhanced_docx import create_enhanced_document

# Read the markdown content
with open('Mock Exams/Energy_Resources_Mock_Exam_1.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Create the DOCX file
create_enhanced_document(
    markdown_content=content,
    title='Module 3.04 – Energy Resources Mock Exam',
    output_filename='Mock Exams/Energy_Resources_Mock_Exam_1.docx'
)

print("✅ Mock exam successfully created!")
