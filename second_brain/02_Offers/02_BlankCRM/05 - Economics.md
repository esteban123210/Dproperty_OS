---
project: B_RealEstate
title: "BlankCRM — Economics"
type: unit_economics
status: Modelled v1.0 — vendor rates sourced 2026-09-24
owner: Esteban
last_updated: 2026-09-24
tags: [offer, blankcrm, economics, unit-economics, cogs]
---

> [!IMPORTANT] Precedence
> [[../../01_Canon/09 - Unit Economics Registry]] is the registry of record · [[../../06_Finance/Pricing Unit Economics and Revenue Policy]] holds the portfolio policy.

# BlankCRM — Economics

> **Status change 2026-09-24.** This offer previously had *no* cost model and its price was recorded as "open." The GoHighLevel cost base is now sourced from published vendor pricing, so a defensible price and margin can be stated. Remaining `[A]` items are labelled.

## The structural finding

**GoHighLevel's reseller model gives BlankCRM near-zero marginal platform cost.**

| Vendor fact | Source | Consequence for BlankCRM |
|---|---|---|
| Agency Pro **$497/month** | `[F]` published | One fixed platform cost for the whole book of business |
| **Unlimited sub-accounts** on Unlimited and Agency Pro | `[F]` published | Each additional customer costs **$0** in platform fees |
| **SaaS Mode requires Agency Pro** | `[F]` published | $497 is mandatory, not optional, to sell BlankCRM as a product |
| **Rebill phone/email/AI usage with markup** (Pro only) | `[F]` published | Messaging and AI are **pass-through at a margin**, not a cost centre |
| AI Employee add-on $97/month per sub-account | `[F]` published | Optional, rebillable to the customer |

This means BlankCRM's gross margin is **not** constrained by vendor cost. It is constrained by **support and onboarding labour**. That is the number to manage.

## Cost structure

| Cost | Type | Amount | Label |
|---|---|---|---|
| GHL Agency Pro platform | **Fixed** (whole business) | $497/month | `[F]` |
| Marginal platform cost per customer | Variable | **$0** | `[F]` |
| SMS / email / voice / AI usage | Variable | Rebilled with markup | `[F]` capability; `[A]` markup rate |
| Onboarding labour | One-off per customer | 8–12 hrs `[A]` | `[A]` |
| Ongoing support labour | Variable per customer | 0.5–1.5 hrs/month `[A]` | `[A]` |
| Loaded labour rate | — | $25–40/hr `[A]` | `[A]` |

## Gross margin at $249/month list

Platform cost is fixed, so margin **improves with customer count** — the opposite of a per-seat resale model.

| Customers | Platform cost allocated | Support labour `[A]` | Gross margin | GM % |
|---:|---:|---:|---:|---:|
| 5 | $99.40 | $12.50–$37.50 | $112–$137 | **45–55%** |
| 10 | $49.70 | $12.50–$37.50 | $162–$187 | **65–75%** |
| 25 | $19.88 | $12.50–$37.50 | $192–$217 | **77–87%** |
| 50 | $9.94 | $12.50–$37.50 | $202–$227 | **81–91%** |

**Breakeven on the platform: 2–3 customers at $249/month.** That is an unusually low bar and is the strongest argument for keeping BlankCRM in the portfolio.

## Onboarding economics at $750 setup

| Item | Amount |
|---|---:|
| Setup fee | $750 |
| Onboarding labour at 8–12 hrs × $25–40/hr | $200–$480 `[A]` |
| **Contribution** | **$270–$550** |

The setup fee covers onboarding with margin **provided onboarding stays under ~15 hours**. Above that it becomes a loss leader — this is the single metric to instrument first.

## What this means commercially

1. **The price is defensible.** $750 + $249/month sits well above cost at any realistic scale.
2. **Margin is a support-discipline problem, not a pricing problem.** Every hour of unplanned support costs ~$25–40 against a $249 monthly ticket.
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
