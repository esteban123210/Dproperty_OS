---
project: B_RealEstate
title: "Building Blocks — Economics"
type: unit_economics
status: Modelled v1.0 — LMS market rates sourced 2026-09-24
owner: Esteban
last_updated: 2026-09-24
tags: [offer, building-blocks, economics, unit-economics, cogs]
---

> [!IMPORTANT] Precedence
> [[../../01_Canon/09 - Unit Economics Registry]] is the registry of record · principle: [[../../01_Canon/19 - Portfolio Composition Principle]]

# Building Blocks — Economics

> **Status change 2026-09-24.** This note previously stated that gross margin **could not be stated** because no LMS cost base existed. Managed Open edX market rates are now sourced, so the platform cost is bounded and a margin can be modelled. A binding vendor quote is still required before spending. `[R]`

## Why this product's economics differ

| | BluePrint | BlankCRM | **Building Blocks** |
|---|---|---|---|
| Revenue unit | Organization/month | Office/month | **Enrollment (episodic)** |
| Recurring? | Yes | Yes | **Repeat, not recurring** |
| Scales with | Customer count | Customer count | **Headcount inside customers** |
| Dominant cost | AI, integrations, support | Support labour | **Content production + maintenance** |
| Margin shape | High, improving | High, improving | **High per marginal enrollment, heavy fixed content cost** |

> **Binding rule:** enrollment revenue is **repeat, not recurring**. It must **never** be reported as ARR. The ARR definition in [[../../01_Canon/12 - Glossary and Metric Dictionary]] explicitly excludes course enrollments. Investors check this.

## Platform cost — now bounded `[F]` market rates

| Option | Cost | Capacity | Per-MAU/month |
|---|---:|---|---:|
| Managed shared (e.g. Edunext EC Core) | **$8,000/year** (~$667/mo) | ≤1,500 monthly active users | **~$0.44** |
| Managed at scale | — | larger | **<$0.50** |
| Self-hosted + support package (e.g. Raccoon Gang) | ~$150/mo hosting + ~$1,200/mo support ≈ **$16,200/year** | varies | varies |
| Dedicated instance (e.g. Edunext Stratus) | **$25,000/year** (~$2,083/mo) | unlimited learners | — |

**Planning assumption: $8,000–$16,000/year (~$667–$1,333/month)** for the realistic early-stage footprint. Dedicated hosting is not justified until learner volume demands it.

**Per-learner platform cost is effectively negligible (<$0.50/MAU).** The constraint is the fixed annual commitment, not variable cost.

## Content production cost `[A]`

Market reference: a full Open edX package including deployment, mobile app, analytics and gamification runs **$20,000–$35,000** as a build engagement. That is a useful ceiling for *platform* build, but **content is separate and is the real cost**.

| Item | Estimate | Label |
|---|---|---|
| Curriculum build per module | 20–40 hrs | `[A]` |
| Modules for core franchise onboarding | 12–20 | `[A]` |
| Loaded content-production rate | $30–60/hr | `[A]` |
| **Core curriculum build (one-off)** | **$7,200–$48,000** | `[A]` wide — needs scoping |
| **Annual content maintenance** | **15–30% of build cost per year** | `[A]` |

The build range is uncomfortably wide because module count and depth have never been scoped. **Scoping the core curriculum is the first task**, not quoting vendors.

## Breakeven — the number that matters

At **$199** blended per enrollment, with negligible marginal delivery cost:

| Platform commitment | Enrollments/year to cover platform |
|---|---:|
| $8,000/year | **~40** |
| $16,000/year | **~80** |
| $25,000/year | **~126** |

Adding content amortization over three years at a $20,000 build:

| Annual cost base | Enrollments/year to break even |
|---|---:|
| $8,000 platform + $6,667 content | **~74** |
| $16,000 platform + $6,667 content | **~114** |

**Sanity check against the model:** the standalone projection shows Building Blocks revenue of **$8.6k in Y1** — roughly **43 enrollments**. That is *below* the breakeven of any scenario that includes content amortization, and only just covers the cheapest platform tier.

**Building Blocks loses money in Year 1 under every scenario modelled.** It reaches breakeven somewhere in Y2 and the projected **$84.2k in Y3** (~423 enrollments) is comfortably profitable. This is a normal fixed-cost-then-scale shape, but it must be stated plainly rather than presented as an immediately profitable product line.

## Gross margin at steady state

Once platform and content are covered, the **marginal enrollment is ~95%+ gross margin** — there is no meaningful per-learner cost. The blended margin depends entirely on volume against the fixed base:

| Annual enrollments | Revenue | Cost base `[A]` | Blended GM |
|---:|---:|---:|---:|
| 100 | $19,900 | ~$14,700 | **~26%** |
| 250 | $49,750 | ~$14,700 | **~70%** |
| 500 | $99,500 | ~$16,000 | **~84%** |

## The real economic risk — content as a subscription

**Content is a fixed cost that behaves like a recurring one.**

Seven processes in `08_Operations/Process Library/` × multiple roles × multiple markets, plus localization. Every process change makes a module stale. Maintenance burden compounds with **market count**, not with revenue.

A learning product with stale content stops converting and starts generating refund pressure. **Model content maintenance as an ongoing operating cost from day one** — 15–30% of build cost annually. This is the most likely path to Building Blocks quietly losing money while appearing profitable on a per-enrollment basis.

**Mitigation:** treat the Process Library as the single source and build modules to reference it, so a process change triggers a known, bounded module-update list rather than an unbounded audit.

## Allocation rule — binding

When Building Blocks is included in a franchise or partner package:

1. allocate at **standalone list price**;
2. package price must **reconcile** to allocated components less an explicit stated discount;
3. **never** record at $0 — that hides both value and cost;
4. **never** double-count in both the package line and the product line.

## Gate — do not spend ahead of this

**Do not invest in content production beyond core franchise onboarding until:**
1. the core curriculum is **scoped** (module count and depth) — the $7k–$48k range must narrow;
2. a **binding LMS quote** is obtained `[R]`;
3. **attach is demonstrated** — enrollments triggered by real BluePrint process signals with real customers.

Bundled enablement is justified by franchise consistency and retention alone. **Standalone expansion revenue must earn its own investment.**

## Still `[A]` / `[R]`

- `[R]` **Binding LMS quotation** — market rates are sourced, but no quote obtained.
- `[R]` **Core curriculum scope** — module count/depth undefined, which is why the build estimate spans 7×.
- `[R]` **Content IP ownership and certification claim limits** — no `06 - Legal.md` exists, and this product issues certificates.
- `[A]` Content production and maintenance rates carry no delivery history.
- `[A]` $199 blended enrollment and 1.5 enrollments/customer/year are untested.
- `[A]` Whether a standalone buyer exists outside the ecosystem — see `02 - ICP`, which rates the individual-professional segment weak.

## Sources

- [Open edX Hosting Guide — Edunext](https://www.edunext.co/articles/open-edx-hosting-how-to-choose-the-right-plan-without-sinking-your-platform/) — EC Core $8,000/yr ≤1,500 MAU; <$0.50/MAU at scale; Stratus $25,000/yr
- [LMS Pricing Guide — Raccoon Gang](https://raccoongang.com/blog/how-much-does-a-custom-lms-cost/) — ~$150/mo hosting, ~$1,200/mo support, $20k–$35k package
- [Open edX Service Providers — Edly](https://edly.io/blog/openedx-service-providers/) — provider comparison
