---
project: B_RealEstate
title: "BlankCRM — Configuration Acceptance Tests"
type: acceptance_plan
status: Design review complete — live tests pending
owner: Esteban
last_updated: 2026-09-29
tags: [blankcrm, qa, gohighlevel, snapshot]
---

# BlankCRM — Configuration Acceptance Tests

Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · product boundary: [[01 - Definition and Boundaries]].

## What has and has not been tested

On 2026-09-29 the proposed configuration was reviewed against the canonical BlankCRM/BluePrint boundary, the Dproperty lead, pre-sale, resale and commission processes, and the failure cases below. **No live GoHighLevel test has run:** the available browser reached the sign-in page, not an authenticated agency account. Every case below is therefore `PENDING LIVE`, even where the design contains the control. Do not call the product or snapshot production-ready until a tester records evidence in a fresh TEST sub-account.

Test with synthetic contacts, units, amounts, document templates and messages. No real client data or outbound messages during the first pass. For each case record snapshot version, office, tester, date, input, observed output, screenshot/export link, result (`pass`, `fail`, `blocked`) and defect owner. Re-run failed cases and the full critical path after fixes.

## Release 1 test matrix

| ID | Priority | Scenario and expected result | Design control | Live result |
|---|---|---|---|---|
| C01 | Critical | Apply snapshot to empty TEST account; assets, names, workflow versions and permissions match manifest; no personal data or client secrets appear | Master/TEST topology | Pending |
| C02 | Critical | Create a lead from each published form and manual entry; source, campaign, consent, owner and first-action deadline persist | Intake/attribution | Pending |
| C03 | Critical | Submit the same person twice; no duplicate outreach or second active opportunity is silently created for the same transaction | Dedupe/transaction ID | Pending |
| C04 | Critical | One person buys two units; two distinct opportunity records and economics remain independent | Opportunity-scoped deal fields | Pending |
| C05 | High | Blank/invalid contact or UTM data enters; missing values show as unknown and trigger QA, never invented attribution | Explicit unknown/QA | Pending |
| C06 | Critical | Lead opts out of WhatsApp/email/SMS; prohibited outreach stops promptly while allowed internal tasks continue | Channel consent/suppression | Pending |
| C07 | High | New lead is unassigned or untouched past pilot SLA; escalation goes to director and appears in overdue queue | SLA and owner rules | Pending |
| C08 | High | Book, reschedule, cancel and miss a meeting; reminders do not duplicate and no-show path does not run after attendance | Calendar/re-entry conditions | Pending |
| C09 | Critical | Advisor tries to send offer or reservation before director approval; request is held, decision logged, director notified | Commercial approval gate | Pending |
| C10 | Critical | Director rejects offer; opportunity returns to rework with reason/version; no developer reservation is sent | Rejection loop | Pending |
| C11 | Critical | Reserved unit expires or developer rejects; unit/contract path pauses, client and owner tasks update, stale offers do not proceed | Reservation exception | Pending |
| C12 | Critical | Legal packet missing required item; contract cannot be sent as approved, blocker/owner visible; override requires named authority/reason | Legal checklist/override | Pending |
| C13 | Critical | Wrong signer or outdated contract version; send is stopped or escalated, latest approved version traceable | Contract version/signers | Pending |
| C14 | Critical | Signature is declined, expires or is partially complete; deal does not become signed/closed | Signature status | Pending |
| C15 | Critical | Expected buyer-to-developer installment exists but bank has not confirmed; status remains expected/reported, not received | Expected vs verified fields | Pending |
| C16 | Critical | Payment is partial, late, disputed or refunded; amount/status/evidence and escalation reflect actual state | Milestone ledger | Pending |
| C17 | Critical | Closing is attempted with unresolved required receipt, legal check or handover item; blocker/override is visible and auditable | Closing gate | Pending |
| C18 | Critical | Developer owes office commission; agent payout and HQ royalty are separate obligations with separate status/evidence | Three commission flows | Pending |
| C19 | Critical | Commission rate changes after offer; calculation uses the recorded effective rule/version, with approved adjustment if needed | Rule snapshot | Pending |
| C20 | High | Deal is cancelled after payment; refund and commission reversal tasks appear; original evidence remains | Cancellation/reversal | Pending |
| C21 | High | Deal is reopened; owner, reason and new next action are required; old signed/paid evidence remains visible | Reopen audit | Pending |
| C22 | High | Handover completes but service defect remains; post-sale owner and due task stay open | Post-sale queue | Pending |
| C23 | Critical | Advisor, director, legal and finance sign in separately; each sees only permitted actions and office records | Role/tenant isolation | Pending |
| C24 | Critical | Workflow/API advances a stage without UI-required fields; audit/guard detects missing prerequisite and alerts owner | Bypass detection | Pending |
| C25 | High | Workflow retries or webhook duplicates arrive; no duplicate contract, invoice, notification or commission obligation | Idempotency/error queue | Pending |
| C26 | Critical | BluePrint integration is disconnected; lead-to-post-sale flow and commercial dashboards still work | Standalone architecture | Pending |
| C27 | High | Optional BluePrint feed receives late/duplicate/corrected event; reconciliation log and management view correct without writing into CRM execution | Read-only integration | Pending |
| C28 | High | Publish form/calendar on both Lovable and Webflow test pages; capture, consent, UTMs, booking and mobile layout work | Website integration | Pending |
| C29 | High | Connect each intended social account; scheduling, source links and attribution work only for channels confirmed supported | Channel capability check | Pending |
| C30 | High | AI receives legal, discount, financing and payment-dispute prompts; it hands off and makes no binding claim | AI guardrails | Pending |
| C31 | Critical | Refresh snapshot after a master fix, clone again and compare; new assets appear, tenant-specific settings and data stay isolated | Release manifest/update protocol | Pending |
| C32 | High | Management dashboard totals agree with raw test deals for lead conversion, stage age, overdue milestones and commission states | Commercial reporting | Pending |
| C33 | Critical | Create two approvals, three payment milestones and three commission obligations for one opportunity; all are associated to that deal, visible in the correct role queues, and absent from another deal for the same contact | One-to-many custom-object associations | Pending |
| C34 | Critical | Submit duplicate event/record IDs; unique object IDs prevent duplicate obligations, while a second legitimate milestone with a new ID is accepted | Unique custom-object IDs/idempotency | Pending |
| C35 | Critical | Create an approval or milestone without an opportunity association, then advance a stage through workflow/API; the exception guard catches both missing link and missing prerequisite | Association/guard audit | Pending |
| C36 | Critical | Clone the country-neutral master for the Panama presale pilot; confirm approved local reservation amount, document checklist, contract authority, buyer-to-developer payment route and three commission rules are present only in the pilot, with no Panama-only values forced into the master | Localized pilot rules / clone boundary | Pending |

## End-to-end golden path

Run a single synthetic new-development transaction in TEST: social link → CEO video landing page → consented form → owner notification → qualification → meeting → project presentation → approved offer → approved reservation → legal packet → approved contract → signature → expected milestone → independently verified receipt → closing/handover → office commission receivable → agent payout and optional HQ royalty → post-sale follow-up. Capture a screen or export at every handoff. Then run the same path with BluePrint disconnected. Both paths must work; BluePrint only observes the optional feed.

## Release decision

- **Block launch** on any failed critical case; on unverified consent, tenant isolation, contract authority or money-state logic; or on any workflow that silently bypasses a required named approval.
- **Pilot-only** may carry a noncritical manual step if a named owner, due time, evidence field, client disclosure and remediation date are documented.
- **Promote** only after all critical cases pass in a fresh TEST clone, the pilot team signs off the local legal/payment/commission rules, and the first real transaction is monitored with daily exception review.

## Design review findings

The blueprint covers the full commercial journey and distinguishes expected from verified cash, stage from evidence, and each commission obligation. The principal untested assumptions are native document/signature capability in this account, whether permission granularity supports the proposed roles, form/calendar behavior on the two published website platforms, social/WhatsApp channel connections, and payment authority. Live tests decide whether each is native, integrated or human-confirmed. Conditional opportunity-field requirements alone cannot guard workflow/API updates; C24 explicitly tests that path.
