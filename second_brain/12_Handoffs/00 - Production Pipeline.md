---
project: B_RealEstate
title: "Production Pipeline — Markdown to Presentable PDF"
type: process
status: Canonical v1.0
owner: Esteban
last_updated: 2026-09-24
tags: [handoff, production, pdf, workflow, tooling]
---

> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation]] · Index: [[00 - Handoff Index]]

# Production Pipeline — Markdown → Presentable PDF

**The rule that governs everything here:** the vault note is the source of truth. A PDF is a **derived artifact**. When a PDF and its source note disagree, the note wins and the PDF is regenerated — never patched.

## The flow

```
Obsidian note (canonical content)
   │
   ├─► Tier 1 · Obsidian native export ──────► internal / quick share
   │        + proposal-print.css snippet
   │
   ├─► Tier 2 · Claude artifact ─────────────► client-facing proposals  ★ default
   │        paste design prompt + content → HTML → print to PDF
   │
   └─► Tier 3 · ChatGPT / Canva ─────────────► decks and heavy design
            code interpreter → .pptx / .xlsx

   Final files → SharePoint or Drive
   Link back into Obsidian. Never store the binary in the vault.
```

## Tier 1 — Obsidian native export (zero setup)

**Use for:** internal review, advisor read-throughs, anything where speed beats polish.

1. Enable once: **Settings → Appearance → CSS snippets → toggle `proposal-print`**
   (snippet lives at `.obsidian/snippets/proposal-print.css`)
2. Open the note → **Ctrl+P** → *Export to PDF*
3. In the dialog, check **Include page numbers** off, and **do not** downscale.

The snippet applies the real brand system — Bone palette, Playfair/Inter/JetBrains Mono, framed callouts, mono truth-label chips, and it **hides YAML frontmatter** so vault metadata never reaches a reader.

**Limits, honestly:** Obsidian's exporter gives you limited control over page breaks and no multi-column layout. It produces a clean, credible document — not a designed one. Good enough for internal and partner review; **not** what you send a seed investor.

## Tier 2 — Claude artifact ★ recommended for proposals

**Use for:** the offer one-pagers, the ecosystem two-pager, anything client- or investor-facing.

**Why this is the default:** full layout control (two-column, real 9-block canvas grid), exact brand fidelity, genuine page-break control, and it is **repeatable** — one prompt reused across nine documents is what makes the set look like a system rather than nine separate attempts.

Template: **[[CLAUDE DESIGN - Offer One-Pager Template]]**

1. New chat at claude.ai.
2. Paste the prompt block from that template.
3. Replace `{{OFFER_CONTENT}}` with the offer's one-pager markdown.
4. Claude returns an HTML artifact → review → **Print → Save as PDF**.
5. **Enable "Background graphics" in the print dialog.** Without it the bone palette prints white and the whole design collapses. This is the single most common failure.
6. Paper **Letter** (Panama/LatAM standard). Swap to A4 for European recipients.

**Reuse the prompt unchanged** between offers. Editing it per document is how a set drifts out of visual consistency.

## Tier 3 — ChatGPT and Canva

| Need | Tool | Note |
|---|---|---|
| **Slide deck** | ChatGPT (code interpreter) → `python-pptx` | Ask for a `.pptx` with the Bone palette and Playfair/Inter. Gives an editable file, not a flat export. |
| **Financial model** | ChatGPT → `openpyxl` | Feed it `06_Finance/` content. Verify every formula — do not trust generated arithmetic. |
| **Heavy visual design** | Canva | Best when you want art direction beyond a document — covers, brochures, social. Manual, not repeatable. |
| **Batch PDF from markdown** | ChatGPT → `weasyprint` / `pandoc` | Useful if you ever need all nine generated at once from a zip. |

**ChatGPT caveat:** it can produce real binary files, which Claude artifacts cannot. That is its genuine advantage for `.pptx` and `.xlsx`. For *documents*, Claude's artifact gives better design control.

## Choosing quickly

| Situation | Tier |
|---|---|
| "Send me what you have" — internal, advisor | **1** — Obsidian export |
| Investor one-pager, franchise proposal, partner pack | **2** — Claude artifact |
| Pitch deck to present live | **3** — ChatGPT `.pptx`, then polish in Canva |
| Financial model to hand to a CFO | **3** — ChatGPT `.xlsx` from `06_Finance/` |
| Brochure, cover, anything art-directed | **3** — Canva |

## Non-negotiables before anything leaves the building

Run this against every generated PDF:

- [ ] Every number matches `06_Finance/Pricing Unit Economics and Revenue Policy.md`
- [ ] Truth labels survived: `[F]` `[D]` `[M]` `[A]` `[T]` `[R]`
- [ ] **No retired figures:** $299/$599/$999 · $650k · $1.5M · $500 blended ARPA · 600k TAM / 100k SAM · "5 franchises / 20 white-label / 15 developers" as company SOM · $1.59M–$1.89M Y5 as company forecast
- [ ] **No legacy names:** Dproperty OS · Plano · La Plataforma · Academy · B_Academy · White-Label · Private Collection · Developer Sales OS · DpropertyLiving
- [ ] **No forbidden claims:** "one shared database" · "CRM propio" · proprietary CRM
- [ ] Disclaimer footer present: assumptions labelled, not an offer or investment solicitation
- [ ] YAML frontmatter is **not** visible
- [ ] Filename convention: `B_RealEstate - <Deliverable> - <Version> - YYYY-MM-DD.pdf`

`.tools/verify_vault.py` catches retired vocabulary and legacy names **in the vault**. It cannot see a PDF. This checklist is the manual equivalent — run it.

## Where the files live

| Artifact | Home | Why |
|---|---|---|
| Source markdown | Obsidian, in the offer folder | Canonical |
| Design prompt | `12_Handoffs/` | Reusable, version-controlled |
| Print CSS | `.obsidian/snippets/` | Travels with the vault |
| **Final PDF** | **SharePoint / Drive** | Heavy/final assets never live in the vault |
| Link to final PDF | Back in the offer folder | So the vault stays the index |

## Source & change log

- **2026-09-24** created. Established Tier 2 (Claude artifact) as the default for client-facing proposals; wrote `proposal-print.css` for Tier 1; recorded the print-dialog "background graphics" failure mode.
