> [!IMPORTANT] Reconciled 2026-09-23 — read the precedence note first
> [[../01_Canon/00 - Precedence and Canonical Reconciliation|18 - Canonical Reconciliation and Precedence]] controls the vault. This folder is **one of three canonical layers**, not the sole authority:
>
> - `01_Canon/` — what the company **is**
> - `02_Offers/01_BluePrint/` — what the product **is**
> - `01_Canon/` — **this folder**: how it is **proven and financed** (finance models, data/AI architecture, operations, compliance, KPIs/gates, investor diligence)
>
> **Naming corrections that override this folder:** **Building Blocks** (not *Academy* / *B_Academy*) · **B_ Partner** (not *White-Label*) · **Dproperty Select** (not *Private Collection*) · **Developer Partnerships** (not *Developer Sales OS*).
>
> **BluePrint is both halves:** the transaction/commission spine from qualified opportunity **and** the management-control layer (budgets, variance, process assurance, Glitches, period close). It never owns property/unit inventory, listings or MLS.

# System of Record and Event Taxonomy

## System-of-record matrix

| Data | Authority | Permitted replicas |
|---|---|---|
| Marketing consent, campaign, appointment, early lead stage | CRM/BlankCRM | Minimal reference in BluePrint |
| Organization, roles, entitlements, transaction and workflow | BluePrint | Analytics and limited CRM status |
| Compliance evidence, document versions, approvals, audit | BluePrint | Secure external share/reference only |
| Detailed course content/activity | LMS | Completion/certification summary in BluePrint |
| Required training/readiness gate | BluePrint policy | Assignment in LMS |
| Project/unit truth | Developer-approved project module | VAULTED/BluePrint read model |
| VAULTED access/NDA/interest | VAULTED/shared platform | Transaction reference in BluePrint |
| Bank receipt/payment | Accounting/bank/processor | Operational status in BluePrint |
| Approved SOP/policy/template metadata | Second Brain/BluePrint knowledge service | Permissioned Copilot index |
| Product analytics events | Event pipeline | Warehouse/defined reports |

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

