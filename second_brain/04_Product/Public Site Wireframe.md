---
project: B_RealEstate
title: "Public Site Wireframe"
type: product_spec
status: Draft v0.6 — copy filled
version: 0.6
owner: Esteban
last_updated: 2026-08-16
source: Claude working session 2026-07-18 (content from Esteban)
tags: [product, wireframe, public-site, brand, marketing, copy]
---

> [!NOTE] Verified against canon 2026-09-23
> Wireframe needs the product-led information architecture in [[../18_Ecosystem/11 - Web Presence and Funnel Architecture]].
>
> Precedence: [[../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]

# Public Site Wireframe (Pre-Login)

> **Architecture note (2026-08-16):** B_RealEstate is the parent ecosystem and BluePrint is the back-office platform. This file remains specific to the Dproperty consumer/flagship site. The live B2B ecosystem site is https://bfranchising.com; use [[../18_Ecosystem/11 - Web Presence and Funnel Architecture]] and [[../18_Ecosystem/15 - Website Audit - bfranchising.com - 2026-08-16]].

> Low-fidelity wireframe + **filled copy** for the public-facing Dproperty site (pre-login). Parent: [[Platform Information Architecture]] (Layer 1). Next: high-fidelity build in Figma per [[Figma Handoff Notes]].
>
> **Naming:** externally = **"Dproperty Select"** (internally = Private Collection).
> **Language:** production is **Spanish-first with English translation** (bilingual toggle). Copy below is drafted in English as the working spec; a Spanish master is the next deliverable. Signature phrases stay in Spanish.
> **Tone:** calm and prestigious, with a human approach — *"we are the best, but we are reachable; we bring the best talent, not the biggest wallets."*
> `[MOCK]` = placeholder to replace before publish (e.g. contact details). Team is intentionally kept **private for now**.

---

## Brand facts (source of truth for this site)
- **Founded:** 2017, Panama.
- **What we are:** the specialist firm in **real estate investment** — without being a fund. We bring serious RE investment within reach of everyday people, through a curated, vetted portfolio.
- **Track record (Panama):** $200M+ transacted · 700+ operations · since 2017.
- **Outcomes:** **99%+ of clients have never lost capital** (in rare extraordinary cases — early exit, personal changes — we've always intermediated to at least recover the client's investment). **80%+ of clients invest with us a second time.**
- **Portfolio proof:** off-market, exclusive pre-sales that went on to become landmarks — **Bioma, Mova, Cavarrosa, Nayamara, Playa Escondida, La Maison by Fendi.**
- **Recognition:** guest speakers at **SIMA (Madrid), ELDI (Panama), Gran Salón Inmobiliario (Bogotá)**; our CEO sits on the board of the **Lonja de Bogotá**.
- **Signature phrase:** *"Somos más amigos de la matemática que de la arquitectura."*
> These facts should also flow into the [[Brand Manual]] and [[Brand Assets Index]].

## Visual direction (from [[Prototype Spec]])
- Background warm off-white `#F6F3ED` · text charcoal `#161616` · accent deep blue `#1F4E79` · secondary champagne `#B89B5E`.
- Editorial **serif** headlines; clean **sans-serif** body. Boutique, calm, editorial; generous whitespace; few, high-quality images.

---

## Public sitemap
```
HOME · ABOUT US · OUR VISION/THE ECOSYSTEM · SERVICES · DPROPERTY SELECT ·
PROJECTS (optional) · BECOME A FRANCHISE (hub) · CONTACT · LOG IN · LEGAL
```

## Global header / footer
```
┌───────────────────────────────────────────────────────────────────────┐
│ [DPROPERTY]   About  Vision  Services  Select  Franchise  │ES/EN│ [Log in] [Book a call] │
└───────────────────────────────────────────────────────────────────────┘
 ...
┌───────────────────────────────────────────────────────────────────────┐
│ DPROPERTY · [tagline]   Company / Work with us / Contact   © · Privacy · Terms · Disclaimer │
└───────────────────────────────────────────────────────────────────────┘
```
- Sticky minimal header; **Book a call** = primary (champagne), **Log in** = ghost. **ES/EN** toggle.

---

## PAGE 1 — HOME

```
┌───────────────────────────────────────────────────────────────────────┐
│ HERO  headline + subhead + dual CTA  (curated Panama/boutique image)   │
├───────────────────────────────────────────────────────────────────────┤
│ TRUST STRIP  since 2017 · $200M+ · 700+ ops · 99%+ · 80%+              │
├───────────────────────────────────────────────────────────────────────┤
│ WHO WE ARE (3 lines → About)                                           │
├───────────────────────────────────────────────────────────────────────┤
│ WHAT WE DO  [Buyers][Sellers][Investors][Developers]                   │
├───────────────────────────────────────────────────────────────────────┤
│ DPROPERTY SELECT teaser (request access)                               │
├───────────────────────────────────────────────────────────────────────┤
│ THE VISION strip (ecosystem north-star → Vision page)                  │
├───────────────────────────────────────────────────────────────────────┤
│ BECOME A FRANCHISE banner (→ hub)                                      │
└───────────────────────────────────────────────────────────────────────┘
```
**Hero headline:** *"The specialists in real estate investment."*
**Subhead:** *"Curated, off-market opportunities and honest, numbers-first advice — bringing serious real estate investment within reach. From Panama to the region."*
**CTAs:** `[ Explore opportunities ]` · `[ Become a franchise ]`
**Tagline (under hero, ES):** *"Somos más amigos de la matemática que de la arquitectura."*
**Trust strip:** *Since 2017 · $200M+ transacted in Panama · 700+ operations · 99%+ of clients never lost capital · 80%+ invest with us again.*
**Who we are (3 lines):** *"Dproperty is a boutique firm specialized in real estate investment. Since 2017 we've curated opportunities most people never see — vetted, safeguarded, and offered on preferential terms. Investment-grade real estate, made human."*

---

## PAGE 2 — ABOUT US / WHO WE ARE

```
┌───────────────────────────────────────────────────────────────────────┐
│ PAGE HEADER — "Who we are"                                             │
├───────────────────────────────────────────────────────────────────────┤
│ OUR HISTORY (timeline / narrative)                                     │
├───────────────────────────────────────────────────────────────────────┤
│ MISSION | VISION (side by side)                                        │
├───────────────────────────────────────────────────────────────────────┤
│ OUR VALUES (grid of 6)                                                 │
├───────────────────────────────────────────────────────────────────────┤
│ RECOGNITION strip (SIMA · ELDI · Gran Salón · Lonja de Bogotá)         │
├───────────────────────────────────────────────────────────────────────┤
│ CTA — Work with us / Become a franchise                                │
└───────────────────────────────────────────────────────────────────────┘
```

### Our History (narrative — timeline)
**2017 — A different kind of firm.** Dproperty was founded to close a gap: between the real investment opportunities in real estate and the advisors who truly understood its intricacies — who saw real estate as *investment*, not just buying property. The idea was simple and rare: be the firm that specializes in real estate investment, **without becoming a fund** — and bring that world closer to everyday people.

**Building the method.** We were tired of projects built only for investors and only reachable by the very wealthy — or worse, sold to first-time buyers with no real guidance. So we built a curated portfolio: validated by the market, backed by developers with proven track records, and safeguarded by due diligence and transparency. That let us offer **preferential terms to new investors**, supported by a team fluent in every part of an investment and connected to the right partners — an ecosystem you could only find at Dproperty.

**Earning our name.** Dproperty became a recognized voice in real estate investment in Panama and the region — on stage at **SIMA (Madrid), ELDI (Panama), and the Gran Salón Inmobiliario (Bogotá)** — and our CEO joined the board of the **Lonja de Bogotá**. Our off-market pre-sales became landmarks: **Bioma, Mova, Cavarrosa, Nayamara, Playa Escondida, La Maison by Fendi.**

**The turning point — a generational step.** Dproperty was built from the ground up by our founder. The next generation sees that what she created can reach far beyond Panama. We believe better buildings create better lifestyles — we want **better real estate**. That conviction, and a perspective shaped by psychology, AI, and business, revealed a bigger opportunity: to turn a career's worth of knowledge into a system others can build on. **BluePrint is only the software that lets this ecosystem exist — it is not the product. The product is the ecosystem, and the knowledge behind it.**

### Mission
> **To connect those with the means to build with those with the vision to lead — so talent is never gated by resources or network, and better real estate becomes inevitable.**

### Vision
> **To become the home of real estate talent, capital, and ideas in LATAM and Iberia — concentrating the value chain in one curated place, so that better buildings create better lives.**

### Our Values
1. **Trust over transactions** — advice we'd give our own family.
2. **Curation over volume** — fewer, better opportunities.
3. **Numbers over hype** — every projection defensible. *(Más amigos de la matemática.)*
4. **Boutique craft** — premium and personal, never mass-market.
5. **Systematized excellence** — great outcomes made repeatable.
6. **Ecosystem-minded** — we grow the whole field, not just ourselves.

---

## PAGE 3 — OUR VISION / THE ECOSYSTEM

```
┌───────────────────────────────────────────────────────────────────────┐
│ HERO — "Building the home of real estate in LATAM & Iberia"            │
├───────────────────────────────────────────────────────────────────────┤
│ WHAT WE STAND FOR — non-negotiables (6)                                │
├───────────────────────────────────────────────────────────────────────┤
│ THE ECOSYSTEM — the hub (diagram + narrative)                          │
├───────────────────────────────────────────────────────────────────────┤
│ WHY PANAMA                                                             │
├───────────────────────────────────────────────────────────────────────┤
│ HOW WE GET THERE — Phase 1 franchise → Phase 2 ecosystem (honest)      │
├───────────────────────────────────────────────────────────────────────┤
│ CTA — Partner with us / Follow the journey                             │
└───────────────────────────────────────────────────────────────────────┘
```

### What we stand for — our non-negotiables *(from the pitch deck)*
- **Boutique, always** — curated access, never volume.
- **Trust and numbers** — advice grounded in confidence *and* math, never hype.
- **Investment-first** — real estate as a vehicle for building wealth and better lives.
- **Quality without compromise** — the Dproperty standard, everywhere we go.
- **Talent over size** — we back the best craftspeople, not the biggest wallets.
- **Bigger than us** — an institution built to outlast its founders.

### The Ecosystem
We're not looking to replicate Dproperty by the book. We want to use our knowledge, expertise, and network to **potentiate the visions of the people who can move real estate forward in their own regions** — each market unique, each leader distinct — under one roof and to one standard of quality.

Picture the best in real estate — developers, agents, investors, innovators — gathered like master craftspeople in a great atelier, sharpening each other and raising the whole field. *The soul of a place like 19M, applied to real estate.* That is the ecosystem we're building toward.

**Diagram:** `Talent · Capital · Ideas → [ Curated Hub ] → better real estate + new ventures` (editorial line art, champagne accents).

### Why Panama
- **A dollarized economy** — no currency risk for cross-border investors; a natural safe harbor for capital.
- **The crossroads of the Americas** — one of the region's great connectivity hubs (air, the Canal, logistics, banking), where people and capital already meet.
- **A stable, investment-friendly destination** — infrastructure oriented to international investors.
- **A bridge between LATAM and Iberia** — the cultural and business link across the Americas and Europe, aligned with where Dproperty is expanding.
- **Where Dproperty was born** — our roots, our track record, our relationships, and our curated inventory all originate here.
- **A market that rewards curation** — premium, investment-grade projects that suit our numbers-first model.

Panama City is the natural first home for the hub.

### How we get there (honest)
- **Phase 1 — Franchise & BluePrint (now):** prove the model, grow the brand, generate the cash.
- **Phase 2 — The Ecosystem (north star):** the curated hub, funded by Phase 1. A direction we're committed to — not a dated promise.

---

## PAGE 4 — SERVICES

```
┌───────────────┬───────────────┬───────────────┬───────────────┐
│ BUYERS        │ SELLERS       │ INVESTORS     │ DEVELOPERS    │
└───────────────┴───────────────┴───────────────┴───────────────┘
  + PROCESS strip (how it works 1-2-3-4)  + CTA Book a call
```
- **Buyers:** *"Find a home with advisors who treat every purchase as a decision that should hold its value — curated options, honest guidance, no pressure."*
- **Sellers:** *"Position and sell your property with a boutique team and a qualified network of serious buyers and investors."*
- **Investors:** *"Access off-market, pre-launch opportunities — vetted developers, due-diligence-backed, with preferential terms and projections you can trust. Real estate investment, without needing to be an expert."* → links to **Dproperty Select**.
- **Developers:** *"Sell your project with a professional sales operation — qualified demand, a disciplined pipeline, and a team that protects your brand and your numbers."* → Developer Sales.

---

## PAGE 5 — DPROPERTY SELECT

```
HERO → WHAT IT IS + WHO IT'S FOR → TEASER CARDS (limited) → REQUEST ACCESS (→ CRM)
```
**Hero:** *"Dproperty Select — curated, off-market opportunities."*
**What it is:** *"Dproperty Select is our curated collection of off-market, pre-launch opportunities: projects we've vetted, negotiated, and secured on exclusive terms before they reach the open market. Each is chosen for a proven developer, sound fundamentals, and genuine investment potential — and offered to our investors on preferential terms. Past Select opportunities have gone on to become landmarks."*
**Who it's for:** *"Serious investors seeking vetted, investment-grade real estate — whether it's your first investment or your tenth."*
- Teaser cards show region/type only, "by request." **Request Access** form → buyer/investor CRM pipeline. No public prices/units.

---

## PAGE 6 — PROJECTS / LISTINGS *(optional, phase-in)*
```
FILTER BAR → GRID of project cards → project detail (gallery, key facts, "Enquire" → CRM)
```

---

## PAGE 7 — BECOME A FRANCHISE (recruitment hub)

```
HERO (dual CTA) → WHY DPROPERTY → YOUR PATH → INVESTMENT & RETURNS →
WHAT'S INCLUDED → TERRITORIES → PROOF → FAQ → strong CTA
```
**Hero:** *"Own a Dproperty. Bring investment-grade, boutique real estate to your market — with our brand, our system, our training, and our network behind you."*
**CTAs:** `[ Book a call ]` · `[ Download info pack ]`
**One-line why:** *"Everything it took us since 2017 to build — the method, the technology, the training, and the network — ready to run in your market from day one."*
**What's included:** BluePrint · white-label CRM · the Academy · brand & manuals · launch support · included AI agents.
**Proof:** *"Testimonials coming soon — you could be part of our founding cohort of franchisees."*
- Feeds the **separate franchise-recruitment CRM pipeline**; booking triggers the **Prep Pack** automation.
- Public numbers must match [[Unit Economics]] / [[Pricing Model]] ($30k→$40k, 7.5%, etc.) — pull, don't retype.

---

## PAGE 8 — CONTACT / BOOK A CALL
```
LEFT: calendar embed (GoHighLevel) — "I'm a client" / "I want a franchise"
RIGHT: quick form + office + email/phone   [all MOCK for now]
```
`[MOCK]` Office: Panama City · Email: hello@dproperty[.]— · Phone: +507 …-…. · Instagram / LinkedIn. Replace before publish.

## PAGE 9 — LOG IN
- Branded login → the OS (Layer 2). "New franchisee? Contact HQ." Password reset. SSO-ready.

## PAGE 10 — LEGAL
- Privacy · Terms · **Investment Disclaimer** (no guaranteed returns; ties to compliance). Plain, accessible.

---

## Resolved this session
Founding (2017) · history/origin/turning point · mission/vision/values · north-stars (non-negotiables) · ecosystem & hub narrative · why Panama · services · Select teaser · franchise one-liner · track-record + outcome stats · portfolio names · tone · language (ES-first bilingual).

## Still open
- [ ] **Spanish master copy** (production language) — next deliverable.
- [ ] "10+ years" vs founded-2017 phrasing — confirm.
- [ ] Real **contact details** (replace `[MOCK]`).
- [ ] **Team** section — deferred (private for now).
- [ ] Final franchise **numbers** to expose publicly (from Pricing Model / Unit Economics).

## Next step
Build the priority pages in **Figma** (Home, About, Vision/Ecosystem, Become a Franchise) using the visual direction above — or first produce the **Spanish master copy**.

## Related
[[Platform Information Architecture]] · [[Figma Handoff Notes]] · [[Strategic Thesis]] · [[Ecosystem Deck Outline]] · [[Brand Manual]]
