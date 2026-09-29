---
project: B_RealEstate
title: "Dproperty OS Business Plan"
type: business_plan
status: In Review
version: 0.9
owner: Esteban
last_updated: 2026-09-29
source: Realigned to 2026-07-02 decisions + Financial Model v0.5
supersedes: v0.5 (2026-07-01 ChatGPT baseline)
tags: [business-plan]
---

> [!WARNING] Historical architecture — superseded 2026-09-29
> Earlier assignments of commercial execution to BluePrint are historical only and must not guide implementation. BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions. See [[00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]].

> [!WARNING] Superseded — historical evidence only (reviewed 2026-09-23)
> The “Dproperty OS & Network” franchise-first plan. Even its name is legacy — the platform is **BluePrint**.
>
> **Current instead:** [[../../04_Business_Plan/B_RealEstate Master Business Plan 2026]]
>
> Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]. Preserved deliberately — old thinking is evidence, not guidance.

> **⚠ SUPERSEDED FOR CURRENT INVESTOR/PRODUCT WORK — 2026-09-20.**  
> This file preserves the pre-reset franchise-first model for historical/audit purposes. Do **not** use its TAM/SAM/SOM, five-year forecast, funding ask, BluePrint transaction-spine assumptions, or “physical hub as the business” framing as current.
> Current source: [[../../04_Business_Plan/B_ Business Model Reset - 2026-09-20]]

# Dproperty OS & Network — Business Plan

> **Version note (2026-07-04):** This is v0.9, realigned to the decisions from the
> 2026-07-02 pitch session and to `Dproperty_OS_Financial_Model.xlsx v0.5`. The prior
> v0.5 draft (2026-07-01) predated those decisions and used retired projections
> ($2.32M / $635k EBITDA) that appeared in no other file. All projection figures below
> are current-model outputs and are marked **[MODEL v0.5]**; unconfirmed items are
> marked **[VALIDATE]** and listed in the Validation Register (Section 19). This plan is
> not investor-final until those clear.
>
> **Pricing revision (2026-07-04b):** Franchise launch fee raised to a staged **$30k/$40k**;
> "brand/network fee" renamed **Network & Brand Fund**; **Private Collection renamed
> Dproperty Select** and moved from a 50/50 gross split to a **fixed % of sale price**
> (2.5% branded / 1.5% white-label, external-partner-broker terms — revised 2026-08-03 from 2.0%).
>
> **Commission waterfall (2026-07-05):** Local sales now modelled as 5% charged → 50/50
> external-advisor co-broke → **2.5% into the company** (35% seller / 10% director / 55%
> franchise net). Royalty (7.5%) is charged on the **2.5% into-company**, not on net.
> Model rebuilt to **v0.7**; Year 5 revenue ~$1.59M, EBITDA ~$630k.

## 1. Executive summary
Dproperty OS & Network is a proposed venture that converts Dproperty’s boutique real estate know-how into a scalable operating platform. The venture will serve three customer types: branded franchise operators, white-label boutique agencies, and developers needing professional sales infrastructure.

The central thesis is that boutique real estate players do not want to become mass-market chains, but they need institutional-grade operations: controlled documents, broker agreements, sales process, projection tools, training, dashboards, compliance, and project intelligence.

The proposed five-year target is deliberately conservative: five branded franchises, twenty white-label agencies, and fifteen developer partnerships/projects. On a collected basis **[MODEL v0.7]**, revenue reaches approximately **$1.59M** in Year 5. EBITDA is negative in Years 1–2 (build phase), turns **positive in Year 3 (~$15k, thin)**, and reaches **~$630k by Year 5**. Local franchise economics run through a commission waterfall (5% charged → 50/50 with external advisors → 2.5% into the company; royalty is charged on that 2.5%). EBITDA depends on the operating-cost plan, currently editable planning estimates in `Dproperty_OS_Financial_Model.xlsx v0.7` — see Section 19.

## 2. Company structure and ownership
The venture is sponsored by the two owners — **Luz Adriana** (Dproperty) and **Simon** (Simon’s entity) — with two operating co-founders, **Esteban** and **Miguel**.

**[VALIDATE — structure]** The 2026-07-02 session surfaced that "bringing the companies together" likely means this is a **joint venture between Dproperty and Simon’s entity**, not a simple spin-out/NewCo. The contribution and IP split between the two sponsoring entities is **undefined and blocks the structure section of the pitch (Slide 12).**

### What the venture owns
- Software platform and workflows.
- Training academy and certification logic.
- Franchise operating manuals.
- White-label product.
- Developer Sales OS.
- Projection methodology.
- Document-template automation and clause logic created for the venture.
- HQ dashboards and compliance system.

### Contributions from the existing businesses
The existing Dproperty business contributes brand credibility, current operating knowledge, market relationships, project access, and Panama Private Collection inventory. Simon’s entity contributes **[VALIDATE — contribution/IP split undefined]**. These contributions should be formalised through a clear internal/JV agreement.

### Cap table (per Decision 2026-07-02, supersedes 40/40/15/5)
| Stakeholder | Role | Ownership | Vesting |
|---|---|---:|---|
| Simon | Sponsoring owner | 35% | — |
| Luz Adriana | Sponsoring owner | 35% | — |
| Miguel | Operating co-founder — communications/creative (reports into Simon’s org) | 15% | 4 years, 1-year cliff |
| Esteban | Operating co-founder — strategy/management (reports into Luz Adriana’s org) | 15% | 4 years, 1-year cliff |

No option pool at formation. The structure intentionally pairs each sponsoring owner with an operating lead. **[VALIDATE]** Future-hire dilution mechanism is open.

### Founder compensation
- **Esteban:** EUR 4,000/mo (months 1–12), automatic step to EUR 5,500/mo at Tranche 2; 15% equity fixed.
- **Miguel:** EUR 3,000/mo **[VALIDATE — placeholder amount]**, drawn from the venture budget; 15% equity.

## 3. Problem statement

### For boutique agencies
Boutique agencies often win because they feel premium, personal, and trusted. Internally, however, many still rely on WhatsApp, Excel, email attachments, manual projections, copied contracts, and scattered project files. They need systems without losing their boutique identity.

### For franchise operators
Buying a brand is not enough. A franchisee needs a working business machine: sales process, documentation, project access, broker system, training, dashboards, and compliance. Without this, the franchisee must recreate the operating infrastructure alone.

### For developers
Developers are often strong at building projects but weaker at selling them systematically. They need trained sales teams, broker coordination, CRM discipline, pipeline visibility, follow-up automation, and investor-grade presentation tools.

## 4. Solution
Dproperty OS is a real-estate-specific operating platform that includes:
- Client, broker, developer, project, unit, and deal databases.
- Document generation for NDAs, broker agreements, client agreements, reservation summaries, and internal approvals.
- Investment projection engine.
- Franchise/white-label dashboards.
- Developer project sales dashboards.
- Training academy and certifications.
- Broker network module.
- Private Collection inventory controls.
- HQ governance and compliance monitoring.
- **GoHighLevel CRM/marketing layer (confirmed over HubSpot)** — white-label sub-accounts per franchisee, with HQ network-level data visibility. GoHighLevel is a **resold margin line**, not a pass-through cost (see Sections 5 and 12).

## 5. Product lines

### 5.1 Dproperty-branded franchise
The franchisee operates under Dproperty. They receive the brand, OS, training, standards, project access, and Private Collection participation.

Pricing:
- **Launch fee: $30,000 (founding); $40,000 after 5 successful franchises.** [VALIDATE — define "successful"]
- $1,000/month OS fee.
- **6% royalty + 1.5% Network & Brand Fund (7.5% total) on GROSS-INTO-COMPANY** — i.e. the commission remaining after the external-advisor co-broke split, collected basis.
- **Commission waterfall:** 5% charged → 50/50 with external advisors → **2.5% enters the company** (the royalty base) → of that, 35% seller, 10% sales director, 55% franchise net. Royalty is on the 2.5% into-company (not on net), so agent-comp choices don't change HQ's take. HQ nets ~$562 per $300k local unit.
- **Minimum royalty floor: $750/month [VALIDATE — placeholder amount] from month 7, creditable against percentage royalty.**
- GoHighLevel: resold as a sub-account with margin (no longer "at cost").
- **Dproperty Select payout to franchisee: 2.5% of sale price** (replaces the former 50/50 split — see §6).

**What the $30k/$40k launch fee covers:** brand-use right, franchise onboarding, Dproperty OS setup, CRM/GoHighLevel setup, pipeline configuration, operating manuals, training/academy, welcome kit, brand assets, sales & presentation templates, reporting structure, Dproperty + Dproperty Select methodology training, first 90-day plan, and HQ launch support. It signals entry into a boutique operating system, not a cheap licence.

**Benchmark basis:** Keller Williams references ~$35k initial fee, 6% royalty on GCI, ~$150k minimum cash to open [VALIDATE]; Engel & Völkers ~$35k (Americas) to €42,500 (Europe) with 3.75%–12.5% royalty. Dproperty lacks their scale but sells a complete system, so $30k founding / $40k mature is defensible.

**Collection-basis rationale:** the franchise playbook targets fast-collecting local sales. Deferred LATAM pre-construction commissions route through the HQ-controlled Dproperty Select rather than the standard royalty line, to protect franchise cash flow and HQ quality control.

### 5.2 White-label OS
Boutique agencies keep their own brand but run on Dproperty’s operating system.

Pricing:
- Starter: $10,000 setup + $1,500/month.
- Growth: $20,000 setup + $2,500/month.
- Enterprise: $50,000+ setup + $5,000+/month.
- Monthly OS fee positioned **higher than branded**, because white-label builds no Dproperty brand value.
- Plus GoHighLevel sub-account resale margin per client.
- **Dproperty Select access included**, on external-partner-broker terms (revised 2026-08-03; the earlier blanket exclusion is retired): **1.5% of sale price** (vs 2.5% for branded — see §5.4).

### 5.3 Developer Sales OS
Developers use Dproperty to train, structure, manage, and monitor project sales.

Pricing:
- Developer-team sales: 0.5% of gross sale value.
- Dproperty/network sales: 2.5%–3% of gross sale value.
- Managed Sales Desk: $3,000–$5,000/month minimum, creditable against success fees.

Per-project revenue varies widely with project size and sales mix (see the illustrative $15M example in Section 12). For **aggregate five-year projections the model uses a conservative blended assumption of ~$40k of Dproperty revenue per project [MODEL v0.5 / VALIDATE]**, not the high-end single-project illustration.

### 5.4 Strategic difference: branded vs white-label
Branded and white-label are **not the same product with a different logo**. Dproperty branded franchises carry **investment priority**: they are oriented to investors, select-project access, Dproperty Select participation, cross-border investment, high-capacity clients, and feeding the HQ opportunity funnel. White-label focuses on local boutique operation, transactional efficiency, and internal process improvement (CRM, OS, templates, reports, training), and receives Dproperty Select access on external-partner-broker terms with a lower payout than branded (1.5% vs 2.5%, revised 2026-08-03).

**Governing rule: the Dproperty brand goes where there is investment potential; the system can go anywhere.** This also guides which markets should be branded vs white-label.

## 6. Dproperty Select (formerly Private Collection)
Dproperty Select is a controlled HQ-managed portfolio of premium, investor-ready projects. It preserves Dproperty’s existing Panama business and ensures that high-end investor opportunities are handled by senior HQ managers.

**Economics (revised 2026-07-04 — replaces the 50/50 split):** HQ pays the originator a **fixed percentage of sale price**, not a share of commission:
- Branded franchise originator: **2.5% of sale price.**
- White-label partner originator: **1.5% of sale price** (external-partner-broker terms, revised 2026-08-03 from 2.0%).

**Projection assumption:** always model Dproperty Select at **5% total commission**. If HQ negotiates 6%–8% on a select project, the originator payout stays fixed and **HQ captures the upside** — so projections are never inflated by optimistic commission assumptions. At exactly 5% the branded payout equals the old 50/50 ($7,500 on a $300k unit); above 5% the fixed-percentage structure is strictly better for HQ.

Rule:
- Local franchise inventory: franchise keeps commission and pays royalty/Network & Brand Fund.
- Dproperty Select inventory: HQ retains control of developer relationships, materials, pricing, projections and negotiation; the originator earns a fixed % of sale price.

## 7. Market sizing

### TAM
The global real estate software market is estimated at USD 15.60B in 2026 and projected to reach USD 39.49B by 2033. The broader PropTech market is projected to grow from USD 44.59B in 2026 to USD 104.57B by 2034.

### SAM
The first serviceable market is boutique real estate agencies, investor-focused brokerages, and developers in Panama, Colombia, Miami/South Florida, Spain, Mexico, the Dominican Republic, and selected LatAm markets. Latin America residential real estate is estimated at USD 256.23B in 2026, reaching USD 333.37B by 2031.

### SOM
The conservative five-year obtainable market is:
- 5 branded franchises.
- 20 white-label agencies.
- 15 developer partnerships/projects.

This translates to Year 5 revenue of approximately **$1.41M [MODEL v0.5]** on a collected-GCI basis.

## 8. Competition

| Competitor type | Examples | Dproperty differentiation |
|---|---|---|
| Real estate franchises | Engel & Völkers, RE/MAX, Keller Williams | Dproperty is boutique-first and can also white-label the system. |
| CRMs/marketing platforms | GoHighLevel, Follow Up Boss, BoomTown, Propertybase | These manage leads; Dproperty OS manages real estate execution, documents, projections, governance, and developer sales. |
| Contract/document tools | DocuSign CLM, Adobe Sign, contract platforms | These automate contracts; Dproperty embeds contracts into the real estate operating method. |
| Local developer sales teams | Internal teams and project brokers | Dproperty adds process, training, broker network, dashboards, and quality control. |
| DIY systems | Excel, WhatsApp, Google Drive, SharePoint | Cheaper initially but do not scale and create operational/legal risk. |

## 9. Moat
Dproperty’s moat is the combination of:
- Boutique brand and trust.
- Existing Panama operating model.
- Private Collection inventory.
- Developer relationships.
- Broker network.
- Approved documents and templates.
- Projection methodology.
- Training academy.
- Franchise/white-label operating manuals.
- Data from real transactions.
- Cross-franchise and developer network effects.

## 10. Go-to-market strategy

### Phase 1 — Internal proof
Build and run Dproperty’s current business through the OS.

### Phase 2 — Pilot customers
Launch with:
- 2 white-label agencies.
- 1 developer project.
- 1 branded franchise candidate.

### Phase 3 — Regional expansion
Focus on Panama, Colombia, Dominican Republic, Mexico, Miami, and Spain through warm networks and developer/broker referrals. The sales playbook prioritises **fast-collecting local sales** to support the collected-GCI royalty model; deferred pre-construction inventory is routed through Private Collection.

### Phase 4 — Platform/network effects
Create inter-franchise referrals, shared developer inventory, Dproperty Select expansion, and benchmark dashboards.

## 11. Operating model and governance

### HQ roles
- Executive Sponsors: Luz Adriana (Dproperty) and Simon (Simon’s entity).
- Venture/Product & Strategy Lead: Esteban — OS, roadmap, business case, implementation, pilots.
- Communications/Creative Lead: Miguel.
- Technical Lead: builds platform and integrations.
- Legal/Compliance Lead: contracts, templates, franchise/white-label/developer agreements.
- Training/Academy Lead: operating manuals and certification.
- Customer Success Lead: onboarding, support, and adoption.
- Sales/BD Lead: recruits white-label clients, developers, and franchise prospects.

### Governance
- Board: the two sponsoring owners plus operating co-founders per agreed ownership.
- Reserved matters: budget, debt, sale of company, equity issuance, major strategic partnerships, IP licensing, and changes to founder equity.
- Monthly operating review: pipeline, product, finances, pilots, risks.
- Quarterly strategy review: market expansion, product roadmap, legal risk, unit economics.

## 12. Unit economics

| Model | Core assumption | Dproperty revenue logic | Example Dproperty revenue |
|---|---|---|---|
| Branded franchise - local sale | $300k unit, 5% = $15k → 50/50 co-broke → **$7,500 into company** | 7.5% on the $7,500 into-company (not on franchise net) | HQ $562 / unit (franchise net $4,125) |
| Dproperty Select - branded | $300k unit, model at 5% = $15k GCI | Franchisee 2.5% of sale price; HQ keeps remainder; upside >5% to HQ | HQ $7,500 / franchise $7,500 per unit |
| Dproperty Select - white-label | $300k unit, model at 5% = $15k GCI | Partner 1.5% of sale price; HQ keeps remainder | HQ $10,500 / partner $4,500 per unit |
| White-label starter | $10k setup + $1.5k/month + GHL resale margin | Platform/implementation revenue + recurring + CRM margin | ~$28k launch-year / ~$18k recurring (+ GHL margin) |
| Developer Sales OS (illustrative high case) | $15M project, 40 team sales + 10 Dproperty/network sales | 0.5% team + 2.5% network | $135k (single large project — illustrative only) |
| Developer Sales OS (model blended) | Average project across portfolio | Conservative blended | **~$40k per project [MODEL v0.5]** |

> The $135k figure is an illustrative ceiling for a large project. Aggregate projections in Section 13 use the conservative ~$40k/project blended assumption.

## 13. Five-year financial projection **[MODEL v0.7 — commission waterfall, new pricing]**

> Source: `98_Archive/Exports/Dproperty_OS_Financial_Model.xlsx v0.7` (built 2026-07-05). Revenue
> is formula-driven off the Assumptions sheet. **OPEX rows are editable planning estimates**
> (not yet owner-validated), so EBITDA below is indicative.

| Year | Branded EOY | WL EOY | Dev Projects/Yr | Revenue | OPEX | EBITDA |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 2 | 1 | $86,800 | $445,000 | ($358,200) |
| 2 | 1 | 5 | 3 | $312,056 | $510,000 | ($197,944) |
| 3 | 2 | 10 | 6 | $659,597 | $645,000 | +$14,597 |
| 4 | 3 | 15 | 10 | $1,055,852 | $805,000 | +$250,852 |
| 5 | 5 | 20 | 15 | $1,594,800 | $965,000 | +$629,800 |

**Revenue mix at Year 5:** developer ($600k), white-label recurring ($378k), Dproperty Select HQ-retained ($360k), local royalty+fund ($63k), WL setup ($60k), launch fees ($60k), OS fees ($48k), GHL margin ($26k). Note local royalty is modest by design — the waterfall means most local commission is co-broked and paid to the selling team; HQ's scalable revenue is recurring + Select + developer.

**Key model assumptions [VALIDATE]:** 50 units/franchise/yr, 70/30 local/Select mix, ramp 0.5→0.8 over Y1–Y5, ~$40k developer revenue/project, WL blended $12k setup / $1.8k month. Change any on the Assumptions sheet to re-run.

**Sensitivity — commission rate:** the 5%-vs-0.75% question only affects the local royalty line (Dproperty Select is HQ-negotiated at ≥5% by definition). At 0.75% local, the local royalty+fund line falls from ~$63k to ~$9k, so **Year 5 revenue is ~$1.54M vs $1.59M** — the venture barely moves, because **~96% of revenue is rate-independent** (subscriptions, setup fees, developer revenue, Dproperty Select, launch fees). This is the single most important robustness point in the plan.

## 14. Why EBITDA is negative in Years 1 and 2
The business requires upfront investment before sufficient recurring revenue exists. Product build, legal structuring, template creation, training academy, implementation capacity, and founder salaries happen before the customer base is mature. The collected-GCI basis also delays early royalty revenue (collection lag + franchise ramp). The model turns EBITDA-positive in Year 3 when platform revenue, developer revenue, and minimum royalty floors begin to cover the fixed operating base.

## 15. Internal venture budget
Positioned as an internal venture budget funded by the sponsoring owners, released in tranches.

- **Headline frame: $650,000 over 24 months.**
- **Actual 24-month cost base with the Miguel salary placeholder: ~$734,000 [VALIDATE].** The pitch discloses this gap and frames tranche gating as the owners’ downside cap.

| Use of funds (envelope, not strict Y1 P&L) | Budget |
|---|---:|
| Product build and development | $140,000 |
| Founder salary reserve (Esteban + Miguel) | ~$234,000 **[VALIDATE — Miguel amount]** |
| Legal/franchise/template structure | $80,000 |
| Training academy and manuals | $55,000 |
| Customer success and pilot implementation | $85,000 |
| Sales/BD/travel | $65,000 |
| Hosting/tools/admin | $60,000 |
| Contingency | $15,000 |
| **Total (indicative)** | **~$734,000** |

Tranche logic: Tranche 1 (~$350k) builds MVP, legal foundation, manuals, pitch, pilots; Tranche 2 (~$300k+) releases after MVP live, 2 white-label pilots, 1 developer pilot, franchise package ready.

## 16. Risk analysis

| Risk | Mitigation |
|---|---|
| **Commission rate conflict: 5% local GCI (franchise model) vs 0.75% deferred advisory (handoff docs)** — flagged "BLOCKS EVERYTHING" | Confirm rate with Fernando/Ernesto. Sensitivity shows survival at 0.75% (Y5 $1.19M vs $1.41M); ~76% of revenue is rate-independent. |
| Projections not yet tied to validated model assumptions | Rebuild/confirm `Dproperty_OS_Financial_Model.xlsx`; confirm 70/30 mix, 45% ramp, 2-yr lag, $40k/project, floor amount. |
| JV contribution/IP split undefined | Define Dproperty vs Simon-entity contributions before signing structure. |
| Product overbuilt before validation | Build MVP internally first, then pilots. |
| Franchisee underperformance | Only approve owner-operators who can reach 40–50 units/year within 24 months. |
| Developer projects underperform | Monthly minimums creditable against success fees. |
| White-label clients copy the system | Strong IP, data, template, and reverse-engineering protections. |
| Operational support burden grows | Build training academy, certification, and customer-success processes early; HQ support cost per franchise still unknown. |
| Dproperty Select quality dilution | HQ senior managers retain control of curated inventory. |

## 17. Exit strategy
Potential outcomes:
- Sale to a premium real estate franchise group.
- Sale to a PropTech/CRM/CLM platform.
- Sale to a developer sales platform or regional real estate network.
- Long-term cash-flow/dividend business.

## 18. Strategic conclusion
This is realistic because the target is not hypergrowth. By Year 5, the plan only assumes five branded franchises, twenty white-label agencies, and fifteen developer projects, reaching ~$1.41M revenue on a conservative collected basis (pending recalculation for the new fee structure). The business creates a scalable venture while also improving Dproperty’s current operations, protecting Dproperty Select inventory, and opening a path toward franchise expansion.

## 19. Validation Register (must clear before investor-final v1.0)
| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | Commission rate: 5% vs 0.75% | Fernando / Ernesto | Everything — projections |
| 2 | ✅ Built — `Financial_Model.xlsx v0.6` (2026-07-04). Remaining: **owner-validate the OPEX/staffing rows** | Esteban / Owners | §13 EBITDA |
| 3 | JV contribution / IP split (Dproperty vs Simon entity) | Owners | §2 structure, pitch Slide 12 |
| 4 | Miguel salary amount | Owners | §2, §15 budget |
| 5 | Model assumptions: 70/30 mix, 45% ramp, 2-yr lag, $40k/project, floor amount | Esteban | §12, §13 |
| 6 | Y3–5 staffing plan behind EBITDA range | Esteban | §13 EBITDA |
| 7 | Minimum royalty floor amount ($750/mo placeholder) | Owners | §5.1 |
| 8 | ✅ Done — recalculated in model v0.6 with $30k/$40k fee + Select fixed payout | Esteban | §13 |
| 9 | Definition of "5 successful franchises" (fee step trigger) | Owners | §5.1 |
| 10 | Does the franchisee pay royalty on Dproperty Select earnings? (default: no) | Owners | §6, §12 |
| 11 | Confirm Keller Williams benchmark figures (~$35k fee, $150k cash, 6%) | Esteban | §5.1 |

## 20. Ecosystem Vision (Phase 2) — added 2026-07-14

This plan describes **Phase 1: the franchise system**. This session established that Phase 1 is the engine for a larger **Phase 2: a physical real estate ecosystem/hub** — "the soul of 19M, the model of Station F, for real estate."

**What Phase 2 is:** a curated hub + digital network where the entire real estate value chain gathers under one roof — emerging architects, interior designers, investment analysts, PropTech founders, developers, boutique agencies, the Dproperty franchise network, and investors. Activities: desks/studios, hackathons, training/certification, networking, showcases, and live deal origination.

**Why franchising first:** we cannot build the hub without (a) proof the model works and (b) capital that isn't ours to burn. Franchising delivers both. Capital-recycling loop: franchise fees + royalties + Select commissions → HQ EBITDA (Year 3+) → seeds hub + talent programs + equity fund → network deepens → franchises become more valuable → more franchises.

**Phase 2 revenue lines (to be modelled before any external raise):** space/membership rental, events, matchmaking fees, equity stakes in hub-born ventures, franchise pull-through, and proprietary data.

**Phased build:** (1) Franchise system Yr 0–5 → (2) Digital community Yr 2–5 → (3) First physical hub Yr 5–8 (city/capex TBD; franchise EBITDA + external capital partner) → (4) Network of hubs Yr 8–15.

**Companion decks:** [[../../05_Pitch_and_Investor/Pitch Deck Outline]] (Deck 1 — franchise, investable now) opens and closes on this vision; [[../Superseded Pitch/Ecosystem Deck Outline]] (Deck 2 — full ecosystem, north-star / future raise). **Deck 2 is not raise-ready until a Phase-2 P&L, hub capex, and location are defined** (see new Validation items below).

**Validation Register additions:**
| # | Item | Owner | Blocks |
|---|---|---|---|
| 12 | Phase-2 (ecosystem/hub) P&L model | Esteban | Deck 2 external use |
| 13 | First hub city, capex, lease-vs-own decision | Owners | Phase 3 go/no-go |
| 14 | Equity-fund structure for hub-born ventures | Owners / Legal | Phase 2 economics |
| 15 | Minimum franchise EBITDA threshold to green-light Phase 3 | Owners | Sequencing |

## References
- **Real estate software market:** Coherent Market Insights estimates the global real estate software market at USD 15.60B in 2026, reaching USD 39.49B by 2033 at 14.2% CAGR. Source: https://www.coherentmarketinsights.com/industry-reports/real-estate-software-market
- **PropTech market:** Fortune Business Insights projects the global PropTech market to grow from USD 44.59B in 2026 to USD 104.57B by 2034 at 11.20% CAGR. Source: https://www.fortunebusinessinsights.com/proptech-market-108634
- **Latin America residential real estate:** Mordor Intelligence estimates Latin America residential real estate at USD 256.23B in 2026, reaching USD 333.37B by 2031. Source: https://www.mordorintelligence.com/industry-reports/residential-real-estate-market-in-latin-america
- **Panama commission benchmark:** Panama real estate sources commonly cite 5% as the standard sales commission; some rural or complex properties can be higher. Source: https://www.panama-real-estate.com/article/selling-your-property-in-panama/
- **Panama commission benchmark 2:** Panama Casa Realty cites 5% of gross selling price as a standard commission and up to 10% in countryside cases. Source: https://www.panamacasarealty.com/en/article/selling-your-property-in-panama
- **GoHighLevel pricing:** GoHighLevel's Pro/SaaS Mode plan is listed at USD 497/month before usage-based costs. Source: https://www.gohighlevel.com/pricing
- **Engel & Völkers franchise benchmark:** Engel & Völkers Germany lists an initial franchise fee of EUR 42,500, average total investment of EUR 250k-400k, and 12.5% royalty on net commission income. Source: https://www.engelvoelkers.com/de/en/resources/your-ideal-franchisor-in-the-real-estate-sector
- **Engel & Völkers US benchmark:** Franchise Direct lists Engel & Völkers ongoing royalties at 6% of annual gross revenues up to USD 1M, with minimum annual royalty language. Source: https://www.franchisedirect.com/realestatefranchises/engel-volkers-franchise-05558/ufoc/
- **Keller Williams benchmark [VALIDATE]:** Referenced initial investment ~USD 183k–337k, ~USD 150k minimum cash to open a Market Center, ~USD 35k initial franchise fee, 6% royalty on gross commission income. Figures to be confirmed against the current KW FDD before pitch use.
- **Follow Up Boss pricing:** Follow Up Boss real estate CRM pricing starts at USD 69/user/month. Source: https://www.followupboss.com/pricing
- **BoomTown pricing benchmark:** Software Advice lists BoomTown starting at USD 1,000/month in its comparison dataset. Source: https://www.softwareadvice.com/crm/boomtown-profile/vs/follow-up-boss/
