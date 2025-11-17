# Chapter 72: Design and Implementation of Emissions Trading Schemes (ETS)

## 1. Introduction

**Emissions Trading Schemes (ETS)**, also known as cap-and-trade systems, represent a market-based approach to reducing greenhouse gas emissions. Unlike carbon taxes which set a price and allow the market to determine the quantity of emissions, an ETS sets a quantity cap on total emissions and allows the market to determine the price through trading of allowances. This chapter examines the design elements, implementation challenges, and tax implications of ETS systems, with specific focus on applications in the oil and gas sector.

## 2. Fundamental Concepts

### 2.1 Definition and Core Mechanism

An **Emissions Trading Scheme** is a regulatory framework that:
1. Establishes a cap (maximum limit) on total emissions from covered sources
2. Issues or auctions emission allowances equal to the cap
3. Requires regulated entities to surrender allowances matching their emissions
4. Permits trading of allowances between participants
5. Imposes penalties for non-compliance

**Key Principle**: Entities facing high abatement costs can purchase allowances from those able to reduce emissions more cheaply, ensuring reductions occur where most economically efficient.

### 2.2 Economic Rationale

**Cost-Effectiveness**: ETS minimizes total abatement cost across economy by:
- Equalizing marginal abatement costs across all emitters
- Allowing flexibility in how and where reductions occur
- Creating continuous incentive for innovation

**Environmental Certainty**: Unlike carbon taxes, ETS guarantees specific emission outcomes through the cap.

**Table 1: Carbon Tax vs. ETS Comparison**

| Feature | Carbon Tax | Emissions Trading Scheme |
|---------|-----------|-------------------------|
| **Price certainty** | Yes (set by government) | No (market-determined) |
| **Quantity certainty** | No (depends on behavior) | Yes (cap guarantees outcome) |
| **Cost-effectiveness** | High (if price set correctly) | Very high (market finds cheapest abatement) |
| **Revenue predictability** | High | Variable (depends on auction design) |
| **Political visibility** | High (explicit tax) | Lower (permits perceived differently) |
| **Volatility** | Low | Can be high (price fluctuations) |
| **International linkage** | Difficult | Relatively easier |

## 3. Key Design Elements

### 3.1 Scope and Coverage

**Coverage Decisions**:

**Sectors**:
- Power generation (most common—large point sources)
- Industry (cement, steel, chemicals, refining)
- Aviation (EU ETS includes intra-European flights)
- Buildings (EU ETS2, starting 2027)
- Road transport (EU ETS2, starting 2027)

**Greenhouse Gases**:
- CO2 only (simplest)
- All six Kyoto Protocol gases converted to CO2-equivalent (comprehensive)

**Threshold**:
- Installation size (e.g., EU: 20 MW thermal capacity)
- Absolute emissions (e.g., California: 25,000 tonnes CO2/year)

**Table 2: Major ETS Coverage Comparison**

| ETS | Launch Year | Coverage (% national emissions) | Sectors Covered |
|-----|-------------|---------------------------------|-----------------|
| **EU ETS** | 2005 | 45% | Power, industry, aviation |
| **China ETS** | 2021 | 40% | Power (initially, expanding to include steel, cement, aluminum) |
| **California** | 2013 | 85% | Power, industry, transport, buildings |
| **UK ETS** | 2021 | 33% | Power, industry, aviation |
| **New Zealand** | 2008 | 50% | All sectors (some agriculture exempt) |
| **South Korea** | 2015 | 70% | Power, industry, buildings, transport, waste |

### 3.2 Cap Setting

The cap is the most critical design element, determining environmental stringency:

**Cap Setting Approaches**:

1. **Absolute Cap**: Fixed number of allowances (e.g., 100 million tonnes/year)
   - Advantage: Clear environmental outcome
   - Disadvantage: Doesn't adjust to economic growth/decline

2. **Intensity-Based Cap**: Allowances per unit output (e.g., tonnes CO2/MWh)
   - Advantage: Accommodates economic fluctuations
   - Disadvantage: Total emissions uncertain

3. **Declining Cap**: Reduces over time to meet long-term targets
   - EU ETS: **Linear Reduction Factor (LRF)** of 4.3%/year (2024-2027) and 4.4%/year (2028-2030) under revised Phase 4
   - Previous LRF: 2.2%/year (2021-2023) - significantly strengthened in 2023 revision
   - Advantage: Provides long-term certainty and accelerates decarbonization trajectory

**EU ETS Cap Evolution**:
- Phase 1 (2005-2007): 2.2 billion allowances/year
- Phase 2 (2008-2012): 2.1 billion/year
- Phase 3 (2013-2020): 1.9 billion declining to 1.5 billion
- Phase 4 (2021-2030): 1.5 billion declining to 0.8 billion
- **Result**: 62% reduction vs. 2005 by 2030

### 3.3 Allowance Allocation

**Free Allocation vs. Auctioning**:

**Free Allocation** (grandfathering or benchmarking):
- **Grandfathering**: Based on historical emissions
  - Advantage: Reduces opposition from incumbents
  - Disadvantage: Rewards past polluters; doesn't incentivize early action

- **Benchmarking**: Based on product output and efficiency benchmark
  - Example: "Best available technology" standard
  - Advantage: Rewards efficient producers
  - Disadvantage: Complex to design; data-intensive

**Auctioning**:
- Allowances sold to highest bidders
- Advantages:
  - Generates government revenue
  - Efficient price discovery
  - Avoids windfall profits to existing emitters
  - Polluter pays principle
- Disadvantages:
  - Increases costs for emitters
  - May face political resistance

**EU ETS Allocation Evolution**:
- Phase 1 (2005-2007): 95% free allocation
- Phase 2 (2008-2012): 90% free allocation
- Phase 3 (2013-2020): 50% average (power sector 100% auction)
- Phase 4 (2021-2030): 57% auctioned; free allocation for trade-exposed industries based on benchmarks

### 3.4 Price Stability Mechanisms

Price volatility can undermine investment certainty and political support. Mechanisms to stabilize prices include:

**Price Floor** (Auction Reserve Price):
- Minimum auction reserve price below which allowances will not be sold
- Example: UK ETS has £22/tonne **Auction Reserve Price** (ARP) in 2024
- Prevents price collapse during low demand periods, providing investment certainty

**Price Ceiling**:
- Maximum allowance price or commitment to issue additional allowances
- Rare in practice (undermines cap)

**Market Stability Reserve (MSR)** (EU ETS):
- Adjusts auction supply based on allowance surplus
- If surplus > 833 million: withhold 24% of auction volume
- If surplus < 400 million: release 100 million allowances
- Reduces volatility without explicit price floor/ceiling

**Allowance Banking**:
- Permits saving current allowances for future use
- Smooths price fluctuations across time
- All major ETS allow unlimited banking

**Borrowing**:
- Use future allowances for current compliance
- Rare (California allows limited borrowing)

### 3.5 Compliance and Enforcement

**Compliance Cycle**:
1. **Registration**: Operators register installations
2. **Monitoring**: Continuous emissions measurement (CEMS) or calculation
3. **Reporting**: Annual verified emission report
4. **Verification**: Independent third-party audit
5. **Surrender**: Submit allowances equal to verified emissions (by deadline)
6. **Penalty**: Non-compliance triggers fines + surrender obligation remains

**Penalties**:
- EU ETS: €100/tonne excess emissions + must still surrender allowances next year
- California: 4 allowances for every 1 tonne shortfall
- Ensures compliance is cheaper than non-compliance

## 4. Implementation Strategies

### 4.1 Phased Approach

**Phase 1: Learning Phase** (EU model)
- Short period (2-3 years)
- Generous cap to build confidence
- Free allocation to minimize opposition
- Identify administrative challenges

**Phase 2: Transition Phase**
- Tighter cap approaching targets
- Introduce auctioning gradually
- Align with international commitment periods (Kyoto Protocol)

**Phase 3: Maturity Phase**
- Stringent cap aligned with long-term goals
- Predominantly auctioned allowances
- Robust price stabilization mechanisms
- Potential for international linking

### 4.2 MRV Systems

**Monitoring**:
- **Tier 4** (highest accuracy): Continuous Emissions Monitoring Systems (CEMS)
  - Required for large power plants
  - Real-time CO2 concentration and flow measurement

- **Tier 3**: Mass balance with sampling
  - Fuel input × emission factor - carbon captured
  - Requires periodic calibration

- **Tier 1/2** (lowest): Standard emission factors
  - Activity data × IPCC default factors
  - Only for small emitters

**Reporting**:
- Annual emission report
- Standardized templates (EU: Electronic template)
- Submission deadline (typically March 31 following compliance year)

**Verification**:
- Independent accredited verifiers
- Risk-based materiality thresholds (e.g., ±5%)
- Site visits and data audits
- Verification opinion: Reasonable assurance

### 4.3 Registry Systems

**Functions**:
- Account management (operator accounts, trading accounts)
- Allowance issuance and tracking
- Transaction recording
- Compliance surrender processing
- Public transparency (aggregate data)

**Security**:
- Two-factor authentication
- Transaction limits and delays
- Government oversight of transfers

**EU Registry**: Union Registry consolidates all Member State accounts post-2012

### 4.4 Offset Mechanisms

**Clean Development Mechanism (CDM)** / **Joint Implementation (JI)**:
- **Kyoto Protocol** flexibility mechanisms allowing developed countries to achieve emission reduction targets through projects in other countries
- **CDM**: Projects in developing countries generate **Certified Emission Reductions (CERs)** - provides technology transfer and sustainable development
- **JI**: Projects in other Annex B (industrialized) countries generate **Emission Reduction Units (ERUs)**
- Can be used for ETS compliance (subject to qualitative and quantitative limits)

**Limits and Quality Concerns**:
- EU ETS Phase 3: Max 50% of reductions via offsets; restricted after 2012
- Concerns: Additionality (would project happen anyway?); permanence; leakage
- Shift toward **domestic offsets** in some jurisdictions (California)

## 5. ETS and the Oil and Gas Sector

### 5.1 Refining and Petrochemicals

**Coverage**:
- Refineries: All combustion units >20 MW thermal (EU)
- Petrochemical plants: Steam crackers, aromatics production
- Among largest industrial emitters (refineries: 5-10 million tonnes CO2/year)

**Allocation Methodology** (EU benchmarking):
- **Fuel benchmark**: 32.5 kg CO2/GJ fuel input (2021-2025)
- **Process emissions**: Product-specific benchmarks
  - Hydrogen: 9.07 kg CO2/tonne H2
  - Aromatics: 0.029 kg CO2/kg product

**Free Allocation Calculation**:
Free allowances = Benchmark × Production × Carbon Leakage Exposure Factor (CLEF) × Cross-Sectoral Correction Factor (CSCF)

**Example**:
- Refinery processing 10 million tonnes crude/year
- Fuel input: 60 PJ/year
- Benchmark allocation: 32.5 kg CO2/GJ × 60,000,000 GJ = 1,950,000 allowances
- CLEF: 100% (refining is carbon leakage exposed)
- CSCF: 1.0 (no scarcity in Phase 4, currently)
- **Total free allocation**: 1,950,000 allowances/year

**Actual emissions**: 2,500,000 tonnes CO2/year (higher than benchmark)
**Shortfall**: 550,000 allowances must be purchased

### 5.2 Upstream Oil and Gas

**Coverage Varies by ETS**:
- **EU/UK ETS**: Offshore installations generally excluded (no combustion units >20 MW typically)
- **Norway**: Dedicated offshore CO2 tax (not ETS)
- **California**: Upstream oil/gas covered if emissions >25,000 tonnes CO2/year
- **Alberta TIER**: Oil sands facilities covered

**Emission Sources**:
- Power generation (gas turbines)
- Flaring and venting
- Fugitive emissions (methane → CO2-eq)

**Intensity-Based Systems** (common for oil/gas):
- Alberta TIER:
  - Facility-specific emission intensity limit
  - Baseline = 0.80 × benchmark intensity
  - Emit below baseline: earn credits
  - Emit above baseline: purchase credits or pay C$50/tonne

### 5.3 Carbon Leakage Risk

Oil and gas sectors face significant carbon leakage risk:

**Factors**:
- **Trade intensity**: Refined products traded globally
- **Inability to pass costs**: Marginal pricing in competitive markets
- **Easy relocation**: Investment can shift to non-ETS regions

**Mitigation Measures**:
1. **Free allocation**: 100% of benchmark for carbon leakage list sectors
2. **Border Carbon Adjustments**: CBAM (EU) for imports
3. **Export rebates**: Return ETS cost for exported products
4. **Intensity-based allocation**: Rewards efficiency, accommodates production changes

**Carbon Leakage List** (EU):
- Refined petroleum products: YES (NACE 19.2)
- Petrochemicals: YES (selected NACE 20.xx codes)
- Extraction: Generally NO (not in ETS)

## 6. International Tax Considerations

### 6.1 Characterization of ETS Costs and Revenues

**Allowance Purchase**:
- **Asset acquisition** or **tax payment**?
- Tax treatment:
  - **Asset view**: Allowances are intangible assets; capitalized and expensed upon surrender
  - **Tax view**: Allowances are pre-paid environmental tax; deductible when purchased
- Most jurisdictions: **Expense when surrendered** (matches obligation recognition)

**Free Allocation**:
- **Taxable income** when received?
- **UK**: Free allowances have nil value; no taxable income
- **Some jurisdictions**: May be taxable subsidy or grant
- Creates book-tax difference for financial reporting

**Offset Sales** (if entity over-allocated):
- **Taxable income** when allowances sold
- Ordinary income vs. capital gain treatment varies by jurisdiction

### 6.2 Transfer Pricing

**Intragroup Allowance Transfers**:

Multinational oil and gas companies may centralize allowance purchasing:

**Example**:
- Parent establishes central ETS desk
- Purchases allowances in market
- Allocates to refinery subsidiaries based on projected needs

**Arm's Length Pricing**:
- Should subsidiaries pay market price or cost?
- **OECD View**: Market price at time of transfer (allowances are commodities)
- **Markup**: Central desk may charge service fee (1-3% of allowance value)

**Comparability Analysis**:
- Comparable uncontrolled price (CUP) method most appropriate
- Market price readily available (exchange-traded)
- Adjustments for:
  - Transaction costs
  - Timing (forward vs. spot)
  - Volume (bulk discounts)

### 6.3 Permanent Establishment Risks

**Carbon Trading Activities**:

If oil and gas company establishes separate trading entity for ETS allowances:
- **Risk**: Creates PE in trading location
- **Analysis**:
  - Fixed place of business? (Yes, if dedicated office)
  - Preparatory/auxiliary? (No, if core profit-making activity)
- **Conclusion**: Likely creates PE if substantive trading

**Planning Consideration**:
- Ensure trading entity has substance in favorable tax jurisdiction
- Or house in existing subsidiary's jurisdiction to avoid new PE

### 6.4 Withholding Tax on Allowance Transactions

**Cross-Border Allowance Sales**:

Jurisdiction A entity sells allowances to Jurisdiction B entity:

**Withholding tax analysis**:
- **Royalty?**: No (not use of intangible property)
- **Dividend?**: No (not distribution of profits)
- **Business profits?**: Yes (Article 7 of OECD Model)
- **Conclusion**: Taxable in Jurisdiction A (seller residence); no withholding in Jurisdiction B unless PE

**Exception**: Some countries impose transaction taxes (stamp duty) on commodity trades

## 7. Worked Examples

### WORKED EXAMPLE 1: EU ETS Compliance and Benchmarking Allocation

**Facts**:

EuroRefinery SA operates an integrated oil refinery in Belgium, processing crude oil into gasoline, diesel, jet fuel, and petrochemicals. The facility is covered by the EU ETS Phase 4 (2021-2030).

**Operational Data (2024)**:
- Crude oil throughput: 12 million tonnes/year
- Total fuel input (combustion): 75 PJ/year (petajoules)
- Hydrogen production: 200,000 tonnes/year
- Ethylene (aromatics) production: 150,000 tonnes/year

**Emissions (2024)**:
- Combustion emissions: 2,800,000 tonnes CO2
- Process emissions (hydrogen): 1,800,000 tonnes CO2
- Process emissions (aromatics): 6,000 tonnes CO2
- **Total verified emissions**: 4,606,000 tonnes CO2

**EU ETS Benchmarks (Phase 4, 2021-2025)**:
- Fuel combustion: 32.5 kg CO2/GJ
- Hydrogen production: 9.07 tonnes CO2/tonne H2
- Aromatics: 0.029 tonnes CO2/kg product

**Allocation Parameters**:
- Carbon Leakage Exposure Factor (CLEF): 100% (refining on CL list)
- Cross-Sectoral Correction Factor (CSCF): 1.0 (sufficient allowances Phase 4)

**Market Data (2024)**:
- Average EUA (EU Allowance) price: €85/tonne
- December 2024 spot price: €92/tonne

**Financial**:
- Revenue: €15 billion
- Operating costs (pre-ETS): €14 billion
- Belgian corporate tax: 25%

**Required**:

1. Calculate total free allocation under EU ETS benchmarking
2. Determine allowance shortfall or surplus
3. Calculate ETS compliance cost
4. Analyze after-tax impact on profitability
5. Evaluate emission reduction investment economics

**Analysis**:

**Step 1: Calculate Free Allocation by Benchmark**

**Fuel Combustion Benchmark**:
- Fuel input: 75 PJ = 75,000,000 GJ
- Benchmark: 32.5 kg CO2/GJ = 0.0325 tonnes CO2/GJ
- Allocation: 75,000,000 × 0.0325 = **2,437,500 allowances**

**Hydrogen Process Benchmark**:
- Production: 200,000 tonnes H2
- Benchmark: 9.07 tonnes CO2/tonne H2
- Allocation: 200,000 × 9.07 = **1,814,000 allowances**

**Aromatics Process Benchmark**:
- Production: 150,000 tonnes = 150,000,000 kg
- Benchmark: 0.029 tonnes CO2/kg = 0.000029 tonnes CO2/kg
- Allocation: 150,000,000 × 0.000029 = **4,350 allowances**

**Total Preliminary Allocation**: 2,437,500 + 1,814,000 + 4,350 = **4,255,850 allowances**

**Application of Allocation Factors**:
- CLEF (100%): 4,255,850 × 1.00 = 4,255,850
- CSCF (1.0): 4,255,850 × 1.00 = **4,255,850 allowances**

**Step 2: Determine Shortfall**

- Verified emissions: 4,606,000 tonnes CO2
- Free allocation: 4,255,850 allowances
- **Shortfall**: 4,606,000 - 4,255,850 = **350,150 allowances**

**Step 3: Calculate ETS Compliance Cost**

**Allowance Purchase Requirement**: 350,150 allowances

**Purchase Strategy**:
Assume purchases made quarterly through 2024 at average price:
- Average price: €85/tonne
- Total cost: 350,150 × €85 = **€29,762,750** (~€29.8 million)

**Adjustments for Banking** (simplified):
If EuroRefinery banked allowances from previous year: Reduce shortfall
If borrowed allowances from future: Increase future obligation

Assume no banking/borrowing for this example.

**Step 4: After-Tax Impact Analysis**

**Income Statement Impact**:

| Item | Amount (€ million) |
|------|--------------------|
| Revenue | 15,000.0 |
| Operating costs | (14,000.0) |
| **EBITDA** | **1,000.0** |
| ETS allowance cost | (29.8) |
| Depreciation (assume) | (200.0) |
| **EBIT** | **770.2** |
| Belgian tax @ 25% | (192.6) |
| **Net income** | **577.6** |

**Tax Deductibility of ETS Cost**:
- EU ETS allowance surrender costs are **tax-deductible** in Belgium
- Tax saving: €29.8m × 25% = **€7.45 million**
- Net after-tax cost: €29.8m - €7.45m = **€22.35 million**

**Per-Barrel ETS Cost**:
- Crude processed: 12 million tonnes ≈ 88 million barrels (at 7.33 bbl/tonne)
- ETS cost per barrel: €29.8m ÷ 88m = **€0.34/barrel** (gross)
- After-tax: €0.25/barrel

**Return on Sales**:
- Without ETS cost: €1,000m ÷ €15,000m = 6.67%
- With ETS cost: €970.2m ÷ €15,000m = 6.47%
- **Impact**: -0.20 percentage points (modest but material)

**Step 5: Emission Reduction Investment Evaluation**

EuroRefinery considers installing waste heat recovery system:

**Project Characteristics**:
- Capital cost: €50 million
- Emission reduction: 150,000 tonnes CO2/year
- Energy cost savings: €2 million/year (reduced fuel consumption)
- Expected life: 20 years

**Annual Benefits**:

**ETS Allowance Savings**:
- Reduced shortfall: 150,000 allowances/year
- Value @ €85/tonne: €12.75 million/year
- After-tax value: €12.75m × (1-0.25) = €9.56 million/year

Wait, this is incorrect. The allowance savings are a **cost avoidance**, not revenue. Correct calculation:

**Without project**:
- Must purchase 350,150 allowances
- Cost: €29.8m (before tax); €22.35m (after tax)

**With project**:
- Emissions reduced by 150,000 tonnes
- Must purchase: 350,150 - 150,000 = 200,150 allowances
- Cost: €17.0m (before tax); €12.76m (after tax)
- **Savings**: €9.59 million after-tax

**Energy Savings**:
- Fuel cost reduction: €2m/year (before tax)
- After-tax: €2m × (1-0.25) = **€1.5 million/year**

**Total Annual Benefit**: €9.59m + €1.5m = **€11.09 million/year**

**NPV Analysis**:
- Initial investment: -€50 million
- Annual benefit: €11.09 million
- Life: 20 years
- Discount rate: 10%
- PV factor (20 years, 10%): 8.514
- PV of benefits: €11.09m × 8.514 = €94.4 million
- **NPV**: €94.4m - €50m = **€44.4 million** (highly positive)

**Internal Rate of Return (IRR)**:
- €50m = €11.09m × [(1 - (1+r)^-20) / r]
- Solving: **IRR ≈ 22%** (well above cost of capital)

**Conclusion**:

The EU ETS creates strong economic incentive for the emission reduction investment. The project generates:
- Simple payback: 4.5 years
- NPV: €44.4 million
- IRR: 22%

This demonstrates the cap-and-trade mechanism effectively incentivizing abatement where marginal abatement cost (€50m ÷ 3m tonnes lifetime = €16.7/tonne) is well below the allowance price (€85/tonne).

**Additional Considerations**:

1. **Price volatility**: If allowance prices fall, investment attractiveness declines
2. **Long-term certainty**: Phase 5 cap (post-2030) unknown; policy risk
3. **Free allocation changes**: Benchmarks may tighten, increasing shortfall
4. **Innovation Fund**: Project may qualify for EU grants, improving economics further

**Recommendation**: Proceed with waste heat recovery investment. Consider additional abatement projects up to marginal cost of ~€85/tonne.

═══════════════════════════════════════════════════════════════

### WORKED EXAMPLE 2: ETS Linking and Carbon Leakage

**Facts**:

GlobalPetro Group operates refineries in three jurisdictions with different carbon pricing regimes:

**Refinery A (EU ETS)**:
- Location: Netherlands
- Capacity: 200,000 barrels/day
- Emissions: 3 million tonnes CO2/year
- Free allocation: 2.4 million allowances/year
- Allowance price: €90/tonne

**Refinery B (California Cap-and-Trade)**:
- Location: California, USA
- Capacity: 180,000 barrels/day
- Emissions: 2.7 million tonnes CO2/year
- Free allocation: Nil (100% auctioned for refineries)
- Allowance price: $32/tonne (€28/tonne @ 1.14 $/€)

**Refinery C (No ETS)**:
- Location: Singapore
- Capacity: 250,000 barrels/day
- Emissions: 3.8 million tonnes CO2/year
- Carbon cost: $0 (no carbon pricing)

**Corporate Structure**:
- Parent: GlobalPetro Holdings (Netherlands) - 25% corporate tax
- All refineries: wholly-owned subsidiaries

**Investment Decision**:
GlobalPetro plans to build a new 150,000 bbl/day refinery. Three locations considered:
- Expansion of Refinery A (Netherlands)
- Expansion of Refinery C (Singapore)
- New refinery in Middle East (no carbon pricing)

**Required**:

1. Calculate annual ETS compliance cost for Refineries A and B
2. Compare total tax burden (corporate tax + ETS) across locations
3. Assess carbon leakage risk: NPV of new refinery by location
4. Analyze impact of California-Quebec ETS linking
5. Evaluate CBAM implications for refined product exports to EU

**Analysis**:

**Step 1: ETS Compliance Costs**

**Refinery A (EU ETS)**:
- Emissions: 3,000,000 tonnes CO2
- Free allocation: 2,400,000 allowances
- Shortfall: 600,000 allowances
- Allowance price: €90/tonne
- **Annual ETS cost**: 600,000 × €90 = **€54 million**
- After-tax cost: €54m × (1-0.25) = **€40.5 million**

**Refinery B (California)**:
- Emissions: 2,700,000 tonnes CO2
- Free allocation: 0 (refineries not allocated free allowances)
- Shortfall: 2,700,000 allowances
- Allowance price: $32/tonne = €28/tonne
- **Annual ETS cost**: 2,700,000 × €28 = **€75.6 million**
- US federal corporate tax: 21%; California: 8.84%
- Combined rate: ~28%
- After-tax cost: €75.6m × (1-0.28) = **€54.4 million**

**Refinery C (Singapore)**:
- **ETS cost**: €0

**Step 2: Total Tax Burden Comparison**

Assume each refinery generates €200 million EBITDA (before ETS costs):

**Refinery A (Netherlands)**:

| Item | Amount (€m) |
|------|-------------|
| EBITDA | 200.0 |
| ETS cost | (54.0) |
| Depreciation | (40.0) |
| **Taxable income** | **106.0** |
| Corporate tax @ 25% | (26.5) |
| **Net income** | **79.5** |

Total burden: ETS €54m + Tax €26.5m = **€80.5 million**
Effective rate: 40.25% of EBITDA

**Refinery B (California)**:

| Item | Amount (€m) |
|------|-------------|
| EBITDA | 200.0 |
| ETS cost | (75.6) |
| Depreciation | (40.0) |
| **Taxable income** | **84.4** |
| Corporate tax @ 28% | (23.6) |
| **Net income** | **60.8** |

Total burden: ETS €75.6m + Tax €23.6m = **€99.2 million**
Effective rate: 49.6% of EBITDA

**Refinery C (Singapore)**:

| Item | Amount (€m) |
|------|-------------|
| EBITDA | 200.0 |
| ETS cost | 0 |
| Depreciation | (40.0) |
| **Taxable income** | **160.0** |
| Corporate tax @ 17% | (27.2) |
| **Net income** | **132.8** |

Total burden: ETS €0 + Tax €27.2m = **€27.2 million**
Effective rate: 13.6% of EBITDA

**Step 3: New Refinery Location Analysis**

New refinery specifications:
- Capacity: 150,000 bbl/day
- Expected EBITDA: €150 million/year
- Expected emissions: 2.25 million tonnes CO2/year
- Capital cost: €1.2 billion
- Expected life: 30 years

**Location 1: Netherlands (EU ETS)**

**Assumptions**:
- EU ETS allowance price forecast: €90/tonne initially, escalating 5%/year
- Free allocation: 50% of emissions (1.125 million allowances initially, declining 2.2%/year with Linear Reduction Factor)

**Year 1 Analysis**:
- Emissions: 2.25 million tonnes
- Free allocation: 1.125 million allowances
- Purchase requirement: 1.125 million allowances
- ETS cost: 1.125m × €90 = **€101.25 million**

**NPV Calculation** (simplified, constant real terms):
- Annual EBITDA: €150m
- Annual ETS cost: €101.25m (escalating with allowance price)
- Taxable income: €150m - €101.25m - depreciation
- After-tax cash flow estimate: ~€30 million/year (decreasing as ETS cost escalates)
- NPV @ 10% discount: Marginally positive or negative (depending on allowance price trajectory)

**Location 2: Singapore (No ETS)**

- Annual EBITDA: €150 million
- ETS cost: €0
- Corporate tax: €25.5 million (17%)
- After-tax cash flow: ~€110 million/year
- **NPV @ 10%, 30 years: €1.2bn investment vs. €110m annuity**
- NPV = -€1,200m + (€110m × 9.427) = **-€163 million** (negative, but much better than Netherlands)

Actually, let me recalculate more carefully:

**Singapore NPV**:
- EBITDA: €150m/year
- Depreciation: €1,200m / 30 = €40m/year
- Taxable income: €110m
- Tax @ 17%: €18.7m
- Net income: €91.3m
- Add back depreciation: €40m
- **Cash flow**: €131.3m/year

NPV = -€1,200m + (€131.3m × 9.427) = **€38.2 million** (positive)

**Netherlands NPV** (revised):
- EBITDA: €150m
- ETS cost: €101.25m
- Depreciation: €40m
- Taxable income: €8.75m
- Tax @ 25%: €2.2m
- Net income: €6.55m
- Add back depreciation: €40m
- **Cash flow**: €46.55m/year (first year; declines as ETS cost escalates)

NPV: Negative due to escalating ETS costs

**Conclusion**: **Singapore location economically superior** due to absence of ETS costs. This demonstrates **carbon leakage risk**: investment flows to jurisdictions without carbon pricing.

**Step 4: California-Quebec Linking Impact**

California and Quebec linked their cap-and-trade systems in 2014, creating larger market.

**Benefits of Linking**:
- Increased liquidity: More buyers/sellers → more efficient price discovery
- Reduced price volatility: Larger market smooths supply/demand shocks
- Lower compliance costs: Access to broader abatement opportunities

**Price Impact**:
- Pre-linking California allowance price: $15-20/tonne (2012-2013)
- Post-linking price: $12-18/tonne (2014-2017) initially
- Current (2024): ~$32/tonne

Linking initially **reduced prices** (Quebec had surplus allowances), benefiting California refiners. Over time, prices converged to efficient market level.

**Implications for Refinery B**:
- Linking provides cost savings vs. standalone California system
- However, still much higher cost than Singapore (zero) or potentially Middle East

**Step 5: CBAM Implications**

If Refinery C (Singapore) exports refined products to EU, the **Carbon Border Adjustment Mechanism (CBAM)** may apply (if/when refined petroleum products added to CBAM scope).

**Current CBAM Coverage** (2026-2034 transition):
- Cement, iron & steel, aluminum, fertilizers, electricity, hydrogen
- Refined products: **Not currently covered** but under consideration

**Hypothetical CBAM Application**:

Refinery C exports diesel to Netherlands: 2 million tonnes/year

**Embedded Emissions**:
- Refinery emissions: 3.8 million tonnes CO2
- Total production: 250,000 bbl/day × 365 × 0.1365 tonnes/bbl = 12.5 million tonnes products
- Emission intensity: 3.8m / 12.5m = **0.304 tonnes CO2/tonne product**

**CBAM Charge**:
- Diesel exports: 2 million tonnes
- Embedded emissions: 2m × 0.304 = 608,000 tonnes CO2
- EU ETS price: €90/tonne
- **CBAM charge**: 608,000 × €90 = **€54.7 million/year**

**Credit for Carbon Price Paid in Singapore**:
- Singapore carbon tax (if applicable): $0
- **CBAM credit**: €0
- **Net CBAM payment**: €54.7 million

**Impact on Competitiveness**:
- CBAM eliminates advantage of Singapore location for EU exports
- Refinery C would face similar carbon cost as EU refiners for EU-destined products
- However, Asian market sales still carbon-cost-free

**Strategic Response**:
- Invest in emission reduction to lower CBAM obligation
- Redirect sales to non-CBAM jurisdictions
- Lobby Singapore to introduce carbon pricing (earn CBAM credits)

**Conclusion**:

ETS costs create substantial competitive differences across jurisdictions:
- Netherlands: Highest burden (ETS + corporate tax)
- California: High burden (full auction) but lower allowance price
- Singapore: Lowest burden (no ETS)

This drives carbon leakage—new investment flows to Singapore/Middle East. However, CBAM can mitigate this for EU-destined exports, though requires refined products to be added to CBAM scope.

**Recommendations for GlobalPetro**:
1. Short-term: Build new refinery in Singapore (absent CBAM for refined products)
2. Medium-term: Monitor CBAM expansion; may need emission reduction investments
3. Long-term: Diversify portfolio to include low-carbon refineries (bio-refineries, hydrogen integration) in anticipation of global carbon pricing convergence
4. Engage policymakers: Advocate for free allocation continuation for trade-exposed refineries
5. Optimize allowance purchasing: Use linking opportunities (California-Quebec) and banking strategies

═══════════════════════════════════════════════════════════════

### WORKED EXAMPLE 3: Transfer Pricing for Intragroup ETS Trading

**Facts**:

MegaOil Corporation, a global integrated oil company headquartered in the UK, operates multiple facilities covered by the EU ETS across different member states:

**Corporate Structure**:
- **Parent**: MegaOil plc (UK)
- **Subsidiaries** (EU):
  - Refinery 1: MegaOil Netherlands BV (Netherlands)
  - Refinery 2: MegaOil Italiana SpA (Italy)
  - Petrochemical: MegaOil Belgium NV (Belgium)
  - Trading: MegaOil Trading GmbH (Germany) - established 2023

**Emissions and Allocations (2024)**:

| Entity | Verified Emissions | Free Allocation | Net Position |
|--------|-------------------|-----------------|--------------|
| Netherlands BV | 4,000,000 | 3,200,000 | -800,000 (short) |
| Italiana SpA | 3,500,000 | 3,000,000 | -500,000 (short) |
| Belgium NV | 2,200,000 | 1,800,000 | -400,000 (short) |
| **Total Group** | **9,700,000** | **8,000,000** | **-1,700,000** |

**Transfer Pricing Issue**:

MegaOil Trading GmbH established to:
- Centralize ETS compliance management
- Purchase allowances in bulk (potential volume discounts)
- Provide market expertise and price risk management
- On-sell allowances to operating subsidiaries

**Transaction Structure (2024)**:
- MegaOil Trading purchases 2 million EU Allowances (EUAs) in market
- Average purchase price: €85/tonne
- On-sells to subsidiaries:
  - Netherlands: 800,000 EUAs @ €88/tonne
  - Italy: 500,000 EUAs @ €88/tonne
  - Belgium: 400,000 EUAs @ €88/tonne
  - Surplus: 300,000 EUAs held for 2025

**Tax Authority Concerns**:
- German tax authority: Is markup justified? Substance of trading entity?
- Dutch/Italian/Belgian authorities: Arm's length pricing for purchases?

**Market Data**:
- EUA spot price December 2024: €87/tonne
- EUA futures (Dec 2025): €92/tonne
- Transaction costs (exchange fees, clearing): €0.15/tonne
- Bank financing cost: 4% annual

**Required**:

1. Determine appropriate transfer pricing method for intragroup allowance sales
2. Assess whether €88/tonne pricing is arm's length
3. Calculate German taxable income and tax liability of Trading entity
4. Evaluate transfer pricing documentation requirements
5. Analyze economic substance requirements for Trading entity
6. Assess permanent establishment risks

**Analysis**:

**Step 1: Transfer Pricing Method Selection**

**OECD Transfer Pricing Guidelines** (Chapter II):

Available methods:
1. **Comparable Uncontrolled Price (CUP)**: Compare to independent transactions
2. **Resale Price Method**: Based on resale margin
3. **Cost Plus Method**: Cost + appropriate markup
4. **Transactional Net Margin Method (TNMM)**: Compare net margins
5. **Profit Split Method**: Allocate profits based on contributions

**Analysis**:
- EUAs are **commodities** traded on regulated exchanges (ICE Futures Europe, EEX)
- Market prices are **publicly available** and transparent
- **CUP method is most appropriate** (reliable comparable prices exist)

**Step 2: Arm's Length Price Determination**

**Comparable Uncontrolled Price (CUP) Analysis**:

**External comparables**:
- Spot market price (December 2024): €87/tonne
- Futures price (delivery 2025): €92/tonne
- Over-the-counter (OTC) transactions: €86-88/tonne (depending on volume, timing)

**Transaction characteristics**:
- Volume: 1.7 million EUAs (substantial)
- Timing: Purchased throughout 2024, transferred Q4 2024
- Terms: Immediate transfer (no financing period)
- Risk: Trading entity bears market risk from purchase to transfer

**Adjustments to comparable price**:

**Volume discounts**:
- Large transactions (>1 million EUAs) may achieve €0.10-0.30/tonne discount
- Adjustment: -€0.20/tonne

**Transaction costs**:
- Exchange fees and clearing: €0.15/tonne
- Adjustment: +€0.15/tonne

**Financing costs**:
- If Trading entity provides payment terms (e.g., 30-day credit): Imputed interest
- Assume immediate payment: No adjustment

**Risk premium**:
- Trading entity holds market risk (price volatility)
- Premium for this service: €0.50-1.50/tonne
- Adjustment: +€1.00/tonne (midpoint)

**Service fee**:
- Market monitoring, compliance expertise, administrative support
- Comparable to commodity trading service fees: 1-3% of value
- At €85 spot price: €0.85-2.55/tonne
- Adjustment: +€1.70/tonne (2%)

**Arm's Length Price Calculation**:

| Component | Amount (€/tonne) |
|-----------|------------------|
| Spot market price | 87.00 |
| Volume discount | (0.20) |
| Transaction costs | 0.15 |
| Risk premium | 1.00 |
| Service fee (2%) | 1.70 |
| **Arm's length range** | **87.65 - 89.65** |
| **Midpoint** | **88.65** |

**Actual charged price**: €88/tonne

**Conclusion**: €88/tonne is **within arm's length range** (87.65-89.65) and therefore defensible.

**Step 3: German Taxable Income and Tax**

**MegaOil Trading GmbH (Germany) Income Statement**:

| Item | Amount (€) |
|------|------------|
| **Revenue** | |
| Allowance sales to Netherlands (800,000 @ €88) | 70,400,000 |
| Allowance sales to Italy (500,000 @ €88) | 44,000,000 |
| Allowance sales to Belgium (400,000 @ €88) | 35,200,000 |
| **Total revenue** | **149,600,000** |
| **Cost of Sales** | |
| Allowance purchases (2,000,000 @ €85) | (170,000,000) |
| Allowance inventory (300,000 @ €85)* | 25,500,000 |
| **Net cost of sales** | **(144,500,000)** |
| **Gross profit** | **5,100,000** |
| Operating expenses (salaries, office, IT) | (1,200,000) |
| **Taxable income** | **3,900,000** |
| German corporate tax @ 15% (federal) | (585,000) |
| Trade tax @ 14% (approx, varies by locality) | (546,000) |
| **Total tax** | **(1,131,000)** |
| **Net income** | **2,769,000** |

*Inventory: 300,000 allowances purchased at €85, held for 2025, valued at cost

**Gross margin**: €5.1m / €149.6m = **3.4%** (reasonable for commodity trading)

**Step 4: Transfer Pricing Documentation Requirements**

Under EU Transfer Pricing Directive and German AO §90(3), MegaOil must prepare:

**Master File** (group-level):
- Organizational structure
- Description of ETS compliance strategy
- Intangible property (if any trading algorithms, expertise)
- Financial and tax positions

**Local File** (MegaOil Trading GmbH):
- Detailed description of controlled transactions
- Functional analysis:
  - **Functions**: Market monitoring, allowance procurement, price risk management, allocation to operating entities
  - **Assets**: Working capital, IT systems, market data subscriptions
  - **Risks**: Price volatility risk, counterparty risk, regulatory risk
- Comparability analysis (CUP method with market price data)
- Selection and application of transfer pricing method
- Documentation of €88/tonne pricing as arm's length

**Key Documentation Elements**:

1. **Market price evidence**:
   - Daily EUA spot prices from ICE Futures Europe
   - Comparable OTC transaction data (if available)
   - Futures curve data

2. **Functional analysis support**:
   - Employment contracts for traders and analysts
   - Evidence of decision-making in Germany (board minutes, email records)
   - Bloomberg/Reuters subscriptions showing market data access
   - Trading platform access records

3. **Economic rationale**:
   - Memo explaining benefits of centralized ETS management:
     - Economies of scale in purchasing
     - Specialized expertise concentration
     - Reduced subsidiary admin burden
     - Risk pooling across entities

4. **Benchmarking** (if available):
   - Commodity trading company margins (1-5% typical)
   - Service fee comparables (1-3% of transaction value)

**Step 5: Economic Substance Analysis**

German tax authorities will scrutinize whether Trading entity has **sufficient substance** to justify profits:

**Substance Requirements**:

**Personnel**:
- **Required**: At minimum 2-3 full-time employees
  - Senior trader (decision-making authority)
  - Analyst/compliance officer
  - Administrative support
- **Actual (assumed)**: 3 employees; total compensation €500,000/year
- **Assessment**: ✓ Adequate

**Office**:
- **Required**: Physical office space in Germany
- **Actual**: Dedicated office in Frankfurt (financial center)
- **Assessment**: ✓ Adequate

**Decision-Making**:
- **Required**: Key business decisions made in Germany
- **Evidence needed**:
  - Board meetings held in Germany
  - Email traffic showing traders in Germany making buy/sell decisions
  - Trading platform access from German IP addresses
- **Assessment**: Critical - must be documented

**Assets**:
- **Required**: IT infrastructure, market data, working capital
- **Actual**: Bloomberg terminal (€20k/year), trading platform, €170m working capital
- **Assessment**: ✓ Adequate

**Risk-Bearing**:
- **Question**: Does Trading entity bear real economic risk?
- **Analysis**:
  - Yes: Holds inventory (300k EUAs subject to price volatility)
  - Yes: Bears credit risk on receivables from subsidiaries
  - Potential issue: Working capital provided by parent (debt or equity?)
- **Assessment**: ✓ Adequate if properly capitalized

**Conclusion**: Trading entity can satisfy substance requirements if:
1. Employees actually work in Germany and make decisions
2. Board meetings held in Germany with documented authority
3. Adequate equity capital (not just debt from parent)

**Step 6: Permanent Establishment Risks**

**Issue**: Does centralized ETS trading create PE for MegaOil plc (UK) in other EU countries?

**Analysis Under OECD Model (Article 5)**:

**Fixed Place of Business PE**:
- Trading entity is separate legal entity (GmbH), not a branch
- Operating subsidiaries are also separate legal entities
- **Conclusion**: No fixed place PE for UK parent (separate entities shield)

**Dependent Agent PE** (Article 5(5)):
- Does Trading entity act as dependent agent of UK parent in EU countries?
- **Analysis**:
  - Trading entity transacts with sister subsidiaries, not on behalf of parent
  - No authority to conclude contracts binding parent in other countries
- **Conclusion**: No dependent agent PE

**Service PE** (UN Model, some treaties):
- Some tax treaties have service PE provisions (183 days, etc.)
- UK's treaties with EU countries: Generally no service PE article
- **Conclusion**: Not applicable

**Overall PE Assessment**: **Low risk** - separate legal entities and substance in Germany protect against PE attribution.

**Conclusion and Recommendations**:

**Transfer Pricing Assessment**:
- €88/tonne pricing is **defensible** (within arm's length range of €87.65-89.65)
- CUP method is appropriate given commodity nature and market price availability
- Gross margin of 3.4% is reasonable for commodity trading services

**Documentation Recommendations**:
1. **Maintain contemporaneous TP documentation** (Master File + Local Files)
2. **Retain market price evidence**: Daily EUA prices, screenshot trading platform quotes
3. **Document economic rationale**: Memo explaining centralization benefits
4. **Evidence substance**: Employment contracts, office lease, board minutes in German language
5. **Benchmark margins**: Collect comparable data on commodity trading margins

**Substance Recommendations**:
1. **Ensure genuine operations**: Traders must be based in Germany and make real decisions
2. **Capitalize appropriately**: Trading entity should have equity capital sufficient for working capital needs (not 100% parent debt)
3. **Document decision-making**: Board resolutions authorizing trades; email traffic showing German employees deciding
4. **Avoid cash box**: Trading entity should perform genuine functions, not merely book transactions decided elsewhere

**Risk Assessment**:

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| TP adjustment (pricing) | Low | Medium | Documentation + pricing within range |
| Substance challenge | Medium | High | Ensure genuine German operations |
| PE creation | Low | High | Separate legal entities + documentation |
| Tax audit | Medium | Medium | Robust documentation prepared |

**Alternative Structure** (if substance concerns):

Instead of separate Trading entity, use **shared services model**:
- UK parent provides ETS trading services to subsidiaries
- Charge arm's length service fee (cost + 5-8% markup)
- Simpler structure; less substance risk
- But: Loses potential tax rate arbitrage (Germany 29% vs. UK 25%)

**Final Recommendation**: Current structure is **defensible** if substance requirements are met. Benefits (centralization, expertise) justify existence of Trading entity. Maintain robust documentation and ensure genuine German operations.

═══════════════════════════════════════════════════════════════
