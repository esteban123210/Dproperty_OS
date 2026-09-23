# AI Handoff Protocol

## Purpose

AI reduces search, summarization, drafting, reporting and workflow friction while preserving permissions and human accountability. It is embedded in BluePrint and the Second Brain; it is not an autonomous broker, lawyer, compliance officer or investment adviser.

## Standard handoff object

```yaml
handoff_id: UUID
organization_id: UUID
requester: user/service identity
authority: role + permissions + entitlement
object_refs: typed IDs and versions
trigger: event or explicit request
intent: desired outcome
source_refs: approved document/data versions
facts: verified inputs
assumptions: uncertain inputs
missing_evidence: required items
proposed_action: reversible next step
risk: low|medium|high|prohibited
approver: required role/person
due_at: UTC timestamp
writeback_target: system and record
idempotency_key: stable key
result: pending|approved|executed|rejected|failed
audit_event_id: UUID
```

## Handoff patterns

1. **Knowledge answer:** retrieve permission-filtered current sources → answer with citations/uncertainty → no writeback unless feedback.
2. **Draft:** load approved template + structured fields → validate missing data → generate labeled draft → human review → save new version only after approval.
3. **Workflow proposal:** inspect current workflow/version and blockers → propose typed tasks/field changes → preview → authorized confirmation → idempotent mutation → audit.
4. **Compliance support:** cite approved requirement and evidence → identify gaps → route to named reviewer; AI never decides.
5. **Financial report:** query authorized semantic metrics → show period/filter/definition → reconcile to ledger/model where required.
6. **Cross-system handoff:** write outbox event → adapter validates/mutates → callback/result → reconciliation and exception queue.

## Safety controls

Permission-filter before retrieval; treat retrieved text as untrusted; isolate tenants; model/provider abstraction; server-side secrets; typed tool schemas; allowlists; rate/usage limits; prompt/model/source/tool logging; human confirmation; idempotency; rollback where possible; retention controls; adversarial tests.

## Prohibited autonomous actions

Compliance approval/override, signature, payment, access grant, deletion, binding external message, commission payout approval, regulated advice, investment suitability, legal conclusion, or transaction cancellation. These require an authorized human or licensed provider.

## Evaluation suite

Grounded answer accuracy; citation correctness; freshness; cross-tenant leakage; prompt injection; field extraction; document merge accuracy; action authorization; duplicate/idempotent execution; refusal correctness; PII minimization; latency/cost. Production use requires thresholds, regression tests and incident rollback.

