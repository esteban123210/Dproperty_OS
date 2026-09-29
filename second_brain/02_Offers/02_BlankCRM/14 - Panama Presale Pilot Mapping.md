---
project: B_RealEstate
title: "BlankCRM — Panama Presale Pilot Mapping"
type: pilot_process_mapping
status: Design review — local authority and live test pending
owner: Esteban
last_updated: 2026-09-29
tags: [blankcrm, panama, presale, pilot]
---

# BlankCRM — Panama Presale Pilot Mapping

Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · product: [[08 - Master Product Specification]] · source: [[../../08_Operations/Process Library/02 - Preventa (Lista Cero)]].

Esteban confirmed the first franchise is **Dproperty** in **Panama**, selling **several pre-construction/new-development projects**. Buyers pay reservation money **directly to the developer**. The inherited Dproperty presale process supplies a starting sequence, not approved Panama legal advice or a final franchise policy. Sales, legal, finance and each developer must confirm local terms before external messages, contracts or payments go live.

## One test transaction, from first meeting to aftercare

| Source step | BlankCRM action and record | Accountable decision / evidence |
|---|---|---|
| 1 Initial meeting | Advisor creates one contact and one opportunity; captures budget, available cash, monthly capacity, motivation and next action | Advisor; consent/source/owner and meeting notes |
| 2 Present project | Select the correct client-local Project record; record unit/version, presentation and ROI worksheet reference on the opportunity | Advisor; approved material, project-specific rule versions and client feedback. Another project can be presented, but the offered deal must select one project. |
| 3 Validate interest | Sales director records fit decision before a reservation offer is treated as final | Director; named approval decision and rationale |
| 4 Reservation payment and deal sheet | Record **buyer-to-developer reservation money** as a Payment Milestone, with payer = buyer, payee = developer, amount, status and developer receipt evidence; keep deal sheet/version linked | Developer/finance confirms receipt. This is never Dproperty-received cash. Payment can be recorded before director approval without authorizing a developer request. Exact collection timing remains a local policy decision. |
| 5 Approve reservation | Director reviews project-specific terms, unit, price, developer payment evidence and exceptions; approves/rejects the specific version | Director; Approval Decision record. Rejection starts a developer disposition/refund follow-up task if money was taken; do not mark a refund complete without developer evidence. |
| 6 Notify developer | Operations sends only approved reservation details through the authorized channel and logs response/expiry | Developer/inventory authority confirms unit; no assumption that CRM itself controls inventory |
| 7 Request documents | Operations collects the pilot's required file; legal reviews completeness and exceptions in its CRM queue | Local legal owner defines checklist; named legal sign-off or documented override |
| 8 Draft contract | Create an approved-template draft in GoHighLevel or register the developer's draft/version for review | Legal checks content, parties and signers; document source recorded |
| 9 Approve contract | Sales director approves commercial terms; legal approves legal readiness; both refer to the same version | Separate Approval Decision records; no send on mismatched versions |
| 10 Sign contract | Authorized sender sends the reviewed draft or records external signing status/evidence | All required signers complete; signed copy/version retained under approved access rules |
| 11 Initial down-payment | Create a **separate** buyer-to-developer Payment Milestone; record expected amount/date and independently verified actual receipt | Finance/developer evidence; do not book it as office revenue |
| 12 Collect commission | Create developer-to-office Commission Obligation; prepare invoice/proforma only under the developer agreement and office policy | Finance tracks receivable, collection and evidence; agent payout and HQ royalty are separate obligations |
| 13 Update CRM and controls | Opportunity, milestone, approval and commission records already exist; reconcile any internal control sheet to them | Operations/finance resolve discrepancies. BluePrint may read management evidence, but does not execute the step. |
| 14 Post-sale | Start owner-led construction/payment updates and client questions after the approved binding-sale event; later complete handover and defect queue | Operations; scheduled tasks, communications and open issues remain visible even if deal is `Won` |

**Parallel timing:** the original process lists commission and post-sale after contract and initial payment, while physical handover can be much later. They therefore run as linked queues alongside the active contract/payment schedule, not as stages that wait for final handover. The source allows a reservation payment before director approval but explicitly forbids sending the reservation to the developer without that approval. These are separate controls.

## Pilot decisions that cannot be guessed

| Decision | Needed from | Build effect if unanswered |
|---|---|---|
| Dproperty franchise legal entity, city and time zone | Office owner | Pilot account details and communications stay draft |
| First two projects/developers and each inventory confirmation method | Sales director/developers | Project-specific offer/reservation rules cannot be tested |
| Reservation amount, developer identity, collection timing, refundability and rejected-reservation procedure | Sales director, finance, legal, developer | Reservation payment automation stays off; **payee class = developer** is already confirmed |
| Required client documents, sensitive-data storage and legal exception approver | Panama legal team | Legal checklist and contract send stay draft |
| Contract source/template, signers, e-sign validity and final version approval | Panama legal team/developer | Contract workflow creates drafts only |
| Initial and later buyer-to-developer payment schedule and verification evidence | Finance/developer | Payment reminders and `verified` status stay manual |
| Developer commission trigger, base, rate, tax treatment, invoice/collection process | Finance/developer agreement | Office receivable proposal cannot calculate or send |
| Agent payout and franchise royalty triggers, bases and approvals | Finance/office/HQ agreements | Distinct obligations remain unpriced/pending |
| Exact `Won`, closing, handover and aftercare start criteria | Sales director, legal, finance | No automatic `Won`/completion change |
| Approved project claims, ROI model and client messages | Sales/marketing/legal | No automated investment-return claim |

No Panama-specific amount, percentage, checklist or legal claim belongs in the country-neutral MASTER. Put approved versions into the pilot sub-account and record the rule version on each resulting deal.

## Evidence before launch

Run synthetic Panama presales for **two different projects** through source steps 1–14, then repeat with (a) developer-direct reservation rejected after money was received, (b) missing legal document, (c) developer down-payment reported but not verified, (d) developer commission due while handover is in the future, and (e) BluePrint disconnected. Record C01–C41 results in the TEST clone. This document is a mapping and test input; it is **not** a passed live test.
