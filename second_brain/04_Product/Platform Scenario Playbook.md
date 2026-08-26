---
project: Dproperty OS
title: "Platform Scenario Playbook"
type: product_spec
status: Draft v0.5
version: 0.5
owner: Esteban
last_updated: 2026-07-18
source: Claude working session 2026-07-18
tags: [product, architecture, scenarios, ux, wireframe]
---

# Platform Scenario Playbook

> 72+ real-world scenarios used to pressure-test the [[Platform Information Architecture]] before wireframing. Framework for every answer: **3 clicks · automation-first · AI only for language.** Tiers defined in [[Platform Information Architecture]] (T0 = no AI, T1 = cheap/local AI, T2 = premium).

> **⚠ Scope filter (2026-08-26):** BluePrint is now back-office-only ([[BluePrint Product Constitution]] §3.11). **Part A scenarios written for a sales advisor inside the OS are out of scope** — that user works in GoHighLevel and has no BluePrint seat. Read them as CRM scenarios or as back-office scenarios performed on the advisor's behalf. Scenarios covering glitches, HR, cases, obligations, templates, resources and reporting remain valid and are now core Release 1 regression material.

---

## Part A — Agent / franchisee (post-login), 20 scenarios

| # | Scenario | How it works (path + clicks) | Tier |
|---|----------|------------------------------|------|
| 1 | Register a new property + photos + price | `New → Listing`. **Structured form** (project, developer, location, price, unit, payment plan, upload photos/floorplans/docs). On submit, T0 automation creates the SharePoint folder by naming convention `Country/Developer/Project/Unit`, uploads files, writes the structured record into the OS DB (source of truth). *Optional* T1: local model drafts the marketing blurb. **No AI touches filing.** | T0 (+T1 opt) |
| 2 | In a meeting: "what do you have available?" | Command Bar → Inventory/Projects → filter by budget/location/status. Field Mode: clean card list w/ price + photos in 2 taps. | T0 |
| 3 | Sign an NDA in under a minute | Command Bar → "NDA" → `Generate NDA` → pick person → auto-fill approved template → e-sign → archived + logged. Target <45s. | T0 |
| 4 | New buyer lead via WhatsApp | Quick-add lead (or GHL WhatsApp auto-capture) → CRM pipeline. T1 SDR agent can qualify/reply if enabled. | T0 (+T1 opt) |
| 5 | Client asks for a specific project's brochure | Command Bar → project → Documents tab → brochure (from Drive) → Send/Share link. 3 clicks. | T0 |
| 6 | Client asks for an ROI projection on a unit | Deal/Unit → `Generate Projection` → price/plan auto-pulled → HQ-locked + editable fields → PDF. Math deterministic. | T0 |
| 7 | Is this unit still available / reserve it | Unit record → live status → "Reserve" → status flips, HQ notified. | T0 |
| 8 | Broker refers a client | `New → Broker Deal` → link broker + client + commission split from agreement → tracked in Deal. | T0 |
| 9 | Need the current price list (prices changed) | Project → Payment Plan/Pricing → always the live HQ-controlled version. | T0 |
| 10 | Show client photos/video on phone | Field Mode → project → media gallery (streams from Drive). | T0 |
| 11 | Generate a reservation/client agreement | Document Generator wizard → type + deal → auto-fill → preview → (legal approval if flagged) → sign. | T0 |
| 12 | What are my follow-ups today? | Workspace → "Follow-ups due today" widget. T1 agent can draft messages. | T0 (+T1) |
| 13 | Send a curated shortlist of 3 projects | Select projects → "Create Shortlist" → shareable link/PDF. | T0 |
| 14 | Need a project's payment plan fast | Command Bar → project → Payment Plan tab. | T0 |
| 15 | Access a Private Collection opportunity | Private Collection → project → "Request Access" → HQ senior manager auto-assigned → register client. | T0 |
| 16 | What's my commission forecast / earnings? | Finance/Commission dashboard → personal (role-filtered) view. | T0 |
| 17 | Onboard a new team member | Launcher → Academy (embedded LMS, SSO) → assigned track → gated certifications. | T0 |
| 18 | Approved template to reply to a lead | Command Bar → "template" → pick email/WhatsApp template → merge fields. | T0 (+T1 opt) |
| 19 | A document needs legal approval before sending | Doc flagged → HQ Legal queue → approve/reject → advisor notified. | T0 |
| 20 | Working offline / traveling | Field Mode caches inventory, prices, brochures, contacts, NDA generator. | T0 |

**Takeaway:** 18/20 daily tasks need zero AI. AI is optional polish on 3–4.

---

## Part B — Prospective franchisee + HQ selling-agent (pre-login), 20 scenarios

### Prospective buyer (just-graduated future franchisee)
| # | Scenario | Path |
|---|----------|------|
| 1 | Where's the info to buy a franchise? | Public site → "Become a Franchise" hub |
| 2 | How do I consult the roadmap? | Franchise hub → "Your Path" / Roadmap |
| 3 | What's the value proposition? | Franchise hub → "Why Dproperty" |
| 4 | What's the investment / cost? | "Investment & Returns" (fees, what's included, sample unit economics) |
| 5 | How do I schedule a meeting? | "Book a Call" on every franchise page → GHL calendar |
| 6 | What should I expect after booking? | Auto-confirmation + **Prep Pack** (agenda, info pack, video) via GHL automation |
| 7 | What territories are available? | Territory Map |
| 8 | What exactly do I get? | "What's Included" page |
| 9 | Do I qualify / requirements? | Requirements section + short pre-qual form |
| 10 | Proof it works? | Case studies / testimonials / numbers |
| 11 | How long until I'm operational? | Roadmap 30-60-90 timeline |
| 12 | What support from HQ? | "What's Included" → Support & Academy |
| 13 | Info pack without a call? | "Download Info Pack" (email-gated → CRM nurture) |
| 14 | What's the Private Collection? | Teaser page (gated depth) |
| 15 | Objections / FAQ | FAQ page |

### HQ selling-agent (closes the franchise)
| # | Scenario | How it works |
|---|----------|--------------|
| 16 | Full presentation package ready for the call | **Franchise Sales Room**: deck, financial model, roadmap, agreement draft, demo video — one launcher |
| 17 | Send a tailored follow-up pack after the meeting | Generate a **per-prospect Data Room link** (personalized microsite) |
| 18 | Pitch deck + financial model + agreement on hand | All in the Sales Room, versioned, always current |
| 19 | Track where each prospect sits | Franchise-recruitment pipeline (separate from property leads) |
| 20 | Answer tough finance/legal questions live | Battle-card / Q&A in the Sales Room (from [[Supervisor and Owner Q&A]]) |

---

## Part C — HQ / Network Management, 8 scenarios

| # | Scenario | Path | Tier |
|---|----------|------|------|
| 1 | Onboard a new franchise | HQ Control Center → `New Tenant` → provisions workspace, GHL sub-account, Academy, brand kit, templates, roles | T0 |
| 2 | Monitor network performance & compliance | HQ Home → dashboard: revenue, deal flow, compliance score, activity, training | T0 |
| 3 | Push a template/price update to all tenants | Template Control → edit → "Publish to network" → versioned, adoption tracked | T0 |
| 4 | Remediate an underperforming/non-compliant franchise | Franchise profile → flags → open Case → assign remediation → track | T0 |
| 5 | Publish a Private Collection project | Private Collection → add → set pool, senior manager, authorized franchises → publish | T0 |
| 6 | Approve items in legal/doc queue | HQ Legal inbox → approve/reject with note | T0 |
| 7 | Audit a franchise | Franchise profile → "Audit" → checklist → report | T0 |
| 8 | Offboard / terminate a franchise | Tenant Lifecycle → wind-down: revoke access, export data, transfer deals, settle royalties, archive | T0 |

---

## Part D — HR / People, 5 scenarios

| # | Scenario | Path | Tier |
|---|----------|------|------|
| 1 | Franchise hires a sales advisor | People → `Add Person` → role + permissions → auto-assign Academy + templates + CRM seat | T0 |
| 2 | Employee requests time off | People → "Request Leave" → routes to Principal → approve → calendar | T0 |
| 3 | Access contract / payslip / HR docs | "My Profile" → Documents (role-gated: only they + HR) | T0 |
| 4 | Performance review / certification tracking | People → person → review + Academy cert status (gated) | T0 |
| 5 | Employee offboarding | People → "Offboard": revoke access, reassign clients/deals, final pay, exit checklist | T0 |

---

## Part E — Complaints & Grievances, 4 scenarios (Cases engine)

**Case type controls who sees it, who it routes to, and the SLA.**

| # | Scenario | How it works | Tier |
|---|----------|--------------|------|
| 1 | Client complaint about an advisor/service | "File a Complaint" → Client Complaint case → routed to Principal (+HQ if severe) → SLA clock → logged | T0 (+T1 summarize) |
| 2 | Employee internal HR grievance (confidential) | "My Profile → Confidential Report" → HR Grievance case, visibility locked to HR/HQ (hidden from Principal if it's about them) | T0 |
| 3 | Franchisee escalates to HQ | "Escalate to HQ" → Franchise Escalation case → HQ queue | T0 |
| 4 | Whistleblower / compliance report | Anonymous intake (no identity) → HQ Compliance only | T0 |

---

## Part F — Accounting / Finance Ops, 8 scenarios

**OS = the record; payment provider = the money movement. AI touches none of it.**

| # | Scenario | How it works | Tier |
|---|----------|--------------|------|
| 1 | Commission payment on a closed deal | Deal closes → auto-calc split (advisor/broker/franchise/HQ) → payout record → approve → pay → reconcile | T0 |
| 2 | Pay HQ royalties / network fees | Auto-compute royalty from revenue → invoice → auto-collect → logged | T0 |
| 3 | Employee expense reimbursement | "Request Reimbursement" → form + receipt → Principal approves → pay → logged | T0 (+T1 read receipt) |
| 4 | Invoice a client or developer | `New → Invoice` → linked to deal/project → template → send → track | T0 |
| 5 | Reconcile a payment received | Provider webhook → auto-match to invoice/deal → flag mismatches | T0 |
| 6 | Refund / cancelled reservation | Deal → "Cancel/Refund" → reverse commission accrual → refund → audit-logged | T0 |
| 7 | Developer success-fee billing | Developer dashboard → milestone/units-sold triggers fee → invoice → track | T0 |
| 8 | Monthly financial close & reporting | Finance → "Close Period" → per-franchise P&L + network roll-up + royalty statements | T0 |

---

## Part G — Claims, Disputes & Edge Cases, 7 scenarios

| # | Scenario | How it works | Tier |
|---|----------|--------------|------|
| 1 | Client disputes a commission/contract | Dispute case → freezes related payout → routes to Legal/Finance → resolution logged against deal | T0 |
| 2 | Signed doc challenged / legal needs it | Command Bar → deal/doc → signed version + version + approval history (immutable) | T0 |
| 3 | Payment fails / chargeback | Provider webhook → flags invoice → Finance case → retry/dunning | T0 |
| 4 | Client "delete my data" request | "Data Request" intake → Data Governance case → Compliance reviews (some records legally retained) → actioned + logged | T0 |
| 5 | OS outage / can't access | Field Mode offline cache + status page. No mission-critical single point of failure. | T0 |
| 6 | Two advisors claim the same lead | Lead has source + first-touch timestamp → attribution case → Principal decides → rule logged | T0 |
| 7 | Fraud / suspicious activity | Audit log flags anomaly (bulk export, off-hours) → Compliance alert → Security case | T0 (+T1 summary) |

---

## Part H — Glitch Report, 5 scenarios (Four Seasons model)

**One click, five seconds, no blame, visible to everyone.**

| # | Scenario | How it flows |
|---|----------|--------------|
| 1 | Brochure shows last quarter's price | "Report a Glitch" → "Brochure price outdated" → Experience tag → HQ updates master → ✅ "updated to Q3 pricing" |
| 2 | A button on the Deal screen does nothing | Glitch → screenshot auto-attached → Product tag → dev backlog → fixed → feed shows ✅ |
| 3 | Client onboarding email had a typo | Glitch → Experience → Marketing fixes template network-wide |
| 4 | Field Mode slow loading photos in a meeting | Glitch 🔴 → clustered with 6 similar → prioritized |
| 5 | Reimbursement form is confusing | Glitch → Product/UX → HQ redesigns form → announces improvement in feed |

**Compounding effect:** hundreds of tiny fixes/year = a platform that feels dramatically better than any competitor's, because every user is a quality sensor and every fix is visible.

---

## What the scenarios forced into the architecture
See [[Platform Information Architecture]] for the consolidated changes. Summary:
- Added: Command Bar, Field Mode, Listing intake form, Shortlist/Share, approval queues, Franchise Sales Room, Data Room generator.
- Added 6 back-office systems: Finance, People/HR, Cases, Tenant Lifecycle, Audit/Data Governance, Glitch Report.
- Pre-login: 7-page "Become a Franchise" hub, dual CRM pipelines, Prep Pack automation, Download Info Pack gate.
- Rulings: confidentiality is a property of the *case*; money/legal actions are always T0 + audit-logged; glitches are never person-attributed.

## Related
- [[Platform Information Architecture]] · [[Roles and Access Matrix]] · [[Prototype Spec]] · [[AI Layer Notes]]
