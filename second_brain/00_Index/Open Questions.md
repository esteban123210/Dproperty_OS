---
project: Dproperty OS
title: "Open Questions"
type: open_questions
status: Baseline Created
owner: Esteban
last_updated: 2026-07-21
source: Merged canonical (00_Index + AI Handoff Pack synced 2026-07-14)
tags: [questions, strategy, legal, finance]
---

# Open Questions

This file tracks unresolved issues.

> **Sync note (2026-07-14):** Merged canonical. `00_Index/Open Questions.md` and `00_Index/AI Handoff Pack/03_Open Questions.md` are now identical.

## Ownership / Governance

- Should Dproperty OS be a separate NewCo or an internal Dproperty division first?
- **RESOLVED (2026-07-14):** Esteban equity = 15% vesting (not the 10%+5% option). Cap table 35/35/15/15.
- **KEY OPEN (2026-07-14): How do operators (Esteban + Miguel) grow their equity as the company grows, while protecting the investors' capital first?** Recommended direction (needs owner + lawyer sign-off):
  - Protect investors: put the $650k in as a **convertible shareholder instrument / loan with a 1x liquidation preference** (capital returned before equity splits on a sale) — cleaner than issuing them more equity.
  - Grow operators: a **milestone-based earn-in / performance ratchet** — Esteban & Miguel earn additional equity (from a reserved pool or founder warrants) when defined milestones hit (MVP live + first franchise; cumulative EBITDA thresholds; Year-5 targets).
  - Governance: reserved matters + board control to investors during Phase 1; good-leaver/bad-leaver buyback on unvested equity.
  - **→ Full proposal drafted: [[Ownership & Investor Protection One-Pager]] (v0.1). Needs owner discussion + lawyer papering.**
- What happens to Esteban's vested equity if he leaves, is terminated, or the project is sold?
- Should there be a formal option pool from day one (vs. a milestone earn-in pool)?

## Funding

- Will the owners approve a 24-month internal venture budget?
- Should the $650k budget be fixed or milestone-based? (Current plan: tranche-gated.)
- What is the minimum viable first-year budget if they want to start leaner?
- Which expenses are paid by existing Dproperty/TheVelopers versus the NewCo?

## Legal

- Which jurisdiction should govern the franchise agreements?
- Which jurisdictions require franchise disclosure documents?
- What franchise/legal advice is needed before selling the first franchise?
- How should data privacy be handled across Panama, Colombia, Europe, and potential other markets?
- Who owns the templates, manuals, brand assets, and software IP?
- What terms prevent franchisees or white-label clients from copying the system?

## Franchise Package

- What is the minimum legally safe franchise package before selling the first franchise?
- Should the onboarding package be English first, Spanish first, or bilingual?
- How much of Dproperty's existing internal process can be shared with franchisees?
- What support level is included versus paid extra?

## Dproperty Select (formerly Private Collection)

- Which existing projects qualify for Dproperty Select? (Candidates from Simon: Dovle Selva, Dovle Cincuentenario, potentially Nayamara, Cavarrosa, the Victory's — confirm which are committed.)
- Who approves client registration?
- What exact steps trigger the fixed-% payout (2.5% branded / 2.0% white-label of sale price)?
- **Does the franchisee pay any royalty/Network fee on Dproperty Select earnings? (Default assumption: no.)**
- What happens if a franchisee introduces a client and HQ closes months later?
- How are disputes over client ownership handled?

## Pricing & Naming

- **RESOLVED (2026-07-14): Currency = USD** everywhere. Launch fee $30k/$40k.
- **RESOLVED (2026-07-14): Minimum royalty floor = $500/month**, creditable, from month 7 (proposed — confirm with owners).
- **RESOLVED (2026-07-18): Naming convention** — keep **"Private Collection"** internally (vault, folder, file names, for link stability); use **"Dproperty Select"** on all handouts / external / client-facing materials. Same program, two names by context.
- How is "5 successful franchises" defined for the $30k → $40k launch-fee step?
- Validate the financial model (v0.7) OPEX/staffing rows — currently planning estimates; Year 3 breakeven is thin (~$15k).
- Confirm Keller Williams benchmark figures used in the pricing rationale (~$35k fee, $150k cash, 6% royalty).

## Pitch Deck Flags (2026-07-14)

- **RESOLVED:** currency (USD), equity (35/35/15/15 for now), Simón contribution (investor: capital + TheVelopers brand + developer insight + network + projects), Miguel salary ($0 for now), royalty floor ($500).
- **STILL OPEN:** Track record numbers ($200M+ transacted, 700+ operations, 10+ yrs) — validate before Slide 1 use.
- **STILL OPEN:** Restate Esteban's EUR salary as a USD figure.
- **STILL OPEN:** Defensible TAM/SAM $ figures for Deck 2.

## Ecosystem / Phase 2 (2026-07-14)

- **RESOLVED:** Deck 2 audience = owners (Simon, Luz) + major investors + potentially government. First hub city = **Panama City.**
- Lease vs. own vs. partner with a developer-owner (Simon/TheVelopers?) for the physical hub?
- What is the equity-fund structure for taking stakes in hub-born ventures?
- What minimum franchise EBITDA threshold green-lights Phase 3 (the physical build)?
- What is the Phase-2 P&L (membership, events, matchmaking, equity, data)?
- Do the owners share the "bigger than us" ecosystem ambition, or prefer to cap at a profitable franchise business?
- Is there a government/economic-development angle in Panama (incentives, city partnership) worth pursuing early?

## White-label

- Should white-label be sold before the first branded franchise?
- Should white-label clients get access only to software/workflows, or also training and manuals?
- Should white-label contracts include non-compete or non-copy clauses?
- Should white-label be restricted by geography or agency size?

## Developer Sales OS

- Which developer/project should be the first pilot? (Simon's projects are natural candidates.)
- Should the first developer offer have no setup fee to reduce friction?
- What level of sales management can Dproperty realistically provide?
- What qualifies as a Dproperty-sourced sale versus developer-team sale?

## Product

- Should the MVP be built first on Microsoft Power Platform or a custom web app?
- Which modules are mandatory for the first franchise?
- Which modules can remain manual/templates for the first 90 days?
- Who will build the prototype?
- Should Figma come before low-code build?

## Finance

- What commission assumptions should be used by market: Panama, Colombia, Dominican Republic, Spain, etc.?
- What is the exact HQ cost to support one franchise?
- What is the minimum number of franchises/white-label clients needed to break even?
- What should the dividend policy be once profitable?

## Brand

- How much should Dproperty look like a premium real estate brand versus a technology-enabled platform?
- Should franchisees be allowed to adapt visuals locally?
- What are non-negotiable brand rules?
- What should the welcome kit physically include?

## Platform / Product Architecture (2026-07-18)

- **LMS vendor:** LearnWorlds vs edX for the embedded Academy (affects white-labeling, SSO, and Academy role provisioning). Leaning LearnWorlds — confirm.
- **Default AI agent bundle** per plan tier (which 2–3 agents are "included")?
- **AI credit-cap sizing** to protect margin against heavy T1 usage?
- **Build stack:** does the "automation-first" model run on Microsoft Power Platform, or a custom web app + Make/n8n? (Links to existing Product open question.)
- Can DeepSeek-local (or equivalent free/cheap model) reliably handle the T1 language tasks (descriptions, summaries, receipt extraction, RAG Q&A) at franchise scale?
- Is **Sales Manager** a required role above N advisors, or always optional?
- Payment provider for Finance/Back Office (Stripe vs local rails per market)?
- Does the per-prospect **Data Room** generator need legal review (what can be shared pre-signature)?
- Confidentiality model: confirm record-level visibility rules (e.g. HR grievance hidden from the Principal it concerns) are feasible in the chosen build stack.

## Manuals / Documentation (2026-07-21)

- **Language:** Are the franchise manuals authored in **Spanish, English, or bilingual**? First markets (Panama, Bogotá, Medellín) are Spanish; investor/deck audience is English. (Broadens the existing Franchise Package question from onboarding-only to all six manuals.)
- **Naming:** Confirm "**Maestro**" = HQ-internal master (M0); the franchisee's manual is "Manual de Operaciones de la Franquicia" (M2).
- **M0 timing:** Confirm the HQ / Franchisor Operations Manual is genuinely deferred until M1–M5 drafts exist.
- **Commission layering:** Confirm how the agency payroll splits (from source Proceso 7) are represented vs. the franchise royalty waterfall in M2/M5 without conflating the two layers.
- See [[../05_Franchise_Package/Manuals System Index|Manuals System Index]] for the full architecture.

## Immediate Questions for Dproperty Owners

- Do they want to build this as an internal tool only, or as a new scalable business (and do they share the ecosystem ambition)?
- Are they willing to fund a dedicated venture lead salary?
- Are they open to the equity-growth mechanism for operators (earn-in) alongside investor protection?
- Which existing assets/projects can be used in the franchise/Dproperty Select package?
- Which markets/countries would they want to test first (beyond Panama as hub)?

## Brand Architecture / Naming (2026-08-03) — P0

Opened by the house-of-brands restructure. See [[../01_Strategy/Brand Architecture|Brand Architecture]].

- **What is the parent company / ecosystem name?** 🔴 **Blocks public launch of the ecosystem website, decks, and all outward assets.**
- **What is the platform's new name** (replacing "Dproperty OS")? Must be brand-neutral so white-label partners can run on it under their own brand. 🔴 Blocker.
- **Does Dproperty Select keep the "Dproperty" name** under the parent architecture? A white-label partner selling "Dproperty Select" inventory under their own brand is a naming collision — but the name carries the flagship's credibility.
- Does the parent brand get its **own visual identity**, or does it inherit the Dproperty system (current interim assumption: inherit)?
- When and how do we do the **vault-wide rename pass**? (Currently "Dproperty OS" ambiguously means both the company and the platform. Recommendation: one controlled pass after naming, not incremental.)

## White-Label × Dproperty Select (2026-08-03) — P0 CONFLICT

- **Do white-label partners get Dproperty Select access?** 🔴 **Direct conflict in the vault.** [[../13_White_Label/White-Label OS Guide|White-Label OS Guide]] says Select is explicitly **not** included; [[Project Context Brief]] says white-label does **not** automatically get access — but the new Pillar 4 makes Select-driven profit uplift the headline proof point for **all** partners, and a 2.0% white-label payout is already defined. These cannot all be true.
  - Likely resolution: white-label **does** get Select at the 2.0% payout as standard; the old exclusion is retired. **Confirm with owners.**
  - Knock-on: if white-label gets Select, what remains genuinely exclusive to the branded franchise? (Currently: brand, investment priority, direct developer relationships, 2.5% vs 2.0%.) Is that enough to justify $30k vs $10k?
- Does a white-label partner pay royalty / Network & Brand Fund on Select earnings? (Existing default for branded: no.)

## Proof & Substantiation (2026-08-03) — P0

- **Substantiate the "proven model" claim.** Pillar 4 states partners materially increased operating profit by adding Dproperty Select to their existing offer. 🔴 We need at least one real, defensible number (named or anonymised) before this goes on a public page. Which partner? What was the uplift? Over what period?
- With zero franchisees, how much credibility load can **Dproperty's own track record** ($200M+, 700+ ops, 99%+, landmarks) carry on a parent-branded site — and is attributing it to the flagship brand honest enough?

## Public Economics Disclosure (2026-08-03)

- **How much of the franchise economics do we publish?** Exact figures ($30k / $1,000 mo / 7.5%) vs. *"desde $30,000"* vs. fully gated behind the info pack. Trade-off: qualification versus negotiating room and locking in a number publicly. Interim default: **"desde $30,000," detail gated.**
- Same question for white-label plans and the developer pricing model.
- **Currency inconsistency:** [[../05_Franchise_Package/Pre-Signing/Franchisee Acquisition Playbook|Franchisee Acquisition Playbook]] quotes **€30k**; everything else is **USD $30k**. Fix before anything public.

## RESOLVED 2026-08-03

- ✅ **Do white-label partners get Dproperty Select access?** **Yes — at 1.5% of sale price (external-partner-broker terms).** Branded stays at 2.5%. The old blanket exclusion is retired; the 2.0% rate is superseded. See [[Decision Log]] 2026-08-03.
- ✅ **What justifies branded $30k vs. white-label $10k?** Brand recognition (10+ years of traction) **plus** a full extra point on Select — a $3,000 delta per $300k Select unit, paying back the fee gap in ~7 operations.
- ✅ **What is the Dproperty brand's focus?** Investment-only. Clients buy to profit, not to live. Product mandate: profitable and reliable over pretty and livable.

## Follow-ups Opened by the 1.5% Select Revision (2026-08-03)

- **Propagate 1.5% into live project files.** 10 files in the `dproperty brain` vault still say 2.0% (`02_Projects/Private Collection/**/10_Dproperty Commercial/Commercial Terms.md` + template). 🔴 **Check whether any terms have already been agreed or signed with a partner at 2.0% before overwriting.**
- **Financial Model v0.7** — white-label Select revenue input must change from 2.0% → 1.5%. What does this do to Year 3 breakeven (already thin at ~$15k) and Year 5 EBITDA? HQ keeps a wider spread on white-label Select, so the effect should be *positive* for HQ — quantify it.
- **Does white-label pay royalty / Network & Brand Fund on Select earnings?** Existing branded default is no. As external-partner-broker terms, presumably also no — confirm.
- **"Powered by Dproperty" usage rules** — where may the endorsement appear, at what size, in which contexts, and how is it withdrawn on termination? Needs a section in the Brand Manual and a clause in the white-label agreement.
- **Does the investment-only mandate need contractual teeth** in the franchise agreement, or is it a brand-standard enforced through Select curation and HQ approval? (E.g. can a Dproperty franchisee list livability-driven product under the brand?)
- **Screening consequence:** the Franchisee Acquisition Playbook lead-scoring matrix does not yet test for *inversión vs. vivienda* orientation. Add it as a scored criterion.

## Financial Model v0.8 — New P0 Inputs (2026-08-03)

- 🔴 **What is the realistic white-label Select attach rate?** Model placeholder: **8% of units** (`Assumptions!C33`). This is now arguably the **most leveraged single number in the business** — every 4 percentage points ≈ **$147k of Year-5 EBITDA**. Currently a guess. Needs either a pilot, a partner conversation, or a defensible analogue.
- 🔴 **How many units per year does a typical white-label partner do?** Placeholder: **25** (`Assumptions!C32`), vs 50 for branded. Unvalidated.
- **Should Select attach-rate be instrumented in Plano from day one?** If it is the key operating metric, it needs to be measured per partner from the first deal, not reconstructed later.
- **Does the Year-3 EBITDA improvement (~$15k → ~$125k) change the funding ask or tranche timing?** See [[../07_Finance/Funding and Tranches]].
- **Standing:** OPEX/staffing rows still owner-unvalidated — they move EBITDA more than any revenue line.
- **Standing:** Phase-2 (ecosystem/hub) financial model still not built.
