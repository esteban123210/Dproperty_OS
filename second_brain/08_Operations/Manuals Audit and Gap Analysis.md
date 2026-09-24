---
project: B_RealEstate
title: "Manuals Audit and Gap Analysis"
type: audit
status: Active
owner: Esteban
last_updated: 2026-07-21
scope: "All franchise manuals + supporting docs, graded against a multinational franchise-hub standard"
tags: [franchise, manuals, audit, gap-analysis, compliance, localization]
---

> [!INFO] Channel-scoped — verified 2026-09-23
> This folder describes the **Dproperty Franchise** channel, not the company and not a product. B_RealEstate is a product-led software company; this is one route to market.
>
> **Canonical name:** Dproperty Franchise — “the company itself” is a legacy alias.
> This is **valuable operating source material** — the process library and manuals feed BluePrint's SOP/process model and Building Blocks. Franchise royalty/launch economics are channel-specific and require contract design plus local legal advice before external use.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# Manuals Audit & Gap Analysis

> **What this is.** A cold-eyed audit of every Dproperty manual as of 2026-07-21, graded against the bar we actually need: a **multinational, multi-line franchise hub** (branded franchise + white-label + developer sales), not a single Panama office. It names weak points, standards violations, systemic gaps, and a prioritized fix path.

## 1. Executive verdict

**Where we are:** a strong *architecture* and one genuinely strong asset (the abstracted [[Process Library/00 - Process Library Index|Process Library]]), sitting on top of manuals that are — with one exception — **thin 2026-07-01 skeletons**. The one detailed manual (First Franchisee Launch Playbook) is rich but **violates our own standards** (names, EUR, Panama-hardcoded).

**Multinational-hub readiness: ~30%.** We can brief an investor and onboard *one Panama franchisee with heavy HQ hand-holding*. We **cannot** yet drop this package into a second country or hand it to a white-label client without material legal and operational risk. The two gates are **compliance depth** and a **localization framework** — both currently near-absent.

### Readiness scorecard
| Dimension | State | Grade |
|---|---|---|
| Manual architecture / governance | Defined (Manuals Index + Process Library) | 🟢 Good |
| Operational process content | Abstracted, role-based, 7/7 processes | 🟢 Good (needs owner validation) |
| Depth of the 5 franchise manuals | Mostly outlines | 🔴 Weak |
| Standards compliance (roles-not-names, USD) | Violated in 1 key doc | 🟡 At risk |
| **Localization / multi-country framework** | Essentially absent | 🔴 **Critical gap** |
| **Compliance & legal coverage** | ~40 lines of "don'ts" | 🔴 **Critical gap** |
| Multi-line coverage (white-label, developer) | Strategy only, no manuals | 🔴 Weak |
| Training rigor | Outline only | 🟡 Weak |

## 2. Manual-by-manual maturity

| ID | Manual | File | Maturity | One-line verdict |
|---|---|---|---|---|
| M0 | HQ / Franchisor Ops | (not started) | ⬜ | Deferred — but it's the backbone of cross-office consistency; risk grows with each new market |
| M1 | Franchise Onboarding | [[../02_Offers/05_Dproperty_Franchise/04 - Onboarding]] | 🟡 Draft | Good narrative skeleton; restates pricing (drift risk); no localization |
| M2 | Franchise Operations Manual | [[Operations Manual]] | 🔴 Skeleton | 60 lines of generic routines; **not yet built on the Process Library** — its biggest missed opportunity |
| M3 | Launch Plan | [[../02_Offers/05_Dproperty_Franchise/04A - 30-60-90 Day Launch Plan]] + [[../02_Offers/05_Dproperty_Franchise/04B - First Franchisee Launch Playbook]] | 🟡 Mixed | 30-60-90 is thin; the 12-week Playbook is detailed **but violates standards** (see §3) |
| M4 | Sales Playbook | [[../02_Offers/05_Dproperty_Franchise/04D - Sales Playbook]] | 🟢 v0.5 | **Rebuilt today** on the Process Library; role-agnostic, USD, multi-market aware |
| M5 | Compliance Manual | [[../07_Legal_and_Compliance/Compliance Package]] | 🔴 Skeleton | **Dangerously thin for cross-border real estate** — highest-risk gap (see §4) |
| — | Brand Manual | [[../10_Brand_and_Web/Brand Manual]] | 🟡 Draft | Voice is clear; visual system is a "to build" list; no multilingual/market-adaptation rules |
| — | Training Academy | [[../02_Offers/04_Building_Blocks/10 - Curriculum Outline]] | 🔴 Outline | Module list only; no assessment rigor, recertification, or localization |
| — | Welcome Kit | [[../02_Offers/05_Dproperty_Franchise/04E - Welcome Kit Checklist]] | 🟡 OK | Fine for purpose; low risk |

## 3. Standards violations (fix before anything ships)

Per Decision 2026-07-21 (roles-never-names) and the USD standard:

| Where | Violation | Fix |
|---|---|---|
| [[../02_Offers/05_Dproperty_Franchise/04B - First Franchisee Launch Playbook]] | Personal names throughout ("Esteban", "Miguel", "witness") | Replace with roles (HQ Lead / Venture Lead → **PRIN/HQ**, Tech → **BI/OC**) |
| [[../02_Offers/05_Dproperty_Franchise/04B - First Franchisee Launch Playbook]] | **Currency in EUR** (€10k, €300k, €4,125) + a stray "$750" | Restate all in **USD**; reference the Pricing Model, don't hardcode |
| [[../02_Offers/05_Dproperty_Franchise/04B - First Franchisee Launch Playbook]] | Panama/2026 calendar hardcoded (Sept 16–Dec 8) | Convert to **relative weeks (Week 1–12)**; dates are a launch-instance variable |
| [[../02_Offers/05_Dproperty_Franchise/04B - First Franchisee Launch Playbook]] §5 | **Commission math is wrong/inconsistent**: labels franchise-net as "gross commission," then subtracts HQ fees again (double count); royalty figures (~€250/€750/€1,250) don't match 7.5% on gross-into-company | Rebuild from the [[Process Library/07 - Commissions]] firewall + Decision Log waterfall |
| Onboarding, Launch, others | Pricing figures **restated inline** (drift risk) | Reference [[../06_Finance/Pricing Model]] / Decision Log as single source |

## 4. Systemic gaps for a multinational hub (the real work)

These are not per-manual polish — they are missing *systems* the whole package needs.

### 4.1 🔴 Localization framework (highest structural priority)
There is no mechanism to take a manual from Panama to Bogotá/Medellín (or a white-label client abroad). Needed:
- A **Market Variables Matrix** per country: currency, commission norms, reservation/down-payment customs, KYC/AML document set, real-estate licensing, tax/withholding on commissions, contract/closing steps, franchise-disclosure law, language.
- A convention (already started in the Process Library: `[local-market variable]`) applied across **all** manuals.
- A rule: **process is global, values are local.** Manuals hold the process; a market pack holds the values.

### 4.2 🔴 Compliance & legal depth
Current M5 is a list of "don'ts." A cross-border real-estate franchise needs real coverage of:
- **Franchise law:** disclosure/registration regimes (e.g. US FDD & registration states, EU block exemption, LATAM franchise rules) — *selling a franchise in the wrong jurisdiction without disclosure is a legal event.*
- **Real-estate licensing** per market (who may broker, under whose license).
- **AML/KYC & sanctions** screening (real estate is a regulated AML sector in most markets).
- **Data privacy:** GDPR + local (Panama Law 81, Colombia 1581) — the CRM holds PII cross-border.
- **Advertising/consumer protection & no-guaranteed-returns** (already hinted — needs teeth).
- **Anti-bribery** (developer relationships), **fair-housing/anti-discrimination**, **PI/E&O insurance** minimums.
- Ties to Open Questions (jurisdiction, disclosure docs) in [[../00_Start_Here/Open Questions]].

### 4.3 🔴 Multi-line coverage
The package is **branded-franchise-only**. The hub sells three lines. Decide the model: a **shared core** (Process Library + Compliance + Brand) with **line-specific overlays** for [[../02_Offers/06_B_Partner/02A - Offer Guide|white-label]] and [[../02_Offers/07_Developer_Partnerships/02A - Program Guide|developer sales]]. Today those lines have strategy notes but no manuals.

### 4.4 🟡 Build M2 on the Process Library
The Franchise Operations Manual should *be* the owner-facing assembly of Processes 1–7 plus people/finance/reporting — not a separate generic list. Right now it duplicates nothing useful and references the Library not at all.

### 4.5 🟡 Manual governance
Only the Process Library and the new Sales Playbook have versions, owners, and status. Adopt the same front-matter (version, status, owner, last_updated, review cadence) across **all** manuals, and a change-control note that points to the Decision Log.

### 4.6 🟡 Training rigor
Move from a module list to: learning objectives, assessment/pass criteria, certification validity + recertification, and per-market localization (esp. compliance & licensing modules).

## 5. What's genuinely good — keep
- The **Process Library** (role-agnostic, RACI-level, localization-flagged) — this is the crown jewel and the real moat content.
- The **Manuals System Index** one-master-source model — prevents drift.
- The **12-week Launch Playbook's operational depth, HQ-support cadence, and risk-mitigation triggers** — excellent thinking; just needs abstraction/USD.
- The **Brand voice** definition — clear and differentiated.
- The **boutique positioning** thread running through every doc.

## 6. Prioritized remediation roadmap

**P0 — before any external use / second market**
1. Build the **Compliance Manual (M5) v0.5** with the §4.2 coverage (HQ + lawyer input).
2. Create the **Localization / Market Variables framework** (§4.1) + first market pack (Panama).
3. **Abstract + fix the Launch Playbook** (names→roles, EUR→USD, dates→relative, commission math).

**P1 — makes the package real**
4. Rebuild **M2 Franchise Operations Manual** on the Process Library (v0.5).
5. Elevate **M1 Onboarding** and **M3 30-60-90** to reference (not restate) pricing/processes; add localization.
6. Apply **manual governance** front-matter to all manuals.

**P2 — hub-scale**
7. Decide and scaffold **multi-line overlays** (white-label, developer).
8. Deepen **Training Academy** (assessment + recertification + localization).
9. Turn **Brand Manual** into an enforceable system (link Figma/Canva assets + multilingual/market rules).
10. Draft **M0 HQ / Franchisor Operations Manual** once M1–M5 stabilize.

## 7. The one decision this audit surfaces
**Do we harden for a *credible pilot* (one market, deep) or for *multinational readiness* (localization + compliance + multi-line) now?** The first is ~3 focused deliverables (P0 items 1–3, Panama-only). The second is the full P0–P2 roadmap. Both are valid; they set very different scopes for the next sessions.

---
*Audit v1.0 — 2026-07-21. Re-run after the P0 items land.*
