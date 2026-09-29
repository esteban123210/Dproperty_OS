---
project: B_RealEstate
title: "BlankCRM — Master Product Specification"
type: product_specification
status: Design baseline — live account validation pending
owner: Esteban
last_updated: 2026-09-29
tags: [blankcrm, gohighlevel, master, snapshot]
---

# BlankCRM — Master Product Specification

Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · product boundary: [[01 - Definition and Boundaries]].

## Decision and release boundary

BlankCRM is the client-facing, GoHighLevel-powered **commercial execution system**. It must run from lead capture through post-sale without BluePrint. BluePrint may read its data to verify results, govern policy, monitor CRM use and recommend management intervention. BluePrint does not advance an opportunity, approve a reservation, sign a contract, collect a payment or execute a commission.

**First release:** one repeatable new-development/pre-sale transaction path for one office. It includes real sales, legal, approval, contract, payment-milestone, closing, commission and post-sale work. The other processes in the [[../../08_Operations/Process Library/00 - Process Library Index|process library]] are mapped below but activate only after this golden path passes acceptance. The pilot's country, currency, developer, forms, document templates and commercial rules remain client-local variables; they must not be baked into the master.

**System of record:** one opportunity per commercial transaction, with a stable transaction ID. One contact can have multiple opportunities. Opportunity fields carry deal facts and states; contact fields carry person and communication facts. A pipeline stage records progression, not proof that an approval, signature or transfer happened. Documents, signed files, receipts and named decisions provide the evidence.

## Account topology and clone contract

| Environment | Purpose | Data policy |
|---|---|---|
| Agency account | SaaS plan, billing, support and snapshot administration | No client transaction records |
| `BlankCRM MASTER` sub-account | Clean source for reusable configuration | Synthetic data only; no live numbers, connections, client users or secrets |
| `BlankCRM TEST` sub-account | Apply each candidate snapshot and run acceptance suite | Synthetic data; reset between releases |
| Pilot office sub-account | First live delivery and measurement | Its own users, channels, payment/signature connections and transaction data |

Snapshot the **configuration**, never assume a clone carries contacts, conversations, appointments, phone numbers, live integrations, Stripe connections, domains or other client-specific connections. Maintain a versioned snapshot manifest, refresh it after master edits, deploy to TEST, then promote only after tests pass. Existing client accounts need a controlled update, field migration check and rollback plan; a snapshot push is not a database migration.

## Product modules and ownership

| Module | Master configuration | Per-office input / authority |
|---|---|---|
| Acquisition | Source taxonomy, tagged links/UTMs, forms, video landing-page pattern, website embed pattern, consent and dedupe rules | Brand, CEO video, domain, ad accounts, Lovable/Webflow placement, privacy language |
| Lead desk | Routing, SLA timers, qualification, calendar, reminders, no-show and nurture paths | Users, hours, territories, lead criteria and approved scripts |
| Deal desk | One sales pipeline, deal-type field, transaction ID, task templates, project/unit fields, offer and reservation states | Projects, inventory authority, prices and reservation terms |
| Legal and approvals | Document checklist, reviewer queue, approval records, rejection loop, signature-ready gate | Local counsel, templates, jurisdictional requirements and named approvers |
| Contracts | Template placeholders, version/status fields, send/signature tracking and exception tasks | Approved contract, authorized signer, e-sign provider and retention rules |
| Payments and closing | Expected milestone ledger, evidence and confirmation fields, overdue queues, closing/handover checklist | Seller/payee, bank or processor confirmation, local closing rules |
| Commissions | Separate office receivable, agent payout and HQ royalty records/statuses; rule-version field | Rates, splits, authorized approver and accounting/payment evidence |
| Post-sale | Handover, service requests, referral/review consent and follow-up | Warranty/aftercare owner and service policy |
| Commercial dashboards | Source conversion, speed-to-lead, stage age, due tasks, contracts, overdue milestones, closed deals and commission status | Office targets and permitted visibility |
| BluePrint feed | Optional, outbound/read-only event mapping and reconciliation log | Explicit integration agreement and endpoint; BlankCRM remains usable if disconnected |

Use native GoHighLevel configuration where it passes the scenario tests. A named human or authorized specialist provider remains responsible where inventory, legal judgment, bank settlement, accounting or local law requires external authority. Label each function **native, configured, integrated or human-confirmed** during the pilot; do not sell an untested integration as built-in.

## Data dictionary — minimum viable schema

| Object | Required fields | Key rules |
|---|---|---|
| Contact | Name, at least one usable contact method, country/time zone, consent by channel, preferred language | One person may have several deals; opt-out suppresses automated outreach on that channel |
| Lead attribution | Original source, channel, campaign/UTM, landing/form, captured-at, source-detail | Preserve first touch and latest touch separately; `unknown` is explicit, never guessed |
| Opportunity | Transaction ID, contact, office, owner, transaction type, stage, status, next action/date, project/unit (or N/A), currency, expected value | One authoritative opportunity per deal; owner and next action required while active |
| Qualification | Intent/timing, budget range, financing, preferred project, fit decision, decision reason | Missing information is distinct from disqualified; AI cannot silently reject |
| Reservation/approval | Offer version, reservation request, approver, decision, time, reason, policy version, developer response | No developer reservation request without sales-director approval |
| Legal/contract | Checklist version, required-item statuses, legal reviewer/decision, contract version, signer(s), sent/signed timestamps, document links | No contract send on incomplete checklist unless a named override with reason is recorded |
| Milestone | Type, payer, payee, amount/currency, due date, expected date, evidence link, verification source, verified-at/by, status | `expected`, `reported`, `verified`, `overdue`, `disputed`, `refunded` are distinct; stage move is not receipt proof |
| Closing/post-sale | Closing date and evidence, handover checklist, open defects, post-sale owner and next action | No `closed/completed` while mandatory handover or payment controls are unresolved without override |
| Commission | Office receivable; agent payout; HQ royalty if applicable; each amount/currency, rule version, approver, due/paid evidence and status | Never collapse developer-to-office income, office-to-agent payment and franchise royalty into one field |

Use an explicit `not applicable` choice for non-applicable checks. Any sensitive document and payment data must have role-limited access, retention and deletion policies. Store only necessary identifiers and links; do not put payment-card or bank credentials in free-text fields.

## Workflow state machine

The **one sales opportunity** moves through these stages. Legal, collections and commission are task/Smart List queues linked to that opportunity, rather than duplicate opportunities in separate pipelines. Status is independent: `active`, `waiting`, `blocked`, `cancelled`, `completed`. Stage changes should trigger checks and tasks; they do not by themselves prove a business event.

| Stage | Entry action and accountable owner | Exit evidence / exception |
|---|---|---|
| 1 New lead | Capture source/consent; route to owner; notify office | First human action scheduled; duplicate merged/reviewed |
| 2 Qualified | Advisor assesses fit and records decision | Qualification result + next meeting or explicit nurture/lost reason |
| 3 Meeting booked | Calendar confirmation and reminders | Attended, no-show retry or cancellation |
| 4 Project presented | Advisor logs project/unit and material shared | Client decision + next action |
| 5 Offer prepared | Offer terms and version; sales director approval task | Approved offer, rejection/rework or lost |
| 6 Reservation requested | Approved terms sent to inventory authority | Developer/seller confirmation or rejection with evidence |
| 7 Reserved | Reservation evidence, deadline, legal intake assigned | Documents complete or blocker/expiry path |
| 8 Legal review | Legal owns checklist and exceptions | Named legal sign-off or rejected/rework/override |
| 9 Contract ready | Approved version and signers verified | Contract sent with version/timestamp |
| 10 Contract signed | E-sign/file evidence recorded | Signature complete, rescinded or disputed |
| 11 Payment milestones | Expected schedule created; finance/collections tracks each item | Verified required receipts or documented waiver/exception |
| 12 Closing/handover | Operations/legal complete closing checklist | Closing evidence, final documents, handover recorded |
| 13 Commission and post-sale | Office receivable, agent payout and royalty tracked independently; aftercare owner assigned | All required states reconciled, post-sale task open or completed |

Long-duration milestone, commission and aftercare tasks may stay open after the commercial close; a `closed won` label must not hide them. `Lost` and `cancelled` require reasons and cancellation/refund checks. Reopening requires a named owner and audit note.

## Automations to build, in order

1. **Intake:** website/social form or manual entry → consent/source capture → dedupe review → office/owner assignment → notification → first-action deadline. Track link UTMs from Instagram, LinkedIn, Facebook and WhatsApp. The CEO video page can qualify interest; viewing it is a signal, not proof of buyer fit.
2. **Contact:** immediate acknowledgement only on permitted channels; advisor task; reminder and escalation on SLA breach. Appointment confirmation, reminders, no-show recovery and controlled nurture stop on reply, booking, opt-out or stage change.
3. **Deal:** stage tasks and checklists; offer approval; reservation approval and expiry; legal intake and missing-document reminders; rejected approval loops.
4. **Contract:** generate/send from approved template after named legal/commercial sign-offs; track send, view, signature, expiry and failure; escalate to a human.
5. **Payments/closing:** create expected milestones; remind payer or internal owner as authorized; flag overdue; only finance/bank/provider confirmation marks actual receipt; launch closing/handover tasks when prerequisites pass.
6. **Commission/post-sale:** calculate proposed splits from versioned rules; human approval; track receivable and each payout independently; service/referral/review follow-up with consent.
7. **AI assistance:** optional, after deterministic flows work. AI may draft replies, answer approved FAQs, summarize and suggest next actions. It must hand off on legal, price/discount, financing, complaint or payment disputes; no autonomous approval, binding offer, legal judgment or receipt confirmation.

Every workflow needs a unique trigger, re-entry rule, idempotency/duplicate policy, suppression condition, owner, error queue and test case. If a GoHighLevel stage/field requirement is bypassable by workflow or API updates, a second audit/guard workflow and human queue must detect it; never describe UI field requirements as an absolute gate.

## Roles and daily work surfaces

| Role | Sees/acts on | Restricted from |
|---|---|---|
| Sales advisor | Assigned leads/deals, communications, meetings and document collection | Approving own commercial exception or marking bank receipt verified |
| Sales director | Assignment, offer/reservation approvals, sales queue and commercial dashboard | Legal sign-off or bank verification without separate authorization |
| Legal | Document queue, checklist, contracts, legal sign-off and blockers | Editing commission rules or final payment verification |
| Operations coordinator | Data QA, deadlines, handover and exception queue | Legal judgment and self-approval |
| Finance/collections | Expected/actual milestones, evidence, commission receivable/payout status | Editing signed contract terms |
| Office owner/manager | Full office overview, escalations and authorized overrides | Cross-client data |
| BlankCRM support/admin | Configuration and support access under documented client authorization | Routine transaction decisions |

Use least privilege and test the actual permission screens in the pilot. A role name alone is not an access control. Daily default views: `new unworked`, `today's calls`, `overdue follow-up`, `legal blocked`, `awaiting approval`, `unsigned contracts`, `milestones due/overdue`, `closing blockers`, `commission exceptions`, `post-sale due`.

## Client-local variables and integrations

At onboarding collect office identity/time zone/currency/language, users and approvers, operating hours, lead ownership/SLAs, approved messages, domains, CEO video and landing copy, calendar availability, forms, project/developer inventory source, document templates, legal checklist, payment authority and payees, commission rules, retention/consent policy, social account owners, reporting targets and escalation contacts. Record each value in a client configuration sheet; no secret or personal data in the master.

Lovable and Webflow are interchangeable front ends for this purpose: connect the same tested CRM form/calendar or supported API/webhook pattern, preserve source UTMs and consent, and test each published site. Social scheduling is a separate marketing operation; do not infer that every listed network supports identical native publishing or WhatsApp automation. Verify channel capability and account connection during onboarding.

## Process coverage and controlled expansion

| Source process | Release treatment |
|---|---|
| 01 Leads | Release 1 intake, routing, qualification, follow-up and dashboards |
| 02 Preventa (Lista Cero) | Release 1 golden transaction, including approvals, legal, reservation, payments, closing and aftercare |
| 03 Secondary Market Sale | Release 2 after its seller/buyer, legal and handover variants pass tests |
| 04 Assignment (Cesión) | Release 2/3 after assignment consent and fee authority are specified |
| 05 Long-Stay Rental | Separate rental variant after lease/deposit and renewal controls are specified |
| 06 Property Management | Separate recurring service/maintenance module, not a sales-stage extension |
| 07 Commissions | Release 1 as three distinct office income, agent payout and HQ royalty flows |

## Source and implementation evidence

This is a **design baseline**, not proof of a live GoHighLevel configuration. The live account was at a sign-in screen on 2026-09-29. Native functionality and snapshot limits should be checked against the current [HighLevel snapshot guide](https://help.gohighlevel.com/support/solutions/articles/48000982511-snapshots-overview), [opportunity-field rules](https://help.gohighlevel.com/support/solutions/articles/155000008427-conditional-custom-fields-for-opportunities), [contract template guide](https://help.gohighlevel.com/support/solutions/articles/155000008460-documents-contracts-templates-with-opportunity-custom-values) and [payment-plan guide](https://help.gohighlevel.com/support/solutions/articles/155000003164-invoice-payment-plans) while building. See [[09 - Configuration Acceptance Tests]] for release proof and [[10 - Snapshot Release and Client Onboarding]] for the sequence.
