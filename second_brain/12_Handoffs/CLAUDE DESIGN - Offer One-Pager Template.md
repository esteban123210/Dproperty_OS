---
project: B_RealEstate
title: "CLAUDE DESIGN — Offer One-Pager Template"
type: design_prompt
status: Ready to use
owner: Esteban
last_updated: 2026-09-24
tags: [handoff, design, pdf, one-pager, proposal]
---

> Pipeline: [[00 - Production Pipeline]] · Brand source: [[CLAUDE DESIGN - Ecosystem Website Design Prompt]]

# CLAUDE DESIGN — Offer One-Pager Template

**What this produces:** a two-page branded document — page 1 executive summary + economics, page 2 full business model canvas — as a self-contained HTML artifact you print to PDF.

**How to use it:**
1. Open a new chat at claude.ai.
2. Paste **everything in the prompt block below**.
3. Replace `{{OFFER_CONTENT}}` with the full markdown of that offer's `08 - One-Pager Exec Summary.md`.
4. Claude returns an HTML artifact. Check it renders correctly.
5. **Print → Save as PDF.** In the print dialog: paper **Letter**, margins **Default**, **enable "Background graphics"** (critical — without it the bone palette prints white).
6. Save the PDF to Drive. Link it back in the offer folder.

Repeat per offer with the same prompt. Consistency across all nine documents comes from reusing this prompt unchanged.

---

## THE PROMPT — paste from here

````text
You are producing a print-ready, two-page business proposal document as a single
self-contained HTML artifact. It must look like it came from a boutique firm, not
a template. Output ONE HTML file with all CSS inline in a <style> block. No frameworks,
no external JS, no images.

## BRAND SYSTEM — follow exactly

Palette (every background stays light — never a dark section, never inverted):
  Bone          #F7F4ED   page background
  Bone Deep     #EFEAE0   table headers, canvas cells
  Bone Warm     #FAF8F3   elevated surfaces, alternating rows
  Charcoal      #1A1A1A   primary text, rules
  Charcoal Soft #55514C   secondary text, labels
  Champagne     #B89B5E   accent — CTAs, key figures, left rules. SEASONING ONLY (<5% of page)
  Deep Blue     #1F4E79   technical/data moments only, sparingly
  Rule          rgba(26,26,26,0.25)

Typography — load from Google Fonts:
  Headlines  'Playfair Display', weights 400/500 only. Never 700+.
             Tight line-height 1.05–1.15, letter-spacing -0.02em. Editorial, not decorative.
  Body       'Inter', 400/500. 9.5pt, line-height 1.5. Max ~62 characters per line.
  Technical  'JetBrains Mono', 12px→7.5pt, UPPERCASE, letter-spacing +0.08em.
             Use for: metric labels, section numbers, truth labels, table headers.
             This is the strongest "techy" signal precisely because it is RARE.

Three voices, clearly separated by role. Never mix within one element.
Shadows: almost none. If needed: 0 2px 24px rgba(26,26,26,0.04).

## PAGE SETUP

@page { size: letter; margin: 14mm 15mm; }
Two pages exactly. Force the break with `page-break-before: always` on the canvas section.
Use `page-break-inside: avoid` on every table and canvas cell.
Design for print first — the screen view is a preview, not the deliverable.

## PAGE 1 LAYOUT — executive summary

1. HEADER
   - Small mono eyebrow, uppercase: the offer type (e.g. "PRODUCT — PROPRIETARY CORE")
   - Playfair H1: the offer name. Large, ~26pt.
   - One-line positioning statement beneath in Inter, Charcoal Soft, ~11pt italic-free.
   - Thin charcoal rule beneath the whole header block.
   - Top-right, mono, small: "B_RealEstate" and the document date.

2. TWO-COLUMN BODY (about 62/38 split)
   LEFT column:
     - "THE IDEA" — 2–3 short paragraphs, plain English, no jargon.
     - "THE PROBLEM" — 1 paragraph or 3 tight bullets.
     - "WHAT IT OWNS / WHAT IT DOES NOT" — two compact stacked lists.
       Render "does not own" in Charcoal Soft so the boundary reads as discipline, not weakness.
   RIGHT column (a Bone Warm panel with a 2.5pt Champagne left rule):
     - "AT A GLANCE" in mono
     - Definition list: Type · Job · Price · Status · Next gate
     - Then 3–4 KEY FIGURES, each as: big Playfair number + small mono label beneath.
       These are the numbers a reader remembers. Champagne for the numerals.

3. ECONOMICS — full width
   - Section header: mono number "01" + Playfair "Economics"
   - A clean table. Right-align all numeric columns.
   - IMPORTANT: if the content contains BOTH a buyer/operator view and a
     B_RealEstate/HQ view, render them as TWO side-by-side tables with clear
     captions ("For the operator" / "For B_RealEstate"). Do not merge them.
   - Beneath the table, a single-line note in Charcoal Soft for caveats.

4. TRUTH LABELS — render inline wherever they appear in the source:
   [F] Fact · [D] Decision · [M] Model · [A] Assumption · [T] Target · [R] Required evidence
   Style as a small mono chip: Bone Deep background, Deep Blue text, 1pt radius.
   These must survive into the PDF — they are the credibility mechanism, not clutter.

5. FOOTER on page 1
   Thin rule, then mono microtype: "Figures marked [A] are unvalidated assumptions.
   [M] denotes model output. Not an offer or investment solicitation." Plus page number.

## PAGE 2 LAYOUT — business model canvas

- Playfair H2: "Business Model Canvas", mono eyebrow "02".
- A real canvas GRID, not a list. Use CSS grid in the classic 9-block arrangement:

    ┌───────────┬───────────┬───────────┬───────────┬───────────┐
    │ Key       │ Key       │  VALUE    │ Customer  │ Customer  │
    │ Partners  │ Activities│  PROP     │ Relations │ Segments  │
    │           ├───────────┤  (center, ├───────────┤           │
    │           │ Key       │  spans 2  │ Channels  │           │
    │           │ Resources │  rows)    │           │           │
    ├───────────┴───────────┼───────────┴───────────┴───────────┤
    │   Cost Structure      │        Revenue Streams            │
    └───────────────────────┴───────────────────────────────────┘

- Each cell: Bone Deep background, 0.5pt Rule border, mono uppercase label at top,
  Inter body beneath at 8pt. Tight but readable.
- Value Proposition cell: Bone Warm + 2.5pt Champagne left rule so it reads as the centre.
- Content must be SHORT per cell — 3–5 bullets or one tight sentence. Do not overflow.
- Footer: same microtype rule as page 1, page number "2 / 2".

## HARD RULES

- No dark sections. No inverted footer. No coloured banners.
- Champagne under 5% of each page. If it feels decorative, remove it.
- No logos, no placeholder image boxes, no icon fonts, no emoji.
- Do not invent numbers, dates or claims. Use ONLY what is in the content below.
- If a figure is missing, write "not yet modelled" in Charcoal Soft rather than guessing.
- Preserve every truth label exactly as written in the source.
- Keep it to exactly two pages. If content overflows, tighten leading and font size
  slightly before cutting substance — but never drop a caveat or a truth label.

## THE CONTENT

{{OFFER_CONTENT}}
````

## Print settings that matter

| Setting | Value | Why |
|---|---|---|
| Paper | **Letter** | Panama/LatAM standard. Swap `size: letter` → `A4` for European recipients. |
| Margins | Default | The `@page` rule already sets them |
| **Background graphics** | **ON** | Without this the bone palette prints as white and the design collapses |
| Headers/footers | OFF | The template provides its own |
| Scale | 100% | Do not "fit to page" |

## QA checklist before sending

- [ ] Exactly two pages — nothing orphaned onto a third
- [ ] Bone background actually printed (background graphics was on)
- [ ] All truth labels `[A]` `[M]` `[R]` survived into the PDF
- [ ] Every number matches `06_Finance/Pricing Unit Economics and Revenue Policy.md`
- [ ] No retired figures: $299/$599/$999 · $650k · $1.5M · $500 ARPA · 600k TAM
- [ ] No legacy names: Dproperty OS · Academy · White-Label · Private Collection · Developer Sales OS
- [ ] Canvas cells all fit without clipping
- [ ] Disclaimer footer present on both pages
- [ ] Filename: `B_RealEstate - <Offer> - One-Pager - 2026-09-24.pdf`

## Source & change log

- **2026-09-24** created. Brand system lifted from the Ecosystem Website Design Prompt so print and web stay visually consistent.

Precedence: [[00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]].
