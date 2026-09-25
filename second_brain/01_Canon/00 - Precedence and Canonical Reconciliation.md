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

| | `18_Ecosystem` + `02_Offers/01_BluePrint/BluePrint` (2026-09-20) | `19_Canonical_B_RealEstate` (2026-09-23) |
|---|---|---|
| BluePrint | Management-control layer. Transaction spine **explicitly retired**. | **Transaction spine**: qualified opportunity → close → commission → audit. |
| 4th product | **Academy** (Open edX), bundled enablement | **Building Blocks**, commercial LMS product |
| Own-brand channel | **B_ Partner** | White-Label partner |
| BluePrint pricing | $299 / $599 / $999 per org | $1,500 setup + $399 / $799 per office |
| Raise | $650k ask retired; rebuild milestone-based | **$950k** capitalization / $800k 18-month plan |

Left unresolved, this makes the vault unusable for investors, developers and AI assistants: two files answer "what are we building" differently, and neither is labelled as losing.

> [!WARNING] Positioning corrected 2026-09-25
> The **boundaries** below still hold, but the **positioning and differentiator do not**.
> BluePrint is an **agentic back office** — a CEO/CFO/COO/CMO without C-suite payroll — whose
> defining rule is that **nothing is recorded without evidence**. The "transaction spine from
> qualified opportunity" framing claimed a differentiator a CRM already provides.
> See [[22 - BluePrint Repositioned - Agentic Back Office]].

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
| 4 | **Building Blocks** | Operate better | Learning content, curricula, assessments, certification and competency evidence | Standalone learning product, powered by Open edX |

**Handoff line:** BlankCRM owns demand until qualification. BluePrint owns everything after qualification. VAULTED owns network supply/access. Building Blocks owns capability. Accounting remains the ledger.

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
| **Building Blocks** | **Academy**, B_Academy, Training Academy |
| **Dproperty** | — |
| **Dproperty Select** | Private Collection |
| **B_ Partner** | White-Label, White-Label OS |
| **Developer Partnerships** | Developer Sales OS |
| **DpropertyLiving** | **PARKED** — remove from all active navigation and economics |

**Academy vs Building Blocks:** **resolved in favour of Building Blocks as a standalone product (2026-09-24, reversing the 2026-09-23 position).** `18_Ecosystem`'s "Academy" is the legacy alias. The portfolio is deliberately composed of separately sellable products — see [[19 - Portfolio Composition Principle]]. The investor hierarchy is unchanged: proprietary value still concentrates in BluePrint and VAULTED.

**Dproperty Select vs VAULTED:** Select is *curated by us*; VAULTED is the *network marketplace*. Select may appear inside VAULTED as an identified curated collection. VAULTED never confers Select approval.

## 5. Canonical economics

| Item | Canonical position | Basis |
|---|---|---|
| BluePrint pricing | **Core $399/mo · Growth $799/mo**, per organization/office, not per agent seat. **Scale tier: quoted, not yet defined.** | `19_Canonical` price points are tied to a built integrated model with CAC/payback outputs; the org-level (not seat-level) shape is from `18_Ecosystem`. |
| BluePrint setup | **$1,500**, higher for complex migration | Implementation-heavy B2B must fund onboarding cost. |
| BlankCRM pricing | **Open.** Build from GHL plan/sub-account + messaging/AI + onboarding/support + target margin. | Both layers agree. |
| VAULTED | Take rate on attributable transactions. Effective base take **0.35% assumption**, unvalidated. | Model only. Never derive from "all BluePrint customers × arbitrary GMV." |
| Building Blocks | **Standalone product** — $199 blended per enrollment `[A]`; core onboarding included in packages at allocated standalone value | Reversed 2026-09-24: see [[19 - Portfolio Composition Principle]]. |
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
3. **This note** — `01_Canon/00 - Precedence and Canonical Reconciliation.md`.
4. The rest of `01_Canon/` — company definition, hierarchy, boundaries, system of record, economics registry, governance.
5. The offer's own `01 - Definition and Boundaries.md` and `03 - Offer and Pricing.md` in `02_Offers/0X_…/`.
6. Current named financial model, for quantitative projections (`06_Finance/`).
7. Everything else — `03_Strategy/` … `13_Research/`.
8. Anything in `98_Archive/` — **historical evidence only, never guidance**.

Higher precedence is not universal authority: a contract governs its parties, a model governs projections, a technical brief governs quotation scope. Never let a pitch slide override a contract or a model.

### Authority is a property of documents, not folders

The two rival canonical folders that made this note necessary — `18_Ecosystem/` and `19_Canonical_B_RealEstate/` — were **dissolved on 2026-09-23** into a single structure with one home per topic. See [[../00_Start_Here/Vault Architecture Map]].

The three "layers" they represented survive as roles, now spread across the flat structure:

- *What the company is* → `01_Canon/`
- *What each offer is* → `02_Offers/0X_…/`
- *How it is proven and financed* → `06_Finance/`, `09_Data_and_AI/`, `08_Operations/`, `05_Pitch_and_Investor/`

Because folder location no longer signals authority, **every material claim must carry a truth label and a date.** That is what precedence now reads.

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

| Area | Required change | Status |
|---|---|---|
| `02_Offers/01_BluePrint/` | Reinstate the transaction/commission spine as the wedge module inside the management OS; keep the inventory/MLS retirement | ✅ done |
| `02_Offers/01_BluePrint/03 - Offer and Pricing.md` | Move to $399 / $799 + $1,500 setup | ✅ done |
| `01_Canon/01`, `02`, `07` | BluePrint owns the verified transaction and commission record | ✅ done |
| Academy naming | "Building Blocks" demoted to legacy alias across all records | ✅ done |
| Channel naming | White-Label → **B_ Partner**; Developer Sales OS → **Developer Partnerships**; Private Collection → **Dproperty Select** | ✅ done — folders renamed |
| Vault architecture | Two parallel canonical folders dissolved; one home per topic; `02_Offers/` created with one folder per sellable thing | ✅ done — see [[../00_Start_Here/Vault Architecture Map]] |
| `03_Strategy/`, `04_Business_Plan/`, `05_Pitch_and_Investor/`, `06_Finance/` | Pre-reset franchise-first material moved to `98_Archive/` or banner-marked | ✅ done |
| `CLAUDE.md`, `00_Start_Here/`, AI Handoff Pack | Rebuilt around this precedence order and the new architecture | ✅ done |
| `12_Handoffs/` | Regenerate every handoff against reconciled canon before external use | ⬜ pending |
| `10_Brand_and_Web/` | Product-led website rewrite | ⬜ pending |

## 10. Open items this decision deliberately does not close

1. **Scale tier** price and contents — undefined on purpose.
2. **Franchise royalty structure** — 6% + 1% restricted fund (Dproperty) vs 4% no fund (own-brand) vs the isolated model's flat 6% + 1.5%. Needs contract design and local advice.
3. **BlankCRM price** — blocked on GHL cost modelling.
4. **VAULTED take rate and legal structure** — per jurisdiction.
5. ~~Whether Academy ever becomes a standalone commercial product.~~ **RESOLVED 2026-09-24: yes — Building Blocks is a standalone product.** See [[19 - Portfolio Composition Principle]].

Tracked in [[../00_Start_Here/Open Questions]].
