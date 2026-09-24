---
project: B_RealEstate
title: "Multi-Line Manual Strategy"
type: framework
status: Active Draft
version: 0.5
owner: Esteban
last_updated: 2026-07-21
tags: [franchise, white-label, developer-sales, manuals, architecture]
---

> [!INFO] Channel-scoped — verified 2026-09-23
> This folder describes the **Dproperty Franchise** channel, not the company and not a product. B_RealEstate is a product-led software company; this is one route to market.
>
> **Canonical name:** Dproperty Franchise — “the company itself” is a legacy alias.
> This is **valuable operating source material** — the process library and manuals feed BluePrint's SOP/process model and Academy. Franchise royalty/launch economics are channel-specific and require contract design plus local legal advice before external use.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# Multi-Line Manual Strategy

> **Problem.** Dproperty OS sells **three business lines** — branded franchise, white-label OS, and Developer Sales OS — but the manual set today is branded-franchise-only. Writing three separate full manual sets would guarantee drift. **Solution: one shared core + thin line-specific overlays.**

## 1. The model: shared core + overlays

```
                 ┌─────────────────────────────┐
                 │        SHARED CORE          │  (write once, all lines use)
                 │  Process Library (1–7)      │
                 │  Compliance Manual (M5)     │
                 │  Brand Manual               │
                 │  Localization Framework     │
                 │  Role Map                   │
                 └──────────────┬──────────────┘
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
 BRANDED FRANCHISE        WHITE-LABEL OS          DEVELOPER SALES OS
 (M1–M5, reference)       (overlay)               (overlay)
```

Each line **inherits** the shared core and only **overrides** what genuinely differs. An overlay is short — it says "same as core, except…".

## 2. What each line inherits vs. overrides

| Element | Branded Franchise | White-Label OS | Developer Sales OS |
|---|---|---|---|
| Process Library (1–7) | ✅ inherit | ✅ inherit (own brand) | ⚠️ partial — mainly P1, P2, reporting |
| Compliance (M5) | ✅ | ✅ | ✅ (developer-deal specifics) |
| Brand Manual | ✅ Dproperty brand | ❌ **client's own brand** | ✅ Dproperty (as sales partner) |
| Localization | ✅ | ✅ | ✅ |
| **Dproperty Select access** | ✅ (2.5% payout) | ✅ external-partner-broker terms (1.5% payout) | ❌ n/a |
| Pricing model | Launch fee + 7.5% royalty + OS fee | Setup + monthly subscription | % of **gross sales value** |
| Who operates | Franchisee + their team | Client agency's own team | **Developer's** sales team (Dproperty trains/manages) |
| Onboarding/Launch | M1 + M3 | White-label onboarding | Developer engagement plan |

## 3. Line overlays (to build)

### 3.1 Branded Franchise — the reference set
M1 Onboarding · M2 Operations · M3 Launch · M4 Sales · M5 Compliance (+ M0 HQ). Status: in progress (see [[Manuals Audit and Gap Analysis]]).

### 3.2 White-Label OS overlay `[to build]`
Governing rule: **the brand goes where there's investment potential; the system can go anywhere.** Overlay must specify:
- **Brand neutrality:** client keeps their brand; Dproperty brand assets are *not* applied. Manuals delivered are un-branded/white-labeled.
- **Dproperty Select access on external-partner-broker terms**; payout 1.5% (revised 2026-08-03 from 2.0%; the earlier blanket exclusion is retired).
- **Pricing:** setup + monthly subscription (see [[../02_Offers/06_B_Partner/03 - Offer and Pricing]]), not a royalty-on-GCI model.
- **Contract differences:** licence to the *system*, not the brand; non-copy/non-compete considerations.
- Inherits: Process Library, Compliance, Localization. Sources: [[../02_Offers/06_B_Partner/02A - Offer Guide]], [[../02_Offers/06_B_Partner/04 - Delivery and Onboarding]], [[../03_Strategy/B_ Partner Strategy]].

### 3.3 Developer Sales OS overlay `[to build]`
- **Not a franchise.** Dproperty professionalizes a developer's project sales (train the team, pipeline discipline, CRM, reporting, network clients).
- Uses mainly **Process 1 (Leads)** and **Process 2 (Preventa)** + a reporting layer; roles map to the **developer's** team + a Dproperty managing layer.
- **Priced on gross sales value** (0.5% developer-team sales; 2.5–3% Dproperty-sourced) + optional managed-desk fee (Decision 2026-07-01).
- Sources: [[../02_Offers/07_Developer_Partnerships/02A - Program Guide]], [[../03_Strategy/Developer Partnerships Strategy]], [[../02_Offers/07_Developer_Partnerships/03 - Offer and Pricing]], [[../02_Offers/07_Developer_Partnerships/04 - Deal Workflow]].

## 4. Rule for building overlays
1. Never copy the shared core into an overlay — **link** to it.
2. An overlay only documents **deltas** (what changes) + line-specific processes.
3. Deltas that touch pricing, Select, or brand must trace to the [[../00_Start_Here/Decision Log]].

## 5. Status & sequence
- Shared core: Process Library ✅, Compliance v0.5 ✅, Localization v0.5 ✅, Brand (draft), Role Map ✅.
- Branded franchise manuals: in progress (P0–P1 in the audit).
- **White-label & developer overlays: scaffolded here, to be written after the branded P0 manuals stabilize** (audit P2).
- Governed by [[Manuals System Index]].
