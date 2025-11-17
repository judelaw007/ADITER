# 44. Thin Capitalisation

## Introduction

**Thin capitalization** (thin cap) refers to a situation where an entity is financed with **excessive debt** relative to **equity**, typically through related-party borrowing. Multinational oil and gas companies may structure subsidiaries with high debt-to-equity ratios to maximize **interest deductions** in high-tax jurisdictions while concentrating profits in low-tax jurisdictions.

Tax authorities combat this through **thin capitalization rules** that limit interest deductibility when debt levels are deemed excessive. The **OECD BEPS Action 4** initiative has led to widespread adoption of **earnings stripping rules** limiting interest deductions to a percentage of **EBITDA** (typically **10-30%**), supplementing or replacing traditional debt-to-equity ratio tests.

---

## 1. Traditional Thin Capitalization Rules

### 1.1 Debt-to-Equity Ratio Tests

Some jurisdictions impose **maximum debt-to-equity ratios** beyond which interest on excess debt is non-deductible. However, many countries have transitioned to earnings-stripping rules (EBITDA-based limits) following OECD BEPS Action 4.

**Historical and Current Examples**:

| Jurisdiction | Debt-to-Equity Ratio | Current Status | Excess Interest Treatment |
|--------------|----------------------|----------------|---------------------------|
| **China** | 2:1 (non-financial) | Active | Non-deductible |
| **Brazil** | 2:1 (related parties) | Active | Non-deductible |
| **Germany** | 1.5:1 (historical) | Replaced 2008 with EBITDA rule | N/A - now uses 30% EBITDA |
| **Spain** | N/A | Uses 30% EBITDA (effective 2024) | N/A - earnings stripping rule |
| **India** | N/A | Uses 30% EBITDA (Section 94B, Finance Act 2017) | N/A - earnings stripping rule |

**Calculation**:

```
Debt-to-Equity Ratio = Related-Party Debt / Equity

If actual ratio > Safe harbor ratio, excess interest is disallowed:

Excess Debt = Total Debt - (Equity × Safe Harbor Ratio)
Disallowed Interest = Total Interest × (Excess Debt / Total Debt)
```

**Example**:

```
Brazilian subsidiary:
Related-party debt: $200M
Equity: $50M
Debt-to-equity ratio: 4:1

Brazil safe harbor: 2:1
Permitted debt: $50M × 2 = $100M
Excess debt: $200M - $100M = $100M

Total interest expense: $16M (at 8%)
Disallowed interest: $16M × ($100M / $200M) = $8M
Allowed deduction: $8M
```

### 1.2 Limitations of Ratio Tests

**Issues**:

1. **Industry differences**: Capital-intensive industries (oil & gas) naturally have higher leverage than service industries
2. **Business cycle**: Ratios fluctuate with commodity prices affecting equity values
3. **Easily circumvented**: Increasing equity slightly can restore ratio compliance

---

## 2. BEPS Action 4: Earnings Stripping Rules

### 2.1 Fixed Ratio Rule

**OECD BEPS Action 4 (2015-2016)**: Recommends limiting interest deductions to **10-30% of EBITDA**, with countries selecting where within this range to set the limit.

**Most Common**: **30% of EBITDA** (adopted by EU under Anti-Tax Avoidance Directive (ATAD), UK, Germany, Netherlands, Spain, India, and others)

**Formula**:

```
Maximum Deductible Interest = EBITDA × 30%

Where:
EBITDA = Earnings Before Interest, Tax, Depreciation, Amortization

If actual interest expense > limit, excess is disallowed (but may be carried forward)
```

**Advantages**:

- **Economic link**: Ties interest deductibility to economic activity
- **Uniform application**: Easier to apply than debt-to-equity ratios
- **Cyclical adjustment**: Automatically adjusts with profitability

### 2.2 Group Ratio Rule

**Alternative Test**: Entity may deduct more interest if it can demonstrate that the **group's** net interest/EBITDA ratio exceeds the entity's ratio.

**Purpose**: Allows highly-leveraged groups to deduct interest up to the group's consolidated ratio, provided the entity's ratio doesn't exceed it.

**Example**:

```
Entity A interest expense: $40M
Entity A EBITDA: $100M
Entity A ratio: 40%

Fixed ratio rule (30%): Would disallow $10M

Group consolidated:
Group interest expense: $300M
Group EBITDA: $1,000M
Group ratio: 30%

Entity A's 40% > Group's 30% → Fixed ratio applies
If Entity A's ratio were ≤ Group's ratio, Entity A could deduct full $40M
```

---

## 3. Application to Oil & Gas Sector

### 3.1 High Leverage in Upstream

**Oil & gas upstream operations** are capital-intensive, requiring significant debt financing for:

- **Exploration and appraisal**: Seismic surveys, drilling exploratory wells
- **Development capex**: Platform construction, subsea infrastructure, pipelines
- **Acquisitions**: Purchasing reserves, concessions, or companies

**Typical Leverage**: Debt-to-equity ratios of **2:1 to 4:1** are common and commercially justifiable.

**Challenge**: Thin cap rules may disallow commercially reasonable interest deductions, creating cashflow pressure.

### 3.2 EBITDA Volatility

**Commodity Price Sensitivity**: EBITDA fluctuates significantly with oil and gas prices.

**Impact on Interest Limitation**:

| Oil Price | Annual EBITDA | 30% Limit | Interest Expense | Disallowed |
|-----------|---------------|-----------|------------------|------------|
| **$80/bbl** | $150M | $45M | $40M | $0 |
| **$50/bbl** | $80M | $24M | $40M | $16M |

**Result**: In low-price environment, significant interest becomes non-deductible despite unchanged debt levels.

---

## 4. Exemptions and Carve-Outs

### 4.1 De Minimis Thresholds

Many jurisdictions provide **exemptions** for:

- **Small entities**: Total interest expense below threshold (e.g., EUR 3 million under EU Anti-Tax Avoidance Directive (ATAD) Article 4, allowing Member States to permit full deduction of exceeding borrowing costs up to this amount)
- **Standalone entities**: No related-party debt
- **Financial institutions**: Banks, insurance companies (subject to sector-specific rules)

### 4.2 Public Infrastructure Exemption

**OECD BEPS Action 4**: Recommends exemption for **public benefit infrastructure projects** with long-term, non-recourse debt.

**Relevance to Oil & Gas**: Large **LNG projects**, **pipelines**, and **offshore platforms** with **project finance** structures may qualify.

### 4.3 Interest Carry-Forward

**Most jurisdictions** allow **disallowed interest** to be **carried forward** and deducted in future years when EBITDA is higher.

**Example**:

```
Year 1: Interest $40M, EBITDA $80M, Limit $24M → $16M disallowed
Year 2: Interest $40M, EBITDA $150M, Limit $45M → $40M + $16M carryforward = $56M

Can deduct: $45M in Year 2
Remaining carryforward: $56M - $45M = $11M (to Year 3)
```

---

## 5. Planning Considerations

### 5.1 Equity vs. Debt Financing

**Trade-Off**:

- **Debt**: Interest deductible (subject to thin cap), but dividend repatriation not deductible
- **Equity**: No interest deduction, but may benefit from participation exemption on dividends

**Optimization**: Model optimal debt-to-equity ratio considering:
- **Thin cap limits** (debt-to-equity and EBITDA tests)
- **CFC rules** (excessive passive income from interest)
- **WHT on dividends vs. interest**

### 5.2 Third-Party Debt Push-Down

**Structure**: Parent borrows externally and **contributes** proceeds as equity to subsidiary, avoiding related-party debt classification.

**Limitation**: Some thin cap rules apply to **all debt** (not just related-party), particularly EBITDA-based rules.

---

## WORKED EXAMPLE: Thin Capitalization Impact on Oil & Gas Subsidiary

### Facts

**GlobalPetro Inc.** (U.S. parent) owns **GlobalPetro Brasil Ltda.**, a Brazilian E&P subsidiary operating in the Santos Basin. The subsidiary was capitalized as follows:

- **Equity**: $100 million (from parent)
- **Intercompany debt**: $400 million (from parent at 8% interest)
- **Total capitalization**: $500 million

**Debt-to-Equity Ratio**: 4:1

**Annual Financial Results (2024)**:

| Item | Amount |
|------|--------|
| Revenue | $300M |
| Operating expenses (excluding interest, depreciation) | $150M |
| Depreciation | $50M |
| **EBITDA** | **$150M** |
| Interest expense (to parent) | $32M |
| **EBT** | $118M |

**Brazil Tax Rules**:

1. **Thin Cap Ratio**: 2:1 (debt-to-equity)
2. **BEPS-Style Earnings Stripping**: 30% of EBITDA (recently implemented)
3. **Corporate tax rate**: 34%

**Parent Loan Terms**:
- **Interest rate**: 8% (arm's length, benchmarked to comparable loans)
- **No guarantee** from parent (subsidiary standalone credit)

### Required

1. Calculate **disallowed interest** under Brazil's thin cap rules
2. Calculate **disallowed interest** under the EBITDA limitation rule
3. Determine the **additional Brazilian tax** due to interest disallowance
4. Evaluate **restructuring options** to optimize tax position

### Analysis

**Step 1: Thin Cap Rule (Debt-to-Equity Ratio Test)**

```
Actual debt-to-equity ratio: $400M / $100M = 4:1
Brazil safe harbor: 2:1

Maximum permitted debt: $100M × 2 = $200M
Excess debt: $400M - $200M = $200M

Total interest: $32M
Disallowed interest (thin cap): $32M × ($200M / $400M) = $16M
Allowed deduction: $16M
```

**Step 2: EBITDA Limitation Rule**

```
EBITDA: $150M
30% EBITDA limit: $150M × 30% = $45M

Actual interest: $32M
Since $32M < $45M → Fully deductible under EBITDA rule
```

**Step 3: Applicable Rule**

**Brazil applies the MORE RESTRICTIVE rule**:

- Thin cap rule: Allows $16M
- EBITDA rule: Allows $32M

**Result**: **$16M interest allowed**, **$16M disallowed** under thin cap rule.

**Step 4: Tax Impact**

**Original Tax Calculation (No Restriction)**:

```
EBITDA: $150M
Less: Depreciation: $50M
EBIT: $100M
Less: Interest: $32M
EBT: $68M
Brazil tax at 34%: $23.12M
```

**With Thin Cap Restriction**:

```
EBITDA: $150M
Less: Depreciation: $50M
EBIT: $100M
Less: Allowed interest: $16M
Adjusted EBT: $84M
Brazil tax at 34%: $28.56M

Additional tax: $28.56M - $23.12M = $5.44M
```

**Step 5: Restructuring Options**

**Option 1: Increase Equity to $200M**

```
New equity: $200M
Debt: $400M
Debt-to-equity ratio: 2:1 (complies with thin cap)

All $32M interest deductible
Tax savings: $5.44M

Cost: Parent must inject additional $100M equity
Opportunity cost: If parent's cost of capital is 10%, annual cost = $10M
Not economically attractive
```

**Option 2: Reduce Debt to $200M**

```
Equity: $100M
Debt: $200M
Debt-to-equity ratio: 2:1

Interest expense: $200M × 8% = $16M (fully deductible)
Tax savings: $5.44M

Cost: Must repay $200M to parent or refinance externally
If external borrowing rate is higher (10%): $200M × 10% = $20M > $16M (increases total interest cost)
```

**Option 3: Hybrid Instrument (Debt/Equity)**

Issue **$200M of preference shares** (treated as equity for thin cap purposes, but yield is deductible):

```
Equity (including prefs): $300M
Debt: $200M
Debt-to-equity ratio: 0.67:1 (complies)

Interest on debt: $16M (deductible)
Preference dividend: $200M × 8% = $16M (if deductible) = $32M total
```

**Caution**: Brazil may not allow preference dividend deduction (depends on specific terms and classification).

**Option 4: Accept Restriction and Claim Carryforward**

```
Disallowed interest in 2024: $16M
Carry forward to future years when EBITDA is higher

If 2025 EBITDA = $200M:
2025 limit: $200M × 30% = $60M
2025 interest: $32M
Available capacity: $60M - $32M = $28M
Can utilize full $16M carryforward
```

**Payback Period**: Depends on future EBITDA levels and oil prices.

### Recommendation

**Option 4 is most practical**: Accept the $5.44M additional tax in 2024 and carry forward the $16M disallowed interest.

**Rationale**:

1. **No immediate cash outlay**: Avoid $100M equity injection or $200M debt refinancing
2. **Commodity cycle**: Oil prices expected to recover; EBITDA in 2025-2026 may allow full carryforward utilization
3. **Temporary impact**: Thin cap restriction is cyclical, not permanent
4. **Cost-benefit**: $5.44M tax cost is less than opportunity cost of restructuring ($10M for equity injection)

**Long-Term Planning**:

- **Monitor EBITDA**: If sustained low EBITDA expected, reconsider capital structure
- **Third-party debt**: Consider replacing $200M of intercompany debt with **external debt** (may not be subject to thin cap in some jurisdictions, though Brazil's EBITDA rule applies to all debt)
- **Advocate for exemptions**: Engage with Brazilian tax authorities on upstream-specific exemptions (given capital intensity of oil & gas)

---
