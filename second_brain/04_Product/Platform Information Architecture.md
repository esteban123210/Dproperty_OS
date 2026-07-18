---
project: Dproperty OS
title: "Platform Information Architecture"
type: product_spec
status: Draft v0.5
version: 0.5
owner: Esteban
last_updated: 2026-07-18
source: Claude working session 2026-07-18
tags: [product, architecture, platform, wireframe, information-architecture]
---

# Platform Information Architecture

> Parent document for the Dproperty OS platform wireframe. Sits one layer **above** [[Prototype Spec]] (which defines screens) and defines the whole ecosystem: public site + logged-in OS + how CRM/Academy/files plug in + who does what.
>
> Companion notes: [[Platform Scenario Playbook]] (72+ tested scenarios) and [[Roles and Access Matrix]] (hierarchy, human/AI split, agent pricing).

---

## The two design principles (these drive every decision)

### Principle 1 — "Three clicks to anything" (the North Star)
One login. A persistent **Command Bar** (top of every screen) + a **Launcher grid** (home). Type or click → land on the file, contact, price, projection, template, brochure, external site, or CRM record. External links are fine **as long as they open from inside the OS** and feel like one ecosystem (SSO, no re-login).

> If you work with us, you log into our site and within a few clicks you reach anything in our ecosystem — files, contacts, websites, information, prices, projections, templates, anything.

### Principle 2 — "Automation first, AI second" (cost control)
Most of what the platform does is **not** generative AI — it's forms, search, templating, and file-routing, which are deterministic and free. Route every task to the cheapest tier that does the job:

| Tier | Tech | Cost | Handles |
|------|------|------|---------|
| **T0 — No AI** | Forms, rules, search index, mail-merge templating, file-naming automation (Make / n8n / Power Automate) | ~$0 | ~85% of daily tasks: registering, filing, finding, generating docs from templates, dashboards, payments |
| **T1 — Cheap/Local AI** | DeepSeek local, or cheap batch API | ~$0 | Writing a listing description, summarizing, extracting data from a messy PDF, Q&A over own files (RAG), categorizing tickets |
| **T2 — Premium AI** | Optional add-on | Paid | Rare heavy reasoning; sold as upsell |

**Hard rules:**
- AI never **files, names, or routes** anything — rules do.
- AI never **calculates, approves, pays, or deletes** — humans + deterministic logic do.
- AI only **writes language** (drafts, summaries, extraction, Q&A).

This keeps the platform deterministic (critical for legal/financial), cheap, and consistent with [[AI Layer Notes]] and the "data first, documents second" principle in [[Product Vision]].

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
- **Learning / Academy** — embedded LMS (LearnWorlds/edX), SSO, gated certifications
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
| **LearnWorlds / edX (Academy)** | White-label + SSO, embed course player; deep-link for full LMS | Onboarding feels native, gated to certifications. LearnWorlds likely the stronger boutique fit — **confirm (Open Question)** |

**Single sign-on is the glue.** One login to the OS carries into CRM and Academy without re-auth. The OS is the **hub/launcher**; GHL and the LMS are **engines behind it**.

---

## File storage: stored in Drive, accessed through the OS (never duplicated)

Extends [[File Storage Rules]]. The OS is the single pane of glass.

| Thing | Stored in | Surfaced in OS as |
|-------|-----------|-------------------|
| Blank templates (contracts, NDAs) | Template Control (governed) | Document Generator pulls them |
| Brochures / brand assets / decks | SharePoint/Drive | Resource Library (links + preview) |
| Signed / legal documents | Secure legal archive | Linked from the Deal, read-only |
| Generated docs & projections | OS document store | Attached to the Deal |
| Structured data (clients, units, deals) | OS database | The source of truth |

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
- [[Product Vision]] · [[Product Modules]] · [[Prototype Spec]] · [[MVP Scope]] · [[Data Model]] · [[AI Layer Notes]]
- [[GoHighLevel Role]] · [[Training Academy Outline]] · [[File Storage Rules]]
