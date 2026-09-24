---
project: B_RealEstate
title: "Process 6 — Property Management"
type: process
status: Abstracted
owner: Esteban
process_id: process6
order: 60
feeds: [M2 Franchise Operations Manual, M5 Compliance Manual]
source: "Commercial Process Manual v002-26 — Proceso 6"
last_updated: 2026-07-21
tags: [process-library, property-management, operations]
---

> [!INFO] Channel-scoped — verified 2026-09-23
> This folder describes the **Dproperty Franchise** channel, not the company and not a product. B_RealEstate is a product-led software company; this is one route to market.
>
> **Canonical name:** Dproperty Franchise — “the company itself” is a legacy alias.
> This is **valuable operating source material** — the process library and manuals feed BluePrint's SOP/process model and Academy. Franchise royalty/launch economics are channel-specific and require contract design plus local legal advice before external use.
>
> Precedence: [[../../../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]

# Process 6 — Property Management

**Objective.** Manage leased properties: guarantee payments, preserve the asset, keep incident traceability, and stay ahead of renewals and contractual maintenance.

**Roles used:** OC, OD, PH, BI. (See [[00 - Process Library Index|Role Map]].)

> **Handoff from Process 5.** At the close of every rental, this process must receive the final file: contract, inventory, handover record, deposits, warranty pendings, expiry date, renewal terms, and maintenance frequencies — the inputs for all alerts below.

## Flow

| Step | Action | Role | Expected result |
|---|---|---|---|
| 1 | Receive rental file | OC | Validate contract, inventory, record, deposits, warranty pendings, expiry, maintenance obligations |
| 2 | Generate billing | OC | Issue monthly invoice per contract |
| 3 | Payment reminder | OC | Send reminder 5 days before due date `[local variable]` |
| 4 | Receive & record payment | OC | Confirm in system; update CRM/control sheet |
| 5 | Calculate deductions | OC | Apply common fees, management fee, authorized maintenance |
| 6 | Validate settlement | OD | Approve settlement before transfer to owner |
| 7 | Transfer to owner | OC | Transfer net; file receipt |
| 8 | Receive incidents | OC | Log tenant/owner reports, inspections, warranty pendings |
| 9 | Authorize repair | OD | Approve spend above threshold or special-authorization work `[local variable: threshold]` |
| 10 | Coordinate repair | PH | Manage approved supplier; don't touch developer-warranty items where it voids warranty |
| 11 | Document work | PH | Photos, cost, supplier, date, warranty, result → file to record |
| 12 | Monthly report | OC | To owner: rent, deductions, incidents, maintenance, property state |
| 13 | Semi-annual inspection | PH | Scheduled visit; refresh photos; flag preventive needs |
| 14 | Expiry alert | OC | Maintain calendar alert 45/60 days before expiry `[local variable]` |
| 15 | Manage renewal or exit | OC | Contact owner + tenant; confirm intent, terms, adjustments, or exit schedule |
| 16 | Maintenance calendar | OC | Keep AC + appliance maintenance schedule per each contract's frequency |
| 17 | Supplier coordination | OC | Reminder to tenant; coordinate recommended supplier; confirm date |
| 18 | File evidence & reschedule | OC | File invoice/photos/proof; schedule next alert |

## RACI

| Task | R | A | C | I |
|---|---|---|---|---|
| Receive & validate file | OC | OD | SA·Tenant Advisor, PH | SA·Listing Advisor, CA |
| Monthly billing | OC | OC | BI | SD |
| Payment recording | OC | OC | — | BI |
| Deduction calculation | OC | OD | — | BI |
| Settlement & payout to owner | OC | OD | SD | BI |
| Incident management | OC | OC | PH | OD |
| Authorize major spend | OD | OD | OC | SD |
| Repair execution & documentation | PH | OC | — | OD |
| Monthly owner report | OC | OD | BI | — |
| Semi-annual inspection | PH | OC | — | OD, BI |
| Create 45/60-day alert | OC | OD | SA·Tenant Advisor, SA·Listing Advisor | CA |
| Manage renewal/exit | OC | OD | SA·Tenant Advisor, SA·Listing Advisor | CA |
| Update maintenance calendar | OC | OD | PH | SA·Tenant Advisor, SA·Listing Advisor |
| Supplier coordination | OC | OC | PH | OD |
| File evidence & new alert | OC | OD | PH | BI |

## KPIs
| KPI | Target / frequency |
|---|---|
| On-time payments | > 95% |
| Incident response time | < 48h |
| Contracts with 45/60-day alert | 100% |
| Maintenance scheduled per contract | 100% |
| Services with filed evidence | 100% |
| Contract renewals | > 70% |

## Abstraction & localization notes
- Roles mapped (ADM→OC, DO→OD, PYE/MAN→PH, CBI→BI, DC→SD).
- Repair authorization threshold, alert windows, reminder timing, management-fee % = local-market variables.
- The owner-settlement math (rent − deductions − management fee) intersects finance; keep the **management fee** definition consistent with the franchise Pricing Model. This is *owner settlement*, not agent commission or HQ royalty — three separate flows.
- Status: `INHERITED` — reconfirm thresholds and management-fee policy with OD/Finance.
