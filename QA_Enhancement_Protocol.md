# Quality Assurance & Enhancement Protocol for Study Notes (Claude Code)

**Purpose:** Systematically review and enhance markdown (.md) study note files using a 7-category quality framework. Claude Code will check each file against these criteria and produce professionally formatted Word documents (.docx) with all improvements integrated.

---

## WORKFLOW FOR CLAUDE CODE

1. **Read the target .md file**
2. **Read the docx skill** (`/mnt/skills/public/docx/SKILL.md`) to understand Word document creation best practices
3. **Conduct 7-category quality check** (document issues internally)
4. **Apply all corrections and enhancements**
5. **Create professional Word document** (.docx) with all improvements, proper formatting, and styling
6. **Provide summary** of changes made

---

## CATEGORY 1: INSTRUCTION FIDELITY

**Objective:** Verify the document delivers the intended educational content accurately.

**Check:**
- Document reflects correct study year/period - flag content referencing events after knowledge cutoff
- All essential topics for the subject matter are covered - no critical gaps
- Content stays within appropriate scope - no excessive tangential material

**Actions:**
- Remove post-cutoff content
- Flag missing critical topics (note in summary)
- Trim out-of-scope content

---

## CATEGORY 2: ACCURACY VERIFICATION

**Objective:** Ensure all factual claims, figures, rates, and calculations are correct.

**Check:**
- ALL tax rates, percentages, thresholds, regulatory figures verified via web_search against official sources
- Recurring figures consistent throughout document (same metric = same value everywhere)
- All mathematical calculations verified step-by-step
- No vague temporal references ("recently," "currently") - use exact years
- Case citations verified (real cases, accurate descriptions)

**Actions:**
- Correct all inaccurate rates/figures (cite source in comments if needed)
- Fix internal inconsistencies
- Correct calculation errors
- Replace vague dates with specific years
- Fix or remove incorrect case citations

---

## CATEGORY 3: LEGISLATION & AUTHORITY

**Objective:** Ensure legal foundations are accurate and properly referenced.

**Check:**
- All legislation correctly named with full titles and dates on first mention (e.g., "Income Tax Act 2023" not "ITA")
- Regulatory bodies accurately named with powers correctly attributed
- Statutory section references verified (exist, not repealed, accurately described)

**Actions:**
- Correct statute names and add dates
- Fix regulatory body attributions
- Update or remove superseded legislation references
- Verify section citations via web_search

---

## CATEGORY 4: REGIME CLARITY

**Objective:** Prevent confusion about which legal/contractual framework applies.

**Check:**
- Old vs new legislation distinctions explicit (context always clear which regime applies)
- Contractual/structural framework specifications clear (JV vs PSC, different entity types, etc.)
- Classification distinctions maintained (license types, entity categories clearly differentiated)

**Actions:**
- Add regime context where ambiguous (e.g., "under pre-2021 legislation" or "under new framework")
- Clarify which framework rules apply to
- Distinguish between different classifications consistently

---

## CATEGORY 5: FOCUS & CLARITY

**Objective:** Ensure document is lean, purposeful, exam-focused, with sequential knowledge building.

**Check:**
- No off-topic sections (Conclusions, Summaries, Future Trends, Key Challenges, Policy Recommendations)
- No meta-content ("this chapter," "this note," "word count," bibliographies, "as we will see")
- No repetition (concepts explained once; subsequent references use "see Section X.X")
- No vague statements ("generally," "many countries," "typically low" - must be specific)
- **CRITICAL: No forward references** - document must ONLY reference previous sections or previously developed notes, NEVER future content

**Actions:**
- Delete off-topic sections
- Remove all meta-content phrases
- Consolidate repeated explanations
- Make vague statements specific
- **Delete or rewrite all forward references** (e.g., "as we will discuss," "see next chapter," "covered later")

---

## CATEGORY 6: CONCEPTUAL DEPTH

**Objective:** Build understanding, not just memorization - students learn WHY and HOW, not just WHAT.

**Check:**
- Major fiscal mechanisms explained functionally (what it is, how it works, purpose) - not just rates
- Policy rationale provided for significant incentives/exemptions/structures
- Technical jargon defined or contextualized on first use, acronyms spelled out

**Actions:**
- Add functional explanations for mechanisms that only show rates
- Add brief policy rationale for major incentives (e.g., "exemption encourages high-risk exploration")
- Define technical terms on first use
- Spell out acronyms on first mention

---

## CATEGORY 7: ORGANIZATION & READABILITY

**Objective:** Ensure clean structure with natural flow.

**Check:**
- **Section numbering:** Proper hierarchical decimal format:
  - Main: 1., 2., 3.
  - Sub: 1.1, 1.2, 1.3
  - Sub-sub: 1.1.1, 1.1.2
  - Further: 1.1.1.1, etc.
  - No skipped numbers, correct parent numbering, consistent formatting
  
- **Heading hierarchy:** Proper nesting (H1 → H2 → H3 → H4), no skipped levels, no orphaned headings

- **Flow:** Smooth transitions between sections, logical progression, not choppy

- **Section length:** No sections under 100 words (too superficial) or over 1,500 words (needs subdivision)

**Actions:**
- Fix numbering sequence and hierarchy
- Correct heading levels
- Add transitions between disconnected sections
- Expand too-short sections or subdivide too-long sections

---

## WORD DOCUMENT CREATION REQUIREMENTS

**MANDATORY: After completing all quality checks and fixes, create a professional Word document (.docx) using the docx skill.**

### Formatting Standards:

**Heading Styles:**
- Document title: Heading 1 style (bold, 16pt)
- Main sections (1., 2., 3.): Heading 2 style (bold, 14pt)
- Subsections (1.1, 1.2): Heading 3 style (bold, 12pt)
- Sub-subsections (1.1.1, 1.1.2): Heading 4 style (bold, 11pt)

**Body Text:**
- Font: Calibri or Arial, 11pt
- Line spacing: 1.15 or 1.5
- Paragraph spacing: 6pt after paragraphs
- Alignment: Left-aligned (not justified)

**Tables:**
- Professional table styles with header rows
- Borders appropriate and consistent
- Sufficient cell padding for readability
- Column widths adjusted for content

**Lists:**
- Bullet points for unordered lists
- Numbered lists for sequential steps
- Consistent indentation

**Examples and Calculations:**
- Use text boxes or shaded backgrounds to distinguish from main text
- Clearly formatted with proper spacing
- Step-by-step calculations clearly presented

**Special Elements:**
- Bold key terms on first introduction
- Italics for emphasis (use sparingly)
- Tables for comparative data
- Clear section breaks between major topics

### File Naming Convention:
`[Original_Filename]_Enhanced_[YYYY-MM-DD].docx`

Example: `Nigeria_Petroleum_Fiscal_Regime_Enhanced_2025-01-15.docx`

---

## OUTPUT FORMAT

After completing the quality check and creating the Word document:

```markdown
## Quality Check Complete: [filename.md]

### Issues Found & Fixed:

**CATEGORY 1: INSTRUCTION FIDELITY**
- [X issues fixed]: [brief description]

**CATEGORY 2: ACCURACY VERIFICATION**
- [X issues fixed]: [specific corrections made with sources]

**CATEGORY 3: LEGISLATION & AUTHORITY**
- [X issues fixed]: [specific corrections made]

**CATEGORY 4: REGIME CLARITY**
- [X issues fixed]: [clarifications added]

**CATEGORY 5: FOCUS & CLARITY**
- [X issues fixed]: [deletions/consolidations made]
- Forward references removed: [X]

**CATEGORY 6: CONCEPTUAL DEPTH**
- [X enhancements added]: [explanations/rationale added]

**CATEGORY 7: ORGANIZATION & READABILITY**
- [X issues fixed]: [structure improvements]

### Summary:
- Total issues addressed: [X]
- Professional Word document created with proper formatting
- Key improvements: [2-3 sentence summary of major enhancements]

### Output Files:
📄 **Word Document:** `[filename]_Enhanced_[date].docx`
✅ **Status:** Ready for review and publication
```

---

## CRITICAL REQUIREMENTS

### Document Creation - Non-Negotiable:
- **MUST read docx skill first:** `/mnt/skills/public/docx/SKILL.md`
- **MUST create .docx file:** Not .md, not plain text - professional Word document only
- **MUST apply professional formatting:** Proper styles, tables, spacing, layout
- **MUST be publication-ready:** Document should look professional and polished

### Web Search Mandatory:
- **Category 2:** Verify EVERY tax rate, threshold, percentage against official sources
- **Category 3:** Verify EVERY statute name, date, section reference
- Document sources in your working notes

### Forward References - Zero Tolerance:
- Delete ANY reference to future sections, future chapters, or content not yet covered
- Replace with backward references or remove entirely
- Students must build knowledge sequentially

### Be Thorough:
- Address EVERY issue across all 7 categories
- Don't just flag - FIX
- Enhance while maintaining accuracy

---

## EXECUTION STEPS

```bash
# Claude Code workflow:
# 1. Read the target .md file
# 2. Read /mnt/skills/public/docx/SKILL.md for Word document best practices
# 3. Execute quality check across all 7 categories (use web_search extensively)
# 4. Apply all fixes and enhancements
# 5. Create professional Word document with proper formatting
# 6. Save as [filename]_Enhanced_[date].docx
# 7. Provide detailed summary report
```

---

## EXAMPLE USAGE

```
User: "Enhance Nigeria_Petroleum_Fiscal_Regime.md using the QA checklist"

Claude Code Actions:
1. ✅ Reads Nigeria_Petroleum_Fiscal_Regime.md
2. ✅ Reads /mnt/skills/public/docx/SKILL.md
3. ✅ Conducts 7-category check with web searches
4. ✅ Fixes all issues found (rates, legislation, structure, etc.)
5. ✅ Creates Nigeria_Petroleum_Fiscal_Regime_Enhanced_2025-01-15.docx
6. ✅ Applies professional formatting (headings, tables, spacing)
7. ✅ Provides detailed summary of improvements

Output: Professional Word document ready for publication
```

---

## QUALITY VERIFICATION CHECKLIST

Before finalizing the Word document, verify:

- [ ] All 7 categories checked and issues addressed
- [ ] Web searches completed for all rates and legislation
- [ ] Docx skill guidelines followed
- [ ] Professional heading styles applied (Heading 1, 2, 3, 4)
- [ ] Tables properly formatted with headers
- [ ] Consistent formatting throughout
- [ ] No forward references remaining
- [ ] Section numbering correct (1., 1.1, 1.1.1)
- [ ] File saved with correct naming convention
- [ ] Document looks professional and publication-ready

---

**This protocol ensures every study note meets MojiTax quality standards and is delivered as a professional, publication-ready Word document.**
