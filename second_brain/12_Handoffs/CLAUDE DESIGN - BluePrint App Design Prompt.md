---
project: B_RealEstate
title: "CLAUDE DESIGN - BluePrint App Design Prompt"
type: design_brief
deliverable: "BluePrint Release 1 — functional back-office application prototype"
target_tool: "Claude Design"
version: 1.0
status: "Ready to paste"
owner: Esteban
created: 2026-08-26
source: "02_Offers/01_BluePrint/BluePrint Wireframe - Back Office OS (Developer Handoff) v1.0 + Product Constitution v2.0"
tags: [handoff, design, product, app, claude-design, blueprint, backoffice]
---

> [!NOTE] Verified against canon 2026-09-23
> **Regenerate before external use.** Handoffs are self-contained snapshots, so this file may still inline pre-reconciliation naming, pricing or product boundaries. Check against canon: BluePrint owns the deal from qualified opportunity · Building Blocks (not Academy) · B_ Partner (not White-Label) · $399/$799 + $1,500 setup · $950k raise · no “one database” or “CRM propio” claims. If a handoff and its source note disagree, **the source note wins**.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# DESIGN PROMPT — BluePrint (Back Office Application)

> **Vault note (not part of the prompt):** source of truth is [[../02_Offers/01_BluePrint/20 - Wireframe - Back Office OS]]. If that file changes, regenerate this prompt. Everything below the line is self-contained and paste-ready.

**Paste everything below into Claude Design.**

---

# 1. WHAT WE ARE BUILDING

A **functional, clickable web application** — not a marketing site, not a landing page, not a dashboard mockup. A working internal tool.

**BluePrint** is the operating brain of a small real-estate back office. A boutique agency runs on three to eight administrative people. Their institutional knowledge — which licences expire when, where the approved templates live, who the accountant is, what went wrong for a client last Tuesday and whether it was put right, how the team is actually performing — currently lives in spreadsheets, WhatsApp threads, individual inboxes and individual memories. BluePrint is where it lives instead.

**Interface language: Spanish.** Build the string layer so English can be swapped in without layout breakage, but design and populate in Spanish.

## Who uses this

Administrative staff only. Four tiers:

| Tier | Who | Sees |
|---|---|---|
| **T1 — Coordinador** | Admin coordinator, receptionist, assistant | Glitch logging, tasks, registries, library, directory, own personal KPIs |
| **T2 — Gerente** | Operations / office manager | The above + team KPIs, glitch review and closure, full registries |
| **T3 — Principal** | Owner, director, C-suite | Everything in the office including confidential HR |
| **T4 — HQ** | Network admin, franchise oversight | All offices, cross-office patterns, template governance |

**Nobody in sales uses this.** Sales advisors work in a separate CRM and have no login here — we want them with clients, not behind software. A salesperson appears in BluePrint as a *record* (in People, in KPIs, in licence tracking) but never as a user.

## The daily anchor

The single most important thing in this product is a **morning ritual**. Every day the back office gathers and reviews yesterday's service failures — what went wrong for a client, and what was done to put it right. It is modelled on the Four Seasons "glitch report." One screen *is* that meeting.

Design for that. If the office opens this app every morning out of habit, the product succeeded. If they don't, nothing else matters.

---

# 2. THE CRITICAL DESIGN TENSION — READ THIS TWICE

The company's marketing site (`bfranchising.com`) is a beautiful editorial piece: enormous whitespace, 88px Playfair headlines, hand-drawn scroll-linked lines, magnetic buttons, pinned horizontal sections, parallax. It is excellent **for a marketing site**.

**Copying that aesthetic into this application would ruin it.**

This is a tool someone uses for eight hours a day, containing dense tables of licence expiries and glitch records. A user needs to read fifteen rows without scrolling, not one poetic statement per viewport.

## What to inherit from the marketing site

- ✅ **The exact palette.** Warm bone/sand neutrals, ink text, champagne accent. Non-negotiable — it is the brand.
- ✅ **The three-font system.** Playfair Display / Inter / JetBrains Mono, each with one strict job.
- ✅ **The signature editorial device:** a small uppercase mono eyebrow above a Playfair heading. Use it on every screen. It is what makes this feel boutique rather than corporate.
- ✅ **Flat surfaces, hairline rules, no ornament.** Restraint as the luxury signal.
- ✅ **Rounded corners, never sharp.**

## What to reject outright

- ❌ **The spacing.** Marketing section padding of 96–128px becomes **24–32px** here. Table rows are **44px**, not 80px.
- ❌ **Headline scale.** 88px H1 becomes **32–36px** page titles.
- ❌ **The motion system.** No scroll-linked drawing, no pinned sections, no parallax, no magnetic cursor, no hand-drawn lines, no count-up numbers on every entry, no smooth-scroll library. See §8.
- ❌ **One-idea-per-viewport pacing.** This is a dense information tool. Fill the screen usefully.
- ❌ **Drop shadows.** Depth comes from bone-tone layering only.

> **The test:** on a 1440×900 laptop, a user must be able to read **at least 15 table rows without scrolling**. If your design can't, the density is wrong regardless of how beautiful it looks.

**Feel target:** *a beautifully made instrument.* Calm, dense, fast, quietly premium. Think a well-designed accounting tool made by people with taste — not a SaaS dashboard, and not a magazine.

---

# 3. DESIGN SYSTEM

These are production values extracted from the live brand stylesheet. Use them exactly.

## Palette

```css
/* Foundation — warm editorial neutrals. NEVER cool grays. */
--bone:        #FAF8F3;   /* app background */
--offwhite:    #F7F4ED;   /* card / panel surface */
--sand:        #EFEAE0;   /* table headers, hover, muted fills, inactive */
--ink:         #1A1A1A;   /* primary text, primary button fill */
--warm:        #55514C;   /* secondary text, labels, meta */
--champagne:   #B89B5E;   /* accent, focus ring, active indicator */
--rule:        rgba(26,26,26,0.12);  /* every border and divider */

/* Semantic status — desaturated to sit inside the editorial palette.
   Do NOT substitute default Tailwind green/amber/red — they look cheap on bone. */
--status-good:     #5F7052;   /* resolved, on track, valid, current */
--status-warn:     #B8823E;   /* due soon, attention, expiring < 60 days */
--status-critical: #A13B2A;   /* overdue, expired, unrecovered */
--status-info:     #4A5A6B;   /* in progress, neutral state */
--status-neutral:  #55514C;   /* closed, archived, no action */
```

## ⚠ The champagne rule — the most likely defect in this build

Contrast ratios on `--bone`, computed:

| Foreground | Ratio | Verdict |
|---|---|---|
| `--ink` | **16.4 : 1** | AAA — all primary text |
| `--warm` | **7.4 : 1** | AAA — all secondary text |
| `--status-critical` | **6.2 : 1** | AA — safe for text |
| `--champagne` | **2.5 : 1** | **FAILS AA** |

**Champagne may never be used for body text, labels or any small text on a light background.** It is permitted only for: focus rings, active-state indicators, 1–2px rules and underlines, icon strokes, decorative numerals ≥ 32px, and as a *background* with bone text on top. Everything else uses ink or warm.

## Typography

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..700;1,400..600&family=Inter:wght@300;400;500&family=JetBrains+Mono:wght@400;500&display=swap"/>
```

| Family | Job — do not mix these up |
|---|---|
| **Playfair Display** 400–700 + italic | Page titles, screen headings, large KPI numerals, empty-state headlines. The boutique signal. |
| **Inter** 300/400/500 | All body copy, UI labels, buttons, form fields, table cells, navigation. |
| **JetBrains Mono** 400/500 | Eyebrows, section numbers, dates, IDs, reference codes, tabular numbers, status chips, countdowns. |

### The signature pattern — use on every screen

```
01 — REVISIÓN DIARIA        ← JetBrains Mono · 12px · uppercase
                               letter-spacing 0.1em · --warm

Glitches de ayer            ← Playfair Display · 32px · weight 400
                               letter-spacing -0.025em · --ink
```

Type scale: `xs` 12px · `sm` 14px · `base` 16px · `lg` 18px · `xl` 20px · `2xl` 24px · `3xl` 30px · `4xl` 36px.
Tracking: **-0.025em** on all Playfair headings · **+0.1em** on all uppercase mono eyebrows.

## Spacing, radius, layout

```css
--spacing: 4px;          /* everything is a multiple */
--radius-card: 16px;     /* cards, panels, modals */
--radius-control: 8px;   /* buttons, inputs, chips */
```

Section padding **24–32px**. Card padding **24px**. Table rows **44px**. Content max-width **72rem**, centred.

```
┌──────────────────────────────────────────────────────────────────┐
│  TOP BAR   56px · bg bone · border-bottom rule                   │
├──────────┬───────────────────────────────────────────────────────┤
│ SIDEBAR  │  CONTENT                                              │
│ 240px    │  max-width 72rem · padding 32px · bg bone             │
│ bg bone  │                                                       │
│ border-r │                                                       │
│ rule     │                                                       │
└──────────┴───────────────────────────────────────────────────────┘
```

## Components

**Button primary** — `bg ink` · `text bone` · radius 8px · padding 10px 20px · Inter 500 14px · hover `#000` · focus ring 2px champagne offset 2px
**Button secondary** — transparent · `border 1px rule` · `text ink` · hover `bg sand`
**Button ghost** — transparent · `text warm` · hover `text ink`
**Card** — `bg offwhite` · `border 1px rule` · radius 16px · padding 24px · **no shadow**
**Input** — `bg bone` · `border 1px rule` · radius 8px · padding 10px 14px · focus `border champagne` + ring champagne@30%
**Status chip** — JetBrains Mono 500 11px uppercase tracking .08em · padding 4px 10px · radius 9999px · bg = status colour @12% · text = status colour (darken if contrast fails)
**Table** — header `bg sand`, mono 11px uppercase warm · rows 44px, `border-bottom rule`, hover `bg offwhite` · numeric columns right-aligned in mono
**KPI tile** — value Playfair 36px ink · label above in mono 11px uppercase warm · delta below in mono 12px in status colour · no chart junk, no gradient, no shadow

---

# 4. APP SHELL — on every screen

```
┌────────────────────────────────────────────────────────────────────────┐
│ B_luePrint   [ ⌘K  Buscar o escribir un comando…    ]  ⚡ Glitch  ◐  EM │
└────────────────────────────────────────────────────────────────────────┘
```

1. **Wordmark** — `B_` + underlined `luePrint`, Playfair Display. Links to Hoy.
2. **Command Bar (⌘K)** — universal search + command palette. Searches every registry, ticket, task, template, contact, manual and person. Typing a verb (`nuevo glitch`, `añadir contacto`) offers the action directly. **Must actually work in the prototype.**
3. **⚡ Glitch** — persistent one-click reporting from any screen. **Never removed from any screen.**
4. **◐ Copilot** — opens the right-hand assistant panel with current screen as context.
5. **Account menu** — profile, office switch (T4), ES/EN, sign out.

Sidebar:

```
┌──────────────────┐
│ 01  Hoy        ▌ │   ← active: bg sand + 2px champagne left border
│ 02  Glitches     │
│ 03  Tareas       │
│ 04  Desempeño    │
│ 05  Equipo       │
│ 06  Legal        │
│ 07  Biblioteca   │
│ 08  Directorio   │
│ ───────────────  │
│ CRM ↗            │   ← opens external system, new tab
│ Academia ↗       │
│ ───────────────  │
│ ⚙  Administración│   ← T3/T4 only
└──────────────────┘
```

Numbers in JetBrains Mono `--warm`; labels Inter 400 `--ink`.

The two `↗` items are **launch links to external systems, not modules.** Nothing from the CRM or the training academy is reproduced inside this app — no lead pipelines, no campaigns, no message threads, no lesson content, no video players. If a screen you're designing starts to look like a CRM or an LMS, it's wrong.

---

# 5. SCREENS

Build all of these as working, navigable screens.

## Screen 01 — HOY

The landing screen and daily anchor. Answers *what needs me today?*

```
┌──────────────────────────────────────────────────────────────────────┐
│  01 — MIÉRCOLES 26 DE AGOSTO                                          │
│  Buenos días, Elena                       ← Playfair 36px             │
│                                                                       │
│  ┌──── REVISIÓN DIARIA DE GLITCHES ──────────────────────────┐       │
│  │  4 de ayer · 2 sin recuperar · 1 arrastrado (3 días)       │       │
│  │                                                            │       │
│  │  ● Cliente esperó 40 min en oficina      Recepción   🔴    │       │
│  │  ● Reporte enviado con precio erróneo    Ventas      🟡    │       │
│  │  ● Llaves no disponibles para visita     Operaciones 🟡    │       │
│  │  ● Correo de bienvenida sin adjunto      Admin       🟢    │       │
│  │                                                            │       │
│  │                  [ Abrir revisión diaria → ]               │       │
│  └────────────────────────────────────────────────────────────┘       │
│                                                                       │
│  ┌─ MIS TAREAS (6) ─────────┐  ┌─ REQUIERE ATENCIÓN (3) ───────┐    │
│  │ ☐ Renovar póliza     HOY │  │ ⚠ Lic. corredor — M. Restrepo │    │
│  │ ☐ Enviar reporte Q3   2d │  │   vence en 24 días            │    │
│  │ ☐ Revisar contrato    4d │  │ ⚠ Contrato limpieza           │    │
│  │ ☐ Actualizar CV       5d │  │   renueva automático en 15d   │    │
│  │        [ Ver todas → ]   │  │ 🔴 Licencia Adobe vencida     │    │
│  └──────────────────────────┘  └───────────────────────────────┘    │
│                                                                       │
│  ┌─ MIS INDICADORES ────────────────────────────────────────────┐    │
│  │   12           94%          3.2 días         4.6/5           │    │
│  │   Tareas       Glitches     Tiempo de        Satisfacción    │    │
│  │   a tiempo     recuperados  respuesta        cliente         │    │
│  │   ▲ +2         ▲ +6 pts     ▼ -0.4           ▲ +0.2          │    │
│  └──────────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────────┘
```

The glitch panel is **always first**. KPI numerals Playfair 36px, labels mono 11px uppercase, deltas mono 12px in status colours.

---

## Screen 02 — REVISIÓN DIARIA (the morning meeting)

**This screen *is* the meeting.** Design it to be projected on a screen while people talk through it.

```
┌──────────────────────────────────────────────────────────────────────┐
│  02 — REVISIÓN DIARIA                    [ Ayer ▾ ]  [ Presentar ⛶ ] │
│  Miércoles 26 de agosto                                               │
│                                                                       │
│  ┌──────────┬──────────┬────────────┬──────────────────────┐        │
│  │    4     │    2     │     1      │        87%           │        │
│  │Reportados│   Sin    │Arrastrados │    Recuperados       │        │
│  │  ayer    │recuperar │ (>2 días)  │    este mes          │        │
│  └──────────┴──────────┴────────────┴──────────────────────┘        │
│                                                                       │
│  ── RECEPCIÓN ──────────────────────────────── Resp.: Coord. ──      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ 🔴  Cliente esperó 40 minutos en oficina                    │    │
│  │     Cliente: J. Restrepo · Reportado 25 ago 16:20 · Día 2   │    │
│  │                                                              │    │
│  │     Qué pasó       La visita no quedó registrada en agenda  │    │
│  │     Recuperación   ⚠ Pendiente                               │    │
│  │     Cliente OK     ⚠ Pendiente                               │    │
│  │                                                              │    │
│  │     [ Registrar recuperación ] [ Asignar ] [ Cerrar ]        │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                       │
│  ── VENTAS ─────────────────────────────────── Resp.: Gerente ──     │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │ 🟡  Reporte enviado con precio desactualizado               │    │
│  │     Cliente: M. Chen · Reportado 25 ago 11:05 · Día 1       │    │
│  │                                                              │    │
│  │     Recuperación   ✓ Llamada + reporte corregido en 2h      │    │
│  │     Cliente OK     ✓ Confirmado por el cliente               │    │
│  │     Prevención     Plantilla ahora extrae precio del sistema│    │
│  │                                                  [ Cerrar ]  │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                       │
│  ⓘ Un glitch permanece aquí hasta que se registre la recuperación.   │
│    Nada se pierde entre las grietas.                                 │
└──────────────────────────────────────────────────────────────────────┘
```

**Rules that must be visible in the design:**
- Grouped **by responsible department** so each head speaks to their own block.
- Open glitches **roll forward daily** with a day counter until closed.
- Cannot close without a recovery action and an explicit client-made-whole answer — the `[ Cerrar ]` button is **disabled** until both are filled.
- **There is no "who is at fault" field. Anywhere.** Do not add one.
- `[ Presentar ⛶ ]` = full-screen presentation mode: larger type, one department at a time, keyboard arrows to advance. Design this state.

---

## Screen 03 — REPORTAR UN GLITCH (modal, from anywhere)

Must be completable in **under 20 seconds** or people stop using it.

```
        ┌────────────────────────────────────────────────┐
        │  REPORTAR UN GLITCH                        ✕   │
        │                                                 │
        │  Sin culpa. Solo mejoramos.  ← Playfair italic │
        │                                                 │
        │  ¿Qué pasó?                                     │
        │  ┌───────────────────────────────────────────┐ │
        │  │ Una línea es suficiente…                  │ │
        │  └───────────────────────────────────────────┘ │
        │                                                 │
        │  Gravedad    ( 🟢 Menor )( 🟡 Media )( 🔴 Alta )│
        │  Tipo        ( Experiencia )( Producto )        │
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

**Only the description is required.** Everything else optional or auto-captured. On submit: modal closes, a quiet confirmation toast appears — *"Gracias. Lo revisamos mañana."* No celebration animation, no confetti. Calm.

---

## Screen 04 — PANEL DE GLITCHES

```
┌──────────────────────────────────────────────────────────────────────┐
│  02 — GLITCHES         [ Revisión diaria ][ Panel ▌][ Todos ]        │
│  Panel de patrones                        [ Últimos 90 días ▾ ]      │
│                                                                       │
│  ┌──────────┬──────────┬────────────┬─────────────────────────┐     │
│  │    47    │   87%    │  1.4 días  │          12             │     │
│  │Reportados│Recuperad.│ Tiempo de  │  Reportados por persona │     │
│  │          │          │ recuperac. │       (promedio)        │     │
│  │  ▲ +11   │ ▲ +9 pts │  ▼ -0.6    │   ▲ +3   ✓ saludable    │     │
│  └──────────┴──────────┴────────────┴─────────────────────────┘     │
│                                                                       │
│  ── PATRONES RECURRENTES ────────────────────────────────────        │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  8×  Agenda de visitas no sincronizada   ▓▓▓▓▓▓▓▓ Recepción │    │
│  │  6×  Precio desactualizado en documentos ▓▓▓▓▓▓   Ventas    │    │
│  │  5×  Documento faltante en expediente    ▓▓▓▓▓    Operac.   │    │
│  │  3×  Retraso en respuesta > 24h          ▓▓▓      Admin     │    │
│  │                                                              │    │
│  │  ◐ Copilot: los 8 glitches de agenda ocurren cuando la      │    │
│  │    visita se agenda desde el CRM en lugar de la agenda      │    │
│  │    compartida. Un cambio de proceso resolvería el 17% de    │    │
│  │    todos los glitches del trimestre.                        │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                       │
│  ── POR DEPARTAMENTO ──────────  ── POR ETAPA DEL CLIENTE ────       │
│  Recepción      ▓▓▓▓▓▓▓▓ 14     Primer contacto ▓▓▓      6          │
│  Ventas         ▓▓▓▓▓▓   11     Visita          ▓▓▓▓▓▓▓▓ 15         │
│  Operaciones    ▓▓▓▓▓     9     Negociación     ▓▓▓▓     8          │
│  Administración ▓▓▓▓      8     Cierre          ▓▓▓▓▓    10         │
│  Marketing      ▓▓         5     Post-venta      ▓▓▓▓     8          │
│                                                                       │
│  ⓘ Un equipo que reporta cero glitches no es un equipo perfecto.     │
│    Es un equipo que dejó de reportar.                                │
└──────────────────────────────────────────────────────────────────────┘
```

**Design rule:** "Reportados por persona" is a **health signal with a healthy floor**, shown positively — never as a negative metric. Recovery rate and recovery time are the performance measures. The footer note is permanent copy, not placeholder text. Bars are simple hairline-bounded fills in `--sand` with a `--champagne` fill — no gradients, no chart library ornament.

---

## Screen 05 — TAREAS

```
┌──────────────────────────────────────────────────────────────────────┐
│  03 — TAREAS               [ Mías ▌][ Equipo ][ Todas ]  [ + Nueva ] │
│  [ 🔍 Filtrar ] [ Responsable ▾ ] [ Origen ▾ ] [ Estado ▾ ]          │
│                                                                       │
│  ── VENCIDAS (1) ───────────────────────────────────────────         │
│  ☐  Renovar licencia de Adobe          🔴 -3d   Admin    ⟵ Legal     │
│                                                                       │
│  ── HOY (2) ────────────────────────────────────────────────         │
│  ☐  Renovar póliza de responsabilidad   Hoy    Coord.    ⟵ Legal     │
│  ☐  Registrar recuperación — J. Restrepo Hoy   Recepción ⟵ Glitch    │
│                                                                       │
│  ── ESTA SEMANA (3) ────────────────────────────────────────         │
│  ☐  Enviar reporte trimestral            2d    Gerente               │
│  ☐  Revisar contrato de limpieza         4d    Coord.    ⟵ Legal     │
│  ☐  Actualizar CV en expediente          5d    RRHH      ⟵ Equipo    │
│                                                                       │
│  ── MÁS ADELANTE (6) ──────────────────────────────  [ Ver → ]       │
└──────────────────────────────────────────────────────────────────────┘
```

The `⟵` badge shows **provenance** — most tasks are *generated* by other modules (an expiring licence, an unrecovered glitch, a missing CV), not typed by hand. Clicking it opens the source record. Make this badge clearly clickable; it's what makes the registries feel alive rather than decorative.

---

## Screen 06 — DESEMPEÑO

```
┌──────────────────────────────────────────────────────────────────────┐
│  04 — DESEMPEÑO   [ Personal ▌][ Equipo ][ Satisfacción ][ Reportes ]│
│                                              [ Este trimestre ▾ ]    │
│  ── MIS INDICADORES ────────────────────────────────────────         │
│  ┌──────────┬──────────┬──────────┬────────────────────────┐        │
│  │   94%    │  1.2d    │   100%   │        4.6 / 5         │        │
│  │ Tareas a │Tiempo de │Registros │  Satisfacción cliente  │        │
│  │  tiempo  │recuperac.│  al día  │                        │        │
│  │ ▲ +6 pts │ ▼ -0.4d  │   = 0    │        ▲ +0.2          │        │
│  └──────────┴──────────┴──────────┴────────────────────────┘        │
│                                                                       │
│  ── TENDENCIA ──────────────────────────────────────────────         │
│  100% ┤                                        ╭──────               │
│       │                      ╭────────╮   ╭────╯                     │
│   75% ┤       ╭──────────────╯        ╰───╯                          │
│       │  ╭────╯                                                       │
│   50% ┼──╯                                                            │
│       └───┬───────┬───────┬───────┬───────┬───────┬────              │
│          Jun     Jul     Ago     Sep     Oct     Nov                 │
│                                                                       │
│  ── ORIGEN DE LOS DATOS ────────────────────────────────────         │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  Tareas, glitches, registros   BluePrint     ✓ En vivo      │    │
│  │  Satisfacción del cliente      Encuestas     ✓ En vivo      │    │
│  │  Campañas y pipeline           CRM           ⟳ Import. 25ago│    │
│  │                                              [ Importar CSV ]│    │
│  └─────────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────────┘
```

**The "Origen de los datos" panel is a permanent UI element, not scaffolding.** Users must always know whether a number is live or imported, and when. Some metrics are generated inside BluePrint; CRM-sourced metrics arrive by CSV import in this version. Design the honesty in.

Charts: single-line, hairline grid in `--rule`, line in `--ink`, active point in `--champagne`. No area fills, no gradients, no legends where a label will do.

Team tab shows the same metrics per person, permission-scoped.

---

## Screen 07 — EQUIPO

```
┌──────────────────────────────────────────────────────────────────────┐
│  05 — EQUIPO   [ Personas ▌][ Casos ][ Licencias ][ Bienestar ]      │
│  [ 🔍 Buscar ]                                      [ + Persona ]    │
│                                                                       │
│  NOMBRE           ROL            LICENCIAS       CV     ESTADO        │
│  ──────────────────────────────────────────────────────────────      │
│  M. Restrepo      Corredora      🟡 Vence 24d    ✓      Activa       │
│  A. Guerrero      Coordinadora   — n/a           🔴 Falta Activa     │
│  C. Molina        Asesor         🟢 Vigente      ✓      Activa       │
│  L. Paredes       Gerente        🟢 Vigente      ✓      Activa       │
│  D. Sarmiento     Asesor         🔴 Vencida      ✓      Suspendida   │
└──────────────────────────────────────────────────────────────────────┘
```

Person record:

```
┌──────────────────────────────────────────────────────────────────────┐
│  ← Equipo                                                             │
│  05 — EXPEDIENTE                                                      │
│  María Restrepo                            ← Playfair 36px            │
│  Corredora de bienes raíces · Activa desde mar 2024                   │
│                                                                       │
│  ┌─ LICENCIAS Y CERTIFICACIONES ──────────────────────────────┐      │
│  │  Licencia de corredor   [Autoridad] #4821  🟡 Vence 19 sep │      │
│  │                                      [ Registrar renovación]│      │
│  │  Certificación Academia  Nivel 2      🟢 Vigente            │      │
│  │                                      [ Ver en Academia ↗ ]  │      │
│  └────────────────────────────────────────────────────────────┘      │
│                                                                       │
│  ┌─ DOCUMENTOS ─────────────┐  ┌─ CONTRATO ──────────────────┐      │
│  │ 📄 CV          Drive ↗   │  │ Tipo      Indefinido         │      │
│  │ 📄 Contrato    Archivo ↗ │  │ Inicio    12 mar 2024        │      │
│  │ 📄 Identidad   Drive ↗   │  │ Revisión  12 mar 2027        │      │
│  └──────────────────────────┘  └─────────────────────────────┘      │
│                                                                       │
│  🔒 Casos de RRHH relacionados        Visible solo para Principal    │
└──────────────────────────────────────────────────────────────────────┘
```

**Casos tab** — HR cases. Confidential by default, supports anonymous submission. A case about a person is structurally invisible to that person regardless of seniority. Every case carries a persistent lock icon and an explicit visibility statement (*"Visible para: Principal, RRHH"*).

> **Critical tonal instruction:** glitches and HR cases share the same underlying engine but must look and feel **opposite**. The glitch screens are bright, open, low-friction, warm — reporting is encouraged. The HR case screens are quiet, private, formal, with visible confidentiality indicators and no encouragement language. Same components, deliberately different atmosphere. Show both so the contrast is legible.

**Bienestar tab** — curated links: psychologists, occupational health, legal aid, confidential helpline. Contact details and link-outs only. **No clinical data is ever stored here** — say so in the UI.

---

## Screen 08 — LEGAL

```
┌──────────────────────────────────────────────────────────────────────┐
│  06 — LEGAL Y ACTIVOS                                                 │
│  [ Contratos ▌][ Licencias ][ Software ][ Impuestos ][ Calendario ]  │
│                                                    [ + Registro ]    │
│  ── REQUIERE ATENCIÓN ──────────────────────────────────────         │
│  🔴  Licencia Adobe Creative Cloud    Venció hace 3 días   Admin     │
│  🟡  Contrato de limpieza             Renueva auto. en 15d Coord.    │
│  🟡  Licencia de corredor — M. R.     Vence en 24 días     RRHH      │
│                                                                       │
│  ── TODOS LOS CONTRATOS ────────────────────────────────────         │
│  REGISTRO             CONTRAPARTE     VENCE        VALOR    RESP.    │
│  ──────────────────────────────────────────────────────────────      │
│  Arrendamiento of.    Inmob. Central  31 dic 2027  $2,400/m Princ.  │
│  Contrato limpieza    ServiClean      15 sep 2026  $380/m   Coord.  │
│  Seguro responsab.    Aseguradora X   30 nov 2026  $1,200/a Princ.  │
│  Contabilidad ext.    Estudio contable Indefinido  $800/m   Princ.  │
│                                                                       │
│  ⓘ BluePrint registra estado, vencimiento y responsable.             │
│    Los documentos firmados viven en el archivo legal seguro. ↗       │
└──────────────────────────────────────────────────────────────────────┘
```

Every tab is the **same table component** with different columns. The footer note is permanent and load-bearing: this is a *tracker*, not a document archive. Signed files are linked, never stored.

**Calendario tab** — all expiry dates across every registry on one 12-month horizontal timeline. The "what's coming at us" view. Design this: months across the top, items as small chips positioned on their expiry date, colour-coded by status.

---

## Screen 09 — BIBLIOTECA

```
┌──────────────────────────────────────────────────────────────────────┐
│  07 — BIBLIOTECA      [ Plantillas ▌][ Manuales ][ Formación ]       │
│  [ 🔍 Buscar en toda la biblioteca ]                                  │
│                                                                       │
│  REPORTES PARA CLIENTES                                               │
│  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐           │
│  │ 📄             │ │ 📊             │ │ 📄             │           │
│  │ Reporte de     │ │ Proyección de  │ │ Informe de     │           │
│  │ mercado        │ │ inversión      │ │ avance de obra │           │
│  │                │ │                │ │                │           │
│  │ PDF · v2.1     │ │ XLSX · v3.0    │ │ PDF · v1.4     │           │
│  │ Rev. ago ✓     │ │ Rev. ago ✓     │ │ Rev. may 🟡    │           │
│  │ [Abrir][Copiar]│ │ [Abrir][Copiar]│ │ [Abrir][Copiar]│           │
│  └────────────────┘ └────────────────┘ └────────────────┘           │
│                                                                       │
│  REPORTES PARA DIRECCIÓN      ▸ 4 plantillas                         │
│  CONTRATOS Y LEGAL            ▸ 9 plantillas                         │
│  CORREOS                      ▸ 12 plantillas                        │
│  FINANCIERO Y PROYECCIONES    ▸ 6 plantillas                         │
│  MARCA Y MARKETING            ▸ 8 plantillas                         │
│                                                                       │
│  ⓘ Los archivos viven en Drive. BluePrint controla versión,          │
│    aprobación y fecha de revisión.                                    │
└──────────────────────────────────────────────────────────────────────┘
```

A template past its review date shows 🟡 and generates a task. **Manuales** = searchable operating procedures, the Copilot's main knowledge source. **Formación** = link-outs to the training academy with completion status — **lessons never render inside this app.**

---

## Screen 10 — DIRECTORIO

```
┌──────────────────────────────────────────────────────────────────────┐
│  08 — DIRECTORIO                                   [ + Contacto ]    │
│  [ 🔍 Buscar ] [ Categoría ▾ ]                                        │
│                                                                       │
│  CONTABILIDAD Y FINANZAS                                              │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  Estudio Contable Asociados       Contabilidad externa      │    │
│  │  Contacto principal · +000 0000-0000 · correo@ejemplo.com   │    │
│  │  ⓘ Cierre mensual antes del día 5. Contrato activo ⟶ Legal  │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                       │
│  LEGAL                                                                │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  Bufete Asociados                 Corporativo e inmobiliario│    │
│  │  Contacto principal · +000 0000-0001 · correo@ejemplo.com   │    │
│  │  ⓘ Consultas de contratos de compraventa                    │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                       │
│  ▸ AUTORIDADES Y REGISTROS                                            │
│  ▸ PROVEEDORES         (limpieza, TI, seguros, imprenta)              │
│  ▸ SITIOS ÚTILES       (portales, tasas, herramientas)                │
│  ▸ BIENESTAR           ⟶ Equipo → Bienestar                           │
└──────────────────────────────────────────────────────────────────────┘
```

The `⟶ Legal` cross-link matters: the accountant's directory entry links to the active contract, which links to its renewal task, which appears on Hoy. Make these connections visible.

---

## Screen 11 — COPILOT

Right-hand panel on every screen, plus a full-screen view.

```
┌──────────────────────────────────────────────────────────────────────┐
│  ◐ COPILOT                                                      ✕   │
│  Contexto: Panel de glitches · Últimos 90 días                       │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  ¿Qué licencias vencen en los próximos 60 días?             │    │
│  └─────────────────────────────────────────────────────────────┘    │
│                                                                       │
│  Tres licencias vencen antes del 25 de octubre:                      │
│                                                                       │
│  • Licencia de corredor — M. Restrepo · 19 sep                       │
│  • Antivirus corporativo · 03 oct · 12 puestos                       │
│  • Permiso de operación · 21 oct                                     │
│                                                                       │
│  La licencia de Adobe ya está vencida (23 ago).                      │
│                                                                       │
│  📎 Fuentes  Legal → Licencias (3) · Equipo → M. Restrepo            │
│  🕐 Datos al 26 ago 2026, 08:14                                       │
│                                                                       │
│  [ Crear tareas de renovación ]   ← requiere confirmación            │
│  ─────────────────────────────────────────────────────────────       │
│  Sugerencias                                                          │
│  · Resumir los glitches de esta semana                               │
│  · ¿Dónde está la plantilla de proyección?                           │
│  · ¿Cuál es el proceso para dar de alta a un empleado?               │
│  ─────────────────────────────────────────────────────────────       │
│  [ Preguntar…                                              ] [ → ]   │
└──────────────────────────────────────────────────────────────────────┘
```

**Every answer must show its sources and a data timestamp.** Actions the assistant proposes require an explicit confirmation step — design the preview-then-confirm state. The assistant can explain, summarise, draft and prepare; it can never approve, sign, pay or waive a control.

---

## Screen 12 — ADMINISTRACIÓN

Tabs: **Usuarios y permisos** · **Oficinas** · **Integraciones** · **Definiciones de indicadores** · **Registro de auditoría**.

"Definiciones de indicadores" is where a KPI's formula, period, source and owner are declared — design it as a proper editable registry, not a settings afterthought.

---

# 6. STATES — design all of these

For every screen:

- **Empty state** — Playfair headline, one line of Inter guidance, one primary action. Warm and human, never a shrug. E.g. *"Ningún glitch reportado ayer."* + *"Eso puede ser una buena señal — o una señal de que dejamos de reportar."* + `[ Reportar un glitch ]`
- **Loading** — subtle skeleton rows in `--sand`. No spinners, no progress bars.
- **Error** — inline, `--status-critical`, plain language, with a retry action.
- **Permission-denied** — explain *why* the user can't see something rather than hiding it silently, except for confidential HR cases which must be genuinely invisible.
- **Disabled action** — e.g. the `[ Cerrar ]` button on an unrecovered glitch. Show *why* it's disabled on hover.

---

# 7. MOCK DATA — make it functional

Populate with realistic demo data so the prototype is genuinely usable. **Use invented names only** — no real staff names. Roughly:

- **12 glitches** across 90 days, various departments, some recovered, two unrecovered and rolling forward, one at day 3
- **8 tasks** — one overdue, two today, three this week, two later; at least four with provenance badges
- **5 people** with varied licence states (one expiring in 24 days, one expired, one missing CV)
- **14 registry records** across contracts, corporate licences, software, taxes — three needing attention
- **6 template categories**, ~12 templates, one past review date
- **12 directory entries** across 5 categories
- **90 days of KPI data** for trend charts
- **3 HR cases**, one anonymous, all confidential

The prototype should be **clickable end to end**: report a glitch → it appears on tomorrow's review → record recovery → it closes → the pattern dashboard updates. Filters, tabs, search and the command palette should actually work within the session.

---

# 8. MOTION — restrained

Motion here is not a product claim; **speed is.** The tool must feel instant.

**Allowed:**
- 120–180ms ease-out on hover, focus, and state changes
- 200ms fade + 8px rise for modals and panels
- Skeleton shimmer while loading
- Tab and route changes: 150ms crossfade, no movement
- Chart lines drawing once on first render, ~400ms

**Forbidden:**
- Scroll-linked animation of any kind
- Pinned sections, parallax, magnetic cursors, hand-drawn line effects
- Count-up numbers on every render (once on first load at most — and even then, prefer not)
- Any transition over 300ms
- Bounce, spring or elastic easing
- Page-load animations that delay usable content

Respect `prefers-reduced-motion` — collapse everything to instant.

> If the interface ever makes a user *wait* for an animation to finish before they can act, it is wrong.

---

# 9. RESPONSIVE

| Breakpoint | Behaviour |
|---|---|
| **≥1440 desktop** | Full experience. Sidebar 240px. Primary target — this is a desk tool. |
| **1024–1439** | Same; sidebar collapses to a 64px icon rail. |
| **768–1023 tablet** | Sidebar becomes a slide-over. Tables scroll horizontally with a sticky first column. KPI tiles 2-up. |
| **<768 mobile** | Bottom sheet navigation. Tables become stacked cards. **Report a Glitch must remain one tap away** — it is the one thing people will do from a phone. |

Desktop-first. Mobile must work but is not the primary case — except for glitch reporting.

---

# 10. TECHNICAL NOTES

- **Stack:** React + Tailwind + TypeScript. Tailwind config should map the tokens in §3 to named theme values (`bone`, `sand`, `ink`, `warm`, `champagne`, status colours) so no hex codes appear in components.
- **Fonts:** Google Fonts link in §3.
- **State:** client-side is fine for the prototype; interactions must persist within a session.
- **Icons:** a single thin-stroke set (Lucide or similar), 1.5px stroke, never filled, always `--warm` or `--ink`.
- **Accessibility:** WCAG AA throughout, full keyboard navigation, visible focus states using the champagne ring, correct heading hierarchy, labelled form fields. The champagne rule in §3 is a hard gate.
- **Language:** Spanish UI, strings in a locale file so English can be added without layout changes.
- **Naming:** `BluePrint` should live as a config variable — trademark clearance isn't complete.

---

# 11. WHAT TO DELIVER

1. All 12 screens, desktop, fully populated with mock data and clickable.
2. The Daily Review screen **in both normal and presentation mode**.
3. The Report-a-Glitch modal and its full flow through to recovery and closure.
4. The Equipo module showing both the open glitch tone and the confidential HR case tone, so the contrast is visible.
5. The Copilot panel including the propose-then-confirm action state.
6. Empty, loading, error and disabled states for at least four screens.
7. Component library sheet: buttons, inputs, cards, tables, status chips, KPI tiles, eyebrow+heading pattern, modal, side panel, command palette.
8. Tablet and mobile views for Hoy, Revisión Diaria and Report-a-Glitch.

---

# 12. THE ONE-SENTENCE TEST

> A back-office coordinator should open this every morning without being asked, find what needs them in under five seconds, and feel that the company they work for is a serious, well-run place.

If a design decision doesn't serve that sentence — especially if it's beautiful but slows someone down — cut it.
