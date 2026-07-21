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
