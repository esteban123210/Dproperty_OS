---
project: B_RealEstate
title: "Handoff - Sales Playbook (M4)"
type: handoff
deliverable: "Sales Playbook (M4)"
target_output: "Printable book (PDF)"
target_tool: "Markdown-to-PDF book generator (e.g. Typora/Pandoc/Prince) or an AI document tool (e.g. Gamma docs, Adobe)"
source_notes: ["02_Offers/05_Dproperty_Franchise/04D - Sales Playbook.md", "Process Library 01–05"]
version: 0.5
status: Ready to generate (tracks M4 v0.5)
owner: Esteban
last_updated: 2026-07-21
tags: [handoff, production, sales, manual]
---

> [!NOTE] Verified against canon 2026-09-23
> **Regenerate before external use.** Handoffs are self-contained snapshots, so this file may still inline pre-reconciliation naming, pricing or product boundaries. Check against canon: BluePrint owns the deal from qualified opportunity · Building Blocks (not Academy) · B_ Partner (not White-Label) · $399/$799 + $1,500 setup · $950k raise · no “one database” or “CRM propio” claims. If a handoff and its source note disagree, **the source note wins**.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# HANDOFF — Sales Playbook (M4)

> **One-file, self-contained package** to generate the final **printable Sales Playbook book (PDF)**. Everything the tool needs is inline. `[local]` marks market-specific values to be filled from the market pack before printing a market edition.

## 0. Production Brief
- **Deliverable:** Dproperty Sales Playbook — the agent-facing selling manual (Tier 2).
- **Output:** print-ready **PDF book**, ~20–30 pages.
- **Target tool:** a Markdown→PDF book generator, or an AI doc tool that accepts structured Markdown and produces a designed, paginated PDF.
- **Fidelity goal:** boutique, premium, clean — looks like a real published playbook, not a Word doc.
- **Audience:** the franchisee's Sales Advisors (SA).
- **Language:** author master in **EN**; produce **ES** edition for Panama/Colombia `[local]`.

## 1. Design & Brand Direction
- **Brand voice:** confident, warm, analytical, premium, international (per [[../10_Brand_and_Web/Brand Manual]]). Never pushy.
- **Typography:** elegant serif or refined sans for headings; highly readable body. Generous white space.
- **Color:** Dproperty palette (from brand kit — insert hex when brand finalizes). Use one accent for section dividers, callouts, and table headers.
- **Layout:** cover page → title page → table of contents → numbered sections → process quick-reference appendix → back cover. Running header with "Dproperty · Sales Playbook"; page numbers footer.
- **Callouts:** style the "Golden rules" and script blocks as boxed callouts.

## 2. Assets Required
| Asset | Purpose | Source | Status |
|---|---|---|---|
| Logo (horizontal + mark) | Cover, header | Drive/Brand | need |
| Brand color hex + fonts | Whole book | Brand kit (pending) | need |
| Cover image (boutique real estate) | Cover | Drive/Brand | need |
| Icon set (optional) | Section dividers | Brand kit | optional |

## 3. Tool Instructions (the prompt)
> Paste this file into the tool with the following instruction:

"Generate a **print-ready PDF book** from the Markdown in *Section 4*. Requirements: (1) a designed **cover** with the Dproperty logo, the title *Sales Playbook*, and subtitle *For Dproperty Sales Advisors*; (2) an auto-generated **table of contents** from the H2/H3 headings; (3) consistent premium typography and spacing per *Section 1*; (4) render every table cleanly and keep them from breaking across pages where possible; (5) style blockquotes and 'Golden rules'/'Script' blocks as boxed callouts in the accent color; (6) include the **Process Quick-Reference appendix** as the final chapter; (7) add running headers and page numbers; (8) output US-Letter and A4 versions. Do **not** invent content — use only what is provided. Preserve `[local]` tags as visible placeholders."

## 4. Final Content (self-contained)

### Cover
**Dproperty — Sales Playbook** · *For Dproperty Sales Advisors* · Version 0.5 · Confidential

### Who this is for
The franchisee's **Sales Advisors (SA)** — prospect, qualify, present, negotiate, close. This is the agent-facing view of Dproperty's commercial processes. Roles, never names (SA, SD, OC, OD, CA, PH). Currency **USD** unless a market overrides. `[local]` values are set per market.

### 1. Sales philosophy
Dproperty sales are **consultative, trust-based, and curated**. The goal is not to push inventory — it is to understand the buyer/investor and match them to the right opportunity. Present quality, not volume. Never overpromise; use data carefully. This boutique difference is non-negotiable.

### 2. The five processes
| # | You are selling… | Process |
|---|---|---|
| 1 | Any lead (pre-deal) | Lead capture & qualification |
| 2 | Off-plan / pre-construction | Preventa (Lista Cero) |
| 3 | An existing property to an end user | Secondary market |
| 4 | An investor's contract to a new buyer | Assignment (cesión) |
| 5 | A long-stay rental | Rental |

**Golden rules (all five):** every lead in the CRM within SLA `[local]`, no lead without a next action; **no offer without SD approval**; everything material is written down; Dproperty Select follows HQ rules (§8).

### 3. Who does what
SA = you (prospecting → close). SD = approves offers/strategy/final contract, runs weekly pipeline. OC = contracts, documents, billing, signing, commission execution. OD = process compliance/exceptions (esp. rentals). CA = approves client/special profiles (esp. rentals). PH = inspection, inventory, handover. *In a small office one person wears several hats — the responsibility still applies.*

### 4. Pipeline stages
`New → Qualified → Presenting → Offer (SD-approved) → Reserved → Contract → Closed → Follow-up`. Keep every deal's stage current in the CRM.

### 5. Prospecting — first 100 contacts
Map & segment 100: family, friends, business contacts, investors, entrepreneurs, expats, brokers, developers, lawyers/accountants, past clients. Work them with the Day 1/3/7/14 cadence (Process 1).

### 6. Client qualification
Ask: buying for investment/lifestyle/family/residency/diversification/income? Budget (liquid vs financed)? Country/city? Risk tolerance & return expectations? Timeline? Financing? Who else decides? Qualification sets the process and the priority (Hot/Warm/Cold).

### 7. Core scripts
**Personal-network launch:** "Hi [Name], I wanted to share something I'm building with Dproperty — a more curated way to guide clients and investors through real estate, with stronger project analysis, trusted processes, and access to selected developments. I thought of you because you may be interested directly, or know someone who'd value this kind of guidance."
**First follow-up:** "Thanks for the interest. The best next step isn't random listings — it's understanding what would actually make sense for you. Can we do a short call so I can explain how Dproperty works?"
**Discovery structure:** motivation → budget/liquidity → location → risk & return → timeline → decision-makers. Log everything; identify the process; set the next step.
**Dproperty Select intro:** "Some opportunities are part of Dproperty Select — curated by HQ and handled with a more controlled process because of the nature of the projects and investor relationships. I can introduce one if it fits your profile."
**Objection handling:** never pressure. Acknowledge → clarify the real concern → reframe with data → propose a small next step. For price/financing, involve OC/SD early.

### 8. Dproperty Select — advisor rules
HQ-controlled. You **may** present it and earn the fixed originator payout `[local: 2.5% branded / 1.5% white-label of sale price]`. You **may not** create/edit projections or materials without HQ approval, negotiate directly with the developer, or bypass HQ on registration.

### 9. Weekly routine
Mon: pipeline review (SD). Tue: outreach. Wed: broker/developer follow-up. Thu: meetings/presentations. Fri: CRM hygiene, follow-ups, report to SD.

### 10. Targets
Time to first contact < 24h `[local]` · Lead→meeting > 25% · Meeting→reservation (preventa) > 30% · Offers→reservations (secondary) > 40% · Rentals: offers with formal backup 100% · NPS > 80.

### 11. Localization
Before use in a new market, HQ confirms currency, commission %, reservation/down-payment norms, KYC/AML set, legal closing steps, deposit rules, language. Process stays the same; values change.

### Appendix — Process Quick-Reference (inline for the book)

**P1 · Leads** — Capture → register (<1h `[local]`) → verify → qualify (Hot/Warm/Cold) → assign (SD) → first contact (<24h) → follow-up (D1/3/7/14) → nurture. *Approver: SD; CRM owner: BI.*

**P2 · Preventa** — Meeting/profile → present + ROI → validate (SD) → reservation `[local amount]` → approve (SD) → notify developer (OC) → KYC docs → contract → approve (SD) → sign → down-payment `[local %]` → collect commission → post-sale. *No reservation to developer without SD.*

**P3 · Secondary** — Profile → visits → offer → **SD approves** → present → negotiate (SD) → reservation → contract → parallel legal checks `[local]` → final approval (SD) → sign + collect → legal closing → handover + inventory (PH) → 30-day follow-up.

**P4 · Assignment** — Profile buyer → visits → **dual validation if SA ≠ originating advisor** → offer → dual approval (SD decides conflicts) → present to assignor → negotiate → reservation → assignment contract → final approval → tripartite signing → handover → ROI report. *Control: protect the originating investor relationship.*

**P5 · Rental** — Register → qualify (flag special profiles) → visit + mandatory disclosures (furnished: 2 deposits + first month `[local]`) → structure offer → phone the owner → inform listing advisor → **formal traceability email** → **CA approves profile** → formal offer + draft (OC) → review route (OD) → **single approved contract version** → sign + payments → renovation record → inventory (PH) → log warranties → handover → activate 45/60-day alerts → 7 & 30-day follow-up. *Rule: the call never replaces the written record.*

## 5. Build & QA Checklist
- [ ] Cover + TOC generated; headings hierarchical.
- [ ] All tables render; no mid-row page breaks.
- [ ] Callouts styled (Golden rules, scripts).
- [ ] Process appendix included.
- [ ] `[local]` placeholders visible (or resolved for a market edition).
- [ ] Brand colors/fonts applied; logo on cover + header.
- [ ] US-Letter + A4 PDFs exported.
- [ ] Content matches source ([[../02_Offers/05_Dproperty_Franchise/04D - Sales Playbook]] v0.5) — no invented material.

## 6. Source & Change Log
- **Source:** [[../02_Offers/05_Dproperty_Franchise/04D - Sales Playbook]] (M4 v0.5) + Process Library [[../08_Operations/Process Library/01 - Leads]]–[[../08_Operations/Process Library/05 - Long-Stay Rental]].
- **Change log:** 0.5 (2026-07-21) — created from M4 v0.5.
