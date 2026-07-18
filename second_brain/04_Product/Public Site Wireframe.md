---
project: Dproperty OS
title: "Public Site Wireframe"
type: product_spec
status: Draft v0.5
version: 0.5
owner: Esteban
last_updated: 2026-07-18
source: Claude working session 2026-07-18
tags: [product, wireframe, public-site, brand, marketing]
---

# Public Site Wireframe (Pre-Login)

> Low-fidelity wireframe + content blueprint for the **public-facing** Dproperty site — everything a visitor sees before logging in. Parent: [[Platform Information Architecture]] (Layer 1). Next step: high-fidelity build in Figma per [[Figma Handoff Notes]].
>
> **Naming:** externally we use **"Dproperty Select"** (internally = Private Collection). See Decision Log 2026-07-18.
>
> **Content flags:** `[CONFIRM]` = fact/number to validate before publish (e.g. founding year, track record). `[DRAFT COPY]` = placeholder microcopy to refine.

---

## Visual direction (carried from [[Prototype Spec]])
- Background: warm off-white `#F6F3ED` · Text: charcoal `#161616`
- Accent: muted deep blue `#1F4E79` · Secondary: champagne/gold `#B89B5E`
- Editorial **serif** for headlines; clean **sans-serif** for body/UI
- Boutique, calm, editorial — a private investment office, not a SaaS template. Generous whitespace, curated imagery (few, high-quality), strong hierarchy.

---

## Public sitemap (what "the people" see)

```
┌─ HOME
├─ ABOUT US  (History · Mission · Vision · Values · Team)
├─ OUR VISION / THE ECOSYSTEM  (North stars · Why Panama)
├─ SERVICES  (Buyers · Sellers · Investors · Developers)
├─ DPROPERTY SELECT  (curated inventory — teaser, gated)
├─ PROJECTS / LISTINGS  (optional public catalog)
├─ BECOME A FRANCHISE  ▸ hub (Why · Path · Investment · What's Included · Territories · Proof · FAQ)
├─ CONTACT / BOOK A CALL
├─ LOG IN  (→ the OS, Layer 2)
└─ LEGAL  (Privacy · Terms · Disclaimers)
```

---

## Global elements (every page)

### Header / top nav
```
┌─────────────────────────────────────────────────────────────────────┐
│  [DPROPERTY logo]    About  Vision  Services  Select  Franchise  │ ES/EN │  [Log in]  [Book a call] │
└─────────────────────────────────────────────────────────────────────┘
```
- Sticky, minimal. Two CTAs, visually distinct: **Book a call** (primary, champagne) and **Log in** (ghost/outline).
- **ES/EN language toggle** (Panama/LATAM + Iberia audience — decision pending, but build for bilingual).

### Footer (every page)
```
┌─────────────────────────────────────────────────────────────────────┐
│ DPROPERTY            Company        Work with us      Contact         │
│ [short tagline]      About          Become a Franchise   Panama City  │
│ [ES/EN]              Vision         Careers [CONFIRM]    email/phone   │
│                      Services       Dproperty Select     [socials]     │
│ ─────────────────────────────────────────────────────────────────── │
│ © Dproperty  ·  Privacy  ·  Terms  ·  Investment Disclaimer          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## PAGE 1 — HOME

**Purpose:** In one screen, say who we are, earn trust, and split traffic two ways — *clients* vs *future franchisees*.

```
┌─────────────────────────────────────────────────────────────────────┐
│  HERO                                                                 │
│  [Editorial headline — boutique real estate, systematized]            │
│  [Subhead — one line]                                                 │
│  [ Explore properties ]   [ Become a franchise ]   ← dual CTA         │
│  (calm, curated hero image: Panama skyline / boutique interior)       │
├─────────────────────────────────────────────────────────────────────┤
│  TRUST STRIP   [10+ yrs · $200M+ · 700+ ops — CONFIRM]  [logos]       │
├─────────────────────────────────────────────────────────────────────┤
│  WHO WE ARE (3-line intro)  →  link to About                          │
├─────────────────────────────────────────────────────────────────────┤
│  WHAT WE DO   [Buyers] [Sellers] [Investors] [Developers]  (4 cards)  │
├─────────────────────────────────────────────────────────────────────┤
│  DPROPERTY SELECT teaser  (curated inventory, "request access")       │
├─────────────────────────────────────────────────────────────────────┤
│  THE VISION strip  (ecosystem north-star, 1 paragraph → Vision page)  │
├─────────────────────────────────────────────────────────────────────┤
│  BECOME A FRANCHISE banner  ("Own a Dproperty" → hub)                 │
├─────────────────────────────────────────────────────────────────────┤
│  FOOTER                                                               │
└─────────────────────────────────────────────────────────────────────┘
```

**Draft hero copy:**
- Headline `[DRAFT COPY]`: *"Boutique real estate, run like a system."*
- Subhead `[DRAFT COPY]`: *"Curated properties, investor-grade advice, and the operating system behind it all — from Panama to the world."*
- Tagline to weave in (from owners): *"More friends of the math than of the architecture."* / *"Somos más amigos de la matemática que de la arquitectura."*

---

## PAGE 2 — ABOUT US / WHO WE ARE

**Purpose:** The "traditional info" a new visitor wants — history, mission, vision, values, people. This is the trust page.

```
┌─────────────────────────────────────────────────────────────────────┐
│  PAGE HEADER — "Who we are"                                           │
├─────────────────────────────────────────────────────────────────────┤
│  OUR HISTORY  (timeline / narrative)                                  │
├─────────────────────────────────────────────────────────────────────┤
│  MISSION  |  VISION   (side by side)                                  │
├─────────────────────────────────────────────────────────────────────┤
│  OUR VALUES  (grid of 5–6)                                            │
├─────────────────────────────────────────────────────────────────────┤
│  THE TEAM  (leadership — photos + short bios) [CONFIRM who to show]   │
├─────────────────────────────────────────────────────────────────────┤
│  CTA — "Work with us"  /  "Become a franchise"                        │
└─────────────────────────────────────────────────────────────────────┘
```

### Our History — narrative arc (client-friendly)
Structure as a short timeline. Draft arc (fill facts):
1. **The beginning `[CONFIRM year/founders]`** — Dproperty started as a boutique real estate agency built on curated project access and trust-based, numbers-first advice (not volume).
2. **Building the method** — over `[CONFIRM]` years and `[$200M+ / 700+ ops — CONFIRM]`, Dproperty refined a repeatable way to qualify clients, present projects, model investments, and manage brokers/developers — documented across 15 operational areas.
3. **The turning point (today)** — that know-how, which lived in people, is being turned into a system: **Dproperty OS** — so boutique excellence can scale beyond any single office.
4. **What's next** — from a great agency to the operating infrastructure behind boutique real estate, and toward a curated ecosystem (see Vision).

> Design note: keep it emotional and human, not a corporate résumé. One strong paragraph per step + a subtle vertical timeline.

### Mission (draft — from founder purpose in [[Strategic Thesis]])
> **Our mission:** to connect those with the means to build with those with the vision to lead — so that talent is never gated by resources or network, and better real estate becomes inevitable.

### Vision (draft — 10–15 yr horizon)
> **Our vision:** to become the category-defining home for real estate talent, capital, and ideas in LATAM and Iberia — concentrating the entire value chain in one curated place. *"The soul of a great community, the model of a great accelerator — for real estate."*

### Values (draft — 6, from boutique positioning)
1. **Trust over transactions** — advice you'd give family.
2. **Curation over volume** — fewer, better opportunities.
3. **Numbers over hype** — every projection defensible.
4. **Boutique craft** — premium, personal, never mass-market.
5. **Systematized excellence** — great outcomes, repeatable, not accidental.
6. **Ecosystem-minded** — we grow the whole field, not just ourselves.

---

## PAGE 3 — OUR VISION / THE ECOSYSTEM

**Purpose:** The north-star page. Communicates commitment to something bigger than transactions, and answers "why Panama."

```
┌─────────────────────────────────────────────────────────────────────┐
│  HERO — "Building the home of real estate in LATAM & Iberia"          │
├─────────────────────────────────────────────────────────────────────┤
│  OUR NORTH STARS  (3–4 commitments)                                   │
├─────────────────────────────────────────────────────────────────────┤
│  THE ECOSYSTEM  (diagram: talent × capital × ideas → curated hub)     │
├─────────────────────────────────────────────────────────────────────┤
│  WHY PANAMA  (the hub rationale)                                      │
├─────────────────────────────────────────────────────────────────────┤
│  HOW WE GET THERE  (Phase 1 franchise → Phase 2 ecosystem, honest)    │
├─────────────────────────────────────────────────────────────────────┤
│  CTA — "Partner with us" / "Follow the journey"                       │
└─────────────────────────────────────────────────────────────────────┘
```

### Our north stars (draft commitments)
- **Concentrate the value chain** — bring developers, agents, investors, capital, and ideas into one curated place so they connect fast.
- **Ungate talent** — make sure ability, not network or capital, decides who gets to build.
- **Raise the standard** — make good real estate the default, through systems, training, and transparency.
- **Build to outlast us** — an institution bigger than any founder.

### The ecosystem (diagram spec)
Simple 3-node → hub diagram: **Talent · Capital · Ideas** feeding a central **Curated Hub (Panama)** that outputs **better real estate + new ventures**. Editorial line art, champagne accents.

### Why Panama (draft rationale — validate specifics)
- **A dollarized economy** — no currency risk for cross-border investors; a natural gateway. `[CONFIRM framing]`
- **The bridge between LATAM and Iberia** — Panama connects the Americas and, via Dproperty's expansion, Europe (DACH, Benelux, Iberia).
- **Where Dproperty already has roots** — real track record, relationships, and curated inventory (Dproperty Select) originate here.
- **Investor-oriented market** — premium, investment-grade projects that suit our numbers-first advisory model.
- **A logical first hub** — the first physical node of the ecosystem is envisaged in **Panama City**.

### How we get there (honesty)
- **Phase 1 — Franchise & OS (now):** prove the model, build the brand, generate the cash.
- **Phase 2 — The Ecosystem (north star):** the curated hub, funded by Phase 1. *Ambition stated as direction, not a dated promise.*

---

## PAGE 4 — SERVICES

**Purpose:** Convert general visitors by audience. Four clear tracks.

```
┌─────────────────────────────────────────────────────────────────────┐
│  PAGE HEADER — "How we help"                                          │
├───────────────┬───────────────┬───────────────┬───────────────┐      │
│  BUYERS       │  SELLERS      │  INVESTORS    │  DEVELOPERS   │      │
│  [icon]       │  [icon]       │  [icon]       │  [icon]       │      │
│  short value  │  short value  │  short value  │  short value  │      │
│  [ Talk to us ]                                                │      │
├───────────────┴───────────────┴───────────────┴───────────────┘      │
│  PROCESS strip ("How buying/investing with Dproperty works" 1-2-3-4)  │
├─────────────────────────────────────────────────────────────────────┤
│  CTA — Book a call                                                    │
└─────────────────────────────────────────────────────────────────────┘
```
- **Investors** card links to **Dproperty Select** teaser. **Developers** card links to a light "Developer Sales" explainer (public version of Developer Sales OS).

---

## PAGE 5 — DPROPERTY SELECT (curated inventory)

**Purpose:** Show the curated program exists and create desire — without exposing sensitive inventory. Gated.

```
┌─────────────────────────────────────────────────────────────────────┐
│  HERO — "Dproperty Select: curated, investor-grade opportunities"     │
├─────────────────────────────────────────────────────────────────────┤
│  WHAT IT IS (3 lines) + WHO IT'S FOR                                  │
├─────────────────────────────────────────────────────────────────────┤
│  TEASER CARDS (blurred/limited: region, type, "by request")          │
├─────────────────────────────────────────────────────────────────────┤
│  REQUEST ACCESS form  (name, email, investor profile) → CRM          │
└─────────────────────────────────────────────────────────────────────┘
```
- No prices/units public. "Request access" routes into the **buyer/investor CRM pipeline**.

---

## PAGE 6 — PROJECTS / LISTINGS *(optional, phase-in)*

**Purpose:** Public catalog to capture organic search + leads. Can launch later.

```
┌─────────────────────────────────────────────────────────────────────┐
│  FILTER BAR  (location · type · budget · status)                     │
├─────────────────────────────────────────────────────────────────────┤
│  GRID of project cards (image, name, city, from-price, CTA)          │
├─────────────────────────────────────────────────────────────────────┤
│  Project detail → gallery, key facts, "Enquire" (→ CRM)              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## PAGE 7 — BECOME A FRANCHISE (recruitment hub)

**Purpose:** The growth engine. A mini-hub (~7 sub-pages from [[Platform Information Architecture]]). Every sub-page carries **Book a Call** + **Download Info Pack**.

```
┌─────────────────────────────────────────────────────────────────────┐
│  HERO — "Own a Dproperty. Get the whole system."                     │
│  [ Book a call ]   [ Download info pack ]                             │
├─────────────────────────────────────────────────────────────────────┤
│  WHY DPROPERTY  (OS + CRM + Academy + brand + AI team included)       │
├─────────────────────────────────────────────────────────────────────┤
│  YOUR PATH  (Discover → Apply → Sign → Onboard → Launch timeline)     │
├─────────────────────────────────────────────────────────────────────┤
│  INVESTMENT & RETURNS  (fees + sample unit economics, honest)         │
├─────────────────────────────────────────────────────────────────────┤
│  WHAT'S INCLUDED  (platform, CRM, academy, brand, support, agents)    │
├─────────────────────────────────────────────────────────────────────┤
│  TERRITORIES  (map: available / taken)                               │
├─────────────────────────────────────────────────────────────────────┤
│  PROOF  (case studies / testimonials / numbers) [CONFIRM]            │
├─────────────────────────────────────────────────────────────────────┤
│  FAQ  (financing, risk, timeline, exclusivity)                       │
├─────────────────────────────────────────────────────────────────────┤
│  STRONG CTA — Book a call                                             │
└─────────────────────────────────────────────────────────────────────┘
```
- Feeds the **separate franchise-recruitment CRM pipeline** (not property buyers).
- Booking a call triggers the **Prep Pack** automation (agenda + info pack + short video).
- Public numbers here must match [[Unit Economics]] / [[Pricing Model]] ($30k→$40k, 7.5%, etc.) — pull, don't retype.

---

## PAGE 8 — CONTACT / BOOK A CALL

```
┌─────────────────────────────────────────────────────────────────────┐
│  Split layout:                                                        │
│  LEFT: calendar embed (GoHighLevel) — pick client vs franchise       │
│  RIGHT: quick contact form + office (Panama City) + email/phone      │
└─────────────────────────────────────────────────────────────────────┘
```
- Routing choice ("I'm a client" / "I want a franchise") sends to the correct pipeline.

---

## PAGE 9 — LOG IN
- Simple, branded login → **the OS (Layer 2)**. "New franchisee? Contact HQ." Password reset. SSO-ready.

## PAGE 10 — LEGAL
- Privacy Policy · Terms · **Investment Disclaimer** (no guaranteed returns — ties to compliance). Plain, accessible.

---

## Content still needed from you (to finalize copy)
- [ ] Founding year, founders, real milestones for **History** `[CONFIRM]`
- [ ] Approve/replace **track-record numbers** (10+ yrs / $200M+ / 700+ ops) — still flagged unvalidated in [[Pitch_Deck_Content]]
- [ ] Final **Mission / Vision / Values** wording (drafts above)
- [ ] **Why Panama** — confirm the points we can state publicly
- [ ] **Team** — who appears on About
- [ ] Language: ES-first, EN-first, or bilingual toggle
- [ ] Proof assets (testimonials/case studies) for the franchise hub

## Next step
Build the priority pages in **Figma** (Home, About, Vision/Ecosystem, Become a Franchise) at high fidelity using the visual direction above. This wireframe is the source spec.

## Related
[[Platform Information Architecture]] · [[Platform Scenario Playbook]] · [[Roles and Access Matrix]] · [[Figma Handoff Notes]] · [[Strategic Thesis]] · [[Ecosystem Deck Outline]]
