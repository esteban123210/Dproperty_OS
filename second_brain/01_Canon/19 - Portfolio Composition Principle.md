---
project: B_RealEstate
title: "Portfolio Composition Principle"
type: decision_record
status: Canonical v1.0
owner: Esteban
date: 2026-09-24
last_updated: 2026-09-24
tags: [canon, products, portfolio, packaging, pricing, decision]
---

> [!IMPORTANT] Precedence
> [[00 - Precedence and Canonical Reconciliation]] controls the vault. This note refines its §3 product definitions and reverses its §4 Academy/Building Blocks position.

# Portfolio Composition Principle — 2026-09-24

## The principle

> **Every product in the portfolio is separately definable, separately priced and separately sellable — so that a package is a composition of named products, never one monolith.**

Four strong products sell better than one product that "has it all."

## The decision

**Building Blocks is a standalone product**, not a bundled enablement layer. This **reverses** the 2026-09-23 position that demoted it to "Academy, a bundled layer."

Canonical name: **Building Blocks**. Legacy aliases: *Academy*, *B_Academy*, *Training Academy*.

## Why — the commercial argument

A franchise or partner buyer evaluating:

> *"You get the B_ platform."*

is evaluating one thing of uncertain scope. A buyer evaluating:

> *"You get **BluePrint** to run the company, **BlankCRM** to sell, **Building Blocks** to train and certify your team, and **VAULTED** for network deal flow."*

is evaluating four things, each of which they can price in their head against an alternative they already know. That is a materially stronger offer at the same underlying cost:

1. **Perceived value is additive.** Named components each anchor their own worth. "Platform" anchors nothing.
2. **The bundle discount becomes credible.** You can only show "this would cost $X separately" if each part has a standalone price.
3. **It forces honest product design.** A component that cannot survive as a standalone product is a feature pretending to be one — better to find that out deliberately.
4. **Expansion revenue gets a path.** Building Blocks priced per enrollment grows with headcount inside an existing customer; BluePrint's org-level pricing does not.
5. **Each product can find its own market.** BlankCRM can acquire agencies that will never buy BluePrint. Building Blocks can reach professionals who buy nothing else.

## The obligations this creates

Calling something a product is a commitment, not a label. Each product must have:

| Requirement | Why |
|---|---|
| Its own **definition and boundaries** | What it owns, and explicitly what it does not |
| Its own **ICP** | Who buys it *when they buy nothing else* |
| Its own **price** | A published standalone list price |
| Its own **economics** | Revenue model, cost drivers, gross margin |
| Its own **P&L line** | Visible separately in the model |
| Its own **legal terms** | Its own risk surface |

**A product without a standalone price is not a product.** That is the test.

## The allocation rule — binding

When a product is included in a package (franchise, B_ Partner, developer):

1. allocate it at **standalone list price** inside the model;
2. the package price must **reconcile** to the sum of allocated components less an **explicit, stated discount**;
3. **never** record an included product at $0 — that hides both its value and its cost;
4. **never** double-count it in both the package line and the product line.

"Included" is a discount decision. It is not an absence of value or of cost.

## What this does NOT change — the investor hierarchy

Commercial packaging and investment thesis are **different conversations for different audiences.** Both are true simultaneously:

| Audience | Frame |
|---|---|
| **Customer / franchisee** | Four named products, each with standalone value, composed into a complete package |
| **Investor** | Proprietary value concentrates in **BluePrint** (transaction/management IP) and **VAULTED** (network effect). BlankCRM is efficient capital allocation on rented infrastructure. Building Blocks is retention, quality and attach revenue. |

Adobe sells many products; investors still know which ones matter. There is no dishonesty in a strong product portfolio with a concentrated moat — **the dishonesty would be implying the moat is broader than it is.**

**Pitch rule unchanged:** BluePrint core SaaS → VAULTED network upside → BlankCRM attach → Building Blocks and channels. Never present all boxes as equal businesses. See [[03 - Product and Channel Hierarchy]].

## The risk to manage

Multiple standalone products create **portfolio drag**: each one demands pricing work, positioning, legal terms, support, roadmap and content maintenance. That cost is real and scales with product count.

**Mitigation — a hard sequencing rule:**

- **BluePrint gets the engineering capital.** It is the only product currently in active build.
- Other products earn investment by **demonstrating attach or standalone demand**, not by existing on the portfolio map.
- A product may be *fully defined* in the vault while being *deliberately unfunded*. That is the correct state for VAULTED and largely for Building Blocks today.

Being a named standalone product does **not** grant a budget.

## Consequences applied

| Area | Change | Status |
|---|---|---|
| `02_Offers/04_Building_Blocks/` | Folder renamed from `04_Academy`; promoted to standalone product | ✅ done |
| Building Blocks `03 - Offer and Pricing` | Created — four revenue lines, $199 blended enrollment `[A]` | ✅ done |
| Building Blocks `02 - ICP`, `05 - Economics` | Created | ✅ done |
| Naming tables vault-wide | Building Blocks canonical; Academy/B_Academy legacy | ✅ done |
| [[04 - Offer Portfolio Map]], [[03 - Product and Channel Hierarchy]] | Updated | ✅ done |
| [[09 - Unit Economics Registry]] | Building Blocks as its own engine with the allocation rule | ✅ done |
| **BlankCRM standalone price** | Still open — blocked on GHL COGS. The principle now makes this **required**, not optional. | ⬜ `[R]` |
| **Building Blocks `06 - Legal.md`** | Missing — certification claims and content IP | ⬜ `[R]` |
| **Package reconciliation model** | Franchise/partner package prices must reconcile to allocated components | ⬜ `[R]` |

## Open items this decision creates

1. **Every product needs a standalone list price.** BlankCRM has none. That is now a blocker, not a nicety.
2. **Franchise and B_ Partner package prices must be rebuilt** as allocated components plus an explicit discount.
3. **Does Building Blocks have a standalone buyer at all?** Segments 1–3 are plausible; the individual-professional segment is weak. See its `02 - ICP`.
4. **Content maintenance cost** must be modelled as recurring, driven by process-change rate.

Tracked in [[../00_Start_Here/Open Questions]].
