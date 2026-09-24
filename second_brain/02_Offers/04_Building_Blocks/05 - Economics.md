---
project: B_RealEstate
title: "Building Blocks — Economics"
type: unit_economics
status: Skeleton — cost base unquoted
owner: Esteban
last_updated: 2026-09-24
tags: [offer, building-blocks, economics, unit-economics]
---

> [!IMPORTANT] Precedence
> [[../../01_Canon/09 - Unit Economics Registry]] is the registry of record. This note holds the Building Blocks engine only.

> [!WARNING] This is a structure, not a model
> The revenue side has hypotheses. **The cost side has no quotes at all.** Gross margin cannot be stated. Do not use this note to support spending or investor claims. `[R]`

# Building Blocks — Economics

## Why this product needs its own economics

Building Blocks is a standalone product, so it carries a standalone P&L line. Its economics are **structurally different** from the rest of the portfolio:

| | BluePrint | BlankCRM | **Building Blocks** |
|---|---|---|---|
| Revenue unit | Organization / month | Sub-account / month | **Enrollment (episodic)** |
| Recurring? | Yes | Yes | **No — repeat, not recurring** |
| Scales with | Customer count | Customer count | **Headcount inside customers** |
| Main cost driver | AI, integrations, support | GHL licence, messaging | **Content production + LMS platform** |
| Margin shape | High, improving | Thin, resale spread | **High per marginal enrollment, heavy fixed content cost** |

**The critical distinction:** enrollment revenue is **repeat, not recurring**. It must never be modelled as ARR. Doing so would overstate recurring revenue quality — a specific thing investors check.

See the ARR definition in [[../../01_Canon/12 - Glossary and Metric Dictionary]], which explicitly excludes course enrollments.

## Revenue model

```
paid enrollment revenue
  = eligible learners
  × enrollments per learner per year (1.5 [A])
  × blended price ($199 [A])

+ certification program fees
+ enterprise/developer cohort licences (quoted)
+ allocated value of core onboarding included in packages
```

`[M]` Modelled output from `06_Finance/Standalone Ecosystem Projection.md`: **$8.6k Y1 → $84.2k Y3 → $320.9k Y5.**

## Cost structure — all unquoted `[R]`

| Cost | Type | Status |
|---|---|---|
| Open edX hosting / platform licence | Fixed + per-learner | **No quote.** Named evidence gap. |
| LMS implementation and integration to BluePrint | One-off | Not scoped |
| **Content production** — curriculum build per role/process | **Fixed, front-loaded, large** | Not estimated |
| **Content maintenance** — updating modules when a process changes | **Recurring, chronically underestimated** | Not estimated |
| Assessment design and certification administration | Recurring | Not estimated |
| Instructor / cohort delivery (enterprise line) | Variable per cohort | Not estimated |
| Learner support | Variable | Not estimated |

## The real economic risk

**Content is a fixed cost that behaves like a subscription.**

Every process in `08_Operations/Process Library/` that changes makes its module stale. Seven processes, multiple roles, multiple markets, plus localization — the maintenance burden compounds with market count, not revenue.

A learning product with stale content stops converting and starts generating refund pressure. **Model content maintenance as an ongoing operating cost from day one, not a one-time build.** This is the single most likely way this product quietly loses money while appearing profitable.

## Allocation rule — binding

When Building Blocks is included in a franchise or partner package:

1. allocate at **standalone list price** inside the model;
2. the package price must **reconcile** to the sum of allocated components less an explicit, stated discount;
3. **never** record it at $0 — that hides both the value and the cost;
4. **never** double-count it in both the package line and the product line.

## What must be built before this note is usable

1. Open edX / LMS quotation — platform, hosting, support, per-learner cost.
2. Content production estimate — hours per module, modules per role, cost per hour.
3. Content maintenance estimate — expected module-change rate driven by process changes.
4. Certification administration cost.
5. Gross margin per enrollment, then per customer per year.
6. Standalone CAC — almost certainly prohibitive for the individual segment; needed to confirm or kill it.

## Gate

**Do not invest in content production beyond franchise onboarding needs until:**
- the LMS cost base is quoted, and
- attach-driven enrollments are demonstrated with real BluePrint customers.

Bundled enablement is justified by retention and franchise consistency alone. **Standalone expansion revenue must earn its own investment.**
