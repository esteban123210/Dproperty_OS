---
project: B_RealEstate
title: "CLAUDE DESIGN - Ecosystem Website Design Prompt"
type: design_brief
deliverable: "B_RealEstate ecosystem website — full visual + motion design"
target_tool: "Claude Design"
version: 1.0
status: "Ready to paste"
owner: Esteban
created: 2026-08-03
tags: [handoff, design, website, motion, claude-design]
---

> [!NOTE] Verified against canon 2026-09-23
> **Regenerate before external use.** Handoffs are self-contained snapshots, so this file may still inline pre-reconciliation naming, pricing or product boundaries. Check against canon: BluePrint oversees management outcomes across the commercial lifecycle without executing the sale · Building Blocks (not Academy) · B_ Partner (not White-Label) · $399/$799 + $1,500 setup · $950k raise · no “one database” or “CRM propio” claims. If a handoff and its source note disagree, **the source note wins**.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# DESIGN PROMPT — B_RealEstate Ecosystem Website

> **Live-site/naming update (2026-08-16):** B_RealEstate and BluePrint are the active names; https://bfranchising.com is live. This handoff remains production history. Before further build work, use [[../10_Brand_and_Web/Website Audit - bfranchising.com - 2026-08-16|the live-site audit]] and [[../01_Canon/09 - Unit Economics Registry|the economics registry]] as the correction list.

**Paste this entire document into Claude Design.**

---

# 1. WHAT WE ARE DESIGNING

A marketing website for a company that operates **a franchising ecosystem for real estate**. Not a franchise directory. Not a SaaS landing page. Something closer to a **well-made architectural monograph that moves**.

The company is **B_RealEstate**. Dproperty is its **flagship brand**, the way Mercure belongs to Accor. The platform is **BluePrint**.

> **B_RealEstate** is the parent ecosystem. **B_** is the core visual identity and extensible marker. **BluePrint** is the back-office platform; in its wordmark, `B_` remains the anchor and `luePrint` is underlined. The name also supports the site's architectural drawing language.

## The strategic job of the design

The visitor is an experienced real estate agent or agency owner considering a $30,000 decision. They have seen a hundred franchise pitches, all of which looked like franchise pitches.

**The website is the product demo.** We sell a technology platform, a CRM, and a learning system. If the site itself feels fast, considered, and alive, the visitor concludes the software is too — before they see a single screenshot. Every motion decision is therefore a *product* claim, not a decorative one.

**Feel target:** *techy but boutique. Premium but accessible. Confident but never loud.*

---

# 2. THE CREATIVE CONCEPT — "THE LINE"

One organizing device runs the entire site: **a single thin, hand-drawn line.**

It enters at the top of the homepage and never breaks. It descends through the page as the visitor scrolls, and **it is the franchisee's path** — it branches at decisions, loops around obstacles, gathers tools as it goes, and arrives somewhere. Section content hangs off it like annotations on an architect's drawing.

Think: **an architect's pen sketch of a journey**, drawn live, at the speed of your scroll.

## Why this device

1. It literally *is* the growth path — the site's structure and its meaning are the same thing.
2. Thin sketch lines are the opposite of mass-market franchise design (stock photos, badges, loud CTAs). It signals *boutique* immediately and without saying the word.
3. It gives us a continuous scroll-linked animation that feels crafted rather than templated.
4. It's a quiet joke on the brand line — *"we're better friends with math than with architecture"* — delivered in architectural drawing language.

## Line behaviour rules

- Stroke weight **1–1.5px**, charcoal at **~25% opacity** for the un-travelled path ahead.
- **Travelled path** behind the scroll position renders solid charcoal, and the ~120px immediately at the scroll head glows **champagne**. The visitor always sees exactly where they are.
- The line is **slightly irregular** — hand-drawn, not geometric. Very subtle wobble, like a fine technical pen. Never a perfect Bézier.
- It **branches** at the three-doors moment into three paths, then two of them fade back while the chosen one continues.
- At tool moments it sprouts **small orthogonal ticks** with labels, like measurement annotations on a plan.
- On mobile it runs down the **left margin** at ~24px inset, thinner, still continuous.

---

# 3. THE OPENING LINE

The hero headline must say: *we franchise, but the boutique approach applies to the franchising itself — not just to the real estate.*

**Three options. Recommendation: Option A.**

### Option A — recommended
- **ES:** *Boutique no es solo cómo trabajamos. Es cómo franquiciamos.*
- **EN:** *Boutique isn't only how we work. It's how we franchise.*

Two short sentences, second one lands the twist. Sets up the whole site: everything that follows is evidence for the claim.

### Option B
- **ES:** *No franquiciamos en serie. Construimos una contigo.*
- **EN:** *We don't mass-produce franchises. We build yours with you.*

More combative, more explicit about the competition.

### Option C
- **ES:** *El mismo cuidado con el que elegimos una inversión, aplicado a elegirte a ti.*
- **EN:** *The same care we use to choose an investment, applied to choosing you.*

Warmest, most flattering; slightly longer, works better as a sub-headline.

**Subhead (both, under whichever headline):**
- **ES:** *Te damos el método, la tecnología, la formación y la red que construimos desde 2017 — y tú decides cuánto de nuestra marca quieres usar.*
- **EN:** *We give you the method, the technology, the training and the network we've built since 2017 — and you decide how much of our brand you want to use.*

---

# 4. ART DIRECTION

## Palette — light always, never a dark section

```
Bone           #F7F4ED   primary background
Bone Deep      #EFEAE0   alternating sections, cards
Bone Warm      #FAF8F3   elevated surfaces, video frames
Charcoal       #1A1A1A   primary text, the line
Charcoal Soft  #55514C   secondary text, captions
Champagne      #B89B5E   accent, CTAs, active path, highlights
Deep Blue      #1F4E79   data & technical moments only — used sparingly
Sketch Grey    rgba(26,26,26,0.25)   un-travelled line, dividers
```

**Rules:**
- **Every background stays light.** No dark-mode sections, no charcoal hero, no inverted footer.
- Depth comes from **bone-tone layering** (Bone → Bone Deep → Bone Warm), never from darkness.
- Champagne is a **seasoning**: CTAs, the active path head, one or two numbers per screen. If more than ~5% of a viewport is champagne, reduce it.
- Deep Blue appears **only** where we're being technical — data viz, the platform section, code-adjacent labels. It should feel like a different register when it shows up.
- Shadows: almost none. Where needed, very soft and warm — `0 2px 24px rgba(26,26,26,0.04)`.

## Typography

**Headlines — Playfair Display**
- Weights 400 and 500. Avoid 700+ except for rare single-word emphasis.
- **Generous sizes.** H1 desktop 72–96px. H2 48–56px. Tight line-height (1.05–1.15) and slightly negative tracking (-0.02em) so it reads editorial, not decorative.
- Use *italic* Playfair for pull-quotes and the signature Spanish phrase. Playfair's italic is beautiful — use it deliberately, maybe 3–4 times site-wide.

**Body — Inter**
- Weights 400 / 500. Body 17–18px, line-height 1.65, `Charcoal Soft`.
- Generous measure limits: max ~62 characters per line.
- *(Acceptable alternatives: Söhne, Suisse Int'l, Neue Haas Grotesk.)*

**Technical accent — JetBrains Mono**
- Used **sparingly and deliberately**: metric labels, percentages, step numbers, video chapter markers, the roadmap phase labels.
- 12–13px, uppercase, letter-spaced +0.08em, `Charcoal Soft` or `Deep Blue`.
- This is the single strongest "techy" signal in the whole system, precisely because it's rare. It should feel like an engineer's annotation on a beautiful drawing.

**Pairing intent:** Playfair carries the boutique. Inter carries the clarity. Mono carries the technology. Three voices, clearly separated by role — never mixed within one element.

## Imagery

- **Very few photographs.** Where they appear: architectural, natural light, warm, un-peopled or lightly peopled. Never stock-photo handshakes, never a smiling team in a boardroom.
- Photos sit in **rounded frames (16px radius)** with a thin bone border, never bleeding full-width edge to edge except the hero.
- **Line drawings do most of the visual work** — sketch diagrams, the path, tool annotations, the roadmap. This is the site's signature.
- All imagery slightly desaturated and warmed to sit inside the bone palette.

## Shape language

- **Buttons:** fully rounded (pill, `border-radius: 100px`). Primary = champagne fill, charcoal text. Secondary = 1px charcoal outline, transparent, fills to bone-deep on hover.
- **Cards / frames:** 16–20px radius.
- **Video frames:** 20px radius with a 1px `Sketch Grey` border and a very soft warm shadow.
- Nothing sharp-cornered anywhere. Softness is part of "accessible."

---

# 5. MOTION SYSTEM — THE PRIORITY

Motion is the product argument. Budget real attention here.

## Global principles

1. **Everything is scroll-linked, nothing is on a timer.** The visitor drives. No autoplaying carousels, no timed reveals.
2. **Smooth scroll throughout** (Lenis or equivalent), lerp ~0.08 — enough to feel expensive, not enough to feel laggy or seasick.
3. **Ease:** custom cubic-bezier `(0.16, 1, 0.3, 1)` — fast start, long soft settle. Use this everywhere for coherence.
4. **Durations:** micro-interactions 200–300ms · content reveals 600–800ms · section transitions 1000–1200ms.
5. **Stagger:** children reveal 60–80ms apart. Never all at once.
6. **Respect `prefers-reduced-motion`** — collapse to simple opacity fades, keep the line static and fully drawn.
7. **Nothing bounces.** No spring overshoot, no elastic. Calm, weighted, decisive.

## The signature animations

### A. The Line draws with scroll
The master interaction. An SVG path spanning the full page height, `stroke-dashoffset` bound directly to scroll progress. The champagne "head" is a short gradient segment that travels with the scroll position. This runs continuously the entire way down the homepage.

### B. Text reveals — masked line rise
Headlines reveal **by line**, each line rising from behind an invisible mask with a 24px upward translate and opacity 0→1, staggered 70ms. Not a fade-in — a *rise*, like type being set. This is the single most-used reveal on the site; make it feel perfect.

### C. Pinned horizontal journey
At the "Your Path" section the page **pins** and the six steps scroll **horizontally** while the visitor scrolls vertically. The line runs horizontally through them. Each step's content reveals as it enters centre. Unpins and returns to vertical flow at the end. This is the moment the site most clearly "isn't a document."

### D. Product video reveals
As each product section enters the viewport, the video frame **scales from 0.94 → 1** with a soft fade while the sketch line draws a bracket around it. Video begins playing muted on entry, pauses on exit. Never autoplay before it's visible.

### E. Number count-ups
Stats ($200M+, 700+, 99%) count up from zero over ~1.2s on entry, in JetBrains Mono, once only. Ease-out so the last digits settle slowly.

### F. Sketch diagram self-drawing
Every diagram (the house-of-brands, the roadmap, the payback comparison) draws itself stroke-by-stroke on entry, 900–1400ms, staggered by element. Like watching someone sketch it.

### G. Magnetic buttons
Primary CTAs subtly attract the cursor within ~40px, translating up to 6px toward it, snapping back on exit. Desktop only.

### H. Parallax layering
Backgrounds and decorative sketch elements move at 0.85–0.95× scroll speed; foreground content at 1×. Very subtle — felt, not noticed.

### I. Page transitions
Route changes: content fades out (300ms), the line **stays continuous** across the transition and redraws into the new page's path (500ms), new content rises in. The line is the thread between pages — it should feel like one continuous document.

---

# 6. HEADER & NAVIGATION

## Header — minimal, always

```
┌──────────────────────────────────────────────────────────────┐
│  B_RealEstate                                              ☰     │
└──────────────────────────────────────────────────────────────┘
```

- **Logo left. Burger right. Nothing else.**
- Fixed, transparent over bone. On scroll past 100px it gains a **1px bottom hairline** in Sketch Grey and a slight bone-warm backdrop blur. No solid bar, no shadow.
- Burger is **two thin lines** (1.5px, 22px wide, 7px apart), charcoal. On hover the lines **shorten slightly and separate by 2px**. On click they cross into an X over 300ms.
- Height 72px desktop / 60px mobile.

## Menu overlay

Clicking the burger opens a **full-screen bone overlay**:

- Overlay wipes in from the right as a **soft mask reveal** (not a slide) over 600ms.
- Nav items are **large Playfair Display, 48–64px**, stacked left-aligned with generous spacing, staggered in 80ms apart.
- Each item has a **thin sketch line to its left** that draws in on hover and extends toward the label.
- Hover: item translates right 8px, colour charcoal → champagne.
- Bottom-left: `ES | EN` toggle in JetBrains Mono, plus small links (Log in, Contact) and social.
- Bottom-right: a small, slowly-drawing decorative sketch of the path — a quiet visual signature.
- Close: X top right, or `Esc`, or clicking any item.

**Menu items:** Inicio · Ecosistema · Franquicia Dproperty · White-Label · Desarrolladores · Plataforma · Nosotros · Contacto
*(EN: Home · Ecosystem · Dproperty Franchise · White-Label · Developers · Platform · About · Contact)*

---

# 7. FULL HOMEPAGE WIREFRAME

The homepage **is the franchisee's growth path**, start to finish. Each section is a stage of the journey. The line connects all of them without a break.

---

## SECTION 1 — HERO · *the invitation*

```
┌──────────────────────────────────────────────────────────────┐
│  B_RealEstate                                              ☰     │
│                                                              │
│                                                              │
│         Boutique no es solo cómo trabajamos.                 │
│         Es cómo franquiciamos.                               │
│                                                              │
│         Te damos el método, la tecnología, la formación      │
│         y la red que construimos desde 2017 — y tú           │
│         decides cuánto de nuestra marca quieres usar.        │
│                                                              │
│         ( Empezar el recorrido )   ( Agendar una llamada )   │
│                                                              │
│                            │                                 │
│                            │  ← the line begins              │
│                        ⌄ scroll                              │
└──────────────────────────────────────────────────────────────┘
```

- Full viewport height. Bone background. **No hero image** — type, whitespace, and the line only. The restraint *is* the statement.
- H1 in Playfair Display 400, 88px desktop, max-width ~14 words per line. Reveals with the masked line-rise, 120ms stagger between the two sentences — the second lands like a turn.
- Subhead fades up 400ms after headline completes.
- CTAs rise in last. Primary = champagne pill. Secondary = outline pill.
- **The line is born** at the bottom centre: it draws downward from the CTA area, 2s, easing out, then waits.
- Scroll cue: a small vertical line that pulses slowly, plus `⌄`. Fades out permanently after first scroll.
- Very subtle grain/paper texture over the bone — 2–3% opacity noise. Gives the whole site a **paper feel** that supports the sketch language.

---

## SECTION 2 — THE PREMISE · *why we're different*

```
┌──────────────────────────────────────────────────────────────┐
│    │                                                         │
│    │   La mayoría de las franquicias venden un manual.       │
│    │                                                         │
│    │   Nosotros llevamos desde 2017 construyendo             │
│    │   una forma de trabajar. Ahora la abrimos —             │
│    │   con la misma curaduría con la que elegimos            │
│    │   cada inversión.                                       │
│    │                                                         │
│    │            ─── +$200M ─── 700+ ─── 99%+ ───             │
│    │                                                         │
└──────────────────────────────────────────────────────────────┘
```

**ES:** *La mayoría de las franquicias venden un manual. Nosotros llevamos desde 2017 construyendo una forma de trabajar — y ahora la abrimos, con la misma curaduría con la que elegimos cada inversión.*
**EN:** *Most franchises sell a manual. We've spent since 2017 building a way of working — and now we're opening it, with the same curation we use to choose every investment.*

- Line runs down the **left third**; text sits right of it. Asymmetric, editorial.
- Stats appear **on the line itself** as annotation ticks, in JetBrains Mono, counting up on entry.
- Small caption beneath, `Charcoal Soft` 13px: *Los números de Dproperty, nuestra marca insignia.* / *Dproperty's numbers — our flagship brand.* **(Required attribution.)**

---

## SECTION 3 — THE FORK · *three doors*

The line **splits into three** — the site's first big visual moment.

```
┌──────────────────────────────────────────────────────────────┐
│                            │                                 │
│                    ┌───────┼───────┐                         │
│                    │       │       │                         │
│              ┌─────┴─┐ ┌───┴───┐ ┌─┴─────┐                   │
│              │DPROP. │ │WHITE- │ │DESARR-│                   │
│              │FRANCH.│ │LABEL  │ │OLLAD. │                   │
│              │       │ │       │ │       │                   │
│              │Opera  │ │Opera  │ │Tu equi│                   │
│              │bajo   │ │bajo la│ │po, sin│                   │
│              │nuestra│ │tuya.  │ │constr-│                   │
│              │marca. │ │       │ │uirlo. │                   │
│              │       │ │       │ │       │                   │
│              │Inver- │ │Tu mer-│ │Tu pro-│                   │
│              │sión,  │ │cado,  │ │ducto, │                   │
│              │exclus.│ │tus re-│ │nuestro│                   │
│              │       │ │glas.  │ │equipo.│                   │
│              │( ver )│ │( ver )│ │( ver )│                   │
│              └───┬───┘ └───┬───┘ └───┬───┘                   │
│                  └─────────┼─────────┘                       │
│                            │                                 │
└──────────────────────────────────────────────────────────────┘
```

**Section heading ES:** *Tres caminos. El mismo ecosistema.*
**EN:** *Three routes. One ecosystem.*

- The split **draws** as it enters: one line becomes three over ~1s, then the three cards rise in staggered.
- **All three cards identical in size, weight, and treatment.** No badge, no "most popular," no highlight. This is a hard rule — white-label must never look like the budget tier.
- Cards: Bone Warm, 20px radius, 1px Sketch Grey border, generous internal padding.
- **Hover:** the card's own path segment brightens to champagne, card lifts 4px, border darkens slightly. The other two dim to 60%. The visitor feels the branch.
- Below the cards the three lines **rejoin into one** — the ecosystem point, made visually.

---

## SECTION 4 — THE PATH · *pinned horizontal journey*

**The centrepiece.** The page pins; the journey scrolls sideways.

```
┌──────────────────────────────────────────────────────────────┐
│   TU CAMINO CON NOSOTROS                          [01 / 06]  │
│                                                              │
│  ──●─────────●─────────●─────────●─────────●─────────●──     │
│    01        02        03        04        05        06      │
│  DESCUBRE  APLICA    FIRMA    ONBOARDING LANZAMIENTO CRECE   │
│                                                              │
│   ┌────────────────────────┐                                 │
│   │  Conversamos sin        │   [ sketch illustration of     │
│   │  presión. Entendemos    │     the current step —         │
│   │  tu mercado, tu red y   │     thin line drawing,         │
│   │  tu ambición — y te     │     draws itself on entry ]    │
│   │  decimos honestamente   │                                │
│   │  qué camino te sirve.   │                                │
│   │                         │                                │
│   │  ~ 2 semanas            │                                │
│   └────────────────────────┘                                 │
└──────────────────────────────────────────────────────────────┘
```

**The six steps (ES / EN):**

| # | ES | EN | Duration | Content |
|---|---|---|---|---|
| 01 | **Descubre** | **Discover** | ~2 semanas | Honest conversation. We assess your market, network and ambition — and tell you which route actually fits. Including "none of them." |
| 02 | **Aplica** | **Apply** | ~2 semanas | Mutual diligence. You meet the team, see the numbers, talk to HQ. We check fit — this is curation, not enrolment. |
| 03 | **Firma** | **Sign** | ~1 semana | Clear terms, no surprises. Territory defined. You know exactly what you're buying and what it returns. |
| 04 | **Onboarding** | **Onboarding** | ~4 semanas | The Academy, the platform, the CRM, the manuals. Your team trained, your systems live, your templates localised. |
| 05 | **Lanzamiento** | **Launch** | 30/60/90 | The launch plan runs. HQ beside you weekly. First listings, first pipeline, first deals. |
| 06 | **Crece** | **Grow** | Ongoing | Dproperty Select access, network events, new markets, and a seat in the ecosystem as it's built. |

**Motion:**
- Section pins for ~600vh of scroll; content translates horizontally.
- The **line runs horizontally** through the step nodes. Each node fills champagne as it becomes active.
- Step counter top-right in JetBrains Mono updates as you travel.
- Each step's text block and sketch illustration reveal as it centres; previous step fades to 30%.
- **Mobile:** unpin entirely. Becomes a vertical timeline with the line down the left, steps stacked, each revealing on scroll.

---

## SECTION 5 — THE TOOLKIT · *what you're actually getting*

The line sprouts **annotation ticks**, each labelling a tool — like a plan drawing with callouts.

```
┌──────────────────────────────────────────────────────────────┐
│   LO QUE RECIBES                                             │
│                                                              │
│         │                                                    │
│    ─────┼──── Plataforma BluePrint                           │
│         │                                                    │
│    ─────┼──── CRM white-label                                │
│         │                                                    │
│    ─────┼──── Academia                                       │
│         │                                                    │
│    ─────┼──── Agentes de IA                                  │
│         │                                                    │
│    ─────┼──── Dproperty Select                               │
│         │                                                    │
│    ─────┼──── Manuales y plantillas                          │
│         │                                                    │
│    ─────┼──── Eventos y red                                  │
│         │                                                    │
│    ─────┼──── Acompañamiento de lanzamiento                  │
│         │                                                    │
└──────────────────────────────────────────────────────────────┘
```

- Each tick **draws outward** from the line as it enters, label fading in behind it, 80ms stagger.
- Labels in Playfair 28px; a one-line Inter description appears on hover in `Charcoal Soft`.
- The three tools with videos (**Plataforma, CRM, Academia**) show a small champagne dot and are clickable — clicking scrolls to their showcase below.

---

## SECTION 6 — PRODUCT SHOWCASES · *three video moments*

Three consecutive full-width sections, one per product. **This is where "techy" earns its keep.**

### Layout per showcase (alternating sides)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   ┌─────────────────────────────┐    LA PLATAFORMA           │
│   │                             │                            │
│   │   [ VIDEO — screen capture  │    Todo tu negocio en      │
│   │     of the platform, muted, │    un solo lugar.          │
│   │     autoplay on entry,      │                            │
│   │     rounded 20px frame ]    │    Pipeline, portafolio,   │
│   │                             │    proyecciones, reporting │
│   └─────────────────────────────┘    y cumplimiento — con    │
│                                      la lógica de inversión  │
│   ─── 01 / PLATAFORMA ───            de Dproperty dentro.    │
│                                                              │
│                                      · Pipeline en tiempo real│
│                                      · Proyecciones validadas│
│                                      · Reporting a HQ        │
└──────────────────────────────────────────────────────────────┘
```

**The three showcases:**

| # | Product | ES headline | EN headline | Video content |
|---|---|---|---|---|
| 01 | **Plataforma BluePrint** | *Todo tu negocio en un solo lugar.* | *Your whole business in one place.* | Screen capture: dashboard → pipeline → a projection being built → reporting view. Smooth, real UI, no cursor jitter. |
| 02 | **CRM white-label** | *Tu marca. Nuestra maquinaria.* | *Your brand. Our machinery.* | The CRM rebranding itself — logo/colour swapping to a partner's identity, then a lead moving through pipeline stages, automation firing. |
| 03 | **La Academia** | *Tu equipo, formado desde la semana uno.* | *Your team, trained from week one.* | Course library → a lesson playing → a progress dashboard → certification. Show a real person learning, briefly. |

**Motion & specs:**
- Video frame **scales 0.94 → 1** with fade as it enters; sketch line draws a **bracket** around the frame.
- **Muted, loops, plays only in viewport, pauses on exit.** Never before visible.
- Silent by design — no audio anywhere on the site.
- Each ~12–20 seconds, seamless loop, no hard cut at the loop point.
- Encode H.264 + WebM, poster frame required, lazy-loaded. Target < 3MB each.
- Sections **alternate** video-left / video-right to keep rhythm.
- Section index (`01 / PLATAFORMA`) in JetBrains Mono, small, above or below the frame.
- Feature bullets reveal staggered after the video settles.
- Background alternates Bone → Bone Deep → Bone between the three.

---

## SECTION 7 — THE ROADMAP · *where this is going*

Explicitly requested. A **horizontal sketch timeline**, drawn as you scroll.

```
┌──────────────────────────────────────────────────────────────┐
│   EL RECORRIDO                                               │
│                                                              │
│   ●────────────●────────────●────────────●────────────○      │
│   2017         2026         2027         2028         2030+  │
│                                                              │
│   Nace         Fase 1       Primeras     Red en 3     Fase 2 │
│   Dproperty    El eco-      franquicias  mercados     El hub │
│                sistema      operando                  físico │
│                                                              │
│   [ each milestone expands on hover with 2-3 lines ]         │
└──────────────────────────────────────────────────────────────┘
```

**Milestones (ES / EN):**

| Year | ES | EN |
|---|---|---|
| **2017** | *Nace Dproperty* — una firma boutique especializada en inversión inmobiliaria en Panamá. | *Dproperty is founded* — a boutique firm specialized in real estate investment in Panama. |
| **2017–2025** | *Construyendo el método* — +$200M transaccionados, +700 operaciones, preventas convertidas en referentes. | *Building the method* — $200M+ transacted, 700+ operations, pre-sales that became landmarks. |
| **2026** | *Fase 1 — El ecosistema* — abrimos el método: franquicia, white-label y alianzas con desarrolladores. | *Phase 1 — The ecosystem* — we open the method: franchise, white-label, and developer partnerships. |
| **2027** | *Primera generación* — las primeras franquicias operando en Panamá, Bogotá y Medellín. | *First generation* — the first franchises operating in Panama, Bogotá and Medellín. |
| **2028** | *Red consolidada* — operaciones en múltiples mercados, Dproperty Select a escala regional. | *Network established* — operations across multiple markets, Dproperty Select at regional scale. |
| **2030+** | *Fase 2 — El hub* — la casa física del talento, el capital y las ideas de los bienes raíces en Latinoamérica e Iberia. | *Phase 2 — The hub* — the physical home of real estate talent, capital and ideas in LATAM and Iberia. |

**Motion:**
- Timeline **draws left to right** as the section enters, ~1.4s.
- Past milestones = **solid** charcoal nodes. Future = **hollow** champagne rings. The present (2026) = **filled champagne, gently pulsing**.
- Hover/tap a node → detail card rises beneath it; the node grows slightly.
- The 2030+ node sits at the very edge and the line **continues past it and fades out** — the story isn't finished. Deliberate.
- **Mobile:** vertical timeline, same drawing behaviour.

---

## SECTION 8 — THE PROOF · *economics, quietly*

```
┌──────────────────────────────────────────────────────────────┐
│   POR QUÉ FUNCIONA                                           │
│                                                              │
│   Cada operación de Dproperty Select es inventario           │
│   que no tuviste que conseguir, con una comisión que         │
│   no tuviste que negociar.                                   │
│                                                              │
│      ┌──────────────────┬──────────────────┐                 │
│      │  FRANQUICIA      │  WHITE-LABEL     │                 │
│      │  DPROPERTY       │                  │                 │
│      │                  │                  │                 │
│      │  Select   2.5%   │  Select   1.5%   │                 │
│      │  Por unidad      │  Por unidad      │                 │
│      │  de $300,000     │  de $300,000     │                 │
│      │     $7,500       │     $4,500       │                 │
│      └──────────────────┴──────────────────┘                 │
│                                                              │
│   La diferencia se recupera en ~7 operaciones Select.        │
└──────────────────────────────────────────────────────────────┘
```

**Copy (ES):** *Cada operación de Dproperty Select es inventario que no tuviste que conseguir, con una comisión que no tuviste que negociar.*
**(EN):** *Every Dproperty Select transaction is inventory you didn't have to source, at a commission you didn't have to negotiate.*

**Closing line (ES):** *La diferencia se recupera en ~7 operaciones Select.*
**(EN):** *The difference is recovered in ~7 Select transactions.*

- Numbers in **JetBrains Mono**, large, counting up on entry.
- The comparison draws as a **thin sketch table** — hairlines only, no fills, no heavy borders.
- The closing line in **Playfair italic**, champagne, given real space. It's the argument.
- **This section makes no claim we cannot defend.** It describes the mechanism (sourced inventory, pre-negotiated commission) and does the arithmetic — both verifiable. It deliberately avoids any "our partners increased profit by X%" statistic, because with zero franchisees there is no such figure, and an unsourced number here would be the first thing a sceptical buyer probes. Add a real case study later, when one exists.

---

## SECTION 9 — THE ECOSYSTEM · *the bigger idea*

```
┌──────────────────────────────────────────────────────────────┐
│   No estás comprando una marca.                              │
│   Estás entrando a un ecosistema.                            │
│                                                              │
│                      B_RealEstate                                │
│                          │                                   │
│         ┌────────────┬───┴───┬────────────┐                  │
│      DPROPERTY   WHITE-LABEL  DESARROL.  BluePrint           │
│      (insignia)  (marcas propias) (alianzas) (plataforma)    │
│                                                              │
│   Dproperty es nuestra marca insignia — la prueba de que     │
│   el modelo funciona, y una de las formas en que puedes      │
│   operar. No es quiénes somos; es lo que construimos.        │
│                                                              │
│                  ( Conocer la visión )                       │
└──────────────────────────────────────────────────────────────┘
```

- The house-of-brands diagram **draws itself** stroke by stroke, 1.4s, staggered.
- Boxes are label-only — no fills. Pure line drawing.
- **Critical framing rule:** the company is never presented as Dproperty. This section exists to make that unmistakable.

---

## SECTION 10 — CLOSE · *the invitation, again*

```
┌──────────────────────────────────────────────────────────────┐
│                            │                                 │
│                            │                                 │
│         Podrías ser parte de nuestra primera generación.     │
│                                                              │
│         ( Agendar una llamada )                              │
│                                                              │
│         Somos más amigos de la matemática                    │
│         que de la arquitectura.                              │
│                            │                                 │
│                            ○  ← the line ends in an open     │
│                                 circle, not a full stop      │
└──────────────────────────────────────────────────────────────┘
```

- **ES:** *Podrías ser parte de nuestra primera generación.* / **EN:** *You could be part of our founding generation.*
- Signature phrase in **Playfair italic**, always Spanish in both locales. In EN, a small Inter gloss beneath: *"We're better friends with math than with architecture."*
- The line terminates in a **small open circle** — an unclosed loop. The journey continues. Do not close it.

---

## FOOTER

Minimal. Bone Deep background.

- Left: `B_RealEstate` logo + tagline — *Un ecosistema de franquicias para el sector inmobiliario.* / *A real estate franchising ecosystem.*
- Columns: **Marcas** (Dproperty) · **Compañía** · **Contacto**
- Bottom row: `© B_RealEstate` · Privacidad · Términos · Aviso de inversión · `ES | EN`
- One thin sketch line across the top of the footer. No heavy divider.

---

# 8. INNER PAGES

Same system, same line, lighter structure. Each inner page's line **continues from** the homepage's (see Motion I).

| Page | Structure notes |
|---|---|
| **Franquicia Dproperty** | Hero → **the investment-brand manifesto block** (the "profitable and reliable, not pretty and livable" argument — give this real typographic weight, it's the brand's thesis) → who it's for → what's included → economics + the ~7-operations payback → territories map (sketched, not a real map) → FAQ accordion → CTA |
| **White-Label** | Must feel **exactly as premium** as the franchise page. Hero → "your focus, your rules" → "powered by Dproperty" endorsement block → what's included/not → **the honest comparison table** (bold the wins in *both* columns) → plans → CTA |
| **Desarrolladores** | Hero → the problem → the dedicated-team proposal → **the four differentiators** (continuity, understanding the product, protecting brand & numbers, partnership not agency) → what we do → levels → landmark projects → CTA |
| **Plataforma** | The most technical page. Deep Blue appears more here. Module grid, each with a short looping video or animated sketch. |
| **Nosotros** | Editorial. Long-form, generous whitespace. The 2017→today story as a vertical sketch timeline. Values as line-drawn icons. |
| **Contacto** | Split: calendar embed left, short form right. **Three self-selection routes** (franchise / white-label / developer) → three separate CRM pipelines. |

---

# 9. COMPONENT LIBRARY

Design these as reusable components:

1. **Button — primary** (champagne pill, magnetic hover)
2. **Button — secondary** (outline pill, fills on hover)
3. **Sketch line** (vertical / horizontal / branching / annotation tick)
4. **Path node** (hollow → filled champagne states)
5. **Card — route** (the three doors)
6. **Card — step** (journey stage)
7. **Video frame** (20px radius, sketch bracket, poster state)
8. **Stat annotation** (mono label on a line tick, count-up)
9. **Timeline node + detail card**
10. **Sketch table** (hairline comparison)
11. **Accordion** (FAQ — thin lines, champagne active state)
12. **Menu overlay**
13. **Section index label** (mono, `01 / NAME`)

---

# 10. RESPONSIVE

| Breakpoint | Behaviour |
|---|---|
| **Desktop ≥1440** | Full experience. Pinned horizontal journey. Line centred/asymmetric per section. |
| **Laptop 1024–1439** | Same; reduce H1 to 72px, tighten section padding. |
| **Tablet 768–1023** | Journey unpins → vertical timeline. Three cards → stacked. Line moves to left margin. |
| **Mobile <768** | Line runs left margin at 24px inset, thinner (1px). H1 40–48px. Videos full-width, 16px radius. All horizontal scroll becomes vertical. **No magnetic hover.** Reduce parallax by half. |

**Mobile is not a downgrade** — the line running down the left edge of a phone screen is arguably the purest expression of the concept. Design it with that intent.

---

# 11. TECHNICAL NOTES (for build)

- **Stack:** React + Tailwind. **GSAP + ScrollTrigger** for scroll-linked animation and pinning. **Lenis** for smooth scroll. Framer Motion acceptable for component-level transitions.
- **The line:** a single inline SVG per page with a computed path; animate `stroke-dashoffset` against ScrollTrigger progress. Champagne head = a gradient stop travelling along the path.
- **Performance is non-negotiable** — the site's speed *is* the product claim. Target Lighthouse ≥ 90. Lazy-load all video, `will-change` only on actively animating elements, `IntersectionObserver` to pause offscreen video, preload only the hero.
- **Bilingual:** full ES/EN, route-based (`/es`, `/en`), Spanish default. All strings in locale files. Full copy in [[LOVABLE - Ecosystem Website Build Brief]].
- **Accessibility:** WCAG AA. Full `prefers-reduced-motion` fallback. Keyboard-navigable menu. Video is decorative — must not carry information unavailable in text.
- **Names:** `B_RealEstate` (company) and `BluePrint` (platform) should still live as **config variables**, single source — trademark clearance is not yet complete, so keep them trivially swappable.
- **Remaining `[MOCK]`:** contact details only (office, email, phone, social). Everything else is resolved.

---

# 12. WHAT TO DELIVER

1. Full homepage design, desktop + mobile, all 10 sections.
2. The three product-showcase sections with video frame treatments.
3. Header + menu overlay, closed and open states.
4. The roadmap section.
5. The pinned horizontal journey (show 2–3 frames of the sequence).
6. At least two inner pages — **Franquicia Dproperty** and **White-Label** (they must feel equally premium).
7. Component library sheet.
8. Motion specification — what animates, when, how long, with what easing.

---

# 13. THE ONE-SENTENCE TEST

> When someone finishes scrolling this site, they should think: *"if their website is this good, their software probably is too — and these people clearly don't do anything carelessly."*

If a design decision doesn't serve that sentence, cut it.

## Product architecture acceptance — 2026-09-29 [D]

BlankCRM executes lead capture, legal workflow, commercial approvals, contracts, payment milestones, closing, commissions and post-sale, with communications, automation and commercial dashboards. BluePrint provides CRM-agnostic financial health, expected-vs-actual cash, expense/budget/variance control, KPI/CRM oversight, Glitches, policies, management audit and executive AI recommendations. Commercial execution screens belong in BlankCRM; BluePrint screens show evidence, verification and management intervention. BlankCRM must operate without BluePrint. A BluePrint management decision does not execute a sales action.

Spanish production copy: BlankCRM ejecuta todo el ciclo comercial: captación, calificación, gestión legal, aprobaciones, contratos, hitos de pago, cierre, comisiones y postventa; comunicaciones, automatización y tableros comerciales. Puede operar sin BluePrint. BluePrint es la capa de gestión interna, gobierno e inteligencia, independiente del CRM: salud financiera, caja esperada frente a real, gastos, presupuestos, desviaciones, KPI, supervisión del CRM, procesos y Glitches, auditoría, políticas y roles ejecutivos de IA. Observa, verifica y recomienda; no ejecuta ventas.
