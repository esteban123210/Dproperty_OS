---
project: B_RealEstate
title: "VAULTED — Economics"
type: unit_economics
status: Funnel model v1.0 — all inputs unvalidated
owner: Esteban
last_updated: 2026-09-24
tags: [offer, vaulted, economics, unit-economics, gmv, take-rate]
---

> [!IMPORTANT] Precedence
> [[../../01_Canon/09 - Unit Economics Registry]] is the registry of record.

> [!WARNING] This is a funnel structure, not a forecast
> Every input below is `[A]`. VAULTED has **no transactions, no listings and no signed participants.** This note exists so the economics can be *reasoned about and falsified* — not so they can be quoted. Do not put these numbers in front of an investor as projections.

# VAULTED — Economics

> **Status change 2026-09-24.** This offer previously had **no economics model at all**. This note builds the funnel the canon requires.

## The binding modelling rule

> **Never estimate VAULTED revenue as "all BluePrint customers × arbitrary GMV."**

That calculation is the single most common way marketplace businesses are overstated. The required model is a funnel where **each stage has its own conversion rate and each rate can be tested independently**:

```
eligible organizations
  → activated participants        (× activation rate)
    → organizations that list      (× listing rate)
      → matches produced           (× match rate)
        → attributable completed transactions   (× close rate × attribution rate)
          → GMV                    (× average transaction value)
            → revenue              (× effective take rate)
```

Revenue is the product of **seven** uncertain factors. If each is off by half, revenue is off by ~100×. That is why this is gated.

## Input assumptions — all `[A]`

| Input | Assumption | Basis | Confidence |
|---|---:|---|---|
| Average transaction value | **$300,000** | Portfolio model | Low-medium — anchored to Dproperty deal sizes |
| Effective base take rate | **0.35%** | Portfolio model | **Low** — no legal or commercial validation |
| Activation rate (eligible → active) | ? | **none** | **No basis** |
| Listing rate (active → lists supply) | ? | **none** | **No basis** |
| Match rate | ? | **none** | **No basis** |
| Attribution survival rate | ? | **none** | **No basis — the critical one** |
| Leakage / circumvention rate | ? | **none** | **No basis** |

**Five of seven stages have no basis whatsoever.** Stating a revenue figure from this model would be fabrication.

## Take-rate mechanics

At **0.35%** effective take on a **$300,000** transaction, VAULTED earns **$1,050 per attributable completed transaction**.

| Attributable transactions/year | GMV | Revenue at 0.35% |
|---:|---:|---:|
| 10 | $3.0M | **$10,500** |
| 50 | $15.0M | **$52,500** |
| 200 | $60.0M | **$210,000** |
| 500 | $150.0M | **$525,000** |

**The scale required is the point.** VAULTED needs **hundreds of attributable completed transactions per year** to become a meaningful revenue line. For context, Dproperty's entire history is cited as ~700 operations. VAULTED is therefore not a near-term revenue story — it is a **network-effect option** whose value is in the possibility of becoming the default venue, not in the fee itself.

## Cost structure

| Cost | Type | Note |
|---|---|---|
| Product build | Fixed, large | Marketplace + access control + attribution engine |
| **Attribution and dispute handling** | **Variable, labour-heavy** | Every contested attribution is a manual investigation |
| Participant vetting / KYC | Variable per participant | Gated access implies screening obligation |
| Legal per jurisdiction | Fixed per market, **high** | Brokerage licensing, commission-sharing legality, AML |
| Network seeding | Variable | Likely below-cost or free early participation |

**No cost figure is stated because the product is unbuilt and unscoped.** `[R]`

## The variable that decides whether this business exists

**Attribution survival on off-platform closing.**

Two parties introduced on VAULTED can close the transaction entirely outside it and pay nothing. If that is easy, the take rate is unenforceable and VAULTED has no revenue model regardless of liquidity.

This is **not** primarily a product problem. It is contract, evidence and incentive design:

- What contractual obligation does a participant accept on joining?
- What evidence proves VAULTED sourced the introduction?
- What makes paying the fee *easier* than avoiding it?
- What is the enforcement path, and is it economic to use?

**Until there is a credible answer, every other VAULTED number is irrelevant.** Model leakage explicitly, and treat a high-leakage scenario as a kill case rather than a downside case.

## Why the take rate may need to be higher

0.35% on $300,000 is $1,050 — small relative to a full brokerage commission, which is deliberate: it must be low enough not to distort the deal. But it is **also low enough to be beneath the cost of enforcing it**. If dispute handling costs more than $1,050 of labour, the unit economics invert on contested deals.

**Open question:** is a higher take rate on fewer, larger, better-documented transactions a stronger model than a low rate at volume? This has not been tested.

## Sequencing — non-negotiable

**VAULTED is gated behind BluePrint stability.** No marketplace automation and no geographic scale before the 90-day gate review.

Prove in this order, and stop if one fails:

1. **Supply liquidity** — will anyone list, in one narrow niche where B_ already has relationships?
2. **Demand liquidity** — will anyone qualified engage with that supply?
3. **Attribution** — can a sourced introduction be evidenced?
4. **Leakage control** — is there a contractual and practical reason to transact on-platform?
5. **Take-rate willingness** — will a participant pay 0.35%?
6. **Legal structure** — per jurisdiction, with counsel.

## What must be built before this note is usable

1. Attribution design and the contractual participation agreement `[R]`
2. Leakage model with an explicit kill threshold `[R]`
3. Legal opinion per launch jurisdiction `[R]`
4. Narrow-niche liquidity test with real relationships `[R]`
5. Product cost estimate `[R]`
6. Dispute-handling cost per contested transaction `[R]`

## Honest investor framing

VAULTED is the **highest-upside and lowest-evidence** component of the portfolio. It is the only part that could produce network-effect economics rather than linear SaaS growth — and it is entirely unproven.

Present it as a **gated option with a defined first experiment**, never as a revenue line. Its presence in the portfolio is justified by the cold-start advantage of existing developer, broker and investor relationships. That advantage is real; the business is not yet.
