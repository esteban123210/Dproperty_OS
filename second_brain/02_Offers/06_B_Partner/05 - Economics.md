---
project: B_RealEstate
title: "White-Label Economics"
type: finance_note
status: Baseline Created
owner: Esteban
last_updated: 2026-07-01
source: ChatGPT baseline vault package
tags: [finance]
---

> [!WARNING] Superseded — historical evidence only (reviewed 2026-09-23)
> Pre-reset finance note. The vault's finance authority is now `01_Canon/06_FINANCE/` plus the named source workbooks.
>
> **Current instead:** [[../../06_Finance/Financial Architecture and Source Models]] · [[../../06_Finance/Pricing Unit Economics and Revenue Policy]] · [[../../01_Canon/09 - Unit Economics Registry]]
>
> Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]. Preserved deliberately — old thinking is evidence, not guidance.

# White-Label Economics

## Starter

- Setup: $10,000.
- Monthly: $1,500.
- Launch-year value: around $19,000 if mid-year timing.
- Full-year recurring: $18,000.

## Growth

- Setup: $20,000.
- Monthly: $2,500.
- Full-year recurring: $30,000.

## Margin Logic

White-label can have attractive margins after setup, but implementation/support needs must be controlled.

## GHL Margin Line (added 2026-07-02)

GoHighLevel sub-accounts are resold, not passed through at cost 
(Decision 2026-07-02). Add per-client margin line to the Excel model. 
[Placeholder: $100-300/month margin per sub-account depending on tier]
## Dproperty Select Access (added 2026-08-03) — now a major economic line

White-label partners **do** get Dproperty Select access, on **external-partner-broker terms: 1.5% of sale price** (revised from 2.0%; branded franchises get 2.5%). The earlier blanket exclusion is retired. See [[../../10_Brand_and_Web/Brand Architecture]] §3.2.

**HQ economics per $300k Select unit:**

| | Partner payout | HQ retains |
|---|---|---|
| Branded franchise | 2.5% — $7,500 | $7,500 (2.5% of price) |
| **White-label** | **1.5% — $4,500** | **$10,500 (3.5% of price)** |

HQ keeps **40% more per unit** on a white-label Select sale than on a branded one — and there are 4× more white-label partners in the Year-5 plan. This is now modelled as its own revenue line (Model row 19, v0.8).

**Open — highest-leverage unknown in the whole model:** white-label **units/year** (`C32`, placeholder 25) and **Select mix** (`C33`, placeholder 8%). Every 4 points of Select mix is worth ~$147k of Year-5 EBITDA. See [[../../06_Finance/Financial Model Summary]] update 2026-08-03.
