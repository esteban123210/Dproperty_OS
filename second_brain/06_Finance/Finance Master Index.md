---
project: B_RealEstate
title: "MASTER INDEX - Complete Financial Model Package"
type: finance_note
status: "v1.0 - MASTER SUMMARY"
version: 1.0
owner: Esteban
last_updated: 2026-08-28
tags: [finance, index, master, complete]
---

> [!WARNING] Stale figures — superseded 2026-09-23
> This note still uses the **retired $650k / 24-month funding ask**. The canonical capital position is a **$950k capitalization envelope with an $800k 18-month operating plan, released in stages against evidence gates**.
>
> The modelled returns, ownership percentages and exit multiples below are derived from the old ask and are **not current investor guidance**. Kept as evidence of the earlier scenario work.
>
> Canon: [[../01_Canon/09 - Unit Economics Registry]] · [[../01_Canon/00 - Precedence and Canonical Reconciliation]]

> [!WARNING] Superseded — historical evidence only (reviewed 2026-09-23)
> Pre-reset finance note. The vault's finance authority is now `01_Canon/06_FINANCE/` plus the named source workbooks.
>
> **Current instead:** [[Financial Architecture and Source Models]] · [[Pricing Unit Economics and Revenue Policy]] · [[../01_Canon/09 - Unit Economics Registry]]
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]. Preserved deliberately — old thinking is evidence, not guidance.

# MASTER INDEX — B_RealEstate Financial Model Complete Package

## Files You Now Have (11 Total)

All files are in: `second_brain/06_Finance/`

### Documentation Files (3)

| # | File | Size | Purpose | Action |
|---|---|---|---|---|
| 1 | **README - Your Complete Financial Model Package.md** | ~6k words | Overview of entire package, action plan, checklist | **READ FIRST** |
| 2 | **Financial Model - Investor Ready - Specification.md** | ~15k words | Sheet-by-sheet blueprint, formulas, assumptions | **REFERENCE GUIDE** |
| 3 | **Excel Model - BUILD & IMPORT GUIDE.md** | ~8k words | Step-by-step build instructions, troubleshooting | **BUILD INSTRUCTIONS** |

### CSV Data Files (8)

These are ready-to-import data files for your spreadsheet:

| # | File | Sheets to Import Into | Format | Action |
|---|---|---|---|---|
| 4 | **Model Data - Blueprint Assumptions (Base Case).csv** | Assumptions | 13 rows × 5 cols | Import first |
| 5 | **Model Data - Revenue Summary (Base Case).csv** | Consolidated P&L (ref) | 8 rows × 7 cols | Reference only |
| 6 | **Model Data - OPEX Breakdown (Base Case).csv** | OPEX Detail | 12 rows × 8 cols | Create new sheet |
| 7 | **Model Data - Consolidated P&L (Base Case).csv** | Consolidated P&L | 48 rows × 6 cols | Main financials |
| 8 | **Model Data - Cash Flow Statement (Base Case).csv** | Cash Flow Statement | 25 rows × 6 cols | Critical metrics |
| 9 | **Model Data - Key Metrics Dashboard (Base Case).csv** | Key Metrics | 30 rows × 7 cols | Investor dashboard |
| 10 | **Model Data - Sensitivity Analysis (Y5 EBITDA).csv** | Sensitivity Analysis | 18 rows × 5 cols | Risk analysis |
| 11 | **Model Data - Three Scenarios (Conservative-Base-Optimistic).csv** | Three Scenarios | 16 rows × 16 cols | Scenario comparison |

---

## Quick Start (2-Hour Build)

### Step 1: Understand the Model (15 minutes)

1. Read: **README - Your Complete Financial Model Package.md** (sections: "WHAT YOU HAVE" and "WHAT THE MODEL SHOWS")
2. Skim: **Financial Model - Investor Ready - Specification.md** (just Sheet 1 Executive Summary)
3. Question: Does the base case seem achievable?

### Step 2: Choose Your Platform (5 minutes)

- **Google Sheets** (Recommended): Easy, shareable, transparent formulas
- **Excel**: More powerful, offline, better formatting

### Step 3: Build the Model (90–120 minutes)

1. Follow: **Excel Model - BUILD & IMPORT GUIDE.md** step-by-step
2. Create: 15 sheet tabs
3. Import: All 8 CSV files
4. Link: Create formulas connecting tabs back to Assumptions

### Step 4: Test & Validate (15 minutes)

1. Change one assumption (e.g., churn rate 4% → 6%)
2. Watch EBITDA recalculate across all sheets
3. If everything updates: ✅ Model works
4. If not: Check BUILD & IMPORT GUIDE troubleshooting section

**Time: 2–2.5 hours. Result: Investor-ready model.**

---

## Deep Dive (If You Have Questions)

| Question | File | Section |
|---|---|---|
| **"What goes in each sheet?"** | Financial Model Specification | Sheet descriptions (15 sheets explained) |
| **"How do I build formulas?"** | Excel Model Build Guide | Step 3: Create Formulas |
| **"How do I import CSV data?"** | Excel Model Build Guide | Step 2: Import CSV Data |
| **"What if this assumption is wrong?"** | Financial Model Specification | Sheet 12: Sensitivity Analysis |
| **"What about franchises?"** | Financial Model Specification | Sheet 6: Franchise Unit Economics |
| **"What about VAULTED?"** | Financial Model Specification | Sheet 4: VAULTED Marketplace |
| **"What about developers?"** | Financial Model Specification | Sheet 5: Developer Programs |
| **"Why is churn 4%?"** | Financial Model Specification | Sheet 2: Assumptions explanation |
| **"When do we break even?"** | CSV Data - Cash Flow | Look for first positive month |
| **"What's the investor return?"** | CSV Data - Key Metrics | Look for "Seed ROI" lines |

---

## The Model at a Glance

### Revenue Growth

```
Year 1: $1.53M
Year 2: $4.99M
Year 3: $10.96M
Year 4: $21.81M
Year 5: $35.93M
```

**Growth rate: 23x over 5 years (23% CAGR)**

### Profitability

```
Year 1 EBITDA: $744k (49% margin)
Year 2 EBITDA: $3.2M (64% margin)
Year 3 EBITDA: $7.4M (68% margin)
Year 4 EBITDA: $15.3M (70% margin)
Year 5 EBITDA: $25.7M (71% margin)
```

**Breakeven: Month 8 of Year 1. Highly profitable by Year 3.**

### Customer Growth

```
BluePrint Organizations: 50 → 1,500 (30x)
VAULTED GMV: $75M → $1.5B (20x)
Developer Projects: 1 → 15 (15x concurrent)
Franchises: 0 → 10 (selective)
```

### Unit Economics

```
BluePrint CAC: $300–500
BluePrint LTV: $4.5k–8k
Payback period: 6–12 months
LTV:CAC ratio: 10:1 to 52:1 (target 3:1+)
```

### Investor Return

```
Conservative case: 256x on $650k seed ($168M exit)
Base case: 553x on $650k seed ($359M exit)
Optimistic case: 874x on $650k seed ($568M exit)
```

---

## File Dependencies & Reading Order

```
README (overview)
    ↓
Financial Model Specification (understand structure)
    ↓
Excel Build Guide (build it)
    ↓
CSV Data Files (import it)
    ↓
Your working model (use it)
```

**For investors, show in this order:**
1. Executive Summary (from Key Metrics sheet)
2. Revenue growth chart (from P&L)
3. EBITDA margins (from P&L)
4. Unit economics (from Key Metrics)
5. Scenarios (from Three Scenarios sheet)
6. Sensitivity analysis (from Sensitivity sheet)

---

## Customization Guide

### Change These If Your Pilots Differ

**If your actual CAC is $500 (not $300):**
- Go to Financial Model Specification, Sheet 11
- Update: BluePrint CAC formula (adjust LTV:CAC calculations)
- Re-run model

**If your pilot churn is 8% (not 4%):**
- Go to Assumptions sheet
- Update: Churn Rate cells for Y1–Y5
- Watch EBITDA recalculate (smaller, but still profitable)

**If you have 5 pilot franchisees interested (not 1):**
- Go to Assumptions sheet
- Update: Franchises (EOY) cells
- Watch franchise revenue jump

**If your VAULTED deals are larger ($500k, not $300k):**
- Go to Assumptions sheet
- Update: VAULTED Avg Transaction Size
- Watch revenue jump proportionally

**Key rule:** Everything flows from Assumptions sheet. Change it once, model updates everywhere.

---

## Pre-Pitch Checklist

### Model Completeness

- [ ] All 15 sheets created and populated
- [ ] All 8 CSV files imported
- [ ] All formulas reference Assumptions sheet
- [ ] Test: Change churn from 4% to 6%, watch EBITDA drop (confirms formulas work)
- [ ] Scenarios sheet shows Conservative / Base / Optimistic
- [ ] Monthly P&L sheet shows breakeven timing
- [ ] Cash flow sheet shows you never go negative

### Pitch Preparation

- [ ] Export P&L chart (revenue growth by year)
- [ ] Export EBITDA margin trend
- [ ] Create 1-page executive summary PDF
- [ ] Prepare talking points for each metric
- [ ] Have pilot data ready (actual customers, actual usage, actual churn)
- [ ] Prepare competitive positioning statement
- [ ] Have market sizing sources handy (TAM/SAM/SOM)

### Investor Readiness

- [ ] Model is professional looking (formatted, colored, clear)
- [ ] At least 2–3 charts included
- [ ] Google Sheets link is shareable (read-only)
- [ ] Formulas are transparent (investor can click and see)
- [ ] Key Metrics sheet is first thing they see
- [ ] Three scenarios are plausible (not just fantasy upside)
- [ ] Sensitivity analysis proves model is resilient (not fragile)

---

## Common Investor Questions (Quick Answers)

| Question | Answer | Where to Point |
|---|---|---|
| **"When do you break even?"** | Month 8 of Year 1 (Model Year 1, row "Net Change in Cash") | Cash Flow sheet |
| **"What's the exit valuation?"** | $168M (conservative), $359M (base), $568M (optimistic) | Three Scenarios sheet, Key Metrics |
| **"What's my return?"** | 256x–874x depending on scenario (on $650k seed) | Key Metrics sheet, "Seed ROI" rows |
| **"What if churn is higher?"** | Still highly profitable (Y5 EBITDA $23.5M if 6% churn) | Sensitivity Analysis sheet |
| **"What if VAULTED doesn't work?"** | Still $31M revenue from other streams (still $1.8M EBITDA) | Sensitivity Analysis sheet |
| **"Why would customers use you vs. Salesforce?"** | We're post-CRM; Salesforce is CRM. Different jobs. | Pitch deck / competitive section |
| **"How will you get 1,500 organizations?"** | 3x annual growth through referrals + content + events + partner channels | GTM Strategy section of pitch |

---

## Maintenance Schedule

### Weekly (Internal Use)

- Track: New customer signups, churn events, revenue closed
- Compare to: Model forecasts
- Identify: Anything materially off?

### Monthly (Internal Review)

- Update: Actual revenue/OPEX in P&L
- Recalculate: Year-to-date variance
- Explain: Any differences (good news or bad)
- Forecast: Updated full-year estimate

### Quarterly (Investor Update)

- Update: Model with Year-to-date actuals
- Generate: Variance report (forecast vs. actual)
- Show: Updated forecast for year and beyond
- Run: Updated scenarios if major changes

### Annually (Full Rebuild)

- Input: Year 1 full actuals
- Recalibrate: Churn, growth, pricing based on real data
- Rebuild: Years 2–5 forecast with new assumptions
- Present: Updated model + learnings

---

## File Locations in Your Vault

```
second_brain/
├── 06_Finance/
│   ├── README - Your Complete Financial Model Package.md ⭐ START HERE
│   ├── Financial Model - Investor Ready - Specification.md (detailed reference)
│   ├── Excel Model - BUILD & IMPORT GUIDE.md (build instructions)
│   ├── MASTER INDEX - All Files & Instructions.md (this file)
│   ├── Model Data - Blueprint Assumptions (Base Case).csv
│   ├── Model Data - Revenue Summary (Base Case).csv
│   ├── Model Data - OPEX Breakdown (Base Case).csv
│   ├── Model Data - Consolidated P&L (Base Case).csv
│   ├── Model Data - Cash Flow Statement (Base Case).csv
│   ├── Model Data - Key Metrics Dashboard (Base Case).csv
│   ├── Model Data - Sensitivity Analysis (Y5 EBITDA).csv
│   └── Model Data - Three Scenarios (Conservative-Base-Optimistic).csv
```

---

## Support & Questions

### If Something Doesn't Work

1. **Check the BUILD & IMPORT GUIDE** (troubleshooting section)
2. **Check the SPECIFICATION** (every line explained)
3. **Check the CSV data** (make sure imported correctly)
4. **Ask a smart advisor** (fresh eyes catch mistakes)

### If You Have a Strategic Question

1. **Read the Specification sheet** (answers 95% of questions)
2. **Run a sensitivity analysis** (what if this assumption changes?)
3. **Look at scenarios** (is this still good in downside case?)

### If You're Pitching and Get Pushed Back

1. **Show the sensitivity analysis** (model is resilient)
2. **Show the scenarios** (works in all cases)
3. **Show pilot data** (proof assumptions are grounded)
4. **Invite audit** (investor can click any formula)

---

## Success Metrics

### By End of Week 1

- ✅ Model built in Google Sheets or Excel
- ✅ All sheets populated and formulas working
- ✅ You can change one assumption and see full impact
- ✅ Model looks professional (formatted, colored, clear)

### By End of Week 2

- ✅ Model refined based on pilot data
- ✅ Executive summary created (1 page)
- ✅ Pitch talking points prepared
- ✅ Shared with 1 advisor for feedback

### By End of Month 1

- ✅ Model shared with first potential investor
- ✅ You can answer any question about assumptions
- ✅ You've pressure-tested scenarios with skeptics
- ✅ Model has been updated based on feedback

### By End of Month 2

- ✅ Multiple investors have seen model
- ✅ You're in serious conversations with 1–2 investors
- ✅ Model is become living document (updated monthly with actuals)

---

## Final Checklist (Before Sending to Investors)

- [ ] Read the README (understand overview)
- [ ] Read the BUILD GUIDE (know how to build it)
- [ ] Build the model (takes 2–3 hours)
- [ ] Test the model (change assumptions, watch cascade)
- [ ] Compare to pilot data (adjust assumptions if needed)
- [ ] Format professionally (colors, fonts, alignment)
- [ ] Add charts (at least 2–3 visualizations)
- [ ] Create executive summary (1-page PDF)
- [ ] Prepare talking points (know every line)
- [ ] Test with advisor (get feedback, iterate)
- [ ] Share with investor (ready to discuss)

---

## What Happens Next

1. **You build the model** (2–3 hours)
2. **You pitch with the model** (proves you've thought deeply)
3. **Investors ask questions** (model answers most of them)
4. **You refine based on feedback** (model becomes living doc)
5. **You close seed round** (model was part of your proof)
6. **You execute the plan** (model becomes your roadmap)

This model isn't perfect prediction. It's disciplined thinking backed by data.

That's all investors need to say yes.

---

**You're ready. Build it. Pitch it. Raise it.**

Good luck.

