---
project: B_RealEstate
title: "Process 7 — Commissions"
type: process
status: Abstracted
owner: Esteban
process_id: process7
order: 70
feeds: [M2 Franchise Operations Manual, M5 Compliance Manual]
source: "Commercial Process Manual v002-26 — Proceso 7"
last_updated: 2026-07-21
tags: [process-library, commissions, finance, operations]
---

> [!INFO] Channel-scoped — verified 2026-09-23
> This folder describes the **Dproperty Franchise** channel, not the company and not a product. B_RealEstate is a product-led software company; this is one route to market.
>
> **Canonical name:** Dproperty Franchise — “the company itself” is a legacy alias.
> This is **valuable operating source material** — the process library and manuals feed BluePrint's SOP/process model and Academy. Franchise royalty/launch economics are channel-specific and require contract design plus local legal advice before external use.
>
> Precedence: [[../../../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]

# Process 7 — Commissions

**Objective.** Standardize the collection, calculation, and payment of commissions with full traceability and on-time cycles.

**Roles used:** OC, SD, BI, SA. (See [[00 - Process Library Index|Role Map]].)

> 🔴 **COMMISSION-LAYER FIREWALL — read before editing.** There are **three separate money flows**. This process covers Flows 1 & 2 only. Never merge them.
>
> | Flow | What it is | Where it lives |
> |---|---|---|
> | **1. Income collection** | Developer/client/counterparty pays commission to the office | This process, steps 1–6 |
> | **2. Agent payout** | Office pays its own advisors (agency scheme: e.g. Junior 35%/70%, Senior 40%/45%) | This process, steps 7–14 — **office-configurable, `[local-market variable]`** |
> | **3. HQ franchise royalty** | Office pays HQ (7.5% on **collected GCI**, computed on gross-into-company) | **NOT here** — franchise reporting / [[../../../00_Index/Decision Log|Decision Log 2026-07-05]] |
>
> The agent-payout percentages are the *originating agency's* internal scheme and are **not** a Dproperty OS mandate. A franchise sets its own advisor payout; HQ royalty is computed independently and is un-gameable (based on gross-into-company, not net).

## Flow

| Step | Action | Role | Expected result |
|---|---|---|---|
| 1 | Confirm client payment | OC | Verify counterparty met the trigger payment (e.g. developer down-payment) |
| 2 | Proforma invoice | OC | Create invoice with unit + counterparty data |
| 3 | Send to counterparty | OC | Send proforma + collection docs |
| 4 | Receive transfer | OC | Confirm inbound transfer |
| 5 | Formal invoice | OC | Issue formal/electronic invoice |
| 6 | Notify advisors | OC | Inform that commission was collected |
| 7 | Submit billing accounts | SA | Advisors submit account + invoice by cutoff `[local variable: weekly cutoff]` |
| 8 | Calculate commissions | OC | Apply the office payout policy `[local variable: e.g. Junior 35/70, Senior 40/45]` |
| 9 | Validate calculations | SD | Review amounts, approve settlement |
| 10 | Validate documents | BI | Check tax ID/registration, completeness |
| 11 | Assemble folders | OC | Organize by unit by cutoff `[local variable]` |
| 12 | Authorize payments | SD | Final sign-off for transfers |
| 13 | Process payments | OC | Execute transfers on the pay cycle `[local variable]` |
| 14 | Archive | OC | Digital + physical in unit folder |

## Commission policy (SOURCE REFERENCE — office-configurable, not HQ policy)

> `[local-market variable]` The originating agency's scheme, kept for reference only:

| Category | Sales | Rentals | Consignment |
|---|---|---|---|
| Junior broker | 35% | 70% | +5% owner / +5% client |
| Senior broker | 40% | 45% | +5% owner / +5% client |
| External broker | 1.5% of value | — | — |

*Percentages are computed on the amount entering the office, not on total property value. Each franchise defines its own scheme in its ops manual.*

## RACI

| Task | R | A | C | I |
|---|---|---|---|---|
| Confirm trigger payment | OC | OC | — | SD |
| Manage collection | OC | SD | — | BI |
| Submit billing accounts | SA | OC | — | — |
| Calculate commissions | OC | SD | — | BI |
| Validate calculations | SD | SD | OC | — |
| Validate documents | BI | BI | OC | — |
| Assemble folders | OC | OC | — | — |
| Authorize payments | SD | SD | OC | BI |
| Process payment | OC | SD | — | SA |
| Final archive | OC | OC | — | BI |

## KPIs
| KPI | Target / frequency |
|---|---|
| Trigger payment → advisor paid | < 10 days `[local variable]` |
| Complete folders | 100% |
| Documentation errors | 0 |

## Abstraction & localization notes
- Roles mapped (ADM/SEC→OC, DC→SD, CBI→BI, AG→SA).
- **All percentages, weekly cutoffs (Tue/Wed/Fri), and pay cycles = local-market variables.**
- The **three-flow firewall** above is the single most important thing to preserve when this feeds M2/M5 and the financial model.
- Status: operational flow `INHERITED`; the firewall framing is `APPROVED` per Decision Log 2026-07-05 / 2026-07-21.
