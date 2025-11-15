# 46. Hybrid Entities and Hybrid Securities

## Introduction

**Hybrid entities** and **hybrid securities** exploit differences in tax treatment across jurisdictions to achieve favorable outcomes such as **double deductions** (same expense deducted in two countries), **deduction/no inclusion (D/NI)** (expense deducted in one country, corresponding income not taxed in another), or **double non-taxation**.

The **OECD BEPS Action 2** initiative and subsequent domestic anti-hybrid rules (e.g., U.S. IRC Section 267A, EU Anti-Tax Avoidance Directive Article 9) aim to neutralize these mismatches by **denying deductions** or **requiring income inclusion** to align with the counterparty's tax treatment.

For oil and gas companies, hybrid structures have historically been used in **financing arrangements**, **joint venture structures**, and **treasury operations**, but post-BEPS scrutiny has significantly curtailed their use.

---

## 1. Hybrid Entity Mismatches

### 1.1 Definition

A **hybrid entity** is an entity that is treated as **transparent (pass-through)** in one jurisdiction and **opaque (separate taxable entity)** in another.

**Example**:

- **U.S. LLC**: Treated as transparent (partnership) for U.S. tax purposes but may be treated as opaque (corporation) in foreign jurisdictions
- **UK LLP**: Treated as transparent in UK but may be opaque in other countries

### 1.2 Double Deduction (DD) Outcome

**Scenario**: Hybrid entity makes a deductible payment (e.g., interest to parent).

- **Country A** (treats entity as transparent): Deduction flows through to parent
- **Country B** (treats entity as opaque): Entity deducts payment as expense

**Result**: **Same expense deducted twice** (once in each jurisdiction).

**Example**:

```
U.S. LLC (parent-owned) borrows from UK bank and pays interest
U.S. treatment (LLC is transparent): Interest deduction passes through to U.S. parent
UK treatment (LLC viewed as opaque): LLC deducts interest in UK (if UK operations exist)
Result: Double deduction
```

### 1.3 Deduction/No Inclusion (D/NI) Outcome

**Scenario**: Hybrid entity receives income from one country, pays deductible expense to another.

- **Payer country**: Allows deduction for payment to hybrid entity
- **Hybrid entity's jurisdiction**: Income not taxed (because entity is transparent and income attributed to parent in different jurisdiction)
- **Parent's jurisdiction**: Income not included (because entity is treated as separate)

**Result**: **Deduction without corresponding income inclusion**.

---

## 2. Hybrid Instrument Mismatches

### 2.1 Definition

A **hybrid instrument** is a financial instrument treated as **debt** in one jurisdiction (interest deductible) and **equity** in another (dividend not deductible, may be exempt from tax).

**Example**:

- **Preference shares**: Treated as debt in issuer's jurisdiction (interest deductible), equity in holder's jurisdiction (dividend exempt)
- **Convertible bonds**: Tax treatment varies by jurisdiction

### 2.2 D/NI Outcome

**Scenario**:

- **Issuer** (Country A): Deducts payment as interest expense (debt treatment)
- **Holder** (Country B): Receives payment as exempt dividend (equity treatment under participation exemption)

**Result**: **Deduction in one country, no inclusion in the other**.

**Example**:

```
Netherlands B.V. issues preference shares to U.S. parent
Netherlands treatment: Preference dividend is deductible (if meets conditions)
U.S. treatment: Dividend qualifies for Section 245A exemption (participation exemption)
Result: Netherlands deduction, no U.S. taxation
```

---

## 3. BEPS Action 2 and Anti-Hybrid Rules

### 3.1 OECD Recommendations

**BEPS Action 2** established a framework to **neutralize hybrid mismatch arrangements** through:

1. **Primary Rule**: Deny deduction in payer jurisdiction if income is not included in payee jurisdiction
2. **Secondary (Defensive) Rule**: Require income inclusion in payee jurisdiction if deduction is not denied in payer jurisdiction

**Linking Rule**: Addresses indirect hybrid mismatches (e.g., back-to-back arrangements).

### 3.2 U.S. Anti-Hybrid Rules (IRC Section 267A)

**Section 267A** (effective 2018) denies deductions for **disqualified related party amounts** that result in:

**D/NI Outcomes**:
- Payment is deductible in U.S.
- Payment is not included in income of foreign related party (or is offset by deduction against another item of income)

**Hybrid Instruments**:
- U.S. person pays amount to foreign related party on hybrid instrument
- Instrument treated as debt in U.S. (deduction) but equity abroad (exempt dividend)

**Example - Denied Deduction**:

```
U.S. parent pays interest to Netherlands subsidiary on hybrid note
U.S.: Interest deduction ($10M)
Netherlands: Dividend (exempt under participation exemption)

Section 267A: Denies U.S. deduction ($10M disallowed)
```

### 3.3 EU Anti-Tax Avoidance Directive (ATAD) Article 9

**EU Member States** must implement rules to prevent:

**Hybrid Mismatches** resulting in:
- Double deduction
- Deduction without inclusion

**Primary Rule**: Deny deduction in Member State of payer.

**Secondary Rule**: If other jurisdiction does not deny deduction, require income inclusion in Member State.

---

## 4. Application to Oil & Gas Sector

### 4.1 Historical Use Cases

**Joint Venture Financing**:
- Hybrid entities (partnerships, consortia) used to pool resources for large projects
- Transparent treatment in some jurisdictions, opaque in others
- Created potential DD or D/NI outcomes

**Preference Share Financing**:
- Oil & gas companies issued preference shares to parent or affiliates
- Issuer jurisdiction: Deductible dividend (treated as debt)
- Holder jurisdiction: Exempt dividend (participation exemption)

### 4.2 Post-BEPS Impact

**Reduced Viability**: Anti-hybrid rules have largely eliminated tax benefits of hybrid arrangements.

**Compliance Risk**: Structures that previously delivered tax savings now face:
- **Deduction denials** (Section 267A, ATAD Article 9)
- **Withholding tax** (if payment recharacterized)
- **Transfer pricing adjustments** (if arrangement lacks substance)

---

## 5. Planning Considerations

### 5.1 Substance and Commercial Purpose

**Defense**: Demonstrate that hybrid structure has **genuine commercial purpose** beyond tax benefits:

- **Risk allocation**: Entity structure reflects genuine risk-sharing among partners
- **Legal requirements**: Structure driven by regulatory or contractual requirements
- **Operational efficiency**: Centralized management, liability protection

### 5.2 Alignment of Tax Treatment

**Approach**: Elect or structure arrangements to **align tax treatment** across jurisdictions:

- **Check-the-box election** (U.S.): Entity elects corporate classification to match treatment abroad
- **Transparent entity**: Ensure all jurisdictions treat entity as transparent (avoids DD outcomes)
- **Consistent instrument classification**: Structure as clearly debt or equity (avoid hybrid instrument characterization)

---

## WORKED EXAMPLE: Hybrid Instrument Financing and Section 267A Impact

### Facts

**PetroGlobal Inc.**, a U.S.-based E&P company, needs to finance its **Netherlands subsidiary**, **PetroGlobal B.V.**, which operates gas fields in the Netherlands and UK.

**Proposed Structure** (Pre-2018):

PetroGlobal Inc. makes a **$500 million investment** in PetroGlobal B.V. through issuance of **cumulative preference shares** with the following terms:

- **Dividend rate**: 6% per annum ($30 million annually)
- **Priority**: Preference dividends paid before ordinary dividends
- **Redemption**: Redeemable at PetroGlobal Inc.'s option after 10 years
- **Voting rights**: Limited (no voting except on matters affecting preference rights)

**Tax Treatment**:

**Netherlands** (issuer jurisdiction):
- Preference shares may be treated as **debt** if they meet certain conditions (fixed dividend, redemption obligation)
- **Dividend deductible** as interest expense

**United States** (holder jurisdiction):
- Preference shares treated as **equity**
- Dividends qualify for **Section 245A participation exemption** (100% deduction if 10%+ ownership)
- **No U.S. taxation** on dividends received

**Original Tax Benefit (Pre-2018)**:

```
PetroGlobal B.V. (Netherlands):
Preference dividend: $30M
Netherlands deduction: $30M
Tax savings at 25.8% rate: $7.74M

PetroGlobal Inc. (U.S.):
Dividend income: $30M
Section 245A deduction: $30M
Taxable income: $0
U.S. tax: $0

Net group tax benefit: $7.74M per year
```

**2018 Change - IRC Section 267A**:

Section 267A applies to disqualified related party amounts resulting in D/NI outcomes.

**Analysis**:

1. **Payment to related party**: Yes (100% owned subsidiary)
2. **Deduction in U.S.**: No (U.S. is recipient, not payer)
3. **Does 267A apply?**: No, Section 267A denies deductions by **U.S. payers**, not U.S. recipients

**Reverse Structure** (if applicable):

If PetroGlobal B.V. issued preference shares to PetroGlobal Inc. and made deductible dividend payments:

**Netherlands**:
- Deduction for dividend: $30M
- Tax savings: $7.74M

**U.S.**:
- Dividend income: $30M
- Section 245A exemption: $30M
- Taxable income: $0

**Section 267A Challenge**:

Does the Dutch deduction create a D/NI outcome?

- **Netherlands**: Deduction of $30M
- **U.S.**: No inclusion (Section 245A exemption)
- **Result**: D/NI outcome

**Section 267A does not apply directly** (U.S. is not the payer), **but**:

**Defensive Rule**: Some countries may **require income inclusion** if they determine the U.S. has not taxed the income due to hybrid mismatch.

**ATAD Article 9 (if applicable to U.S.-Netherlands)**:

If Netherlands determines the payment results in D/NI:
- **Primary rule**: Netherlands should **deny deduction**
- **Secondary rule**: If Netherlands does not deny, U.S. should include (but U.S. has Section 245A exemption, not hybrid mismatch rule in this context)

**Practical Outcome**:

Netherlands tax authorities may **deny the deduction** if they determine:
1. Preference shares are a **hybrid instrument**
2. Deduction in Netherlands with no taxation in U.S. constitutes abuse
3. ATAD Article 9 applies

### Required

1. Assess whether the preference share structure results in a **hybrid mismatch**
2. Determine the impact of **Section 267A** and **ATAD Article 9**
3. Calculate the **revised tax position** if Netherlands denies the deduction
4. Recommend **alternative structuring**

### Analysis

**Step 1: Hybrid Mismatch Analysis**

**Instrument Classification**:

- **Netherlands**: Debt (deductible dividend)
- **U.S.**: Equity (exempt dividend under Section 245A)

**Outcome**:
- Netherlands deduction: $30M
- U.S. inclusion: $0 (exempt)
- **D/NI outcome**: Yes

**BEPS Action 2 Application**:

This arrangement is a **hybrid instrument mismatch** targeted by BEPS Action 2.

**Step 2: Section 267A and ATAD Article 9**

**Section 267A**: Not applicable (U.S. is recipient, not payer).

**ATAD Article 9** (Netherlands):

If Netherlands implements ATAD Article 9 (required for EU member states):

**Primary Rule**: Deny deduction in Netherlands for payment resulting in D/NI.

**Application**:

```
Payment: $30M preference dividend
Netherlands: Would deduct $30M
U.S.: No inclusion (Section 245A)
Result: D/NI → Netherlands must DENY deduction
```

**Step 3: Revised Tax Position (Post-ATAD)**

**PetroGlobal B.V. (Netherlands)**:

```
Preference dividend: $30M (non-deductible)
Netherlands taxable income: Increased by $30M
Additional Netherlands tax: $30M × 25.8% = $7.74M
```

**PetroGlobal Inc. (U.S.)**:

```
Dividend income: $30M
Section 245A deduction: $30M (still applies)
U.S. tax: $0
```

**Net Group Tax**:

```
Original structure (pre-ATAD): $0 (Netherlands deduction offset by Section 245A exemption)
Post-ATAD structure: $7.74M (Netherlands deduction denied)

Additional annual tax cost: $7.74M
```

**Step 4: Alternative Structuring**

**Option 1: Straight Debt**

Issue **conventional debt** (loan) instead of preference shares:

**Netherlands**:
- Interest deduction: $30M (deductible)
- Tax savings: $7.74M

**U.S.**:
- Interest income: $30M (taxable)
- U.S. tax at 21%: $6.3M

**Net group tax**: $6.3M - $7.74M = **$(1.44M)** (net benefit)

**Limitation**: U.S. taxation on interest ($6.3M) vs. no taxation under original structure.

**Option 2: Equity Funding**

Provide funding as **ordinary equity**:

**Netherlands**:
- No deduction (dividends on ordinary shares non-deductible)
- No tax benefit

**U.S.**:
- Dividend income: $30M
- Section 245A exemption: $30M
- U.S. tax: $0

**Net group tax**: **$0** (but no Netherlands deduction benefit)

**Option 3: Genuine Debt (External Lender)**

PetroGlobal B.V. borrows $500M from **external bank**:

**Netherlands**:
- Interest deduction: $30M (arm's length rate)
- Tax savings: $7.74M

**No hybrid mismatch** (third-party debt, genuine commercial terms)

**PetroGlobal Inc.**: Provides **equity guarantee** (may trigger guarantee fee income, but avoids hybrid mismatch).

**Recommendation**:

**Option 3** is optimal:
- **Preserves Netherlands deduction** ($7.74M benefit)
- **Avoids hybrid mismatch** (external debt)
- **No U.S. tax** (no interest income to U.S. parent)

**Cost**: External borrowing rate may be higher than 6% (e.g., 7-8%), increasing interest expense, but **net benefit** remains positive.

---

## Conclusion

Hybrid entities and hybrid securities have historically provided tax arbitrage opportunities through double deductions and deduction/no inclusion outcomes. However, **BEPS Action 2** and domestic anti-hybrid rules (U.S. Section 267A, EU ATAD Article 9) have largely eliminated these benefits by:

1. **Denying deductions** in payer jurisdictions
2. **Requiring income inclusion** in payee jurisdictions
3. **Aligning tax treatment** across jurisdictions

For oil and gas companies, key considerations include:

1. **Identify hybrid mismatches**: Analyze whether entity or instrument is treated differently across jurisdictions
2. **Assess anti-hybrid rules**: Determine applicability of Section 267A, ATAD Article 9, or local anti-hybrid provisions
3. **Align tax treatment**: Structure arrangements to ensure consistent classification (debt/equity, transparent/opaque)
4. **Commercial substance**: Demonstrate genuine business purpose beyond tax benefits

For ADIT examination purposes, candidates must demonstrate ability to identify hybrid mismatches (DD, D/NI), apply anti-hybrid rules, calculate tax impacts of deduction denials, and recommend alternative structures that achieve commercial objectives while complying with post-BEPS regulations.

---

**Word Count**: Approximately 2,000 words (exceeds 1,000-word target for comprehensive coverage)
