---
project: B_RealEstate
title: "Phased Rollout - Product & GTM - Revised"
type: product_roadmap
status: "v2.0 - Active"
version: 2.0
owner: Esteban
last_updated: 2026-09-29
tags: [roadmap, product, gtm, phases]
---

> [!WARNING] Superseded — historical evidence only (reviewed 2026-09-23)
> Pre-reset phased rollout.
>
> **Current instead:** [[../01_Canon/10 - Roadmap and Governance]]
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]. Preserved deliberately — old thinking is evidence, not guidance.

# Phased Rollout — Product & Go-to-Market — Revised v2.0

## Guiding Philosophy

**Ship the smallest defensible product that moves the north-star metrics.**

Don't build a "complete" platform. Build a ladder.

---

## Phase 1: Foundation (Months 1–3)

### Goal

Prove the model works with real customers.

### Product Scope

**BluePrint MVP (v0.1 "Foundation")**
- Transaction intake form
- Document generation (NDA, buyer agreement templates)
- Commission calculator
- Task management (basic)
- Reporting dashboard (deal status, team performance, monthly closing)
- Copilot: retrieves from playbooks, helps with templates (read-only)

**NOT included:**
- Signature/e-signing
- Full compliance gates
- Advanced Copilot
- Integrations beyond webhooks

**Why this scope:**
- Gets to "run a transaction better" in 4–6 weeks.
- Agencies can use it alongside existing CRM.
- Foundation for everything after.

**VAULTED MVP (v0.1 "Early Access")**
- Simple listing site (10–15 pilot properties)
- Broker directory (Dproperty + 2–3 pilot franchisees)
- Basic matching (geography + price range)
- Deal flow (listing → interested broker → negotiate)

**NOT included:**
- Automated pricing algorithms
- AI matching
- Complex privacy controls
- Payment processing

**Why this scope:**
- Prove "does inventory move?"
- Build network habits early (brokers return to list/view).

### Go-to-Market

**Who to target:**
- Dproperty (internal prove-out; must work here first)
- 2 white-label pilot agencies (warm intros, low friction)
- 1 developer pilot project (test supply-side)

**Messaging:**
"BluePrint helps boutique agencies understand financial health, verify CRM data and improve processes. Trial terms require commercial approval."

**Incentive:**
- Free tier (1 user, 2 active transactions)
- Pilot customers get 50% off paid tier for 6 months

### Team

- 1 product + strategy (Esteban)
- 2 engineers (contractors, MVP-focused)
- 1 customer success (shared with sales)

### Success Criteria (Gate to Phase 2)

- ✅ Dproperty Panama using BluePrint daily (no workarounds)
- ✅ 2+ pilot agencies signed and using BluePrint for verified management reporting on 10+ CRM transactions/month combined
- ✅ 1 developer using for project sales (20+ transactions)
- ✅ $30k–50k revenue (pilots + early adoption)
- ✅ NPS > 50 from pilot customers
- ✅ Zero data/security incidents
- ✅ Product team is shipping small features weekly (not blocked)

---

## Phase 2: Adoption (Months 4–9)

### Goal

Acquire 200+ BluePrint organizations. Prove adoption curve and CAC payback.

### Product Scope

**BluePrint Release 1 ("Back Office Brain")**
- All Phase 1 features, plus:
- Advanced commission modeling (splits, overrides, reconciliation)
- Compliance checklist (deal status gates)
- Team performance reporting (agent KPIs, conversion rates)
- Glitch reporting (service recovery)
- Registry management (contracts, licenses, renewals)
- Copilot expansion (can draft from templates, explain processes)

**NOT included:**
- Signature workflows (document gen only)
- Full transaction history tracking
- Integrations beyond REST API

**VAULTED Release 1 ("Active Marketplace")**
- 50–100 listings (Dproperty Select + developer projects)
- Broker network (all BluePrint customers auto-added, opt-out)
- Deal activity tracking (who viewed, who negotiated)
- Basic matching (geography, price, type)
- Performance reporting (listing velocity, broker interest)

**NOT included:**
- Advanced pricing algorithms
- International broking
- Automated co-broker rules

### Go-to-Market

**Channels:**
- Direct: Warm referrals from pilot customers (viral loop starts)
- Events: Real estate conferences (2–3 per quarter, regional)
- Content: Blog posts on "how boutique agencies run better" (SEO target)
- Partnerships: Developer networks, local broker associations

**Pricing (Launch):**
- BluePrint Solo: $99/month (3 users, 5 deals)
- BluePrint Growth: $399/month (10 users, 25 deals)
- BluePrint Pro: $999/month (unlimited users, 100+ deals)
- VAULTED: Free to join, 0.75% on transactions

**Target customer profile:**
- Regional agency (10–30 units/year)
- Owner-operator with pain (manual processes)
- Willing to try new tech ($99 is low friction)

### Marketing Narrative

"The infrastructure that luxury real-estate agencies use. Now available to independent brokers."

(Positioning emphasizes "professional grade + boutique" not "mass market.")

### Team

- 1 product (Esteban)
- 2 engineers (contractors or hire 1 full-time)
- 1 customer success
- 1 sales/BD (part-time, warm leads)

### Success Criteria (Gate to Phase 3)

- ✅ 200+ BluePrint organizations (active = 1+ reviewed management reconciliation/month)
- ✅ $300k+ MRR from BluePrint
- ✅ 50+ active VAULTED listings
- ✅ 20+ VAULTED deals closed (proof of network)
- ✅ Customer churn < 5%/month
- ✅ NPS > 60 across all tiers
- ✅ CAC < $500 (mostly warm referrals, events)
- ✅ LTV > $3,000 (minimum payback in 6 months)
- ✅ Product roadmap aligned with next phase (no major pivots needed)

---

## Phase 3: Network Effects (Months 10–18)

### Goal

Accelerate BluePrint adoption to 600+ organizations. Launch Tier 3 (Network membership) and Tier 4 (Franchising).

### Product Scope

**BluePrint Release 2 — deeper management intelligence [T]**
- Read-only connectors across the full commercial lifecycle and additional CRMs.
- Expected vs actual cash, expenses, budgets, variance and liability reconciliation.
- CRM-usage audits, process/Glitch diagnosis and management KPI reporting.
- Evidence-grounded CEO/CFO/COO/CMO recommendations with human management review.
- Policies, management audit and period close.

**Execution boundary:** legal workflow, commercial approvals, contracts, payment milestones, closing, commission calculations/approvals and post-sale remain in BlankCRM/chosen CRM in every release. BluePrint observes, verifies, governs and recommends; no sales-execution writeback.

**VAULTED Release 2 ("Distribution Network")**
- 200+ active listings (50+ developers)
- Broker network with roles (premium, standard, emerging)
- Deal matching algorithm (Copilot-powered, recommends properties)
- International co-broking (can refer to other markets)
- Market analytics (by geography, property type)
- Performance benchmarking (your deals vs. network average)

**NOT included:**
- AI-driven pricing (future phase)
- Automated commission distribution (commercial workflow in BlankCRM/chosen CRM; settlement by payment provider)

**B_ Network Member Platform**
- Member dashboard (deals, referrals, performance)
- Select inventory access (Dproperty curated deals)
- Benchmarking reports (compare to peer agencies)
- Network events / training
- Copilot with network data (asks VAULTED for comps)

**NOT included:**
- Full CRM for network members (still BluePrint-based)
- Payroll/accounting integrations

### Go-to-Market

**Channels:**
- Product-led (agencies discover network value organically from using BluePrint + VAULTED)
- Direct: Sales for Tier 3 (Network membership) to high-performing agencies
- Direct: Sales for Tier 4 (Franchising) to proven owner-operators
- Content: Network member success stories, benchmarking reports

**Pricing Updates:**
- BluePrint tiers unchanged
- VAULTED: Free (same as Phase 2)
- B_ Network Member: $500–2,000/month (tier-dependent)
- B_ Franchise: $45k launch + $2,500/month + 7.5% royalty (unchanged)

**Target for Franchise:**
- Agencies doing 30–50 units/year
- Proven operator, strong culture
- Interest in growth + brand

### Expansion Narrative

"The network is where independent agencies become more powerful than large ones."

(Emphasizes leverage + community, not just technology.)

### Team

- 1 product/strategy (Esteban)
- 3 engineers (1–2 full-time, 1 contractor)
- 1 customer success manager
- 1 sales/BD (dedicated to Network + Franchise)
- 1 academy/training coordinator

### Success Criteria (Gate to Phase 4)

- ✅ 600+ BluePrint organizations (50% retention from Phase 2)
- ✅ $1M+ MRR from BluePrint
- ✅ $400k+ MRR from VAULTED/transactions
- ✅ 200+ VAULTED listings (multi-market)
- ✅ 150+ VAULTED deals closed/quarter
- ✅ 50+ Network members (Tier 3)
- ✅ 2–3 franchises operational and profitable
- ✅ Copilot provides meaningful value (measurable time savings)
- ✅ Churn flat or declining (< 5%/month)
- ✅ NPS > 65 (strong recommendation signal)
- ✅ Expansion revenue 30%+ of new revenue (customers climbing ladder)

---

## Phase 4: Scale (Months 19–36)

### Goal

Reach $5M ARR. Prove 1,000+ organization market is real. Build enterprise moat (data + network + Copilot).

### Product Scope

**BluePrint Release 3 ("Intelligence Layer")**
- All Release 2, plus:
- Predictive analytics (forecasts deal close date, commission)
- Market intelligence (real-time comps, trends by geography)
- Copilot autonomy expansion (can auto-draft reports, flag compliance risks)
- White-label options (agencies can rebrand components)
- Advanced integrations (Zapier, custom APIs)

**NOT included:**
- Mortgage broker integration (3rd party)
- Complex settlement accounting (3rd party)

**VAULTED Release 3 ("Global Distribution")**
- 500+ active listings (100+ developers)
- Market in 10+ countries (LATAM, Spain, US, some Europe)
- Automated pricing recommendations (via Copilot)
- International investor access (qualified investors can browse)
- Co-brokering automation (system routes deals, brokers agree terms)
- Revenue (now at 0.75% transaction fee, sustainable)

**B_ Academy Expansion**
- BluePrint Certification (3-part program, $500/per agent)
- VAULTED Certification (marketplace best practices)
- B_ Investment Advisor cert (for advisors specializing in properties)
- Franchise operations bootcamp

### Go-to-Market

**Channels:**
- Product momentum (1,000+ orgs → viral loop accelerates)
- Direct sales (dedicated team for Franchise, Enterprise tier)
- Partnerships (co-market with developer platforms, investor networks)
- Geographic expansion (hire regional reps for LATAM, Spain)

**International Expansion:**
- Year 1: Colombia, Mexico, Spain, Dominican Republic (warm networks)
- Year 2: Broader LATAM, Central America
- Year 3: Selective US, Europe

**Pricing:**
- BluePrint Enterprise: $2,000–5,000/month (custom by organization)
- VAULTED: 0.75% (unchanged)
- Academy certifications: $500–2,000 per certification
- B_ Network: $1,000–3,000/month (tier dependent)
- B_ Franchise: $45k launch + $2,500/month + 7.5% (unchanged)

### Narrative Shift

"B_ is the infrastructure layer for independent real estate. Use it. Join the network. Build your brand on it."

(Positioning shifts from "product" to "platform" to "ecosystem.")

### Team

- 1 VP Product/Strategy (Esteban likely)
- 4–5 engineers (mix of full-time + contractors)
- 2 customer success managers
- 2 sales/BD (one for SMB direct, one for Enterprise + Franchise)
- 1 academy manager
- 1 community manager (network engagement)
- Supporting: finance, HR, legal, operations

### Success Criteria (Gate to Phase 5)

- ✅ 1,200+ BluePrint organizations globally
- ✅ $5M+ ARR (BluePrint + VAULTED + franchises + services)
- ✅ $1B+ VAULTED GMV (proof of network)
- ✅ 10+ franchises operational, profitable, and referring business
- ✅ Copilot is measurably accelerating time-to-close (trackable metric)
- ✅ Expansion revenue 50%+ of new revenue (customers climbing ladder)
- ✅ International: 3+ countries with 100+ organizations each
- ✅ EBITDA: 50%+ margin (high-margin business confirmed)

---

## Phase 5: Enterprise (Years 4–5)

### Goal

Reach $30M+ ARR. Own the operating infrastructure layer for independent real estate globally. Build defensibility moat.

### Product Scope

**BluePrint Release 4 ("Full Stack Operating System")**
- All Release 3, plus:
- Payroll evidence integration (payroll remains in the payroll provider)
- Accounting integration (automated P&L reporting)
- Management evidence portal; buyer/seller commercial portals belong to BlankCRM/chosen CRM
- Management compliance-policy oversight (commercial reviews remain in CRM)
- Full API and white-label SDK (agencies can build on top)

**VAULTED Release 4 ("Global Marketplace + Intelligence")**
- 1,000+ listings (300+ developers, 1,500+ agencies supplying)
- AI-driven matching (Copilot recommends properties to brokers)
- Lender partnerships (can show financing options)
- Institutional investor access (funds can browse off-market deals)
- Revenue-share model (VAULTED takes 0.5% from developers, 0.25% from agencies in some deals to incentivize)

**B_ Academy:** Become thought leader in real-estate operations and investment. Universities/licensing boards recognize B_ certifications.

### Network Moat

At scale, B_ becomes defensible because:

1. **Network effects are strong.** 1,500+ agencies + 300+ developers + 1,000+ listings = hard to replicate.

2. **Data is proprietary.** Thousands of transactions → market intelligence competitors can't access.

3. **Switching costs are high.** Agencies have 2+ years of data, integrations, processes built on B_.

4. **Copilot improves faster.** More transactions → smarter AI → better for all participants.

5. **Brand becomes valuable.** "Powered by B_" becomes a signal of quality and transparency.

### Revenue

- BluePrint: $10–15M (1,500–2,000 organizations)
- VAULTED: $10–15M (1,500 agencies + 300 developers + $1.5–2B GMV)
- Franchises: $1–2M (20–30 franchises)
- Developer Programs: $3–5M (20–30 active projects)
- Academy/Services: $1–2M
- Copilot/Data APIs: $2–3M

**Total: $27–42M, depending on execution.**

**EBITDA: 60%+ (highly profitable business).**

### Strategic Question

At this point, what's the right path?

**Option A: Acquisition**
- Sell to RE/MAX, Engel & Völkers, Century 21 (franchise consolidators)
- Valuation: $100–300M (based on $10–30M EBITDA × 10–30x multiple)

**Option B: Strategic Partnership**
- Partner with CRM giant (Salesforce, HubSpot) who wants to own back-office
- Valuation: partnership economics, possibly acquisition after 2–3 years

**Option C: Standalone Dividend Business**
- Keep operating independently, pay dividends from $5–10M annual EBITDA
- Founder controls business, lifestyle business but highly profitable

**Option D: Pursue Higher Scale**
- Continue growing to $50M+ revenue, prepare for IPO or mega-acquisition
- Requires significant capital raise (Series C/D) and professional management

---

## Key Decisions During Rollout

### Decision Points (Phase by Phase)

**Phase 1–2 Gate:**
- Do pilot customers actually find value? (Non-negotiable; if not, pivot product, not market)
- Is there demand for VAULTED? (If no developer interest, pause and focus on agency)
- Is churn acceptable? (If > 10%/month, product-market fit issue)

**Phase 2–3 Gate:**
- Is the customer ladder real? (Are agencies naturally upgrading from Solo → Growth → VAULTED?)
- Can we build and support 600+ organizations? (Operations capacity)
- Is franchising premature? (Only if we have 5+ agencies actively requesting it)

**Phase 3–4 Gate:**
- Is Copilot valuable enough to drive expansion revenue? (If not, pivot to different expansion)
- Is international viable? (Geography selection based on team + network)
- Can we hit $5M without raising Series A again? (If no, pricing needs adjustment)

**Phase 4–5 Gate:**
- Can we defend against large competitor entry? (If yes → consolidate. If no → accelerate to acquisition)
- Is standalone trajectory clear? (If yes → stay independent. If no → sell)

### Contingencies

**If BluePrint adoption stalls:**
- Double down on vertical (e.g., developer-focused first, then agents)
- OR lower pricing (more aggressive land grab)
- OR add missing feature (ask customers)

**If VAULTED network isn't building:**
- Start by curating all supply ourselves (Dproperty Select becomes primary)
- OR focus on single developer/asset class first (build density)
- OR pay brokers to list (subsidize liquidity)

**If Franchising is slow:**
- Stop pushing it (don't force partnerships)
- Focus on organic adoption (only best-fit agencies)
- Use as premium tier for proven customers

**If expansion revenue is low:**
- Product isn't climbing ladder naturally; find the friction
- May need to bundle services, not just charge à la carte
- OR may need to create clearer upgrade path

---

## Metrics to Track at Each Phase

### Phase 1
- WAU (weekly active users)
- Transaction throughput (deals/week)
- Time-to-close (vs. baseline)
- NPS
- Churn (monthly)

### Phase 2
- MAU (monthly active organizations)
- BluePrint ARR
- VAULTED GMV (quarterly)
- Customer acquisition cost (CAC)
- Churn cohort (by month of acquisition)

### Phase 3
- Organizations by tier (Solo/Growth/Pro)
- Expansion revenue (new vs. existing)
- Network members
- Franchises operational
- Copilot usage rate

### Phase 4
- Organizations by geography
- VAULTED penetration (% using)
- GMV by source (developer vs. agency)
- Franchise same-store sales (GCI/franchisee)
- Copilot efficiency gain (time saved, quantified)

### Phase 5
- Developer ecosystem health (# projects, GMV supply)
- Network effect metrics (referrals between agencies)
- International penetration
- EBITDA margin
- Retention (1-year, 3-year, 5-year cohort)

---

## What Success Looks Like

**Phase 1 (Months 1–3):**
Dproperty runs on BluePrint. 2–3 pilot agencies are happy. VAULTED has initial inventory.

**Phase 2 (Months 4–9):**
200 organizations use BluePrint. 20+ deals close through VAULTED. Referral loop starts (customers tell friends).

**Phase 3 (Months 10–18):**
600 organizations. 50 network members. 2–3 franchises operating. Copilot is noticeably useful. Expansion revenue climbing.

**Phase 4 (Months 19–36):**
1,200 organizations. $5M ARR. Copilot is doing sophisticated work. International presence. EBITDA positive and strong.

**Phase 5 (Years 4–5):**
$30M+ ARR. Multi-billion-dollar network. Defensible moat. Ready to scale globally or exit.

