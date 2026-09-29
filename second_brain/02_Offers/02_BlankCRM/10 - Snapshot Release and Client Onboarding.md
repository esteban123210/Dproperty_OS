---
project: B_RealEstate
title: "BlankCRM — Snapshot Release and Client Onboarding"
type: delivery_runbook
status: Design baseline — live build pending
owner: Esteban
last_updated: 2026-09-29
tags: [blankcrm, gohighlevel, onboarding, snapshot]
---

# BlankCRM — Snapshot Release and Client Onboarding

Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · product boundary: [[01 - Definition and Boundaries]].

This is the step-by-step build order for a nontechnical founder and the person configuring GoHighLevel. Follow [[08 - Master Product Specification]] for what to build and [[09 - Configuration Acceptance Tests]] for proof. A checkbox means complete only when evidence is linked; creating an empty screen is not a pass.

## Phase 0 — decide the pilot rules before clicking in GoHighLevel

1. Name the pilot office, country, primary language, currency and time zone. Confirm its first transaction type is new-development/pre-sale, or record a revised golden path.
2. Name one owner for sales, legal, operations, finance/collections and office management. Ask each to approve their actual decision authority, documents and escalation times.
3. Write the local rules sheet: qualification criteria, lead SLAs, approved scripts, reservation authority, document checklist, contract signer, buyer/developer payment routes, closing evidence, office commission, agent split and franchise royalty if applicable. Mark unknowns as decisions, not default values.
4. Inventory the current Lovable and Webflow site forms/calendars, social accounts, CEO video, domains, email sender, phone/WhatsApp number, e-sign/payment providers and privacy/consent copy. Keep credentials out of this document.
5. Set the pilot commercial scope and price after estimating actual setup, support, usage and integration cost. The prior $750/$249 list was modelled for a narrower setup and is a **validation hypothesis** for the full product.

**Gate:** a signed-off local rules sheet and named owners. Missing bank, legal or commission authority blocks the relevant automation.

## Phase 1 — foundation and clean master

1. In Agency Pro, create `BlankCRM MASTER`, `BlankCRM TEST`, and a separate pilot office sub-account. The MASTER has no real people, money, connected client accounts or live conversations.
2. Configure brand-neutral folders/naming, time zone defaults and module prefixes. Record product version `1.0.0-draft` in the snapshot manifest.
3. Create custom fields and the three associated custom objects from [[12 - GoHighLevel Build Manifest]], with contact/person fields separate from opportunity/deal fields. Establish transaction ID, active status and next-action rules. Create explicit `unknown` and `not applicable` options where relevant.
4. Create one authoritative sales opportunity pipeline and the daily role queues. Make roles/permission presets, then test with separate synthetic user logins.
5. Add only synthetic contacts/opportunities needed to develop and test. Never snapshot or export client secrets.

**Gate:** C01, C04 and C23 design can be demonstrated in TEST after first snapshot.

## Phase 2 — acquire and qualify

1. Build a branded lead form template with consent and hidden/source fields; a CEO-video landing-page template; and a calendar template. Track original and latest source, campaign, link and form.
2. Build intake, dedupe review, routing, first-contact, appointment, no-show, opt-out and nurture workflows. Give every workflow a stop rule and error owner.
3. Connect one test Lovable page and one test Webflow page to the same field map. Use a test lead from each, checking UTMs, consent, notification, calendar and mobile experience.
4. Connect one social account at a time. Test scheduling/links only for supported channels; create a separate channel plan for WhatsApp if native publishing is unavailable.

**Gate:** C02–C08 and C28–C29 pass. No real campaign traffic until capture and opt-out work.

## Phase 3 — execute the transaction

1. Build the offer → director approval → reservation request → developer response loop.
2. Configure legal intake, named reviewer, document checklist, missing-document reminders and rejection/override record.
3. Load one approved, local contract template and test opportunity merge fields, signers, version, signature and expiry.
4. Build expected payment milestones separately from independently verified receipts. Test the real payer/payee route; agency invoice tools apply only when the agency is actually invoicing/collecting.
5. Build closing and handover checklist with blockers and evidence. Add the three distinct commission flows and post-sale queue.

**Gate:** C09–C22 pass in TEST, including rejection, missing document, late payment, cancellation and reversal.

## Phase 4 — manage and clone

1. Build commercial dashboards from the same opportunity records and compare totals to synthetic raw deals.
2. If BluePrint is present, map read-only events/evidence, reconcile duplicates/corrections and test the full path with the link disabled. BluePrint never writes transaction decisions back.
3. Refresh the master snapshot, record included assets, clone into a **fresh** TEST sub-account, reconnect only test integrations and run C01–C35. Record gaps and fixes.
4. Freeze a numbered release, save export/configuration evidence and a change log. Promote only after the acceptance gate. For existing offices, review each snapshot update for field conflicts, overwritten local customization and workflow duplication before push.

**Gate:** all critical tests pass; noncritical manual gaps have owners and dates.

## Phase 5 — pilot office onboarding

1. Create or update the pilot sub-account from the approved snapshot. Fill only its local variables: brand, domains, team, permissions, languages, SLAs, consent text, legal templates, commercial rules, numbers, email sender, calendars, social accounts and authorized integrations.
2. Migrate a small, deduplicated sample only after field mapping and consent review. Run synthetic end-to-end tests in the pilot account before contacting real leads.
3. Train each role on its daily queue and one exception. Sales rehearses an unworked lead; legal rehearses a rejected packet; finance rehearses an unverified payment; manager rehearses an escalation.
4. Activate one lead source and one transaction path. Observe daily for two weeks: capture rate, first-contact time, overdue tasks, contract errors, payment-state errors, support minutes and actual onboarding hours.
5. Hold a release review. Fix defects in MASTER first, refresh snapshot, retest in TEST, then roll the update to the pilot. Expand to other sources, offices or transaction types only after the golden path is stable.

## Client handover pack

Provide the office with a one-page daily routine by role, workflow/approval authority list, connected-account inventory, privacy/consent map, escalation contacts, known manual steps, commercial dashboard definitions and support route. Keep an agency-side version ledger: snapshot version, local overrides, live connections, test evidence, launch date, defects and change approvals.

## Current status — 2026-09-29

The architecture, build order and test protocol are written. Live construction and testing are **not started** because no authenticated GoHighLevel agency account was available in this session. The first hands-on step is Phase 0 rule collection and Agency Pro access; the first release cannot be called tested until the TEST clone passes the acceptance matrix.
