> **⚠ SUPERSEDED FOR CURRENT INVESTOR/PRODUCT WORK — 2026-09-20.**  
> This file preserves the pre-reset franchise-first model for historical/audit purposes. Do **not** use its TAM/SAM/SOM, five-year forecast, funding ask, BluePrint transaction-spine assumptions, or “physical hub as the business” framing as current.  
> Current source: [[../02_Business_Plan/B_ Business Model Reset - 2026-09-20]] and [[../18_Ecosystem/14 - Unit Economics Registry]]

---
project: Dproperty OS
title: "Financial Model Summary"
type: finance_note
status: Baseline Created
owner: Esteban
last_updated: 2026-07-01
source: ChatGPT baseline vault package
tags: [finance]
---
---
project: Dproperty OS
title: "Financial Model Summary"
type: finance_note
status: Needs Rebuild
version: 0.5
owner: Esteban
last_updated: 2026-07-02
tags: [finance]
---

# Financial Model Summary

## STATUS WARNING

The Y1-Y5 figures below are the ChatGPT baseline, computed BEFORE the 
collected-GCI royalty decision (2026-07-02) and WITHOUT an underlying 
spreadsheet. No Excel model file currently exists. These numbers must 
not appear in the pitch deck until re-run in the Excel model.

## Baseline Conservative Case (STALE, for reference only)

- Year 5: 5 branded franchises, 20 white-label, 15 developer projects.
- Revenue ~$2.27M, EBITDA ~$601k, net ~$395k.

## Known Directional Corrections vs. Baseline

- Y1-Y2 royalty revenue: LOWER (collected-GCI lag + franchise ramp).
- New revenue line: minimum royalty floors from month 7 per franchise.
- New margin line: GHL sub-account resale margin (was pass-through).
- Y3-Y5: deferred royalty cohorts arrive on top of current-year 
  collections; steady state converges toward baseline.
- Launch fees and white-label subscriptions: unchanged timing.

## Required Model Inputs Before Build

1. Commission rate by market and sale type (5% vs 0.75% conflict). 
   Owner: Fernando/Ernesto. BLOCKS EVERYTHING.
2. Sales mix (70/30 assumption) and franchise ramp curve.
3. Deferral lag distribution (18-30 month assumption).
4. Miguel salary in/out of budget.
5. EUR/USD convention.
6. HQ support cost per franchise (currently unknown; Blunt Skeptic 
   flag from 2026-07-02 session stands).

## Source of Truth

Excel model at `09_Exports/` (to be built), linked from this note. 
This note explains logic only.

## Update (2026-07-14) — Two Financial Models Now Needed

**Note:** the Phase-1 model has since been built (`Dproperty_OS_Financial_Model.xlsx v0.7`; Y5 ~$1.59M revenue, ~$630k EBITDA). The "STALE baseline" numbers above ($2.27M/$601k) are retired — kept only for history.

This session's ecosystem reframe means finance now has **two model scopes**:
1. **Phase 1 — Franchise model (exists, v0.7):** still needs OPEX/staffing owner validation.
2. **Phase 2 — Ecosystem/hub model (NOT built):** required before [[Ecosystem Deck Outline]] can be used for any external raise. Must cover: space/membership rental, events, matchmaking fees, equity-fund returns, franchise pull-through, data monetization, and the physical-hub capex (location, lease-vs-own). Trigger to build: once Phase-1 EBITDA is proven (Year 3+) or earlier if an external hub partner conversation starts.
---

## Update (2026-08-03) — v0.8: White-Label Dproperty Select Line Added

**Source of truth:** `09_Exports/Dproperty_OS_Financial_Model.xlsx` **v0.8**. v0.7 archived as `Dproperty_OS_Financial_Model_v0.7_ARCHIVE_20260803.xlsx`.

### What changed and why

The 2026-08-03 decision granting white-label partners Dproperty Select access at **1.5% of sale price** exposed a **structural gap in v0.7**: the model had **no white-label Select revenue line at all**. Assumption cell `C14` (white-label Select payout) existed but was **never referenced by any formula** — Select revenue (Model row 18) counted **branded franchises only**. That was correct under the old rules, where white-label had no Select access. It is wrong now.

Two changes:
1. `Assumptions!C14`: **2.0% → 1.5%** (external-partner-broker terms).
2. **New revenue line — Model row 19:** *"Dproperty Select — white-label HQ retained."*

### The economics are counter-intuitive: HQ earns MORE per white-label Select unit

Because HQ retains the commission net of the partner payout, a **lower** payout means a **higher** HQ margin per unit:

| Per $300k Select unit | Payout | HQ retains |
|---|---|---|
| Branded franchise | 2.5% ($7,500) | **$7,500** |
| White-label (old, 2.0%) | 2.0% ($6,000) | $9,000 |
| **White-label (new, 1.5%)** | 1.5% ($4,500) | **$10,500** |

HQ keeps **3.5% of sale price** on a white-label Select unit vs **2.5%** on a branded one — **40% more per unit**. And by Year 5 there are **20 white-label partners vs 5 branded franchises**.

### New projection (v0.8)

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| v0.7 revenue | $86,800 | $312,056 | $659,597 | $1,055,852 | $1,594,800 |
| **+ WL Select (new)** | $10,500 | $44,100 | $110,250 | $196,875 | **$294,000** |
| **v0.8 revenue** | **$97,300** | **$356,156** | **$769,847** | **$1,252,727** | **$1,888,800** |
| v0.7 EBITDA | -$358,200 | -$197,944 | **$14,597** | $250,852 | $629,800 |
| **v0.8 EBITDA** | **-$347,700** | **-$153,844** | **$124,847** | **$447,727** | **$923,800** |
| v0.8 EBITDA margin | -357% | -43% | 16% | 36% | 49% |

**Headline: Year 3 EBITDA moves from ~$15k (dangerously thin) to ~$125k.** Breakeven is no longer knife-edge. Year 5 EBITDA rises ~47%, from ~$630k to ~$924k.

### ⚠️ The new line rests on two UNVALIDATED placeholder inputs

| Cell | Input | Placeholder | Basis |
|---|---|---|---|
| `Assumptions!C32` | White-label units / year | **25** | vs 50 for branded — assumes smaller, less mature operations |
| `Assumptions!C33` | White-label Select mix | **8%** | vs 30% for branded — white-label carries **no investment-only mandate**, so most volume is assumed non-Select |

These were chosen deliberately conservative. **They are the single highest-leverage open input in the model.**

**Year 5 sensitivity on Select mix** (units/year held at 25):

| WL Select mix | New line | Y5 EBITDA |
|---|---|---|
| 0% (no uptake) | $0 | $629,800 |
| 4% | $147,000 | $776,800 |
| **8% (model default)** | **$294,000** | **$923,800** |
| 12% | $441,000 | $1,070,800 |
| 20% | $735,000 | $1,364,800 |

Every 4 percentage points of white-label Select mix is worth ~$147k of Year-5 EBITDA. **This is the most valuable number in the model to get right**, and it is currently a guess.

### Strategic read

Select attach-rate among white-label partners is arguably now the **most important operating metric in the business** — more leveraged than franchise count. It also validates Pillar 4 of the public argument from the other direction: if partners really do lift profitability by adding Select, they will attach heavily, and HQ captures 3.5% of every unit. Worth instrumenting in [OS_NAME] from day one.

**Still open:** OPEX/staffing rows remain owner-unvalidated (they drive EBITDA more than any revenue line). The Phase-2 ecosystem model still does not exist.
