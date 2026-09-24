---
project: B_RealEstate
title: "KPIs & North-Star Metrics - Revised"
type: strategy_note
status: "v2.0 - Active"
version: 2.0
owner: Esteban
last_updated: 2026-08-28
tags: [strategy, metrics, kpis, north-star]
---

> [!WARNING] Superseded — historical evidence only (reviewed 2026-09-23)
> Pre-reset KPI set tied to franchise-unit growth.
>
> **Current instead:** [[../19_Canonical_B_RealEstate/09_ROADMAP/KPIS_GATES_AND_KILL_CRITERIA]] and [[../19_Canonical_B_RealEstate/00_HOME/GLOSSARY_AND_METRIC_DICTIONARY]]
>
> Precedence: [[../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]. Preserved deliberately — old thinking is evidence, not guidance.

# KPIs & North-Star Metrics — Revised v2.0

## Strategic Shift in Metrics

### Previous Model (v1.0)

North-star metrics were:
- # of franchises (5 by Year 5)
- # of white-label agencies (20)
- # of developer projects (15)

**Problem:** These metrics track partnership count, not infrastructure adoption.

### New Model (v2.0)

North-star metrics measure whether **B_RealEstate is becoming infrastructure**:

---

## Seven North-Star Metrics

### 1. BluePrint Organizations (Primary)

**What:** Total number of distinct organizations actively using BluePrint.

**Why it matters:**
- Shows market adoption of the core product.
- Indicates whether "any agency can use this" is real.
- Is the leading indicator for everything else (more orgs = more transactions = more data = more VAULTED value).

**Target (Y5):** 1,500–2,000 organizations

**Tracking:**
- Monthly active organizations (vs. total signups)
- By geography (Colombia, Panama, Mexico, Spain, US, etc.)
- By tier (Solo, Growth, Pro, Enterprise)
- By use case (boutique agency, developer sales team, etc.)

**Dashboard red flag:** Stalled growth (< 5% MoM growth) or sudden increase in churn.

---

### 2. Transactions Processed (Volume)

**What:** Total real-estate transactions managed through BluePrint monthly.

**Why it matters:**
- Shows actual economic activity flowing through the platform.
- Is the denominator for Copilot training (more transactions = smarter AI).
- Drives VAULTED supply/demand (transactions create data about market).

**Target (Y5):** 5,000–8,000 transactions/month

**Example:** If avg organization closes 5 deals/month, and you have 1,200 orgs, that's ~6,000 transactions.

**Tracking:**
- Monthly transaction count
- Transaction volume by geography
- Transaction type (resale, development, rental, lease)
- Transaction velocity (time from intake to close)

**Dashboard red flag:** Declining transaction count (may indicate churn or slower market).

---

### 3. BluePrint GMV (Gross Merchandise Value)

**What:** Total property value of transactions processed through BluePrint annually.

**Why it matters:**
- Shows scale of economic activity under B_ infrastructure.
- Is the basis for VAULTED commission calculation.
- Demonstrates defensibility (we are the infrastructure for $Bn in real-estate activity).

**Target (Y5):** $200–400B annually

**Calculation:**
- 6,000 transactions/month = 72,000/year
- Avg transaction value: $300k (varies by market)
- Total GMV: 72,000 × $300k = $21.6B

(Conservative estimate; actual will vary by market.)

**Tracking:**
- Annual BluePrint GMV
- By geography and property type
- Avg transaction value
- GMV per organization (org health metric)

---

### 4. VAULTED GMV (Transactions)

**What:** Total property value transacted through VAULTED marketplace annually.

**Why it matters:**
- Shows how much of BluePrint activity is being driven through the network.
- Is direct measure of network effects.
- Drives transaction revenue (0.75% commission).

**Target (Y5):** $1.5B annually (10% of BluePrint GMV)

**Calculation:**
- If 10% of BluePrint agencies use VAULTED actively.
- And they close 5% of deals through VAULTED.
- That's 72,000 × 10% × 5% = 360 deals/year through VAULTED.
- 360 × $300k = $108M/year.

(Conservative; actual should be higher as network matures.)

**Tracking:**
- Monthly VAULTED GMV
- % of BluePrint GMV flowing through VAULTED
- Deal origination source (developer vs. agency vs. investor)
- Avg deal size
- Time from listing to close

---

### 5. Network Supply (Inventory Available)

**What:** Total property value available for sale/investment through VAULTED.

**Why it matters:**
- Shows depth of inventory available to network.
- Is upstream indicator of VAULTED GMV (more supply = more potential deals).
- Demonstrates value to developers (their inventory reaches 1,500+ agencies).

**Target (Y5):** $100–200B in available inventory

**Calculation:**
- If 100 developers are listed on VAULTED.
- Avg developer portfolio: $500M–$1B.
- Total inventory: 100 × $750M = $75B.

(Grows as more developers join and projects launch.)

**Tracking:**
- Total active listings (by property)
- Total inventory value
- By geography and property type
- Inventory freshness (median age of listing)
- Inventory-to-closed ratio (how much converts to deals)

---

### 6. Expansion Revenue (Customer LTV Growth)

**What:** Revenue per existing customer in Year 2+.

**Why it matters:**
- Shows whether customers are climbing the ladder (BluePrint → VAULTED → Network → Franchise).
- Is healthiest metric for SaaS (expansion > acquisition).
- Indicates product-market fit (customers grow with you).

**Target (Y5):** 
- Solo customer: $1,200–2,000/year (from $1,200)
- Growth customer: $8,000–12,000/year (from $4,200)
- Pro customer: $15,000–25,000/year (from $12,000)

**Tracking:**
- Expansion revenue as % of total new revenue
- Tier upgrade rate (Growth → Pro)
- Tier upgrade velocity (months to upgrade)
- New services adoption rate (Copilot, Academy, Premium support)
- VAULTED participation rate (% of customers active on marketplace)
- Network membership rate (% of customers in tier 3)

**Dashboard red flag:** Stalled expansion (customers not climbing ladder = LTV plateau = profitability ceiling).

---

### 7. VAULTED Network Penetration

**What:** % of BluePrint organizations actively trading on VAULTED.

**Why it matters:**
- Shows strength of network effects.
- Is indicator of whether two-sided marketplace is working.
- Is predictor of future VAULTED GMV.

**Target (Y5):** 60–80% of BluePrint orgs active on VAULTED

**Calculation:**
- If 1,500 BluePrint orgs exist.
- And 1,000 are active on VAULTED (>=1 deal/quarter).
- That's 67% penetration.

**Tracking:**
- % of BluePrint orgs with VAULTED activity (month-over-month)
- By tier (Solo, Growth, Pro)
- By geography
- Activity frequency (deals per org per quarter)

**Dashboard red flag:** Low penetration (< 40%) indicates VAULTED is not sticky or valuable.

---

## Secondary Metrics (By Business Line)

### BluePrint Health

| Metric | Target | Why |
|---|---|---|
| **ARR per organization** | $4,200–5,000 | Shows successful tier mix and upsell |
| **Churn rate** | < 5%/month | Standard for SaaS, shows stickiness |
| **NPS (Net Promoter Score)** | > 60 | Shows customer satisfaction and referral likelihood |
| **Time to value** | < 1 week | Shows product maturity and onboarding efficiency |
| **Support tickets per org** | < 1/month | Shows product stability and self-service capability |

### VAULTED Health

| Metric | Target | Why |
|---|---|---|
| **Commission revenue per transaction** | $1,500–3,000 | Shows healthy deal size and B_ take |
| **Time from listing to close** | 30–60 days | Shows market efficiency |
| **Repeat buyer rate** | > 40% | Shows brokers coming back to buy again |
| **Merchant satisfaction** | > 70% | Developer NPS on VAULTED experience |
| **Fraud/dispute rate** | < 0.5% of GMV | Shows platform trust and quality control |

### Developer Program Health

| Metric | Target | Why |
|---|---|---|
| **Projects on platform** | 15–25 active | Shows developer adoption and supply depth |
| **Avg deals per project** | 20–30 | Shows distribution effectiveness |
| **Commission revenue per project** | $600k–900k | Shows platform value to developer |
| **Developer NPS** | > 70 | Shows satisfaction with distribution |
| **Retention rate** | > 85% | Shows stickiness of developer contracts |

### Franchise Health

| Metric | Target | Why |
|---|---|---|
| **Franchisee GCI** | 40–60 units/year | Shows franchisee success (predicts retention) |
| **Franchisee royalty contribution** | $40k–80k/year | Shows economics are working |
| **Franchisee retention** | > 95% | Shows strong economics and support |
| **Franchisee NPS** | > 70 | Shows satisfaction with brand + system |
| **Time to profitable** | 6–12 months | Shows franchisee ramp is healthy |

---

## Derived/Composite Metrics

### Network Health Score

Composite of:
- % BluePrint orgs active on VAULTED
- Avg expansion revenue per org
- Month-over-month growth in transaction volume
- Developer satisfaction (NPS)

**Target:** 75–85 (scale 1–100)

**Why it matters:** Tells you overall health of the ecosystem without one single metric.

### Customer Lifetime Value (LTV)

| Customer Segment | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| BluePrint Solo | $1.2k | $2.5k | $3.5k | $4.5k | $5.5k |
| BluePrint Growth | $4.2k | $9k | $15k | $22k | $30k |
| BluePrint Pro | $12k | $25k | $35k | $50k | $65k |
| VAULTED participant | +$1.5k | +$4.5k | +$9k | +$15k | +$25k |
| Network member | +$6k | +$15k | +$25k | +$40k | +$60k |
| Franchise | $62.8k | $125k | $190k | $250k | $315k |

**Why it matters:** Shows whether customer acquisition ROI is increasing (good) or plateauing (bad).

---

## Leading vs. Lagging Indicators

### Leading Indicators (Predict Future Success)

| Indicator | What It Means | Red Flag |
|---|---|---|
| **New BluePrint signups MoM** | Adoption momentum | < 10/month |
| **% orgs with > 2 features used** | Product fit | < 50% |
| **New VAULTED listings/month** | Supply momentum | < 20/month |
| **Developer pipeline (projects in discussion)** | Supply future | < 5 projects |
| **Expansion revenue as % new revenue** | Customer climbing ladder | < 20% |

### Lagging Indicators (Confirm Success)

| Indicator | What It Means | Red Flag |
|---|---|---|
| **BluePrint organizations (total)** | Market penetration | Flat growth 2+ months |
| **BluePrint ARR** | Revenue scale | < 20% YoY growth |
| **VAULTED GMV annual** | Transaction scale | Declining trends |
| **Expansion revenue (absolute)** | Customer LTV | Not growing 2x YoY |
| **Franchise count** | Vertical integration | Stalled (< 1 new/quarter) |

---

## Quarterly Business Reviews (QBRs)

### What We Track

**Every quarter, review:**

1. **Top metrics (7 north stars)**
   - Are we moving in right direction?
   - Are growth rates slowing or accelerating?

2. **Metric breakdowns (geographic, by segment)**
   - Where is growth coming from?
   - Where are we weak?

3. **Derived metrics (LTV, NPS, churn)**
   - Are customers getting healthier?

4. **Cohort analysis**
   - How do organizations onboarded in Q1 compare to Q2?
   - Where is cohort health improving/declining?

5. **Sensitivity analysis**
   - If BluePrint growth slows 50%, how does that affect our revenue forecast?
   - If VAULTED penetration doesn't reach targets, what else needs to accelerate?

---

## What to Ignore

### Vanity Metrics (Don't Track)

- Total signups (everyone signs up; retention matters)
- Revenue (result of everything else; track the drivers)
- Franchise count (quality > quantity)
- Number of features built (velocity > delivery)

### Context-Dependent Metrics (Don't Obsess Over)

- MRR/ARR absolute numbers (track growth rate instead)
- Blended CAC (track per-channel instead)
- Churn rate alone (track cohort retention instead)

---

## How to Use These Metrics

### For Internal Management

Track weekly dashboards of top 7 metrics + 2–3 secondary metrics most relevant to this month's focus.

Spend 10% of time on metrics, 90% on actions to move them.

### For Investor Updates

Report monthly:
- Top 7 metrics + month-over-month change
- Key highlights (What moved? What didn't?)
- Forecast update (Are we on track to targets?)

Report quarterly:
- Full breakdown by segment, geography, customer tier
- Cohort analysis
- Strategic updates based on what metrics revealed

### For Decision Making

When evaluating a new feature / partnership / market expansion:

1. "Does this move our north-star metrics?"
2. "What's the LTV impact?"
3. "What's the leading indicator we can track?"

If a decision doesn't move metrics, it's a nice-to-have. Not a priority.

