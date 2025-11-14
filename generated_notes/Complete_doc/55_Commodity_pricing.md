# 55. Commodity Pricing

## 1. Introduction

**Commodity pricing** is the cornerstone of transfer pricing in the oil and gas sector. Crude oil, natural gas, LNG, and refined products are traded globally with prices determined by **supply and demand dynamics**, **quality specifications**, **geographic location**, and **contract terms**. Unlike manufactured goods where cost-based methods may be appropriate, commodities have **actively traded markets** with **published benchmark prices**, making the **Comparable Uncontrolled Price (CUP) method** the most appropriate transfer pricing approach.

The OECD Transfer Pricing Guidelines explicitly recognize the unique characteristics of commodity transactions: **"The comparable uncontrolled price method would generally be the most appropriate transfer pricing method for establishing the arm's length price for commodity transfers between associated enterprises"** [OECD Guidelines 2022, Chapter II, Section C].

This chapter examines **benchmark pricing mechanisms** (Brent, WTI, Dubai, Henry Hub, JKM), **quality and location adjustments**, **pricing date selection**, **contract terms**, **quotational period**, and **tax authority challenges** specific to commodity transfer pricing.

---

## 2. Commodity Benchmarks

### 2.1 Crude Oil Benchmarks

**A. Brent Crude**

**Geographic coverage**: North Sea (UK and Norway)

**Specifications**:
- **API gravity**: 38° (light crude)
- **Sulfur content**: 0.37% (sweet crude)
- **Delivery point**: Sullom Voe (Scotland) or equivalent North Sea loading terminals

**Trading platforms**:
- **ICE Brent Crude Futures**: Intercontinental Exchange (ICE)
- **Platts Brent**: Published by S&P Global Platts (Dated Brent assessment)

**Global significance**: Brent is the **primary benchmark** for Atlantic Basin crude (Europe, Africa, Middle East exports to Europe). Approximately **2/3 of global crude oil** is priced relative to Brent.

**B. West Texas Intermediate (WTI)**

**Geographic coverage**: United States (Permian Basin, Midland, Cushing hub)

**Specifications**:
- **API gravity**: 39.6° (light crude)
- **Sulfur content**: 0.24% (sweet crude)
- **Delivery point**: Cushing, Oklahoma (landlocked)

**Trading platforms**:
- **NYMEX WTI Futures**: New York Mercantile Exchange (CME Group)
- **Platts WTI**: Published assessment

**Regional significance**: WTI is the primary benchmark for **U.S. domestic crude**. However, due to landlocked delivery point (Cushing), WTI can trade at discount to Brent during periods of U.S. inventory builds.

**C. Dubai/Oman (Fateh)**

**Geographic coverage**: Middle East

**Specifications**:
- **API gravity**: 31° (medium crude)
- **Sulfur content**: 2.0% (sour crude)

**Trading platforms**:
- **DME Oman Futures**: Dubai Mercantile Exchange
- **Platts Dubai**: Published assessment (Dubai/Oman average)

**Regional significance**: Primary benchmark for **Middle East crude exports to Asia**. Singapore traders use Dubai as pricing basis for spot transactions.

### 2.2 Natural Gas Benchmarks

**A. Henry Hub (U.S.)**

**Delivery point**: Henry Hub, Louisiana (major pipeline interconnection)

**Trading platform**: **NYMEX Henry Hub Natural Gas Futures** (CME Group)

**Pricing unit**: USD per million British thermal units (MMBtu)

**Significance**: Primary benchmark for **U.S. natural gas**; increasingly referenced globally due to U.S. LNG exports.

**B. National Balancing Point (NBP, UK)**

**Delivery point**: Virtual trading point in UK gas transmission system

**Trading platform**: **ICE UK Natural Gas Futures**

**Pricing unit**: GBP per therm (or pence/therm)

**Significance**: European gas benchmark (though TTF now more liquid).

**C. Title Transfer Facility (TTF, Netherlands)**

**Delivery point**: Virtual trading point at Dutch-German border

**Trading platform**: **ICE TTF Natural Gas Futures**

**Pricing unit**: EUR per megawatt-hour (MWh)

**Significance**: **Most liquid European gas benchmark** (has surpassed NBP).

**D. Japan-Korea Marker (JKM)**

**Geographic coverage**: Northeast Asia LNG imports

**Trading platform**: **S&P Global Platts JKM** (assessment-based, not futures)

**Pricing unit**: USD per MMBtu

**Significance**: Benchmark for **Asian spot LNG** prices.

### 2.3 Refined Products Benchmarks

| **Product** | **Benchmark** | **Trading Hub** | **Price Reporter** |
|---|---|---|---|
| **Gasoline** | RBOB (Reformulated Blendstock for Oxygenate Blending) | New York Harbor | NYMEX / Platts |
| **Diesel / Gasoil** | ULSD (Ultra-Low Sulfur Diesel) | New York Harbor, Singapore | NYMEX / Platts |
| **Jet Fuel** | Jet Kerosene | Singapore, Rotterdam, U.S. Gulf Coast | Platts |
| **Fuel Oil** | 380 CST / VLSFO | Singapore | Platts |

---

## 3. Quality Adjustments

### 3.1 API Gravity Adjustment

**API gravity** measures crude oil density (lighter crude has higher API gravity; heavier crude has lower API gravity).

**General principle**: **Lighter crude commands premium** (easier to refine into valuable products like gasoline and diesel).

**Typical adjustment**: **+/- $0.30 to $0.50 per barrel per API degree** difference from benchmark.

**Example**:

```
Benchmark: Brent (API 38°) = $80/barrel
Produced crude: API 35° (3° heavier than Brent)

Quality adjustment: -3° × $0.40/degree = -$1.20/barrel
Adjusted price: $80 - $1.20 = $78.80/barrel
```

**Data source**: Platts publishes API differentials for various crude grades in **Crude Oil Marketwire**.

### 3.2 Sulfur Content Adjustment

**Sulfur content** affects refining costs (high-sulfur "sour" crude requires more expensive processing to meet environmental standards).

**General principle**: **Low-sulfur (sweet) crude commands premium**.

**Typical adjustment**: **-$1.00 to $2.00 per barrel per 0.5% sulfur** above benchmark.

**Example**:

```
Benchmark: Brent (sulfur 0.37%) = $80/barrel
Produced crude: Sulfur 1.5% (1.13% higher than Brent)

Quality adjustment: -(1.13% ÷ 0.5%) × $1.50 = -$3.39/barrel
Adjusted price: $80 - $3.39 = $76.61/barrel
```

**Data source**: Platts, Argus Media publish sulfur differentials.

### 3.3 Combined Quality Adjustment

**Example**: Nigerian Bonny Light vs. Brent

Nigerian **Bonny Light** crude:
- API: 35.4° (2.6° lighter than Brent 38°)
- Sulfur: 0.14% (0.23% lower than Brent 0.37%)

```
Base price: Brent = $80/barrel

API adjustment: +2.6° × $0.40 = +$1.04/barrel (premium for lighter)
Sulfur adjustment: -(0.23% ÷ 0.5%) × $1.50 = +$0.69/barrel (premium for sweeter)

Combined adjustment: +$1.04 + $0.69 = +$1.73/barrel
Bonny Light price: $80 + $1.73 = $81.73/barrel
```

**Result**: Bonny Light trades at **premium to Brent** due to superior quality (lighter, sweeter).

---

## 4. Location (Freight) Adjustments

### 4.1 FOB vs. CIF Pricing

**FOB (Free On Board)**: Seller delivers crude to vessel at loading port; buyer bears freight, insurance, and risk during transportation.

**CIF (Cost, Insurance, Freight)**: Seller delivers crude to destination port; seller bears freight, insurance, and risk.

**Pricing differential**: CIF price = FOB price + Freight + Insurance

**Example**:

```
Nigerian crude (Bonny terminal) sold to European refinery (Rotterdam):

FOB Bonny price: $81.73/barrel (Brent + quality adjustments)
Freight (Bonny to Rotterdam): $2.50/barrel (Suezmax tanker, 1M barrels)
Insurance: $0.15/barrel
CIF Rotterdam price: $81.73 + $2.50 + $0.15 = $84.38/barrel
```

### 4.2 Freight Rate Determination

Freight rates vary based on:
- **Tanker class**: VLCC (Very Large Crude Carrier, 2M barrels), Suezmax (1M barrels), Aframax (750,000 barrels)
- **Route**: Short-haul (intra-regional) vs. long-haul (intercontinental)
- **Market conditions**: Charter rates fluctuate with supply/demand (published by **Baltic Exchange**)

**Data source**: **Worldscale** (tanker freight rate index), **Baltic Exchange** (dry bulk and tanker indices).

### 4.3 Pipeline Transportation

For **landlocked fields** or **domestic sales**, pipeline tariffs apply:

**Example**: U.S. Permian Basin crude to Gulf Coast refinery

```
Wellhead price (Midland): $75/barrel (WTI Midland)
Pipeline tariff (Midland to Houston): $3.50/barrel
Delivered price (Houston): $78.50/barrel
```

**Regulation**: U.S. pipeline tariffs are **FERC-regulated** (Federal Energy Regulatory Commission); tariffs publicly available.

---

## 5. Pricing Date (Quotational Period)

### 5.1 Importance of Pricing Date

Oil prices are **volatile** (daily fluctuations of 1-5% common). The **pricing date** determines which benchmark price applies to the transfer pricing calculation.

**Common approaches**:

1. **Date of lifting**: Price on the date crude is loaded onto vessel (Bill of Lading date)
2. **Date of delivery**: Price on the date crude is delivered to buyer
3. **Monthly average**: Average benchmark price for the month of delivery
4. **Quotational period**: Average of prices over specified period (e.g., 5-day quotational period before Bill of Lading)

### 5.2 Quotational Period Formula

**Example**: 5-day quotational period

```
Bill of Lading date: March 15, 2025
Quotational period: March 10-14, 2025 (5 days preceding)

Brent prices:
- March 10: $80.50
- March 11: $81.20
- March 12: $80.80
- March 13: $81.50
- March 14: $81.00

Average Brent (5-day QP): ($80.50 + $81.20 + $80.80 + $81.50 + $81.00) ÷ 5 = $81.00/barrel

Transfer price: $81.00 + quality adjustments + freight
```

**Rationale**: Quotational period **smooths volatility** and reflects prices during period when buyer/seller finalize commercial terms.

### 5.3 OECD Guidance on Pricing Date

OECD Guidelines state: **"A particularly relevant comparability factor for commodity transactions is the pricing date"** [Chapter II, para. 2.18].

**Key principle**: **Consistency required**:
- If **controlled transaction** uses monthly average pricing, **comparable uncontrolled transaction** must also use monthly average pricing for same period.
- If controlled transaction uses date of lifting, comparable must use date of lifting.

**Mismatch risk**: Using different pricing dates for controlled vs. comparable transactions can lead to adjustment (e.g., if controlled uses March average but comparable uses April average, and prices moved significantly, transfer price would not be arm's length).

---

## 6. Contract Terms

### 6.1 Term Contracts vs. Spot Contracts

**A. Term Contracts (Long-term supply agreements)**

**Characteristics**:
- **Duration**: 1-5 years (or longer)
- **Volume commitment**: Fixed or minimum volume (e.g., 100,000 bbl/month)
- **Pricing**: Formula-based (Brent + adjustments, monthly reset)
- **Take-or-pay**: Buyer obligated to pay for minimum volume even if not lifted

**Advantages**:
- **Certainty**: Secure supply/off-take for extended period
- **Relationship**: Deeper buyer-seller relationship

**Transfer pricing implication**: Term contracts may command **premium** (for security of supply) or **discount** (for volume commitment), typically **+/- $0.50-1.50/barrel**.

**B. Spot Contracts**

**Characteristics**:
- **Duration**: Single cargo (1-2 million barrels)
- **Volume**: No commitment beyond single transaction
- **Pricing**: Prevailing market price at time of transaction

**Advantages**:
- **Flexibility**: No long-term obligation
- **Market pricing**: Reflects current supply/demand

**Transfer pricing implication**: Spot transactions are most comparable to independent trades; term contract premiums/discounts must be documented if applied.

### 6.2 Volume Discounts

**Large-volume purchases** may qualify for discounts:

**Typical threshold**: 500,000+ barrels/month

**Discount**: $0.25-0.75/barrel

**Rationale**: Economies of scale (reduced per-unit marketing, administrative, and logistics costs for seller).

**Documentation requirement**: Evidence that independent buyers receive similar discounts for similar volumes (e.g., term sheets from third-party contracts, industry surveys).

---

## 7. Tax Authority Challenges

### 7.1 Common Challenge Areas

**A. "Six Method" Rule (Nigeria, Ghana, Kenya)**

Several **resource-rich countries** have introduced the **"Six Method"**, allowing tax authorities to:

1. **Disregard benchmark pricing** if deemed not to reflect local market conditions
2. **Apply alternative valuation**: Use government-determined prices or posted prices
3. **Impose minimum pricing**: Override intercompany pricing if below government threshold

**Example**: Nigeria's **"Sixth Method"** (Finance Act 2023)

> Petroleum Income Tax Act Section 22(1): *"Where the Commissioner considers that the market value of any commodity does not reflect the prevailing commercial realities, the Commissioner may determine the market value by reference to such method as the Commissioner considers appropriate, including the method prescribed by regulations."*

**Practical impact**: Even if producer uses Brent CUP with documented adjustments, Nigerian tax authority may substitute alternative price.

**Defense strategies**:
1. **Contemporaneous documentation**: Robust Local File demonstrating arm's length pricing using CUP
2. **Advance Pricing Agreement (APA)**: Bilateral APA with Nigeria to obtain pre-approval of methodology
3. **Third-party sales**: Evidence of sales to independent buyers at same price as related party sales (Internal CUP)

**B. Transfer Pricing Audits Focused on Adjustments**

Tax authorities may challenge:
- **Magnitude of quality adjustments**: Claiming sulfur/API adjustments are excessive
- **Freight rates**: Claiming freight charges to related party exceed market rates
- **Quotational period**: Claiming selected period is cherry-picked to achieve favorable pricing

**Defense strategies**:
1. **Third-party data**: Use Platts, Argus, or other recognized price reporters for adjustments
2. **Independent freight quotes**: Obtain quotes from unrelated shipping companies
3. **Consistent methodology**: Apply same quotational period methodology year-over-year

**C. Related Party Freight and Insurance**

If **shipping** or **insurance** provided by related party, transfer pricing scrutiny extends to these services:

**Example**:

```
Producer Co. (Nigeria) sells crude FOB to Trading Co. (Singapore, related):
- Transfer price: $80/barrel FOB (arm's length)

Trading Co. charters vessel from ShipCo (related):
- Freight charge: $3.50/barrel (Nigeria to Rotterdam)

Tax authority challenge: Independent shippers charge $2.50/barrel for same route; ShipCo overcharging $1.00/barrel.

Result: Transfer pricing adjustment of $1.00/barrel attributed to Producer Co. (reducing deductible expense) or Trading Co. (increasing income), depending on which entity is selected as "tested party."
```

**Best practice**: **Benchmark freight and insurance charges** separately using independent quotes (Baltic Exchange for freight, insurance quotes from Lloyd's or independent brokers).

---

## 8. Natural Gas and LNG Pricing

### 8.1 Natural Gas Pricing Mechanisms

**A. Pipeline Gas (Continental Markets)**

**Pricing basis**: **Hub pricing** (U.S., Europe)

**U.S. (Henry Hub)**:
- Price determined by supply/demand at Henry Hub interconnection
- Regional differentials for other hubs (Waha, Permian, Marcellus)

**Europe (TTF)**:
- Virtual trading point pricing
- Converged with NBP (UK) following increased pipeline interconnections

**Transfer pricing method**: **CUP using published hub prices** + adjustments for:
- **Delivery point differential** (if delivery away from hub)
- **Pipeline transportation tariffs** (if applicable)

**B. LNG (Liquefied Natural Gas)**

**Historical pricing**: **Oil-indexed** (price linked to crude oil or refined products, with 3-6 month lag)

**Formula (Asian LNG, traditional)**:
```
LNG Price ($/MMBtu) = 0.1485 × (JCC 3-month average) + Constant
Where JCC = Japan Crude Cocktail (weighted average of crude imports)
```

**Modern pricing**: **Hub-linked** or **hybrid**

- **U.S. LNG exports**: Henry Hub + liquefaction fee (e.g., Henry Hub + $3.00/MMBtu)
- **Spot LNG (Asia)**: JKM (Japan-Korea Marker) benchmark

**Transfer pricing method**: **CUP using JKM or hub-linked pricing** + adjustments for:
- **Destination flexibility** (premium for cargoes with flexible delivery)
- **Volume commitments** (term vs. spot)

### 8.2 LNG Transfer Pricing Example

**Facts**:

LNG Producer Co. (Qatar) sells LNG to Trading Co. (Singapore, related):

```
Production: 100,000 MMBtu
Delivery: Singapore (FOB Qatar)
Contract: Spot basis

Benchmark: Platts JKM (Asian LNG spot price) = $12.50/MMBtu (monthly average)

Quality adjustment: None (LNG is fungible commodity)
Location adjustment: -$0.50/MMBtu (FOB Qatar vs. delivered Asia; buyer bears freight)

Transfer price: $12.50 - $0.50 = $12.00/MMBtu
Total transaction value: 100,000 MMBtu × $12.00 = $1.2 million
```

**Alternative approach**: If term contract, may use **oil-indexed formula** (Brent-linked) with documented comparables showing independent LNG buyers accept similar formulas.

---

## 9. Worked Examples

═══════════════════════════════════════════
**WORKED EXAMPLE 1: Crude Oil Transfer Pricing with Multiple Adjustments**
═══════════════════════════════════════════

**Facts:**

BrazilPetro SA (Brazil, producer) sells crude oil to GlobalTrade BV (Netherlands, related trading company):

**Crude specifications**:
- **Production**: 500,000 barrels/month
- **API gravity**: 32° (medium crude)
- **Sulfur content**: 0.9% (slightly sour)
- **Location**: Santos Basin (offshore Brazil)

**Contract terms**:
- **Delivery basis**: FOB Santos (Brazil loading terminal)
- **Pricing date**: Monthly average Brent
- **Contract type**: Term contract (2-year agreement)

**Month**: June 2025

**Market data**:
- **Brent monthly average (June 2025)**: $85.00/barrel
- **Platts published differentials**:
  - API adjustment: -$0.45/barrel per degree below 38°
  - Sulfur adjustment: -$1.80/barrel per 0.5% above 0.4%
- **Term contract premium**: Industry surveys indicate term contracts command +$0.75/barrel premium vs. spot for security of supply

**Required:**

Calculate arm's length transfer price per barrel for June 2025 delivery.

**Analysis:**

**Step 1: Base Price**

```
Base price: Brent monthly average (June 2025) = $85.00/barrel
```

**Step 2: API Gravity Adjustment**

```
Benchmark API (Brent): 38°
BrazilPetro crude API: 32°
Difference: 32° - 38° = -6° (heavier than Brent)

Adjustment: -6° × $0.45/degree = -$2.70/barrel
```

**Step 3: Sulfur Content Adjustment**

```
Benchmark sulfur (Brent): 0.37%
BrazilPetro crude sulfur: 0.9%
Difference: 0.9% - 0.37% = +0.53% (more sulfur than Brent)

Adjustment: -(0.53% ÷ 0.5%) × $1.80 = -1.06 × $1.80 = -$1.91/barrel
```

**Step 4: Location Adjustment**

```
Delivery basis: FOB Santos (same as Brent FOB Sullom Voe)
No freight adjustment required (both FOB basis)

Location adjustment: $0
```

**Step 5: Contract Term Adjustment**

```
Contract type: Term contract (2-year agreement)
Premium for term contract: +$0.75/barrel (documented by industry survey showing independent buyers pay premium for security of supply)

Adjustment: +$0.75/barrel
```

**Step 6: Calculate Transfer Price**

```
Base price (Brent):                          $85.00/barrel
API adjustment (heavier):                     -$2.70/barrel
Sulfur adjustment (sour):                     -$1.91/barrel
Location adjustment:                          $0.00/barrel
Term contract premium:                        +$0.75/barrel
───────────────────────────────────────────
Arm's length transfer price:                  $81.14/barrel
```

**Step 7: Total Transaction Value**

```
Monthly volume: 500,000 barrels
Transfer price: $81.14/barrel
Total monthly payment: 500,000 × $81.14 = $40.57 million
```

**Documentation Requirements (Local File)**:

1. **CUP method justification**: Explanation that CUP is most appropriate method for commodity transactions per OECD Guidelines

2. **Benchmark selection**: Brent selected as appropriate benchmark for Atlantic Basin crude (Brazilian exports primarily to U.S. and Europe)

3. **Quality adjustments**:
   - Platts Crude Oil Marketwire (June 2025 edition) documenting API and sulfur differentials
   - Technical specifications of BrazilPetro crude (API 32°, sulfur 0.9%) from laboratory analysis

4. **Term contract premium**:
   - Industry survey (e.g., Wood Mackenzie, Rystad Energy) showing term contracts trade at $0.50-1.00/barrel premium vs. spot
   - Selected $0.75/barrel (midpoint) as arm's length

5. **Pricing date**:
   - Monthly average Brent for June 2025: $85.00/barrel (ICE Brent settlement prices, June 1-30 average)

6. **Consistency**:
   - Same methodology applied in prior years (2023, 2024)
   - Same methodology applied to third-party sales (if any)

═══════════════════════════════════════════

---

═══════════════════════════════════════════
**WORKED EXAMPLE 2: Internal CUP vs. External CUP Comparison**
═══════════════════════════════════════════

**Facts:**

NorthOil AS (Norway, producer) produces **1 million barrels/month** of crude oil:

**Allocation**:
- **700,000 barrels** sold to **TradeCo Ltd.** (Singapore, related trading company)
- **300,000 barrels** sold to **Shell Trading** (independent third party)

**Crude specifications**:
- **API**: 36°
- **Sulfur**: 0.5%
- **Location**: Delivered Mongstad terminal (Norway)

**Contract terms** (both TradeCo and Shell):
- **Pricing**: Monthly average Brent
- **Delivery**: FOB Mongstad
- **Contract type**: Spot (monthly negotiations)

**Month**: May 2025

**Market data**:
- **Brent monthly average (May 2025)**: $82.00/barrel
- **Shell purchase price (actual transaction, May 2025)**: $80.25/barrel FOB Mongstad

**Norwegian tax authority review** (2026 audit):
- Questions whether NorthOil is pricing sales to TradeCo (related) at arm's length
- Requests transfer pricing analysis

**Required:**

1. Calculate arm's length transfer price using **External CUP** (benchmark-based)
2. Calculate arm's length transfer price using **Internal CUP** (Shell transaction)
3. Compare methods and determine which is more reliable
4. Assess Norwegian tax authority's likely conclusion

**Analysis:**

**APPROACH 1: External CUP (Benchmark-Based)**

**Step 1: Benchmark Price**

```
Base price: Brent monthly average (May 2025) = $82.00/barrel
```

**Step 2: Quality Adjustments**

```
Benchmark (Brent): API 38°, sulfur 0.37%
NorthOil crude: API 36°, sulfur 0.5%

API adjustment: (36° - 38°) × $0.40/degree = -2° × $0.40 = -$0.80/barrel
Sulfur adjustment: ((0.5% - 0.37%) ÷ 0.5%) × $1.50 = -0.26 × $1.50 = -$0.39/barrel

Total quality adjustment: -$0.80 - $0.39 = -$1.19/barrel
```

**Step 3: Location Adjustment**

```
Delivery basis: FOB Mongstad (same as Brent FOB Sullom Voe; both North Sea terminals)
Location adjustment: $0
```

**Step 4: Transfer Price (External CUP)**

```
Base price (Brent):                           $82.00/barrel
Quality adjustments:                          -$1.19/barrel
Location adjustment:                          $0.00/barrel
───────────────────────────────────────────
Arm's length price (External CUP):            $80.81/barrel
```

**APPROACH 2: Internal CUP (Shell Transaction)**

**Step 1: Identify Comparable Transaction**

NorthOil sold **300,000 barrels** to **Shell Trading (independent)** in **May 2025**:
- **Price**: $80.25/barrel FOB Mongstad
- **Same crude**: API 36°, sulfur 0.5%
- **Same contract terms**: Monthly average Brent pricing, FOB Mongstad, spot
- **Same month**: May 2025

**Step 2: Comparability Analysis**

| **Factor** | **TradeCo (Related)** | **Shell (Independent)** | **Comparable?** |
|---|---|---|---|
| **Product** | NorthOil crude (API 36°, sulfur 0.5%) | Same | ✓ Yes |
| **Quantity** | 700,000 bbl/month | 300,000 bbl/month | ✓ Yes (both material volumes) |
| **Delivery** | FOB Mongstad | Same | ✓ Yes |
| **Pricing date** | May 2025 monthly average Brent | Same | ✓ Yes |
| **Contract type** | Spot | Same | ✓ Yes |
| **Payment terms** | 30 days | 30 days | ✓ Yes |

**Conclusion**: **Highly comparable** (no adjustments required).

**Step 3: Transfer Price (Internal CUP)**

```
Shell purchase price (May 2025):              $80.25/barrel
Adjustments:                                  None (identical terms)
───────────────────────────────────────────
Arm's length price (Internal CUP):            $80.25/barrel
```

**COMPARISON: External CUP vs. Internal CUP**

| **Method** | **Transfer Price** | **Difference** | **Reliability** |
|---|---|---|---|
| **External CUP** (Brent benchmark) | $80.81/barrel | +$0.56 vs. Internal CUP | Moderate (requires quality adjustments based on published differentials) |
| **Internal CUP** (Shell transaction) | $80.25/barrel | Reference | **Highest** (actual transaction with independent party; no adjustments required) |

**Step 4: Determine Most Reliable Method**

**OECD Guidelines, Chapter II, para. 2.15**:

> "Internal comparables may have a more direct and closer relationship to the transaction under review than external comparables. Therefore, if an internal comparable meets the comparability standard... it may be the most reliable means of determining an arm's length price."

**Conclusion**: **Internal CUP ($80.25/barrel) is more reliable** than External CUP ($80.81/barrel) because:

1. **Same seller** (NorthOil)
2. **Same product** (identical crude specifications)
3. **Same contract terms** (FOB Mongstad, monthly average Brent, spot)
4. **Same time period** (May 2025)
5. **No adjustments required** (eliminates subjectivity and potential errors)

**Step 5: Norwegian Tax Authority Conclusion**

**Likely outcome**: Tax authority will **accept Internal CUP** as arm's length transfer price, provided NorthOil documents:

1. **Shell contract**: Copy of sales agreement and invoices showing $80.25/barrel price
2. **Volume materiality**: Shell transaction (300,000 bbl) represents **30% of total sales** (sufficiently material to be reliable comparable)
3. **Arm's length negotiation**: Evidence that Shell price was negotiated at arm's length (no special relationship or non-market terms)
4. **Consistency**: NorthOil applied same pricing methodology (monthly average Brent formula) to both TradeCo and Shell transactions

**Documentation (Local File)**:

> "NorthOil AS applies the Comparable Uncontrolled Price (CUP) method for crude oil sales to related party TradeCo Ltd. The arm's length price is determined based on the price charged to Shell Trading (independent third party) for sales of identical crude under identical contract terms during the same month. This Internal CUP provides the most reliable evidence of arm's length pricing as it involves the same seller (NorthOil), same product (API 36°, sulfur 0.5%), same delivery terms (FOB Mongstad), and same pricing date (monthly average Brent). No adjustments are required. Transfer price: $80.25/barrel (May 2025)."

**Result**: NorthOil demonstrates arm's length pricing; **no transfer pricing adjustment** by Norwegian tax authority.

═══════════════════════════════════════════

---

## 10. Key Takeaways

1. **CUP method is most appropriate for commodity transfer pricing** [OECD Guidelines]; crude oil, natural gas, and LNG have actively traded markets with published benchmarks.

2. **Primary crude oil benchmarks**: **Brent** (Atlantic Basin), **WTI** (U.S.), **Dubai/Oman** (Middle East to Asia); selection depends on crude origin and export destination.

3. **Quality adjustments** are critical:
   - **API gravity**: +/- $0.30-0.50/barrel per degree difference
   - **Sulfur content**: -$1.00-2.00/barrel per 0.5% additional sulfur
   - Use **Platts, Argus** published differentials for documentation

4. **Location adjustments** account for freight and insurance:
   - **FOB vs. CIF** pricing
   - **Freight rates** from Baltic Exchange, Worldscale
   - **Pipeline tariffs** (if landlocked production)

5. **Pricing date (quotational period)** must be consistent:
   - Common approaches: date of lifting, monthly average, 5-day quotational period
   - **Mismatch risk**: Using different pricing dates for controlled vs. comparable transactions violates arm's length principle

6. **Contract terms** affect pricing:
   - **Term contracts** may command +$0.50-1.50/barrel premium vs. spot
   - **Volume discounts** ($0.25-0.75/barrel for large volumes)

7. **Internal CUP is more reliable than External CUP** when available [OECD Guidelines]: Actual sales to independent third parties provide direct evidence of arm's length price with minimal adjustments.

8. **"Six Method" rule** (Nigeria, Ghana, Kenya): Tax authorities may disregard benchmark pricing and impose alternative valuations; defense requires **contemporaneous documentation**, **APAs**, and **third-party sales evidence**.

9. **Natural gas and LNG pricing**: Hub-based (Henry Hub, TTF, JKM) or oil-indexed (traditional Asian LNG); transfer pricing method is CUP with hub price + adjustments.

10. **Best practices**:
    - Maintain **contemporaneous documentation** (benchmark prices, quality certificates, freight quotes)
    - Use **recognized price reporters** (Platts, Argus, Bloomberg)
    - Apply **consistent methodology** year-over-year and across all transactions
    - Evidence **third-party sales** at same prices (Internal CUP)

---

**This chapter has examined commodity pricing methodologies, benchmark selection, quality and location adjustments, pricing date determination, and tax authority challenges, enabling tax professionals to establish defensible arm's length pricing for crude oil, natural gas, and LNG transactions.**
