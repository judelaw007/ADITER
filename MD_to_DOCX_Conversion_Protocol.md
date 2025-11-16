# Markdown to Word Document Conversion Protocol (Claude Code)

**Purpose:** Convert quality-checked markdown (.md) study note files into professionally formatted Word documents (.docx) with proper styling and layout.

---

## WORKFLOW FOR CLAUDE CODE

1. **Read the docx skill** (`/mnt/skills/public/docx/SKILL.md`) to understand Word document creation best practices
2. **Read the target .md file(s)** from quality_checked folder
3. **Convert to professional Word document** with proper formatting and styling
4. **Save .docx file** to the same quality_checked folder
5. **Provide summary** of files converted

---

## WORD DOCUMENT FORMATTING REQUIREMENTS

### Heading Styles:
- **Document title:** Heading 1 style (bold, 16pt)
- **Main sections (1., 2., 3.):** Heading 2 style (bold, 14pt)
- **Subsections (1.1, 1.2):** Heading 3 style (bold, 12pt)
- **Sub-subsections (1.1.1, 1.1.2):** Heading 4 style (bold, 11pt)

### Body Text:
- **Font:** Calibri or Arial, 11pt
- **Line spacing:** 1.15 or 1.5
- **Paragraph spacing:** 6pt after paragraphs
- **Alignment:** Left-aligned (not justified)

### Tables:
- Professional table styles with header rows
- Borders appropriate and consistent
- Sufficient cell padding for readability
- Column widths adjusted for content
- Alternating row colors for readability (optional)

### Lists:
- Bullet points for unordered lists
- Numbered lists for sequential steps
- Consistent indentation for nested lists
- Proper spacing between list items

### Examples and Calculations:
- Use text boxes or shaded backgrounds to distinguish from main text
- Clearly formatted with proper spacing
- Step-by-step calculations clearly presented
- Consider using bordered boxes with light gray background

### Special Elements:
- **Bold** key terms on first introduction
- *Italics* for emphasis (use sparingly)
- Tables for comparative data
- Clear section breaks between major topics
- Page breaks before major sections if needed

---

## FILE NAMING CONVENTION

**Output Format:** `[Original_Filename]_Enhanced.docx`

**Examples:**
- `Tax_and_fiscal_regimes_Royalties.md` → `Tax_and_fiscal_regimes_Royalties_Enhanced.docx`
- `Tax_and_fiscal_regimes_PSCs.md` → `Tax_and_fiscal_regimes_PSCs_Enhanced.docx`

**Save Location:** Same folder as source markdown file (quality_checked folder)

---

## EXECUTION STEPS

```bash
# Claude Code workflow:
# 1. Read /mnt/skills/public/docx/SKILL.md for Word document best practices
# 2. Read target .md file(s) from quality_checked folder
# 3. Convert markdown content to Word document with professional formatting
# 4. Apply proper styles (headings, tables, lists, spacing)
# 5. Save as [filename]_Enhanced.docx in quality_checked folder
# 6. Provide summary of conversions completed
```

---

## BATCH CONVERSION SUPPORT

This protocol supports converting **multiple files at once**.

**Usage:**
```
User: "Convert all files in quality_checked folder to Word documents"

Claude Code Actions:
1. ✅ Reads docx skill guidelines
2. ✅ Lists all .md files in quality_checked folder
3. ✅ Converts each file to .docx with professional formatting
4. ✅ Saves all .docx files to quality_checked folder
5. ✅ Provides summary of all conversions

Output: Multiple Word documents ready for publication
```

---

## EXAMPLE USAGE

### Single File Conversion
```
User: "Convert Tax_and_fiscal_regimes_Royalties.md to Word document"

Claude Code Actions:
1. ✅ Reads /mnt/skills/public/docx/SKILL.md
2. ✅ Reads quality_checked/Tax_and_fiscal_regimes_Royalties.md
3. ✅ Creates Word document with professional formatting
4. ✅ Applies proper heading styles, tables, and spacing
5. ✅ Saves as quality_checked/Tax_and_fiscal_regimes_Royalties_Enhanced.docx

Output: Professional Word document ready for publication
```

### Multiple Files Conversion
```
User: "Convert all tax notes to Word documents"

Claude Code Actions:
1. ✅ Reads docx skill guidelines
2. ✅ Identifies 6 markdown files in quality_checked folder
3. ✅ Converts each file with professional formatting
4. ✅ Saves 6 Word documents to quality_checked folder

Output: 6 professional Word documents ready for publication
```

---

## OUTPUT FORMAT

After completing conversion(s):

```markdown
## Conversion Complete

### Files Converted:
1. ✅ Tax_and_fiscal_regimes_Royalties.md → Tax_and_fiscal_regimes_Royalties_Enhanced.docx
2. ✅ Tax_and_fiscal_regimes_PSCs.md → Tax_and_fiscal_regimes_PSCs_Enhanced.docx
[... additional files ...]

### Summary:
- Total files converted: [X]
- All documents saved to: quality_checked/
- Formatting applied: Professional styles, tables, headings, spacing
- Status: Ready for review and publication

### Output Location:
📁 **Folder:** `generated_notes/02_Tax_and_fiscal_regimes/quality_checked/`
📄 **Format:** Professional Word documents (.docx)
✅ **Status:** Publication-ready
```

---

## QUALITY VERIFICATION CHECKLIST

Before finalizing each Word document, verify:

- [ ] Docx skill guidelines followed
- [ ] Professional heading styles applied (Heading 1, 2, 3, 4)
- [ ] Tables properly formatted with headers and borders
- [ ] Lists formatted with proper indentation
- [ ] Consistent font and spacing throughout
- [ ] Examples and calculations clearly distinguished
- [ ] Section numbering preserved (1., 1.1, 1.1.1)
- [ ] File saved with correct naming convention
- [ ] Document looks professional and publication-ready
- [ ] All markdown elements properly converted

---

## CRITICAL REQUIREMENTS

### Document Creation - Non-Negotiable:
- **MUST read docx skill first:** `/mnt/skills/public/docx/SKILL.md`
- **MUST create .docx file:** Professional Word document only
- **MUST apply professional formatting:** Proper styles, tables, spacing, layout
- **MUST be publication-ready:** Document should look professional and polished
- **MUST preserve all content:** No information lost in conversion

### Conversion Accuracy:
- All headings converted to proper Word heading styles
- All tables converted to Word table format with proper styling
- All lists converted to Word list format
- All bold/italic formatting preserved
- All section numbering preserved
- All content accuracy maintained

### Efficiency:
- Support batch conversion of multiple files
- Reuse docx skill knowledge across multiple conversions
- Provide clear summary of all conversions completed

---

**This protocol ensures markdown study notes are converted to professional, publication-ready Word documents that meet MojiTax quality standards.**
