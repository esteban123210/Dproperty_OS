---
project: B_RealEstate
title: "Canonical Reconciliation and Precedence"
type: decision_record
status: Canonical v1.0 — CONTROLS THE VAULT
owner: Esteban
date: 2026-09-23
last_updated: 2026-09-23
tags: [ecosystem, governance, precedence, decision, source-of-truth]
---

# Canonical Reconciliation and Precedence — 2026-09-23

> **This note resolves the conflict between the `18_Ecosystem` canon (2026-09-20) and the `19_Canonical_B_RealEstate` baseline (2026-09-23). It controls the whole vault. Every other note is subordinate to it.**

## 1. Why this note exists

Two internally-consistent canonical layers were built three days apart and they contradicted each other on the single most important question in the company: **what BluePrint is**.

| | `18_Ecosystem` + `04_Product/BluePrint` (2026-09-20) | `19_Canonical_B_RealEstate` (2026-09-23) |
|---|---|---|
| BluePrint | Management-control layer. Transaction spine **explicitly retired**. | **Transaction spine**: qualified opportunity → close → commission → audit. |
| 4th product | **Academy** (Open edX), bundled enablement | **Building Blocks**, commercial LMS product |
| Own-brand channel | **B_ Partner** | White-Label partner |
| BluePrint pricing | $299 / $599 / $999 per org | $1,500 setup + $399 / $799 per office |
| Raise | $650k ask retired; rebuild milestone-based | **$950k** capitalization / $800k 18-month plan |

Left unresolved, this makes the vault unusable for investors, developers and AI assistants: two files answer "what are we building" differently, and neither is labelled as losing.

## 2. The decision

**The two definitions were never actually mutually exclusive. They are merged, not chosen between.**

> **BluePrint is a chat-first, AI-native management operating system for small and growing real-estate agencies, whose system of record is the verified transaction, commission and management-control record, beginning at qualified opportunity.**

The `18_Ecosystem` strategic frame wins (product-led company, CRM-agnostic, one authority per data class, verification hierarchy, franchising is a channel). The `19_Canonical` **transaction/commission object** wins as BluePrint's core entity, because it is the atom of management truth for a brokerage.

### Why this is the right answer business-wise

1. **You cannot verify what you do not hold.** The `18_Ecosystem` verification hierarchy — Reported → Operationally verified → Financially verified → Closed — *is a transaction lifecycle*. Its own worked example is a deal marked Won in CRM becoming verified in BluePrint. That requires BluePrint to hold a deal and commission record.
2. **A management layer with no owned transaction object is a BI tool.** `13 - Personas` names the buyer's top fear as "buying another dashboard." A pure reporting layer over someone else's data *is* that dashboard. It will not sustain $399–$799/month.
3. **Commission calculation and deal-file compliance are the real, expensive, defensible pain.** They are what spreadsheets currently do badly, they touch money, and they are genuinely hard to copy. That is a wedge people pay for.
4. **`03 - Architecture` already conceded it**, listing "receivables, commission liabilities" inside BluePrint's scope.
5. **`19_Canonical`'s MVP gate is sharper and falsifiable**: "one workflow executes from qualified intake through commission/report without a shadow spreadsheet as authority." That is a testable product thesis. Keep it.

### What stays retired — and this is the important part

The 2026-09-20 decision record was **right to retire** the *property / project / unit inventory* ambition. That retirement stands permanently:

- ❌ property, project and unit inventory
- ❌ listing management and MLS
- ❌ pre-qualification lead pipeline and marketing automation
- ❌ general ledger, tax, payroll
- ❌ property management
- ❌ LMS / course delivery
- ❌ marketplace listings and matching

**What was over-retired was the transaction and commission record.** That comes back, and only that. The distinction is: BluePrint owns *the deal as a governed management object*, not *the property as inventory*.

## 3. Canonical product and channel definitions

### Products

| # | Product | Job | Owns | Status |
|---|---|---|---|---|
| 1 | **BluePrint** | Run and control the company | Qualified opportunity → transaction file → documents/compliance evidence → approvals → closing → commission calculation → budgets/variance/KPIs → process assurance/Glitches → management actions → period close → audit trail | Proprietary core SaaS/IP |
| 2 | **BlankCRM** | Sell | Leads, contacts, WhatsApp/email/SMS, forms/calendars, nurture, pre-qualification pipeline, campaign attribution | Attach/acquisition product, powered by GoHighLevel |
| 3 | **VAULTED** | Access the network | Gated listings/opportunities, access rules, participant identity, matches, introductions, attribution, GMV, marketplace fees | Network-effect hypothesis; gated pilot after BluePrint stability |
| 4 | **Academy** | Operate better | Learning content, assessments, certification evidence | Enablement layer, powered by Open edX; mostly bundled |

**Handoff line:** BlankCRM owns demand until qualification. BluePrint owns everything after qualification. VAULTED owns network supply/access. Academy owns capability. Accounting remains the ledger.

### Channels — not products

| Channel | Role |
|---|---|
| **Direct SaaS** | BluePrint and/or BlankCRM to independent agencies |
| **B_ Partner** | Managed stack + operating model under the customer's own brand |
| **Dproperty Franchise** | Branded, vertically integrated deployment of the full stack |
| **Developer Partnerships** | Revenue + supply + distribution + product learning |

**B_Franchising** is retained as the commercial/partnership gateway and support *function* — it is **not** the definition of the company.

### Strategic assets — not products

Dproperty brand and testbed · Dproperty Select · developer/broker/investor relationships · the process library / Second Brain.

## 4. Naming — binding

| Canonical | Legacy aliases (do not use in new work) |
|---|---|
| **B_RealEstate** / **B_** | Cantera, Dproperty OS & Network |
| **BluePrint** | Dproperty OS, Plano, "La Plataforma", `[OS_NAME]` |
| **BlankCRM** (powered by GoHighLevel) | "CRM propio", proprietary CRM, GoHighLevel-as-product |
| **VAULTED** | Private Collection *as a marketplace* (see below) |
| **Academy** / **B_Academy** | **Building Blocks**, Training Academy |
| **Dproperty** | — |
| **Dproperty Select** | Private Collection |
| **B_ Partner** | White-Label, White-Label OS |
| **Developer Partnerships** | Developer Sales OS |
| **DpropertyLiving** | **PARKED** — remove from all active navigation and economics |

**Academy vs Building Blocks:** resolved in favour of **Academy**. An LMS is not defensible IP and must not carry investor weight as a standalone product. `19_Canonical`'s "Building Blocks" is a legacy alias for the same learning business.

**Dproperty Select vs VAULTED:** Select is *curated by us*; VAULTED is the *network marketplace*. Select may appear inside VAULTED as an identified curated collection. VAULTED never confers Select approval.

## 5. Canonical economics

| Item | Canonical position | Basis |
|---|---|---|
| BluePrint pricing | **Core $399/mo · Growth $799/mo**, per organization/office, not per agent seat. **Scale tier: quoted, not yet defined.** | `19_Canonical` price points are tied to a built integrated model with CAC/payback outputs; the org-level (not seat-level) shape is from `18_Ecosystem`. |
| BluePrint setup | **$1,500**, higher for complex migration | Implementation-heavy B2B must fund onboarding cost. |
| BlankCRM pricing | **Open.** Build from GHL plan/sub-account + messaging/AI + onboarding/support + target margin. | Both layers agree. |
| VAULTED | Take rate on attributable transactions. Effective base take **0.35% assumption**, unvalidated. | Model only. Never derive from "all BluePrint customers × arbitrary GMV." |
| Academy | Mostly bundled; premium/custom later | Both layers agree. |
| Raise | **$950k capitalization envelope; $800k 18-month operating plan; staged against evidence gates.** | Model-backed. Supersedes both the $650k and $1.5M concepts. |
| Franchise / B_ Partner / Developer economics | Separate **channel** models. Historical figures are hypotheses until contracts and local advice confirm them. No double-counting of software revenue inside bundles. | Both layers agree. |

### Permanently retired as current guidance

- "5 franchises / 20 white-label / 15 developers" as the **company** SOM
- $1.59M–$1.89M Y5 as the **company** forecast
- $650k, and $1.5M, as the funding ask
- $500/month blended ecosystem ARPA
- 600k TAM / 100k SAM headline
- VAULTED revenue derived from arbitrary GMV per BluePrint account
- physical hub as near-term thesis or moat
- "one shared database" / "una sola base de datos"
- "CRM propio" / proprietary CRM
- DpropertyLiving as an active brand, product or entry route

These remain **historical scenario work** and are preserved as evidence, not guidance.

## 6. Precedence — use this order

1. Executed contract, law, regulator instruction, bank/payroll record, audited actual.
2. Board-approved decision record and budget.
3. **This note** (`18 - Canonical Reconciliation and Precedence`).
4. `18_Ecosystem/` canon and `04_Product/BluePrint/` product folder.
5. `19_Canonical_B_RealEstate/` records — for finance models, data/AI architecture, operations, diligence and investor material.
6. Current named financial model, for quantitative projections.
7. Everything else in `00_Index` … `17_Handoff_Files`.
8. Session closeouts, exports, and pre-2026-09-20 strategy/pitch/finance notes — **historical evidence only**.

Higher precedence is not universal authority: a contract governs its parties, a model governs projections, a technical brief governs quotation scope. Never let a pitch slide override a contract or a model.

### Division of labour between the two canonical folders

They are no longer rivals. They are layers:

- **`18_Ecosystem/`** — *what the company is*: thesis, product/channel hierarchy, boundaries, naming, personas, economics registry, roadmap, governance.
- **`04_Product/BluePrint/`** — *what the product is*: constitution, architecture, modules, MVP, pricing, build briefs.
- **`19_Canonical_B_RealEstate/`** — *how it is proven and financed*: financial models, data/AI architecture, operating workflows, compliance, KPIs/gates/kill criteria, investor diligence and two-pagers.

## 7. Truth labels — required on material claims

| Label | Meaning | May support spending? |
|---|---|---|
| `[F] Fact` | Verified actual or executed agreement with evidence | Yes |
| `[D] Decision` | Approved management/board decision | Yes, within budget |
| `[M] Model` | Output of a named financial model | Only with scenario context |
| `[A] Assumption` | Not yet verified | Only via a gated experiment |
| `[T] Target` | Desired future state | No |
| `[R] Required evidence` | Missing proof needed for a decision | No |

## 8. Document lifecycle

`DRAFT → REVIEW → APPROVED → SUPERSEDED → ARCHIVED`

Versioning: `v0.1` rough · `v0.5` structured · `v0.9` ready for review · `v1.0` approved · `v1.1` small update · `v2.0` major revision.

Superseded notes keep their content and open with a visible supersession banner pointing here. **Nothing is deleted** — old thinking is evidence.

## 9. Downstream consequences of this decision

| Area | Required change |
|---|---|
| `04_Product/BluePrint/` | Reinstate the transaction/commission spine as the wedge module inside the management OS; keep the inventory/MLS retirement |
| `04_Product/BluePrint/08 - Pricing` | Move to $399 / $799 + $1,500 setup |
| `18_Ecosystem/02` and `12` | BluePrint owns the verified transaction and commission record |
| `19_Canonical` | Building Blocks → Academy alias; precedence points here; franchise projections are channel models |
| `01_Strategy`, `02_Business_Plan`, `03_Pitch`, `07_Finance` | Pre-reset franchise-first material marked superseded |
| `13_White_Label` | Reframed as B_ Partner |
| `11_Developer_Sales_OS` | Reframed as Developer Partnerships |
| `12_Private_Collection` | Reframed as Dproperty Select |
| `CLAUDE.md`, `00_Index`, AI Handoff Pack | Rebuilt around this precedence order |

## 10. Open items this decision deliberately does not close

1. **Scale tier** price and contents — undefined on purpose.
2. **Franchise royalty structure** — 6% + 1% restricted fund (Dproperty) vs 4% no fund (own-brand) vs the isolated model's flat 6% + 1.5%. Needs contract design and local advice.
3. **BlankCRM price** — blocked on GHL cost modelling.
4. **VAULTED take rate and legal structure** — per jurisdiction.
5. **Whether Academy ever becomes a standalone commercial product.** Default: no.

Tracked in [[../00_Index/Open Questions]].
