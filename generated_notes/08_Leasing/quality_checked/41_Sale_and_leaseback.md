# 41. Sale and Leaseback

## Introduction

A **sale and leaseback** transaction involves an asset owner (seller-lessee) selling an asset to a buyer (buyer-lessor) and simultaneously leasing it back. This financing technique is widely used in the oil and gas sector to **unlock capital** tied up in assets (drilling rigs, production facilities, pipelines, FPSOs) while maintaining operational control through the leaseback.

The tax implications are complex, as tax authorities scrutinize whether the transaction represents a **genuine sale** or a **disguised financing arrangement**. If recharacterized as financing, the tax benefits (immediate gain recognition, rental expense deductions) may be denied.

---

## 1. Commercial Rationale

### 1.1 Benefits for Seller-Lessee

**Liquidity**: Immediate cash injection from asset sale without losing operational use

**Off-balance sheet financing** (pre-International Financial Reporting Standards (IFRS) 16 / Accounting Standards Codification (ASC) 842): Historically removed assets and liabilities from balance sheet, improving financial ratios

**Tax benefits**:
- **Immediate gain recognition**: If asset sold at a gain, gain is recognized (potentially at favorable capital gains rates)
- **Rental deductions**: Lease payments are fully deductible (may exceed depreciation deductions on retained ownership)

**Example**:

An operator owns a production facility with:
- **Original cost**: $100 million
- **Accumulated depreciation**: $40 million
- **Net book value**: $60 million
- **Fair market value**: $150 million
- **Annual depreciation** (if retained): $5 million

**Sale and leaseback**:
- **Sale price**: $150 million (cash received)
- **Gain on sale**: $150M - $60M = $90 million
- **Annual lease payment**: $20 million (deductible)

**Tax comparison**:

| Scenario | Annual Deduction | Gain Recognition |
|----------|------------------|------------------|
| **Retain ownership** | $5M depreciation | No gain |
| **Sale and leaseback** | $20M rental expense | $90M gain (year 1) |

If the gain is taxed at **capital gains rate** (lower than ordinary income) and the **rental deduction** offsets high-taxed operating income, the transaction can be tax-advantageous.

### 1.2 Benefits for Buyer-Lessor

**Investment return**: Earns rental income with security of asset ownership

**Depreciation deductions**: Buyer depreciates asset based on purchase price (stepped-up basis)

**Residual value**: Retains asset at lease end (or exercises purchase option)

---

## 2. Tax Treatment - True Sale vs. Financing

### 2.1 True Sale

For tax purposes, a **true sale** occurs if:

- **Legal title** and **substantially all risks and rewards** of ownership transfer to buyer
- **Seller-lessee** has no continuing ownership interest (no repurchase obligation or option at below FMV)
- **Transaction has economic substance** (not purely tax-motivated)

**Tax Consequences**:

**Seller-Lessee**:
1. **Recognize gain or loss** on sale: Sale price - Net book value
2. **Deduct lease payments** as ordinary business expenses
3. **No depreciation** (no longer owns asset)

**Buyer-Lessor**:
1. **Capitalize asset** at purchase price (stepped-up basis)
2. **Recognize rental income**
3. **Depreciate asset** over its useful life

### 2.2 Disguised Financing (Failed Sale)

If the transaction **lacks economic substance**, tax authorities may recharacterize it as a **secured loan**:

**Indicators of Financing**:
- **Repurchase obligation** or **fixed-price repurchase option** at below FMV
- **Seller-lessee retains substantial risks** (e.g., responsible for all maintenance, insurance, obsolescence)
- **Lease term** covers substantially all of asset's useful life
- **Lease payments** approximate debt service (principal + interest)

**Tax Consequences (Recharacterized as Financing)**:

**Seller-Lessee**:
1. **No gain recognition** on "sale" (treated as receipt of loan proceeds)
2. Asset remains on seller's books; **continue depreciation**
3. Lease payments bifurcated:
   - **Interest component**: Deductible
   - **Principal component**: Non-deductible loan repayment

**Buyer-Lessor**:
1. **No asset acquisition** (treated as loan to seller)
2. Rental income recharacterized as **interest income**

### 2.3 IRS Factors for Sale Treatment

The **Internal Revenue Service (IRS)** considers the following factors (no single factor determinative):

1. **Transfer of legal title**: Clear, unconditional transfer?
2. **Transfer of benefits and burdens**: Who bears risk of loss, obsolescence, and receives residual value?
3. **Seller's continuing involvement**: Does seller retain control or have right to reacquire?
4. **Terms of repurchase**: If repurchase option exists, is it at FMV or fixed price?
5. **Arm's length terms**: Are lease payments and sale price consistent with FMV?
6. **Business purpose**: Is there a genuine business reason beyond tax benefits?

---

## 3. Timing of Gain Recognition

### 3.1 Immediate Recognition (True Sale)

If the transaction qualifies as a **true sale**, the gain is **immediately recognizable**:

```
Gain = Sale price - Adjusted basis
Tax = Gain × Applicable tax rate (capital gains or ordinary income)
```

**Capital Gains Treatment**: If the asset is a **capital asset** or **Section 1231 property** held for more than one year, gain may qualify for favorable **long-term capital gains rates** (lower than ordinary income rates).

**Section 1245 Recapture**: For **depreciable personal property** (equipment, machinery), **accumulated depreciation** is recaptured as **ordinary income**; only appreciation above original cost receives capital gains treatment.

### 3.2 Deferred Recognition (Failed Sale)

If recharacterized as **financing**, no gain is recognized. The seller continues to own the asset for tax purposes and depreciates it.

### 3.3 Partial Gain Recognition (Proportionate Leaseback)

In some jurisdictions, if the **leaseback term** is significantly shorter than the asset's remaining useful life, **partial gain recognition** may apply:

```
Immediate gain = Total gain × (1 - PV of leaseback / FMV)
Deferred gain = Total gain - Immediate gain
```

The deferred portion is **amortized** over the lease term and offsets rental deductions.

---

## 4. Transfer Pricing Considerations

### 4.1 Related-Party Transactions

When sale and leaseback occurs between **related parties** (e.g., parent company sells asset to subsidiary, then leases it back), **transfer pricing rules** require:

- **Sale price** must be at **fair market value** (arm's length)
- **Lease payments** must be at **arm's length rates**

**Risk**: Tax authorities may challenge:
- **Inflated sale price** (artificially increasing gain, shifting profits to low-tax buyer jurisdiction)
- **Excessive lease payments** (shifting profits from lessee to lessor)

**Documentation**: Requires **independent valuation** of asset and **comparable lease rate analysis**.

### 4.2 Cross-Border Transactions

**Withholding Tax**: Lease payments from seller-lessee (in one country) to buyer-lessor (in another country) may be subject to **withholding tax** (see Chapter 40 on Leasing and Tax Treaties).

**Exit Tax**: If the sale involves transfer of asset from one jurisdiction to another, **exit taxation** may apply (deemed disposition at FMV).

---

## 5. Accounting vs. Tax Treatment

### 5.1 IFRS 16 / ASC 842

Under **IFRS 16 (Leases)** and **ASC 842 (Leases)** (effective 2019), sale and leaseback accounting depends on whether the transfer qualifies as a **sale** under revenue recognition standards (IFRS 15 (Revenue from Contracts with Customers) / ASC 606 (Revenue from Contracts with Customers)):

**If qualifies as a sale**:
- **Seller-lessee**: Recognizes gain (limited to rights transferred to buyer; retains retained interest)
- **Leaseback**: Recognized as a new lease (ROU asset and lease liability)

**If does not qualify as a sale**:
- **Seller-lessee**: No gain recognition; transaction treated as **financing arrangement**
- Asset remains on books; cash received is a **financial liability**

**Key Condition**: Buyer must obtain **control** of the asset (not merely a security interest).

### 5.2 Tax-Book Differences

**Tax treatment** may diverge from **accounting treatment**:

- A transaction that is a **sale for accounting purposes** (IFRS 15 / ASC 606 met) may be **financing for tax purposes** (IRS factors not satisfied)
- Conversely, a transaction that is **financing for accounting** may be a **sale for tax** (if tax authorities accept genuine transfer of risks and rewards)

**Consequence**: Creates **temporary differences** requiring deferred tax accounting.

---

## WORKED EXAMPLE: Sale and Leaseback of Production Facility

### Facts

**TropicOil Inc.**, a U.S.-based E&P company, owns a **natural gas processing facility** in Texas with the following characteristics:

- **Original cost**: $200 million (placed in service 10 years ago)
- **Accumulated MACRS depreciation**: $140 million
- **Adjusted tax basis**: $60 million
- **Fair market value**: $180 million

**Transaction Structure**:

TropicOil sells the facility to **GasLease Capital LLC**, an unrelated third-party leasing company, for **$180 million cash**. Simultaneously, TropicOil leases the facility back under the following terms:

- **Lease type**: Operating lease (GasLease retains ownership)
- **Lease term**: 12 years
- **Annual lease payment**: $22 million
- **Purchase option at end**: TropicOil has option to repurchase at **fair market value** (not fixed price)
- **Maintenance**: TropicOil responsible for routine maintenance; GasLease responsible for major capital expenditures

**Remaining Useful Life**: 20 years

**Tax Rates**:
- **U.S. corporate tax**: 21%
- **Long-term capital gains**: 21% (same rate for corporations; no preferential rate)

### Required

1. Determine whether the transaction qualifies as a **true sale** for tax purposes
2. Calculate the **immediate tax impact** on TropicOil
3. Calculate the **annual tax benefit** from rental deductions vs. retained ownership
4. Evaluate the **net present value** of tax benefits (assume 8% discount rate)

### Analysis

**Step 1: True Sale Qualification**

**IRS Factors Analysis**:

| Factor | Analysis | Supports Sale? |
|--------|----------|----------------|
| **Legal title transfer** | Full transfer to GasLease | ✓ Yes |
| **Benefits and burdens** | GasLease bears residual value risk, major capital expenditures | ✓ Yes |
| **Seller's continuing involvement** | TropicOil operates facility (typical for leaseback) | Neutral |
| **Repurchase option** | At **FMV** (not fixed), optional | ✓ Yes |
| **Arm's length terms** | Unrelated parties, negotiated terms | ✓ Yes |
| **Lease term** | 12 years (60% of 20-year useful life) | ✓ Yes (not substantially all) |
| **Business purpose** | Genuine liquidity need (cash for drilling capex) | ✓ Yes |

**Conclusion**: The transaction **qualifies as a true sale** for tax purposes:

- Clear transfer of legal title and substantial risks
- Repurchase option at FMV (not a financing disguise)
- Lease term (60%) does not cover substantially all useful life
- Genuine business purpose (TropicOil needs capital for drilling program)

**Step 2: Immediate Tax Impact**

**Gain Calculation**:

```
Sale price = $180,000,000
Less: Adjusted basis = $60,000,000
Total gain = $120,000,000
```

**Section 1245 Recapture Analysis**:

Processing facility is **Section 1245 property** (depreciable tangible personal property). Accumulated depreciation is **recaptured as ordinary income**:

```
Section 1245 recapture (ordinary income) = MIN(Accumulated depreciation, Gain)
= MIN($140M, $120M) = $120,000,000

All $120M gain is ordinary income (recapture)
Capital gain = $0
```

**Tax on Gain**:

```
Ordinary income = $120,000,000
Tax at 21% = $25,200,000
```

**After-Tax Cash Flow (Year 0)**:

```
Sale proceeds = $180,000,000
Less: Tax on gain = $25,200,000
Net cash = $154,800,000
```

**Step 3: Annual Tax Benefit - Leaseback vs. Retained Ownership**

**Scenario A: Sale and Leaseback**

```
Annual lease payment = $22,000,000 (fully deductible)
Tax benefit = $22,000,000 × 21% = $4,620,000 per year
```

**Scenario B: Retained Ownership**

If TropicOil had **retained ownership**:

```
Remaining depreciable basis = $60,000,000
Remaining useful life = 20 years
Annual depreciation = $60,000,000 / 20 = $3,000,000 (straight-line)
Tax benefit = $3,000,000 × 21% = $630,000 per year
```

**Incremental Annual Tax Benefit from Leaseback**:

```
Leaseback tax benefit = $4,620,000
Retained ownership tax benefit = $630,000
Incremental benefit = $3,990,000 per year (for 12 years)
```

**Step 4: Net Present Value Analysis**

**Initial Tax Cost**:

```
PV of tax on gain (Year 0) = $25,200,000
```

**Present Value of Incremental Tax Benefits**:

```
Annual benefit = $3,990,000
Lease term = 12 years
Discount rate = 8%
PV factor (annuity, 12 years, 8%) = 7.536

PV of incremental tax benefits = $3,990,000 × 7.536 = $30,069,000
```

**Net Tax Benefit (NPV)**:

```
PV of incremental tax benefits = $30,069,000
Less: PV of tax on gain = $25,200,000
Net NPV of tax benefits = $4,869,000
```

**Plus Cash Flow Benefit**:

The $154.8 million net cash received in Year 0 can be **reinvested** in drilling projects with expected returns exceeding the 8% discount rate, generating additional value.

**Conclusion**: The sale and leaseback is **economically advantageous** from a tax perspective:

- **Net tax NPV**: +$4.87 million
- **Immediate liquidity**: $154.8 million to fund drilling program
- **Continued operational control**: Through leaseback

### Recommendation

**Proceed with sale and leaseback** because:

1. **Qualifies as true sale**: Clear transfer of ownership and risks
2. **Positive tax NPV**: $4.87 million net benefit
3. **Liquidity benefit**: $154.8 million immediate cash for drilling capex
4. **Operational continuity**: 12-year leaseback ensures uninterrupted operations
5. **Flexibility**: Purchase option at FMV allows reacquisition if economically attractive

**Risk Considerations**:

- **Lease payment escalation**: If lease payments increase significantly in future years, may become burdensome
- **Market value risk**: If facility value declines, TropicOil may not exercise repurchase option, losing long-term asset appreciation
- **Refinancing risk**: At lease end (year 12), TropicOil must either repurchase or relocate operations

**Alternative**: If TropicOil expects **significant facility value appreciation** over 12 years and wants to retain that upside, **debt financing** (mortgage loan) may be preferable to sale-leaseback, despite slightly higher annual cost.

