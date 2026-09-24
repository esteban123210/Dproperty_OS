---
project: B_RealEstate
title: "Process 5 — Long-Stay Rental"
type: process
status: Abstracted
owner: Esteban
process_id: process5
order: 50
feeds: [M4 Sales Playbook, M2 Franchise Operations Manual, M5 Compliance Manual]
source: "Commercial Process Manual v002-26 — Proceso 5 (Acta 002-26, 2026-06-14)"
last_updated: 2026-07-21
tags: [process-library, rental, alquiler, sales, operations]
---

> [!INFO] Channel-scoped — verified 2026-09-23
> This folder describes the **Dproperty Franchise** channel, not the company and not a product. B_RealEstate is a product-led software company; this is one route to market.
>
> **Canonical name:** Dproperty Franchise — “the company itself” is a legacy alias.
> This is **valuable operating source material** — the process library and manuals feed BluePrint's SOP/process model and Building Blocks. Franchise royalty/launch economics are channel-specific and require contract design plus local legal advice before external use.
>
> Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# Process 5 — Long-Stay Rental

**Objective.** Manage leasing with full traceability from visit and offer through signing, handover, follow-up, and activation of administrative alerts (which hand off to Process 6).

**Roles used:** SA·Tenant Advisor, SA·Listing Advisor, OC, OD, CA, PH. (See [[00 - Process Library Index|Role Map]].)

> ⚠️ **Traceability rule.** The phone call to the owner does **not** replace formal backup. Every offer is documented by email with the profile summary, deal terms, supporting docs, and call outcome. **No progress to signing until both parties have approved the same contract version.** `[APPROVED — Acta 002-26]`

## Mandatory operating decisions

| Case | Rule | Status |
|---|---|---|
| Furnished units | Disclose at visit: two guarantee deposits + first month as the general condition. A single deposit needs prior OC authorization. `[local-market variable: deposit terms]` | APPROVED (Acta 002-26) |
| Special profiles | Reinforced-validation profiles (e.g. lawyers, public figures) require extra documentation and **written CA sign-off** before signing. | APPROVED |
| Contract review route | Standard: owner → tenant. Fast: tenant → owner. Both parties must approve exactly the same version. | APPROVED |
| Developer warranties | Pending warranty items are explained from the visit, repeated at handover, and logged **without intervening** where that could void the warranty. | APPROVED |

## Flow

| Step | Action | Role | Expected result |
|---|---|---|---|
| 1 | Receive & register lead | SA·Tenant Advisor | CRM: client, unit, budget, dates, source, listing advisor, special needs |
| 2 | Qualify & initial docs | SA·Tenant Advisor | Validate term, income, move-in date, references; flag reinforced-validation profiles |
| 3 | Visit & mandatory disclosures | SA·Tenant Advisor | Furnished: disclose 2 deposits + first month. New units: explain warranty pendings |
| 4 | Receive & structure offer | SA·Tenant Advisor | Document amount, term, start, deposits, furniture, special requests |
| 5 | Phone presentation to owner | SA·Tenant Advisor | Present verbally; log call outcome, notes, counter-offers |
| 6 | Inform Listing Advisor | SA·Tenant Advisor → SA·Listing Advisor | Notify so they can support profile/negotiation |
| 7 | Formal traceability email | SA·Tenant Advisor | Send OC (cc CA, Listing Advisor): docs, profile, terms, call outcome |
| 8 | Approve profile | CA | Approve/reject; for special profiles, written sign-off + extra docs |
| 9 | Formal offer to owner | OC | Send formal offer, profile summary, supporting docs, draft contract |
| 10 | Define review route | OD + OC | Standard (owner→tenant) or Fast (tenant→owner) |
| 11 | Contract version control | OC | Consolidate comments; confirm both parties approve the same final version |
| 12 | Signing & payments | OC | Coordinate signing; confirm first month + deposits; any furnished-deposit exception pre-authorized |
| 13 | Third-party renovation record | OC | When applicable, request record of floors, finishes, equipment, fixed furniture, improvements, warranties, suppliers |
| 14 | Prep, inspection & inventory | PH | Prepare unit; build inventory from renovation record, photos, real condition |
| 15 | Log warranties & pendings | PH + OC | Record developer pendings; don't intervene where it voids warranty; note timelines depend on developer |
| 16 | Handover | SA·Tenant Advisor + PH | Keys, inventory, signed record; restate warranty pendings + follow-up channels |
| 17 | Activate admin alerts | OC | Create contract alerts at 45/60 days + AC/appliance maintenance calendar. Connect to Process 6 `[local variable: alert windows]` |
| 18 | Post-handover follow-up | SA·Tenant Advisor + OC | Contact at 7 and 30 days; log incidents; formal handoff to recurring management |

## RACI

| Task | R | A | C | I |
|---|---|---|---|---|
| Receive, register & qualify | SA·Tenant Advisor | OD | OC | CA |
| Visit & mandatory disclosures | SA·Tenant Advisor | OD | SA·Listing Advisor | OC |
| Phone presentation of offer | SA·Tenant Advisor | OD | SA·Listing Advisor | OC |
| Inform Listing Advisor | SA·Tenant Advisor | OD | SA·Listing Advisor | OC |
| Formal email with backup | SA·Tenant Advisor | OD | OC, SA·Listing Advisor | CA |
| Approve profile | OC | CA | SA·Tenant Advisor, OD | SA·Listing Advisor |
| Special-profile documentation | OC | CA | SA·Tenant Advisor, OD | SA·Listing Advisor |
| Furnished single-deposit exception | OC | OD | SA·Tenant Advisor, CA | SA·Listing Advisor |
| Send formal offer + draft | OC | OD | CA, SA·Tenant Advisor, SA·Listing Advisor | — |
| Define contract review route | OC | OD | SA·Tenant Advisor, SA·Listing Advisor | CA |
| Version control & bilateral approval | OC | OD | SA·Tenant Advisor | SA·Listing Advisor, CA |
| Signing & payment confirmation | OC | OD | SA·Tenant Advisor | SA·Listing Advisor, CA |
| Request renovation record | OC | OD | SA·Listing Advisor, PH | SA·Tenant Advisor |
| Prep & inventory | PH | OC | SA·Tenant Advisor, SA·Listing Advisor | OD |
| Log warranties & pendings | PH | OD | OC, SA·Tenant Advisor | SA·Listing Advisor, CA |
| Handover | SA·Tenant Advisor + PH | OD | OC | SA·Listing Advisor, CA |
| Contract & maintenance alerts | OC | OD | PH | SA·Tenant Advisor, SA·Listing Advisor, CA |
| Post-handover follow-up | SA·Tenant Advisor | OD | OC | SA·Listing Advisor, CA |

## KPIs
| KPI | Target / frequency |
|---|---|
| Offers with formal backup | 100% |
| Special profiles with written approval | 100% |
| Contracts with same approved version | 100% |
| Handovers with signed inventory | 100% |
| Alerts created at close | 100% |
| Follow-up at 7 & 30 days | ≥ 95% |

## Abstraction & localization notes
- Roles mapped: ATI→SA·Tenant Advisor, ACO→SA·Listing Advisor, ADM (Silvia/Maria Isabel)→OC, DO→OD, LA (Luz Adriana)→CA, PYE→PH. Personal names removed.
- Deposit structure, alert windows (45/60d), AC/appliance maintenance = local-market variables.
- This process is the **most validated** in the source (Acta 002-26); most rules tagged `APPROVED`. Still: re-confirm with the accountable OD/CA before publishing as franchise policy.
- **Handoff:** Step 17–18 feed [[00 - Process Library Index|Process 6 — Property Management]] (next batch).
