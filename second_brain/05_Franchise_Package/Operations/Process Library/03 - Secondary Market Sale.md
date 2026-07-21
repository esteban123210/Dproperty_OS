---
project: Dproperty OS
title: "Process 3 — Secondary Market Sale"
type: process
status: Abstracted
owner: Esteban
process_id: process3
order: 30
feeds: [M4 Sales Playbook]
source: "Commercial Process Manual v002-26 — Proceso 3"
last_updated: 2026-07-21
tags: [process-library, secondary, sales]
---

# Process 3 — Secondary Market Sale (Resale to End User)

**Objective.** Manage the sale of existing properties to an end user, from profiling to physical handover.

**Roles used:** SA, SD, OC, PH. (See [[00 - Process Library Index|Role Map]].)

## Critical rules
- No offer is presented without SD approval of strategy and terms.
- Legal validations (property tax, buyer credit, seller mortgage) run in parallel before final approval.
- Handover always includes a detailed inventory.

## Flow

| Step | Action | Role | Expected result |
|---|---|---|---|
| 1 | Initial meeting | SA | Profile: budget, size, zone, buildings, financing, special needs |
| 2 | Build visit agenda | SA | Select properties to profile; log in CRM |
| 3 | Conduct visits | SA | Show properties; log detailed feedback in CRM |
| 4 | Prepare offer | SA | Structure offer with negotiation strategy |
| 5 | Approve offer | SD | Approve strategy + terms before presenting |
| 6 | Present to seller | SA | Send formal offer; manage counter-offer |
| 7 | Negotiate | SA + SD | SD supervises and approves counters to agreement |
| 8 | Reservation | OC | Deal sheet + reservation agreement + ID docs + payment |
| 9 | Draft contract | OC | Promise-to-buy contract with agreed terms |
| 10 | Parallel validations | OC | Property tax, buyer credit, seller mortgage `[local-market variable: legal steps]` |
| 11 | Final approval | SD | Validate final contract before signing |
| 12 | Sign + collect | OC | Coordinate signing; collect commission installment `[local variable: %]` |
| 13 | Legal closing | OC | Settlement letter, payment promise, protocol, deed `[local variable]` |
| 14 | Handover | SA + PH | Physical handover + detailed inventory |
| 15 | 30-day follow-up | SA | Satisfaction call one month after handover |

## RACI

| Task | R | A | C | I |
|---|---|---|---|---|
| Initial meeting + profile | SA | SD | — | BI |
| Agenda & visits | SA | SD | — | — |
| Log feedback in CRM | SA | BI | — | SD |
| Prepare offer | SA | SD | OC | — |
| Approve offer | SD | SD | SA | BI |
| Negotiate with seller | SA | SD | OC | BI |
| Reservation | OC | SD | SA | — |
| Draft contract | OC | SD | SA | BI |
| Legal validations | OC | OC | SD | SA |
| Final contract approval | SD | SD | OC | SA |
| Physical handover | SA | SD | PH | OC |
| Post-sale follow-up | SA | SD | OC | BI |

## KPIs
| KPI | Target / frequency |
|---|---|
| Visits → offers | > 20% |
| Offers → reservations | > 40% |
| Reservation → contract | < 10 days |
| Satisfaction (NPS) | > 80 |

## Abstraction & localization notes
- Roles mapped (AG→SA, ADM→OC, MAN→PH, DC→SD).
- Legal closing steps (deed, protocol, settlement), commission %, tax rules = local-market variables (jurisdiction-specific).
- Status: `INHERITED` — legal steps must be localized per market before publishing.
