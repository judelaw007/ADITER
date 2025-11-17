# 60. Intellectual Property

## 1. Introduction

**Intellectual property (IP)** in the oil and gas sector encompasses **technical know-how**, **proprietary drilling technologies**, **seismic processing algorithms**, **reservoir simulation software**, **enhanced oil recovery (EOR) methods**, **carbon capture technologies**, **patents**, and **trade secrets**. Multinational groups often centralize IP ownership in dedicated **IP holding companies** located in **low-tax jurisdictions**, licensing the IP to operating affiliates for **royalty payments**.

From a transfer pricing perspective, IP transactions raise complex questions: What is the **arm's length royalty rate**? Which entity is entitled to **IP-related returns**? How should **development costs**, **enhancements**, and **maintenance** be allocated? The **Organisation for Economic Co-operation and Development (OECD) Transfer Pricing Guidelines for Multinational Enterprises and Tax Administrations** (2022 edition) address IP extensively in **Chapter VI** (Special Considerations for Intangibles) and the **DEMPE framework** (Development, Enhancement, Maintenance, Protection, Exploitation).

This chapter examines **types of IP in oil and gas**, **transfer pricing methods for IP** (Comparable Uncontrolled Transaction (CUT), profit split, Discounted Cash Flow (DCF) valuation), **royalty rate benchmarking**, **DEMPE analysis**, **cost contribution arrangements (CCAs)**, and **hard-to-value intangibles (HTVI)** guidance.

---

## 2. Types of IP in Oil and Gas

### 2.1 Technical Know-How and Trade Secrets

**Examples**:
- **Drilling techniques**: Directional drilling, horizontal drilling, managed pressure drilling
- **Reservoir management**: Water injection patterns, pressure maintenance strategies
- **Production optimization**: Artificial lift methods (gas lift, Electric Submersible Pump (ESP), rod pump selection)
- **EOR methods**: Carbon dioxide (CO2) injection, steam-assisted gravity drainage (SAGD), chemical flooding

**Characteristics**:
- **Not patented** (maintained as trade secrets to avoid disclosure)
- **Proprietary knowledge** developed through research and development (R&D) and operational experience
- **Competitive advantage**: Superior well productivity, lower operating costs

**Transfer pricing issue**: Should operating affiliates pay **royalties** to parent for use of proprietary know-how?

### 2.2 Patents

**Examples**:
- **Drilling equipment**: Drill bits, downhole tools, blowout preventers (BOPs)
- **Subsea systems**: Subsea trees, manifolds, control systems
- **Liquefied Natural Gas (LNG) technologies**: Liquefaction processes (Air Products, Shell Dual Mixed Refrigerant (DMR), ConocoPhillips Optimized Cascade)
- **Carbon capture**: CO2 capture solvents, compression systems

**Characteristics**:
- **Legally protected** (20-year patent term)
- **Publicly disclosed** (patent applications, granted patents)
- **Licensing potential**: Can be licensed to third parties for royalties

**Transfer pricing issue**: Arm's length royalty rates for **patented technologies**.

### 2.3 Software and Algorithms

**Examples**:
- **Seismic processing**: Depth imaging algorithms, noise reduction techniques
- **Reservoir simulation**: Finite difference models, streamline simulation, decline curve analysis
- **Production optimization**: Real-time optimization algorithms, predictive maintenance (machine learning)
- **Trading algorithms**: Price forecasting, arbitrage identification, risk management

**Characteristics**:
- **Software** (code, user interfaces, databases)
- **Algorithms** (mathematical models, machine learning models)
- **Continuous enhancement** (updates, new features, accuracy improvements)

**Transfer pricing issue**: Should affiliates pay **software license fees** or **royalties** for proprietary software?

### 2.4 Data and Databases

**Examples**:
- **Seismic data libraries**: 2D, 3D, 4D seismic surveys (terabytes of data)
- **Well databases**: Drilling data, completion data, production histories
- **Geological databases**: Core samples, formation tops, petrophysical properties
- **Market intelligence**: Commodity price databases, trading counterparty credit data

**Characteristics**:
- **Expensive to acquire**: Seismic surveys cost $10-100M depending on area/quality
- **Long-lived value**: Seismic data used for 10-20 years (reprocessing with new algorithms)
- **Proprietary**: Competitive advantage (e.g., exclusive seismic data for offshore block)

**Transfer pricing issue**: Should affiliates pay for **access to databases**?

---

## 3. Transfer Pricing Methods for IP

### 3.1 Comparable Uncontrolled Transaction (CUT) Method

**Definition**: Compare royalty rate in controlled transaction to royalty rate in comparable uncontrolled transaction.

**Application to IP licensing**:

**Formula**:
```
Arm's Length Royalty Rate = CUT (comparable uncontrolled royalty rate) ± Adjustments
```

**Example**:

```
IP Holding Co. (Ireland) licenses drilling technology to Operating Co. (Nigeria):

Internal comparable:
- IP Holding Co. licenses same technology to independent third party (Baker Hughes) for 5% royalty on revenue

Transfer pricing:
- Use Internal CUT: 5% royalty rate
- No adjustments required (same technology, same industry)

Operating Co. annual revenue: $500 million
Royalty payment: $500M × 5% = $25 million
```

**Challenges**:
- **Lack of comparables**: Most IP licensing in oil & gas is **intra-group** (limited third-party licensing)
- **Confidentiality**: Third-party royalty rates often **confidential** (not publicly disclosed)
- **Comparability**: IP is unique; finding "comparable" technology difficult

**Data sources**:
- **ktMINE**: Royalty rate database (covers various industries, including oil & gas technology)
- **RoyaltyRange**: IP valuation and royalty rate database
- **RoyaltyStat**: Transfer pricing comparables database

**Typical royalty rates** (oil & gas):

| **Technology Type** | **Typical Royalty Rate** |
|---|---|
| **Drilling technology** (routine) | 3-5% of revenue or 5-10% of cost savings |
| **Advanced drilling** (deepwater, High Pressure High Temperature (HPHT)) | 5-10% of revenue or 10-20% of cost savings |
| **Seismic processing software** | 2-5% of revenue from seismic services |
| **EOR technology** (incremental recovery) | 5-15% of incremental revenue or profit |
| **LNG liquefaction process** | 3-7% of liquefaction revenue |

### 3.2 Profit Split Method

**Application**: When IP is developed **jointly** by multiple entities, or when IP is **highly valuable** and no reliable CUTs exist.

**Example**:

```
Scenario: Parent (Norway) and Subsidiary (Brazil) jointly develop subsea production system:
- Parent: Contributed initial concept, design engineering (cost: $10M)
- Subsidiary: Field testing, adaptation to local conditions (cost: $5M)

Technology licensed to third party (Angola OpCo): Generates $30M annual profit

Profit split:
- Parent contribution: 67% (design, concept development)
- Subsidiary contribution: 33% (field testing, adaptation)

Allocated profit:
- Parent: $30M × 67% = $20.1M
- Subsidiary: $30M × 33% = $9.9M
```

**Documentation**: Functional analysis documenting each entity's contribution to IP development.

### 3.3 Discounted Cash Flow (DCF) Valuation

**Application**: Valuing IP for **transfer pricing purposes** (e.g., IP transfer from one entity to another) or determining **arm's length royalty rate** based on IP's economic value.

**Steps**:

1. **Project cash flows** attributable to IP (incremental revenue or cost savings from using IP)
2. **Discount to present value** using appropriate discount rate (Weighted Average Cost of Capital (WACC) or risk-adjusted rate)
3. **Calculate royalty rate** that allocates appropriate share of IP value to licensor

**Example**:

```
IP: Proprietary EOR technology increasing recovery by 10% (incremental 50 million barrels over 10 years)

Incremental cash flows:
- Year 1-10: 5M bbl/year × $80/bbl = $400M annually
- Operating costs: $200M annually
- Incremental cash flow: $200M annually

DCF valuation:
- Discount rate: 12% (reflecting technology risk, oil price risk)
- Present value (PV) factor (10 years, 12%): 5.650
- PV of incremental cash flows: $200M × 5.650 = $1.13 billion

Arm's length royalty:
- IP Holding Co. (owner) should receive fair compensation for $1.13B value created
- Typical allocation: 40-60% of value to IP owner (depending on other contributions)
- IP value allocated to owner: $1.13B × 50% = $565M

Royalty rate calculation:
- Annual royalty (annuity over 10 years): $565M ÷ 5.650 = $100M annually
- As % of incremental revenue: $100M ÷ $400M = 25% royalty rate
```

**Sensitivity analysis**: Test impact of varying oil prices, recovery factors, and discount rates.

---

## 4. DEMPE Analysis

### 4.1 OECD DEMPE Framework

**OECD Guidelines Chapter VI** (2017 revisions incorporated into 2022 edition) introduced the **DEMPE framework** to determine which entity(ies) are entitled to **IP-related returns**.

**DEMPE stands for**:
- **D**evelopment: R&D activities creating IP
- **E**nhancement: Improvements to IP (upgrades, new features)
- **M**aintenance: Ongoing support (bug fixes, user support)
- **P**rotection: Legal protection (patents, trademarks, trade secret controls)
- **E**xploitation: Commercial use of IP (licensing, embedding in products/services)

**Key principle**: Entity **performing and controlling** DEMPE functions (and **funding** DEMPE activities) is entitled to **IP-related returns**.

**Implication**: **Legal ownership alone is insufficient**; tax authorities will **attribute profits** to entities performing DEMPE functions.

### 4.2 Example: Seismic Processing Software

**Scenario**:

```
Structure:
- IP Holding Co. (Ireland): Owns seismic processing software (legal owner)
- R&D Co. (Norway): Employs 50 software engineers developing and enhancing software
- Operating Co. (Nigeria): Uses software for seismic processing services (revenue: $100M)

Royalty: Operating Co. pays IP Holding Co. $10M (10% of revenue)

Tax authority challenge (Norway):
- R&D Co. performs **Development and Enhancement** (employs all engineers, funds $20M annually)
- IP Holding Co. performs minimal functions (owns IP legally, but no personnel, no funding)
- Norway claims: IP-related returns should be attributed to R&D Co. (where DEMPE occurs), not IP Holding Co.
```

**DEMPE analysis**:

| **Function** | **IP Holding Co. (Ireland)** | **R&D Co. (Norway)** | **Operating Co. (Nigeria)** |
|---|---|---|---|
| **Development** | ✗ (no R&D personnel) | ✓ (50 engineers, $20M funding) | ✗ |
| **Enhancement** | ✗ | ✓ (ongoing software updates) | ✗ |
| **Maintenance** | ✗ | ✓ (bug fixes, user support) | ✗ |
| **Protection** | ✓ (owns legal rights, copyright registration) | ✗ | ✗ |
| **Exploitation** | ✓ (licenses to Operating Co.) | ✗ | ✓ (uses software commercially) |

**Conclusion**: **R&D Co. performs majority of DEMPE functions** (D, E, M); entitled to **IP-related returns**.

**Arm's length allocation**:

```
Operating Co. revenue: $100M
Operating Co. costs (excluding royalty): $70M
Gross profit: $30M

Allocation:
- R&D Co. (DEMPE): 60% of gross profit = $18M (compensation for D, E, M functions)
- IP Holding Co. (legal owner, exploitation): 25% = $7.5M (compensation for ownership, licensing)
- Operating Co. (routine processing): 15% = $4.5M (routine margin for service provider)

Revised royalties:
- Operating Co. → R&D Co.: $18M (cost-sharing or service fee for software development)
- Operating Co. → IP Holding Co.: $7.5M (royalty for IP license)
```

**Documentation**: Service agreements documenting R&D Co.'s development services and cost allocation.

---

## 5. Cost Contribution Arrangements (CCAs)

### 5.1 Definition

A **Cost Contribution Arrangement (CCA)** is an agreement among group members to **share costs and risks** of developing IP in exchange for **proportionate shares** of IP ownership and benefits.

**OECD Guidelines Chapter VIII** (Cost Contribution Arrangements): CCAs provide framework for **joint IP development** where participants contribute and receive benefits proportionate to contributions.

### 5.2 Structure

**Example**:

```
Participants:
- Parent (UK): Contributes $60M (60% of total R&D costs)
- Subsidiary A (U.S.): Contributes $30M (30%)
- Subsidiary B (Brazil): Contributes $10M (10%)

Total R&D costs: $100M

IP developed: Deepwater drilling technology

Benefits allocation:
- Parent: 60% of IP rights (can use in UK and licensed territories)
- Subsidiary A: 30% of IP rights (can use in U.S. and licensed territories)
- Subsidiary B: 10% of IP rights (can use in Brazil and licensed territories)

Expected benefits:
- Parent UK operations: $120M Net Present Value (NPV)
- Subsidiary A U.S. operations: $60M NPV
- Subsidiary B Brazil operations: $20M NPV
Total: $200M NPV

Contribution proportionality check:
- Parent: 60% contribution ($60M) vs. 60% expected benefits ($120M ÷ $200M) ✓
- Subsidiary A: 30% contribution vs. 30% benefits ✓
- Subsidiary B: 10% contribution vs. 10% benefits ✓
```

**Arm's length requirement**: Contributions must be **proportionate to expected benefits** (OECD Chapter VIII, para. 8.12).

### 5.3 Buy-In Payments

**Issue**: If a new participant **joins existing CCA** after IP has been partially developed, the new participant must make a **buy-in payment** to compensate existing participants for prior contributions.

**Example**:

```
Year 1-3: Parent (UK) develops drilling technology alone (cost: $50M; technology 60% complete)
Year 4: Subsidiary (Nigeria) joins CCA; contributes $25M for remaining 40% development

Buy-in payment calculation:
- Value of existing IP (60% complete): $80M (DCF valuation of expected benefits)
- Subsidiary's intended share: 30%
- Buy-in payment: $80M × 30% = $24M

Total Subsidiary contribution:
- Buy-in payment: $24M
- Future R&D costs (40% remaining): $25M × 30% = $7.5M
- Total: $31.5M

Parent receives: $24M buy-in payment (compensation for prior contributions)
```

**Buy-in valuation methods**: DCF, relief from royalty, market capitalization.

---

## 6. Hard-to-Value Intangibles (HTVI)

### 6.1 OECD BEPS Action 8 (HTVI Guidance)

**Hard-to-value intangibles (HTVI)** are IP where:
- **No reliable comparables** exist at time of transaction
- **Projections** of future cash flows are **highly uncertain**

**Examples in oil & gas**:
- **Unproven EOR technology**: No track record; uncertain recovery rates
- **Frontier exploration technology**: Deepwater drilling in unexplored basins; high technical and commercial risk

**OECD guidance** (Chapter VI, Section D.4): Tax authorities may use **ex post outcomes** (actual results 5-10 years later) to assess whether **ex ante pricing** (at time of transaction) was arm's length.

### 6.2 Application

**Example**:

```
Year 1 (2020):
- IP Holding Co. (Ireland) acquires subsea drilling technology from Parent (UK) for $50M
- Valuation based on projections: $500M NPV over 10 years

Year 6 (2024):
- Actual results: Technology generates $1.2B NPV (2.4× projected)

Tax authority challenge (UK His Majesty's Revenue and Customs (HMRC)):
- Claims $50M purchase price was too low (based on ex post outcomes)
- Applies ex post analysis: Technology worth $1.2B; arm's length purchase price should have been $120M
- Adjustment: $70M additional taxable income to Parent (2020)

Taxpayer defense:
1. **Ex ante analysis**: Demonstrate that $50M was reasonable based on information available in 2020
   - Projected NPV: $500M (mid-case scenario; sensitivity analysis showed $200M-800M range)
   - Purchase price: $50M = 10% of mid-case NPV (reasonable given risk)
   - Comparables: Other subsea technology transactions valued at 5-15% of projected NPV

2. **Uncertainty**: Document high degree of uncertainty:
   - Technology unproven (no field trials completed in 2020)
   - Commercialization risk (regulatory approvals, customer acceptance)
   - Market risk (oil prices, deepwater development activity)

3. **Pricing documentation**: Contemporaneous valuation report (2020) with DCF model, sensitivity analysis, risk assessment

Likely outcome: HMRC accepts $50M pricing if robust ex ante analysis and documentation exist; otherwise, may adjust based on ex post outcomes.
```

**Best practice**: Maintain **detailed contemporaneous documentation** of valuation assumptions, risk analysis, and scenario modeling for HTVI transactions.

---

## 7. Worked Examples

═══════════════════════════════════════════
**WORKED EXAMPLE 1: Royalty Rate Benchmarking for EOR Technology**
═══════════════════════════════════════════

**Facts:**

EnhanceOil Tech Inc. (U.S. parent) has developed proprietary **CO2-enhanced oil recovery (EOR)** technology:

**Technology benefits**:
- Increases recovery factor by 8-12 percentage points (vs. primary/secondary recovery)
- Applicable to mature fields with existing infrastructure

**Licensing structure**:
- TechCo (Netherlands IP holding subsidiary) owns technology (acquired from U.S. parent in 2018 for $100M)
- TechCo licenses technology to operating affiliates (Norway, UK, Brazil, Kazakhstan)

**2024 licensing to Kazakhstan OpCo**:

```
Field characteristics:
- Original oil in place (OOIP): 500 million barrels
- Primary/secondary recovery: 30% (150M barrels already produced)
- Remaining reserves: 350M barrels (70% of OOIP)

EOR technology impact:
- Incremental recovery: 10 percentage points × 500M = 50 million barrels
- Incremental production period: 10 years (5M bbl/year)

Economics:
- Oil price: $80/barrel
- Operating cost: $40/barrel (CO2 injection, monitoring, incremental lifting)
- Incremental cash flow: ($80 - $40) × 5M bbl = $200M annually

Kazakhstan OpCo royalty proposal: 5% of incremental revenue = $80M × 5M bbl × 5% = $20M annually
```

**Kazakhstan tax authority challenge**:
- Claims 5% royalty is excessive
- Proposes 2% royalty ($8M annually)

**Requirements**:

1. Benchmark arm's length royalty rate for EOR technology
2. Calculate NPV of royalty stream at different rates
3. Determine defensible royalty range
4. Assess impact of Kazakhstan adjustment

**Analysis:**

**Step 1: Comparable Uncontrolled Transaction (CUT) Search**

**Search criteria**:
- **Industry**: Oil & gas EOR technology
- **Transaction type**: Technology licensing (not equipment sales)
- **Royalty basis**: % of incremental revenue or % of incremental profit

**Data sources**: ktMINE royalty rate database, RoyaltyRange

**Identified comparables**:

| **Technology** | **Licensor** | **Royalty Rate** | **Basis** | **Year** |
|---|---|---|---|---|
| **Chemical EOR (polymer flooding)** | SNF Floerger | 8-12% | Incremental revenue | 2018 |
| **Thermal EOR (SAGD)** | Cenovus Energy | 6-10% | Incremental revenue | 2020 |
| **CO2 EOR** | Occidental Petroleum | 7-15% | Incremental revenue | 2019 |
| **Smart waterflooding** | BP | 3-7% | Incremental revenue | 2021 |

**Median royalty rate**: 7-10% of incremental revenue (for CO2 EOR specifically: 7-15%)

**Step 2: Profit-Based Royalty Calculation**

**Alternative approach**: Calculate royalty as **% of incremental profit** (instead of revenue).

```
Incremental revenue: $400M annually (5M bbl × $80)
Incremental costs: $200M annually (5M bbl × $40)
Incremental profit: $200M annually

Royalty as % of profit:
- Industry range: 20-40% of incremental profit for technology licensing
- Selected rate: 30%

Annual royalty: $200M × 30% = $60M
As % of incremental revenue: $60M ÷ $400M = 15%
```

**Step 3: DCF-Based Royalty Calculation**

**Step 3a: Value of technology to Kazakhstan OpCo**

```
Incremental cash flows (10 years):
- Year 1-10: $200M annually (incremental revenue $400M - costs $200M)

Discount rate: 12% (Kazakhstan country risk + oil price risk)
PV factor (10 years, 12%): 5.650

NPV to OpCo: $200M × 5.650 = $1.13 billion
```

**Step 3b: Allocation between OpCo and TechCo**

**Functional analysis**:
- **TechCo**: Owns technology, assumes R&D risk (spent $100M developing technology)
- **OpCo**: Applies technology, assumes operational risk (CO2 injection, production operations), country risk (Kazakhstan regulatory, political)

**Typical allocation**:
- **Technology owner (TechCo)**: 30-50% of value created (compensation for R&D investment, technology risk)
- **Technology user (OpCo)**: 50-70% of value created (compensation for operational risk, country risk, capital investment)

**Selected allocation**: **40% to TechCo**, **60% to OpCo**

```
Value to TechCo: $1.13B × 40% = $452M
Annual royalty (annuity over 10 years): $452M ÷ 5.650 = $80M annually

As % of incremental revenue: $80M ÷ $400M = 20%
As % of incremental profit: $80M ÷ $200M = 40%
```

**Step 4: Reconciliation of Methods**

| **Method** | **Annual Royalty** | **% of Incremental Revenue** | **% of Incremental Profit** |
|---|---|---|---|
| **CUT (comparables)** | $28-60M | 7-15% | 14-30% |
| **Profit-based** | $60M | 15% | 30% |
| **DCF-based** | $80M | 20% | 40% |

**Observation**: DCF-based royalty ($80M, 20%) is at **upper end** of comparable range (7-15%) but below **profit-based maximum** (40%).

**Step 5: Arm's Length Range Determination**

**Interquartile range (IQR)** from comparables: **7-12% of incremental revenue**

```
Lower quartile (7%): $400M × 7% = $28M annually
Upper quartile (12%): $400M × 12% = $48M annually
```

**Kazakhstan OpCo proposed royalty**: **5% of incremental revenue = $20M**

**Analysis**: 5% is **below arm's length range** (7-12% IQR).

**Recommended royalty**: **10% of incremental revenue = $40M annually** (median of comparable range)

**Step 6: Kazakhstan Tax Authority Adjustment Impact**

**Kazakhstan proposal**: Reduce royalty from 5% to 2% ($20M to $8M).

**Error**: Kazakhstan proposes to **reduce** royalty (benefiting OpCo), but comparables show 5% is already **too low**.

**Correct adjustment**: Kazakhstan should **increase** royalty from 5% to 10% (arm's length median).

```
Current royalty (5%): $20M
Arm's length royalty (10%): $40M
Adjustment: +$20M annual deduction disallowed

Kazakhstan tax impact:
- Additional taxable income: $20M
- Kazakhstan Corporate Income Tax (CIT) rate: 20%
- Additional tax: $20M × 20% = $4M annually
```

**Taxpayer response**:

1. **Accept 10% royalty**: Align with arm's length range; avoid controversy
2. **Negotiate 7-8% royalty**: Lower end of comparable range; conservative approach
3. **Defend 5% royalty**: Claim OpCo assumes **higher risk** (Kazakhstan country risk, operational complexity); justify 5% as arm's length based on risk allocation

**Likely outcome**: Kazakhstan tax authority **accepts 7-10% royalty** after reviewing comparables analysis.

**Recommendation**: **Revise royalty to 10%** ($40M annually) and document in **bilateral Advance Pricing Agreement (APA)** (Netherlands-Kazakhstan) for 10-year certainty.

═══════════════════════════════════════════

---

═══════════════════════════════════════════
**WORKED EXAMPLE 2: DEMPE Analysis for Seismic Processing Software**
═══════════════════════════════════════════

**Facts:**

Structure:
- **IP Holding Co. (Ireland)**: Owns seismic processing software (legal owner)
- **R&D Co. (Norway)**: Develops and enhances software (employs 50 software engineers)
- **OpCo (Angola)**: Uses software for seismic processing services (generates $100M annual revenue)

**Current transfer pricing structure**:

```
OpCo (Angola) → IP Holding Co. (Ireland): $10M annual royalty (10% of revenue)
IP Holding Co. (Ireland) → R&D Co. (Norway): $5M annual service fee (cost plus 10% for software development)
```

**R&D Co. financial data (2024)**:

```
Costs:
- Software engineer salaries: $8M (50 engineers @ $160K average)
- Software licenses (development tools): $500K
- IT infrastructure (servers, cloud): $1M
- Allocated overhead: $1M
Total costs: $10.5M

Revenue:
- Service fee from IP Holding Co.: $5M
- Shortfall: -$5.5M (loss)
```

**Norwegian tax authority audit** (2024):
- Claims R&D Co. performs majority of DEMPE functions but receives only $5M (cost plus 10%), while IP Holding Co. receives $10M royalty (with minimal functions)
- Proposes reattribution of $6M IP-related profit from IP Holding Co. to R&D Co.

**Requirements**:

1. Conduct DEMPE analysis
2. Determine arm's length allocation of IP-related returns
3. Calculate revised transfer prices
4. Assess impact of Norwegian adjustment

**Analysis:**

**Step 1: DEMPE Functional Analysis**

| **DEMPE Function** | **IP Holding Co. (Ireland)** | **R&D Co. (Norway)** | **OpCo (Angola)** |
|---|---|---|---|
| **Development** | ✗ (no R&D personnel, no funding) | ✓ **Performs** (50 engineers, $10.5M annual budget) | ✗ |
| **Enhancement** | ✗ | ✓ **Performs** (quarterly software updates, new features) | ✗ |
| **Maintenance** | ✗ | ✓ **Performs** (bug fixes, user support, documentation) | ✗ |
| **Protection** | ✓ **Owns** (copyright registration, trade secret controls) | ✗ | ✗ |
| **Exploitation** | ✓ **Licenses** to OpCo (licensing agreement, royalty collection) | ✗ | ✓ **Uses** commercially (seismic services) |
| **Funding** | ✗ (only pays $5M to R&D Co.; insufficient to cover $10.5M costs) | ✓ **Self-funds** (bears $5.5M annual loss) | ✗ |
| **Control** | ✗ (no oversight of R&D activities) | ✓ **Controls** (decides development priorities, feature roadmap) | ✗ |

**Conclusion**: **R&D Co. performs and controls D, E, M functions** and **funds** majority of costs; entitled to **IP-related returns** beyond routine cost-plus compensation.

**Step 2: Quantify IP-Related Returns**

**Total profit in IP value chain**:

```
OpCo revenue: $100M
OpCo costs (excluding royalty):
- Direct costs (seismic acquisition, data management): $60M
- Royalty to IP Holding Co.: $10M
Total costs: $70M

OpCo gross profit: $30M
```

**Allocation of $30M gross profit**:

**Entity 1: OpCo (Angola)**
- **Functions**: Seismic data acquisition, processing using software, customer management
- **Assets**: Seismic equipment, working capital
- **Risks**: Operational risk, customer credit risk, country risk (Angola)
- **Arm's length return**: **15% of costs** (comparable to contract seismic processors)

```
OpCo costs (excluding royalty): $60M
OpCo arm's length return: $60M × 15% = $9M
```

**Entity 2: IP Holding Co. (Ireland)**
- **Functions**: Legal ownership, licensing (administrative)
- **Assets**: Legal rights to software
- **Risks**: Minimal (no R&D risk, no operational risk)
- **Arm's length return**: **5-10% of royalty collected** (passive ownership return)

```
Selected return: 10% of IP-related profit (conservative)
IP Holding Co. return: ($30M - $9M OpCo) × 10% = $21M × 10% = $2.1M
```

**Entity 3: R&D Co. (Norway)**
- **Functions**: Development, Enhancement, Maintenance (DEMPE)
- **Assets**: Software engineers, development tools, IP know-how
- **Risks**: R&D risk (technology may not work), obsolescence risk (competitors develop better software)
- **Arm's length return**: **Residual profit** (after allocating routine returns to OpCo and IP Holding Co.)

```
Residual profit: $30M - $9M (OpCo) - $2.1M (IP Holding Co.) = $18.9M
```

**Step 3: Revised Transfer Prices**

**Current structure**:
```
OpCo → IP Holding Co.: $10M royalty
IP Holding Co. → R&D Co.: $5M service fee
R&D Co. profit: $5M - $10.5M costs = -$5.5M (loss) ✗ Not arm's length
```

**Revised structure (post-DEMPE analysis)**:

**Option 1: Direct royalty from OpCo to R&D Co.**

```
OpCo → R&D Co.: $18.9M annual payment (software development and licensing)
OpCo → IP Holding Co.: $2.1M annual royalty (legal ownership, administrative licensing)

R&D Co. profit: $18.9M - $10.5M costs = $8.4M ✓ Reflects DEMPE contribution
IP Holding Co. profit: $2.1M ✓ Reflects passive ownership
OpCo profit: $30M - $18.9M - $2.1M = $9M ✓ Reflects routine processing
```

**Option 2: Cost-sharing arrangement (CCA)**

```
R&D Co. and IP Holding Co. enter CCA:
- R&D Co. contributes: $10.5M (development costs)
- IP Holding Co. contributes: $10.5M (funding)
- Benefit allocation: 50/50 (both share IP ownership and returns)

IP-related profit: $30M - $9M (OpCo) = $21M
R&D Co. share (50%): $10.5M
IP Holding Co. share (50%): $10.5M

OpCo pays:
- R&D Co.: $10.5M (50% royalty)
- IP Holding Co.: $10.5M (50% royalty)
```

**Step 4: Norwegian Tax Authority Adjustment**

**Norwegian proposal**: Reallocate $6M from IP Holding Co. to R&D Co.

**Calculation**:

```
Current R&D Co. profit: -$5.5M (loss)
Arm's length R&D Co. profit: $18.9M (Option 1) or $10.5M (Option 2, with CCA funding)

If using Option 1 (direct allocation):
Adjustment: $18.9M - (-$5.5M) = $24.4M additional taxable income to R&D Co.
Norway tax impact: $24.4M × 22% (Norway CIT) = $5.37M additional tax
```

**Corresponding adjustment in Ireland**:
- IP Holding Co. profit reduced: $10M (current) - $2.1M (arm's length) = $7.9M reduction
- Ireland tax saved: $7.9M × 12.5% (Ireland standard CIT rate) = $988K
- Net group tax cost: $5.37M (Norway) - $988K (Ireland) = **$4.38M**

**Step 5: Resolution**

**Mutual Agreement Procedure (MAP)**:
- R&D Co. (Norway) files MAP request with Norwegian competent authority
- Norway contacts Ireland under **Norway-Ireland tax treaty**
- Competent authorities negotiate: Agree on revised allocation (likely **Option 2: CCA** with 50/50 split)
- Both countries adjust consistently; **double taxation avoided**

**Proactive solution**: **Bilateral APA** between Norway and Ireland for 5-year term:
- Pre-approve **CCA** or **direct DEMPE compensation** structure
- Cost: $200K-400K (application, advisors)
- Benefit: Avoids $4.38M tax cost + penalties; provides certainty

═══════════════════════════════════════════

---