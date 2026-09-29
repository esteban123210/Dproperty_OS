> [!IMPORTANT] Reconciled 2026-09-23 — read the precedence note first
> [[../01_Canon/00 - Precedence and Canonical Reconciliation|18 - Canonical Reconciliation and Precedence]] controls the vault. This folder is **one of three canonical layers**, not the sole authority:
>
> - `01_Canon/` — what the company **is**
> - `02_Offers/01_BluePrint/` — what the product **is**
> - `01_Canon/` — **this folder**: how it is **proven and financed** (finance models, data/AI architecture, operations, compliance, KPIs/gates, investor diligence)
>
> **Naming corrections that override this folder:** **Building Blocks** (not *Academy* / *B_Academy*) · **B_ Partner** (not *White-Label*) · **Dproperty Select** (not *Private Collection*) · **Developer Partnerships** (not *Developer Sales OS*).
>
> **Architecture decision — 2026-09-29 [D]:** BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions.

# System of Record and Event Taxonomy

## System-of-record matrix

| Data | Authority | Permitted replicas |
|---|---|---|
| Commercial lifecycle, legal workflow, approvals, contracts, payment milestones, closing, commissions, post-sale | BlankCRM / chosen CRM and specialist providers | Read-only sourced observations in BluePrint |
| Management budgets, expenses/forecast views, verification, KPI definitions, Glitches, policies and interventions | BluePrint | Permissioned management reports |
| Organization, roles and entitlements | Each product for its own tenant/access | Explicit mapped identities; no implied cross-product execution permission |
| Bank settlement and statutory books | Bank / payment provider / accounting | Evidence-backed actuals in BluePrint |
| Signed files and legal originals | Signature provider / legal archive | Secure evidence references |
| Learning activity | Building Blocks / LMS | Certification observations for management oversight |
| Inventory / marketplace | Developer / VAULTED | Authorized references |

BluePrint event families are observations, verification changes, reconciliation exceptions, management decisions, Glitches and audit events. Commercial stage/approval/commission events below are consumed from the CRM, not commands BluePrint executes.

## Canonical event envelope

`event_id`, `event_type`, `schema_version`, `occurred_at`, `recorded_at`, `actor_type/id`, `organization_id`, `object_type/id`, `correlation_id`, `causation_id`, `idempotency_key`, `source_system`, `data_classification`, payload, and trace/request context. Sensitive values are minimized/masked.

## Event families

- Identity/access: user_invited, membership_activated, role_changed, access_granted/revoked.
- Commercial: lead_qualified, opportunity_handoff_requested/accepted/rejected.
- Transaction: created, stage_changed, blocked, reopened, cancelled, completed.
- Evidence/content: requested, uploaded, scanned, versioned, approved, expired, shared.
- Approval/compliance: review_requested, decided, overridden, exception_raised/resolved.
- Inventory: project_published, unit_updated, snapshot_expired, allocation_confirmed.
- Finance: commission_calculated, adjustment_approved, receivable_updated, payout_status_changed.
- Learning: assigned, started, completed, certified, expired.
- Integration: webhook_received, mapped, failed, retried, reconciled.
- AI: retrieval_performed, draft_created, action_proposed, confirmed, executed, refused.

## Metric governance

Each KPI records name, business question, formula, numerator/denominator, event/table source, inclusion/exclusion, grain, timezone/currency, owner, refresh, effective version and known limitation. Dashboard labels never silently redefine a metric.

