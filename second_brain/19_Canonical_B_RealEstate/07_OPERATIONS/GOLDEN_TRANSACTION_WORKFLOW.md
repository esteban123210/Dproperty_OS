# Golden Transaction Workflow

| Stage | Primary action | System control | Exit evidence |
|---|---|---|---|
| 1. Qualified intake | Accept CRM opportunity or manual intake | Deduplicate, consent/source, owner, minimum fields | Party/opportunity and owner |
| 2. Workspace | Select type, asset/unit, parties, economics, dates | Workflow/jurisdiction version and generated tasks | Required parties/object linked |
| 3. Compliance | Request and review evidence | Checklist, deadlines, exceptions, named reviewer | All required decisions or approved override |
| 4. Documents | Generate/upload, review and version | Approved templates, merge validation, malware scan, immutable versions | Approved signature-ready version |
| 5. Approvals | Route commercial/legal/developer/manager decisions | Policy, prerequisites, rejection loop, reason/time | All configured approvals complete |
| 6. Contract/reservation | Sign, hold/reserve, record deposit evidence | E-sign status, deadline, inventory state | Binding milestone/evidence |
| 7. Closing | Complete financing/legal/notary/balance/handover | Checklist, blocker and escalation | Closing confirmation/final records |
| 8. Commission | Calculate/approve receivable and splits | Effective rule snapshot, adjustments, segregation | Approved calculation/payment state |
| 9. Report/archive | Update metrics and retention | Completion validation, audit, legal hold/retention | Closing summary and open exceptions |

Stage and status are separate. Stage is progression; status is active, blocked, on hold, cancelled, completed or archived. Required controls cannot be silently skipped. Overrides record permission, reason, approver, time and policy version.

## Workflow ownership

CRM owns pre-qualification. BluePrint owns the transaction. VAULTED owns gated discovery/access and creates/references the workspace. LMS owns detailed learning; BluePrint may gate roles/access using completion status. Finance/accounting validates actual receipts/payouts and returns status; BluePrint is operational commission authority, not bank ledger.

## First MVP transaction type

Choose one new-development/investment sale corridor with predictable documents and willing developer/agency partners. Configure other transaction types after the golden path works. Manual intake uses the same records and is not a second-class workflow.

## Operational SLOs to validate

Qualified handoff processed <4 business hours; integration reconciliation daily; inventory freshness by project SLA; critical document/approval blocker escalated same business day; launch support response by severity; commission discrepancy resolved with source evidence. Final SLOs require pilot data.

