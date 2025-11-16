# Quality Assurance & Enhancement Protocol for Study Notes (Claude Code)

**Purpose:** Systematically review and enhance markdown (.md) study note files using a 7-category quality framework. Claude Code will check each file against these criteria and produce enhanced markdown files with all improvements integrated.

---

## WORKFLOW FOR CLAUDE CODE

1. **Read the target .md file**
2. **Conduct 7-category quality check** (document issues internally)
3. **Apply all corrections and enhancements**
4. **Save enhanced .md file** to the designated quality_checked folder
5. **Provide summary** of changes made

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

## MARKDOWN FORMATTING STANDARDS

**Maintain professional markdown formatting:**

**Heading Hierarchy:**
- Document title: `# Title` (H1)
- Main sections (1., 2., 3.): `## 1. Section Name` (H2)
- Subsections (1.1, 1.2): `### 1.1 Subsection Name` (H3)
- Sub-subsections (1.1.1, 1.1.2): `#### 1.1.1 Sub-subsection Name` (H4)

**Text Formatting:**
- **Bold** key terms on first introduction
- *Italics* for emphasis (use sparingly)
- Proper paragraph spacing (blank line between paragraphs)

**Tables:**
- Use markdown table syntax with proper alignment
- Include header rows
- Ensure consistent column widths

**Lists:**
- Use `-` or `*` for unordered lists
- Use `1.`, `2.`, etc. for ordered lists
- Maintain consistent indentation for nested lists

**Code and Examples:**
- Use code blocks (```) for calculations and examples
- Use inline code (`) for technical terms and formulas

### File Naming Convention:
Save enhanced files with same name to the quality_checked folder

Example: `Tax_and_fiscal_regimes_Royalties.md` → `generated_notes/02_Tax_and_fiscal_regimes/quality_checked/Tax_and_fiscal_regimes_Royalties.md`

---

## OUTPUT FORMAT

After completing the quality check and saving the enhanced markdown file:

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
- Enhanced markdown file saved to quality_checked folder
- Key improvements: [2-3 sentence summary of major enhancements]

### Output Files:
📄 **Enhanced Markdown:** `quality_checked/[filename].md`
✅ **Status:** Ready for review
```

---

## CRITICAL REQUIREMENTS

### Enhancement Standards - Non-Negotiable:
- **MUST enhance existing content:** Do not rewrite - improve and fix issues while maintaining original structure
- **MUST save as .md file:** Enhanced markdown file saved to quality_checked folder
- **MUST maintain markdown formatting:** Proper headings, tables, lists, and spacing
- **MUST be review-ready:** Document should be clean, accurate, and well-structured

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
# 2. Execute quality check across all 7 categories (use web_search extensively)
# 3. Apply all fixes and enhancements to the content
# 4. Save enhanced markdown file to quality_checked folder
# 5. Provide detailed summary report
```

---

## EXAMPLE USAGE

```
User: "Run QA check on Tax_and_fiscal_regimes_Royalties.md"

Claude Code Actions:
1. ✅ Reads Tax_and_fiscal_regimes_Royalties.md
2. ✅ Conducts 7-category check with web searches
3. ✅ Fixes all issues found (rates, legislation, structure, etc.)
4. ✅ Saves enhanced file to quality_checked/Tax_and_fiscal_regimes_Royalties.md
5. ✅ Provides detailed summary of improvements

Output: Enhanced markdown file ready for review
```

---

## QUALITY VERIFICATION CHECKLIST

Before finalizing the enhanced markdown file, verify:

- [ ] All 7 categories checked and issues addressed
- [ ] Web searches completed for all rates and legislation
- [ ] Markdown formatting clean and consistent
- [ ] Proper heading hierarchy (H1 → H2 → H3 → H4)
- [ ] Tables properly formatted with markdown syntax
- [ ] Consistent formatting throughout
- [ ] No forward references remaining
- [ ] Section numbering correct (1., 1.1, 1.1.1)
- [ ] File saved to quality_checked folder
- [ ] Document is accurate, clear, and well-structured

---

**This protocol ensures every study note meets MojiTax quality standards and is delivered as an enhanced, review-ready markdown document.**
