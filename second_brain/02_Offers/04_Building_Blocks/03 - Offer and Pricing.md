---
project: B_RealEstate
title: "Building Blocks — Offer and Pricing"
type: pricing
status: Working hypothesis — validate before publication
owner: Esteban
last_updated: 2026-09-24
tags: [offer, building-blocks, pricing]
---

> [!IMPORTANT] Precedence
> [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · [[../../01_Canon/04 - Offer Portfolio Map]] · [[../../01_Canon/09 - Unit Economics Registry]]

> [!WARNING] These are hypotheses, not validated prices
> Every figure below is `[A]` **Assumption**. No paid external cohort has run. Do not publish externally before the LMS cost base is quoted and the economics approved.

# Building Blocks — Offer and Pricing

## Pricing philosophy

**Price per enrollment and per cohort, not per organization seat.**

This is deliberately different from BluePrint (priced per organization) and BlankCRM (priced per sub-account). Learning is consumed by *individuals* on an *episodic* basis, and pricing should follow consumption. It also means Building Blocks revenue scales with headcount growth inside an existing customer — a genuine expansion lever that BluePrint's org-level pricing does not provide.

## The four revenue lines

| # | Line | What is sold | Price `[A]` | Buyer |
|---|---|---|---|---|
| 1 | **Core onboarding** | Launch-readiness curriculum for a new franchise or partner team | **Included** in the franchise/partner package — allocated internally, not free | Franchise / B_ Partner |
| 2 | **Paid specialist courses** | Individual enrollments: investing, project sales, compliance ops, leadership, advanced product | **$199** blended per enrollment | Agency, individual professional |
| 3 | **Certification** | Assessment + certificate + expiry/renewal cycle | **$199–$349** per program *(range undefined — see gaps)* | Agency, individual, franchise |
| 4 | **Enterprise / developer cohort** | Branded closed cohort, project-specific training, manager dashboards | **Scoped licence + setup — quoted** | Developer, large agency |

**Volume assumption:** 1.5 paid enrollments per customer per year `[A]`.

## Standalone vs bundled — the allocation rule

Building Blocks is sold three ways, and the accounting must not blur them:

1. **Standalone** — direct to an agency or individual with no other B_ product. This is the test of whether it is genuinely a product.
2. **Attached** — to a BluePrint or BlankCRM customer as paid expansion.
3. **Included** — inside the Dproperty Franchise and B_ Partner packages.

> **Binding rule:** when Building Blocks is included in a package, its value is **allocated at standalone list price** inside the model, and the package price must reconcile. It is never counted twice, and it is never recorded as $0 — "included" is a discount decision, not an absence of cost or value.

See [[../../01_Canon/09 - Unit Economics Registry]].

## Why "included" must still carry a price

If core onboarding is modelled at zero, three things break:

- the franchise package cannot show credible bundled value;
- LMS hosting and content-maintenance cost has no revenue line to sit against, so gross margin is overstated elsewhere;
- there is no basis for pricing the product standalone, because nobody ever priced it.

## Modelled revenue — from the standalone ecosystem projection `[M]`

| | Y1 | Y3 | Y5 |
|---|---|---|---|
| Building Blocks revenue | $8.6k | $84.2k | $320.9k |

Source: `06_Finance/Standalone Ecosystem Projection.md`. These are **model outputs on unvalidated assumptions**, not forecasts. Note the shape: this is a real revenue line but it is an order of magnitude below BluePrint — which is exactly the correct relationship.

## Value logic

The product is easy to justify if:

- a new franchise reaches launch readiness **faster and more consistently** than with shadowing and manuals;
- certification gating measurably reduces compliance and process failures;
- a manager can see a competency gap and act on it without building training themselves;
- an individual professional will pay for a course that is visibly tied to how real transactions are run.

If buyers perceive it as "generic real-estate videos," $199 will not hold — there is abundant free content. **The defensibility is the loop with BluePrint, not the courseware.**

## Gaps blocking publication `[R]`

1. **No LMS cost base.** Open edX hosting, support and platform cost per learner is unquoted. This is a named evidence gap in `01_Canon/13 - Status Dashboard`.
2. **Certification price range undefined** ($199–$349 is a placeholder spread, not a decision).
3. **Content production cost unmodelled** — curriculum build and per-process maintenance.
4. **Enterprise/developer cohort has no price structure**, only "quoted."
5. **No standalone demand evidence.** Nobody outside the ecosystem has been asked to pay.
6. **Content IP ownership undocumented** — see the missing `06 - Legal.md`.

## Metrics to validate

Willingness to pay at $199 standalone · enrollments per customer per year · completion rate (a low completion rate destroys renewal) · certification renewal rate · gross margin after LMS and content cost · attach rate to BluePrint · whether standalone buyers exist at all.
