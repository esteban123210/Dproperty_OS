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