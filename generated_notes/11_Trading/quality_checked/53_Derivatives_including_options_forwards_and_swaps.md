# 53. Derivatives - Including Options, Forwards, and Swaps

## 1. Introduction

**Derivatives** are financial instruments whose value derives from an underlying asset, index, or reference rate. In the oil and gas sector, derivatives serve two primary functions: **hedging** (reducing price, currency, or interest rate risk) and **trading** (speculating on price movements for profit). The most common derivatives used by energy companies are **options** (call and put), **forwards and futures**, and **swaps** (plain vanilla, credit default, total return).

The tax treatment of derivatives varies significantly across jurisdictions, with key issues including:
- **Timing**: Whether gains/losses are recognized on **accrual basis** (mark-to-market) or **realization basis** (upon settlement)
- **Character**: Whether gains/losses are **ordinary income/expense** or **capital gains/losses**
- **Hedging**: Whether **hedge accounting** is available to match derivative gains/losses with hedged item
- **Withholding tax**: Whether payments under swaps (particularly cross-border) trigger withholding tax

Oil and gas companies use derivatives for four primary purposes: (1) **price risk hedging** to lock in commodity sale prices or purchase costs, (2) **currency risk management** to eliminate foreign exchange exposure on USD-denominated transactions, (3) **interest rate hedging** to convert floating-rate debt to fixed rates, and (4) **credit risk mitigation** through credit default swaps protecting against counterparty default.

---

## 2. Options

### 2.1 Definition and Types

An **option** is a contract granting the holder the **right (but not obligation)** to buy or sell a specified quantity of a commodity at a predetermined price (the **strike price**) on or before a specified date (the **expiration date**).

**A. Call Options**

A **call option** grants the holder the right to **purchase** the underlying commodity at the strike price.

**Example:**
- EnergyTrade Ltd. purchases a **call option** on 100,000 barrels of Brent crude
- **Strike price**: $80/barrel
- **Expiration date**: December 31, 2025
- **Premium paid**: $2/barrel ($200,000 total)

**Scenarios:**
1. **Price rises to $90/barrel**: EnergyTrade exercises the option, purchasing at $80 and selling at $90, generating $10/barrel profit (minus $2 premium = **$8/barrel net profit** = **$800,000 total**)
2. **Price falls to $70/barrel**: EnergyTrade does not exercise (worthless); **loss = $2/barrel premium** = **$200,000 total**

**B. Put Options**

A **put option** grants the holder the right to **sell** the underlying commodity at the strike price.

**Example:**
- Producer Inc. purchases a **put option** on 200,000 barrels of WTI crude
- **Strike price**: $75/barrel
- **Expiration date**: June 30, 2026
- **Premium paid**: $3/barrel ($600,000 total)

**Scenarios:**
1. **Price falls to $65/barrel**: Producer Inc. exercises, selling at $75 (via option) instead of $65 (market), generating $10/barrel benefit (minus $3 premium = **$7/barrel net profit** = **$1.4 million total**)
2. **Price rises to $85/barrel**: Producer Inc. does not exercise (sells at market $85); **loss = $3/barrel premium** = **$600,000 total**

### 2.2 Tax Treatment of Options

**A. Premium Payment (Buyer's Perspective)**

The tax treatment of the **option premium** paid by the buyer varies:

| **Jurisdiction** | **Tax Treatment** |
|---|---|
| **United States (Internal Revenue Code (IRC) Section 1234)** | • Premium capitalized (not immediately deductible) <br>• If option exercised: Premium added to cost basis of commodity purchased (call) or reduces proceeds of commodity sold (put) <br>• If option lapses: Premium recognized as capital loss or ordinary loss (if hedging) |
| **United Kingdom (Corporation Tax Act (CTA) 2009, Part 7)** | • Derivative contracts taxed on **mark-to-market basis** (fair value accounting per International Financial Reporting Standards (IFRS) 9) <br>• Premium recognized over option life (accrual basis) <br>• Gains/losses treated as ordinary income/expense (not capital) |
| **Singapore** | • Premium treated as **capital expenditure** if hedging <br>• If trading: Premium recognized as expense (deductible) when incurred <br>• Gains/losses on settlement: Ordinary income/expense |
| **Switzerland** | • Premium capitalized and amortized over option life <br>• Gains/losses on exercise: Ordinary income/expense <br>• If option lapses: Loss deductible in year of lapse |

**B. Premium Receipt (Seller's Perspective)**

The **option writer** (seller) receives the premium:

- **United States**: Premium is income when **option lapses** or **obligation discharged** (not when received)
- **United Kingdom**: Premium recognized on **accrual basis** (mark-to-market)
- **Singapore/Switzerland**: Premium is income when received (cash basis) or over option life (accrual basis, depending on accounting method)

**C. Hedging vs. Trading Options**

Many jurisdictions provide **hedge accounting** treatment, allowing:
- Deferral of derivative gains/losses to match recognition of hedged item
- Treatment as ordinary income/expense (not capital)

**Hedging requirements** (typically):
1. **Identified hedged item**: Specific commodity inventory, future production, or purchase commitment
2. **Documented hedge relationship**: Contemporaneous documentation linking derivative to hedged item
3. **Effectiveness test**: Derivative must be "highly effective" in offsetting hedged item's risk (80-125% correlation)

---

## 3. Forwards and Futures

### 3.1 Definition and Mechanics

**A. Forward Contracts**

A **forward contract** is a binding agreement to buy or sell a specified quantity of a commodity at a predetermined price on a specified future date.

**Key characteristics:**
- **Customized**: Terms (quantity, price, date, delivery location) negotiated bilaterally
- **Over-the-counter (OTC)**: Not exchange-traded
- **Counterparty risk**: Risk of default by either party
- **Settlement**: Physical delivery or cash settlement at maturity

**Example:**
- Refinery Co. enters a **forward contract** to purchase 500,000 barrels of Brent crude
- **Forward price**: $78/barrel
- **Delivery date**: March 15, 2026
- **Obligation**: Refinery Co. **must** purchase at $78/barrel (no optionality)

**B. Futures Contracts**

A **futures contract** is a standardized forward contract traded on an exchange (e.g., **Intercontinental Exchange (ICE) Brent Crude Futures**, **New York Mercantile Exchange (NYMEX) WTI Futures**).

**Key characteristics:**
- **Standardized**: Contract size (typically 1,000 barrels), delivery dates, and terms set by exchange
- **Exchange-traded**: Liquid secondary market; can be sold before maturity
- **Mark-to-market**: Daily settlement of gains/losses through **margin accounts**
- **Clearinghouse**: Exchange clearinghouse guarantees performance (eliminates counterparty risk)

**Example:**
- Trader buys **10 NYMEX WTI futures contracts** (10,000 barrels total)
- **Futures price**: $80/barrel
- **Contract month**: December 2025
- **Daily mark-to-market**: If price rises to $82, trader's margin account credited $2 × 10,000 = **$20,000**; if price falls to $78, account debited **$20,000**

### 3.2 Tax Treatment of Forwards and Futures

**A. Timing: Accrual vs. Realization**

The **critical tax issue** is whether gains/losses are recognized:
- **Accrual basis** (mark-to-market): Gains/losses recognized as they accrue, even before settlement
- **Realization basis**: Gains/losses recognized only upon settlement or termination

| **Jurisdiction** | **Tax Treatment** |
|---|---|
| **United States (IRC Section 1256)** | • **Section 1256 contracts** (exchange-traded futures, certain options): **Mark-to-market** at year-end <br>• Gains/losses treated as **60% long-term capital gain**, **40% short-term capital gain** ("60/40 rule") <br>• **Forward contracts** (non-Section 1256): Realization basis (gain/loss upon settlement) <br>• **Hedging exception**: IRC Section 1221(a)(7) treats hedging transactions as ordinary income/expense |
| **United Kingdom (CTA 2009, Part 7)** | • All derivative contracts taxed on **mark-to-market basis** (fair value accounting) <br>• Gains/losses: Ordinary income/expense (not capital) <br>• Aligns with **IFRS 9** financial instrument accounting |
| **Singapore** | • **Trading derivatives**: Mark-to-market (accrual basis) <br>• **Hedging derivatives**: May elect realization basis (match with hedged item) <br>• Gains/losses: Ordinary income/expense |
| **Switzerland** | • **Trading derivatives**: Mark-to-market (accrual basis) <br>• **Hedging derivatives**: Realization basis (match with hedged item) <br>• Gains/losses: Ordinary income/expense |

**B. Delivery vs. Cash Settlement**

- **Physical delivery**: Gain/loss recognized as part of commodity's cost basis or sales proceeds
- **Cash settlement**: Gain/loss recognized separately as derivative income/expense

**Example (U.S. hedging treatment):**

Producer Inc. (U.S. company) hedges future production with WTI futures:

```
Date: January 1, 2025
• Sell 100,000 barrels WTI futures at $80/barrel (expecting to produce and deliver in December 2025)

Date: December 31, 2025
• Futures price: $70/barrel
• Gain on futures: ($80 - $70) × 100,000 = $1 million
• Physical production sold at spot market: $70/barrel = $7 million
• Net proceeds: $7M + $1M futures gain = $8 million (equivalent to $80/barrel, the hedged price)

Tax treatment (hedging election under IRC Section 1221(a)(7)):
• Futures gain ($1M): Ordinary income (not capital)
• Production sale ($7M): Ordinary income
• Total ordinary income: $8 million
```

Without hedging election:
- Futures gain would be subject to 60/40 capital gain treatment (Section 1256)
- Production sale: Ordinary income
- Mismatched tax character (capital vs. ordinary)

---

## 4. Swaps

### 4.1 Plain Vanilla Swaps

**A. Definition**

A **plain vanilla swap** is an agreement to exchange cash flows between two parties based on a **notional principal amount**. In oil and gas, common swaps include:

1. **Commodity price swaps**: Exchange fixed price for floating price (based on benchmark like Brent, WTI)
2. **Interest rate swaps**: Exchange fixed interest rate for floating rate (e.g., Secured Overnight Financing Rate (SOFR), successor to London Interbank Offered Rate (LIBOR) discontinued in 2021)
3. **Currency swaps**: Exchange cash flows in different currencies (e.g., USD to EUR)

**B. Commodity Price Swap Example**

**Facts:**
- Producer Co. expects to produce 1 million barrels of crude oil in 2026
- Current spot price: $75/barrel (volatile)
- Producer Co. wants **price certainty** to secure financing

**Swap structure:**
- **Counterparty**: Investment Bank
- **Notional amount**: 1 million barrels
- **Fixed price** (received by Producer Co.): $75/barrel
- **Floating price** (paid by Producer Co.): Monthly average Brent crude price
- **Term**: 12 months (2026)

**Settlement mechanics (monthly cash settlement, no physical delivery):**

| **Month** | **Brent Average Price** | **Fixed Receipt** | **Floating Payment** | **Net Cash Flow to Producer Co.** |
|---|---|---|---|---|
| **January** | $70/barrel | +$75 | -$70 | +$5/barrel |
| **February** | $80/barrel | +$75 | -$80 | -$5/barrel |
| **March** | $72/barrel | +$75 | -$72 | +$3/barrel |

**Economic effect:**
- Producer Co. sells physical production at **spot market price** (e.g., $70, $80, $72)
- Swap **offsets** price volatility: Receives fixed $75, pays floating (spot)
- **Net realized price**: Always $75/barrel (spot ± swap settlement)

**C. Interest Rate Swap Example**

**Facts:**
- Oil & Gas Corp. has **$500 million floating-rate debt** (SOFR + 2%)
- Current SOFR: 4.5%, thus current interest rate: 6.5%
- Concerned about rising rates

**Swap structure:**
- **Notional amount**: $500 million
- **Fixed rate** (paid by Oil & Gas Corp.): 6.0%
- **Floating rate** (received by Oil & Gas Corp.): SOFR + 2%
- **Term**: 5 years

**Economic effect:**
- Oil & Gas Corp. pays **floating rate** (SOFR + 2%) on actual debt
- Receives **floating rate** (SOFR + 2%) from swap, pays **fixed 6.0%**
- **Net interest cost**: Fixed 6.0% (eliminates rate risk)

**D. Currency Swap Example**

**Facts:**
- European refinery (EUR functional currency) purchases crude oil (priced in USD)
- Annual purchases: $1 billion
- Exchange rate risk: EUR/USD volatility

**Swap structure:**
- **Notional amount**: $1 billion
- Refinery pays **EUR** (fixed or floating), receives **USD** (fixed or floating)
- Typically structured as **fixed-for-fixed** or **floating-for-floating**

**Economic effect:**
- Locks in EUR/USD exchange rate, eliminating currency risk
- Refinery knows exact EUR cost of USD-denominated crude purchases

### 4.2 Credit Default Swaps (CDS)

**A. Definition**

A **credit default swap (CDS)** is a contract providing **insurance** against default on a loan or bond. The **protection buyer** pays periodic premiums; the **protection seller** compensates the buyer if the reference entity (borrower) defaults.

**B. Application in Oil & Gas**

**Scenario:**
- Bank lends $200 million to Oil Producer Inc.
- Bank concerned about credit risk (oil price volatility, production decline)

**CDS structure:**
- **Protection buyer**: Bank
- **Protection seller**: Insurance company or investment bank
- **Reference entity**: Oil Producer Inc.
- **Notional amount**: $200 million
- **Premium**: 200 basis points (2%) annually = $4 million/year
- **Term**: 5 years

**Outcomes:**
1. **No default**: Bank pays $4M annually for 5 years; no compensation received (total cost: $20M)
2. **Default (e.g., Year 3)**: Protection seller pays $200M (or recovery value less principal); Bank made whole

**C. Tax Treatment**

| **Jurisdiction** | **Tax Treatment** |
|---|---|
| **United States** | • Premium payments: Deductible as ordinary expense (insurance-like) <br>• Compensation received upon default: Ordinary income <br>• May not qualify as "interest" for withholding tax purposes |
| **United Kingdom** | • Treated as derivative contract (CTA 2009, Part 7) <br>• Mark-to-market accounting <br>• Gains/losses: Ordinary income/expense |
| **Cross-border withholding tax** | • If protection seller is non-resident: Premium payments may trigger WHT (10-30%) <br>• Treaty relief: Typically, premiums **not** characterized as interest or royalties (thus business profits, requiring permanent establishment (PE) for taxation) |

### 4.3 Total Return Swaps (TRS)

**A. Definition**

A **total return swap (TRS)** allows the **TRS receiver** to obtain the **economic return** (income and capital appreciation) of an asset without owning it. The TRS receiver pays a **financing cost** (typically SOFR + spread) to the **TRS payer**.

**B. Application in Oil & Gas**

**Scenario:**
- Investment fund wants exposure to shares of **Big Oil plc** but:
  - Faces regulatory restrictions on direct ownership
  - Wants leverage (magnify returns without full capital outlay)

**TRS structure:**
- **TRS receiver**: Investment fund
- **TRS payer**: Investment bank (which owns Big Oil shares)
- **Notional amount**: $100 million (equivalent to 10 million shares at $10/share)
- **TRS receiver receives**:
  - Dividends on notional shares
  - Capital appreciation (if share price rises)
- **TRS receiver pays**:
  - Capital depreciation (if share price falls)
  - Financing cost (SOFR + 2%)
- **Term**: 2 years

**Example cash flows (Year 1):**

Assumptions:
- Big Oil share price: $10 (start) → $12 (end) = **20% appreciation**
- Dividends: $0.50/share = $5 million on notional 10M shares
- SOFR: 4.5%, financing cost: 4.5% + 2% = 6.5% on $100M = $6.5 million

```
TRS receiver receives:
  Dividends:                                    +$5.0 million
  Capital appreciation: ($12 - $10) × 10M:     +$20.0 million
  Total:                                        +$25.0 million

TRS receiver pays:
  Financing cost (6.5% on $100M):              -$6.5 million

Net to TRS receiver:                            +$18.5 million
Return on $0 capital outlay:                    Infinite (leveraged exposure)
```

**C. Tax Treatment**

| **Jurisdiction** | **Tax Treatment** |
|---|---|
| **United States** | • **IRC Section 1234A**: Capital gain/loss treatment (unless dealer or trader) <br>• Dividends received via TRS: May not qualify for dividends received deduction (DRD) <br>• Payments to non-resident TRS payer: May trigger WHT (not always characterized as interest) |
| **United Kingdom** | • Treated as derivative contract (CTA 2009, Part 7) <br>• Mark-to-market accounting <br>• Gains/losses: Ordinary income/expense |
| **Singapore / Switzerland** | • Payments to non-resident: **Withholding tax risk** (10-30%) if characterized as interest or deemed interest <br>• May not qualify as interest under treaties (requires case-by-case analysis) |

---

## 5. Tax Planning Considerations

### 5.1 Hedging Documentation

To obtain **favorable hedge accounting treatment** (matching derivative gains/losses with hedged item), companies must:

1. **Contemporaneous documentation** (at inception):
   - Identify specific hedged item (production, inventory, debt)
   - Document hedge objective and strategy
   - Describe risk being hedged (price, interest rate, currency)

2. **Effectiveness testing** (periodic):
   - Demonstrate high correlation (80-125%) between derivative and hedged item
   - If hedge becomes ineffective: Loses hedge accounting (immediate gain/loss recognition)

3. **Example**:

```
Hedge Documentation - January 1, 2025

Hedged Item: 500,000 barrels of WTI crude oil expected to be produced in Q4 2025

Derivative: 500,000 barrels WTI put options (strike $75/barrel, expiration Dec 2025)

Risk Being Hedged: Decline in WTI prices below $75/barrel

Hedge Effectiveness Test: Monthly comparison of option intrinsic value vs. spot price movement
```

### 5.2 Cross-Border Withholding Tax Planning

**Issue**: Swap and derivative payments between **related parties** across borders may trigger withholding tax.

| **Payment Type** | **WHT Risk** | **Treaty Relief** | **Planning Strategy** |
|---|---|---|---|
| **Interest rate swap** (fixed-for-floating) | **High** (may be characterized as interest) | 0-15% treaty rate | • Use back-to-back swaps through low-WHT jurisdiction <br>• Central treasury company as swap counterparty |
| **Commodity price swap** | **Low** (typically business profits, not interest) | Requires PE for taxation | • Generally no WHT if no PE |
| **Credit default swap premium** | **Moderate** (uncertain characterization) | Case-by-case | • Treaty analysis (business profits vs. interest vs. insurance premium) |
| **Total return swap** | **Moderate to High** (financing cost may be interest) | 0-15% treaty rate | • Structure as loan + equity return (separate components) |

**Best practice**: Obtain **advance ruling** from tax authority on characterization (interest, royalty, business profits) to avoid surprise WHT assessments.

---

## 6. Worked Example

═══════════════════════════════════════════
**WORKED EXAMPLE: Tax Treatment of Crude Oil Price Hedging with Options and Swaps**
═══════════════════════════════════════════

**Facts:**

NorthSea Energy Ltd. (UK tax resident) produces crude oil from UK Continental Shelf. For 2025, the company expects to produce **2 million barrels** of Brent crude. Current Brent price: **$75/barrel** (volatile).

The CFO proposes two hedging strategies to secure minimum realized price of **$70/barrel**:

**Strategy 1: Put Options**
- Purchase **put options** on 2 million barrels
- **Strike price**: $70/barrel
- **Expiration**: December 31, 2025
- **Premium**: $3/barrel = **$6 million** total

**Strategy 2: Commodity Price Swap**
- Enter **fixed-for-floating swap** on 2 million barrels
- **Fixed price** (received): $72/barrel
- **Floating price** (paid): Monthly average Brent price
- **Term**: 12 months (2025)
- **No upfront premium**

**Assume actual 2025 average Brent price**: **$65/barrel** (decline from current $75)

**Required:**

1. Calculate realized price and cash flows under each strategy
2. Analyze UK tax treatment under **Corporation Tax Act (CTA) 2009, Part 7** (derivative contracts on mark-to-market basis)
3. Compare after-tax economics (assume UK corporate tax rate: **25%**)

**Analysis:**

**STRATEGY 1: PUT OPTIONS**

**Step 1: Calculate Cash Flows**

**At inception (January 1, 2025):**
```
Premium paid:                                   -$6 million
```

**At expiration (December 31, 2025):**

Actual average Brent price: $65/barrel (below $70 strike)
- **Options are in-the-money**: Exercise put options

```
Physical production sale (spot market):         2M barrels × $65 = $130 million
Option payoff:                                  2M barrels × ($70 - $65) = $10 million
Gross realized price:                           $130M + $10M = $140 million
Equivalent per-barrel price:                    $140M ÷ 2M = $70/barrel ✓
```

**Net cash flow (after premium):**
```
Gross realized:                                 $140 million
Less: Premium paid (Jan 1):                     -$6 million
Net cash:                                       $134 million
Net per-barrel price:                           $134M ÷ 2M = $67/barrel
```

**Step 2: UK Tax Treatment (CTA 2009, Part 7)**

**Mark-to-Market Accounting (Fair Value):**

**Year-end 2025:**
- **Premium paid (Jan 1)**: $6M capitalized
- **Fair value at year-end**: Options exercised, $10M payoff received
- **Net derivative gain**: $10M payoff - $6M premium = **$4 million gain**

**Tax recognition:**
```
Production revenue (ordinary income):           $130 million
Derivative gain (ordinary income):              $4 million
Total taxable income:                           $134 million
UK corporation tax (25%):                       $33.5 million
After-tax cash:                                 $134M - $33.5M = $100.5 million
```

**Effective after-tax realized price**: $100.5M ÷ 2M = **$50.25/barrel**

**Step 3: Alternative Scenario (Brent Rises to $80/barrel)**

If Brent rises to $80/barrel (above $70 strike):
- **Options are out-of-the-money**: Do not exercise (lapse worthless)

```
Physical production sale:                       2M × $80 = $160 million
Option payoff:                                  $0
Gross realized:                                 $160 million
Less: Premium paid:                             -$6 million
Net cash:                                       $154 million
Net per-barrel price:                           $154M ÷ 2M = $77/barrel
```

**UK tax treatment:**
```
Production revenue:                             $160 million
Derivative loss (premium):                      -$6 million
Taxable income:                                 $154 million
UK corporation tax (25%):                       $38.5 million
After-tax cash:                                 $154M - $38.5M = $115.5 million
```

**Effective after-tax realized price**: $115.5M ÷ 2M = **$57.75/barrel**

---

**STRATEGY 2: COMMODITY PRICE SWAP**

**Step 1: Calculate Cash Flows**

**No upfront payment** (swaps typically have zero initial value)

**Monthly settlements (2025):**

Assume actual average Brent: **$65/barrel**

```
Physical production sale (spot market):         2M × $65 = $130 million

Swap cash flows (net monthly settlements):
  Fixed received:                               2M × $72 = $144 million
  Floating paid:                                2M × $65 = $130 million
  Net swap receipt:                             $144M - $130M = $14 million

Total cash:                                     $130M + $14M = $144 million
Equivalent per-barrel price:                    $144M ÷ 2M = $72/barrel ✓
```

**Net realized price**: **$72/barrel** (locked in via swap, regardless of spot price)

**Step 2: UK Tax Treatment (CTA 2009, Part 7)**

**Mark-to-Market Accounting:**

Throughout 2025, swap fair value fluctuates:
- **January**: Brent $75 (above fixed $72): Swap liability (negative fair value)
- **June**: Brent $70 (below fixed $72): Swap asset (positive fair value)
- **December**: Brent $65 (below fixed $72): Swap asset $14M (final settlement)

**Year-end 2025 tax recognition:**
```
Production revenue (ordinary income):           $130 million
Derivative gain (net swap receipt):             $14 million
Total taxable income:                           $144 million
UK corporation tax (25%):                       $36 million
After-tax cash:                                 $144M - $36M = $108 million
```

**Effective after-tax realized price**: $108M ÷ 2M = **$54/barrel**

**Step 3: Alternative Scenario (Brent Rises to $80/barrel)**

If Brent rises to $80/barrel (above fixed $72):

```
Physical production sale:                       2M × $80 = $160 million

Swap cash flows:
  Fixed received:                               2M × $72 = $144 million
  Floating paid:                                2M × $80 = $160 million
  Net swap payment:                             $144M - $160M = -$16 million (loss)

Total cash:                                     $160M - $16M = $144 million
Realized per-barrel price:                      $144M ÷ 2M = $72/barrel ✓
```

**UK tax treatment:**
```
Production revenue:                             $160 million
Derivative loss (net swap payment):             -$16 million
Taxable income:                                 $144 million
UK corporation tax (25%):                       $36 million
After-tax cash:                                 $144M - $36M = $108 million
```

**Effective after-tax realized price**: $108M ÷ 2M = **$54/barrel**

---

**COMPARISON: STRATEGY 1 (PUT OPTIONS) VS. STRATEGY 2 (SWAP)**

| **Metric** | **Put Options** | **Commodity Swap** |
|---|---|---|
| **Upfront cost** | $6 million premium | $0 |
| **Realized price (Brent $65)** | $70/barrel gross ($67/barrel net of premium) | $72/barrel |
| **After-tax cash (Brent $65)** | $100.5M ($50.25/barrel) | $108M ($54/barrel) |
| **Realized price (Brent $80)** | $80/barrel gross ($77/barrel net of premium) | $72/barrel (locked) |
| **After-tax cash (Brent $80)** | $115.5M ($57.75/barrel) | $108M ($54/barrel) |
| **Upside participation** | **Yes** (benefit if prices rise above strike) | **No** (locked at $72, no upside) |
| **Downside protection** | **Yes** (floor at $70, net $67) | **Yes** (locked at $72) |
| **Cash flow certainty** | **Lower** (depends on Brent; premium paid upfront) | **Higher** (locked at $72; no upfront cost) |

**Decision Framework:**

**Choose Put Options if:**
- Company wants **upside participation** (benefit from price increases above strike)
- Willing to pay **upfront premium** ($6M)
- Comfortable with **price uncertainty** (but protected from extreme declines)

**Choose Commodity Swap if:**
- Company wants **complete price certainty** ($72/barrel locked in)
- Prefers **no upfront cost** (zero initial value)
- Does **not** need upside participation (willing to forgo gains if prices rise)

**Recommendation for NorthSea Energy:**

Given the **decline scenario** (Brent $65), the **commodity swap** provides **$7.5M higher after-tax cash** ($108M vs. $100.5M) due to:
1. **Higher realized price**: $72/barrel (swap) vs. $70/barrel gross / $67/barrel net (put options)
2. **No upfront premium**: Swap has zero cost; put options require $6M upfront

However, if Brent rises to $80, **put options provide $7.5M higher after-tax cash** ($115.5M vs. $108M) because NorthSea retains upside.

**Conclusion**: If NorthSea's priority is **cash flow certainty** and **no upfront cost**, choose the **swap**. If NorthSea wants **downside protection** while retaining **upside potential**, choose **put options**.

**Tax Planning Note**:
Under UK CTA 2009, Part 7, both strategies benefit from **mark-to-market accounting** aligning derivative gains/losses with production revenue in the same tax year (ordinary income treatment). No special hedge accounting election is required; the statutory regime automatically matches derivative and hedged item.

═══════════════════════════════════════════

---
