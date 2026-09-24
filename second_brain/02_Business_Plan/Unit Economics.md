---
project: B_RealEstate
title: "Unit Economics"
type: business_plan_note
status: In Review
version: 0.7
owner: Esteban
last_updated: 2026-07-05
source: Updated per 2026-07-05 commission-waterfall clarification
supersedes: v0.6 (2026-07-04)
tags: [business-plan, unit-economics]
---

> [!WARNING] Superseded — historical evidence only (reviewed 2026-09-23)
> Pre-reset unit economics blending channel and software revenue.
>
> **Current instead:** [[../18_Ecosystem/14 - Unit Economics Registry]] and [[../19_Canonical_B_RealEstate/06_FINANCE/PRICING_UNIT_ECONOMICS_AND_REVENUE_POLICY]]
>
> Precedence: [[../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]. Preserved deliberately — old thinking is evidence, not guidance.

> **⚠ SUPERSEDED FOR CURRENT INVESTOR/PRODUCT WORK — 2026-09-20.**  
> This file preserves the pre-reset franchise-first model for historical/audit purposes. Do **not** use its TAM/SAM/SOM, five-year forecast, funding ask, BluePrint transaction-spine assumptions, or “physical hub as the business” framing as current.  
> Current source: [[../18_Ecosystem/14 - Unit Economics Registry]]

# Unit Economics

> **Revision 2026-07-05:** Added the commission waterfall. A 5% commission is charged;
> HQ shares 50/50 with external advisors; 2.5% enters the company. Royalty is charged on
> **gross-into-company (the 2.5%)**, not on franchise net — so a franchise cannot lower
> royalty by inflating agent pay. Dproperty Select remains separate (fixed % of price).

## Base Sale

- Unit price: $300,000.
- Commission charged: 5% = $15,000.

## Local Franchise Deal — Commission Waterfall

```
Gross commission (5%) ................. $15,000
  Less external advisors (50/50) ...... $7,500   (co-broke, shared out)
Into the company (2.5%) ............... $7,500   ← ROYALTY BASE
  Seller (35%) ........................ $2,625
  Sales director (10%) ................ $750
  Franchise net (55%) ................. $4,125   (franchise take-home)
```

**HQ take on a local sale** (charged on the $7,500 into-company, not on net):

- Royalty (6%): $450.
- Network & Brand Fund (1.5%): $112.50.
- **HQ total per local unit: ~$562.**

**Why on gross-into-company, not net:** if royalty were charged on the $4,125 net, a franchise could inflate seller/director pay to shrink net and pay less royalty every month. Charging on the $7,500 that enters the company makes HQ revenue independent of the franchise's internal agent-comp choices.

**Note:** the 50/50 external-advisor split is the standard modelling assumption. On deals with no external advisor, the full 5% ($15,000) enters the company and the royalty base is higher; this is an editable input (`external_advisor_share`) in the model.

## Dproperty Select Sale (separate structure — unchanged)

Projection assumption: HQ signs the select project at 5% total commission = $15,000 on a $300k unit. The originator earns a **fixed % of sale price**:

**Branded franchise:** 2.5% × $300,000 = **$7,500** to franchisee; HQ retains **$7,500**.
**White-label partner:** 1.5% × $300,000 = **$4,500** to partner; HQ retains **$10,500** (external-partner-broker terms, revised 2026-08-03 from 2.0%).

Dproperty Select does **not** run through the seller/director waterfall or the external-advisor split — it is HQ-controlled and priced separately. Upside above 5% is retained by HQ.

## Franchise Entry

- Launch fee (founding): $30,000; after 5 successful franchises: $40,000.

## Interpretation

Local sales are thinner for HQ per unit ($562) than the old headline suggested, because most of the commission is shared with co-brokers and paid out to the selling team. The scalable HQ economics come from **recurring** lines (OS fees, white-label subscriptions), **Dproperty Select** (HQ keeps $7,500/unit), and **developer revenue** — not from local royalty. Local royalty is a modest, un-gameable recurring layer on top.
