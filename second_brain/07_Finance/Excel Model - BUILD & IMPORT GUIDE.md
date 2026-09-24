---
project: B_RealEstate
title: "Excel Financial Model - Build & Import Guide"
type: finance_note
status: "v1.0 - Ready"
version: 1.0
owner: Esteban
last_updated: 2026-08-28
tags: [finance, model, excel, guide]
---

> [!WARNING] Superseded — historical evidence only (reviewed 2026-09-23)
> Pre-reset finance note. The vault's finance authority is now `19_Canonical_B_RealEstate/06_FINANCE/` plus the named source workbooks.
>
> **Current instead:** [[../19_Canonical_B_RealEstate/06_FINANCE/FINANCIAL_ARCHITECTURE_AND_SOURCE_MODELS]] · [[../19_Canonical_B_RealEstate/06_FINANCE/PRICING_UNIT_ECONOMICS_AND_REVENUE_POLICY]] · [[../18_Ecosystem/14 - Unit Economics Registry]]
>
> Precedence: [[../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]. Preserved deliberately — old thinking is evidence, not guidance.

# B_RealEstate Excel Model — Build & Import Guide

## Overview

You have everything you need to build a professional investor-ready financial model in 2–3 hours.

**Files you have:**
1. `Financial Model - Investor Ready - Specification.md` — Complete sheet-by-sheet blueprint
2. `Model Data - Blueprint Assumptions (Base Case).csv` — All BluePrint inputs
3. `Model Data - Revenue Summary (Base Case).csv` — Revenue by stream
4. `Model Data - OPEX Breakdown (Base Case).csv` — Operating expenses
5. `Model Data - Consolidated P&L (Base Case).csv` — Full P&L statement
6. `Model Data - Cash Flow Statement (Base Case).csv` — Cash flow
7. `Model Data - Key Metrics Dashboard (Base Case).csv` — KPI dashboard
8. `Model Data - Sensitivity Analysis (Y5 EBITDA).csv` — Sensitivity testing
9. `Model Data - Three Scenarios (Conservative-Base-Optimistic).csv` — Scenario analysis

---

## OPTION 1: Google Sheets (Recommended for Investors)

### Why Google Sheets?
- Investors can access from anywhere
- Real-time collaboration (you update, they see changes)
- Easy to share read-only view
- Formula transparency (they can audit every cell)
- Mobile-friendly

### Step 1: Create the Base Sheet Structure

1. Go to **Google Drive** → **Create** → **Google Sheet**
2. Rename it: "B_RealEstate Financial Model (Base Case)"
3. Create 15 sheets (tabs) by clicking the `+` at bottom:
   - Executive Summary
   - Assumptions
   - BluePrint Cohort Model
   - VAULTED Marketplace
   - Developer Programs
   - Franchise Economics
   - Academy & Services
   - Consolidated P&L
   - Monthly P&L (Y1-2)
   - Cash Flow Statement
   - Key Metrics Dashboard
   - Sensitivity Analysis
   - Three Scenarios
   - Capital Allocation
   - Waterfall & Returns

### Step 2: Import CSV Data

**For each CSV file:**

1. Open the CSV file in a text editor (or keep it in your downloads)
2. Copy all content (Ctrl+A, Ctrl+C)
3. Go to your Google Sheet → go to the matching sheet tab
4. Click cell A1
5. Paste (Ctrl+V)
6. Let Google Sheets auto-format the data
7. Clean up: adjust column widths, freeze header row

**Order to import:**
1. Import `Model Data - Blueprint Assumptions (Base Case).csv` → Assumptions sheet
2. Import `Model Data - Revenue Summary (Base Case).csv` → Consolidated P&L sheet (use as reference)
3. Import `Model Data - OPEX Breakdown (Base Case).csv` → create "OPEX Detail" sheet
4. Import `Model Data - Consolidated P&L (Base Case).csv` → Consolidated P&L sheet
5. Import `Model Data - Cash Flow Statement (Base Case).csv` → Cash Flow Statement sheet
6. Import `Model Data - Key Metrics Dashboard (Base Case).csv` → Key Metrics Dashboard sheet
7. Import `Model Data - Sensitivity Analysis (Y5 EBITDA).csv` → Sensitivity Analysis sheet
8. Import `Model Data - Three Scenarios (Conservative-Base-Optimistic).csv` → Three Scenarios sheet

### Step 3: Create Formulas

Now link everything together.

**Executive Summary sheet:**

```
Cell A1: "B_RealEstate Financial Model"
Cell A2: "Base Case Scenario"

Cell A4: "Revenue Projections"
Cell A5: "Year 1"
Cell B5: =SUM('Consolidated P&L'!B5:B11)  [or direct reference to revenue line]

Cell A10: "EBITDA Projections"
Cell B10: ='Consolidated P&L'!B24  [link to EBITDA line]
```

**Assumptions sheet:**

Already imported. These are your control cells. Change these to update all projections.

**Consolidated P&L sheet:**

This drives everything. Example formulas:

```
BluePrint Revenue (Y1):
=('Assumptions'!B2 * 'Assumptions'!B8 * 12) + 
 ('Assumptions'!B2 * 'Assumptions'!B9 * 12) +
 ('Assumptions'!B2 * 'Assumptions'!B10 * 12) +
 ('Assumptions'!B2 * 'Assumptions'!B11 * 12)

Or simpler: =SUM(range of revenue lines)

COGS:
=BluePrint Revenue * COGS %
=Formula that references Assumptions sheet COGS %

Gross Profit:
=Total Revenue - Total COGS

EBITDA:
=Gross Profit - OPEX
```

### Step 4: Add Scenario Tabs

Create two more sheets:
- **Conservative Case** (copy Assumptions, change key inputs per spec)
- **Optimistic Case** (copy Assumptions, change key inputs per spec)

Each scenario should have its own Revenue/P&L/Cash Flow calculations.

**Example: Conservative Assumptions sheet**

Copy all of Assumptions sheet, then change:
- BluePrint Growth Rate: 2.5x (instead of 3x)
- Churn Rate: 6% (instead of 4%)
- VAULTED GMV Y5: $750M (instead of $1.5B)
- OPEX Growth: 2.0x (instead of 1.73x)

All P&L calculations auto-update based on new assumptions.

### Step 5: Share & Lock

1. Click **Share** (top right)
2. Add investor email
3. Set to **Viewer** (read-only)
4. Uncheck "Notify people" (if you don't want email)

**To prevent accidental changes:**
- Select all sheets
- **Tools** → **Protect sheets** → Require viewer authentication

---

## OPTION 2: Excel (Advanced)

### Why Excel?
- More powerful formulas (data tables, pivot tables)
- Better formatting options
- Offline capability
- Can export to PDF for formal board packages

### Step 1: Create the Workbook

1. Open Excel
2. Save as: `B_RealEstate_Financial_Model_BaseCase.xlsx`
3. Create 15 sheets (right-click sheet tab → Insert)

### Step 2: Import CSV Data

**For each CSV:**

1. In Excel, go to **Data** → **Get External Data** → **From Text**
2. Select the CSV file
3. Click **Import**
4. Excel auto-detects delimiters and data types
5. Click **OK** to paste into sheet

**Alternatively (manual):**

1. Open CSV in notepad
2. Copy all content
3. Go to Excel sheet, cell A1
4. Paste (Ctrl+V)

### Step 3: Create Formulas

Use same logic as Google Sheets, but with Excel functions:

```
=SUMIF() for conditional sums
=VLOOKUP() to reference Assumptions sheet
=IF() for scenario switches
=INDEX/MATCH for more complex lookups
```

**Example formula (Excel):**

```
BluePrint MRR (Month 1):
=SUM(D5:D8)*12/12  [Average price × org count × 12 months ÷ 12 months in year = monthly]

Or more sophisticated:
=SUMPRODUCT('Assumptions'!B2:B5, 'Assumptions'!B8:B11)
[This multiplies orgs × tier percentages × prices]
```

### Step 4: Add Charts & Dashboards

**Create visualizations for investors:**

1. **Revenue Growth Chart** (line graph)
   - X-axis: Year 1–5
   - Y-axis: Revenue
   - Legend: By revenue stream

2. **EBITDA Margin Trend** (column chart)
   - X-axis: Year
   - Y-axis: EBITDA %

3. **Cash Flow Waterfall**
   - Shows: Opening cash → Operating CF → Investing CF → Financing CF → Closing cash

4. **Unit Economics Scorecard**
   - CAC, LTV, Payback, Churn, Expansion % in tiles

### Step 5: Protect & Format

**Format for investors:**
- Use professional color scheme (blues, whites, light grays)
- Bold headers
- Currency formatting ($)
- Percentage formatting (%)
- Freeze top rows and left columns

**Protect sheets:**
- **Review** → **Protect Sheet** → Set password
- Allow: Select locked cells, select unlocked cells
- Lock: All cells except input cells (Assumptions)

---

## OPTION 3: Hybrid (Google Sheets + Excel Export)

### Best of Both Worlds

1. **Build in Google Sheets** (real-time, shareable)
2. **Export to Excel** monthly for board packages
3. **Maintain one source of truth** (Sheets)

**Workflow:**

1. Create model in Google Sheets
2. Update Assumptions each month
3. Export as PDF for formal board presentation
4. Keep Google Sheets link for investor access/audit

---

## QUICK SETUP (2-Hour Build)

If you're in a hurry:

### Minimum Viable Model (Just the Essentials)

**Create 5 sheets only:**

1. **Assumptions** → Import CSV
2. **P&L** → Import CSV + add formulas to link to Assumptions
3. **Cash Flow** → Import CSV
4. **Key Metrics** → Import CSV + add linking formulas
5. **Scenarios** → Import Three Scenarios CSV

**Add one chart:**
- Revenue by year (bar chart, all scenarios)

**Share:**
- Invite investor as Viewer in Google Sheets
- Export one-pager PDF summary

**Time: ~2 hours. Result: Investable.**

---

## MAINTAINING THE MODEL

### Monthly Update Cadence

**1st of each month:**
1. Update actual revenue (by stream) in P&L
2. Update actual OPEX (by category) in P&L
3. Update actual customer counts (BluePrint orgs, dev projects, franchises)
4. Recalculate year-to-date actuals vs. forecast
5. Identify variances (why did we miss?)

**Example variance explanation:**

```
BluePrint Revenue:
- Forecast: $50k
- Actual: $35k
- Variance: -$15k (-30%)
- Reason: 1 customer churned, slower new customer acquisition
- Revised forecast: $45k next month
```

**Weekly dashboard (internal):**
- New customers signed
- Churn events
- Revenue recognized
- Burn rate (monthly)

### Quarterly Board Presentation

**Include in deck:**
1. Actual vs. Forecast variance (all line items)
2. Key metrics dashboard (actual)
3. Updated full-year forecast
4. Cohort analysis (retention by acquisition month)
5. Scenario update (are we tracking Conservative/Base/Optimistic?)

**Format:**
- 1-page summary (headline metrics)
- 5-page detail (variance analysis, updated forecast)
- Optional: Live Google Sheets for investor questions

### Annual Rebuild

**End of Year 1:**
1. Input Year 1 actual data
2. Update Year 2–5 assumptions based on actual performance
3. Rebuild cohort model with real customer data
4. Adjust churn/LTV estimates
5. Create updated forecast (Years 2–6)
6. Present to board with learnings

---

## COMMON INVESTOR QUESTIONS (Answered by Model)

### "When do you break even?"

**Answer:** Go to Cash Flow sheet → find when "Ending Cash Balance" stops declining → that's cash breakeven.

Expected: Month 7–8 of Year 1.

### "What if churn is 2x higher?"

**Answer:** Go to Sensitivity Analysis sheet → BluePrint Churn Rate section → see Y5 EBITDA under "6%" → shows impact.

Expected: Y5 EBITDA drops ~28% but still highly profitable.

### "Can you really grow 3x annually?"

**Answer:** Go to Assumptions sheet → show CAC math:
- CAC: $300–500 (mostly warm leads, no paid ads)
- LTV: $4.5k–8k (low churn + strong retention)
- So cost to acquire is tiny relative to lifetime value
- → Growth is constrained by GTM execution, not unit economics

### "What's your exit timeline?"

**Answer:** Three Scenarios sheet shows:
- Year 3: ~$100M valuation (good exit)
- Year 4: ~$200M valuation (strong exit)
- Year 5: ~$340M valuation (great exit)
- Investor should see 100x–500x return

### "What are your key risks?"

**Answer:** Sensitivity Analysis sheet shows:
- **Biggest risk:** BluePrint churn > 5% (reduces profitability 30%)
- **Mitigation:** NPS > 60, measure churn weekly, focus on retention
- **Second risk:** VAULTED doesn't scale (reduces revenue 15–20%)
- **Mitigation:** Curate supply first (Dproperty Select), build demand organically

---

## SHARING WITH INVESTORS

### What to Send

**Option A: One-Pager + Model**
- Executive Summary PDF (1 page)
- Link to Google Sheets model (read-only)
- Allows investor to explore + ask questions

**Option B: Formal Deck + Model**
- Pitch deck (10–15 slides with financial summary)
- Detailed model in Google Sheets
- Backup: PDF of key sheets

**Option C: Excel Package**
- All three scenarios in one Excel file
- Protected sheets (no accidental changes)
- Summary dashboard (first sheet)

### Presentation Order

1. **Show the Executive Summary first** (Key Metrics sheet)
   - "Here's what success looks like"

2. **Show the Path to Profitability** (Consolidated P&L sheet)
   - "We're EBITDA positive by Month 8 of Year 1"

3. **Show the Unit Economics** (Key Metrics sheet)
   - "CAC is $300, LTV is $4.5k, payback is 10 months"

4. **Show the Sensitivity Analysis** (Sensitivity sheet)
   - "Here's what happens if our assumptions are wrong"

5. **Show the Scenarios** (Three Scenarios sheet)
   - "Even in downside case, we're profitable and defensible"

6. **Answer Questions** (Invite them to dig into formulas)
   - "Click any cell, see exactly how we calculated it"

---

## TROUBLESHOOTING

### Formula Not Working

**Check:**
1. Is the cell formatted as a number? (Format → Number)
2. Are you referencing the right sheet? (Sheet!Cell)
3. Are there spaces in cell references? (=A1 not = A 1)

**Example:**
```
Wrong: =Assumptions.B2  (period instead of exclamation)
Right: =Assumptions!B2
```

### Data Not Updating

**Check:**
1. Are formulas using cell references or hard-coded numbers?
   - Wrong: =1500 * 12
   - Right: =Assumptions!B2 * 12
2. Is the dependent formula using the right range?
3. Did you hit F9 to recalculate? (Excel sometimes doesn't auto-update)

### Scenario Not Reflecting

**Check:**
1. Did you copy Assumptions sheet and change inputs?
2. Did the P&L formulas reference the new Assumptions tab?
3. Try: Rebuild the formula using the new tab reference

---

## FINAL CHECKLIST (Before Sharing with Investors)

- [ ] All sheets populated (no blank tabs)
- [ ] All formulas reference Assumptions sheet (easy to scenario)
- [ ] Assumptions are labeled clearly (what does this number mean?)
- [ ] Monthly P&L shows actual cash breakeven timing
- [ ] Sensitivity analysis shows model isn't fragile
- [ ] Three scenarios are all plausible (not just upside fantasy)
- [ ] Cash flow never goes negative (with seed tranches)
- [ ] Key Metrics are compelling (Rule of 40, LTV:CAC, etc.)
- [ ] Formulas are transparent (investor can click and see)
- [ ] Professional formatting (colors, fonts, alignment)
- [ ] At least one chart (revenue or EBITDA growth)
- [ ] Investor ROI scenarios show 100x+ potential

**Once checked:**
→ Share with investor
→ Be prepared to defend assumptions
→ Show pilot data proving reasonability
→ Invite questions on formulas

---

## NEXT STEPS

1. **Choose your platform** (Google Sheets recommended)
2. **Build in 2–3 hours** using this guide
3. **Test with a trusted advisor** (does the model make sense?)
4. **Prepare your pitch** using the model as visual support
5. **Share with investors** as your financial proof

The model itself is 50% of the work. The other 50% is the story (why this market, why now, why you). But numbers back up the story.

Good luck. This model should get you to "serious conversation" with investors.

