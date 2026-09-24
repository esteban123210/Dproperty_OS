---
project: B_RealEstate
title: "2026-09-23 - Vault-Wide Canonical Alignment"
type: session_closeout
status: Complete
owner: Esteban
last_updated: 2026-09-23
tags: [closeout, governance, reconciliation]
---

> [!IMPORTANT] Precedence
> [[../../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]] controls the vault.

# 2026-09-23 — Vault-Wide Canonical Alignment

## 1. Session summary

**Goal:** treat `01_Canon/` as the base of truth, go document by document through the Second Brain, update every file to match, resolve collisions on business merit, and leave the vault with a correct architecture and working AI handoffs.

**The central problem found:** the vault contained **two competing canonical layers** created three days apart, and neither was marked as losing.

| | `01_Canon/` + `02_Offers/01_BluePrint/` (09-20) | `01_Canon/` (09-23) |
|---|---|---|
| BluePrint | Management-control layer; transaction spine **explicitly retired** | **Transaction spine**: qualified opportunity → close → commission |
| 4th product | Academy (bundled) | Building Blocks (commercial) |
| Own-brand channel | B_ Partner | White-Label |
| Pricing | $299 / $599 / $999 | $1,500 setup + $399 / $799 |
| Raise | $650k retired | $950k / $800k |

`CLAUDE.md` pointed at `19_Canonical` as authoritative while `02_Offers/01_BluePrint/11 - Decision Record` said the opposite. Any AI assistant reading the vault would contradict itself.

## 2. The decision

**The two definitions were never mutually exclusive. They were merged, not chosen between.**

> **BluePrint is a chat-first, AI-native management operating system for small and growing real-estate agencies, whose system of record is the verified transaction, commission and management-control record, beginning at qualified opportunity.**

The `18_Ecosystem` strategic frame wins (product-led, CRM-agnostic, one authority per data class, verification hierarchy, franchising is a channel). The `19_Canonical` transaction/commission object wins as BluePrint's core entity.

### Why, business-wise

1. **You cannot verify what you do not hold.** The Reported → Operationally verified → Financially verified → Closed hierarchy *is* a transaction lifecycle; its own example is a CRM deal becoming verified in BluePrint.
2. **A management layer with no owned transaction object is a BI tool** — the "another dashboard" product the ICP explicitly fears. It will not sustain $399–$799/month.
3. **Commission calculation and deal-file compliance are the real, expensive, defensible pain**, and are what spreadsheets do badly.
4. `03 - Architecture` already conceded "receivables, commission liabilities."
5. `19_Canonical`'s MVP gate is falsifiable and worth keeping.

### What stays retired — permanently

Property/project/unit **inventory** · listings · MLS · pre-qualification pipeline · GL/tax/payroll · property management · LMS delivery · marketplace listings · escrow/custody/FX.

**Boundary in one line:** BluePrint owns *the deal as a governed management object*; it does not own *the property as inventory*.

## 3. Decisions made

1. **Three-layer architecture with one precedence order.** `01_Canon/` = what the company is · `02_Offers/01_BluePrint/` = what the product is · `01_Canon/` = how it is proven and financed.
2. **BluePrint definition merged** (above).
3. **Naming:** Academy (not Building Blocks) · B_ Partner (not White-Label) · Dproperty Select (not Private Collection) · Developer Partnerships (not Developer Sales OS) · BluePrint (not Dproperty OS / Plano / La Plataforma). DpropertyLiving parked.
4. **Pricing:** Core $399 · Growth $799 · $1,500 setup, per organization. Scale quoted, undefined.
5. **Capital:** $950k capitalization / $800k 18-month plan, staged. $650k and $1.5M both retired.
6. **Vault-wide truth labels** `[F] [D] [M] [A] [T] [R]` and the `DRAFT → REVIEW → APPROVED → SUPERSEDED → ARCHIVED` lifecycle.

## 4. Significant recovery

The 2026-09-20 reset replaced three product notes with redirect stubs. Those files held the **transaction-spine design work that is now back in scope** — **1,427 lines**, recoverable from git commit `ff84d37^`:

| File | Lines |
|---|---|
| `BluePrint Wireframe - Back Office OS (Developer Handoff).md` | 918 |
| `BluePrint Golden Workflow - Wireframe and Validation.md` | 432 |
| `Data Model.md` | 77 |

Each stub now carries a recovery command. **Review before reuse** — the pre-reset versions may also contain inventory/MLS scope, which stays retired.

## 5. Work done

- **256 markdown files** reviewed; **100% now reference the precedence note**.
- **0 broken wikilinks** (verified programmatically).
- **0 unmarked retired claims** — every instance of the retired tiers, funding asks, "one database", "CRM propio" and "Building Blocks" now sits in a file that marks it as retired, legacy or historical.
- **Fixed a pre-existing YAML bug in 20 files** where a banner had been placed *above* the frontmatter, breaking Obsidian's property parsing.
- Created: the precedence note, AI Handoff Pack file `00`, this closeout.
- Rewrote: `CLAUDE.md`, `Project Context Brief`, `Vault Manifest`, `Current Priorities`, `AI Handoff Pack - Read Me`, `07_Latest Session Closeout`.
- Renamed `Dproperty OS - Master Index.md` → `Master Index.md`, all inbound links fixed.
- Normalized all 92 `project: Dproperty OS` frontmatter fields to `B_RealEstate`.
- Amended the whole `02_Offers/01_BluePrint/` folder to carry the transaction spine.
- Banner-marked every folder by category: superseded-historical, channel-scoped, or verified-current.

## 6. Open — needs Esteban's ratification

1. The reconciled **BluePrint definition**.
2. Whether a **Scale tier** exists, and its contents/price.
3. The **$950k / $800k** envelope as the single current position.
4. **Academy over Building Blocks** as the commercial name.

Also newly open: the **franchise royalty structure** (6% + 1% fund vs 4% no fund vs flat 6% + 1.5%) needs contract design and local advice.

**Pitch decks and the financial model should not be rebuilt until items 1–3 are ratified.**

## 7. Next session

1. Ratify the four items above.
2. Recover the golden-workflow and wireframe specs from git; strip inventory scope.
3. Rebuild the investor deck on the reconciled hierarchy.
4. Rebuild the integrated financial model on $399/$799 + $950k.
5. Regenerate `12_Handoffs/` against reconciled canon.

**Open first next session:** [[../../01_Canon/00 - Precedence and Canonical Reconciliation]], then [[../Current Priorities]].

## 8. Git

Baseline before this work: `f51c9f0`. All changes are uncommitted and revertible.
