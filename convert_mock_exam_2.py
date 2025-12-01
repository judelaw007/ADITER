#!/usr/bin/env python3
"""
Script to convert Energy Resources Mock Exam 2 to DOCX format
"""
from create_enhanced_docx import create_enhanced_document

# Read the markdown content
with open('Mock Exams/Energy_Resources_Mock_Exam_2.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Create the DOCX file
create_enhanced_document(
    markdown_content=content,
    title='Module 3.04 – Energy Resources Mock Exam 2',
    output_filename='Mock Exams/Energy_Resources_Mock_Exam_2.docx'
)

print("✅ Mock exam 2 successfully created!")
