---
project: B_RealEstate
title: "Manuals System Index"
type: franchise_note
status: Active
owner: Esteban
last_updated: 2026-07-21
source: Work session 2026-07-21 — manuals architecture decision
tags: [franchise, manuals, architecture, source-of-truth]
---

> [!INFO] Channel-scoped — verified 2026-09-23
> This folder describes the **Dproperty Franchise** channel, not the company and not a product. B_RealEstate is a product-led software company; this is one route to market.
>
> **Canonical name:** Dproperty Franchise — “the company itself” is a legacy alias.
> This is **valuable operating source material** — the process library and manuals feed BluePrint's SOP/process model and Academy. Franchise royalty/launch economics are channel-specific and require contract design plus local legal advice before external use.
>
> Precedence: [[../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]

# Manuals System Index

> **Purpose.** This note is the master architecture for every Dproperty OS manual. It defines *how many* manuals exist, *who each one is for*, *where the content lives*, and *how they stay in sync*. Every manual below is a curated **view** of a single shared source. Do not draft or edit a manual without checking this index first.

## 0. Governing principle — one master source, many audience views

The biggest risk with multiple manuals is **drift**: the same process described three slightly different ways in three documents. We avoid that with one rule:

> **Process content is written once in the Process Library. Each manual is a curated view of it, scoped to its audience.**

- The **raw** operating know-how (verbatim, agency-specific, with names) lives in **Source Material** (`05_Franchise_Package/Operations/Source Material/`), seeded from the real agency **Commercial Process Manual (v002-26)** — 7 processes: Leads, Lista Cero, Mercado Secundario, Cesiones, Alquiler, Administración de Propiedades, Comisiones. **Read-only.**
- The **abstracted, role-based, market-agnostic** version lives in the **Process Library** (`05_Franchise_Package/Operations/Process Library/`). This is the canonical layer every manual draws from. Its [[Operations/Process Library/00 - Process Library Index|Index]] holds the **Role Map** (the project-wide role taxonomy — Decision 2026-07-21, roles never names).
- Each manual **references and abstracts** Process Library content for its reader — it does not re-invent it.
- We adopt the *concept* of the source doc's "single source → generated outputs" model, but **not** its Python/HTML build tooling. Obsidian is our source of truth.

## 1. The three audiences (why there are six manuals)

| Tier | Reader | Question the manual answers | Confidentiality |
|---|---|---|---|
| **0 — HQ (us)** | Franchisor team | "How do *we* run the franchise system?" | HQ-only. Never shared. |
| **1 — Franchisee owner** | The person who buys a franchise | "How do I run *my* Dproperty office?" | Shared with owner under agreement |
| **2 — Agents/employees** | The franchisee's salespeople | "How do I actually sell and execute deals?" | Shared with agents |
| **Cross-cutting** | Owner **and** agents | "What rules must everyone follow?" | Shared, HQ-owned & enforced |

## 2. The six manuals

| ID | Manual | ES name | Tier / audience | Vault home | Status | Build order |
|---|---|---|---|---|---|---|
| **M0** | HQ / Franchisor Operations Manual | Manual Maestro de Operaciones (HQ) | 0 — HQ internal | `05_Franchise_Package/Operations/` (to create) | 🔴 Planned (deferred) | 6th |
| **M1** | Franchise Onboarding | Onboarding de Franquicia | 1 — owner | [[Onboarding/Franchise Onboarding PDF]] | 🟡 Baseline | 4th |
| **M2** | Franchise Operations Manual | Manual de Operaciones de la Franquicia | 1 — owner | [[Operations/Operations Manual]] | 🟢 v0.5 (on Process Library) | 3rd |
| **M3** | Launch Plan (30-60-90) | Plan de Lanzamiento | 1 — owner | [[Launch/30-60-90 Day Franchise Launch Plan]] | 🟡 Baseline (+ [[Launch/First Franchisee Launch Playbook|12-wk Playbook]], needs standards fix) | 5th |
| **M4** | Sales Playbook | Playbook de Ventas | 2 — agents | [[Sales/Sales Playbook]] | 🟢 v0.5 (on Process Library) | 2nd |
| **M5** | Compliance Manual | Manual de Cumplimiento | Cross-cutting | [[Compliance/Compliance Package]] | 🟢 v0.5 (needs legal sign-off) | 7th |

Legend: 🟢 Ready for review · 🟡 Thin baseline exists · 🔴 Not started

### Supporting frameworks (shared core)
- [[Operations/Process Library/00 - Process Library Index|Process Library]] — 7/7 abstracted, role-agnostic.
- [[Localization/Localization Framework|Localization Framework]] — process-global / values-local; market packs.
- [[Multi-Line Manual Strategy]] — shared core + white-label / developer overlays.
- [[Manuals Audit and Gap Analysis]] — maturity, gaps, and the P0→P2 remediation roadmap.

### Naming decision to confirm
"**Maestro**" is reserved for the **HQ internal master (M0)** — the one document everything else derives from and that we never hand out. The franchisee's operations manual is **"Manual de Operaciones de la Franquicia" (M2)**, not "maestro." *Confirm this convention before we rename the baseline file.*

## 3. How the Spanish source manual feeds the six

The 7-process **Commercial Process Manual (v002-26)** is mostly **Tier 2 (agent execution)** content, with the commission section straddling Tier 1 (owner finance).

| Source process | Feeds primarily | Also feeds |
|---|---|---|
| 1. Leads | M4 Sales Playbook | M2 Ops (CRM discipline) |
| 2. Lista Cero (preventa) | M4 Sales Playbook | M2 Ops |
| 3. Mercado Secundario | M4 Sales Playbook | — |
| 4. Cesiones | M4 Sales Playbook | M5 Compliance (dual-approval) |
| 5. Alquiler | M4 Sales Playbook | M2 Ops (handoff to admin) |
| 6. Administración de Propiedades | M2 Franchise Operations Manual | M5 Compliance |
| 7. Comisiones | M2 Ops + M5 Compliance | Finance model (not agent-facing) |

> ⚠️ **Commission-layer caution.** The source manual's Proceso 7 splits (agency payroll: Junior 35/70, Senior 40/45) are the **agency's internal payroll layer**, *not* the Dproperty OS **franchise royalty waterfall** (5% → 50/50 co-broke → 35/10/55) in the [[../00_Index/Decision Log]]. These are different layers. **Never conflate them.** Reconcile explicitly when M2/M5/M7-finance touch commissions.

## 4. What must be abstracted (agency → franchise-portable)

The source is written for one Panama office. Before its content enters any manual, strip and generalize:
- Real names (Silvia, Maria Isabel, Luz Adriana, etc.) → **roles** (Admin, Compliance Approver, Sales Director).
- Panama/ACOBIR-specific rules → mark as **local-market variables**.
- Spanish → decide language per audience (see Open Question below).
- Single-office team of 14 → **role-based**, works at any franchise size.

## 5. Build roadmap

1. ✅ **This index** — architecture + master-source model (2026-07-21).
2. ⬜ **Import + abstract the Process Library** — drop the v002-26 source in verbatim, then build the role-based, market-agnostic process layer.
3. ⬜ **M4 Sales Playbook** — first real manual, mined from the Process Library.
4. ⬜ **M2 Franchise Operations Manual** — the backbone the on-ramp attaches to.
5. ⬜ **M1 Onboarding** — the day-0 entry sequence into M2.
6. ⬜ **M3 Launch Plan** — day 0→90 companion to M2.
7. ⬜ **M5 Compliance Manual** — cross-cutting rules, HQ-enforced.
8. ⬜ **M0 HQ Operations Manual** — deferred per decision 2026-07-21.

## 6. Relationship to existing package notes

This index governs the **manual content**. The delivery/checklist notes stay as-is and link here:
- [[Franchise Launch Package Index]] — full delivery package (manuals are items 6, 7, 13).
- [[Franchise Deliverables Checklist]] — human-readable checklist.

## 7. Open questions raised by this architecture

- **Language:** Are franchise manuals authored in **Spanish, English, or bilingual**? (First markets: Panama, Bogotá, Medellín = Spanish; but investor/deck audience = English.)
- **Naming:** Confirm "Maestro" = HQ internal (M0), franchisee gets "Manual de Operaciones de la Franquicia" (M2).
- **M0 timing:** Confirm HQ manual is genuinely deferred until M1–M5 drafts exist.
