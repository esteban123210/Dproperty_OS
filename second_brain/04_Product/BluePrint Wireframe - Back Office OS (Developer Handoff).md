---
project: B_RealEstate
title: "BluePrint Wireframe — Back Office OS (Developer Handoff)"
type: product_spec
status: "Canonical v1.0 — Release 1 build spec"
version: 1.0
owner: Esteban
created: 2026-08-26
last_updated: 2026-08-26
source: "Founder scope redirection 2026-08-26 + Board of Advisors session + bfranchising.com design-token extraction"
tags: [blueprint, product, wireframe, developer-handoff, design-system, backoffice, glitch-report, mvp]
---

# BluePrint Wireframe — Back Office OS (Developer Handoff)

> **This document is self-contained and buildable.** Hand it to a developer or a code-generation tool as-is. It contains the product scope, access model, complete design system with real token values, screen-by-screen wireframes, the two reusable primitives that generate most of the app, the permission matrix, build order and acceptance criteria.
>
> **Controlling documents:** [[BluePrint Product Constitution]] §2 (boundary), §4 (ownership), §9 (release boundary), §10 (service recovery), §13 (shell) · [[BluePrint Product Map]]. Where this file and the Constitution disagree, the Constitution wins and this file is regenerated.
>
> **Release scope:** This is **Release 1 — the Back Office Brain**. The transaction/compliance/document/commission spine is **Release 2** and is specified separately in [[BluePrint Golden Workflow - Wireframe and Validation]]. Do not build Release 2 screens from this document.

---

## 1. What BluePrint is (and is not)

**BluePrint is the operating brain of a lean real-estate back office.**

A boutique agency runs on 3–8 administrative people. Their institutional knowledge — which licenses expire when, where the contract templates live, who the accountant is, what went wrong for a client last Tuesday, how the team is performing — currently lives in spreadsheets, WhatsApp threads, someone's inbox, and someone's memory. BluePrint is where all of it lives instead.

### The two-tool split (this is the core product decision)

```
SALES TEAM          →  GoHighLevel (CRM)      →  in the street, on a phone
BACK OFFICE         →  BluePrint              →  at a desk, running the company
```

Salespeople do **not** get BluePrint accounts. We want them with clients, not behind software. Whatever the back office needs *from* the CRM (campaign performance, pipeline metrics, conversion) flows **into** BluePrint as metrics. Nothing is duplicated.

### Hard boundaries — never build these

| Do NOT build | Because it belongs to |
|---|---|
| Lead pipelines, contacts-as-CRM, campaigns, messaging, nurture, call logs | **GoHighLevel** |
| Course content, lessons, video player, quizzes, enrollment | **B_Academy (Open edX)** — BluePrint links out only |
| Off-market listing browsing and negotiation | **VAULTED** |
| Binary file storage / document warehouse | **Drive / SharePoint** — BluePrint stores links + metadata |
| Signed-document archive | **Secure legal archive** — BluePrint tracks *status and expiry*, not the signed PDF |
| Accounting ledger, invoicing, payroll processing | **Accounting provider** |
| Transaction workspace, compliance gates, commission engine | **BluePrint Release 2** — not this release |

If a screen in this document appears to duplicate one of the above, it is a link-out or a metric, never a rebuild.

---

## 2. Who uses it — access tiers

BluePrint is **administrative-staff-only**. Four tiers:

| Tier | Who | Broad access |
|---|---|---|
| **T4 — HQ / Network Admin** | HQ operations, franchise oversight | All tenants, cross-office glitch and performance patterns, template governance, tenant provisioning |
| **T3 — Principal / C-Suite** | Office owner, director | Everything in own tenant, including confidential HR and full financial visibility |
| **T2 — Manager** | Operations manager, sales manager, office manager | Own tenant operations, team KPIs for their team, glitch review, tasks, registries. **Not** confidential HR cases about themselves or their peers |
| **T1 — Coordinator / Secretary** | Admin coordinator, receptionist, assistant | Day-to-day: glitch logging, tasks, registries, library, directory, own personal KPIs. No team-wide financials, no HR case detail |

**Not a tier:** Sales Advisor. They live in the CRM. A sales advisor may appear *as a record* inside BluePrint (in People, in KPIs) without ever having a login.

**Confidentiality is a property of the record, not the module.** An HR complaint about a Principal must be invisible to that Principal. Build record-level visibility once, reuse everywhere. See §9.

---

## 3. Design system

Extracted directly from the live `bfranchising.com` stylesheet on 2026-08-26. These are the real production values, not an approximation.

### 3.1 Color tokens

```css
/* Foundation — warm editorial neutrals, NOT cool grays */
--bone:        #FAF8F3;  /* app background */
--offwhite:    #F7F4ED;  /* card / panel surface */
--sand:        #EFEAE0;  /* muted fill, table header, hover, inactive */
--ink:         #1A1A1A;  /* primary text, primary button fill */
--warm:        #55514C;  /* secondary text, labels, meta */
--champagne:   #B89B5E;  /* accent, focus ring, active indicator */
--rule:        rgba(26, 26, 26, 0.12);  /* all borders and dividers */
--destructive: #A13B2A;  /* critical / overdue / error */
```

**Semantic status colors — extend the palette (the marketing site has no status system).** These are desaturated to sit inside the editorial palette. Do not substitute default Tailwind green/amber/red; they will look cheap against bone.

```css
--status-good:     #5F7052;  /* resolved, on-track, valid, current */
--status-warn:     #B8823E;  /* due soon, attention, expiring < 60d */
--status-critical: #A13B2A;  /* overdue, expired, unrecovered glitch */
--status-info:     #4A5A6B;  /* in progress, informational, neutral state */
--status-neutral:  #55514C;  /* closed, archived, no action */
```

### 3.2 Accessibility — verified contrast ratios on `--bone`

Computed, not estimated. **Respect these or the app fails accessibility review.**

| Foreground | Ratio on bone | Verdict |
|---|---|---|
| `--ink` #1A1A1A | **16.4 : 1** | Passes AAA. Use for all primary text |
| `--warm` #55514C | **7.4 : 1** | Passes AAA. Use for all secondary text |
| `--destructive` #A13B2A | **6.2 : 1** | Passes AA. Safe for text |
| `--champagne` #B89B5E | **2.5 : 1** | **FAILS AA.** |

> ⚠️ **Champagne rule:** never use `--champagne` for body text, labels, or small text on a light background. It is permitted only for: focus rings, active-state indicators, 1–2px rules and underlines, icon strokes, decorative numerals ≥ 32px, and as a *background* with `--bone` text on top. This is the single most likely accessibility defect in this build.

### 3.3 Typography

Three families, loaded from Google Fonts. Each has one job — do not mix them up.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..700;1,400..600&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@400;500&display=swap"/>
```

| Family | Weights | Used for |
|---|---|---|
| **Playfair Display** (serif) | 400–700 + italic | Page titles, screen headings, large KPI numerals, empty-state headlines. The "boutique" signal |
| **Inter** (sans) | 300 / 400 / 500 | All body copy, UI labels, buttons, form fields, table cells, navigation |
| **JetBrains Mono** (mono) | 400 / 500 | Eyebrows, section numbers, dates, IDs, reference codes, tabular data, status chips, expiry countdowns |

**Signature editorial pattern — reuse everywhere.** The bfranchising numbered-section device is the brand's strongest visual asset. Carry it into the app:

```
┌────────────────────────────────────────────────────┐
│  01 — REVISIÓN DIARIA        ← JetBrains Mono, 12px,│
│                                 uppercase,           │
│                                 letter-spacing .1em, │
│                                 color: --warm        │
│                                                     │
│  Glitches de ayer            ← Playfair Display,     │
│                                 32px, weight 400,    │
│                                 letter-spacing -.025em│
│                                 color: --ink         │
└────────────────────────────────────────────────────┘
```

Type scale (rem):

| Token | Size | Line height | Typical use |
|---|---|---|---|
| `xs` | 0.75 | 1.0 | Mono eyebrows, chips, table meta |
| `sm` | 0.875 | 1.43 | Table cells, secondary text, form help |
| `base` | 1.0 | 1.5 | Body copy, inputs |
| `lg` | 1.125 | 1.56 | Lead paragraph, card titles |
| `xl` | 1.25 | 1.4 | Sub-headings |
| `2xl` | 1.5 | 1.3 | Card headings (Playfair) |
| `3xl` | 1.875 | 1.25 | Section headings (Playfair) |
| `4xl` | 2.25 | 1.11 | Page titles, hero KPI numerals (Playfair) |

Letter-spacing: `--tracking-tight: -0.025em` on all Playfair headings · `--tracking-widest: 0.1em` on all uppercase mono eyebrows.

### 3.4 Spacing, radius, layout

```css
--spacing: 0.25rem;    /* 4px base unit — all spacing is a multiple */
--radius-card: 1rem;      /* 16px — cards, panels, modals */
--radius-control: 0.5rem; /* 8px — buttons, inputs, chips */
--radius-full: 9999px;    /* avatars, status dots */
```

> **Density adaptation — important.** bfranchising.com is a *marketing* site: enormous whitespace, one idea per screen. This is an application used eight hours a day with dense tables. **Keep the palette and typography exactly; compress the spacing.** Marketing section padding of 96–128px becomes 24–32px in-app. Table rows are 44px, not 80px. Preserve the luxury *feel* through type, color and restraint — not through empty space. Getting this wrong produces a beautiful app that requires ten scrolls to read twelve rows.

Layout shell:

```
┌──────────────────────────────────────────────────────────────────────┐
│  TOP BAR  (h: 56px, bg --bone, border-bottom --rule)                 │
├────────────┬─────────────────────────────────────────────────────────┤
│            │                                                          │
│  SIDEBAR   │   CONTENT                                                │
│  240px     │   max-width 72rem, centered, padding 32px               │
│  bg --bone │   bg --bone                                              │
│  border-   │                                                          │
│  right     │                                                          │
│  --rule    │                                                          │
│            │                                                          │
└────────────┴─────────────────────────────────────────────────────────┘
```

Responsive: sidebar collapses to icon rail < 1024px, to a bottom sheet < 768px. The app is desktop-first (back office at a desk) but must be usable on tablet.

### 3.5 Core components

**Button — primary**
`bg: --ink` · `text: --bone` · `radius: 8px` · `padding: 10px 20px` · `font: Inter 500, 14px` · hover `bg: #000` · focus `ring: 2px --champagne, offset 2px`

**Button — secondary**
`bg: transparent` · `border: 1px --rule` · `text: --ink` · hover `bg: --sand`

**Button — ghost**
`bg: transparent` · `text: --warm` · hover `text: --ink`

**Card**
`bg: --offwhite` · `border: 1px --rule` · `radius: 16px` · `padding: 24px` · no drop shadow (flat editorial — shadows break the aesthetic)

**Input**
`bg: --bone` · `border: 1px --rule` · `radius: 8px` · `padding: 10px 14px` · `font: Inter 400, 14px` · focus `border: --champagne` + `ring: 2px champagne@30%`

**Status chip**
`font: JetBrains Mono 500, 11px, uppercase, tracking .08em` · `padding: 4px 10px` · `radius: 9999px` · background = status color @ 12% · text = status color at full (verify contrast; darken text token if needed)

**Table**
Header: `bg: --sand`, mono 11px uppercase, `--warm`. Rows: 44px, `border-bottom: 1px --rule`, hover `bg: --offwhite`. Numeric columns right-aligned in JetBrains Mono.

**Data / KPI tile**
Value in Playfair Display 36px `--ink`. Label above in mono 11px uppercase `--warm`. Delta below in mono 12px, colored by `--status-good` / `--status-critical`. No chart junk, no gradient, no shadow.

---

## 4. Global shell

Present on **every** screen.

```
┌──────────────────────────────────────────────────────────────────────────┐
│ B_luePrint    [ ⌘K  Buscar o escribir un comando…        ]  ⚡Glitch  ◐ EM │
└──────────────────────────────────────────────────────────────────────────┘
```

1. **Wordmark** — `B_` + underlined `luePrint`, Playfair Display. Links to Today.
2. **Command Bar (⌘K / Ctrl+K)** — universal search + command palette. The "three clicks to anything" principle. Searches across every registry, ticket, task, template, contact, manual and person. Typing a verb (`nuevo glitch`, `añadir contacto`) offers the action directly.
3. **Report a Glitch (⚡)** — persistent, one click, from any screen. Pre-captures page, module, role, tenant, timestamp. **Never removed from any screen.**
4. **Copilot (◐)** — opens the right-hand assistant panel with the current record as context.
5. **Account menu** — profile, tenant switch (T4 only), language (ES/EN), sign out.

Sidebar navigation:

```
┌──────────────────┐
│ 01  Hoy          │  ← Today
│ 02  Glitches     │
│ 03  Tareas       │
│ 04  Desempeño    │  ← Performance
│ 05  Equipo       │  ← People / HR
│ 06  Legal        │  ← Legal & Assets
│ 07  Biblioteca   │  ← Library
│ 08  Directorio   │  ← Directory
│                  │
│ ─────────────    │
│ CRM ↗            │  ← launches GoHighLevel (SSO, new tab)
│ Academia ↗       │  ← launches Open edX (SSO, new tab)
│ ─────────────    │
│ ⚙  Administración│  ← T3/T4 only
└──────────────────┘
```

Numbers are JetBrains Mono `--warm`; labels are Inter 400 `--ink`. Active item: `bg --sand` + 2px `--champagne` left border.

The two `↗` items are **link-outs, not modules.** They open the external system. Nothing from the CRM or Academy is reproduced inside BluePrint.

---

## 5. The two primitives (build these first — they generate most of the app)

This is the architectural core of the release. Nine of the surfaces below are **configurations of two objects**, not nine separate builds. Build the primitives properly and the modules become configuration.

### 5.1 Primitive A — REGISTRY

A tracked record with an owner, a lifecycle, an optional expiry, and links to files that live elsewhere.

```
Registry record
├── id, tenant_id, registry_type
├── title, description
├── owner (user reference)
├── status              (enum, configurable per registry_type)
├── effective_date, expiry_date       ← drives the alert engine
├── renewal_reminder_offsets[]        ← e.g. [90, 60, 30, 7] days
├── external_links[]                  ← Drive/SharePoint URL + label (NEVER a stored binary)
├── tags[]
├── custom_fields{}                   ← per registry_type schema
├── confidentiality_tier              ← T1 / T2 / T3 / T4
├── created_at, updated_at, created_by
└── audit_events[]
```

Instantiated as **six registries** from one build:

| registry_type | Screen | Key custom fields |
|---|---|---|
| `legal_contract` | Legal | counterparty, contract value, auto-renew, notice period |
| `license_corporate` | Legal | issuing authority, license number, jurisdiction |
| `license_software` | Legal | vendor, seats, cost/month, billing owner |
| `tax_obligation` | Legal | period, authority, filing frequency |
| `person_record` | Equipo | role, start date, professional licenses, CV link, emergency contact |
| `template` | Biblioteca | category, format, version, approved-by, last review |
| `manual` | Biblioteca | section, version, owner, last review, Academy course link |
| `directory_entry` | Directorio | organization, category, contact person, phone, email, website, notes |

The **alert engine** is a single service that reads `expiry_date` + `renewal_reminder_offsets` across *all* registry types and produces the "Requiere atención" feed on Today. Build once.

### 5.2 Primitive B — TICKET

A reported item that gets routed, worked and closed.

```
Ticket
├── id, tenant_id, ticket_type
├── title, body
├── reporter (nullable — anonymous permitted for HR)
├── context{}          ← auto-captured: page, module, role, timestamp
├── assigned_owner
├── status             (enum per ticket_type)
├── severity           (low / medium / high)
├── category           (per ticket_type taxonomy)
├── confidentiality_tier + explicit_visibility_list[]
├── sla_due_at
├── linked_records[]   ← client ref, person ref, registry ref
├── resolution{}       ← per ticket_type schema
├── comments[]
└── audit_events[]
```

Instantiated as:

| ticket_type | Screen | Visibility | Resolution schema |
|---|---|---|---|
| `glitch` | Glitches | **Transparent** — visible to all BluePrint users in tenant | recovery_action, client_made_whole, root_cause, prevention |
| `hr_case` | Equipo | **Confidential** — explicit visibility list only | outcome, actions_taken, closed_by |
| `internal_request` | Tareas | Standard role-based | resolution note |

> **Critical:** `glitch` and `hr_case` share a database table and a service layer but must have **completely different UI tone**. A glitch screen is bright, open, low-friction, celebratory about reporting. An HR case screen is quiet, private, formal, with visible confidentiality indicators. Same engine, opposite atmosphere.

---

## 6. Screen-by-screen wireframes

### Screen 01 — Hoy (Today)

The default landing screen and the daily anchor. Answers: *what needs me today?*

```
┌──────────────────────────────────────────────────────────────────────────┐
│ B_luePrint     [ ⌘K  Buscar…                    ]   ⚡ Glitch    ◐    EM  │
├──────────┬───────────────────────────────────────────────────────────────┤
│ 01 Hoy ▌ │  01 — MIÉRCOLES 26 DE AGOSTO                                  │
│ 02 Glit. │  Buenos días, Esteban                     ← Playfair 36px      │
│ 03 Tareas│                                                                │
│ 04 Desem.│  ┌──── REVISIÓN DIARIA DE GLITCHES ──────────────────────┐    │
│ 05 Equipo│  │  4 de ayer · 2 sin recuperar · 1 arrastrado (3 días)   │    │
│ 06 Legal │  │                                                        │    │
│ 07 Bibl. │  │  ● Cliente esperó 40 min en oficina    Recepción  🔴   │    │
│ 08 Direc.│  │  ● Reporte enviado con precio erróneo  Ventas    🟡    │    │
│          │  │  ● Llaves no disponibles para visita   Operac.   🟡    │    │
│ CRM ↗    │  │  ● Correo de bienvenida sin adjunto    Admin     🟢    │    │
│ Acad. ↗  │  │                                                        │    │
│          │  │              [ Abrir revisión diaria → ]               │    │
│ ⚙ Admin  │  └────────────────────────────────────────────────────────┘    │
│          │                                                                │
│          │  ┌─ MIS TAREAS (6) ────────┐ ┌─ REQUIERE ATENCIÓN (3) ────┐   │
│          │  │ ☐ Renovar póliza    HOY │ │ ⚠ Lic. corredor — María    │   │
│          │  │ ☐ Enviar reporte Q3 2d  │ │   vence en 24 días         │   │
│          │  │ ☐ Revisar contrato  4d  │ │ ⚠ Contrato limpieza        │   │
│          │  │ ☐ Actualizar CV Ana 1sem│ │   renueva automático 15d   │   │
│          │  │        [ Ver todas → ]  │ │ 🔴 Licencia Adobe vencida  │   │
│          │  └─────────────────────────┘ └────────────────────────────┘   │
│          │                                                                │
│          │  ┌─ MIS INDICADORES ──────────────────────────────────────┐   │
│          │  │   12          94%           3.2 días        4.6/5      │   │
│          │  │   Tareas      Glitches      Tiempo de       Satisf.    │   │
│          │  │   a tiempo    recuperados   respuesta       cliente    │   │
│          │  │   ▲ +2        ▲ +6pts       ▼ -0.4          ▲ +0.2     │   │
│          │  └────────────────────────────────────────────────────────┘   │
└──────────┴───────────────────────────────────────────────────────────────┘
```

Behaviour:
- The Glitch panel is **always first**. It is the daily ritual and the adoption anchor.
- "Requiere atención" is fed by the registry alert engine across all six registries.
- KPI tile numerals are Playfair 36px; labels mono 11px uppercase; deltas mono 12px in status colors.
- T1 sees only own tasks and own KPIs. T2+ additionally see a team roll-up.

---

### Screen 02 — Revisión Diaria de Glitches (the morning meeting)

**This screen *is* the meeting.** It replaces Four Seasons' printout. Designed to be projected on a screen while department heads talk through it.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  02 — REVISIÓN DIARIA                        [ Ayer ▾ ]  [ Presentar ⛶ ] │
│  Miércoles 26 de agosto                                                   │
│                                                                           │
│  ┌─────────────┬─────────────┬──────────────┬─────────────────────────┐  │
│  │      4      │      2      │      1       │        87%              │  │
│  │  Reportados │     Sin     │  Arrastrados │     Recuperados         │  │
│  │     ayer    │  recuperar  │   (>2 días)  │     este mes            │  │
│  └─────────────┴─────────────┴──────────────┴─────────────────────────┘  │
│                                                                           │
│  ── RECEPCIÓN ─────────────────────────────────────── Resp.: Coord. ──   │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │ 🔴  Cliente esperó 40 minutos en oficina                            │ │
│  │     Cliente: J. Restrepo · Reportado 25 ago 16:20 · Día 2           │ │
│  │                                                                      │ │
│  │     Qué pasó      La visita no fue registrada en la agenda          │ │
│  │     Recuperación  ⚠ Pendiente                                        │ │
│  │     Cliente OK    ⚠ Pendiente                                        │ │
│  │                                                                      │ │
│  │     [ Registrar recuperación ]  [ Asignar ]  [ Cerrar ]              │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  ── VENTAS ────────────────────────────────────────── Resp.: Gerente ──  │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │ 🟡  Reporte enviado con precio desactualizado                       │ │
│  │     Cliente: M. Chen · Reportado 25 ago 11:05 · Día 1               │ │
│  │                                                                      │ │
│  │     Recuperación  ✓ Llamada + reporte corregido en 2h               │ │
│  │     Cliente OK    ✓ Confirmado por el cliente                        │ │
│  │     Prevención    Plantilla ahora extrae precio del registro        │ │
│  │                                                          [ Cerrar ]  │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  ⓘ  Un glitch permanece en esta pantalla hasta que se registre la        │
│     recuperación. Nada se pierde entre las grietas.                      │
└──────────────────────────────────────────────────────────────────────────┘
```

Rules:
- Grouped **by responsible department**, so each head speaks to their own block.
- Open glitches **roll forward** every day with a visible day counter until closed with a recovery outcome. This is the "nothing falls between the cracks" mechanic.
- A glitch **cannot be closed** without `recovery_action` and `client_made_whole` filled.
- **There is no "who is at fault" field.** Anywhere. By design.
- `[ Presentar ⛶ ]` = full-screen presentation mode for the actual morning meeting.

---

### Screen 03 — Reportar un Glitch (modal, from anywhere)

Must be completable in under 20 seconds or people stop using it.

```
        ┌────────────────────────────────────────────────┐
        │  REPORTAR UN GLITCH                        ✕   │
        │                                                 │
        │  Sin culpa. Solo mejoramos.   ← Playfair italic │
        │                                                 │
        │  ¿Qué pasó?                                     │
        │  ┌───────────────────────────────────────────┐ │
        │  │ Una línea es suficiente…                  │ │
        │  └───────────────────────────────────────────┘ │
        │                                                 │
        │  Gravedad     ( 🟢 Menor )( 🟡 Media )( 🔴 Alta )│
        │                                                 │
        │  Tipo         ( Experiencia )( Producto )       │
        │                                                 │
        │  Cliente afectado (opcional)                    │
        │  ┌───────────────────────────────────────────┐ │
        │  │ 🔍 Buscar…                                │ │
        │  └───────────────────────────────────────────┘ │
        │                                                 │
        │  📎 Captura (opcional)                          │
        │                                                 │
        │  ⓘ Capturado automáticamente: página, módulo,   │
        │    rol, oficina, fecha y hora.                  │
        │                                                 │
        │              [ Cancelar ]  [ Reportar ]         │
        └────────────────────────────────────────────────┘
```

Only **one field is required**: the description. Everything else is optional or auto-captured.

---

### Screen 04 — Panel de Glitches (patterns and health)

The individual glitch matters less than the pattern.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  02 — GLITCHES                    [ Revisión diaria ] [ Panel ▌] [ Todos ]│
│  Panel de patrones                          [ Últimos 90 días ▾ ]        │
│                                                                           │
│  ┌──────────────┬──────────────┬──────────────┬──────────────────────┐   │
│  │     47       │     87%      │    1.4 días  │        12            │   │
│  │  Reportados  │ Recuperados  │   Tiempo de  │  Reportados por      │   │
│  │              │              │  recuperación│  persona (promedio)  │   │
│  │  ▲ +11       │  ▲ +9 pts    │  ▼ -0.6      │  ▲ +3  ✓ saludable   │   │
│  └──────────────┴──────────────┴──────────────┴──────────────────────┘   │
│                                                                           │
│  ── PATRONES RECURRENTES ────────────────────────────────────────────    │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │  8×  Agenda de visitas no sincronizada        ▓▓▓▓▓▓▓▓  Recepción   │ │
│  │  6×  Precio desactualizado en documentos      ▓▓▓▓▓▓    Ventas      │ │
│  │  5×  Documento faltante en expediente         ▓▓▓▓▓     Operaciones │ │
│  │  3×  Retraso en respuesta > 24h               ▓▓▓       Admin       │ │
│  │                                                                      │ │
│  │  ◐ Copilot: los 8 glitches de agenda ocurren cuando la visita se    │ │
│  │    agenda desde el CRM en lugar de la agenda compartida. Un cambio  │ │
│  │    de proceso resolvería el 17% de todos los glitches del trimestre.│ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  ── POR DEPARTAMENTO ───────────  ── POR ETAPA DEL CLIENTE ────────────  │
│  Recepción      ▓▓▓▓▓▓▓▓  14      Primer contacto  ▓▓▓       6           │
│  Ventas         ▓▓▓▓▓▓    11      Visita           ▓▓▓▓▓▓▓▓  15          │
│  Operaciones    ▓▓▓▓▓     9       Negociación      ▓▓▓▓      8           │
│  Administración ▓▓▓▓      8       Cierre           ▓▓▓▓▓     10          │
│  Marketing      ▓▓        5       Post-venta       ▓▓▓▓      8           │
│                                                                           │
│  ⓘ Un equipo que reporta cero glitches no es un equipo perfecto.         │
│    Es un equipo que dejó de reportar.                                    │
└──────────────────────────────────────────────────────────────────────────┘
```

> **Metric design rule — non-negotiable.** *Under-reporting is the failure mode, not glitch volume.* "Reportados por persona" is displayed as a **health signal with a healthy floor**, never as a negative. Recovery rate and recovery time are the performance metrics. If a manager can be punished for a high glitch count, reporting stops within a month and the system becomes theater. The UI must actively communicate this — hence the footer note, which is permanent copy, not a placeholder.

For **T4 (HQ)**, this screen gains a cross-tenant view: glitch and recovery rates by franchise office. This is how "premium boutique experience" becomes an enforceable network standard rather than a brand promise.

---

### Screen 05 — Tareas

```
┌──────────────────────────────────────────────────────────────────────────┐
│  03 — TAREAS                    [ Mías ▌][ Equipo ][ Todas ]  [ + Nueva ]│
│                                                                           │
│  [ 🔍 Filtrar ]  [ Responsable ▾ ] [ Origen ▾ ] [ Estado ▾ ]             │
│                                                                           │
│  ── VENCIDAS (1) ──────────────────────────────────────────────────      │
│  ☐  Renovar licencia de Adobe            🔴 -3d   Admin      ⟵ Legal     │
│                                                                           │
│  ── HOY (2) ───────────────────────────────────────────────────────      │
│  ☐  Renovar póliza de responsabilidad     Hoy    Coord.      ⟵ Legal     │
│  ☐  Registrar recuperación — J. Restrepo  Hoy    Recepción   ⟵ Glitch    │
│                                                                           │
│  ── ESTA SEMANA (3) ───────────────────────────────────────────────      │
│  ☐  Enviar reporte trimestral a socios    2d     Gerente                 │
│  ☐  Revisar contrato de limpieza          4d     Coord.      ⟵ Legal     │
│  ☐  Actualizar CV de Ana en expediente    5d     RRHH        ⟵ Equipo    │
│                                                                           │
│  ── MÁS ADELANTE (6) ──────────────────────────────────────  [ Ver → ]   │
└──────────────────────────────────────────────────────────────────────────┘
```

The `⟵` badge shows **provenance**: tasks are largely *generated* by other modules (an expiring license, an unrecovered glitch, a missing CV) rather than typed by hand. Clicking the badge opens the source record. This is what makes the registries useful rather than decorative.

---

### Screen 06 — Desempeño (Performance)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  04 — DESEMPEÑO         [ Personal ▌][ Equipo ][ Satisfacción ][ Reportes]│
│                                                    [ Este trimestre ▾ ]  │
│                                                                           │
│  ── MIS INDICADORES ────────────────────────────────────────────────     │
│  ┌────────────┬────────────┬────────────┬────────────────────────────┐  │
│  │    94%     │    1.2d    │    100%    │          4.6 / 5           │  │
│  │  Tareas a  │  Tiempo de │  Registros │      Satisfacción del      │  │
│  │   tiempo   │ recuperac. │ al día     │        cliente             │  │
│  │  ▲ +6 pts  │  ▼ -0.4d   │  = 0       │        ▲ +0.2              │  │
│  └────────────┴────────────┴────────────┴────────────────────────────┘  │
│                                                                           │
│  ── TENDENCIA ──────────────────────────────────────────────────────     │
│  100% ┤                                              ╭──────             │
│       │                            ╭────────╮   ╭────╯                   │
│   75% ┤        ╭───────────────────╯        ╰───╯                        │
│       │   ╭────╯                                                          │
│   50% ┼───╯                                                               │
│       └────┬────────┬────────┬────────┬────────┬────────┬────────        │
│           Jun      Jul      Ago      Sep      Oct      Nov               │
│                                                                           │
│  ── ORIGEN DE LOS DATOS ────────────────────────────────────────────     │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │  Tareas, glitches, registros    BluePrint        ✓ En vivo          │ │
│  │  Satisfacción del cliente       Encuestas        ✓ En vivo          │ │
│  │  Campañas y pipeline            GoHighLevel      ⟳ Importado 25 ago │ │
│  │                                                  [ Importar CSV ]    │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

**Release 1 data strategy — read carefully.** Three feeds:

1. **Native (live).** Task completion, glitch recovery, registry currency, SLA adherence. Generated inside BluePrint by the primitives. Free — no integration work.
2. **Native surveys (live).** Satisfaction polls sent and collected by BluePrint.
3. **CRM metrics (manual bridge in R1).** Sales pipeline, campaign performance, conversion. In Release 1 these arrive by **CSV import mapped to defined metric definitions**. In Release 1.5 the GoHighLevel connector replaces the import and feeds the *same* metric definitions and the *same* screens.

Build the metric-definition layer properly now; swap the feed later. **The provenance panel is a permanent UI element**, not a temporary scaffold — users must always know whether a number is live or imported, and when.

Team tab (T2+) shows the same metrics per person, permission-scoped: a manager sees their own team, a Principal sees everyone, a coordinator sees only themselves.

---

### Screen 07 — Equipo (People / HR)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  05 — EQUIPO      [ Personas ▌][ Casos ][ Licencias ][ Bienestar ]       │
│                                                       [ + Persona ]      │
│  [ 🔍 Buscar ]                                                            │
│                                                                           │
│  NOMBRE            ROL              LICENCIAS         CV      ESTADO      │
│  ─────────────────────────────────────────────────────────────────────   │
│  María R.          Corredora        🟡 Vence 24d      ✓      Activa      │
│  Ana G.            Coordinadora     — n/a             🔴 Falta  Activa   │
│  Carlos M.         Asesor           🟢 Vigente        ✓      Activa      │
│  Luisa P.          Gerente          🟢 Vigente        ✓      Activa      │
│  Diego S.          Asesor           🔴 Vencida        ✓      Suspendida  │
│                                                                           │
└──────────────────────────────────────────────────────────────────────────┘
```

Person record (drill-in) — a `person_record` registry entry:

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ← Equipo                                                                 │
│  05 — EXPEDIENTE                                                          │
│  María Restrepo                              ← Playfair 36px              │
│  Corredora de bienes raíces · Activa desde mar 2024                       │
│                                                                           │
│  ┌─ LICENCIAS Y CERTIFICACIONES ──────────────────────────────────────┐  │
│  │  Licencia de corredor    ACOBIR    #4821    🟡 Vence 19 sep 2026   │  │
│  │                                              [ Registrar renovación]│  │
│  │  Certificación B_Academy  Nivel 2            🟢 Vigente             │  │
│  │                                              [ Ver en Academia ↗ ]  │  │
│  └────────────────────────────────────────────────────────────────────┘  │
│                                                                           │
│  ┌─ DOCUMENTOS ──────────────┐  ┌─ CONTRATO ────────────────────────┐   │
│  │ 📄 CV            Drive ↗  │  │ Tipo      Indefinido               │   │
│  │ 📄 Contrato      Archivo ↗│  │ Inicio    12 mar 2024              │   │
│  │ 📄 Cédula        Drive ↗  │  │ Revisión  12 mar 2027              │   │
│  └───────────────────────────┘  └────────────────────────────────────┘   │
│                                                                           │
│  ┌─ DESEMPEÑO ────────────────────────────────────────────────────────┐  │
│  │  Ver indicadores en Desempeño → Equipo → María R.        [ Abrir ] │  │
│  └────────────────────────────────────────────────────────────────────┘  │
│                                                                           │
│  🔒 Casos de RRHH relacionados          Visible solo para T3/T4          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Casos tab** — `hr_case` tickets. Confidential by default, visible only to the explicit visibility list. Supports **anonymous submission**. A case about a person is structurally invisible to that person regardless of their tier. The UI carries a persistent lock indicator and a visibility statement on every case ("Visible para: Principal, RRHH HQ").

**Bienestar tab** — a curated `directory_entry` list: psychologists, occupational health, legal aid, employee assistance, confidential helpline. Link-outs and contact details only. No clinical data is ever stored in BluePrint.

---

### Screen 08 — Legal (Legal & Assets)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  06 — LEGAL Y ACTIVOS                                                     │
│      [ Contratos ▌][ Licencias ][ Software ][ Impuestos ][ Calendario ]  │
│                                                        [ + Registro ]    │
│                                                                           │
│  ── REQUIERE ATENCIÓN ──────────────────────────────────────────────     │
│  🔴  Licencia Adobe Creative Cloud       Venció hace 3 días    Admin     │
│  🟡  Contrato de limpieza                Renueva auto. en 15d  Coord.    │
│  🟡  Licencia de corredor — María R.     Vence en 24 días      RRHH      │
│                                                                           │
│  ── TODOS LOS CONTRATOS ────────────────────────────────────────────     │
│  REGISTRO              CONTRAPARTE      VENCE         VALOR      RESP.   │
│  ────────────────────────────────────────────────────────────────────    │
│  Arrendamiento oficina  Inmob. Central  31 dic 2027  $2,400/m   Princ.  │
│  Contrato de limpieza   ServiClean      15 sep 2026  $380/m     Coord.  │
│  Seguro responsabilidad Aseguradora X   30 nov 2026  $1,200/a   Princ.  │
│  Contabilidad externa   Estudio Pérez   Indefinido   $800/m     Princ.  │
│                                                                           │
│  ⓘ  BluePrint registra estado, vencimiento y responsable.                │
│     Los documentos firmados viven en el archivo legal seguro. ↗          │
└──────────────────────────────────────────────────────────────────────────┘
```

Every tab is the **same registry component** with a different `registry_type` and column set. The footer note is permanent and load-bearing: BluePrint is a *tracker*, not the legal archive. Signed documents are linked, never stored.

The **Calendario** tab renders all `expiry_date` values across all registries on a 12-month timeline — the single "what's coming at us" view.

---

### Screen 09 — Biblioteca (Library)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  07 — BIBLIOTECA          [ Plantillas ▌][ Manuales ][ Formación ]       │
│  [ 🔍 Buscar en toda la biblioteca ]                                      │
│                                                                           │
│  ── PLANTILLAS ─────────────────────────────────────────────────────     │
│                                                                           │
│  REPORTES PARA CLIENTES                                                   │
│  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐         │
│  │ 📄               │ │ 📊               │ │ 📄               │         │
│  │ Reporte de       │ │ Proyección de    │ │ Informe de       │         │
│  │ mercado          │ │ inversión        │ │ avance de obra   │         │
│  │                  │ │                  │ │                  │         │
│  │ PDF · v2.1       │ │ XLSX · v3.0      │ │ PDF · v1.4       │         │
│  │ Rev. ago 2026 ✓  │ │ Rev. ago 2026 ✓  │ │ Rev. may 2026 🟡 │         │
│  │ [Abrir] [Copiar] │ │ [Abrir] [Copiar] │ │ [Abrir] [Copiar] │         │
│  └──────────────────┘ └──────────────────┘ └──────────────────┘         │
│                                                                           │
│  REPORTES PARA DIRECCIÓN     ▸ 4 plantillas                              │
│  CONTRATOS Y LEGAL           ▸ 9 plantillas                              │
│  CORREOS                     ▸ 12 plantillas                             │
│  FINANCIERO Y PROYECCIONES   ▸ 6 plantillas                              │
│  MARCA Y MARKETING           ▸ 8 plantillas                              │
│                                                                           │
│  ⓘ  Los archivos viven en Drive. BluePrint controla versión,             │
│     aprobación y fecha de revisión.                                       │
└──────────────────────────────────────────────────────────────────────────┘
```

- **Plantillas** — `template` registry. Versioned, with an approver and a review date. A template past its review date shows 🟡 and generates a task. Files open from Drive; BluePrint governs the metadata.
- **Manuales** — `manual` registry. Operating procedures, brand manual, compliance manual. Full-text searchable and **indexed for the Copilot** — this is the Copilot's primary knowledge source.
- **Formación** — link-outs to B_Academy course catalogue with the user's completion status pulled from Open edX. **Lessons are never rendered inside BluePrint.**

---

### Screen 10 — Directorio (Directory)

```
┌──────────────────────────────────────────────────────────────────────────┐
│  08 — DIRECTORIO                                        [ + Contacto ]   │
│  [ 🔍 Buscar ]  [ Categoría ▾ ]                                           │
│                                                                           │
│  CONTABILIDAD Y FINANZAS                                                  │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │  Estudio Pérez & Asociados            Contabilidad externa          │ │
│  │  Lic. Ramón Pérez · +507 6000-0000 · ramon@perez.com                │ │
│  │  ⓘ Cierre mensual antes del día 5. Contrato activo ⟶ Legal          │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  LEGAL                                                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │  Morgan Abogados                      Corporativo e inmobiliario    │ │
│  │  Dra. Elena Morgan · +507 6000-0001 · elena@morgan.com              │ │
│  │  ⓘ Consultas de contratos de compraventa                            │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  ▸ AUTORIDADES Y REGISTROS   (ACOBIR, Registro Público, DGI)             │
│  ▸ PROVEEDORES               (limpieza, TI, seguros, imprenta)           │
│  ▸ SITIOS ÚTILES             (portales, tasas, herramientas)             │
│  ▸ BIENESTAR                 ⟶ Equipo → Bienestar                        │
└──────────────────────────────────────────────────────────────────────────┘
```

The `⟶ Legal` cross-link is the payoff of the shared registry primitive: the directory entry for the accountant links to the active contract record, which links to its renewal task, which appears on Today.

---

### Screen 11 — Copilot

Available as a right-hand panel on every screen (context-aware) and as a full screen.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ◐ COPILOT                                                          ✕   │
│  Contexto: Panel de glitches · Últimos 90 días                           │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │  ¿Qué licencias vencen en los próximos 60 días?                     │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  Tres licencias vencen antes del 25 de octubre:                          │
│                                                                           │
│  • Licencia de corredor — María R. · 19 sep · ACOBIR                     │
│  • Antivirus corporativo · 03 oct · 12 puestos                           │
│  • Permiso de operación · 21 oct · Municipio                             │
│                                                                           │
│  La licencia de Adobe ya está vencida (23 ago).                          │
│                                                                           │
│  📎 Fuentes  Legal → Licencias (3 registros) · Equipo → María R.         │
│  🕐 Datos al 26 ago 2026, 08:14                                           │
│                                                                           │
│  [ Crear tareas de renovación ]  ← requiere confirmación (AI-3)          │
│                                                                           │
│  ────────────────────────────────────────────────────────────────────    │
│  Sugerencias                                                              │
│  · Resumir los glitches de esta semana                                   │
│  · ¿Dónde está la plantilla de proyección?                               │
│  · ¿Cuál es el proceso para dar de alta a un empleado?                   │
│  ────────────────────────────────────────────────────────────────────    │
│  [ Preguntar…                                                    ] [ → ] │
└──────────────────────────────────────────────────────────────────────────┘
```

Authority is governed by [[BluePrint Product Constitution]] §11 (AI-0 to AI-4), unchanged:

- **AI-0/AI-1** — answer from manuals, registries and metrics. Always cite sources and data timestamp. Execute immediately.
- **AI-2** — draft from approved templates. Output is always a draft.
- **AI-3** — prepare an action (create tasks, update a non-restricted status). **Preview + explicit confirmation required.**
- **AI-4** — approve, sign, pay, publish a template, waive a control. **Prohibited.**

The Copilot can never retrieve a record the requesting user cannot open directly. Permission filtering happens **before** model invocation, not after.

---

### Screen 12 — Administración (T3/T4 only)

Tabs: **Usuarios y permisos** · **Oficinas** (T4) · **Integraciones** · **Definiciones de indicadores** · **Registro de auditoría**

- **Definiciones de indicadores** is more important than it sounds: it is where a KPI's formula, period, source and owner are declared. It is what lets the CSV bridge become a live connector in R1.5 without changing any dashboard.
- **Registro de auditoría** is immutable and covers every restricted data change, permission change, confidential-record access and external handoff.

---

## 7. Data model additions (Release 1)

Extends [[BluePrint Product Constitution]] §7. Existing tenancy/security, knowledge, AI and audit domains are unchanged.

| Domain | New entities |
|---|---|
| Registry | `Registry`, `RegistryType`, `RegistryRecord`, `RenewalRule`, `ExternalLink`, `Alert` |
| Ticketing | `Ticket`, `TicketType`, `TicketComment`, `Resolution`, `VisibilityGrant`, `SLARule` |
| Glitch | `Glitch` (ticket_type view), `RecoveryAction`, `GlitchPattern`, `DailyReview` |
| People | `PersonRecord`, `ProfessionalLicense`, `EmploymentTerm`, `DocumentLink` |
| Performance | `MetricDefinition`, `MetricValue`, `MetricSource`, `Snapshot`, `Survey`, `SurveyResponse` |
| Directory | `DirectoryEntry`, `DirectoryCategory` |
| Work | `Task`, `TaskSource` (provenance link to originating record) |

Every entity carries `tenant_id`, timestamps, actor/provenance, lifecycle status and `confidentiality_tier` per Constitution §7.

---

## 8. Permission matrix

| Surface | T1 Coordinator | T2 Manager | T3 Principal | T4 HQ |
|---|---|---|---|---|
| Today | Own | Own + team | Full tenant | Cross-tenant |
| Report a glitch | ✓ | ✓ | ✓ | ✓ |
| Daily glitch review | View | View + close | Full | Cross-tenant |
| Glitch dashboard | View | View | Full | Cross-tenant patterns |
| Tasks | Own + assigned | Team | Full tenant | Cross-tenant |
| Personal KPIs | Own only | Own | Own | Own |
| Team KPIs | ✗ | Own team | Full tenant | Cross-tenant |
| People — records | View | View + edit team | Full | Full |
| People — HR cases | Submit only | Submit only | Full tenant | Full |
| People — wellbeing links | ✓ | ✓ | ✓ | ✓ |
| Legal & Assets | View + edit assigned | View + edit | Full | Full |
| Library — use | ✓ | ✓ | ✓ | ✓ |
| Library — govern versions | ✗ | ✗ | Tenant templates | Network templates |
| Directory | View + add | Full | Full | Full |
| Copilot | Scoped to own access | Scoped | Scoped | Scoped |
| Administration | ✗ | ✗ | Tenant | Network |

Enforce **server-side** for UI, API, exports and Copilot tools alike. A client-side-only permission check is a release blocker.

---

## 9. Build order

**Phase 0 — Foundation (must be full strength; do not shortcut)**
Multi-tenancy · authentication · roles and record-level access · confidentiality tiers · immutable audit · base entity conventions · design-system component library.

> This foundation is shared with Release 2. Phasing the *modules* is safe. Shortcutting the *foundation* turns Release 2 into a rewrite and defeats the entire sequencing decision.

**Phase 1 — Primitives**
Registry engine + Ticket engine + alert/renewal service + task engine with provenance.

**Phase 2 — The daily ritual (the adoption anchor — ship this early and get it right)**
Report a Glitch modal · Daily Review screen · Glitch dashboard · Today screen.

**Phase 3 — Registries**
Legal & Assets · People · Library · Directory. Four screens, one component.

**Phase 4 — Performance**
Metric definitions · native metrics · surveys · CSV bridge · personal and team dashboards.

**Phase 5 — Copilot**
Knowledge indexing over manuals and registries · AI-0/AI-1 retrieval with citations · AI-2 drafting · AI-3 confirmed actions.

**Phase 6 — Administration + hardening**
Permissions UI · metric definitions UI · audit viewer · integrations · accessibility and security pass.

**Release 1.5** — GoHighLevel metrics connector replaces the CSV bridge, feeding the same metric definitions.
**Release 2** — the transaction spine, per [[BluePrint Golden Workflow - Wireframe and Validation]].

---

## 10. Acceptance criteria for Release 1

**Functional**
- A glitch can be reported from any screen in under 20 seconds with one required field.
- An open glitch rolls forward on the Daily Review with a visible day counter until closed with a recorded recovery.
- A glitch cannot be closed without `recovery_action` and `client_made_whole`.
- No "fault" or "blamed person" field exists anywhere in the schema or UI.
- Every registry record with an `expiry_date` generates alerts at its configured offsets and appears on Today.
- A task generated by another module links back to its source record.
- An HR case about a person is invisible to that person at every tier, including Principal.
- Anonymous HR submission works and cannot be de-anonymized through the audit log by a tenant admin.
- Every Copilot answer over company knowledge cites its sources and data timestamp.
- No Copilot response returns a record the requesting user cannot open directly.
- Every KPI displays its source and whether it is live or imported, with the import date.

**Design**
- `--champagne` appears nowhere as small text on a light background.
- Playfair / Inter / JetBrains Mono are each used only for their assigned role.
- Table rows are ≤ 44px; no screen requires scrolling to read fewer than 15 table rows on a 1440×900 display.
- No drop shadows. Flat editorial surfaces only.
- The mono-eyebrow + Playfair-heading pattern appears on every screen.

**Non-functional**
- No cross-tenant data path in automated security tests.
- Server-side authorization for UI, API, export and Copilot tool calls.
- Audit event for every restricted change, permission change and confidential-record access.
- Full keyboard navigation; visible focus states; WCAG AA contrast throughout.
- Spanish is the primary interface language; the string layer must support EN without layout breakage.

---

## 11. Explicitly out of scope for Release 1

Lead pipelines, contacts-as-CRM, campaigns, messaging · course content or delivery · marketplace browsing · transaction workspace, compliance gates, document generation, e-signature, commission engine (**Release 2**) · native file storage · payroll processing · accounting ledger · automated GoHighLevel connector (**Release 1.5**) · cross-tenant benchmarking beyond HQ's own network view · client portal · native mobile applications · general workflow builder.

---

## 12. Source and change log

- **2026-08-26 v1.0** — Created from the founder scope redirection of 2026-08-26 and the Board of Advisors session. Restores and formalizes the back-office architecture originally specified on 2026-07-18 in [[Platform Information Architecture]] and [[Product Modules]] (Glitch Report, People/HR, Cases, Resource Library, Command Bar), which [[BluePrint Product Constitution]] v1.0 had narrowed away. Design tokens extracted from the live `bfranchising.com` stylesheet (`/assets/styles-D1Axz5EQ.css`) on 2026-08-26; contrast ratios computed, not estimated.

## Related

[[BluePrint Product Constitution]] · [[BluePrint Product Map]] · [[MVP Scope]] · [[Product Modules]] · [[Platform Information Architecture]] · [[Roles and Access Matrix]] · [[BluePrint Golden Workflow - Wireframe and Validation]] · [[../18_Ecosystem/02 - BluePrint]] · [[../18_Ecosystem/15 - Website Audit - bfranchising.com - 2026-08-16]]
