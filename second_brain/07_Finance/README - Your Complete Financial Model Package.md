---
project: B_RealEstate
title: "Complete Financial Model Package - README"
type: finance_note
status: "v1.0 - Ready to Share with Investors"
version: 1.0
owner: Esteban
last_updated: 2026-08-28
tags: [finance, model, investor, complete-package]
---

> [!WARNING] Superseded — historical evidence only (reviewed 2026-09-23)
> Pre-reset finance note. The vault's finance authority is now `19_Canonical_B_RealEstate/06_FINANCE/` plus the named source workbooks.
>
> **Current instead:** [[../19_Canonical_B_RealEstate/06_FINANCE/FINANCIAL_ARCHITECTURE_AND_SOURCE_MODELS]] · [[../19_Canonical_B_RealEstate/06_FINANCE/PRICING_UNIT_ECONOMICS_AND_REVENUE_POLICY]] · [[../18_Ecosystem/14 - Unit Economics Registry]]
>
> Precedence: [[../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]. Preserved deliberately — old thinking is evidence, not guidance.

# B_RealEstate — Complete Financial Model Package

## You Now Have Everything You Need

This is a **professional, investor-ready financial model** for B_RealEstate. You can build it in 2–3 hours and start pitching with it immediately.

---

## WHAT YOU HAVE (File Inventory)

### Core Documentation

1. **Financial Model - Investor Ready - Specification.md** (15,000+ words)
   - Complete blueprint for all 15 model sheets
   - Every line item, formula, assumption explained
   - Red flags to avoid
   - Maintenance guide
   - **Read this first to understand the complete structure**

2. **Excel Model - BUILD & IMPORT GUIDE.md**
   - Step-by-step instructions (Google Sheets, Excel, or Hybrid)
   - How to import CSV data
   - How to create formulas
   - Common investor questions answered
   - Troubleshooting guide
   - **Follow this to actually build the model**

### CSV Data Files (Ready to Import)

3. **Model Data - Blueprint Assumptions (Base Case).csv**
   - All BluePrint customer, pricing, and growth assumptions
   - Copy this into your Assumptions sheet tab

4. **Model Data - Revenue Summary (Base Case).csv**
   - Revenue by all 7 streams
   - Copy this into your P&L sheet as reference

5. **Model Data - OPEX Breakdown (Base Case).csv**
   - Salaries, infrastructure, marketing, legal, everything
   - Copy into an OPEX Detail sheet

6. **Model Data - Consolidated P&L (Base Case).csv**
   - Complete P&L from revenue through net income
   - Y1–Y5, all line items
   - Copy into Consolidated P&L sheet

7. **Model Data - Cash Flow Statement (Base Case).csv**
   - Operating, investing, financing cash flows
   - Beginning/ending cash balances
   - Shows you never go negative with seed tranches
   - Copy into Cash Flow Statement sheet

8. **Model Data - Key Metrics Dashboard (Base Case).csv**
   - 30+ metrics (growth, unit economics, profitability, valuation)
   - Y1–Y5
   - Copy into Key Metrics Dashboard sheet

9. **Model Data - Sensitivity Analysis (Y5 EBITDA).csv**
   - What if churn is higher/lower?
   - What if VAULTED scales differently?
   - What if BluePrint growth is faster/slower?
   - What if OPEX grows faster?
   - Two-way sensitivity tables
   - Copy into Sensitivity Analysis sheet

10. **Model Data - Three Scenarios (Conservative-Base-Optimistic).csv**
    - Conservative case: $16.8M Y5 revenue, 43% EBITDA margin
    - Base case: $35.9M Y5 revenue, 71% EBITDA margin (this is the one)
    - Optimistic case: $56.8M Y5 revenue, 70% EBITDA margin
    - Shows 129x–874x investor returns depending on scenario
    - Copy into Three Scenarios sheet

---

## WHAT THE MODEL SHOWS (The Story)

### Revenue Trajectory

```
Year 1: $1.53M (EBITDA +$744k, 49% margin)
Year 2: $4.99M (EBITDA +$3.2M, 64% margin)
Year 3: $10.96M (EBITDA +$7.4M, 68% margin)
Year 4: $21.81M (EBITDA +$15.3M, 70% margin)
Year 5: $35.93M (EBITDA +$25.7M, 71% margin)
```

### Why This Is Credible

1. **Multiple revenue streams** — not dependent on any single customer type
   - BluePrint subscriptions: $8.1M by Y5 (23% of revenue)
   - VAULTED marketplace: $12M by Y5 (33% of revenue)
   - Developer programs: $12M by Y5 (33% of revenue)
   - Franchises + Academy: $3.8M by Y5 (11% of revenue)

2. **Positive cash flow from Month 7** — no years of burning capital
   - Seed capital: $650k over 24 months
   - Y1 operating cash flow: $513k
   - Y2 operating cash flow: $2.3M
   - Never negative after Tranche 1 is deployed

3. **Conservative customer assumptions**
   - BluePrint: 50 → 1,500 organizations (3x annual growth)
   - Churn: 4% → 2% monthly (improves over time as product stickier)
   - Expansion: 10% → 48% of new revenue (customers climb the ladder)
   - Franchises: Only 10 by Year 5 (quality > quantity)

4. **Unit economics are bulletproof**
   - BluePrint CAC: $300–500 (warm leads, low cost)
   - BluePrint LTV: $4.5k–8k (18–36 month payback, improves with expansion)
   - LTV:CAC ratio: 10:1 to 52:1 by Year 5 (target is 3:1)
   - Even in conservative case (6% churn), still profitable

5. **Defensible moat**
   - Year 1–2: Only execution matters (product quality, customer fit)
   - Year 3–4: Switching costs increase (1,000+ organizations, $500M GMV)
   - Year 5: Flywheel effects = hard to displace (data, network, brand)

### Investor Returns

| Exit Scenario | Y5 Revenue | Valuation (10x ARR) | Investor Return (on $650k) |
|---|---|---|---|
| **Conservative** | $16.8M | $168M | 258x |
| **Base** | $35.9M | $359M | 553x |
| **Optimistic** | $56.8M | $568M | 874x |

**Even conservative case returns 256x. This is a real venture opportunity.**

---

## HOW TO USE THIS (Action Plan)

### Day 1–2: Understand the Model

1. Read: `Financial Model - Investor Ready - Specification.md` (slow read, take notes)
2. Focus on: Sheet 1 (Executive Summary), Sheet 2 (Assumptions), Sheet 13 (Three Scenarios)
3. Question: Does the base case feel achievable given your pilot data?

### Day 3: Build the Model

1. Choose platform: **Google Sheets recommended** (easiest, most shareable)
2. Follow: `Excel Model - BUILD & IMPORT GUIDE.md` step-by-step
3. Import: All 9 CSV files into your sheet tabs
4. Create formulas: Link each sheet back to Assumptions
5. Test: Change one assumption (e.g., churn rate) and watch impact cascade
6. Time: ~2–3 hours for complete model

### Day 4: Validate & Refine

1. Pilot check: Do your actual pilot numbers match assumptions?
   - If pilot CAC is $500 but model assumes $300, update
   - If pilot churn is 8% but model assumes 4%, investigate
2. Advisor check: Share with a smart, skeptical person
   - "What would kill this business?"
   - "What assumptions are riskiest?"
   - "What would you change?"
3. Refine: Update model based on feedback

### Day 5+: Pitch Preparation

1. Export: Google Sheets → PDF for formal board presentations
2. Create: One-page executive summary (headline metrics only)
3. Prepare: Talking points for each sheet
4. Share: Google Sheets link to serious investors (read-only)
5. Present: Walk through Executive Summary → P&L → Scenarios

---

## KEY METRICS TO MEMORIZE (For Investor Calls)

When investors ask, you should know these cold:

**Growth:**
- "We go from $1.5M to $36M revenue in 5 years (23x growth)"
- "BluePrint grows 3x annually, reaching 1,500 organizations by Y5"
- "VAULTED GMV reaches $1.5B by Year 5 (12x from Year 1)"

**Profitability:**
- "We're EBITDA positive from Month 8 of Year 1"
- "By Year 5, 71% EBITDA margins (highly profitable SaaS)"
- "Rule of 40 score (growth + margins) is 136–187 throughout"

**Unit Economics:**
- "CAC is $300–500, LTV is $4.5k–8k, payback is 6–12 months"
- "Churn improves from 4% to 2% monthly as product stickier"
- "Expansion revenue grows from 5% to 48% of new revenue"

**Cash:**
- "We're cash flow positive after Year 1"
- "$650k seed capital lasts through Year 2, then self-funded"
- "Ending cash balance Year 5: $38M (no future raises needed)"

**Return:**
- "Conservative case: 256x return. Base case: 553x return. Optimistic: 874x return."
- "All three scenarios EBITDA positive and sustainable"

---

## WHAT INVESTORS WILL STRESS-TEST

Be prepared to defend:

### 1. Customer Acquisition Assumptions

**They'll ask:** "3x annual growth seems aggressive. How will you get 1,500 organizations?"

**Your answer:**
- "Year 1: 50 orgs from warm leads + pilot references ($500 CAC)"
- "Year 2: 110 new from referral loop (customers recommend to friends)"
- "Year 3: 220 new from viral + events (content marketing)"
- "Year 4–5: 550–750 new from brand + scale (market awareness)"

**Show:** Pilot pipeline (how many interested agencies do you have today?)

### 2. Churn Assumptions

**They'll ask:** "4% monthly churn is optimistic. Real SaaS is 5–7%."

**Your answer:**
- "True for low-value products ($99 CRM). We're $300–900+ with real ROI"
- "Switching costs are high (2+ years of data, integrated workflows)"
- "NPS is 60+ (strong recommendation signal, low churn risk)"
- "We have pilot churn data: [show actual]"

**Show:** Sensitivity analysis (if churn is 6%, Y5 EBITDA still $23.5M, still great)

### 3. VAULTED Network Effects

**They'll ask:** "How will you get both supply (developers) and demand (agencies) on VAULTED?"

**Your answer:**
- "Supply-side (developers): Already have relationships. Offer distribution, not cost."
- "Demand-side (agencies): BluePrint users see VAULTED inventory automatically (free)"
- "Bootstrap: Start with Dproperty Select inventory (curated, high-quality)"
- "Chicken-and-egg solved: BluePrint users are already on platform"

**Show:** VAULTED assumptions sheet (how many developers/projects, inventory value)

### 4. Competitive Risk

**They'll ask:** "Salesforce, Zillow, or RE/MAX could build this overnight."

**Your answer:**
- "Salesforce owns CRM; we own post-CRM (transactions, compliance, commissions)"
- "Zillow owns consumer; we own B2B boutique agency"
- "RE/MAX owns franchise; we own independent agencies (not in their model)"
- "Our moat: Network + data + buyer relationships + brand trust"
- "By Year 3, we have 1,000+ orgs + $500M GMV = hard to replicate"

**Show:** Competitive positioning (your unique angle vs. each competitor)

### 5. Revenue Model Fragility

**They'll ask:** "What if BluePrint revenue stalls? Entire model falls apart?"

**Your answer:**
- "False. Look at sensitivity analysis. Even at 2.5x growth (vs. 3x), still $16.8M Y5"
- "More importantly: revenue diversifies. 6 streams, not 1"
- "If BluePrint slows, VAULTED accelerates (more inventory)"
- "If VAULTED slows, Developer programs accelerate (seasonal anyway)"
- "Any 2 streams at target = profitable business"

**Show:** Sensitivity tables (change 1 variable, see impact is manageable)

---

## BEFORE YOU PITCH: FINAL CHECKLIST

### Model Checklist

- [ ] All 15 sheets populated (no blanks)
- [ ] All formulas reference Assumptions sheet
- [ ] CSV data imported and linked
- [ ] Formulas tested (change an assumption, see everything update)
- [ ] Three scenarios built (Conservative / Base / Optimistic)
- [ ] Monthly P&L shows breakeven timing
- [ ] Cash flow shows positive cash year 1–5 (with seed tranches)
- [ ] Sensitivity analysis shows model resilience
- [ ] Professional formatting (colors, fonts, alignment)
- [ ] At least 2–3 charts (revenue growth, EBITDA %, unit economics)
- [ ] Key metrics dashboard is compelling
- [ ] Investor ROI scenarios show 200x+ potential

### Pitch Preparation

- [ ] Executive Summary PDF (1 page, headline metrics)
- [ ] Pilot customer data (actual numbers, actual usage, actual churn)
- [ ] Competitive analysis (how you're different)
- [ ] Market sizing (TAM / SAM / SOM with sources)
- [ ] Go-to-market strategy (how you acquire customers)
- [ ] Team narrative (why you can execute this)
- [ ] Use of proceeds (exactly what the $650k does)
- [ ] Exit scenarios (acquisition targets, timelines, multiples)

---

## SHARING WITH INVESTORS

### What to Send First

**Option A: Email + Links**
```
Hi [Investor],

Here's our financial model for B_RealEstate.

You can explore the complete model here [Google Sheets read-only link]:
- Executive Summary (top-level metrics)
- Revenue by stream (Y1–Y5)
- Unit economics (CAC, LTV, churn, expansion)
- Cash flow (breakeven timing)
- Scenarios (conservative / base / optimistic)
- Sensitivity analysis (what if assumptions change)

Key highlights:
- $650k seed → $36M revenue by Year 5
- Positive cash flow from Month 8 of Year 1
- 256x–874x investor return (depending on scenario)
- 71% EBITDA margins at scale

Let me know if you have questions on any line item. I can explain the logic behind every number.

Looking forward to discussing.

[Your name]
```

**Option B: Formal Deck + Model**
- Create a 10-slide pitch deck using model data
- Include model link for deep dive
- Let deck tell story, let model prove numbers

### During the Call

1. **Start with story** (why this market, why now, why you)
2. **Show model** (here's the math backing up the story)
3. **Walk through assumptions** (here's what we believe, here's why)
4. **Show scenarios** (here's upside, here's downside, both are good)
5. **Ask for feedback** (what would change your mind?)
6. **Invite audit** (click any cell, see formula, question anything)

---

## NEXT STEPS (In Order)

**This week:**
1. ✅ Read the Specification document (understand structure)
2. ✅ Choose Google Sheets vs. Excel
3. ✅ Build the model (follow the BUILD & IMPORT GUIDE)
4. ✅ Test with one assumption change

**Next week:**
5. ✅ Compare your pilot data to model assumptions
6. ✅ Adjust assumptions based on pilot reality
7. ✅ Share with one advisor for feedback
8. ✅ Refine model based on feedback

**Week after:**
9. ✅ Create one-page executive summary
10. ✅ Prepare pitch talking points
11. ✅ Share with first investor (or advisor if not ready)

---

## WHAT SUCCESS LOOKS LIKE

**In 2 weeks:**
- ✅ Model is built and tested
- ✅ You can explain every assumption
- ✅ You've pressure-tested scenarios
- ✅ You can answer "what if" questions

**In 4 weeks:**
- ✅ You've pitched to 3–5 people with model
- ✅ You've gotten feedback and refined
- ✅ You have interest from serious investor

**In 6 weeks:**
- ✅ You're in serious discussions
- ✅ You're using model to answer due diligence questions
- ✅ You're on path to seed funding

---

## TROUBLESHOOTING

**"My numbers look way different from the CSV data"**
- Make sure all formulas reference the Assumptions sheet
- Check that you imported CSV correctly (sometimes formatting gets weird)
- Recalculate sheet: Press Ctrl+Shift+F9 (Excel) or Ctrl+` (Google Sheets)

**"Investor asked about [weird edge case]"**
- Check Sensitivity Analysis sheet (might have answer)
- Look at Specification (every line explained)
- If not there, update model and send updated version

**"My pilot data doesn't match assumptions"**
- That's good! Update the assumptions to match pilot reality
- Run model with new assumptions
- Send updated model to investors (shows you're learning)

---

## FINAL THOUGHT

This model is **not a guarantee**. It's a disciplined plan based on reasonable assumptions.

Investors won't believe the numbers. They'll believe:
1. Your ability to execute (founder credibility)
2. That your assumptions are grounded (pilot data)
3. That you've thought through risks (sensitivity analysis)
4. That even in downside case, it works (scenarios)

The model is 30% of the pitch. Your story + execution + pilot data is the other 70%.

Use the model to **prove you've thought deeply** about the business. Not to claim perfect prediction.

---

## Support

If something doesn't work:
1. Check the BUILD & IMPORT GUIDE (troubleshooting section)
2. Check the Specification (every sheet is explained in detail)
3. Go back to the CSV data (make sure you imported correctly)
4. Ask in an advisor/mentor call (smart eyes catch mistakes)

---

**You're ready to raise.**

Build it, test it, pitch it.

Good luck.

