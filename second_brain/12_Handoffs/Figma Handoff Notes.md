---
project: B_RealEstate
title: "Figma Handoff Notes"
type: product_note
status: Baseline Created
owner: Esteban
last_updated: 2026-09-29
source: ChatGPT baseline vault package
tags: [product]
---

> [!NOTE] Verified against canon 2026-09-23
> Design notes remain useful. Screen inventory includes **CRM Oversight and Evidence**; deal execution screens belong in BlankCRM.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# Figma Handoff Notes

> **⚠ Design system update (2026-08-26):** The BluePrint application's visual system is now **fixed and specified**, inherited from the live `bfranchising.com` stylesheet. Do not invent colors, type or components in Figma. Use [[../02_Offers/01_BluePrint/20 - Wireframe - Back Office OS]] §3 as the source: bone `#FAF8F3` · offwhite `#F7F4ED` · sand `#EFEAE0` · ink `#1A1A1A` · warm `#55514C` · champagne `#B89B5E` · destructive `#A13B2A`, plus the desaturated semantic status palette; Playfair Display (display) / Inter (UI) / JetBrains Mono (labels, data); radius 16px cards, 8px controls; flat surfaces, no drop shadows.
>
> Two constraints that are easy to get wrong: **champagne fails WCAG AA on light backgrounds (2.5:1)** and may never be used for small text; and the marketing site's generous spacing must be **compressed to application density** (44px table rows, 24–32px section padding) or the app becomes unusable for daily back-office work.
>
> Screens to prototype are the Release 1 set in the Wireframe, not the older screen list below.

> **Naming and scope update (2026-08-16):** The platform is **BluePrint**, part of **B_RealEstate**. GoHighLevel remains the CRM, Open edX the Building Blocks technology, and VAULTED the off-market marketplace. The canonical boundaries live in [[../01_Canon/01 - Ecosystem Master Map]] and [[../01_Canon/07 - System of Record and Integration Matrix]].

## Goal

Translate the product specs into a clickable Figma prototype.

## First Screens

1. Login / workspace selector.
2. HQ Dashboard.
3. Franchise Dashboard.
4. Client List.
5. Client Profile.
6. Project List.
7. Project Profile.
8. Deal Pipeline.
9. Deal Detail.
10. Private Collection Request.
11. Projection Generator.
12. Commission Liability Oversight (read-only source calculations; no approval or payout).
13. Training Dashboard.

## Design Principles

- Clean, premium, quiet.
- Not too many colors.
- Strong hierarchy.
- Simple tables.
- Clear status pills.
- Good mobile/tablet readability.
- Real estate visuals should be curated, not cluttered.

## Claude/Figma Prompt Use

Use Claude for long UX copy and Figma prompt drafting. Use ChatGPT for product logic and data model.

## 2026-07-18 Update — Platform Architecture & Priority Screens

Full platform architecture is now in [[../02_Offers/01_BluePrint/22 - Platform Information Architecture]]. Before the OS screens above, the wireframe also needs the **public site** (Home, About, Services, Become-a-Franchise hub) and two **always-on top-bar elements** (Command Bar + Report a Glitch) present on every OS screen.

**Recommended first wireframe set (priority, not all at once):**
1. Public Home (dual CTA: client vs franchise)
2. "Become a Franchise" hub page
3. Login / workspace selector
4. Franchise Workspace Home (with Command Bar + Glitch button)
5. Deal Detail
6. Resource Library
7. Glitch Report + Glitch Feed

Then extend to the remaining OS modules and back-office systems. See [[../02_Offers/01_BluePrint/23 - Platform Scenario Playbook]] for the flows each screen must support and [[../09_Data_and_AI/Roles and Access Matrix]] for what each role sees.

## Product architecture acceptance — 2026-09-29 [D]

BlankCRM executes lead capture, legal workflow, commercial approvals, contracts, payment milestones, closing, commissions and post-sale, with communications, automation and commercial dashboards. BluePrint provides CRM-agnostic financial health, expected-vs-actual cash, expense/budget/variance control, KPI/CRM oversight, Glitches, policies, management audit and executive AI recommendations. Commercial execution screens belong in BlankCRM; BluePrint screens show evidence, verification and management intervention. BlankCRM must operate without BluePrint. A BluePrint management decision does not execute a sales action.

Spanish production copy: BlankCRM ejecuta todo el ciclo comercial: captación, calificación, gestión legal, aprobaciones, contratos, hitos de pago, cierre, comisiones y postventa; comunicaciones, automatización y tableros comerciales. Puede operar sin BluePrint. BluePrint es la capa de gestión interna, gobierno e inteligencia, independiente del CRM: salud financiera, caja esperada frente a real, gastos, presupuestos, desviaciones, KPI, supervisión del CRM, procesos y Glitches, auditoría, políticas y roles ejecutivos de IA. Observa, verifica y recomienda; no ejecuta ventas.
