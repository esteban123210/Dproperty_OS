---
project: B_RealEstate
title: "BlankCRM — Offer and Pricing"
type: pricing
status: Resolved v1.0 — cost-backed, validate willingness to pay
owner: Esteban
last_updated: 2026-09-29
tags: [offer, blankcrm, pricing]
---

> [!IMPORTANT] Precedence
> [[../../01_Canon/04 - Offer Portfolio Map]] · [[../../01_Canon/09 - Unit Economics Registry]] · cost model: [[05 - Economics]]

# BlankCRM — Offer and Pricing

> **Resolved 2026-09-24.** This offer previously carried a contradiction: the offer folder said *"price open, blocked on GHL COGS"* while the finance policy listed $750 + $249/month. The COGS model is now built from published vendor rates, so **$750 + $249/month is confirmed as the canonical list price** — no longer "open."

## Canonical price

| Line | Price | Status |
|---|---:|---|
| **Setup / configuration** | **$750** one-off | `[A]` cost-backed, validate |
| **Subscription** | **$249/month per office** | `[A]` cost-backed, validate |
| **Messaging / voice / AI usage** | **Rebilled at markup** | `[F]` capability; `[R]` markup % undecided |
| AI Employee (optional) | $97/month per sub-account, rebilled | `[F]` vendor rate |
| Complex migration, extra offices, integrations | Quoted separately | — |

**Pricing unit: per office (sub-account), not per agent seat.** Consistent with BluePrint's org-level shape.

## Why this price is defensible

Platform cost is **fixed at $497/month** for the entire book of business, and GoHighLevel sub-accounts are **unlimited**. Marginal platform cost per customer is **$0**.

- **Breakeven: 2–3 customers.**
- Gross margin **65–75% at 10 customers**, rising to **81–91% at 50** `[A]` (support labour assumptions).
- The $750 setup covers 8–12 hours of onboarding with $270–$550 contribution.

Full workings: [[05 - Economics]].

## The three ways it sells

1. **Standalone** — to an agency that needs a CRM and is not ready for BluePrint. This is the **gateway/acquisition** motion: it lands the relationship cheaply, and BluePrint is the expansion.
2. **Attached** to BluePrint — 35% attach assumption `[A]`. Shared platform cost does not eliminate onboarding, support, integration or usage costs; contribution must be measured for the full lifecycle.
3. **Included** in Dproperty Franchise and B_ Partner packages — allocated at **standalone list price** per the binding allocation rule in [[../../01_Canon/19 - Portfolio Composition Principle]]. Never recorded at $0.

## Value logic

The customer is not buying CRM technology — they can buy GoHighLevel themselves. They are buying:

- a **real-estate-configured** front office (pipelines, stages, forms, follow-up sequences that match how property actually transacts);
- **BluePrint integration** — the qualified-opportunity handoff, which no generic GHL setup provides;
- **setup done for them**, in days rather than weeks of self-configuration;
- **one support relationship** across CRM and back office.

If a prospect concludes they could replicate this themselves with a GHL subscription, the honest answer is *yes, with effort* — and the offer must compete on configuration, integration and support. **Never by obscuring the engine.** Canon requires stating that BlankCRM is powered by GoHighLevel.

## Positioning guardrail

BlankCRM is **not the moat** and must never be pitched as proprietary CRM technology. It is efficient capital allocation: it buys distribution and front-office capability without spending proprietary engineering budget on commodity infrastructure. Proprietary value concentrates in BluePrint and VAULTED.

## Metrics to validate

Willingness to pay at $249 · standalone conversion vs attach conversion · onboarding hours (must stay under 15) · support hours per customer per month (must stay under 1.5) · realized usage markup · standalone vs attached churn · whether standalone BlankCRM customers ever upgrade to BluePrint.

## Open items

- `[R]` **Markup percentage on rebilled usage** — must be set before first invoice.
- `[R]` **GoHighLevel reseller / SaaS-Mode contract terms** not legally reviewed. Single-vendor dependency is the largest risk in this offer.
- `[R]` **Trademark availability for "BlankCRM"** unverified.
- `[A]` Labour rates and support-load assumptions carry no delivery history.

## Sources

- [HighLevel Pricing](https://www.gohighlevel.com/pricing)
- [GoHighLevel Pricing 2026 (Apexure)](https://www.apexure.com/blog/gohighlevel-pricing)

Precedence: [[00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]].
