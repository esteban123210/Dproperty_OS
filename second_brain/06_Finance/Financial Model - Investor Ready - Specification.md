---
project: B_RealEstate
title: "Financial Model - Investor Ready - Specification"
type: finance_note
status: "v1.0 - Build Ready"
version: 1.0
owner: Esteban
last_updated: 2026-08-28
tags: [finance, model, investor, seed-funding]
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

# B_RealEstate Financial Model — Investor-Ready Specification

## Overview

This document specifies the complete financial model for B_RealEstate. Use this to build in Excel, Google Sheets, or any spreadsheet tool.

**Model characteristics:**
- Monthly detail for Years 1–2
- Quarterly detail for Years 3–5
- All formulas transparent and auditable
- All assumptions in one place (easy to update)
- Sensitivity analysis built in
- Three scenarios: Conservative, Base, Optimistic

---

## SHEET STRUCTURE

### Sheet 1: EXECUTIVE SUMMARY

Display only the most critical metrics for an investor in one view.

#### Section A: Key Assumptions (Input)

| Metric | Conservative | Base | Optimistic | Units |
|---|---|---|---|---|
| **Seed Capital** | 650,000 | 650,000 | 650,000 | USD |
| **Y1 BluePrint Orgs (end)** | 40 | 50 | 70 | Orgs |
| **BluePrint Avg Price (Y1)** | 280 | 300 | 320 | USD/mo |
| **Y1 VAULTED GMV** | 50,000,000 | 75,000,000 | 100,000,000 | USD |
| **Y1 Dev Projects** | 0.5 | 1 | 1.5 | Projects |
| **BluePrint Growth Rate (Y2)** | 2.5x | 3.0x | 3.5x | Multiplier |
| **Churn Rate (monthly)** | 6% | 4% | 2% | % |
| **Gross Margin (blended)** | 75% | 80% | 85% | % |
| **OPEX Growth Y2** | 1.5x | 1.73x | 2.0x | Multiplier |

#### Section B: Headline Projections (Output)

| Year | Revenue | Gross Profit | OPEX | EBITDA | EBITDA % | BluePrint Orgs | VAULTED GMV |
|---|---|---|---|---|---|---|---|
| **Y1** | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| **Y2** | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| **Y3** | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| **Y4** | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| **Y5** | Formula | Formula | Formula | Formula | Formula | Formula | Formula |

#### Section C: Key Metrics

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **CAC (Customer Acq. Cost)** | Formula | Formula | Formula | Formula | Formula |
| **LTV (Customer Lifetime Value)** | Formula | Formula | Formula | Formula | Formula |
| **LTV:CAC Ratio** | Formula | Formula | Formula | Formula | Formula |
| **Months to Payback** | Formula | Formula | Formula | Formula | Formula |
| **Rule of 40 Score** | Formula | Formula | Formula | Formula | Formula |

---

### Sheet 2: ASSUMPTIONS

This is the "control panel." Every input variable goes here. This way, an investor can change one cell and see impact across all sheets.

#### Section A: Macroeconomic Assumptions

| Assumption | Value | Notes |
|---|---|---|
| Model Currency | USD | All values in USD |
| EUR/USD Exchange Rate | 1.10 | For salary conversions |
| Inflation Rate | 3% | Applied to salaries, opex |
| Tax Rate (EBITDA → Net) | 25% | Conservative; varies by jurisdiction |
| Discount Rate (for NPV) | 12% | Investor required return |

#### Section B: BluePrint Assumptions (SaaS Subscriptions)

| Assumption | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **Orgs (End of Year)** | 50 | 150 | 350 | 850 | 1,500 | Cumulative (net of churn) |
| **New Orgs (Year)** | 50 | 110 | 220 | 550 | 750 | Gross additions |
| **Churn Rate (monthly)** | 4% | 4% | 3% | 3% | 2% | Standard for SaaS |
| **Solo % of Base** | 40% | 30% | 20% | 15% | 15% | Lower tier % |
| **Growth % of Base** | 40% | 45% | 50% | 50% | 50% | Middle tier % |
| **Pro % of Base** | 15% | 20% | 25% | 30% | 30% | Upper tier % |
| **Enterprise % of Base** | 5% | 5% | 5% | 5% | 5% | Custom tier % |
| **Solo Price** | $120 | $125 | $130 | $135 | $140 | USD/month |
| **Growth Price** | $350 | $375 | $400 | $425 | $450 | USD/month |
| **Pro Price** | $900 | $950 | $1,000 | $1,050 | $1,100 | USD/month |
| **Enterprise Price (avg)** | $2,000 | $2,200 | $2,500 | $2,800 | $3,000 | USD/month |
| **Expansion Uplift (annual)** | 10% | 15% | 20% | 20% | 20% | % of base that upgrade yearly |
| **Blueprint COGS %** | 15% | 14% | 13% | 12% | 12% | Infrastructure + minimal support |

#### Section C: Copilot / AI Assumptions

| Assumption | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **% Orgs using Copilot** | 30% | 50% | 70% | 80% | 85% | Penetration rate |
| **Avg Usage (queries/mo)** | 15 | 30 | 50 | 75 | 100 | Per using org |
| **Price per Query** | $0.10 | $0.12 | $0.15 | $0.18 | $0.20 | Above included |
| **Copilot COGS %** | 40% | 38% | 35% | 32% | 30% | API costs, infrastructure |

#### Section D: VAULTED Marketplace Assumptions

| Assumption | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **Annual GMV** | $75M | $250M | $500M | $900M | $1,500M | Gross merchandise value |
| **Transaction Commission %** | 0.75% | 0.75% | 0.75% | 0.75% | 0.75% | B_ take from deals |
| **Premium Listings (active)** | 10 | 50 | 150 | 300 | 500 | Featured listings |
| **Premium Listing Price/mo** | $250 | $300 | $350 | $400 | $450 | Optional add-on |
| **Broker Memberships (active)** | 5 | 20 | 60 | 150 | 300 | Annual subscriptions |
| **Broker Membership Price/yr** | $3,000 | $3,500 | $4,000 | $4,500 | $5,000 | Exclusive access tier |
| **Data/Analytics Subscriptions** | 0 | 10 | 30 | 80 | 150 | Annual subscriptions |
| **Data Subscription Price/yr** | $0 | $1,000 | $1,500 | $2,000 | $2,500 | Market intelligence |
| **VAULTED COGS %** | 10% | 10% | 10% | 10% | 10% | Platform hosting, payment processing |

#### Section E: Developer Programs Assumptions

| Assumption | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **Active Projects (avg)** | 1 | 3 | 6 | 10 | 15 | Concurrent projects |
| **Avg Project Duration (mo)** | 12 | 15 | 18 | 18 | 20 | Length of engagement |
| **Platform Fee/Project/mo** | $3,500 | $4,000 | $4,500 | $5,000 | $5,500 | Monthly retainer |
| **Avg Dev Project GMV** | $15M | $15M | $16M | $17M | $18M | Per project |
| **Team Sales % of Dev GMV** | 70% | 65% | 60% | 55% | 50% | Handled by dev's team |
| **Network Sales % of Dev GMV** | 30% | 35% | 40% | 45% | 50% | Closed via B_ network |
| **Team Sales Commission %** | 0.5% | 0.5% | 0.5% | 0.5% | 0.5% | Of property value |
| **Network Sales Commission %** | 2.5% | 2.5% | 2.5% | 2.5% | 2.5% | Of property value |
| **Developer COGS %** | 30% | 30% | 30% | 30% | 30% | Project mgmt, support |

#### Section F: Franchise Program Assumptions

| Assumption | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **Franchises (end of year)** | 0 | 1 | 3 | 6 | 10 | Cumulative |
| **New Franchises (year)** | 0 | 1 | 2 | 3 | 4 | Gross additions |
| **Launch Fee** | $45,000 | $45,000 | $45,000 | $45,000 | $45,000 | One-time fee |
| **Avg Franchisee GCI/year** | $87,500 | $87,500 | $87,500 | $87,500 | $87,500 | 50 units @ $350k @ 5% |
| **Royalty %** | 6% | 6% | 6% | 6% | 6% | Of local GCI |
| **Network Fund %** | 1.5% | 1.5% | 1.5% | 1.5% | 1.5% | Co-op marketing |
| **Platform Fee/mo** | $2,500 | $2,500 | $2,500 | $2,500 | $2,500 | Included in franchise |
| **Select Commission %** | 2.5% | 2.5% | 2.5% | 2.5% | 2.5% | Of sale price |
| **Avg Select Deals/Franchisee/yr** | 3 | 3 | 3 | 4 | 4 | Properties from Select |
| **Avg Select Deal Value** | $350,000 | $350,000 | $350,000 | $375,000 | $400,000 | Property value |
| **Franchise COGS %** | 25% | 25% | 25% | 25% | 25% | Support, training |

#### Section G: Academy & Services Assumptions

| Assumption | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **Certifications Sold** | 30 | 100 | 300 | 700 | 1,200 | Annual certifications |
| **Avg Certification Price** | $1,000 | $1,100 | $1,200 | $1,300 | $1,400 | Per course |
| **Custom Training Projects** | 2 | 5 | 10 | 15 | 20 | Annual projects |
| **Avg Training Project Value** | $10,000 | $15,000 | $20,000 | $25,000 | $30,000 | Per project |
| **Academy COGS %** | 35% | 35% | 35% | 35% | 35% | Content, instructors |

#### Section H: Operating Expense Assumptions

**Salaries (Annual, USD, fully loaded with benefits)**

| Role | Y1 | Y2 | Y3 | Y4 | Y5 | FTE |
|---|---|---|---|---|---|---|
| **Venture Lead / CEO** | $60,000 | $75,000 | $100,000 | $130,000 | $160,000 | 1.0 |
| **Product Manager** | $0 | $80,000 | $100,000 | $120,000 | $140,000 | 0.5 in Y2, 1.0 Y3+ |
| **Engineers** | $120,000 | $240,000 | $450,000 | $700,000 | $1,050,000 | 1.5 / 2.5 / 4 / 5 / 6 FTE |
| **Customer Success** | $50,000 | $100,000 | $200,000 | $350,000 | $500,000 | 0.5 / 1 / 2 / 3 / 4 FTE |
| **Sales & BD** | $0 | $70,000 | $120,000 | $200,000 | $300,000 | 0.5 / 1 / 1.5 / 2 FTE |
| **Finance & Admin** | $40,000 | $80,000 | $120,000 | $180,000 | $250,000 | 0.5 / 1 / 1 / 1.5 / 2 FTE |
| **Other/Contractors** | $30,000 | $50,000 | $80,000 | $100,000 | $120,000 | Variable |

**Other Operating Expenses**

| Category | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **Platform/Infrastructure** | $45,000 | $70,000 | $120,000 | $200,000 | $300,000 | Cloud, databases, tools |
| **Legal & Compliance** | $40,000 | $50,000 | $75,000 | $100,000 | $150,000 | Contracts, franchising |
| **Marketing** | $30,000 | $60,000 | $120,000 | $250,000 | $400,000 | Content, events, ads |
| **Travel & Events** | $20,000 | $40,000 | $80,000 | $150,000 | $250,000 | Conferences, customer visits |
| **Office & Misc.** | $30,000 | $40,000 | $60,000 | $100,000 | $150,000 | Rent, utilities, supplies |

---

### Sheet 3: BLUEPRINT COHORT MODEL

This sheet tracks customer acquisition, retention, and expansion by month.

#### Structure

**Rows:**
- Cohort 1 (Jan Y1), Cohort 2 (Feb Y1), ... Cohort 60 (Dec Y5)

**Columns:**
- Cohort Start Date
- Tier Distribution (% Solo / Growth / Pro / Enterprise)
- Tier Pricing (auto-links to Assumptions)
- Monthly Retention (cumulative survival %)
- Tier Upgrades (% moving up each month)
- Avg Price (weighted by tier)
- MRR (monthly recurring revenue)
- Expansion (add-ons: Copilot, etc.)
- Total Cohort MRR

#### Key Formula Logic

**MRR for Cohort N, Month M:**

```
= (New Customers in Cohort N) 
  × (Retention % at Month M)
  × (Avg Blended Price at Month M, accounting for tier upgrades)
  × (1 + Expansion Uplift %)
```

**Total BluePrint Revenue (Month):**

```
= SUM(All Cohort MRRs for that month)
```

---

### Sheet 4: VAULTED MARKETPLACE MODEL

Tracks VAULTED GMV, transactions, fees.

#### Section A: VAULTED Supply & Demand

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **Annual GMV** | $75M | $250M | $500M | $900M | $1,500M | From Assumptions |
| **Avg Transaction Size** | $300k | $300k | $300k | $320k | $350k | Property value |
| **Transactions (annual)** | 250 | 833 | 1,667 | 2,813 | 4,286 | Derived |
| **Avg Broker Participation %** | 15% | 30% | 45% | 60% | 70% | % of BluePrint using VAULTED |
| **Developers Supplying (count)** | 5 | 15 | 35 | 75 | 150 | Cumulative |
| **Inventory Value (supplied)** | $50M | $200M | $500M | $1,000M | $1,800M | Available for sale |

#### Section B: VAULTED Revenue

| Revenue Type | Y1 | Y2 | Y3 | Y4 | Y5 | Formula |
|---|---|---|---|---|---|---|
| **Transaction Commission** | Formula | Formula | Formula | Formula | Formula | GMV × 0.75% |
| **Premium Listings (count)** | 10 | 50 | 150 | 300 | 500 | From Assumptions |
| **Premium Listing Revenue** | Formula | Formula | Formula | Formula | Formula | Count × Price × 12 |
| **Broker Memberships** | Formula | Formula | Formula | Formula | Formula | Count × Price |
| **Data/Analytics** | Formula | Formula | Formula | Formula | Formula | Count × Price |
| **TOTAL VAULTED REVENUE** | Formula | Formula | Formula | Formula | Formula | Sum |

---

### Sheet 5: DEVELOPER PROGRAM MODEL

Tracks developer projects, fees, success fees.

#### Section A: Project Portfolio

| Project | Year Started | Duration (mo) | GMV | Platform Fee/mo | Team Sales % | Network Sales % | Total Annual Revenue |
|---|---|---|---|---|---|---|---|
| Project 1 | Y1 Q1 | 18 | $15M | $3,500 | 70% | 30% | Formula |
| Project 2 | Y1 Q3 | 15 | $15M | $3,500 | 70% | 30% | Formula |
| Project 3 | Y2 Q2 | 18 | $16M | $4,000 | 65% | 35% | Formula |
| ... | ... | ... | ... | ... | ... | ... | ... |

#### Section B: Developer Revenue Model (Consolidated)

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **Active Projects (avg concurrent)** | 1 | 3 | 6 | 10 | 15 | From Assumptions |
| **Platform Fees (monthly)** | Formula | Formula | Formula | Formula | Formula | Projects × Retainer |
| **Annualized Platform Fees** | Formula | Formula | Formula | Formula | Formula | × 12 |
| **Avg GMV per Project** | $15M | $15M | $16M | $17M | $18M | From Assumptions |
| **Team Sales GMV** | Formula | Formula | Formula | Formula | Formula | GMV × Team % |
| **Network Sales GMV** | Formula | Formula | Formula | Formula | Formula | GMV × Network % |
| **Team Sales Commission (0.5%)** | Formula | Formula | Formula | Formula | Formula | Team GMV × 0.5% |
| **Network Sales Commission (2.5%)** | Formula | Formula | Formula | Formula | Formula | Network GMV × 2.5% |
| **TOTAL Developer Revenue** | Formula | Formula | Formula | Formula | Formula | Platform + Commissions |

---

### Sheet 6: FRANCHISE UNIT ECONOMICS

Tracks franchisee performance and HQ revenue.

#### Section A: Per-Franchisee Economics

| Component | Assumption | Calculation | Annual Value |
|---|---|---|---|
| **Units Closed/Year** | 50 | From Assumptions | — |
| **Avg Unit Price** | $350,000 | Market assumption | — |
| **Gross Commission** | 5% | Standard rate | $87,500 |
| **Royalty (6%)** | 6% of GCI | $87,500 × 6% | $5,250 |
| **Network Fund (1.5%)** | 1.5% of GCI | $87,500 × 1.5% | $1,312 |
| **Platform Fee** | $2,500/mo | $2,500 × 12 | $30,000 |
| **Select Deals/Year** | 3 | From Assumptions | — |
| **Avg Select Deal Value** | $350,000 | From Assumptions | — |
| **Select Commission (2.5%)** | 2.5% of price | $350k × 2.5% × 3 | $26,250 |
| **TOTAL HQ REVENUE** | — | Sum above | **$62,812** |

#### Section B: Franchise Program Consolidation

| Year | Franchises (EOY) | New Launch Fees | Recurring Revenue/Franchisee | Total Franchise Revenue |
|---|---|---|---|---|
| Y1 | 0 | $0 | — | $0 |
| Y2 | 1 | $45,000 | $40,000 (ramp) | $85,000 |
| Y3 | 3 | $90,000 | $62,812 × 2 previous | $185,624 |
| Y4 | 6 | $135,000 | $62,812 × 5 previous | $479,060 |
| Y5 | 10 | $180,000 | $62,812 × 9 previous | $745,308 |

---

### Sheet 7: ACADEMY & SERVICES

| Service | Y1 | Y2 | Y3 | Y4 | Y5 | Formula |
|---|---|---|---|---|---|---|
| **Certifications (count)** | 30 | 100 | 300 | 700 | 1,200 | From Assumptions |
| **Certification Revenue** | Formula | Formula | Formula | Formula | Formula | Count × Price |
| **Training Projects (count)** | 2 | 5 | 10 | 15 | 20 | From Assumptions |
| **Training Revenue** | Formula | Formula | Formula | Formula | Formula | Count × Price |
| **TOTAL Academy Revenue** | Formula | Formula | Formula | Formula | Formula | Sum |

---

### Sheet 8: CONSOLIDATED P&L (ANNUAL)

#### Section A: Revenue Summary

| Line | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **BluePrint Subscriptions** | Formula | Formula | Formula | Formula | Formula | From BluePrint Cohort Model |
| **Copilot / AI Usage** | Formula | Formula | Formula | Formula | Formula | From Copilot Assumptions |
| **VAULTED Transactions** | Formula | Formula | Formula | Formula | Formula | From VAULTED Model |
| **VAULTED Add-ons** | Formula | Formula | Formula | Formula | Formula | Premium listings + Memberships |
| **Developer Programs** | Formula | Formula | Formula | Formula | Formula | From Developer Model |
| **Franchise Royalties + Fees** | Formula | Formula | Formula | Formula | Formula | From Franchise Model |
| **Academy & Services** | Formula | Formula | Formula | Formula | Formula | From Academy Model |
| **TOTAL REVENUE** | Formula | Formula | Formula | Formula | Formula | Sum of all lines |

#### Section B: Cost of Goods Sold (COGS)

| Line | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **Blueprint COGS** | Formula | Formula | Formula | Formula | Formula | BluePrint Revenue × COGS % |
| **Copilot COGS** | Formula | Formula | Formula | Formula | Formula | Copilot Revenue × COGS % |
| **VAULTED COGS** | Formula | Formula | Formula | Formula | Formula | VAULTED Revenue × COGS % |
| **Developer COGS** | Formula | Formula | Formula | Formula | Formula | Dev Revenue × COGS % |
| **Franchise COGS** | Formula | Formula | Formula | Formula | Formula | Franchise Revenue × COGS % |
| **Academy COGS** | Formula | Formula | Formula | Formula | Formula | Academy Revenue × COGS % |
| **TOTAL COGS** | Formula | Formula | Formula | Formula | Formula | Sum of all |

#### Section C: Gross Profit

| Line | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **Gross Profit** | Formula | Formula | Formula | Formula | Formula | Revenue - COGS |
| **Gross Margin %** | Formula | Formula | Formula | Formula | Formula | Gross Profit / Revenue |

#### Section D: Operating Expenses

| Category | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **Salaries & Benefits** | Formula | Formula | Formula | Formula | Formula | Sum from Assumptions |
| **Infrastructure** | Formula | Formula | Formula | Formula | Formula | From Assumptions |
| **Legal & Compliance** | Formula | Formula | Formula | Formula | Formula | From Assumptions |
| **Marketing** | Formula | Formula | Formula | Formula | Formula | From Assumptions |
| **Travel & Events** | Formula | Formula | Formula | Formula | Formula | From Assumptions |
| **Office & Misc.** | Formula | Formula | Formula | Formula | Formula | From Assumptions |
| **TOTAL OPEX** | Formula | Formula | Formula | Formula | Formula | Sum of all |

#### Section E: EBITDA & Net Profit

| Line | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **EBITDA (Earnings Before Tax, D&A)** | Formula | Formula | Formula | Formula | Formula | Gross Profit - OPEX |
| **EBITDA %** | Formula | Formula | Formula | Formula | Formula | EBITDA / Revenue |
| **D&A (Depreciation & Amortization)** | $20,000 | $30,000 | $40,000 | $50,000 | $60,000 | Capitalized software / equipment |
| **EBIT** | Formula | Formula | Formula | Formula | Formula | EBITDA - D&A |
| **Interest Expense** | $0 | $0 | $0 | $0 | $0 | Assuming no debt |
| **Taxes (25%)** | Formula | Formula | Formula | Formula | Formula | EBIT × 25% (if positive) |
| **Net Income** | Formula | Formula | Formula | Formula | Formula | EBIT - Taxes |
| **Net Margin %** | Formula | Formula | Formula | Formula | Formula | Net Income / Revenue |

---

### Sheet 9: MONTHLY P&L (YEAR 1–2)

| Month | Jan | Feb | Mar | ... | Dec | YTD |
|---|---|---|---|---|---|---|
| **BluePrint MRR** | Formula | Formula | Formula | ... | Formula | Sum |
| **Copilot MRR** | Formula | Formula | Formula | ... | Formula | Sum |
| **VAULTED MRR** | Formula | Formula | Formula | ... | Formula | Sum |
| **Developer MRR** | Formula | Formula | Formula | ... | Formula | Sum |
| **Other MRR** | Formula | Formula | Formula | ... | Formula | Sum |
| **TOTAL MRR** | Formula | Formula | Formula | ... | Formula | Sum |
| **Monthly COGS** | Formula | Formula | Formula | ... | Formula | Sum |
| **Gross Profit** | Formula | Formula | Formula | ... | Formula | Sum |
| **Monthly OPEX** | Formula | Formula | Formula | ... | Formula | Sum |
| **Monthly EBITDA** | Formula | Formula | Formula | ... | Formula | Sum |

**Note:** This shows precisely when cash flow breakeven occurs. Investors want to see this.

---

### Sheet 10: CASH FLOW STATEMENT

#### Section A: Operating Cash Flow

| Line | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **Net Income** | Formula | Formula | Formula | Formula | Formula |
| **Add: D&A** | Formula | Formula | Formula | Formula | Formula |
| **Add: Changes in Working Capital** | Formula | Formula | Formula | Formula | Formula |
| **Operating Cash Flow** | Formula | Formula | Formula | Formula | Formula |

#### Section B: Investing Cash Flow

| Line | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **Capitalized Software Development** | ($100,000) | ($80,000) | ($100,000) | ($150,000) | ($200,000) |
| **Equipment & IT** | ($20,000) | ($20,000) | ($30,000) | ($40,000) | ($50,000) |
| **Investing Cash Flow** | ($120,000) | ($100,000) | ($130,000) | ($190,000) | ($250,000) |

#### Section C: Financing Cash Flow

| Line | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **Seed Capital Raised** | $350,000 | $300,000 | $0 | $0 | $0 | Tranches |
| **Financing Cash Flow** | $350,000 | $300,000 | $0 | $0 | $0 |

#### Section D: Net Cash Flow

| Line | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **Operating Cash Flow** | Formula | Formula | Formula | Formula | Formula |
| **Investing Cash Flow** | Formula | Formula | Formula | Formula | Formula |
| **Financing Cash Flow** | Formula | Formula | Formula | Formula | Formula |
| **Net Change in Cash** | Formula | Formula | Formula | Formula | Formula |
| **Beginning Cash Balance** | $0 | Formula | Formula | Formula | Formula |
| **Ending Cash Balance** | Formula | Formula | Formula | Formula | Formula |

**Red flag:** Cash balance should never go negative. If it does, you need more capital or need to adjust opex.

---

### Sheet 11: KEY METRICS DASHBOARD

This is what investors look at first. Make it compelling.

#### Section A: Growth & Scale

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 | Target |
|---|---|---|---|---|---|---|
| **Revenue Growth YoY** | — | Formula | Formula | Formula | Formula | > 50% |
| **BluePrint Organizations** | 50 | 150 | 350 | 850 | 1,500 | Growth trajectory |
| **VAULTED GMV** | $75M | $250M | $500M | $900M | $1,500M | Market dominance |
| **Developer Projects (active)** | 1 | 3 | 6 | 10 | 15 | Supply scaling |
| **Franchises (cumulative)** | 0 | 1 | 3 | 6 | 10 | Quality over quantity |

#### Section B: Unit Economics

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 | Target |
|---|---|---|---|---|---|---|
| **BluePrint Avg Price (monthly)** | $300 | $350 | $380 | $420 | $450 | ARPU growth |
| **BluePrint CAC** | Formula | Formula | Formula | Formula | Formula | < $500 |
| **BluePrint LTV** | Formula | Formula | Formula | Formula | Formula | > $3,000 |
| **BluePrint Payback (months)** | Formula | Formula | Formula | Formula | Formula | < 12 |
| **Churn Rate (monthly)** | 4% | 4% | 3% | 3% | 2% | Improving |
| **Expansion Revenue %** | 0% | 10% | 30% | 45% | 55% | Growing |

#### Section C: Profitability

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 | Target |
|---|---|---|---|---|---|---|
| **Gross Margin %** | Formula | Formula | Formula | Formula | Formula | > 80% |
| **EBITDA** | Formula | Formula | Formula | Formula | Formula | Positive by Y1 |
| **EBITDA %** | Formula | Formula | Formula | Formula | Formula | > 50% by Y5 |
| **Rule of 40 Score** | Formula | Formula | Formula | Formula | Formula | > 40 |
| **Cash on Hand (end)** | Formula | Formula | Formula | Formula | Formula | Never negative |

#### Section D: Valuation Metrics

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 | Notes |
|---|---|---|---|---|---|---|
| **Implied Valuation (3x ARR)** | Formula | Formula | Formula | Formula | Formula | Conservative |
| **Implied Valuation (5x ARR)** | Formula | Formula | Formula | Formula | Formula | Moderate |
| **Implied Valuation (10x ARR)** | Formula | Formula | Formula | Formula | Formula | Optimistic |
| **Seed ROI (at 3x ARR)** | Formula | Formula | Formula | Formula | Formula | $650k → ? |
| **Seed ROI (at 5x ARR)** | Formula | Formula | Formula | Formula | Formula | $650k → ? |

---

### Sheet 12: SENSITIVITY ANALYSIS

Show investors what happens if key assumptions change.

#### Section A: One-Variable Sensitivity

**Variable 1: BluePrint Churn Rate (What if it's higher?)**

| Churn Rate | Y1 Revenue | Y2 Revenue | Y3 Revenue | Y5 EBITDA | Impact |
|---|---|---|---|---|---|
| **2% (Better)** | Formula | Formula | Formula | Formula | Upside |
| **3% (Base)** | Formula | Formula | Formula | Formula | Base case |
| **4% (Worse)** | Formula | Formula | Formula | Formula | Downside |
| **5% (Bad)** | Formula | Formula | Formula | Formula | Risk |
| **6% (Very Bad)** | Formula | Formula | Formula | Formula | Major risk |

**Variable 2: BluePrint Customer Acquisition (What if growth is slower?)**

| New Orgs per Year | Y1 Revenue | Y2 Revenue | Y3 Revenue | Y5 Revenue | Impact |
|---|---|---|---|---|---|
| **50% slower** | Formula | Formula | Formula | Formula | Downside |
| **Base (3x growth)** | Formula | Formula | Formula | Formula | Base case |
| **50% faster** | Formula | Formula | Formula | Formula | Upside |

**Variable 3: VAULTED GMV (What if marketplace scales differently?)**

| Y5 VAULTED GMV | Y1 Revenue | Y2 Revenue | Y3 Revenue | Y5 Revenue | Y5 EBITDA |
|---|---|---|---|---|---|
| **$750M (50% lower)** | Formula | Formula | Formula | Formula | Formula |
| **$1.5B (Base)** | Formula | Formula | Formula | Formula | Formula |
| **$2.25B (50% higher)** | Formula | Formula | Formula | Formula | Formula |

**Variable 4: OPEX Growth (What if costs grow faster?)**

| OPEX Growth Rate | Y1 EBITDA | Y3 EBITDA | Y5 EBITDA | Impact |
|---|---|---|---|---|
| **1.5x per year (Low)** | Formula | Formula | Formula | Upside |
| **1.73x per year (Base)** | Formula | Formula | Formula | Base case |
| **2.0x per year (High)** | Formula | Formula | Formula | Downside |

#### Section B: Two-Variable Sensitivity (Matrix)

**BluePrint Churn vs. Acquisition Speed (Y5 EBITDA)**

|  | 2x Growth | 3x Growth (Base) | 4x Growth |
|---|---|---|---|
| **2% Churn** | Formula | Formula | Formula |
| **4% Churn (Base)** | Formula | Formula | Formula |
| **6% Churn** | Formula | Formula | Formula |

---

### Sheet 13: THREE SCENARIOS

Compare Conservative, Base, and Optimistic cases side-by-side.

#### Scenario A: Conservative

**Key Changes:**
- BluePrint grows 2.5x annually (not 3x)
- Churn is 6% monthly (higher)
- VAULTED GMV is 50% lower
- OPEX grows faster (2x per year)
- Smaller franchises ramp

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **Revenue** | $1.2M | $3.2M | $6.5M | $11.2M | $16.8M |
| **EBITDA** | $280k | $800k | $2.1M | $4.5M | $7.2M |
| **EBITDA %** | 23% | 25% | 32% | 40% | 43% |
| **Exit Valuation (10x ARR)** | — | — | — | — | $168M |

#### Scenario B: Base (Most Likely)

**As specified in Assumptions sheet**

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **Revenue** | $1.5M | $4.9M | $10.7M | $21.6M | $34.2M |
| **EBITDA** | $521k | $2.75M | $6.6M | $14M | $22.5M |
| **EBITDA %** | 35% | 56% | 62% | 65% | 66% |
| **Exit Valuation (10x ARR)** | — | — | — | — | $342M |

#### Scenario C: Optimistic

**Key Changes:**
- BluePrint grows 3.5x annually
- Churn is 2% monthly (lower, sticky)
- VAULTED GMV is 50% higher
- OPEX leverages better (1.5x growth)
- Faster franchise adoption

| Metric | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| **Revenue** | $1.9M | $7.2M | $16.5M | $35.2M | $56.8M |
| **EBITDA** | $812k | $4.3M | $11.2M | $24M | $40M |
| **EBITDA %** | 43% | 60% | 68% | 68% | 70% |
| **Exit Valuation (10x ARR)** | — | — | — | — | $568M |

#### Summary: Which Case?

**Conservative:** $168M exit
**Base:** $342M exit (2x Conservative)
**Optimistic:** $568M exit (1.7x Base)

Investors should believe Base case is reasonable based on pilot data.

---

### Sheet 14: CAPITAL ALLOCATION & FUNDING

#### Section A: Use of Seed Proceeds

| Category | Amount | % of Total | Timing | Justification |
|---|---|---|---|---|
| **Product Development** | $180,000 | 28% | Months 1–24 | MVP, Release 1, Release 2 |
| **Venture Lead Salary** | €48,000 | $52,800 | Months 1–12 | CEO/Founder salary (@€4k/mo) |
| **Engineering & Tech** | $70,000 | 11% | Months 1–24 | Contractors, part-time FTE |
| **Customer Success** | $50,000 | 8% | Months 4–24 | Onboarding, support |
| **Legal & Compliance** | $85,000 | 13% | Months 1–24 | Franchise agreements, entity setup |
| **Training & Marketing** | $85,000 | 13% | Months 4–24 | Academy, launch materials, events |
| **Infrastructure & Tools** | $60,000 | 9% | Months 1–24 | Cloud, software licenses, services |
| **Contingency (5%)** | $32,400 | 5% | As-needed | Buffer for overruns |
| **TOTAL** | $615,200 | 100% | — | — |

**Note:** Slightly below $650k ask to show precision and leave buffer.

#### Section B: Funding Tranches

**Tranche 1: $350,000 (Months 1–12)**

| Use | Amount | Timing |
|---|---|---|
| Product MVP | $120,000 | Months 1–8 |
| Founder salary (8 mo) | $32,000 | Months 1–8 |
| Team (CS, part-time eng) | $80,000 | Months 4–12 |
| Legal, marketing | $60,000 | Months 1–12 |
| Contingency | $58,000 | As-needed |
| **Tranche 1 Total** | **$350,000** | — |

**Release Tranche 2 Upon:**
- ✅ BluePrint MVP live and tested with Dproperty
- ✅ 2+ pilot agencies signed
- ✅ 1 developer project initiated
- ✅ $30–50k revenue achieved
- ✅ NPS > 50 from pilots
- ✅ Product roadmap de-risked

**Tranche 2: $300,000 (Months 13–24)**

| Use | Amount | Timing |
|---|---|---|
| Product Release 1, Release 2 | $60,000 | Months 13–24 |
| Founder salary (12 mo) | $60,000 | Months 13–24 |
| Full-time engineer | $120,000 | Months 13–24 |
| Additional team (CS, BD) | $45,000 | Months 13–24 |
| Contingency | $15,000 | As-needed |
| **Tranche 2 Total** | **$300,000** | — |

#### Section C: Burn & Runway

| Metric | Y1 | Y2 |
|---|---|---|
| **Monthly Burn (avg)** | $29k | $55k |
| **Cash Received (Tranche 1)** | $350k | — |
| **Cash Received (Tranche 2)** | — | $300k |
| **Revenue (by month end)** | $0 → $50k MRR | $50k → $400k MRR |
| **Breakeven Month** | Month 7–8 | Month 4–5 (if Tranche 2 released) |
| **Cash Runway** | 12 months | Perpetual (after Tranche 2) |

**Key:** The model shows positive cash flow by mid-Year 1. Tranche 2 is insurance, not necessity.

---

### Sheet 15: WATERFALL & INVESTOR RETURN

#### Section A: Return on Seed Investment

**Seed Investment:** $650,000 at $20M post-money valuation (seed round size).

**Your ownership (assuming founder's 15% already allocated):**
- Pre-seed: Founder 15%, existing $350k funding maybe 5%, other investors TBD
- Seed: New investors get equity based on $650k contribution

**Example:**
- Pre-money valuation: $20M
- Post-money valuation: $20.65M (if seed is pure extension)
- New investor ownership: $650k / $20.65M = 3.15%

(This is simplified; actual depends on prior capital structure.)

#### Section B: Return at Different Exit Scenarios

| Exit Scenario | Exit Valuation | Exit Year | Investor Entry | Investor Return |
|---|---|---|---|---|
| **Year 3 (Optimistic)** | $100M | Y3 | $650k | 154x |
| **Year 4 (Base+)** | $200M | Y4 | $650k | 308x |
| **Year 5 (Base)** | $340M | Y5 | $650k | 523x |
| **Year 6 (Conservative)** | $168M | Y6 | $650k | 258x |

**Note:** These are gross returns. Net of carry/fees (~20%), investor realizes ~70% of gross.

---

## HOW TO BUILD THIS

### Option 1: Google Sheets (Recommended for Investors)

1. Create a new Google Sheet
2. Create 15 sheets (tabs) as described above
3. Use the formulas specified
4. Share read-only view with investors
5. Share editable version with your team

**Advantage:** Investors can comment, audit formulas in real-time, suggest scenarios.

### Option 2: Excel

1. Download this spec as CSV/structured data
2. Build sheets in Excel
3. Use Excel formulas (same logic as Google Sheets)
4. Export as PDF for investor distribution

**Advantage:** More control, offline capability.

### Option 3: Hybrid

1. Build in Google Sheets (shared with team)
2. Export monthly to Excel for formal board packages
3. Maintain one source of truth (Sheets)

---

## MAINTENANCE & UPDATING

### Monthly Review

**Update these fields:**
- Actual revenue (by stream)
- Actual OPEX (by category)
- Actual customer count (BluePrint orgs, dev projects, franchises)
- Actual churn (cohort by cohort)

**Recalculate:**
- YTD actuals vs. forecast
- Variance (why did we miss?)
- Revised full-year forecast
- Updated scenarios based on new data

### Quarterly Board Review

**Report:**
- Variance analysis (actual vs. forecast, by line item)
- Key metrics (7 north stars)
- Cohort health (retention, expansion)
- Scenario updates (is base case still likely?)
- Updated forecast for rest of year

### Annual Update

**Rebuild:**
- New year assumptions (update Assumptions sheet)
- New revenue growth assumptions (based on Year 1 data)
- New cohort models (based on actual acquisition pattern)
- Updated multi-year forecast (years 2–6)

---

## AUDITING FOR INVESTORS

Investors will ask:

**"Why is this realistic?"**
- Show pilot customer data (actual signups, actual usage, actual churn)
- Show Dproperty operating history (proof you can build real-estate businesses)
- Show industry benchmarks (CAC, LTV for SaaS, real-estate software)

**"What if churn is higher?"**
- Show sensitivity analysis (already built in Sheet 12)
- Explain why you believe churn will be low (switching costs, value delivery)

**"Can you really grow BluePrint 3x per year?"**
- Show pilot pipeline (how many orgs interested?)
- Show channel strategy (warm leads, referrals, events)
- Show competitive alternatives (why not use BoomTown or Salesforce?)

**"Why would developers use you?"**
- Show developer pain (lack of professional distribution)
- Show competitive advantage (VAULTED network + training + broker ecosystem)

**"When is this cash-flow positive?"**
- Show monthly P&L (Sheet 9)
- Highlight breakeven month
- Show cash flow statement (never negative cash)

---

## RED FLAGS FOR INVESTORS (Avoid These)

❌ **Hockey stick revenue growth** (50% month 1, 100% month 2)
- Be conservative. Real growth is lumpy and slows over time.

❌ **Unrealistic churn assumptions** (1% monthly for consumer, 0.5% for SMB SaaS)
- Real churn for new products is 4–6% initially, improves to 2–3% at scale.

❌ **Opex not growing with revenue**
- If revenue grows 3x, team costs should grow 1.5–2x (you get leverage, not magic).

❌ **No customer acquisition strategy**
- "We'll spend $5k on marketing and acquire 100 customers"
- Show actual CAC math (even if it's warm leads at $200 CAC).

❌ **Ignoring competitive risk**
- Salesforce, Zillow, and RE/MAX won't ignore a successful platform
- Show why you can't be easily displaced (moat, network, brand)

❌ **Missing cash flow**
- Even profitable companies can go bankrupt (receivables-heavy models)
- Show when cash is actually received vs. revenue recognized

---

## FINAL CHECKLIST

Before sharing with investors:

- [ ] All sheets have data for Years 1–5
- [ ] All formulas reference Assumptions sheet (easy to update)
- [ ] Monthly P&L shows actual breakeven timing
- [ ] Sensitivity analysis shows model isn't fragile
- [ ] Three scenarios (Conservative / Base / Optimistic) are all plausible
- [ ] Cash flow statement shows never negative cash (with tranches)
- [ ] Key Metrics sheet is compelling and audit-able
- [ ] Formulas are **transparent** (no black boxes)
- [ ] Investor can change one assumption and see impact across all sheets
- [ ] Unit economics are defensible (CAC < LTV, payback < 12 months)
- [ ] Exit scenarios show 100x+ potential for early investors
- [ ] Model has been pressure-tested by at least one smart advisor

**Good luck. This should be a solid investor document.**

