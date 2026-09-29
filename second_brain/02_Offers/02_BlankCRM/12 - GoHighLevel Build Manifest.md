---
project: B_RealEstate
title: "BlankCRM — GoHighLevel Build Manifest"
type: implementation_manifest
status: Draft 1.0.0 — not installed in a live account
owner: Esteban
last_updated: 2026-09-29
tags: [blankcrm, gohighlevel, configuration, snapshot]
---

# BlankCRM — GoHighLevel Build Manifest

Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · scope: [[08 - Master Product Specification]] · tests: [[09 - Configuration Acceptance Tests]].

This is the exact **build list**, not evidence that it exists in GoHighLevel. Build in `BlankCRM MASTER`, load the snapshot into a fresh `BlankCRM TEST` account and record actual field keys/asset IDs in a release log. Names below are stable labels for builders and support; HighLevel may generate different internal keys. Search for an existing equivalent before creating a field. Do not create the same business fact on Contact and Opportunity.

## 1. Folders and naming

Use `BC |` at the start of every reusable asset name and these folders: `00 Core`, `01 Intake`, `02 Sales`, `03 Legal`, `04 Payments & Closing`, `05 Commissions`, `06 Post-sale`, `07 Reporting`, `90 Exceptions`. Within workflows, prefix IDs `BC-WF-01` through `BC-WF-15`. Leave test-only assets out of the master snapshot.

## 2. Records and associations

| Record | Cardinality | Required connection | Why |
|---|---|---|---|
| Contact (native) | One person can have many deals | Native opportunity contact | Identity, consent, communication |
| Opportunity (native) | One per transaction | Contact and office owner | Authoritative deal and pipeline stage |
| `BC Approval Decision` (custom object) | Many per opportunity | One approval → one opportunity | Offer, reservation, legal and override decisions remain versioned |
| `BC Payment Milestone` (custom object) | Many per opportunity | One milestone → one opportunity | Multiple dates/amounts and independent expected vs verified state |
| `BC Commission Obligation` (custom object) | Many per opportunity | One obligation → one opportunity | Developer-to-office, office-to-agent and HQ royalty never share a status |

Create one-to-many Opportunity associations for the three custom objects. Give each custom-object record a **unique, single-line ID** and a transaction-ID reference for reconciliation. Creating an object record without a verified opportunity link enters the `90 Exceptions` queue. Test whether record creation/association can be automated in this account; if not, make the named owner create/link it manually. Custom-object associations and workflow support are documented by HighLevel, but some association automation has been described as beta; do not assume it works until C33 passes. [Objects](https://help.gohighlevel.com/support/solutions/articles/155000003897) · [Opportunity associations](https://help.gohighlevel.com/support/solutions/articles/155000004033) · [Association workflow](https://help.gohighlevel.com/support/solutions/articles/155000007718-workflow-action-associate-records).

## 3. Field creation order

`Required` here means required by BlankCRM's workflow/review policy, not a guarantee that HighLevel UI validation blocks every API or workflow edit. Native fields such as name, email, phone, pipeline, stage and owner are not duplicated.

| Record/folder | Field label | Type/values | Required at |
|---|---|---|---|
| Contact / Intake | `BC Country` | Single-line or local list | Intake QA |
| Contact / Intake | `BC Preferred language` | Single-select: office-approved languages, unknown | First outbound |
| Contact / Intake | `BC Original source` | Single-select: website, Instagram, Facebook, LinkedIn, WhatsApp, referral, event, manual, other, unknown | Capture |
| Contact / Intake | `BC Latest source` | Same values | Each new inquiry |
| Contact / Intake | `BC Original campaign` | Single-line | When URL provides it |
| Contact / Intake | `BC Latest campaign` | Single-line | When URL provides it |
| Contact / Intake | `BC Landing/form ID` | Single-line | Digital capture |
| Contact / Consent | `BC Consent evidence` | Short reference/URL; channel, time and wording version in record | Before automated outbound |
| Opportunity / Core | `BC Transaction ID` | Single-line stable ID | Creation |
| Opportunity / Core | `BC Office code` | Single-line | Creation |
| Opportunity / Core | `BC Transaction type` | Single-select: new development, resale, assignment, rental, property management | Qualification |
| Opportunity / Core | `BC Deal status` | Single-select: active, waiting, blocked, cancelled, completed | Creation |
| Opportunity / Core | `BC Next action` | Single-line | Every active stage |
| Opportunity / Core | `BC Next action date` | Date | Every active stage |
| Opportunity / Qualification | `BC Fit decision` | Single-select: pending, qualified, nurture, disqualified | Leaving qualification |
| Opportunity / Qualification | `BC Fit reason` | Multi-line | Disqualified/nurture |
| Opportunity / Sales | `BC Project name` | Single-line or project reference | Project presentation |
| Opportunity / Sales | `BC Unit reference` | Single-line or N/A | Reservation |
| Opportunity / Sales | `BC Offer version` | Single-line | Offer approval |
| Opportunity / Sales | `BC Approved offer evidence` | Link/reference | Reservation request |
| Opportunity / Sales | `BC Reservation expiry` | Date | Reserved |
| Opportunity / Legal | `BC Checklist version` | Single-line | Legal intake |
| Opportunity / Legal | `BC Legal packet state` | Single-select: not started, collecting, review, approved, rejected, override | Contract draft |
| Opportunity / Legal | `BC Contract version` | Single-line | Contract draft |
| Opportunity / Legal | `BC Contract document ID` | Single-line/link | Contract sent |
| Opportunity / Closing | `BC Closing evidence` | Link/reference | Closing complete |
| Opportunity / Closing | `BC Handover state` | Single-select: pending, blocked, complete, N/A | Closing |
| Opportunity / Finance | `BC Commission rule version` | Single-line | Offer approval |
| Opportunity / Post-sale | `BC Aftercare owner` | User/reference | Handover |

Do not rely on a dropdown called `consent = yes` to send messages. Test native DND/opt-out and channel connections. Keep exact decision times in HighLevel audit/document status and evidence records; date-only fields are for scheduling, not a substitute for an audit timestamp. HighLevel documents that an existing field cannot later switch from Contact to Opportunity. [Custom fields](https://help.gohighlevel.com/support/solutions/articles/155000008466-creating-and-managing-custom-fields-for-better-data-organization) · [Opportunity fields](https://help.gohighlevel.com/support/solutions/articles/155000000521).

### Custom-object fields

| Object | Field labels | Required rule |
|---|---|---|
| Approval Decision | `Approval ID` (unique text), `Transaction ID`, `Kind`, `Offer/contract version`, `Requested by`, `Approver`, `Decision` (pending/approved/rejected/overridden), `Reason`, `Policy version`, `Evidence reference` | Named approver and decision evidence before downstream action; override never silently replaces rejection |
| Payment Milestone | `Milestone ID` (unique text), `Transaction ID`, `Kind`, `Payer`, `Payee`, `Expected amount`, `Currency`, `Due date`, `Status` (expected/reported/partially verified/verified/overdue/disputed/refunded/waived), `Verified amount`, `Verifier`, `Evidence reference` | Verified amount and evidence required for verified; seller/developer payment is not agency revenue |
| Commission Obligation | `Obligation ID` (unique text), `Transaction ID`, `Type` (office receivable/agent payout/HQ royalty), `Rule version`, `Amount`, `Currency`, `Due date`, `Status` (proposed/approved/due/paid/disputed/reversed/N/A), `Approver`, `Payment evidence` | Three flows remain separate; one obligation can be reversed without rewriting the other two |

## 4. Sales pipeline and queues

Create pipeline `BC | Commercial Transaction` with ordered stages: `01 New lead`, `02 Qualified`, `03 Meeting booked`, `04 Project presented`, `05 Offer prepared`, `06 Reservation requested`, `07 Reserved`, `08 Legal review`, `09 Contract ready`, `10 Contract signed`, `11 Payment milestones`, `12 Closing/handover`, `13 Commission and post-sale`. `Lost` is a closed/lost outcome with a reason; `Cancelled` is deal status and a recovery/reversal workflow, not a way to erase history. Do not set `Won` merely because a contract was sent or one payment was reported.

Create role queues/views: `Unworked new leads`, `Follow-up due`, `No-show`, `Offer approval`, `Reservation expiry`, `Legal blocked`, `Contract draft review`, `Unsigned contract`, `Milestone due`, `Milestone overdue`, `Unverified payment`, `Closing blocker`, `Commission due`, `Commission disputed`, `Aftercare due`, `Missing association`, `Workflow error`. Where HighLevel cannot join a custom-object field to an opportunity Smart List, use a native custom-object list view or task queue; verify each view with a test record.

## 5. Workflow build cards

For each workflow, record actual HighLevel trigger/action names after building, re-entry choice, stop/suppression conditions, owner, failure route and test evidence. Keep outbound communications in draft/off until consent and test numbers work.

| ID | Trigger and guarded action | Stop/failure rule | Acceptance IDs |
|---|---|---|---|
| BC-WF-01 Intake | Form/manual inquiry → capture source, consent evidence and original/latest touch → QA/dedupe → assign owner and next action | No duplicate active deal for same transaction; unknown source to QA | C02–C05 |
| BC-WF-02 First contact | Assigned new lead → acknowledgement on permitted channel and advisor task; overdue → director escalation | Native DND, opt-out, reply, stage move or owner change suppresses stale sends | C06–C07 |
| BC-WF-03 Meeting | Calendar booking/reschedule/no-show → confirmations, reminders and correct advisor task | Attendance/cancellation ends no-show sequence | C08 |
| BC-WF-04 Offer | Offer version ready → create approval decision and director task | No external offer/reservation until matching approved version exists | C09–C10, C33 |
| BC-WF-05 Reservation | Director-approved offer → developer request/expiry task → record response | Rejection/expiry blocks legal/contract send and starts rework | C09–C11 |
| BC-WF-06 Legal | Reserved → checklist and reviewer task → approve/reject/override | Missing item or rejected decision prevents contract release | C12, C33 |
| BC-WF-07 Contract draft | Matching commercial+legal approvals → create draft from approved template | Authorized sender reviews; wrong signer/version or no email stays in draft | C12–C14 |
| BC-WF-08 Signature | Document status change → update deal evidence and next task | Declined/expired/partial signature never marks signed | C14 |
| BC-WF-09 Milestone schedule | Signed contract → create/link each expected milestone from approved local schedule | Duplicate ID/association failure to exception queue | C15–C16, C33–C34 |
| BC-WF-10 Milestone monitoring | Due/overdue or reported payment → finance verification task and alert | Only named finance/provider evidence may mark verified; no automatic bank assumption | C15–C17 |
| BC-WF-11 Closing | Required legal and payment checks passed → closing/handover checklist | Missing evidence blocks completion or creates named override record | C17 |
| BC-WF-12 Commission | Signed/closed trigger + rule version → proposed obligation records and approval tasks | No payout status without payment evidence; reversal preserves history | C18–C20, C33–C34 |
| BC-WF-13 Post-sale | Handover complete → aftercare owner, service/referral tasks | Open defect stays in queue; consent governs review request | C22 |
| BC-WF-14 Exception guard | Stage or object changes, daily sweep → detect missing prerequisites, owner, next action, association, stale blocker | Notify named manager; never silently fix money/legal decisions | C21, C24–C25, C35 |
| BC-WF-15 BluePrint feed | Optional event/evidence update → outbound read-only management message and reconciliation log | Retry/dedupe, no CRM execution writeback; disconnected CRM continues | C26–C27 |

## 6. Clone release inventory

Snapshot selection should include custom fields, three custom objects and associations, pipeline, tags, forms, landing template, calendar template, workflow folders/workflows, contract template(s), dashboards and saved views where supported. Compare assets actually present after load against the manifest; source-account edits require a snapshot refresh. Keep phone numbers, domains, senders, social/WhatsApp accounts, payment/signature connections, live templates that require external approval, users, credentials, real contacts, appointments and conversations on the **client-local reconnect checklist**. [Snapshot overview](https://help.gohighlevel.com/support/solutions/articles/48000982511-snapshots-overview) · [Custom objects in snapshots](https://help.gohighlevel.com/support/solutions/articles/155000004922-creating-custom-objects-using-snapshots).

**First live build step once signed in:** verify Agency Pro and account ownership in Agency View, then create the clean MASTER and TEST sub-accounts. Take screenshots/asset counts before and after the first clone and update C01. Until then, every item in this manifest is `planned`, not `installed`.
