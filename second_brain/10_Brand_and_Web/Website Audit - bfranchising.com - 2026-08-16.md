---
project: B_RealEstate
title: "Website Audit - bfranchising.com - 2026-08-16"
type: website_audit
status: Completed
owner: Esteban
last_updated: 2026-09-29
source: Live browser inspection of https://bfranchising.com
tags: [ecosystem, website, audit]
---

> [!WARNING] Superseded — historical evidence only (reviewed 2026-09-23)
> This audit remains useful **evidence** about the live site's problems, but the strategy has moved twice since. The site needs a **product-led rewrite** around BluePrint / BlankCRM / VAULTED, with Dproperty Franchise, B_ Partner and Developer Partnerships as adoption channels. DpropertyLiving is parked and the physical hub is not a near-term headline.
>
> Its P0 corrections **still stand**: name the product BluePrint · disclose that BlankCRM is powered by GoHighLevel · remove “one database” language · reconcile all economics · remove DpropertyLiving · correct Dproperty Select governance · verify lead capture.
>
> **Current instead:** [[Web Presence and Funnel Architecture]] · [[../01_Canon/00 - Precedence and Canonical Reconciliation]]

# Website Audit — bfranchising.com — 2026-08-16

## Executive verdict

The site is live, coherent, visually distinctive and much closer to the B_RealEstate strategy than the older Cantera handoff. Its strongest elements are the editorial identity, clear three-model routing, ecosystem narrative, unique metadata and concrete operating language.

It is not yet safe to treat as the commercial source of truth. Product boundaries, naming, economics and several public claims conflict with the repository or describe capabilities more strongly than the current architecture supports.

## Pages inspected

`/` · `/ecosistema` · `/plataforma` · `/franquicia` · `/white-label` · `/desarrolladores` · `/franquicias` · `/nosotros` · `/contacto`

## What works

- Strong Spanish-first boutique/editorial identity.
- Clear route to Dproperty franchise, white-label and developer models.
- Consistent page-specific titles, descriptions and canonical URLs.
- Correct HTML language and useful image alt text in most places.
- Dproperty proof is central and the ecosystem is described as more than software.
- VAULTED and the Academy are already visible in the customer narrative.
- Demo numbers on `/plataforma` are labeled as demonstration data.
- Contact CTAs are present across pages.

## P0 — Correct before actively driving paid or high-stakes traffic

### 1. Rename the product

Replace “La Plataforma” as the product name with **BluePrint**. First-use copy: “BluePrint, la plataforma de back office de B_RealEstate.” Apply to navigation, headings, metadata, ecosystem diagrams and previews.

### 2. Correct the CRM claim

`/ecosistema` calls it “CRM propio” and `/plataforma` describes CRM pipeline functions as part of one platform/database. The canonical architecture uses white-labeled GoHighLevel. Replace with transparent wording and show the handoff: BlankCRM executes the full commercial lifecycle; BluePrint observes, verifies and governs company management.

### 3. Remove “one database” language

The site says the five pieces share one database. The target architecture is a connected ecosystem with several governed systems of record. Replace with “una identidad, una operación conectada y fuentes de verdad definidas.”

### 4. Reconcile all economics

The live branded, white-label and developer figures conflict with the Decision Log and financial model. Do not leave competing numbers online. See [[../01_Canon/09 - Unit Economics Registry]].

### 5. Resolve DpropertyLiving

The site introduces DpropertyLiving as both a brand side and a fourth entry route, while the canonical model has three commercial doors and an investment-only Dproperty. Either approve and document it or remove it from the ecosystem/entry model until defined. See [[../98_Archive/Parked/DpropertyLiving - Parked]].

### 6. Correct Dproperty Select governance

The site states that franchises curate/propose the portfolio and implies broad network availability. Canonical rule: HQ controls curation, materials, assumptions and terms; partners may submit candidates but cannot approve or modify them.

### 7. Verify lead capture

The inspected forms use same-page GET form actions, and booking routes to Cal.com rather than an evident GHL calendar. Verify actual submission persistence. All forms must create/update the appropriate GoHighLevel pipeline with attribution and consent.

## P1 — Improve positioning and trust

- Attribute +$200M and +700 operations explicitly to Dproperty wherever used above the fold.
- Replace unsupported payback ranges and the $235k “build it alone” total with sourced assumptions or remove them.
- Avoid stating that inventory, commission and availability are live/in real time until the integrations support that claim.
- The roadmap names 2027/2028 country expansion as dated outcomes. Reframe as directional targets unless formally approved and resourced.
- Clarify developer economics: total commission pool versus B_RealEstate retained fee.
- Replace “sin hojas de cálculo” with a more credible statement about reducing fragmented spreadsheets.
- Add Legal links/pages for privacy, terms, cookies and investment/franchise disclaimers.

## P2 — UX, accessibility and conversion

- `/franquicia` and `/franquicias` are easily confused. Rename the latter to `/modelos` or `/sistema` and redirect.
- The home page uses a very long pinned seven-step scroll journey; browser inspection showed roughly 6,000px where the same journey headings remain in view. Shorten it or provide direct navigation for users who do not want the full animation.
- Full-page capture initially showed large visually empty areas because scroll-triggered content had not activated. Ensure content remains visible with JavaScript failure, reduced-motion preference and automated rendering.
- Verify that visible input labels are programmatically associated with fields; inspected form elements did not expose label/ARIA relationships.
- Add an obvious Login/Portal path in global navigation once BluePrint authentication exists.
- Align the footer email domain and website domain explanation to avoid trust friction.

## Recommended corrected ecosystem sentence

“BluePrint coordina el back office; GoHighLevel gestiona la demanda y las conversaciones; Building Blocks forma al equipo; Dproperty Select gobierna el inventario curado; y VAULTED abre el mercado off-market por invitación. Conectados, con una fuente de verdad definida para cada dato.”

## Release gate

Do not redesign the visual system. Preserve it. Prioritize factual architecture, economics, forms/integrations, legal pages and conversion clarity before aesthetic changes.

