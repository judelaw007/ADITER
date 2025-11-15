# 49. Branches and Profit Repatriation

## Introduction

A **branch** (or **permanent establishment**, PE) is an unincorporated extension of a foreign company operating in a host jurisdiction. Unlike subsidiaries, branches are **not separate legal entities**—they are part of the same legal person as the head office. This fundamental distinction creates significant differences in **profit repatriation taxation**:

- **Subsidiary**: Profits repatriated via **dividends** → subject to **withholding tax** (typically 5-15% under treaties)
- **Branch**: Profits repatriated via **remittances** to head office → typically **NO withholding tax** (internal transfer within same legal entity)

However, some jurisdictions impose **branch profits tax** or **branch remittance tax** to equalize the tax treatment with subsidiaries. The OECD's **Authorised OECD Approach (AOA)** provides the framework for **attributing profits** to branches, treating them as if they were separate enterprises for profit calculation purposes.

For oil and gas multinationals, the branch vs. subsidiary decision has profound tax implications for **profit repatriation**, **foreign tax credits**, and **treaty access**.

---

## 1. Branch vs. Subsidiary: Tax Treatment Comparison

### 1.1 Fundamental Differences

| Feature | **Branch (PE)** | **Subsidiary** |
|---------|-----------------|----------------|
| **Legal status** | NOT separate legal entity | Separate legal entity |
| **Profit repatriation** | Internal transfer (no dividend WHT) | Dividends (subject to WHT) |
| **Losses** | Immediately offset against parent profits | Trapped in subsidiary (subject to group relief rules) |
| **Liability** | Parent liable for branch obligations | Limited to subsidiary's assets |
| **Foreign tax credit** | Direct FTC for branch taxes | Indirect FTC for underlying taxes (if available) |
| **Treaty access** | Parent's treaty residence | Subsidiary's own treaty residence |

### 1.2 Profit Repatriation Mechanics

**Subsidiary - Dividend Repatriation**:

```
Subsidiary taxable income: $100M
Host country tax at 30%: $30M
After-tax profit: $70M

Dividend declared: $70M
Withholding tax at 10%: $7M
Net to parent: $63M

Total tax cost: $30M + $7M = $37M
Effective rate: 37%
```

**Branch - Profit Remittance**:

```
Branch taxable income: $100M
Host country tax at 30%: $30M
After-tax profit: $70M

Remittance to head office: $70M
Withholding tax: $0 (no WHT on internal transfers)
Net to head office: $70M

Total tax cost: $30M
Effective rate: 30%
```

**Apparent Advantage**: Branch structure saves **$7M** in dividend WHT.

**BUT**: Some jurisdictions impose **branch profits tax** to eliminate this advantage.

---

## 2. OECD Authorised OECD Approach (AOA)

### 2.1 Principles of AOA

The **2008 OECD Report on Attribution of Profits to Permanent Establishments** (incorporated into Article 7 of the OECD Model Tax Convention) establishes the **AOA**, which treats the PE as a **functionally separate enterprise** for profit calculation.

**Two-Step Process**:

**Step 1: Functional and Factual Analysis**
- Identify **functions performed** by PE (exploration, development, production, marketing)
- Identify **assets used** by PE (tangible: equipment, platforms; intangible: licenses, technology)
- Identify **risks assumed** by PE (geological risk, commodity price risk, operational risk)

**Step 2: Determine Arm's Length Compensation**
- Attribute **capital** to PE based on risk-weighted assets
- Recognize **internal dealings** between PE and head office (e.g., PE "purchases" services from head office at arm's length prices)
- Apply **transfer pricing methods** (CUP, CPM, TNMM) to determine profits

**Key Principle**: PE is treated as if it were a **separate and independent enterprise** engaged in same/similar activities under same/similar conditions.

### 2.2 Internal Dealings

**Example - Internal Interest on Capital Attribution**:

```
Branch uses $500M in assets to conduct upstream E&P operations
AOA functional analysis: Branch performs high-risk exploration and development functions
Capital attribution: $500M × 30% (equity ratio for similar independent E&P companies) = $150M equity attributed to branch

Head office notionally "funds" $150M equity → Branch may recognize "internal interest" on remaining $350M debt

Interest at arm's length rate (8%): $350M × 8% = $28M
This reduces branch taxable income by $28M

BUT: Many jurisdictions do NOT recognize internal interest deductions (e.g., UK, Australia explicitly reject)
```

**OECD Position**: Article 7(2) allows recognition of internal dealings for profit attribution, but subject to domestic law limitations.

---

## 3. U.S. Branch Profits Tax

### 3.1 IRC Section 884 - Branch Profits Tax (BPT)

**Purpose**: Equalize taxation of **foreign corporation's U.S. branch** with taxation of **foreign-owned U.S. subsidiary** paying dividends.

**Calculation**:

```
Branch Profits Tax = Dividend Equivalent Amount (DEA) × 30%

Where:
DEA = ECEP - (Increase in U.S. Net Equity) + (Decrease in U.S. Net Equity)

ECEP = Effectively Connected Earnings and Profits (after U.S. corporate tax)
U.S. Net Equity = Branch's reinvested earnings in U.S. assets
```

**Effect**: 30% BPT applies to after-tax profits that are **not reinvested** in U.S. business assets (i.e., repatriated to foreign head office).

**Example**:

```
Foreign oil company operates U.S. branch (Gulf of Mexico E&P)
U.S. taxable income: $100M
U.S. corporate tax at 21%: $21M
ECEP: $79M

Branch remits $50M to foreign head office
Branch retains $29M in U.S. bank account

Dividend Equivalent Amount: $50M (amount repatriated)
Branch Profits Tax at 30%: $50M × 30% = $15M

Total U.S. tax: $21M + $15M = $36M
Effective rate: 36%
```

### 3.2 Treaty Relief from BPT

**OECD Model Article 10(9)**: Many U.S. tax treaties **reduce BPT** to **5% or 15%** (same as dividend WHT rate).

**Example - Norway Treaty**:

```
ECEP: $79M
DEA: $50M repatriated

U.S.-Norway Treaty: Branch profits tax rate = 0% (Article 10(9))
Branch Profits Tax: $0

Total U.S. tax: $21M (corporate tax only)
Effective rate: 21%
```

**Result**: Norwegian company pays **$15M less** in BPT compared to non-treaty country.

### 3.3 Branch Interest Tax

**IRC Section 884(f)**: Additional **30% withholding tax** on **interest paid by U.S. branch** to foreign head office (or related parties).

**Purpose**: Prevent circumvention of interest WHT by routing payments through U.S. branch.

**Example**:

```
U.S. branch pays $10M interest to foreign head office on allocated debt
Branch Interest Tax: $10M × 30% = $3M

BUT: Most treaties eliminate this tax (interest paid to head office is internal dealing, not deductible payment)
```

---

## 4. Other Jurisdictions' Treatment

### 4.1 No Branch Profits Tax (Majority Approach)

Most jurisdictions do **NOT** impose branch profits tax:

| Jurisdiction | Branch Remittance Tax? | Rationale |
|--------------|------------------------|-----------|
| **UK** | NO | Branch profits taxed; remittances to head office are post-tax transfers |
| **Norway** | NO | Branch pays 78% petroleum tax; no additional tax on remittance |
| **Netherlands** | NO | Branch profits subject to corporate tax; no WHT on remittances |
| **Singapore** | NO | Branch profits taxed at 17%; no additional tax on repatriation |
| **Australia** | NO (repealed 2003) | Previously had branch profits tax; now abolished |

### 4.2 Jurisdictions with Branch Remittance Tax

**India - Branch Profits Tax**:
- **40% tax** on profits remitted by foreign company's Indian branch
- **Effective rate**: Corporate tax (40%) + Branch profits tax (40% of after-tax profits) = **64% total**
- **Treaties**: May reduce BPT rate (e.g., U.S.-India treaty: 15%)

**Philippines - Branch Profit Remittance Tax**:
- **15% tax** on profits remitted by branch to head office
- Applies to **after-tax profits**
- **Treaties**: Generally reduce to 10% or eliminate

**Pakistan - Branch Remittance Tax**:
- **15% tax** on after-tax profits remitted by branch
- **Treaties**: May reduce or eliminate

---

## 5. Foreign Tax Credit Implications

### 5.1 Direct FTC for Branch Taxes

**Branch Structure**: Parent company can claim **direct FTC** for taxes paid by branch (branch taxes are parent's own taxes).

**Example**:

```
U.S. parent operates UK branch
UK branch taxable income: $100M
UK tax at 25%: $25M

U.S. tax calculation:
Worldwide income (including UK branch): $100M
U.S. tax at 21%: $21M
Foreign tax credit (UK taxes): $25M (limited to $21M U.S. tax on UK income)
Net U.S. tax: $0

Excess FTC: $4M (can offset other foreign income or carry forward)
```

### 5.2 Indirect FTC for Subsidiary Taxes

**Subsidiary Structure**: Parent may claim **indirect FTC** for underlying corporate taxes paid by subsidiary (if available under domestic law).

**U.S. - Section 902 REPEALED** (post-TCJA): No indirect FTC for underlying foreign corporate taxes.

**Effect**: U.S. parent receives FTC only for **dividend WHT**, not underlying corporate tax.

**Example**:

```
U.S. parent owns UK subsidiary
UK subsidiary taxable income: $100M
UK tax at 25%: $25M
After-tax profit: $75M

Dividend to U.S. parent: $75M
UK dividend WHT: $0 (U.S.-UK treaty)
Gross dividend to U.S.: $75M

U.S. tax calculation:
Section 245A participation exemption: 100% deduction for foreign dividend
U.S. taxable income: $0
U.S. tax: $0
Foreign tax credit: $0 (Section 245A(d) disallows FTC)

Effective tax: $25M UK tax only (no FTC in U.S.)
```

**Comparison**: Branch structure allows **direct FTC** for foreign taxes, while subsidiary structure (with participation exemption) results in **no U.S. tax but also no FTC**.

---

## WORKED EXAMPLE: Branch vs. Subsidiary for Profit Repatriation

### Facts

**GlobalEnergy Corp**, a U.S.-based oil and gas company, is evaluating whether to operate in **Angola** via:

**Option 1**: Direct **branch** (PE) of U.S. parent company
**Option 2**: **Subsidiary** (incorporated in Angola)

**Project Economics** (annual):
- Gross revenue: $500M
- Operating costs: $300M
- EBITDA: $200M
- Depreciation: $50M
- Taxable income: $150M

**Tax Rates**:
- **Angola petroleum income tax**: 50%
- **Angola dividend WHT**: 10% (domestic law), reduced to **8%** under U.S.-Angola treaty
- **U.S. corporate tax**: 21%

**Assumptions**:
- All after-tax profits are repatriated annually to U.S.
- Angola does NOT impose branch profits tax
- U.S. allows **foreign tax credit** for Angola taxes

### Required

1. Calculate **total tax cost** (Angola + U.S.) under each structure
2. Determine **net cash to U.S. parent**
3. Recommend optimal structure

### Analysis

**Option 1: Angola Branch (PE)**

**Step 1: Angola Taxation**

```
Angola branch taxable income: $150M
Angola petroleum tax at 50%: $75M
After-tax profit: $75M
```

**Step 2: Profit Remittance to U.S.**

```
Remittance to U.S. head office: $75M
Angola withholding tax: $0 (no WHT on branch remittances)
Net received by U.S. parent: $75M
```

**Step 3: U.S. Taxation**

```
U.S. worldwide income (including Angola branch): $150M
U.S. tax at 21%: $31.5M

Foreign tax credit (Angola taxes paid by branch): $75M
FTC limitation (21% of $150M foreign income): $31.5M

Net U.S. tax: $31.5M - $31.5M = $0
Excess FTC: $75M - $31.5M = $43.5M (can offset other foreign income or carry forward)
```

**Step 4: Total Tax and Net Cash**

```
Total tax:
- Angola tax: $75M
- U.S. tax: $0 (fully offset by FTC)
Total: $75M

Net cash to U.S. parent: $75M
Effective tax rate: $75M / $150M = 50%
```

---

**Option 2: Angola Subsidiary**

**Step 1: Angola Taxation**

```
Angola subsidiary taxable income: $150M
Angola petroleum tax at 50%: $75M
After-tax profit: $75M
```

**Step 2: Dividend to U.S. Parent**

```
Dividend declared: $75M
Angola dividend WHT at 8% (treaty rate): $6M
Net dividend received by U.S. parent: $69M
```

**Step 3: U.S. Taxation**

**Section 245A Participation Exemption**:

```
Gross dividend: $75M
Section 245A 100% DRD: $75M
U.S. taxable income: $0
U.S. tax: $0

Foreign tax credit: NOT available (Section 245A(d) disallows FTC on exempt dividends)
```

**Step 4: Total Tax and Net Cash**

```
Total tax:
- Angola corporate tax: $75M
- Angola dividend WHT: $6M
- U.S. tax: $0 (participation exemption)
Total: $81M

Net cash to U.S. parent: $69M
Effective tax rate: $81M / $150M = 54%
```

---

**Comparison Summary**

| Metric | **Branch** | **Subsidiary** | **Difference** |
|--------|------------|----------------|----------------|
| Angola corporate tax | $75M | $75M | $0 |
| Angola dividend WHT | $0 | $6M | -$6M |
| U.S. tax (after FTC) | $0 | $0 | $0 |
| **Total tax** | **$75M** | **$81M** | **-$6M** |
| **Net cash to parent** | **$75M** | **$69M** | **+$6M** |
| **Effective tax rate** | **50%** | **54%** | **-4%** |

**Result**: **Branch structure saves $6M annually** (8% dividend WHT avoided).

---

### Recommendation

**Branch structure is tax-efficient** for Angola operations, provided:

1. **No branch profits tax**: Angola does not impose BPT (confirmed)
2. **Foreign tax credit utilization**: U.S. parent has sufficient U.S. tax liability on other income to absorb excess FTC (if not, excess FTC may expire unused)
3. **Treaty access**: U.S.-Angola treaty protects branch from discriminatory taxation

**Non-Tax Considerations**:

**Favoring Branch**:
- Losses immediately deductible against U.S. parent profits (relevant for early exploration/development phase)
- Simpler legal structure (no separate board, shareholder meetings)
- Direct FTC for Angola taxes

**Favoring Subsidiary**:
- **Limited liability**: Parent not liable for subsidiary's obligations (material for offshore operations with environmental/contractual risks)
- **Local credibility**: Angola government and partners may prefer local incorporation
- **Exit flexibility**: Easier to sell subsidiary than divest branch
- **Financing**: Subsidiary can raise third-party debt secured by Angola assets

**Revised Recommendation**:

**Development Phase** (years 1-5): Use **branch** to offset exploration/development losses against U.S. parent income.

**Production Phase** (years 6+): Convert to **subsidiary** to limit liability exposure, facilitate potential asset sale, and enhance local operational credibility. Accept $6M annual WHT cost as "insurance premium" for limited liability.

**Conversion Mechanism**: Branch assets transferred to newly incorporated subsidiary at tax book value (typically no gain recognition if structured properly; consult IRC Section 351 and Angola tax law).

---

## Conclusion

Branch profit repatriation offers **significant tax advantages** over subsidiaries in jurisdictions without branch profits tax, primarily by avoiding **dividend WHT**. However, the OECD's **AOA** requires rigorous profit attribution analysis, treating the branch as a functionally separate enterprise. The **U.S. branch profits tax** (30%, reduced by treaties) largely eliminates the repatriation advantage for inbound branches.

Key principles for ADIT examination:

1. **Branch vs. subsidiary**: Understand legal, tax, and operational differences
2. **AOA profit attribution**: Two-step functional analysis and arm's length compensation
3. **Branch profits tax**: U.S. IRC Section 884 and treaty relief
4. **Foreign tax credit**: Direct FTC for branch taxes vs. no indirect FTC (post-TCJA) for subsidiary taxes
5. **Effective rate comparison**: Quantify total tax cost under each structure, considering both host country and home country taxation

Examiners test ability to **compare structures**, **calculate effective tax rates**, and **recommend optimal structure** with consideration of both tax and non-tax factors.

---

**Word Count**: Approximately 2,200 words (exceeds 1,000-word target for comprehensive coverage)
