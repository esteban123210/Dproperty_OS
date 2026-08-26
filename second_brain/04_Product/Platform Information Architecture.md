---
project: B_RealEstate
title: "Platform Information Architecture"
type: product_spec
status: Supporting Draft v0.6
version: 0.6
owner: Esteban
last_updated: 2026-08-16
source: Claude working session 2026-07-18
tags: [product, architecture, platform, wireframe, information-architecture]
---

# Platform Information Architecture

> **Naming and scope update (2026-08-16):** The platform is **BluePrint**, part of **B_RealEstate**. GoHighLevel remains the CRM, Open edX the Academy technology, and VAULTED the off-market marketplace. The canonical boundaries live in [[../18_Ecosystem/00 - Ecosystem Master Map]] and [[../18_Ecosystem/12 - System of Record and Integration Matrix]].

> **Precedence update (2026-08-16):** [[BluePrint Product Constitution]] controls the product boundary and [[BluePrint Golden Workflow - Wireframe and Validation]] controls the MVP journey. This file remains supporting information architecture for the wider public/logged-in ecosystem.
>
> Companion notes: [[BluePrint Product Map]], [[Platform Scenario Playbook]] (72+ scenarios), and [[Roles and Access Matrix]] (hierarchy and permissions).

> ## ⚠ Scope redirection — 2026-08-26 (read this before Layer 2 below)
>
> [[BluePrint Product Constitution]] v2.0 confirms BluePrint as the **back-office brain for administrative staff only** and sequences delivery into **Release 1 (Back Office Brain)** and **Release 2 (Transaction Spine)**.
>
> **What survives from this document and is now canonical:** Principle 1 (three clicks to anything, Command Bar), Principle 2 (deterministic core / governed Copilot, T0–T2 routing), the Glitch Report system, the People/HR and Cases systems, the Audit/Data Governance system, the file-storage rules, Layer 1 (public site) and the franchisee lifecycle. The 2026-07-18 architecture was correct; Constitution v1.0 had narrowed it away and v2.0 restores it.
>
> **What changed:**
>
> | 2026-07-18 position | 2026-08-26 position |
> |---|---|
> | ~25 OS modules including embedded CRM and embedded Academy | ~9 nav items. CRM and Academy are **launch links only** — never embedded, never rendered inside BluePrint (Constitution §2 non-duplication rendering rule) |
> | Everyone in a franchise office logs into the OS | **Administrative staff only.** Sales advisors use GoHighLevel and receive no BluePrint seat (Constitution §3.11) |
> | Cases and Glitch Report as two separate engines | One **Ticket** primitive, two configurations with deliberately opposite UI tone. Same for the six registries, which share one **Registry** primitive (Constitution §3.13) |
> | Field Mode (mobile) for in-meeting advisors | Removed — that user is now a CRM user |
> | Resource Library + Support/Help Desk as distinct systems | Absorbed into the Registry and Ticket primitives |
>
> **The Release 1 navigation is:** Today · Glitches · Tasks · Performance · People · Legal · Library · Directory · Administration, with Command Bar, Report a Glitch and Copilot on every screen. Release 2 adds Transactions, Documents and Finance to this shell rather than replacing it.
>
> **The binding Release 1 build specification — design system, screens, primitives, permissions, build order — is [[BluePrint Wireframe - Back Office OS (Developer Handoff)]].** Where that document and the Layer 2 inventory below disagree, the Wireframe wins.

---

## The two design principles (these drive every decision)

### Principle 1 — "Three clicks to anything" (the North Star)
One login. A persistent **Command Bar** (top of every screen) + a **Launcher grid** (home). Type or click → land on the file, contact, price, projection, template, brochure, external site, or CRM record. External links are fine **as long as they open from inside the OS** and feel like one ecosystem (SSO, no re-login).

> If you work with us, you log into our site and within a few clicks you reach anything in our ecosystem — files, contacts, websites, information, prices, projections, templates, anything.

### Principle 2 — Deterministic core, governed Copilot

BluePrint includes the Copilot from MVP, but it does not turn deterministic workflow into probabilistic workflow. Route each task to the lowest-cost reliable mechanism:

| Tier | Mechanism | Handles |
|---|---|---|
| **T0 — Deterministic** | Forms, rules, search index, templates, workflow services and calculations | Filing/routing, stage gates, document assembly, commissions, dashboards and audit |
| **T1 — Cost-efficient GPT** | Permission-filtered retrieval, classification, extraction and summaries | Q&A over approved knowledge, transaction summaries, missing-item explanations |
| **T2 — Stronger GPT** | Controlled complex drafting/analysis | Approved-template document drafts and management narratives |

**Hard rules:**

- Deterministic rules own filing, routing, calculations, stage gates and audit.
- AI may prepare a low-risk record action only with preview, explicit confirmation and authorization.
- AI never approves, signs, pays, publishes templates, waives controls or makes regulated decisions.
- Tenant/role/record permissions are enforced before retrieval and tool execution.
- Company/process/metric answers cite sources, definitions and period.

See [[BluePrint Product Constitution]] §11 and [[AI Layer Notes]].

---

## The core architecture: two layers, one door

```
LAYER 1 — PUBLIC SITE (no login)   → storefront / brand / recruitment
LAYER 2 — THE OS (after login)     → operating platform, role-gated
        └ single login link for everyone in a franchise office
        └ what you SEE is filtered by your ROLE, not by a different URL
```

Everyone in a franchisee's office uses **one login link**. Role decides what loads (see [[Roles and Access Matrix]]).

---

## Layer 1 — Public site (pre-login): ~14 pages

### Main public site (~8 pages)
| # | Page | Purpose |
|---|------|---------|
| 1 | Home | Positioning, hero, proof, dual CTA (client vs franchise) |
| 2 | About Us / Who We Are | Story, team, mission & vision |
| 3 | Services | Buyers, sellers, investors, developers |
| 4 | Private Collection (teaser) | Curated inventory, gated — "request access" |
| 5 | Projects / Listings (optional) | Public catalog, feeds leads into CRM |
| 6 | Contact / Book a call | Routes into GoHighLevel |
| 7 | Login / Portal entry | Door to Layer 2 |
| 8 | Legal | Privacy, terms, disclaimers |

### "Become a Franchise" recruitment hub (~7 pages) — the growth engine
| # | Page | Purpose |
|---|------|---------|
| 1 | Why Dproperty | Value proposition (OS + CRM + Academy + brand + AI team included) |
| 2 | Your Path (Roadmap) | Discover → Apply → Sign → Onboard → Launch timeline |
| 3 | Investment & Returns | Fees, what's included, sample unit economics |
| 4 | What's Included | Platform, CRM, academy, brand, support, AI agents |
| 5 | Territories | Map of available/taken |
| 6 | Proof | Case studies, testimonials, numbers |
| 7 | FAQ | Financing, risk, timeline, exclusivity |

Every recruitment page carries **Book a Call** + **Download Info Pack** (email-gated → drops into CRM nurture).

**Two separate CRM pipelines:** *property buyers* vs *franchise prospects*. Never mix them.
**Prep Pack automation:** booking a call auto-sends agenda + info pack + short video (conversion multiplier).

---

## Layer 2 — The OS (post-login): ~25 modules

### Two always-on top-bar elements (on every screen)
1. **Command Bar** — universal search + command palette (the "three clicks to anything").
2. **Report a Glitch** — one-click, no-blame improvement reporting (see Glitch system below).

### Core operating modules (from [[Prototype Spec]] + additions)
HQ Control Center · Franchise Workspace Home · Clients · Brokers · Developers · Projects · Units · Deals · Document Generator · Projection Generator · Private Collection · Developer Sales Dashboard · Finance / Commission · Settings / Permissions

### Modules added by this session
- **Resource Library** — templates, brochures, brand assets (surfaced from Drive, **not re-hosted**)
- **Learning / Academy** — embedded LMS (Open edX), SSO, gated certifications
- **CRM & Marketing** — embedded, white-labeled GoHighLevel, SSO
- **AI Assistant** — the T1 agent layer
- **Support / Help Desk** — tickets to HQ, knowledge base
- **Field Mode (mobile)** — stripped in-meeting/offline view (inventory, prices, media, contacts, NDA generator)
- **Franchise Sales Room** (HQ role) — full pitch package in one place for closing franchises
- **Data Room generator** — per-prospect shareable personalized microsite

### Six back-office systems
| System | Purpose |
|--------|---------|
| **Finance / Back Office** | Commissions, royalties, invoices, payments, reimbursements, refunds, reconciliation, close. OS records; payment provider moves money. |
| **People / HR** | Users, roles, contracts, leave, payslips, reviews, on/offboarding, self-service "My Profile" |
| **Cases / Ticketing** | One engine for complaints, grievances, claims, disputes, escalations, whistleblower. **Case type controls visibility + routing + SLA.** |
| **Tenant Lifecycle** (in HQ Control Center) | Provision → audit → wind-down a franchise |
| **Audit Log & Data Governance** | Immutable trail, data requests, security flags |
| **Glitch Report** | No-blame, transparent, fast continuous-improvement reporting (Four Seasons model) |

---

## Embedding strategy: CRM & Academy (hybrid — embed + SSO)

| System | Recommendation | Why |
|--------|---------------|-----|
| **GoHighLevel (CRM)** | White-label + embed via iframe/SSO inside "CRM & Marketing" | GHL is built for white-label reselling; franchisee never sees "GoHighLevel" |
| **Open edX (Academy)** | White-label + SSO, embed course player; deep-link for full LMS | Selected Academy engine. Onboarding should feel native and certifications must gate relevant BluePrint permissions/workflows. |

**Single sign-on is the glue.** One login to the OS carries into CRM and Academy without re-auth. The OS is the **hub/launcher**; GoHighLevel and Open edX are **connected engines behind it**.

---

## File storage: stored in Drive, accessed through the OS (never duplicated)

Extends [[File Storage Rules]]. The OS is the single pane of glass.

| Thing | Stored in | Surfaced in OS as |
|-------|-----------|-------------------|
| Blank templates (contracts, NDAs) | Template Control (governed) | Document Generator pulls them |
| Brochures / brand assets / decks | SharePoint/Drive | Resource Library (links + preview) |
| Signed / legal documents | Secure legal archive | Linked from the Deal, read-only |
| Generated docs & projections | OS document store | Attached to the Deal |
| Structured operational data (party references, units, transactions) | BluePrint database | Source of truth only for BluePrint-owned fields; CRM-owned fields retain provenance |

---

## The Glitch Report system (Four Seasons model)

Separate from the Cases engine — different tone, visibility, and goal.

| | Cases engine | Glitch Report |
|---|---|---|
| Trigger | Something went wrong for a person; needs resolution | Anyone notices anything imperfect |
| Tone | Formal, accountable, SLA-bound | No-blame, low-friction, "help us improve" |
| Visibility | Confidential, role-gated | Transparent — visible to everyone |
| Goal | Resolve the case | Spot patterns → continuously improve |

**Design:**
- Persistent **"Report a Glitch"** button on every screen + Field Mode.
- Near-zero friction: one line + auto-captured context (page, module, role, tenant, timestamp) + optional screenshot + severity mood (🟢/🟡/🔴).
- Two light tags: **Product glitch** (bug/UX) or **Experience glitch** (service/operation).
- **Glitch Feed:** network-wide live board of reported → in-progress → fixed (✅ + one-line "what we changed").
- **No-blame at the schema level:** glitches are never person-attributed.
- **AI (T1 only):** auto-categorize, de-duplicate/cluster, weekly "top 5 recurring" summary. Never resolves.
- Feeds HQ's improvement backlog → the loop that makes the ecosystem compound in quality.

---

## Franchisee lifecycle → login state

```
DISCOVER → APPLY → SIGN → ONBOARD → LAUNCH → OPERATE → GROW
```
- **Discover / Apply** = public site (Layer 1)
- **Sign** = legal archive
- **Onboard → Grow** = inside the OS (Layer 2), role-gated

---

## System count (current)
- **~14 public pages** (8 main + 7 recruitment hub, minus shared)
- **~25 OS modules**
- **6 back-office systems:** Finance, People/HR, Cases, Tenant Lifecycle, Audit/Data Governance, Glitch Report
- **2 always-on top-bar elements:** Command Bar + Report a Glitch

---

## Next steps
1. ✅ Save architecture (this note + [[Platform Scenario Playbook]] + [[Roles and Access Matrix]])
2. Wireframe priority screens first (Public Home, Franchise Workspace Home, Deal Detail, Resource Library, Command Bar, Glitch Report) — not all 25 at once
3. Wireframes → Figma (per [[Figma Handoff Notes]] and [[File Storage Rules]])

## Related
- [[BluePrint Product Map]] · [[BluePrint Product Constitution]] · [[BluePrint Golden Workflow - Wireframe and Validation]] · [[Product Vision]] · [[Product Modules]] · [[Prototype Spec]] · [[MVP Scope]] · [[Data Model]] · [[AI Layer Notes]]
- [[GoHighLevel Role]] · [[Training Academy Outline]] · [[File Storage Rules]]
