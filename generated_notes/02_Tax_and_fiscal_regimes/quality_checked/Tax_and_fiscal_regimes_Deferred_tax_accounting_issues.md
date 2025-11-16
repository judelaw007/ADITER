# Deferred Tax Accounting Issues - Energy Resources

## 1. Core Framework and Statutory Basis

**Deferred tax accounting** addresses timing differences between accounting income and taxable income, recognizing tax consequences of future recovery or settlement of assets and liabilities. In energy resources, significant capital investments, long-lived assets, and complex provisions create substantial deferred tax positions requiring careful analysis under **IAS 12** (IFRS) or **ASC 740** (US GAAP).

### 1.1 IAS 12 and ASC 740 Principles

Both standards adopt a **balance sheet approach** (versus historical income statement approach), focusing on temporary differences between:
- **Carrying amount** of assets/liabilities (financial reporting basis)
- **Tax base** of assets/liabilities (tax reporting basis)

**IAS 12 "Income Taxes"** (issued 1996, most recently amended 2023) requires:
- Recognition of deferred tax for all temporary differences (subject to limited exceptions)
- Measurement using enacted or substantively enacted tax rates
- Recognition of deferred tax assets only when probable that taxable profit will be available

**ASC 740 "Income Taxes"** applies similar principles but differs in:
- "More likely than not" threshold (>50% probability) versus IAS 12's "probable" (typically interpreted as >50%)
- Recognition of deferred tax on undistributed foreign earnings unless indefinitely reinvested
- Prohibition on discounting deferred tax balances (IAS 12 also prohibits)

### 1.2 Deferred Tax Assets vs. Liabilities

| Type | Arises From | Energy Sector Example | Tax Impact |
|------|-------------|----------------------|------------|
| **Deferred Tax Liability (DTL)** | Taxable temporary difference - tax deduction exceeds book expense | Accelerated tax depreciation on production facilities | Future taxable amount when asset recovered |
| **Deferred Tax Asset (DTA)** | Deductible temporary difference - book expense exceeds tax deduction | Decommissioning provisions recognized but not yet deductible | Future deductible amount when liability settled |

**Calculation**: Deferred tax = Temporary difference × Applicable tax rate

### 1.3 Temporary vs. Permanent Differences

**Temporary differences** reverse over time and create deferred tax:
- Depreciation timing (accelerated tax vs. straight-line book)
- Decommissioning provisions (accrued book vs. cash basis tax)
- E&E expenditure (capitalized book vs. expensed tax)
- Unrealized foreign exchange gains/losses

**Permanent differences** never reverse and affect only current tax:
- Non-deductible entertainment expenses
- Tax-exempt income (e.g., certain government grants)
- Non-deductible penalties
- Resource rent tax adjustments

## 2. Energy Sector Specific Issues

### 2.1 Exploration and Evaluation (E&E) Assets

Under **IFRS 6 "Exploration for and Evaluation of Mineral Resources"**, companies may capitalize E&E costs until technical feasibility is established. Tax treatment varies by jurisdiction:

**Immediate tax deduction**: Creates deductible temporary difference (DTA)
- Carrying amount: USD 100M (capitalized)
- Tax base: USD 0 (deducted)
- Temporary difference: USD 100M deductible
- DTA at 30%: USD 30M

**Tax capitalization**: No temporary difference initially, but depreciation timing differs subsequently.

### 2.2 Decommissioning Provisions

**IAS 37 "Provisions, Contingent Liabilities and Contingent Assets"** / **ASC 410 "Asset Retirement and Environmental Obligations"** require recognition of asset retirement obligations (ARO) at present value, with offsetting increase to asset cost. Tax deduction typically allowed only when costs incurred.

**Example timing**:
- Year 1: Book provision USD 50M (PV), no tax deduction → DTA USD 15M (30% rate)
- Year 20: Actual spend USD 150M, tax deduction USD 150M → DTA reverses plus additional deduction

**Unwinding discount**: Annual accretion expense (interest expense on the provision) creates additional deductible temporary differences as it is recognized in book expense but not deductible for tax until paid.

### 2.3 Successful Efforts vs. Full Cost Accounting

**Successful efforts** (IFRS, US GAAP for most): Unsuccessful exploration expensed, successful wells capitalized
- Dry holes expensed for both book and tax → Permanent difference if timing aligns
- Deferred tax arises only from depreciation timing differences on successful wells

**Full cost** (permitted under US GAAP in certain circumstances): All exploration costs capitalized within cost centers
- Creates larger temporary differences when tax deduction is immediate but book capitalized
- Impairment charges may create permanent differences

### 2.4 Tax Depreciation vs. Book Depreciation

Energy assets commonly receive **accelerated tax depreciation** or enhanced capital allowances to incentivize capital investment:

| Jurisdiction | Asset Type | Tax Treatment | Book Treatment |
|--------------|------------|---------------|----------------|
| **US** | Production equipment | MACRS 7-year (accelerated) | 20-30 year straight-line |
| **UK** | North Sea installations | 100% first-year allowance | 20-25 year UOP/straight-line |
| **Norway** | Petroleum facilities | Declining balance 16.67% | UOP over reserves |
| **Australia** | LNG plant | Diminishing value 15% | 25-40 year straight-line |

Result: **Significant DTL** in early years (tax deductions exceed book depreciation), reversing as asset ages and book depreciation exceeds remaining tax allowances.

## 3. Recognition and Measurement

### 3.1 Recognition Criteria

**Deferred Tax Liabilities**: Recognized for all taxable temporary differences except:
- Goodwill (IAS 12.15, ASC 740-10-25-13) - because amortization of goodwill is typically not deductible
- Initial recognition of assets/liabilities in transactions that are not business combinations and affect neither accounting nor taxable profit

**Deferred Tax Assets**: Recognized only when **probable** (IAS 12) or **more likely than not** (ASC 740) that:
- Sufficient taxable profit will be available against which deductible temporary differences can be utilized
- Evidence includes: taxable temporary differences reversing in same period, tax planning opportunities, history of taxable profits

### 3.2 Valuation Allowances

When realization is uncertain, **valuation allowance** (ASC 740) or reduced recognition (IAS 12) required:

**Negative evidence**:
- Cumulative losses in recent years (typically three years)
- History of tax loss carryforwards expiring unused
- Uncertain future profitability (e.g., unproven reserves, volatile commodity prices)
- Short expiration periods for tax attributes

**Positive evidence**:
- Existing contracts (e.g., long-term offtake agreements at fixed prices)
- Proven reserves supporting future production
- Strong forward commodity prices under long-term contracts
- Reversing DTLs of same tax jurisdiction and timing

**Example**: Company with USD 100M tax loss carryforward (DTA USD 30M at 30%) and three consecutive loss years → Valuation allowance USD 30M likely required unless substantial proven reserves and contracted sales demonstrate future profitability.

### 3.3 Tax Rate Selection

Use **enacted** (ASC 740) or **substantively enacted** (IAS 12) tax rates expected to apply when temporary difference reverses:

**Multi-rate regimes**: Common in energy taxation where specialized petroleum taxes apply
- Norwegian petroleum: 22% general corporate tax + 56% special petroleum tax = 78% combined marginal rate
- UK North Sea (as of 2024): 30% ring fence corporation tax + 10% supplementary charge + 38% Energy Profits Levy = 78% total rate

**Rate changes**: Remeasure all deferred tax balances when new rates are enacted or substantively enacted, recognizing impact in current period tax expense (unless related to items recognized in OCI, in which case the remeasurement is recognized in OCI).

## 4. Disclosure Requirements

### 4.1 Balance Sheet Presentation

**Classification**: Offset deferred tax assets and liabilities only if:
- Legal right to offset current tax assets and liabilities exists
- Same tax jurisdiction and same taxable entity

Energy companies often have:
- Current DTL: Accelerated depreciation on production facilities
- Non-current DTA: Long-term decommissioning provisions
- Separate presentation by jurisdiction required when offsetting criteria not met

### 4.2 Income Statement Reconciliation

**IAS 12.81(c)** and **ASC 740-10-50-12** require reconciliation of tax expense to accounting profit × statutory rate:

| Item | Amount (USD M) | Rate Impact |
|------|----------------|-------------|
| Accounting profit | 500.0 | - |
| Tax at statutory rate (30%) | 150.0 | 30.0% |
| Resource rent tax (non-deductible) | 25.0 | 5.0% |
| Tax depreciation vs. book | (35.0) | (7.0)% |
| Decommissioning provision increase | (8.0) | (1.6)% |
| Valuation allowance on losses | 12.0 | 2.4% |
| **Effective tax expense** | **144.0** | **28.8%** |

### 4.3 Deferred Tax Roll-forward

Disclose movements in deferred tax balances by major category of temporary difference:
- Opening balance
- Recognized in profit/loss
- Recognized in OCI or equity
- Business combinations
- Exchange differences
- Closing balance

## 5. Worked Example: Deferred Tax Calculation

### Fact Pattern

**PetroNorth Ltd.** commences North Sea production in Year 1. Initial transaction data:

**Assets**:
- Production platform: Cost USD 800M, 20-year straight-line depreciation (book), 100% first-year allowance (tax)
- E&E capitalized: USD 200M (successful wells), amortizing over 10 years (book), immediately deductible (tax)

**Liabilities**:
- Decommissioning provision: USD 60M (present value), actual cost expected in Year 20, tax deductible when paid

**Tax rate**: 40% (UK ring fence corporation tax 30% + supplementary charge 10%)

**Year 1 profit before tax**: USD 150M

### Analysis - Temporary Differences Table

| Item | Carrying Amount | Tax Base | Temporary Difference | DT Asset (Liability) |
|------|-----------------|----------|---------------------|---------------------|
| **Production platform** | 760M (800-40) | 0 | 760M taxable | (304.0M) |
| **E&E assets** | 180M (200-20) | 0 | 180M taxable | (72.0M) |
| **Decommissioning provision** | (60M) | 0 | 60M deductible | 24.0M |
| **Net deferred tax liability** | - | - | - | **(352.0M)** |

### Year 1 Current Tax Calculation

| Description | Amount (USD M) |
|-------------|----------------|
| Accounting profit | 150.0 |
| Add: Book depreciation (platform) | 40.0 |
| Add: Book amortization (E&E) | 20.0 |
| Add: Decommissioning accretion | 2.0 |
| Less: Tax depreciation (platform) | (800.0) |
| Less: E&E deduction | (200.0) |
| Less: Decommissioning payment | 0 |
| **Taxable profit** | **(788.0)** |
| Tax loss carried forward | 788.0 |

**Current tax payable**: USD 0 (loss position)

**Deferred tax on loss carryforward**: USD 315.2M (788M × 40%)

### Complete Deferred Tax Position

| Component | DTA (DTL) (USD M) |
|-----------|-------------------|
| Platform depreciation timing | (304.0) |
| E&E amortization timing | (72.0) |
| Decommissioning provision | 24.0 |
| Tax loss carryforward | 315.2 |
| **Net deferred tax asset** | **(36.8)** |

**Valuation allowance assessment**: If PetroNorth has proven reserves supporting 15-year profitable production and long-term offtake contracts, full recognition is appropriate. If reserves are unproven or commodity prices are weak and volatile, a valuation allowance on the loss carryforward DTA may be required.

### Journal Entries

```
Dr. Deferred Tax Asset - Loss Carryforward    315.2M
Dr. Deferred Tax Asset - Decommissioning       24.0M
    Cr. Deferred Tax Liability - Platform              304.0M
    Cr. Deferred Tax Liability - E&E                    72.0M
    Cr. Tax Benefit (Income Statement)                 (36.8M)
```

**Income statement impact**: Tax benefit of USD 36.8M reduces effective rate to -24.5% on profit of USD 150M (benefit of USD 36.8M divided by profit of USD 150M).

## 6. Recent Developments (2023-2025)

**IAS 12 Amendments - Single Transaction (effective January 2023)**: "Deferred Tax related to Assets and Liabilities arising from a Single Transaction" (issued May 2021, effective for annual periods beginning on or after January 1, 2023) requires recognition of deferred tax on transactions creating equal taxable and deductible temporary differences (e.g., leases under IFRS 16, decommissioning provisions). Eliminates the initial recognition exemption for these transactions, increasing both DTA and DTL recognition.

**Pillar Two Implementation (2024-2025)**: IAS 12 amendments issued May 2023 provide a temporary exception from recognizing and disclosing deferred taxes arising from Pillar Two income taxes. Instead, companies account for Pillar Two tax as current tax when incurred and provide specific disclosures about exposure to Pillar Two income taxes.

**IFRS 18 "Presentation and Disclosure in Financial Statements" (effective January 2027)**: Replaces IAS 1 and introduces enhanced presentation requirements including more detailed disaggregation of tax expenses by jurisdiction and nature, improving transparency of multinational energy companies' tax positions.

**ASC 740 Enhanced Disclosures (2024)**: SEC requirements mandate enhanced disclosure of rate reconciliation items exceeding 5% threshold in annual filings, affecting energy companies with complex multi-jurisdictional operations and specialized petroleum taxes.

**Climate-related tax incentives**: Increased deferred tax complexity from investment tax credits (ITCs) for carbon capture (US Section 45Q providing USD 60-85 per metric ton of CO2), hydrogen production (Section 45V), and renewable energy projects, requiring careful assessment of realizability based on project economics and technical feasibility.
