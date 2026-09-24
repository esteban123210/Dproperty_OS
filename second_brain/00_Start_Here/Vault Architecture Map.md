---
project: B_RealEstate
title: "Vault Architecture Map"
type: architecture_map
status: Canonical v1.0
owner: Esteban
last_updated: 2026-09-23
tags: [architecture, navigation, governance, source-of-truth]
---

# Vault Architecture Map

> **This note defines where everything lives and why.** If you cannot find something, the answer is here. If something is in the wrong place, fix the file — not this map.

## 1. What was wrong before

The vault previously ran `00_Index` through `19_Canonical_B_RealEstate`. Those folder names are listed below as history — they no longer exist.

| Problem | Evidence |
|---|---|
| **Two parallel vaults** | The old `19_Canonical_B_RealEstate/` re-covered company, strategy, products, finance, operations and roadmap — the same domains as the old `01_Strategy` through `07_Finance`. Two homes for every topic, and no rule saying which won. |
| **Products scattered across six folders** | BluePrint lived in `04_Product/`, BlankCRM in `14_CRM_GoHighLevel/`, Building Blocks (then called Academy) inside `05_Franchise_Package/Training/`, VAULTED only as a one-pager in `18_Ecosystem/`, Dproperty Select in `12_Private_Collection/`, B_ Partner in `13_White_Label/`, Developer Partnerships in `11_Developer_Sales_OS/`. |
| **`04_Product` meant "BluePrint"** | Eight sellable things; exactly one of them had a product folder. |
| **Canon buried at the end** | `18_Ecosystem/` held the controlling definitions but sorted second-to-last, after every superseded file. |
| **Legacy names as folder names** | `13_White_Label` (now B_ Partner), `12_Private_Collection` (now Dproperty Select), `11_Developer_Sales_OS` (now Developer Partnerships). The folder tree actively taught retired vocabulary. |
| **No archive** | Superseded July material sat beside current canon with no separation. |

## 2. Design principles

1. **One topic, one home.** No parallel structures.
2. **Every sellable thing gets a first-class folder** with the same internal skeleton.
3. **Navigation follows the question you are asking**, not the order things were created.
4. **Canon sorts first.** Precedence is impossible to miss.
5. **Folder names use canonical vocabulary only.** Legacy names appear inside notes as aliases, never as folders.
6. **Nothing is deleted.** Superseded material moves to `98_Archive/` with a banner. Old thinking is evidence.
7. **Every folder has a `README.md`** stating what it holds, what is current, and what is missing.

## 3. The architecture

```
second_brain/
│
├── 00_Start_Here/          "Where do I begin? What did we decide?"
├── 01_Canon/               "What IS the company?"          ← controls the vault
├── 02_Offers/              "What do we SELL?"              ← one folder per offer
├── 03_Strategy/            "How do we win?"
├── 04_Business_Plan/       "What is the plan?"
├── 05_Pitch_and_Investor/  "How do we raise?"
├── 06_Finance/             "What are the numbers?"
├── 07_Legal_and_Compliance/"What are we bound by?"
├── 08_Operations/          "How is work actually done?"    ← shared standards
├── 09_Data_and_AI/         "Where does data live? AI rules?"
├── 10_Brand_and_Web/       "How do we look and sound?"
├── 11_Execution/           "What am I doing this week?"
├── 12_Handoffs/            "Tool-ready briefs for external production"
├── 13_Research/            "What do we still need to learn?"
├── 98_Archive/             "Superseded — evidence only"
└── 99_Templates/           "Reusable scaffolds"
```

### Why this order

`00`–`02` is the daily path: orient → check canon → work on an offer. `03`–`07` is the company layer, read in the order an investor reads it. `08`–`10` is how the business runs and presents. `11`–`13` is execution and inputs. `98`–`99` sort out of the way.

## 4. `02_Offers/` — the core change

An **offer** is anything a customer can buy. Strategy still distinguishes *product* from *channel* from *asset* — that lives in the note content, in `01_Canon/03 - Product and Channel Hierarchy`. But **navigation is organized by what we sell**, because that is how you actually look for things.

| Folder | Offer | Type | Canonical name note |
|---|---|---|---|
| `01_BluePrint/` | BluePrint | **Product** — proprietary core | — |
| `02_BlankCRM/` | BlankCRM | **Product** — attach, powered by GoHighLevel | — |
| `03_VAULTED/` | VAULTED | **Product** — network/marketplace | — |
| `04_Building_Blocks/` | Building Blocks | **Product** — learning/certification | legacy aliases: *Academy*, *B_Academy* |
| `05_Dproperty_Franchise/` | Dproperty Franchise | **Channel** — branded full stack | — |
| `06_B_Partner/` | B_ Partner | **Channel** — managed own-brand | legacy alias: *White-Label* |
| `07_Developer_Partnerships/` | Developer Partnerships | **Channel** — revenue/supply/distribution | legacy alias: *Developer Sales OS* |
| `08_Dproperty_Select/` | Dproperty Select | **Strategic asset** — curated inventory | legacy alias: *Private Collection* |

### Standard skeleton inside every offer folder

```
0X_Offer_Name/
├── 00 - README.md                     what it is · status · what exists · what is missing
├── 01 - Definition and Boundaries.md  canonical definition, what it owns, what it does NOT own
├── 02 - ICP and Jobs To Be Done.md    who buys, who uses, the job
├── 03 - Offer and Pricing.md          what is sold, at what price, with what status label
├── 04 - Delivery and Operations.md    how it is implemented, onboarded, supported
├── 05 - Economics.md                  unit economics, COGS, margin
├── 06 - Legal.md                      agreement notes, commission rules, jurisdiction flags
├── 07 - Investor Two-Pager.md         the comparable investor summary
└── …                                  offer-specific: Architecture, Modules, MVP, Build Briefs
```

**Not every offer has every file.** The `00 - README.md` always states which exist and which are genuine gaps — an empty placeholder is worse than a named gap.

`01_BluePrint/` carries the most: it keeps its full product canon (constitution, architecture, modules, data trust, chat-first model, MVP plan, competitive positioning, build brief, decision records).

## 5. What each top-level folder holds

| Folder | Holds | Does not hold |
|---|---|---|
| **`00_Start_Here/`** | Master Index, Project Context Brief, Decision Log, Open Questions, Current Priorities, Vault Manifest, Source Map, **AI Handoff Pack**, Meeting Notes, this map | Strategy content, offer content |
| **`01_Canon/`** | Precedence note, Ecosystem Master Map, company definition, product/channel hierarchy, offer portfolio map, personas, customer journeys, system-of-record matrix, entitlement contracts, unit-economics registry, roadmap/governance, glossary, status dashboard, QA report | Per-offer detail (that lives in `02_Offers/`) |
| **`02_Offers/`** | One folder per sellable thing, standard skeleton | Cross-offer strategy, shared SOPs |
| **`03_Strategy/`** | Positioning, moat, GTM, customer ladder, KPIs, PESTEL, SWOT/TOWS/Porter, market & TAM method, originality | Offer definitions, financial models |
| **`04_Business_Plan/`** | Master business plan, business model canvas, ownership & governance, compensation, roadmap & milestones | Projections (those are Finance) |
| **`05_Pitch_and_Investor/`** | Deck outlines, pitch scripts, Q&A, investment memo, IC attack sheet, data-room index, evidence status | Two-pagers (those live with their offer) |
| **`06_Finance/`** | Financial architecture & source models, projections, funding & use of funds, pricing/revenue policy, unit economics, assumptions & diligence gaps, model build guides | Per-offer economics detail (lives in the offer folder, summarized here) |
| **`07_Legal_and_Compliance/`** | Legal architecture, contract template index, compliance & legal register, data/privacy, compliance package | Per-offer agreement notes (live in the offer folder) |
| **`08_Operations/`** | **Process Library** (shared, role-based), Operations Manual, golden transaction workflow, onboarding/support/QA, reporting & management cadence, localization framework, manuals system, source material | Offer-specific launch packaging |
| **`09_Data_and_AI/`** | Data architecture & canonical entities, system-of-record & event taxonomy, AI handoff protocol, AI navigation, knowledge ingestion & retention, roles & access matrix | Product feature specs |
| **`10_Brand_and_Web/`** | Brand architecture, brand manual, brand assets index, file storage rules, web presence & funnel architecture, site copy/wireframes, website audit | Design binaries (those live in Figma/Canva/Drive) |
| **`11_Execution/`** | Deliverables tracker, current sprint, weekly workflow, roadmaps, phased rollout | Strategy |
| **`12_Handoffs/`** | Self-contained tool-ready production briefs | Source notes |
| **`13_Research/`** | Research backlog, market evidence requests | Conclusions (those become canon or strategy) |
| **`98_Archive/`** | Superseded strategy/plans/pitches/finance, historical exports, parked concepts, old session closeouts | Anything current |
| **`99_Templates/`** | Note, meeting, deliverable, record and closeout templates | Filled-in instances |

## 6. Where the two old canonical folders went

The old `18_Ecosystem/` and `19_Canonical_B_RealEstate/` folders are **dissolved into the single structure**. The three-layer precedence model from 2026-09-23 survives as a **precedence rule on documents**, not as a folder split — which is what it should always have been.

Old paths below are history; they no longer exist on disk.

| Was | Now |
|---|---|
| `18_Ecosystem/18 - Canonical Reconciliation` | `01_Canon/00 - Precedence and Canonical Reconciliation.md` |
| `18_Ecosystem/00, 01, 12, 13, 14, 16, 17` | `01_Canon/` (map, company definition, system of record, personas, economics registry, roadmap, hierarchy) |
| `18_Ecosystem/02, 03, 03A, 04, 05, 06, 07, 08, 09` | the matching `02_Offers/0X_…/01 - Definition and Boundaries.md` |
| `18_Ecosystem/10 - DpropertyLiving` | `98_Archive/Parked/` |
| `18_Ecosystem/11, 15` | `10_Brand_and_Web/` |
| `19_…/00_HOME` | `01_Canon/` (governance, glossary, status, QA) + `09_Data_and_AI/` (AI navigation) |
| `19_…/01_COMPANY` | `04_Business_Plan/` + `10_Brand_and_Web/` (corporate brand) |
| `19_…/02_FRANCHISING` | `02_Offers/05, 06, 07/` + `08_Operations/Shared Operating Model.md` + `01_Canon/18 - Franchise and Partner Portfolio.md` |
| `19_…/03_PRODUCTS` | `02_Offers/01–04/04 - Product Record.md` |
| `19_…/04_ECOSYSTEM` | `01_Canon/06`, `08`, `15` |
| `19_…/05_STRATEGY` | `03_Strategy/` |
| `19_…/06_FINANCE` | `06_Finance/` |
| `19_…/07_OPERATIONS` | `08_Operations/` + `07_Legal_and_Compliance/` |
| `19_…/08_DATA_AI` | `09_Data_and_AI/` |
| `19_…/09_ROADMAP` | `01_Canon/16`, `17` + `03_Strategy/Roadmap and Validation Experiments.md` |
| `19_…/10_INVESTOR_DILIGENCE` | `05_Pitch_and_Investor/` |
| `19_…/11_TEMPLATES` | `99_Templates/Record Templates.md` |
| `19_…/12_INVESTOR_TWO_PAGERS` | the matching `02_Offers/0X_…/07 - Investor Two-Pager.md` |
| `19_…/00_HOME/README`, `MASTER_INDEX` | `98_Archive/Superseded Canon/` |

### Other folder moves

| Was | Now |
|---|---|
| `00_Index/` | `00_Start_Here/` |
| `01_Strategy/` | `03_Strategy/` (+ `10_Brand_and_Web/`, `05_Pitch_and_Investor/`) |
| `02_Business_Plan/` | `04_Business_Plan/` (+ `06_Finance/`) |
| `03_Pitch/` | `05_Pitch_and_Investor/` |
| `04_Product/BluePrint/` | `02_Offers/01_BluePrint/` |
| `04_Product/` loose files | `02_Offers/01_BluePrint/`, `09_Data_and_AI/`, `10_Brand_and_Web/`, `12_Handoffs/`, `98_Archive/` |
| `05_Franchise_Package/` | `02_Offers/05_Dproperty_Franchise/` + `08_Operations/` + `07_Legal_and_Compliance/` + `10_Brand_and_Web/` + `02_Offers/04_Building_Blocks/` |
| `06_Legal/` | `07_Legal_and_Compliance/` + each offer's `06 - Legal.md` |
| `07_Finance/` | `06_Finance/` + each offer's `05 - Economics.md` |
| `08_Research/` | `13_Research/` |
| `09_Exports/` | `98_Archive/Exports/` |
| `10_Templates/` | `99_Templates/` |
| `11_Developer_Sales_OS/` | `02_Offers/07_Developer_Partnerships/` |
| `12_Private_Collection/` | `02_Offers/08_Dproperty_Select/` |
| `13_White_Label/` | `02_Offers/06_B_Partner/` |
| `14_CRM_GoHighLevel/` | `02_Offers/02_BlankCRM/` |
| `15_Brand_Assets_Index/` | `10_Brand_and_Web/` |
| `16_Task_Management/` | `11_Execution/` (+ `98_Archive/Superseded Execution/`) |
| `17_Handoff_Files/` | `12_Handoffs/` |

## 7. Precedence after the merge

Folder location no longer signals authority. **Authority is stated on the document.** When records conflict:

1. Executed contract, law, regulator instruction, bank/payroll record, audited actual.
2. Board-approved decision record and budget.
3. `01_Canon/00 - Precedence and Canonical Reconciliation.md`.
4. The rest of `01_Canon/`.
5. The offer's own `01 - Definition and Boundaries.md` and `03 - Offer and Pricing.md`.
6. The current named financial model, for projections.
7. Everything else.
8. Anything in `98_Archive/` — **evidence only, never guidance**.

Every material claim carries a truth label: `[F] Fact` · `[D] Decision` · `[M] Model` · `[A] Assumption` · `[T] Target` · `[R] Required evidence`.

## 8. How to navigate — by question

| Your question | Go to |
|---|---|
| "What did we decide about X?" | `00_Start_Here/Decision Log.md` |
| "What is still undecided?" | `00_Start_Here/Open Questions.md` |
| "What am I working on?" | `00_Start_Here/Current Priorities.md` → `11_Execution/` |
| "What IS BluePrint / VAULTED / Building Blocks?" | `02_Offers/0X/01 - Definition and Boundaries.md` |
| "What does it cost?" | `02_Offers/0X/03 - Offer and Pricing.md` |
| "Who owns this data?" | `01_Canon/07 - System of Record and Integration Matrix.md` |
| "What do we tell investors?" | `05_Pitch_and_Investor/` + `02_Offers/0X/07 - Investor Two-Pager.md` |
| "What are the numbers?" | `06_Finance/` |
| "How is a deal actually processed?" | `08_Operations/Process Library/` |
| "Can AI touch this?" | `09_Data_and_AI/AI Handoff Protocol.md` |
| "I need to produce a deck/site/manual" | `12_Handoffs/` |
| "What did we used to think?" | `98_Archive/` |

## 9. Rules for adding new material

1. **New offer?** Create `02_Offers/0X_Name/` with the full skeleton and a `00 - README.md`. Register it in `01_Canon/04 - Offer Portfolio Map.md` and `01_Canon/03 - Product and Channel Hierarchy.md`.
2. **New note?** It belongs in exactly one folder. If it seems to belong in two, it is probably two notes, or it belongs in `01_Canon/`.
3. **Superseding something?** Move the old note to `98_Archive/`, add a supersession banner pointing at the replacement. Never delete.
4. **Using a legacy name?** Don't. Check §4 for the canonical name.
5. **Publishing a number?** It needs a truth label, a source, and a matching model.
