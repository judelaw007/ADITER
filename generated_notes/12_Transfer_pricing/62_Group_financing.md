# 62. Group Financing

## 1. Introduction

**Group financing** arrangements are critical in capital-intensive oil and gas operations, involving **intercompany loans**, **cash pooling**, **guarantees**, **back-to-back financing**, and **centralized treasury operations**. Multinational groups establish **group treasury companies** in favorable jurisdictions to manage **liquidity**, **foreign exchange risk**, **interest rate risk**, and **optimize funding costs**.

From a transfer pricing perspective, the key issues are: (1) What is the **arm's length interest rate** on intercompany loans? (2) Should subsidiaries pay **guarantee fees** to parent (see Chapter 57)? (3) How should **treasury services** be compensated? (4) Are financing arrangements subject to **thin capitalization rules** or **interest limitation rules**?

This chapter examines **transfer pricing methods for intercompany loans** (credit rating adjustment, CUT method), **arm's length interest rate determination**, **debt vs. equity characterization**, **thin capitalization rules**, **OECD BEPS Action 4** (interest limitations), **treasury company remuneration**, and **documentation requirements**.

---

## 2. Arm's Length Interest Rate Determination

### 2.1 Credit Rating Adjustment Method

**Principle**: Determine borrower's **standalone credit rating** (without parent support); apply market interest rate for that credit rating.

**Steps**:

1. **Determine borrower's standalone credit rating**: Use credit rating agency methodology (S&P, Moody's, Fitch) or financial analysis
2. **Identify market interest rate** for that credit rating (based on comparable bonds, bank loans)
3. **Adjust for loan-specific factors**: Maturity, currency, collateral, covenants

**Example**:

```
Borrower: OpCo (Nigeria subsidiary)
Standalone credit rating: BB (based on financial ratios, country risk)
Loan terms: $100M, 5-year term, USD, unsecured

Market interest rates (2025):
- BB-rated corporate bonds (5-year, USD): 8.0-9.0%
- Selected arm's length rate: 8.5%

Intercompany loan interest rate: 8.5%
Annual interest expense: $100M × 8.5% = $8.5 million
```

**Credit rating determination** (if no formal rating exists):

**Financial ratio analysis**:

| **Ratio** | **OpCo (Nigeria)** | **Rating Indication** |
|---|---|---|
| **Interest coverage** (EBIT / Interest) | 3.5x | BB+ to BBB- |
| **Debt / EBITDA** | 3.0x | BB to BB+ |
| **Debt / Equity** | 1.5:1 | BBB- to BBB |
| **Country risk** (Nigeria) | High | Downgrade by 2-3 notches |

**Conclusion**: Standalone credit rating = **BB** (after adjusting for Nigeria country risk)

### 2.2 Comparable Uncontrolled Transaction (CUT) Method

**Application**: Compare intercompany loan interest rate to interest rate on **comparable external loans**.

**Example**:

```
OpCo (Brazil) borrows $200M from Parent (UK) at 7.0% interest.

External comparable:
- OpCo also borrowed $50M from HSBC (independent bank) at 7.5% interest (same year, similar terms)

Transfer pricing analysis:
- Internal CUT: OpCo borrows from independent bank at 7.5%
- Intercompany rate (7.0%) is **below** external rate (7.5%)
- Conclusion: 7.0% is arm's length (conservative; within range)

Alternative analysis:
- If HSBC loan has parent guarantee (reducing rate to 7.5%), but intercompany loan has no guarantee, then 7.0% may be too low
- Adjustment: Intercompany loan should be at higher rate (e.g., 8.0-8.5%) reflecting absence of guarantee
```

### 2.3 LIBOR/SOFR Plus Spread

**Market practice**: Intercompany loans priced as **LIBOR + spread** (historical) or **SOFR + spread** (post-LIBOR transition).

**Formula**:
```
Interest Rate = Base Rate (LIBOR/SOFR) + Credit Spread

Credit spread reflects:
- Borrower's credit risk
- Country risk
- Loan-specific factors (maturity, collateral, covenants)
```

**Typical credit spreads** (over LIBOR/SOFR):

| **Credit Rating** | **5-Year Spread** |
|---|---|
| **AAA** | +0.5% to 1.0% |
| **AA** | +1.0% to 1.5% |
| **A** | +1.5% to 2.5% |
| **BBB** | +2.5% to 4.0% |
| **BB** | +4.0% to 6.0% |
| **B** | +6.0% to 10.0% |

**Example**:

```
Borrower: OpCo (Kazakhstan, BB rating)
Loan: $150M, 7-year term, USD
Base rate: SOFR (currently 5.25%, as of 2025)
Credit spread: 5.0% (BB rating, 7-year term)

Arm's length interest rate: 5.25% + 5.0% = 10.25%
Annual interest: $150M × 10.25% = $15.375 million
```

---

## 3. Thin Capitalization and Debt/Equity Characterization

### 3.1 Thin Capitalization Rules

**Purpose**: Limit **interest deductions** to prevent **excessive debt financing** and **profit shifting** (interest deductible in high-tax subsidiary, received as income in low-tax parent).

**Common rules**:

**A. Debt-to-Equity Safe Harbor**

Specified **maximum debt-to-equity ratio**; interest deductible if within safe harbor.

| **Jurisdiction** | **Safe Harbor Ratio** | **Excess Treatment** |
|---|---|---|
| **Germany** | 1.5:1 | Interest on excess debt non-deductible |
| **India** | 2:1 | Interest on excess debt non-deductible |
| **Indonesia** | 4:1 | Interest on excess debt non-deductible |
| **Brazil** | 2:1 (foreign affiliates) | Interest on excess debt non-deductible; recharacterized as deemed dividend (subject to WHT) |

**Example (India)**:

```
OpCo (India):
- Debt (from parent): $100M
- Equity: $40M
- Debt-to-equity ratio: 2.5:1

India safe harbor: 2:1

Excess debt: $100M - ($40M × 2) = $100M - $80M = $20M

Interest expense (8% rate):
- Total interest: $100M × 8% = $8M
- Deductible interest (on $80M): $80M × 8% = $6.4M
- Non-deductible interest (on $20M): $20M × 8% = $1.6M

India tax impact:
- Disallowed deduction: $1.6M
- Additional tax: $1.6M × 30% (India CIT) = $480,000
```

**B. Arm's Length Debt Test**

Some jurisdictions apply **arm's length test**: Would independent lender provide same debt level?

**Factors**:
- Borrower's creditworthiness (standalone, without parent support)
- Industry norms (oil & gas companies typically carry higher debt due to capital intensity)
- Purpose of loan (project financing vs. working capital)
- Collateral and covenants

### 3.2 Debt vs. Equity Characterization

**Issue**: If intercompany loan has **equity-like features**, tax authorities may **recharacterize** as equity; interest non-deductible.

**Equity-like features**:

| **Feature** | **Debt** | **Equity** | **Risk of Recharacterization** |
|---|---|---|---|
| **Fixed maturity** | Yes (5-10 years) | No (perpetual) | High if no maturity |
| **Fixed interest rate** | Yes (8% annually) | No (dividend subject to profits) | High if interest contingent on profits |
| **Security/collateral** | Often secured | Unsecured | High if unsecured and subordinated |
| **Subordination** | Senior or pari passu | Subordinated to all creditors | High if subordinated |
| **Convertibility** | Not convertible | N/A | High if convertible to equity |
| **Participation in profits** | No (fixed interest only) | Yes (dividends from profits) | High if interest varies with profits |

**Example of recharacterization**:

```
Intercompany loan terms:
- Amount: $200M
- Interest: 12% annually **if OpCo is profitable**; 0% if loss
- Maturity: **None** (perpetual loan)
- Security: **Unsecured, subordinated** to all external debt
- Convertible: At lender's option, **convertible to 40% equity** in OpCo

Tax authority analysis:
- **Equity-like features**: Contingent interest, perpetual, subordinated, convertible
- **Conclusion**: Loan is **equity in substance**; recharacterize as equity contribution

Result:
- $24M annual interest ($200M × 12%) **non-deductible**
- Additional tax: $24M × 30% = $7.2M
- Penalties for aggressive transfer pricing
```

**Best practice**: Ensure intercompany loans have **debt characteristics** (fixed maturity, fixed interest, senior or pari passu, non-convertible).

---

## 4. OECD BEPS Action 4: Interest Limitation Rules

### 4.1 Overview

**OECD BEPS Action 4** recommends limiting interest deductions to **10-30% of EBITDA** (earnings before interest, tax, depreciation, amortization).

**Purpose**: Prevent **base erosion** through excessive interest deductions.

**Adoption**: 40+ countries have implemented interest limitation rules (Germany, UK, France, Australia, India, Japan).

### 4.2 Common Rules

**A. Germany Interest Barrier Rule (Section 4h EStG)**

**Limit**: Interest deductions capped at **30% of tax EBITDA**

**Exceptions**:
- Net interest expense <€3M (de minimis)
- Standalone entity (not part of group)
- Group equity escape clause (entity's equity ratio ≥ group's equity ratio)

**Example**:

```
OpCo (Germany):
- EBITDA: €50M
- Interest expense (intercompany loan from parent): €20M

Interest limitation:
- Maximum deductible interest: €50M × 30% = €15M
- Actual interest: €20M
- Disallowed interest: €20M - €15M = €5M

Germany tax impact:
- Disallowed deduction: €5M
- Additional tax: €5M × 30% (Germany CIT + trade tax) = €1.5M

Carryforward: €5M disallowed interest can be carried forward indefinitely (deducted in future years if EBITDA sufficient)
```

**B. UK Corporate Interest Restriction (CIR)**

**Limit**: Interest deductions capped at **30% of tax EBITDA**

**Exceptions**:
- Group net interest expense <£2M (de minimis)
- Public benefit infrastructure exemption
- Group ratio method (entity can deduct interest up to group's net interest/EBITDA ratio)

**Example**:

```
OpCo (UK):
- EBITDA: £100M
- Interest expense: £40M (intercompany loan from Singapore parent)

Interest limitation (30% EBITDA):
- Maximum deductible: £100M × 30% = £30M
- Disallowed: £40M - £30M = £10M

UK tax impact:
- Additional tax: £10M × 25% = £2.5M
```

### 4.3 Group Ratio Method (Alternative)

**OECD Action 4**: Allows entity to deduct interest up to **group's external net interest/EBITDA ratio**.

**Rationale**: If group has high external debt (due to business model, not profit shifting), entities should be allowed same ratio.

**Example**:

```
Group consolidated:
- External interest expense: $100M (to independent banks)
- EBITDA: $500M
- Group ratio: $100M ÷ $500M = 20%

OpCo (UK):
- EBITDA: £100M
- Interest expense: £40M (intercompany)

Standard limitation (30% EBITDA): £30M deductible
Group ratio method (20% EBITDA): £100M × 20% = £20M deductible

Comparison:
- Standard: £30M deductible (£10M disallowed)
- Group ratio: £20M deductible (£20M disallowed)

Result: Standard method (30%) is more favorable; OpCo uses standard method
```

**When group ratio method helps**:

If group external debt ratio is **>30%**, group ratio method allows **higher deduction** than standard 30% limit.

---

## 5. Treasury Company Remuneration

### 5.1 Functions of Treasury Company

**Typical functions**:
1. **Centralized borrowing**: Raise external financing (bank loans, bonds); on-lend to operating affiliates
2. **Cash pooling**: Consolidate cash from operating affiliates; reduce external borrowing
3. **Foreign exchange management**: Hedge FX risk; provide FX forward contracts to affiliates
4. **Interest rate risk management**: Hedge interest rate risk through swaps
5. **Guarantee provision**: Provide guarantees for affiliates' bank loans (see Chapter 57)

### 5.2 Transfer Pricing Methods

**A. Interest Margin (Spread)**

Treasury company earns **interest spread** between:
- **Borrowing rate** (from external banks)
- **On-lending rate** (to operating affiliates)

**Typical spread**: **0.5-2.0%** depending on functions, risks, and capital employed.

**Example**:

```
Treasury Co. (Netherlands):
- Borrows $500M from banks at 6.0%
- On-lends to operating affiliates at 7.5%
- Interest spread: 1.5%

Annual revenue (interest margin):
- Interest received from affiliates: $500M × 7.5% = $37.5M
- Interest paid to banks: $500M × 6.0% = $30.0M
- Net interest income (spread): $37.5M - $30.0M = $7.5M

Treasury Co. costs:
- Treasury personnel (10 professionals): $2.0M
- IT systems (treasury management): $500K
- Overhead: $500K
Total costs: $3.0M

Treasury Co. profit: $7.5M - $3.0M = $4.5M
Operating margin: $4.5M ÷ $7.5M = 60% (high profit for limited-risk treasury function)
```

**Benchmarking**: Compare spread (1.5%) and operating margin (60%) to independent treasury service providers and captive finance companies.

**Typical arm's length ranges**:
- **Interest spread**: 0.5-2.0%
- **Operating margin**: 15-30%

**Analysis**: 1.5% spread is arm's length; but 60% operating margin is excessive (suggests Treasury Co. is overcapitalized or underperforms functions).

**B. Service Fee (Cost Plus)**

Alternative: Treasury company charges **service fees** (cost plus markup) instead of earning interest spread.

**Application**: When treasury provides **cash pooling**, **hedging**, and **advisory services** without on-lending.

**Example**:

```
Treasury Co. (Singapore) provides:
- Cash pooling administration
- FX hedging (forward contracts)
- Interest rate hedging (swaps)
- Treasury advisory

Annual costs: $5M (personnel, systems, overhead)
Markup: 10%
Service fee: $5M × 1.10 = $5.5M

Allocation to affiliates: Based on size of operations (assets, revenue, or headcount)
```

---

## 6. Documentation Requirements

### 6.1 Loan Agreement

**Key terms**:
- **Principal amount**: $100M
- **Interest rate**: 8.5% per annum (fixed or floating)
- **Maturity**: 7 years
- **Security**: Unsecured (or specify collateral)
- **Covenants**: Financial ratios (e.g., debt/EBITDA <3x, interest coverage >2x)
- **Events of default**: Non-payment, breach of covenants, insolvency
- **Governing law**: English law, New York law, etc.

### 6.2 Transfer Pricing Documentation

**Required components**:

1. **Credit rating analysis**: Borrower's standalone credit rating (financial ratios, country risk, industry analysis)
2. **Interest rate benchmarking**: Comparable bonds, bank loans, credit spreads for borrower's credit rating
3. **Comparables analysis** (if using CUT): External loans by borrower or comparable companies
4. **Thin capitalization analysis**: Demonstrate compliance with debt-to-equity safe harbors
5. **Arm's length debt capacity**: Analysis of maximum debt independent lender would provide

---

## 7. Worked Example

═══════════════════════════════════════════
**WORKED EXAMPLE: Intercompany Loan and Thin Capitalization**
═══════════════════════════════════════════

**Facts:**

NigeriaOil Ltd. (Nigeria subsidiary) requires $200M financing for offshore field development.

**Financing options**:

**Option 1: External bank loan**
- Lender: HSBC
- Amount: $200M
- Interest rate: 10.0% (reflecting Nigeria country risk, OpCo's BB credit rating)
- Term: 10 years
- **Requires parent guarantee** (reduces rate to 10.0%; without guarantee, rate would be 12.0%)

**Option 2: Intercompany loan from parent**
- Lender: GlobalPetro plc (UK parent, A credit rating)
- Amount: $200M
- Proposed interest rate: 7.0%
- Term: 10 years
- No guarantee (parent is lender)

**NigeriaOil financial data**:
- Equity: $100M
- Existing debt: $50M (external)
- New debt (proposed): $200M
- Total debt (post-financing): $250M
- Debt-to-equity ratio: 2.5:1

**Nigeria thin capitalization rule**: 2:1 safe harbor (excess debt interest non-deductible)

**Requirements**:

1. Determine arm's length interest rate for intercompany loan
2. Calculate thin capitalization impact
3. Compare Option 1 (external) vs. Option 2 (intercompany)
4. Recommend optimal structure

**Analysis:**

**Step 1: Arm's Length Interest Rate Determination**

**Method: Credit Rating Adjustment**

**NigeriaOil standalone credit rating**: BB (based on financial analysis)

**Market interest rates for BB credit (10-year, USD, 2025)**:
- BB-rated oil & gas bonds: 9.5-11.0%
- Median: 10.25%

**Adjustments**:
- **Country risk (Nigeria)**: +1.0% (political risk, currency risk, regulatory risk)
- **Unsecured**: +0.5% (no collateral)
- **Adjusted rate**: 10.25% + 1.0% + 0.5% = **11.75%**

**Comparison to external loan**:
- External bank (with parent guarantee): 10.0%
- External bank (without guarantee): 12.0%
- Arm's length rate (standalone): 11.75%

**Conclusion**: Arm's length rate for intercompany loan is **11.5-12.0%** (within range of standalone rate and external bank rate without guarantee).

**Proposed intercompany rate (7.0%)** is **significantly below** arm's length (11.5-12.0%).

**Tax authority risk**: Nigeria may challenge 7.0% as too low; adjust to 11.75%, disallowing $200M × (11.75% - 7.0%) = **$9.5M annually**.

**Step 2: Thin Capitalization Analysis**

**Nigeria safe harbor**: 2:1 debt-to-equity ratio

**NigeriaOil capital structure** (post-intercompany loan):
```
Equity: $100M
Total debt: $250M ($50M existing + $200M new)
Debt-to-equity ratio: 2.5:1
```

**Excess debt calculation**:
```
Safe harbor debt: $100M equity × 2 = $200M
Actual debt: $250M
Excess debt: $250M - $200M = $50M
```

**Interest deductibility** (assuming 11.75% arm's length rate):

```
Interest on allowable debt ($200M): $200M × 11.75% = $23.5M (deductible)
Interest on excess debt ($50M): $50M × 11.75% = $5.875M (non-deductible)

Nigeria tax impact:
- Disallowed deduction: $5.875M
- Additional tax: $5.875M × 30% = $1.7625M
```

**Step 3: Option Comparison**

**Option 1: External Bank Loan ($200M at 10.0% with parent guarantee)**

```
Annual interest: $200M × 10.0% = $20.0M
Guarantee fee (to parent): $200M × 1.5% = $3.0M (see Chapter 57)
Total annual cost: $20.0M + $3.0M = $23.0M

Thin capitalization:
- Total debt: $250M (2.5:1 ratio; excess $50M)
- Interest on allowable debt: $200M × 10.0% = $20.0M (deductible)
- Interest on excess debt: $50M × 10.0% = $5.0M (non-deductible)
- Guarantee fee on allowable debt: $200M × 1.5% = $3.0M (deductible)
- Guarantee fee on excess debt: $50M × 1.5% = $750K (non-deductible)

Tax calculation:
- Deductible: $20.0M (interest) + $3.0M (guarantee) = $23.0M
- Non-deductible: $5.0M (interest) + $750K (guarantee) = $5.75M
- Additional tax: $5.75M × 30% = $1.725M

After-tax cost:
- Cash cost: $23.0M
- Tax on non-deductible: $1.725M
- Less: Tax saving on deductible: $23.0M × 30% = $6.9M
- Net after-tax cost: $23.0M + $1.725M - $6.9M = $17.825M
```

**Option 2: Intercompany Loan ($200M at 11.75% arm's length rate)**

```
Annual interest (at arm's length 11.75%): $200M × 11.75% = $23.5M

Thin capitalization:
- Interest on allowable debt ($200M): $23.5M (deductible)
- Interest on excess debt ($50M): $5.875M (non-deductible)

Tax calculation:
- Deductible interest: $23.5M
- Additional tax (thin cap): $5.875M × 30% = $1.7625M

After-tax cost:
- Cash cost: $23.5M
- Tax on non-deductible: $1.7625M
- Less: Tax saving on deductible: $23.5M × 30% = $7.05M
- Net after-tax cost: $23.5M + $1.7625M - $7.05M = $18.2125M
```

**Comparison**:

| **Metric** | **Option 1 (External + Guarantee)** | **Option 2 (Intercompany)** | **Difference** |
|---|---|---|---|
| **Gross interest** | $20.0M | $23.5M | +$3.5M |
| **Guarantee fee** | $3.0M | $0 | -$3.0M |
| **Total cash cost** | $23.0M | $23.5M | +$0.5M |
| **Thin cap disallowance** | $5.75M | $5.875M | +$0.125M |
| **Additional tax** | $1.725M | $1.7625M | +$0.0375M |
| **Net after-tax cost** | **$17.825M** | **$18.2125M** | **+$0.3875M** |

**Conclusion**: **Option 1 (external bank loan with parent guarantee)** is **slightly more cost-effective** ($387,500 annual savings vs. intercompany loan).

**However**, intercompany loan has **non-tax advantages**:
- **Flexibility**: Parent can waive interest or extend maturity if cash flow issues arise
- **No external covenants**: Bank loan has restrictive covenants (debt/EBITDA, interest coverage); intercompany loan can be more flexible
- **Group cash management**: Interest paid to parent stays within group (can be redeployed); interest to bank leaves group

**Step 4: Optimal Structure Recommendation**

**Recommended**: **Hybrid structure**

```
Structure:
- External bank loan: $100M at 10.0% (with parent guarantee)
- Intercompany loan: $100M at 11.75%
- Total: $200M
- Equity: $100M
- Debt-to-equity ratio: 2.0:1 (within safe harbor!)

Benefits:
1. **Thin capitalization compliance**: 2.0:1 ratio (no disallowance)
2. **Lower average rate**: ($100M × 10.0% + $100M × 11.75%) ÷ $200M = 10.875%
3. **Flexibility**: Intercompany portion provides flexibility; external portion provides market discipline
4. **Tax efficiency**: Full deductibility (no thin cap disallowance)

Annual cost:
- External interest: $100M × 10.0% = $10.0M
- Intercompany interest: $100M × 11.75% = $11.75M
- Guarantee fee: $100M × 1.5% = $1.5M
- Total: $23.25M

Tax savings: $23.25M × 30% = $6.975M
Net after-tax cost: $23.25M - $6.975M = $16.275M

Savings vs. Option 1: $17.825M - $16.275M = $1.55M annually
```

**Documentation**:
1. **Loan agreements**: External bank facility agreement; intercompany loan agreement
2. **Parent guarantee**: Guarantee for external loan
3. **Transfer pricing analysis**: Credit rating analysis (BB), interest rate benchmarking (11.75%), thin capitalization analysis (2.0:1 ratio)
4. **Guarantee fee benchmarking**: Credit rating improvement method (see Chapter 57)

═══════════════════════════════════════════

---

## 8. Key Takeaways

1. **Arm's length interest rate** determined using **credit rating adjustment method** (borrower's standalone credit rating + market rate for that rating) or **CUT method** (comparable external loans).

2. **Typical credit spreads** (over LIBOR/SOFR): AAA (+0.5-1.0%), A (+1.5-2.5%), BBB (+2.5-4.0%), BB (+4.0-6.0%), B (+6.0-10.0%).

3. **Thin capitalization rules** limit interest deductions to prevent excessive debt: Common safe harbors are **2:1 to 4:1 debt-to-equity** ratios; excess debt interest non-deductible.

4. **Debt vs. equity characterization**: Intercompany loans with **equity-like features** (perpetual, contingent interest, subordinated, convertible) may be **recharacterized as equity**; interest non-deductible.

5. **OECD BEPS Action 4** (interest limitation): 40+ countries limit interest deductions to **10-30% of EBITDA**; prevents base erosion through excessive interest.

6. **Group ratio method**: Alternative to fixed EBITDA limit; allows entity to deduct interest up to **group's external net interest/EBITDA ratio** (helps if group has legitimately high external debt).

7. **Treasury company remuneration**: Treasury earns **interest spread** (0.5-2.0%) or **service fee** (cost plus 5-15% markup) depending on functions (centralized borrowing, cash pooling, hedging).

8. **Documentation requirements**: Loan agreements, credit rating analysis, interest rate benchmarking, comparables analysis, thin capitalization compliance analysis.

9. **Tax authority challenges**: Common issues include:
   - **Below-market interest rates** (parent charges subsidiary 5% when arm's length is 10%)
   - **Excessive debt levels** (thin capitalization violations)
   - **Debt disguised as equity** (hybrid instruments recharacterized)

10. **Best practices**:
    - **Benchmark interest rates** using credit rating methodology or external CUPs
    - **Monitor thin capitalization compliance** (maintain debt/equity within safe harbors)
    - **Structure loans with debt characteristics** (fixed maturity, fixed interest, senior, non-convertible)
    - **Consider hybrid structures** (part external, part intercompany) to optimize tax and flexibility
    - **Pursue APAs** for material financing arrangements (>$100M debt)

---

**This chapter has examined transfer pricing for group financing, including arm's length interest rate determination, thin capitalization rules, OECD BEPS Action 4 interest limitations, treasury company remuneration, and documentation requirements, enabling tax professionals to establish defensible arm's length pricing for intercompany loans and treasury operations in the oil and gas sector.**
