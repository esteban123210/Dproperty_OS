---
project: B_RealEstate
title: "GoHighLevel Setup Checklist"
type: crm_note
status: Baseline Created
owner: Esteban
last_updated: 2026-09-29
source: ChatGPT baseline vault package
tags: [crm, gohighlevel]
---

> [!INFO] Channel-scoped — verified 2026-09-23
> This folder describes the **BlankCRM product**, powered by GoHighLevel. It is independently sellable.
>
> **Canonical name:** BlankCRM — “GoHighLevel-as-product” is a legacy alias.
> GoHighLevel is third-party **infrastructure powering BlankCRM**, never a product in its own right and never “CRM propio”. BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions. See [[01 - Definition and Boundaries]].
>
> Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# GoHighLevel Setup Checklist

> **Execution order:** [[08 - Master Product Specification]] defines the product; [[12 - GoHighLevel Build Manifest]] names the exact assets; [[10 - Snapshot Release and Client Onboarding]] gives the build order; [[09 - Configuration Acceptance Tests]] defines launch proof. This short list is an orientation, not a completed configuration.

## Franchise Setup

- Account/workspace created.
- Branding configured.
- Domain/email setup.
- Pipeline stages created.
- Contact fields created.
- Lead forms created.
- Appointment calendar created.
- Welcome automation created.
- Follow-up sequences created.
- Broker pipeline created.
- Reporting dashboard configured.
- User permissions configured.

## Legacy pipeline sketch — superseded by the full-lifecycle specification

- This sketch covers early sales only. Build the opportunity stage and independent status model in [[08 - Master Product Specification#Workflow state machine]]. Legal, contract, verified payment, closing, commission and post-sale must remain visible and testable after reservation.

## Full commercial lifecycle acceptance — 2026-09-29 [D]

- Configure a clean master template and separate pilot client workspace; keep client secrets and data out of snapshots.
- Define sales, legal, administration, finance/collections and manager roles, permissions and escalation owners.
- Extend stages through legal documentation, internal approval, contract/signature, payment milestones, closing/handover, commission and post-sale. Include blocked, cancelled, refund and reopened paths.
- Configure required evidence, versioned commercial rules, approval tasks, reminders and auditable decisions. Test rejected approvals and missing prerequisites.
- Validate document, signature, payment and commission capabilities; record native, configured, integrated and manual-supported steps with costs and limitations.
- Prove standalone lead-to-post-sale completion with BluePrint disconnected.
- Optionally connect read-only lifecycle events/evidence to BluePrint; test missing, delayed, duplicated and corrected events. No BluePrint sales-execution writeback.
- Verify commercial dashboards in BlankCRM and expected-vs-actual cash/KPI/Glitch oversight in BluePrint separately.
