---
project: B_RealEstate
title: "Vault Manifest"
type: vault_manifest
status: Active v2.0
owner: Esteban
last_updated: 2026-09-23
tags: [manifest, ai-handoff]
---

# Vault Manifest

## Latest — 2026-09-23 Architecture Migration

The vault was restructured from the accreted `00_Index`…`19_Canonical_B_RealEstate` tree into a coherent 16-folder architecture. **263 files moved, 0 lost.** Full definition and old→new mapping: [[Vault Architecture Map]].

- **Two parallel vaults eliminated.** `18_Ecosystem/` and `19_Canonical_B_RealEstate/` both covered company/strategy/product/finance/operations. They are dissolved; one topic now has one home.
- **`02_Offers/` created** — one first-class folder per sellable thing, with a standard skeleton and an honest `00 - README.md` naming real gaps. This replaces `04_Product/` meaning "BluePrint only".
- **Canon sorts first** as `01_Canon/`; precedence is now impossible to miss.
- **Legacy names removed from the folder tree:** `13_White_Label` → `02_Offers/06_B_Partner`, `12_Private_Collection` → `08_Dproperty_Select`, `11_Developer_Sales_OS` → `07_Developer_Partnerships`, `14_CRM_GoHighLevel` → `02_BlankCRM`.
- **`98_Archive/` created** for superseded strategy, business plan, pitch, product, execution material, session closeouts, exports and parked concepts. Evidence only, never guidance.
- **README in every folder** stating what it holds, what is current and what is missing.
- **Stale-figure banners** added to 17 live notes still carrying the retired $650k ask or retired pricing — the model internals were *not* rewritten, because inventing replacement numbers would be fabrication.
- **Authority is now a property of documents, not folders.** Truth labels `[F] [D] [M] [A] [T] [R]` carry precedence.
- **Verifier added:** `.tools/verify_vault.py` checks broken wikilinks, stale paths, retired vocabulary and README coverage. Currently passing clean.

## Latest — 2026-09-23 Canonical Reconciliation

The vault had **two competing canonical layers** three days apart. They are now reconciled by [[../01_Canon/00 - Precedence and Canonical Reconciliation]], which controls the vault.

- **BluePrint definition merged, not chosen between.** It is a chat-first AI management OS **whose system of record is the verified transaction, commission and management-control record, beginning at qualified opportunity.**
- The *property/project/unit inventory and MLS* ambition stays **permanently retired**. The *transaction and commission record* is reinstated as the wedge.
- **Academy** is canonical; `19_Canonical`'s "Building Blocks" is a legacy alias.
- **B_ Partner** is canonical; "White-Label" is a legacy alias.
- BluePrint pricing moved to **Core $399 / Growth $799 / $1,500 setup**; $299/$599/$999 retired.
- Raise is **$950k capitalization / $800k 18-month plan**, staged; $650k and $1.5M both retired.
- Precedence order and truth labels (`[F] [D] [M] [A] [T] [R]`) are now vault-wide standards.
- `00_Start_Here/Dproperty OS - Master Index.md` renamed to `00_Start_Here/Master Index.md`; inbound links fixed.

### Three-layer architecture

| Layer | Answers | Folder |
|---|---|---|
| Company canon | What the company **is** | `01_Canon/` |
| Product canon | What the product **is** | `02_Offers/01_BluePrint/` |
| Proof canon | How it is **proven and financed** | `01_Canon/` |

## Previous — 2026-09-20 Ecosystem Reset

- B_RealEstate changed from franchise-first to **product-led operating infrastructure**.
- Canonical hierarchy: **BluePrint / BlankCRM / VAULTED / Academy**.
- Dproperty Franchise, B_ Partner and Developer Partnerships became channels/packages.
- BlankCRM created as sellable GHL-powered front office.
- VAULTED elevated as network/transaction engine.
- DpropertyLiving parked.
- Physical hub downgraded to optional long-term vision.
- Old TAM/SAM/SOM, Y5 forecast and $650k funding plan marked historical.

## Canonical entrypoints

[[../01_Canon/00 - Precedence and Canonical Reconciliation]] ← **start here**
[[Project Context Brief]]
[[Decision Log]]
[[Open Questions]]
[[Current Priorities]]
[[Master Index]]
[[../01_Canon/README]]
[[../01_Canon/03 - Product and Channel Hierarchy]]
[[../02_Offers/01_BluePrint/00 - README]]
[[../98_Archive/Superseded Canon/19_Canonical README]]
[[../11_Execution/Deliverables Tracker - Compact MD]]

## Status of each folder

| Folder | Status |
|---|---|
| `00_Start_Here/` | **Current** — reconciled 2026-09-23 |
| `03_Strategy/` | Mostly **superseded** (pre-reset); banner-marked |
| `04_Business_Plan/` | Mostly **superseded**; `B_ Business Model Reset - 2026-09-20` is current |
| `05_Pitch_and_Investor/` | `Pitch Deck Outline` current; rest superseded |
| `02_Offers/01_BluePrint/` | `BluePrint/` subfolder **canonical**; loose files historical |
| `02_Offers/05_Dproperty_Franchise/` | **Valuable operating source material**; channel-scoped, not company strategy |
| `07_Legal_and_Compliance/` | Notes valid; economics must be reconciled before contract use |
| `06_Finance/` | **Superseded** by `19_Canonical/06_FINANCE` + named workbooks |
| `13_Research/` | Active backlog |
| `98_Archive/Exports/` | **Historical evidence only** |
| `99_Templates/` | Current |
| `02_Offers/07_Developer_Partnerships/` | Channel = **Developer Partnerships** |
| `02_Offers/08_Dproperty_Select/` | Channel/asset = **Dproperty Select** |
| `02_Offers/06_B_Partner/` | Channel = **B_ Partner** |
| `02_Offers/02_BlankCRM/` | Engine behind **BlankCRM** |
| `10_Brand_and_Web/` | Current |
| `11_Execution/` | Tracker current; July roadmaps historical |
| `12_Handoffs/` | Regenerate against reconciled canon before external use |
| `01_Canon/` | **Company canon + precedence** |
| `01_Canon/` | **Finance / data-AI / operations / diligence canon** |

## Historical note

The vault contains extensive July/August franchise-first material. **Preserve it** for operating, legal and historical value — but the 2026-09-23 reconciliation and the 2026-09-20 reset take precedence wherever strategy, product scope, market sizing, forecast or funding assumptions conflict. Nothing is deleted; old thinking is evidence.
