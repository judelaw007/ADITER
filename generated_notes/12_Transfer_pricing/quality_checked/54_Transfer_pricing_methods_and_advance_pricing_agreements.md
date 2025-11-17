# 54. Transfer Pricing Methods and Advance Pricing Agreements (APAs)

## 1. Introduction

**Transfer pricing** is the practice of determining prices for transactions between related entities within a multinational group. In the oil and gas sector, transfer pricing affects virtually every cross-border transaction: **crude oil sales**, **technical services**, **financing arrangements**, **intellectual property licensing**, **procurement contracts**, and **management services**.

The **arm's length principle**—requiring related party transactions to be priced as if the parties were independent—is the international standard codified in **Article 9 of the OECD Model Tax Convention on Income and on Capital** and adopted by over 140 countries. Tax authorities worldwide scrutinize transfer pricing to prevent **base erosion and profit shifting (BEPS)**, particularly in capital-intensive, high-margin industries like oil and gas.

This chapter examines the **five OECD-approved transfer pricing methods** (CUP, Cost Plus, Resale Price, TNMM, Profit Split), their application to oil and gas transactions, **Advance Pricing Agreements (APAs)** for obtaining certainty, **documentation requirements** (Master File, Local File, Country-by-Country Reporting), and **Amount B** simplification for baseline distribution activities.

---

## 2. The Arm's Length Principle

### 2.1 OECD Model Tax Convention Article 9

**Article 9(1)** of the **OECD Model Tax Convention on Income and on Capital** states:

> "Where... conditions are made or imposed between the two enterprises in their commercial or financial relations which differ from those which would be made between independent enterprises, then any profits which would, but for those conditions, have accrued to one of the enterprises, but, by reason of those conditions, have not so accrued, may be included in the profits of that enterprise and taxed accordingly."

**Interpretation**: If related parties transact on terms different from independent parties, tax authorities may adjust profits to reflect arm's length pricing.

### 2.2 OECD Transfer Pricing Guidelines (2022)

The **OECD Transfer Pricing Guidelines for Multinational Enterprises and Tax Administrations (2022)** provide detailed guidance on applying the arm's length principle. The 2022 edition, published in January 2022, is the current authoritative version used by tax administrations worldwide. **Key chapters**:

- **Chapter I**: The Arm's Length Principle
- **Chapter II**: Traditional Transaction Methods (CUP, Cost Plus, Resale Price)
- **Chapter III**: Transactional Profit Methods (TNMM, Profit Split)
- **Chapter VI**: Special Considerations for Intangibles
- **Chapter VII**: Special Considerations for Intra-Group Services
- **Chapter VIII**: Cost Contribution Arrangements
- **Chapter IX**: Transfer Pricing Aspects of Business Restructurings

### 2.3 Comparability Analysis

The arm's length principle requires **comparability analysis** examining five factors:

1. **Characteristics of property or services**: Quality, volume, reliability
2. **Functions performed**: Manufacturing, distribution, R&D, marketing
3. **Contractual terms**: Payment terms, warranties, risk allocation
4. **Economic circumstances**: Market conditions, geographic location
5. **Business strategies**: Market penetration, diversification, risk appetite

**Application to oil and gas**: Crude oil transactions must consider **API gravity**, **sulfur content**, **location**, and **contract terms** (term vs. spot, take-or-pay obligations).

---

## 3. Traditional Transaction Methods

### 3.1 Comparable Uncontrolled Price (CUP) Method

**A. Definition**

The **CUP method** compares the price charged in a controlled transaction to the price charged in a comparable uncontrolled transaction.

**Formula**:
```
Arm's Length Price = CUP (comparable uncontrolled price) ± Adjustments
```

**B. Application to Crude Oil**

The CUP method is the **most appropriate** method for commodity transactions (OECD Transfer Pricing Guidelines 2022, Chapter II, Section C).

**Purpose**: Crude oil is a relatively homogenous product with established public benchmarks, making direct price comparisons reliable. This method provides the most direct measure of whether related-party transactions reflect market prices that independent parties would agree to.

**Benchmarks**:
- **Brent Crude** (North Sea): Global benchmark for Atlantic Basin crude
- **West Texas Intermediate (WTI)**: U.S. benchmark
- **Dubai/Oman** (Fateh): Middle East benchmark
- **Henry Hub**: U.S. natural gas benchmark
- **JKM (Japan Korea Marker)**: Asian LNG benchmark

**Example**:

Producer Co. (Norway) sells crude to Trading Co. (Singapore, related party):

```
Benchmark: Brent Crude (published by Platts, ICE)
Date: Monthly average for delivery month
Quality adjustment: -$2/barrel (higher sulfur content vs. Brent)
Location adjustment: -$1/barrel (transportation differential)

Transfer Price = Brent Average - $2 - $1
If Brent = $80/barrel, Transfer Price = $77/barrel
```

**C. Internal vs. External CUP**

| **Type** | **Description** | **Reliability** |
|---|---|---|
| **Internal CUP** | Comparing controlled transaction to uncontrolled transaction by the same entity (e.g., Producer Co. sells to both related Trading Co. and unrelated traders) | **High** (same seller, similar product) |
| **External CUP** | Comparing controlled transaction to uncontrolled transaction between two independent parties (e.g., published benchmark prices) | **Moderate** (requires adjustments for differences) |

**D. Pricing Date**

Critical consideration: **When is the price determined?**

- **Date of lifting** (bill of lading date)
- **Date of delivery** (arrival at destination)
- **Monthly average** (average benchmark price for delivery month)
- **Fixed price** (negotiated price set at contract signing)

**Best practice**: Use consistent methodology across all controlled and comparable transactions.

### 3.2 Cost Plus Method

**A. Definition**

The **Cost Plus method** adds an appropriate markup to the costs incurred by the supplier in a controlled transaction.

**Purpose**: This method is appropriate when the tested party performs routine manufacturing or service functions where the value created is best measured by costs incurred plus a reasonable profit margin. It reflects the economic reality that service providers and manufacturers recover their costs plus a profit consistent with their risk profile and functions performed.

**Formula**:
```
Arm's Length Price = Direct Costs + Indirect Costs + Arm's Length Markup
```

**B. Application to Oilfield Services**

The Cost Plus method is appropriate for **services** and **manufacturing** activities where the tested party is a **cost center** providing services to related parties.

**Example**: Drilling services

DrillTech Ltd. (U.S., subsidiary) provides drilling services to Parent Oil Co. (UK):

```
Direct costs: Rig rental, crew wages, drilling fluids = $10 million
Indirect costs: Office overhead, equipment depreciation = $2 million
Total costs: $12 million

Comparable markup analysis:
- Independent drilling contractors earn 8-15% markup on costs
- Selected arm's length markup: 12% (midpoint)

Arm's length service fee: $12M × 1.12 = $13.44 million
```

**C. Comparability Factors**

When selecting comparable markups, consider:
- **Complexity of services**: Routine drilling vs. deepwater/HPHT drilling
- **Risks assumed**: Equipment ownership, performance guarantees
- **Intangibles employed**: Proprietary drilling technology
- **Geographic location**: Onshore vs. offshore, political risk

**D. Cost Base**

**Full cost vs. direct cost**:

| **Cost Base** | **Components** | **Application** |
|---|---|---|
| **Full cost** | Direct costs + allocated indirect costs (overhead) | Preferred by OECD; reflects total economic cost |
| **Direct cost** | Only costs directly attributable to transaction | Used when indirect cost allocation is arbitrary |

**Best practice**: Use **full cost** including reasonable allocation of indirect costs (e.g., management overhead, IT support, facilities).

### 3.3 Resale Price Method

**A. Definition**

The **Resale Price method** subtracts an appropriate gross margin from the price at which a product is resold to an independent party.

**Purpose**: This method is most reliable when a distributor purchases from a related party and resells without significant value addition. The gross margin represents compensation for the distributor's marketing, sales, and limited risk-bearing functions.

**Formula**:
```
Arm's Length Price = Resale Price - Gross Margin
```

**B. Application to Refined Products Trading**

The Resale Price method is appropriate when a **distributor** purchases from a related party and resells to independent customers without significant value addition.

**Example**: Refined products distribution

Refining Co. (Saudi Arabia, parent) sells diesel to Distribution Co. (UAE, subsidiary), which resells to independent customers:

```
Resale price (to independent customers): $100/barrel
Comparable gross margin analysis:
- Independent distributors earn 8-12% gross margin
- Selected arm's length margin: 10%

Arm's length purchase price: $100 - ($100 × 10%) = $90/barrel
```

**C. Functions Analysis**

The distributor's gross margin reflects:
- **Marketing and sales** functions
- **Inventory carrying costs** (working capital, storage)
- **Credit risk** (accounts receivable)
- **Limited product risk** (price volatility during distribution period)

If the distributor performs **additional functions** (blending, branding, extensive marketing), a higher gross margin is justified.

---

## 4. Transactional Profit Methods

### 4.1 Transactional Net Margin Method (TNMM)

**A. Definition**

The **TNMM** examines the net profit margin relative to an appropriate base (sales, costs, assets) that a taxpayer realizes from a controlled transaction.

**Purpose**: TNMM is used when traditional transaction methods are not reliable due to lack of comparable pricing data. Net profit margins are less sensitive to transactional differences than gross prices, making this method suitable for routine functions where comparable company data is available.

**Formula**:
```
Arm's Length Net Margin = Comparable Net Profit Indicator (NPI)

Common NPIs:
- Operating Margin (OM) = EBIT / Sales
- Return on Assets (ROA) = EBIT / Total Assets
- Return on Costs (ROC) = EBIT / Operating Costs
- Berry Ratio = Gross Profit / Operating Expenses
```

**B. Application to Support Services**

TNMM is appropriate for **routine services** and **distribution** activities where the tested party performs limited functions and assumes limited risks.

**Example**: Regional headquarters services

RegionalHQ Co. (Netherlands) provides management, HR, IT, and legal services to group operating companies:

```
Annual costs: €20 million
Selected NPI: Return on Costs (ROC) = EBIT / Operating Costs

Comparable companies analysis:
- Independent service providers earn ROC of 5-10%
- Selected arm's length ROC: 7.5% (median)

Arm's length EBIT: €20M × 7.5% = €1.5 million
Service fees charged to operating companies: €20M + €1.5M = €21.5 million
```

**C. Advantages and Limitations**

**Advantages**:
- Less sensitive to transactional differences than CUP
- Publicly available comparables (financial statements of independent companies)
- Tolerates minor functional differences

**Limitations**:
- Net margins affected by factors other than transfer pricing (efficiency, market power)
- Requires adjustments for differences in functions, risks, assets
- Less direct measurement of arm's length price than CUP or Cost Plus

### 4.2 Profit Split Method

**A. Definition**

The **Profit Split method** allocates the combined profits from controlled transactions between related parties based on their relative contributions.

**Purpose**: This method is appropriate when transactions are highly integrated and both parties make unique, valuable contributions that cannot be reliably evaluated separately. It reflects the economic principle that profit should be allocated based on value creation.

**Two approaches**:

1. **Contribution analysis**: Split profits based on relative value of functions, assets, and risks
2. **Residual analysis**: Allocate routine returns first, then split residual profit

**B. Application to Joint Ventures and Integrated Operations**

The Profit Split method is appropriate when:
- Transactions are **highly integrated** (difficult to evaluate separately)
- Both parties make **unique and valuable contributions**
- No reliable comparables available

**Example**: Joint development project

Oil Major A (technology, financing) and National Oil Company B (reserves, infrastructure) jointly develop offshore field:

```
Combined profit from field development: $500 million

Step 1: Allocate routine returns
- Oil Major A capital: $1 billion × 8% cost of capital = $80M
- NOC B infrastructure: $500M × 6% return = $30M
- Total routine returns: $110M

Step 2: Residual profit
- Residual profit: $500M - $110M = $390M

Step 3: Split residual based on relative contributions
- Oil Major A: Advanced drilling technology (40%), financing (30%) = 70%
- NOC B: Access to reserves (20%), local expertise (10%) = 30%

Final allocation:
- Oil Major A: $80M (routine) + ($390M × 70%) = $353 million
- NOC B: $30M (routine) + ($390M × 30%) = $147 million
```

**C. Comparability and Documentation**

Profit Split requires **robust documentation**:
- **Functional analysis**: Detailed description of each party's contributions
- **Intangibles valuation**: Technology, know-how, trade secrets
- **Risk analysis**: Who bears exploration risk, price risk, political risk?
- **Capital contributions**: Financing, infrastructure, equipment

**Challenges**: Subjectivity in determining relative contributions; requires agreement between tax authorities (often via **bilateral APA**).

---

## 5. Advance Pricing Agreements (APAs)

### 5.1 Definition and Purpose

An **Advance Pricing Agreement (APA)** is an agreement between a taxpayer and one or more tax authorities establishing the transfer pricing methodology for future transactions.

**Benefits**:
- **Certainty**: Pre-approval of methodology eliminates risk of adjustment
- **Efficiency**: Reduces compliance costs and audit risk
- **Dispute prevention**: Avoids costly and time-consuming controversies

### 5.2 Types of APAs

| **Type** | **Parties** | **Scope** | **Duration** |
|---|---|---|---|
| **Unilateral** | Taxpayer + one tax authority | Covers transactions in one jurisdiction only; risk of double taxation if other jurisdiction disagrees | 3-5 years |
| **Bilateral** | Taxpayer + two tax authorities | Covers transactions between two jurisdictions; eliminates double taxation via Mutual Agreement Procedure (MAP) | 3-5 years |
| **Multilateral** | Taxpayer + three or more tax authorities | Covers transactions across multiple jurisdictions (e.g., regional supply chain) | 3-5 years |

**Recommendation**: **Bilateral APAs preferred** for material cross-border transactions to ensure elimination of double taxation.

### 5.3 APA Process

**Step 1: Pre-filing meeting**
- Taxpayer meets with tax authority to discuss scope, timeline, and data requirements
- Typical duration: 1-3 months

**Step 2: Formal application**
- Submit detailed documentation:
  - Functional analysis
  - Proposed transfer pricing methodology
  - Financial data and projections
  - Benchmarking study (comparables analysis)
  - Proposed critical assumptions (e.g., pricing dates, volume ranges)

**Step 3: Review and negotiation**
- Tax authority reviews application, requests additional information
- For bilateral/multilateral APAs: Competent authorities negotiate under MAP
- Typical duration: 12-24 months

**Step 4: APA execution**
- Final agreement signed specifying:
  - Covered transactions and entities
  - Transfer pricing methodology (specific method, comparables, adjustments)
  - Critical assumptions (conditions under which APA remains valid)
  - Term (typically 3-5 years)
  - Annual reporting requirements

**Step 5: Annual compliance**
- Taxpayer submits annual report demonstrating compliance with APA terms
- If critical assumptions breached, APA may be revised or terminated

### 5.4 APA Statistics and Trends

**India** (leading APA program):
- **Total APAs signed (as of March 2025)**: 815 (615 unilateral, 199 bilateral, 1 multilateral)
- **FY 2024-25**: 174 new APAs signed (highest in any year), including 65 bilateral and India's first multilateral APA
- **Average processing time**: 35.76 months for unilateral APAs; 58.90 months for bilateral APAs
- **Record single-day achievement**: 34 APAs signed on March 27, 2025

**United States**:
- IRS Advance Pricing and Mutual Agreement (APMA) Program under Internal Revenue Code
- Average time: 24-36 months for bilateral APAs
- Most common industries: Pharmaceuticals, technology, manufacturing, **oil and gas**

**Singapore**:
- IRAS (Inland Revenue Authority of Singapore) offers bilateral APAs under tax treaties
- Application fee: SGD 25,000-50,000
- Strong uptake for regional headquarters and trading companies

### 5.5 APA Fees and Costs

| **Jurisdiction** | **Application Fee** | **Professional Advisor Costs** | **Total Estimated Cost** |
|---|---|---|---|
| **United States** | $121,600 (IRS user fee, 2025 for original APAs; $65,900 for renewals) | $200,000-500,000 | $320,000-620,000 |
| **Singapore** | SGD 25,000-50,000 | SGD 150,000-300,000 | SGD 175,000-350,000 |
| **UK (HMRC)** | £50,000-100,000 | £200,000-400,000 | £250,000-500,000 |
| **Switzerland** | CHF 50,000-100,000 | CHF 200,000-400,000 | CHF 250,000-500,000 |
| **Netherlands** | €25,000-75,000 | €150,000-300,000 | €175,000-375,000 |

**Cost-benefit analysis**: APAs are economically justified for **material transactions** (typically >$50 million annually) given certainty benefits and avoidance of double taxation risk.

---

## 6. Transfer Pricing Documentation Requirements

### 6.1 OECD BEPS Action 13: Three-Tiered Documentation

**A. Master File**

**Purpose**: High-level overview of MNE group's global operations and transfer pricing policies.

**Contents** (OECD Transfer Pricing Guidelines 2022, Annex I to Chapter V):

1. **Organizational structure**: Legal entity chart, ownership structure
2. **Business description**: Nature of business, supply chain, value drivers
3. **Intangibles**: Ownership, development, exploitation, payment flows
4. **Intercompany financial activities**: Financing arrangements, cash pooling
5. **Financial and tax positions**: Consolidated financial statements, list of APAs

**Filing threshold**: Varies by jurisdiction; typically required for MNEs with **consolidated revenue >€750 million**.

**B. Local File**

**Purpose**: Detailed transfer pricing analysis for transactions involving the local entity.

**Contents** (OECD Transfer Pricing Guidelines 2022, Annex II to Chapter V):

1. **Local entity description**: Management structure, business strategy, key competitors
2. **Controlled transactions**:
   - Description of material transactions (goods, services, intangibles, financing)
   - Volume and value of transactions
3. **Functional analysis**: Functions performed, assets employed, risks assumed (FAR analysis)
4. **Comparables analysis**:
   - Selection criteria for comparables
   - Financial data for selected comparables
   - Adjustments for differences
5. **Transfer pricing method**:
   - Selection of most appropriate method
   - Application to controlled transactions
   - Documentation of arm's length pricing

**Filing threshold**: Varies; typically required for entities with **intercompany transactions >€15 million** (India), **>£5 million** (UK), or similar thresholds.

**C. Country-by-Country Report (CbCR)**

**Purpose**: Provides tax authorities with high-level information on global allocation of income, taxes paid, and economic activity.

**Contents** (OECD Transfer Pricing Guidelines 2022, Annex III to Chapter V):

**Table 1**: Aggregate data by jurisdiction:
- Revenue (related party, unrelated party)
- Profit (loss) before income tax
- Income tax paid (on cash basis)
- Income tax accrued (current year)
- Stated capital
- Accumulated earnings
- Number of employees
- Tangible assets (other than cash)

**Table 2**: List of entities by jurisdiction

**Table 3**: Additional information (explanations for unusual data)

**Filing threshold**: **Consolidated group revenue ≥€750 million**.

**Filing deadline**: Within **12 months** of fiscal year-end.

**Example**:

For fiscal year ending December 31, 2024, CbCR must be filed by December 31, 2025.

### 6.2 Contemporaneous Documentation

**Critical principle**: Transfer pricing documentation must be prepared **contemporaneously** (i.e., **before or when** the transaction occurs, not after an audit notice).

**Rationale**: Demonstrates that taxpayer acted in good faith to comply with arm's length principle.

**Penalty relief**: Many jurisdictions provide **penalty relief** (or reduced penalties) if contemporaneous documentation is maintained, even if transfer pricing adjustment is made.

**Example penalties** (if documentation not maintained):

| **Jurisdiction** | **Penalty** |
|---|---|
| **United States** | 20% of underpayment (IRC Section 6662); 40% if gross valuation misstatement (net adjustment >$20M or >20% of gross receipts) |
| **UK** | 0-100% of additional tax: 0% with reasonable care; up to 30% for careless behavior; 70% for deliberate inaccuracies; 100% for deliberate and concealed |
| **India** | 100-300% of tax on under-reported income attributable to transfer pricing adjustment |
| **Nigeria** | N10,000,000 or 1% of transaction value (whichever higher) for failure to submit TP documentation within 21 days; N10,000 per day for continuing failure (Income Tax (Transfer Pricing) Regulations 2018) |

---

## 7. Amount B Simplification

### 7.1 OECD Pillar One - Amount B

**Amount B** (part of OECD **Pillar One**, distinct from Pillar Two Global Minimum Tax) provides a **simplified and streamlined approach** to transfer pricing for **baseline marketing and distribution activities**.

**Objective**: Reduce disputes and compliance burdens, particularly for **low-capacity countries**.

**Release date**: Consolidated report published February 2025 incorporating guidance released throughout 2024.

**Implementation**: Jurisdictions may adopt Amount B for fiscal years starting on or after **January 1, 2025** (optional, not mandatory).

### 7.2 Scope of Amount B

**In-scope activities**: **Baseline marketing and distribution** including:
- Wholesalers purchasing from related party and reselling to independent customers
- Sales agents earning commissions
- Commissionaires (selling in own name on behalf of principal)

**Out-of-scope activities**:
- Commodity marketing, trading, or distribution (specifically **excluded**)
- Manufacturing
- R&D
- Intangible development

**Implication for oil and gas**: **Commodity trading excluded** from Amount B simplification; traditional transfer pricing methods (primarily CUP) continue to apply.

### 7.3 Amount B Return on Sales

Amount B specifies a **fixed return on sales** for in-scope distributors based on:
- **Operating expenses** (OPEX) level
- **Geographic region** (different rates for different countries)
- **Industry** (general vs. specific)

**Pricing Automation Tool**: OECD provides a tool to calculate the Amount B return based on local financial statement inputs.

**Benefit**: Eliminates need for benchmarking study; provides certainty and reduces compliance costs.

### 7.4 Adoption Status

| **Jurisdiction** | **Status** | **Effective Date** |
|---|---|---|
| **United States** | Adopted (elective for taxpayers) | January 1, 2025 |
| **Ireland** | Adopted (mandatory for in-scope distributors) | January 1, 2025 |
| **India** | Under consideration | TBD |
| **New Zealand** | Opted out (confirmed) | N/A |

**Implication**: Multinational groups must assess on a **jurisdiction-by-jurisdiction basis** whether Amount B applies and whether it provides favorable or unfavorable results compared to traditional methods.

---

## 8. Worked Examples

═══════════════════════════════════════════
**WORKED EXAMPLE 1: Selecting Transfer Pricing Method for Crude Oil Sales**
═══════════════════════════════════════════

**Facts:**

PetroNord AS (Norway, producer) sells crude oil to PetroTrade Ltd. (Singapore, related trading company). The crude has the following characteristics:

- **Production**: 200,000 barrels/month
- **Quality**: API 35°, sulfur 0.8% (slightly higher sulfur than Brent)
- **Location**: Delivered to Rotterdam
- **Contract terms**: Monthly spot sales

PetroNord must establish arm's length transfer price for sales to PetroTrade.

**Available benchmarks**:
- **Brent Crude** (ICE): API 38°, sulfur 0.37%
- **Brent monthly average** (April 2025): $82.50/barrel
- **Platts published differentials**:
  - Sulfur adjustment: -$1.50/barrel for each 0.5% sulfur above 0.4%
  - API adjustment: -$0.50/barrel for each API degree below 38°

**Alternative approach**: PetroNord also sells **50,000 barrels/month** to **independent trader** (Vitol) under similar contract terms.

**Required:**

1. Determine the most appropriate transfer pricing method
2. Calculate arm's length transfer price using selected method
3. Compare CUP methods: External (benchmark-based) vs. Internal (actual uncontrolled transaction)

**Analysis:**

**Step 1: Method Selection**

For **commodity transactions**, the **CUP method** is the most appropriate (OECD Transfer Pricing Guidelines 2022, Chapter II, Section C).

**Rationale**:
- Published benchmark prices (Brent, WTI) provide reliable comparables
- Crude oil is a relatively homogenous product (adjustments for quality/location are well-established)
- CUP provides most direct measure of arm's length price

**Alternative methods rejected**:
- **Cost Plus**: Inappropriate (would require producer to document extraction costs; no relation to market value)
- **Resale Price**: N/A (tested party is producer, not reseller)
- **TNMM / Profit Split**: Less direct; used only when CUP not available

**Step 2: External CUP (Benchmark-Based)**

**Calculation**:

```
Base price: Brent monthly average (April 2025) = $82.50/barrel

Quality adjustments:
- Sulfur: PetroNord sulfur (0.8%) vs. Brent (0.37%) = +0.43% difference
  Adjustment: -(0.43% ÷ 0.5%) × $1.50 = -$1.29/barrel

- API: PetroNord API (35°) vs. Brent (38°) = -3° difference
  Adjustment: -3 × $0.50 = -$1.50/barrel

Total quality adjustment: -$1.29 - $1.50 = -$2.79/barrel

Location adjustment: Delivered Rotterdam (same as Brent) = $0

Transfer price (External CUP): $82.50 - $2.79 = $79.71/barrel
```

**Step 3: Internal CUP (Actual Uncontrolled Transaction)**

PetroNord sells 50,000 barrels/month to **Vitol (independent trader)** under same contract terms (monthly spot, Rotterdam delivery).

**Comparison**:

If PetroNord sells to Vitol at **$79.50/barrel** (April 2025), this is an **Internal CUP**.

**Advantages of Internal CUP**:
- **Same seller** (PetroNord)
- **Same crude quality** (API 35°, sulfur 0.8%)
- **Same location** (Rotterdam)
- **Same contract terms** (monthly spot)
- **Highly comparable**: Minimal adjustments required

**Arm's length transfer price using Internal CUP**: **$79.50/barrel**

**Step 4: Reconciliation and Selection**

| **Method** | **Transfer Price** | **Difference** | **Reliability** |
|---|---|---|---|
| **External CUP** (Brent benchmark) | $79.71/barrel | +$0.21 | High (published benchmark, documented adjustments) |
| **Internal CUP** (Vitol transaction) | $79.50/barrel | Reference | **Highest** (same seller, no adjustments) |

**Conclusion: Use Internal CUP ($79.50/barrel)**

**Rationale**:
- OECD Guidelines state that **Internal CUP is generally more reliable** than External CUP when available (Chapter II, para. 2.15)
- Eliminates need for quality/location adjustments (same crude, same terms)
- Direct evidence of arm's length price (actual transaction with independent party)

**Documentation requirements**:

1. **Contract with Vitol**: Copy of sales agreement specifying price, terms, delivery
2. **Invoice**: Evidence of actual $79.50/barrel price charged
3. **Volume comparison**: Demonstrate Vitol transaction is material (50,000 bbl/month represents 20% of PetroTrade volume; sufficient comparability)
4. **Contemporaneous analysis**: Document CUP analysis at time of establishing transfer price (not after audit)

**Transfer pricing policy (Local File)**:

> "PetroNord AS applies the Comparable Uncontrolled Price (CUP) method for crude oil sales to related party PetroTrade Ltd. The arm's length price is determined based on the price charged to Vitol (independent trader) for sales of identical crude under identical contract terms during the same period. No adjustments are required due to high comparability. Price: $79.50/barrel (April 2025)."

═══════════════════════════════════════════

---

═══════════════════════════════════════════
**WORKED EXAMPLE 2: Advance Pricing Agreement for Oilfield Services**
═══════════════════════════════════════════

**Facts:**

EngineerCo Ltd. (UK-based subsidiary of OilMajor plc) provides technical services to group operating companies in **Nigeria**, **Angola**, and **Brazil**:

- **Services**: Reservoir engineering, production optimization, drilling engineering
- **Annual cost base**: £50 million (including allocated overhead)
- **Historical markup**: 8% on costs
- **Annual service fees**: £54 million
- **Current transfer pricing method**: Cost Plus

**Issue**: Nigerian tax authority has challenged the 8% markup as too low, citing independent service providers earning 12-15% margins. EngineerCo faces potential adjustment of **£2-3.5 million** annually, plus penalties.

**Proposed solution**: Seek **bilateral APA** between **UK (HMRC)** and **Nigeria (FIRS)** to establish approved markup for 5-year term.

**Required:**

1. Assess whether bilateral APA is appropriate
2. Outline APA process and timeline
3. Conduct benchmarking analysis to support proposed markup
4. Estimate costs and benefits of pursuing APA

**Analysis:**

**Step 1: APA Appropriateness Assessment**

**Factors favoring APA**:
- **Material transaction**: £54 million annually (Nigerian portion ≈£25M based on allocation)
- **Existing controversy**: Nigerian tax authority already challenging current pricing
- **Recurring transaction**: Services will continue for foreseeable future (ongoing reservoir management)
- **Risk of double taxation**: If Nigeria adjusts EngineerCo income upward, UK may not provide correlative adjustment, resulting in double taxation
- **Certainty value**: APA provides 5-year certainty; eliminates annual audit risk

**Recommendation**: **Bilateral APA is highly appropriate.**

**Step 2: APA Process and Timeline**

**Phase 1: Pre-filing (Months 1-3)**

- EngineerCo meets with **HMRC** (UK competent authority) to discuss scope
- HMRC contacts **FIRS** (Nigeria) under **UK-Nigeria tax treaty Mutual Agreement Procedure (MAP)**
- Pre-filing meeting establishes:
  - Covered transactions (technical services from EngineerCo to Nigerian operating company)
  - Proposed methodology (Cost Plus)
  - Data requirements

**Phase 2: Formal Application (Month 4)**

Submit APA application to HMRC including:

1. **Functional analysis**:
   - **EngineerCo**: Employs 120 engineers (reservoir, production, drilling specialists); uses proprietary software; assumes limited risk (no performance guarantees)
   - **Nigerian OpCo**: Receives technical advice; implements recommendations; bears full operational and production risk

2. **Proposed transfer pricing methodology**:
   - **Method**: Cost Plus
   - **Cost base**: Full costs including direct costs (salaries, travel) + allocated overhead (IT, facilities, management)
   - **Proposed markup**: 10% on costs

3. **Benchmarking study**: (see Step 3 below)

4. **Financial projections**: Expected costs and revenues for APA term (Years 1-5)

5. **Critical assumptions**:
   - Cost base remains within ±20% of Year 1 baseline
   - Services remain substantially similar in nature and complexity
   - No fundamental change in functions, assets, or risks

**Phase 3: Review and Negotiation (Months 5-18)**

- HMRC reviews application; requests additional information (Months 5-8)
- HMRC and FIRS negotiate under MAP (Months 9-18):
  - **HMRC position**: 10% markup is arm's length based on EngineerCo's limited risk profile
  - **FIRS position**: 12-15% markup appropriate given specialized services
  - **Negotiated outcome**: **11% markup** (compromise; reflects median of comparables range)

**Phase 4: APA Execution (Month 19-20)**

- Final APA signed by EngineerCo, HMRC, and FIRS
- **Effective date**: January 1, 2025
- **Term**: 5 years (through December 31, 2029)
- **Rollback**: Parties agree to apply 11% markup retroactively to Year 2023-2024 (resolves existing controversy)

**Total timeline**: 20 months (pre-filing to execution)

**Step 3: Benchmarking Analysis**

**Objective**: Identify independent companies providing comparable engineering services to oil and gas operators.

**Search criteria**:
- **Industry**: Oilfield services (SIC/NAICS codes)
- **Services**: Engineering, technical consulting (exclude drilling contractors with equipment-intensive operations)
- **Geographic scope**: Global (but prefer companies operating in Nigeria or similar jurisdictions)
- **Financial data**: Publicly available (listed companies or databases like Orbis, TP Catalyst)

**Selected comparables**:

| **Company** | **Country** | **Services** | **EBIT/Sales** | **EBIT/Costs (Markup)** |
|---|---|---|---|---|
| TechEngCo A | Norway | Reservoir engineering | 9.5% | 10.5% |
| ServiceProvB | UK | Production optimization | 10.2% | 11.4% |
| ConsultCo C | Netherlands | Drilling engineering | 8.8% | 9.6% |
| OilfieldTechD | Canada | Technical consulting | 11.5% | 13.0% |
| **Median** | — | — | **9.9%** | **11.0%** |
| **Interquartile range** | — | — | **8.8-11.5%** | **9.6-13.0%** |

**Adjustments**: No material adjustments required; comparables perform similar functions, assume similar risks (no equipment ownership, no performance guarantees).

**Conclusion**: **11% markup on costs** is within arm's length range (median of comparables).

**Step 4: Cost-Benefit Analysis**

**Costs**:

| **Item** | **Amount (GBP)** |
|---|---|
| **HMRC application fee** | £75,000 |
| **FIRS application fee** (Nigeria) | £30,000 (NGN equivalent) |
| **Professional advisor fees** (Big 4 transfer pricing team) | £350,000 (benchmarking, application drafting, negotiation support) |
| **Internal costs** (EngineerCo management time, data gathering) | £50,000 (estimated) |
| **Total APA costs** | **£505,000** |

**Benefits (5-year term)**:

**Scenario 1: Without APA (Continued Dispute)**

Assume FIRS adjusts EngineerCo markup from 8% to 13% (midpoint of FIRS position):

```
Current service fee: £54M (8% markup on £50M costs)
FIRS-adjusted service fee: £50M × 1.13 = £56.5M
Annual adjustment: £2.5M
Nigeria corporate tax (30%): £2.5M × 30% = £750,000 additional tax annually

5-year total:
Additional tax: £750K × 5 = £3.75M
Penalties (50% of tax, assuming non-contemporaneous documentation): £1.875M
Professional fees (annual audit defense): £200K × 5 = £1.0M
Total 5-year cost: £6.625M
```

**Scenario 2: With Bilateral APA**

```
APA upfront cost: £505K
Agreed markup: 11%
Service fee: £50M × 1.11 = £55.5M
Annual increase vs. current: £1.5M
Nigeria tax impact: £1.5M × 30% = £450K annually
5-year total tax: £450K × 5 = £2.25M

Total 5-year cost: £505K (APA) + £2.25M (tax) = £2.755M
Annual compliance (APA reports): £50K × 5 = £250K
Grand total: £3.005M
```

**Net benefit of APA**:

```
5-year cost without APA: £6.625M
5-year cost with APA: £3.005M
Net benefit: £3.62 million over 5 years
Annual average benefit: £724,000
ROI: 717% (£3.62M benefit ÷ £505K APA cost)
```

**Conclusion**:

**Recommendation: Pursue bilateral APA.**

**Benefits**:
1. **Financial**: Saves £3.62M over 5 years (717% ROI)
2. **Certainty**: Eliminates audit risk and double taxation risk
3. **Operational**: Reduces management time spent on annual audits/disputes
4. **Reputational**: Demonstrates good faith compliance; strengthens relationships with tax authorities

**Implementation plan**:
- **Month 1-2**: Engage Big 4 advisor; prepare benchmarking study
- **Month 3**: Pre-filing meeting with HMRC
- **Month 4**: Submit formal APA application
- **Month 5-18**: HMRC-FIRS negotiation (EngineerCo provides data as requested)
- **Month 19-20**: APA execution; apply rollback to resolve 2023-2024 controversy
- **Years 1-5**: Annual APA compliance reports (£50K annually)

═══════════════════════════════════════════

---

## 9. Practical Application Guidance

**Method Selection Framework**:

1. **Start with CUP** for commodities and transactions with reliable market comparables
2. **Use Cost Plus** for routine service providers and manufacturers where cost data is reliable
3. **Apply Resale Price** for distributors that add limited value
4. **Apply TNMM** when traditional methods are unreliable but comparable company data exists
5. **Use Profit Split** only for highly integrated transactions with unique contributions from multiple parties

**Documentation Best Practices**:

1. Prepare transfer pricing documentation **contemporaneously** (before or when transaction occurs)
2. Update documentation annually to reflect changes in business operations or market conditions
3. Maintain Master File, Local File, and CbCR (if applicable) in accordance with OECD BEPS Action 13
4. Ensure consistency across all documentation levels
5. Retain supporting evidence (comparable data, benchmark prices, financial statements)

**APA Considerations**:

1. Pursue bilateral APAs for material cross-border transactions (>$50M annually)
2. Begin APA process early (18-24 month timeline)
3. Engage experienced transfer pricing advisors for benchmarking and negotiation support
4. Prepare robust functional analysis and financial projections
5. Monitor critical assumptions and report annually to maintain APA validity

---

**This chapter has examined the five OECD-approved transfer pricing methods, their application to oil and gas transactions, Advance Pricing Agreements for obtaining certainty, and documentation requirements under BEPS Action 13, equipping tax professionals to select appropriate methodologies, document arm's length pricing, and obtain advance rulings for intercompany transactions.**
