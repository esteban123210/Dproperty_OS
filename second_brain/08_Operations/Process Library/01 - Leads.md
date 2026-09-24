---
project: B_RealEstate
title: "Process 1 — Leads"
type: process
status: Abstracted
owner: Esteban
process_id: process1
order: 10
feeds: [M4 Sales Playbook, M2 Franchise Operations Manual]
source: "Commercial Process Manual v002-26 — Proceso 1"
last_updated: 2026-07-21
tags: [process-library, leads, sales]
---

> [!INFO] Channel-scoped — verified 2026-09-23
> This folder describes the **Dproperty Franchise** channel, not the company and not a product. B_RealEstate is a product-led software company; this is one route to market.
>
> **Canonical name:** Dproperty Franchise — “the company itself” is a legacy alias.
> This is **valuable operating source material** — the process library and manuals feed BluePrint's SOP/process model and Academy. Franchise royalty/launch economics are channel-specific and require contract design plus local legal advice before external use.
>
> Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# Process 1 — Leads (Registration & Management)

**Objective.** Standardize capture, qualification, and follow-up of leads from events, digital channels, and referrals — every lead registered, owned, and worked on time.

**Roles used:** SA, OC, BI, SD. (See [[00 - Process Library Index|Role Map]].)

## Critical rules
- Every lead is registered in the CRM **within 1 hour** of capture. `[local-market variable: SLA]`
- Every lead has one owner and a qualification status before it is worked.
- No lead sits without a next action; unresponsive leads route to automated nurture.

## Flow

| Step | Action | Role | Expected result |
|---|---|---|---|
| 1 | Capture lead | SA | Collect name, email, phone, country, investor type at event/web |
| 2 | Register in CRM | SA | Full record created in <1h `[local variable]` |
| 3 | Verify data | OC | Complete, no duplicates |
| 4 | Qualify | SA | Classify Hot (<30d) / Warm (1–6m) / Cold (>6m) `[local variable: thresholds]` |
| 5 | Propose assignment | BI | Suggest owner per rules (Hot→senior SA, Cold→prospecting) |
| 6 | Validate assignment | SD | Approve or reassign |
| 7 | First contact | SA | Contact <24h with script + intro material `[local variable: SLA]` |
| 8 | Structured follow-up | SA | Day 1 message / Day 3 material / Day 7 questions / Day 14 offer |
| 9 | Pipeline supervision | SD | Weekly review of leads per advisor |
| 10 | Automated nurture | BI | No response in 30d → automated CRM flow |
| 11 | Weekly report | BI | Dashboard: leads, conversions, ROI by source |

## RACI

| Task | R | A | C | I |
|---|---|---|---|---|
| Capture (event/digital) | SA | SD | — | BI |
| Register in CRM | SA | BI | OC | SD |
| Verify data | OC | BI | SA | — |
| Qualify lead | SA | SD | BI | — |
| Propose assignment | BI | SD | — | SA |
| Approve assignment | SD | SD | BI | SA |
| First contact (<24h) | SA | SD | — | BI |
| Structured follow-up | SA | SD | — | BI |
| Weekly pipeline supervision | SD | SD | BI | SA |
| Configure automated flows | BI | BI | SD | SA |
| Weekly lead report | BI | BI | SD | OC |

## KPIs
| KPI | Target / frequency |
|---|---|
| Time to first contact | < 24h |
| Leads registered in <1h | > 90% |
| Lead → meeting conversion | > 25% |
| ROI by source | Monthly |

## Abstraction & localization notes
- Names removed; agency roles mapped (AG→SA, SEC→OC, CBI→BI, DC→SD).
- "HubSpot" → "the CRM".
- SLAs, qualification windows = local-market variables.
- Status: source content `INHERITED` — reconfirm SLAs and assignment rules with the SD/BI owner before publishing.
