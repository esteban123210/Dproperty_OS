---
project: B_RealEstate
title: "BlankCRM — Economics"
type: unit_economics
status: Historical cost model — full-lifecycle scope requires pilot validation
owner: Esteban
last_updated: 2026-09-29
tags: [offer, blankcrm, economics, unit-economics, cogs]
---

> [!IMPORTANT] Precedence
> [[../../01_Canon/09 - Unit Economics Registry]] is the registry of record · [[../../06_Finance/Pricing Unit Economics and Revenue Policy]] holds the portfolio policy.

# BlankCRM — Economics

> **Scope correction 2026-09-29.** The tables below preserve the earlier subscription and labour assumptions for comparison. They do **not** establish price or margin for the corrected full-lifecycle BlankCRM product. Legal workflows, approval rules, contract templates, payment/commission mapping, integrations, QA and role training may materially raise onboarding and support cost. Measure these in the pilot and revise this model before confirming the package economics.

## The structural finding

**The earlier model assumed near-zero marginal platform cost.** This does not mean near-zero marginal delivery, integration, usage or support cost.

| Vendor fact | Source | Consequence for BlankCRM |
|---|---|---|
| Agency Pro **$497/month** | `[F]` published | One fixed platform cost for the whole book of business |
| **Unlimited sub-accounts** on Unlimited and Agency Pro | `[F]` published | Each additional customer costs **$0** in platform fees |
| **SaaS Mode requires Agency Pro** | `[F]` published | $497 is mandatory, not optional, to sell BlankCRM as a product |
| **Rebill phone/email/AI usage with markup** (Pro only) | `[F]` published | Messaging and AI are **pass-through at a margin**, not a cost centre |
| AI Employee add-ons $50/month Growth or $97/month Unlimited per sub-account (published 2026-09-29) | `[F]` published | Optional; select only after pilot use case and costs are approved |

Vendor cost is one input. Full-lifecycle gross margin also depends on implementation, third-party integrations, usage, support and exception handling. The tables below are scenarios, not observed margins.

## Cost structure

| Cost | Type | Amount | Label |
|---|---|---|---|
| GHL Agency Pro platform | **Fixed** (whole business) | $497/month | `[F]` |
| Marginal platform cost per customer | Variable | **$0** | `[F]` |
| SMS / email / voice / AI usage | Variable | Rebilled with markup | `[F]` capability; `[A]` markup rate |
| Onboarding labour | One-off per customer | 8–12 hrs `[A]` | `[A]` |
| Ongoing support labour | Variable per customer | 0.5–1.5 hrs/month `[A]` | `[A]` |
| Loaded labour rate | — | $25–40/hr `[A]` | `[A]` |

## Historical gross-margin scenario at $249/month list

Platform cost is fixed, so margin **improves with customer count** — the opposite of a per-seat resale model.

| Customers | Platform cost allocated | Support labour `[A]` | Gross margin | GM % |
|---:|---:|---:|---:|---:|
| 5 | $99.40 | $12.50–$37.50 | $112–$137 | **45–55%** |
| 10 | $49.70 | $12.50–$37.50 | $162–$187 | **65–75%** |
| 25 | $19.88 | $12.50–$37.50 | $192–$217 | **77–87%** |
| 50 | $9.94 | $12.50–$37.50 | $202–$227 | **81–91%** |

**Platform-fee coverage in this simplified scenario: 2–3 customers at $249/month.** This is not full-business breakeven.

## Historical onboarding scenario at $750 setup

| Item | Amount |
|---|---:|
| Setup fee | $750 |
| Onboarding labour at 8–12 hrs × $25–40/hr | $200–$480 `[A]` |
| **Contribution** | **$270–$550** |

This contribution exists only if the 8–12-hour assumption holds for the full scope. Instrument actual hours by module and revise the model.

## What this means commercially

1. **The price is unproven for the corrected scope.** Compare pilot labour, integrations, usage and support with the hypothesis before confirming it.
2. **Margin depends on package design and delivery discipline.** Every extra hour of support costs against a $249 monthly ticket if that list price is retained.
3. **Usage should be rebilled, not absorbed.** Agency Pro allows markup; absorbing messaging cost would convert a margin line into a variable cost with no ceiling.
4. **Attach economics are excellent.** At a 35% attach rate to BluePrint `[A]`, BlankCRM adds meaningful contribution with no incremental platform cost.

## The risks that actually matter

| Risk | Severity | Note |
|---|---|---|
| **Single-vendor dependency** | **High** | The entire product is GoHighLevel. A price change, terms change, feature removal or outage hits every customer at once. There is no second source. |
| GHL raises Agency Pro price or restricts SaaS Mode | Medium | Fixed cost is small, so absorbable — but re-check annually. |
| GHL changes rebilling terms | Medium | Would convert usage from margin to cost. |
| Support load exceeds 1.5 hrs/customer/month | **High** | The main margin destroyer. Instrument from customer one. |
| Onboarding exceeds 15 hours | Medium | Turns the setup fee into a loss. |
| Customer discovers they could buy GHL directly | Medium | Mitigated by the real-estate configuration, BluePrint integration and support — **not** by obscuring the engine. Canon requires transparency. |

**Strategic note:** the vendor dependency is accepted deliberately. BlankCRM exists so that proprietary engineering capital goes to BluePrint and VAULTED instead of to commodity CRM infrastructure. It is efficient capital allocation, not a moat — and should never be presented as one.

## Metrics to instrument from customer one

Onboarding hours per customer · support hours per customer per month · usage margin actually realized · attach rate to BluePrint · standalone churn vs attached churn · loaded CAC.

## Still `[A]` / `[R]`

- `[A]` labour rates, onboarding and support hour estimates — no delivery history exists.
- `[A]` the 35% attach rate.
- `[R]` markup percentage on rebilled usage — not yet decided.
- `[R]` GoHighLevel reseller/SaaS-Mode contract terms not reviewed. Vendor-dependency risk is unassessed legally.
- `[R]` Trademark availability for "BlankCRM" unverified.

## Sources

- [HighLevel Pricing](https://www.gohighlevel.com/pricing) — plan tiers, sub-account limits, SaaS Mode, rebilling
- [GoHighLevel Pricing 2026 (Apexure)](https://www.apexure.com/blog/gohighlevel-pricing) — $97 / $297 / $497 tiers
- [GoHighLevel Pricing 2026 (Automize)](https://getautomized.com/gohighlevel-pricing/) — AI Employee add-on, voice AI usage rates

Precedence: [[00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]].
