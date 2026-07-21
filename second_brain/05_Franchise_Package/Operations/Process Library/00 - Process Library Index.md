---
project: Dproperty OS
title: "Process Library Index"
type: franchise_note
status: Active
owner: Esteban
last_updated: 2026-07-21
source: Abstracted from Commercial Process Manual v002-26 (Source Material)
tags: [franchise, operations, process-library, roles, source-of-truth]
---

# Process Library Index

> **What this is.** The canonical, **role-based, market-agnostic** version of Dproperty's commercial processes. Every manual (M1–M5) is a curated *view* of these files. This index also holds the **Role Map** — the project-wide role taxonomy required by Decision 2026-07-21 (*roles, never names*).
>
> **Source vs. Library.** Raw agency content (verbatim, with names) lives in `../Source Material/`. That folder is read-only. This Library is the abstracted layer we actually build from. If they ever conflict, the more recent *approved* decision wins (see [[../../../00_Index/Decision Log|Decision Log]]).

## Role Map (project-wide standard)

All Dproperty OS deliverables use these codes. Never use personal names or single-office headcounts.

| Code | Role (agnostic) | What they own | Agency origin (source manual) |
|---|---|---|---|
| **PRIN** | Principal / Franchise Owner | Ultimate office accountability; may hold SD/OD hats in a small office | (franchise-level) |
| **SD** | Sales Director | Approves offers, negotiations, pricing strategy, pipeline | DC (Directora Comercial) |
| **SA** | Sales Advisor | Prospecting, visits, negotiation, closing, client follow-up | AG (Agentes) |
| **OC** | Operations Coordinator | Documents, contracts, billing, commission execution, filing, CRM data hygiene | ADM + SEC |
| **OD** | Operations Director | Process compliance, traceability, exceptions, contract-version control | DO (Dirección de Operaciones) |
| **CA** | Compliance Approver | Approves client profiles; written sign-off on special profiles/exceptions | LA (Luz Adriana) |
| **BI** | Coordination / BI | CRM configuration, analytics, reporting, process supervision (often HQ-shared) | CBI (Coordinación/BI) |
| **PH** | Property & Handover | Inspection, inventory, handover, maintenance coordination | PYE + MAN |

### Role hats (worn by a Sales Advisor, not separate people)
| Hat | Meaning | Agency origin |
|---|---|---|
| **SA · Tenant Advisor** | The SA representing the tenant/buyer in a deal | ATI (Asesor del Inquilino) |
| **SA · Listing Advisor** | The SA who holds the owner/listing relationship | ACO (Asesor Consignador) |
| **SA · Originating Advisor** | The SA who originally sourced an investor (relevant in assignments/cesiones) | AG (orig) |

### Small-office rule
Per Decision 2026-07-18, a franchise must staff at minimum **PRIN + SA + OC**. Other roles (SD, OD, CA, BI, PH) start as **HQ-shared services or AI**, or are held by the Principal, and are split out as the office grows. So a role code = *a responsibility*, not necessarily a separate headcount.

## Systems (agnostic references)
| Use "…" | Not the vendor name |
|---|---|
| "the CRM" | HubSpot / GoHighLevel |
| "the OS" / "the deal record" | Dproperty OS |
| Amounts, %, thresholds | Always tag as **local-market variable** |

## Abstraction rules applied to every file
1. Names → role codes. Headcounts removed.
2. Currency amounts, commission %, deposit rules, tax/legal steps, and body names (e.g. ACOBIR) → flagged **`[local-market variable]`**.
3. Each item carries a status tag where relevant: `APPROVED` (formal decision/acta), `INHERITED` (from source, needs reconfirm), `ASSUMPTION` (working design). Default for un-validated source content = `INHERITED`.
4. **Commission-layer firewall:** agency payroll splits ≠ franchise royalty waterfall. Never merge. See [[../../../00_Index/Decision Log|Decision Log]].

## Process files & status

| # | Process | File | Feeds manual | Abstraction status |
|---|---|---|---|---|
| 1 | Leads | [[01 - Leads]] | M4 Sales Playbook | 🟢 Abstracted |
| 2 | Preventa (Lista Cero) | [[02 - Preventa (Lista Cero)]] | M4 | 🟢 Abstracted |
| 3 | Secondary Market Sale | [[03 - Secondary Market Sale]] | M4 | 🟢 Abstracted |
| 4 | Assignment (Cesión) | [[04 - Assignment (Cesion)]] | M4 | 🟢 Abstracted |
| 5 | Long-Stay Rental | [[05 - Long-Stay Rental]] | M4 + M2 | 🟢 Abstracted |
| 6 | Property Management | [[06 - Property Management]] | M2 Franchise Ops | 🟢 Abstracted |
| 7 | Commissions | [[07 - Commissions]] | M2 + M5 (commission-layer firewall) | 🟢 Abstracted |

**Process Library complete (7/7).** All processes abstracted, role-agnostic, and localization-flagged as of 2026-07-21. Pending: owner re-validation and market localization before any becomes published policy.

## Validation note
These abstractions are faithful to source v002-26 but **not yet re-validated by role owners**. Before any process becomes published franchise policy, confirm it with the accountable role and mark items `APPROVED`.
