---
project: B_RealEstate
title: "Process 2 — Preventa (Lista Cero)"
type: process
status: Abstracted
owner: Esteban
process_id: process2
order: 20
feeds: [M4 Sales Playbook, M2 Franchise Operations Manual]
source: "Commercial Process Manual v002-26 — Proceso 2"
last_updated: 2026-07-21
tags: [process-library, preventa, sales]
---

> [!INFO] Channel-scoped — verified 2026-09-23
> This folder describes the **Dproperty Franchise** channel, not the company and not a product. B_RealEstate is a product-led software company; this is one route to market.
>
> **Canonical name:** Dproperty Franchise — “the company itself” is a legacy alias.
> This is **valuable operating source material** — the process library and manuals feed BluePrint's SOP/process model and Academy. Franchise royalty/launch economics are channel-specific and require contract design plus local legal advice before external use.
>
> Precedence: [[../../../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]

# Process 2 — Preventa (Lista Cero / Pre-Construction)

**Objective.** Manage the sale of off-plan units directly with developers, from reservation to commission collection.

**Roles used:** SA, SD, OC. (See [[00 - Process Library Index|Role Map]].)

## Critical rules
- No reservation is sent to the developer without SD approval.
- The client file must be complete before contract issuance.
- Commission is collected against the developer per the developer agreement. `[commission-layer note: developer-paid; keep separate from franchise royalty]`

## Flow

| Step | Action | Role | Expected result |
|---|---|---|---|
| 1 | Initial meeting | SA | Profile: total budget, available, monthly, motivation |
| 2 | Present project | SA | Show projects + ROI table; log feedback in CRM |
| 3 | Validate interest | SD | Confirm project fits client profile |
| 4 | Reservation | SA | Receive reservation payment + complete deal sheet `[local variable: reservation amount]` |
| 5 | Approve reservation | SD | Validate terms, authorize sending to developer |
| 6 | Notify developer | OC | Send project, unit, client, price, ID |
| 7 | Request documents | OC | Due diligence, statements, employment letter from client `[local variable: KYC set]` |
| 8 | Draft contract | OC | Dproperty-format contract or receive developer's |
| 9 | Approve contract | SD | Validate terms, approve final version |
| 10 | Sign contract | OC | Coordinate signing (digital/in person), all parties |
| 11 | Initial payment | OC | Client pays developer down-payment; confirm & file `[local variable: % and payee]` |
| 12 | Collect commission | OC | Proforma invoice to developer; manage collection |
| 13 | Update CRM | OC | Record in CRM + internal control sheet |
| 14 | Post-sale | OC | Follow payments, queries, client communication |

## RACI

| Task | R | A | C | I |
|---|---|---|---|---|
| Initial meeting + profile | SA | SD | — | BI |
| Project presentation + ROI | SA | SD | — | — |
| Validate interest | SD | SD | SA | BI |
| Receive reservation | SA | SD | — | OC |
| Approve reservation | SD | SD | SA | OC |
| Notify developer | OC | OC | SD | SA |
| Request client docs | OC | OC | SA | — |
| Draft contract | OC | SD | SA | BI |
| Approve contract | SD | SD | OC | SA |
| Coordinate signing | OC | SD | — | SA |
| Confirm down-payment | OC | OC | SD | SA, BI |
| Manage commission collection | OC | SD | — | SA |
| Update CRM | OC | BI | — | SD |
| Post-sale follow-up | OC | SD | SA | BI |

## KPIs
| KPI | Target / frequency |
|---|---|
| Meeting → reservation | > 30% |
| Reservation → contract | < 15 days |
| Complete files | 100% |
| Real vs projected ROI | ±10% |

## Abstraction & localization notes
- Roles mapped (AG→SA, ADM/SEC→OC, DC→SD).
- Reservation amount, down-payment %, KYC document set = local-market variables.
- Developer commission is **developer-paid** and separate from the franchise royalty waterfall — do not conflate. `[commission-layer]`
- Status: `INHERITED` — confirm reservation/payment figures with SD and Finance.
