> [!IMPORTANT] Reconciled 2026-09-23 — read the precedence note first
> [[00 - Precedence and Canonical Reconciliation|18 - Canonical Reconciliation and Precedence]] controls the vault. This folder is **one of three canonical layers**, not the sole authority:
>
> - `01_Canon/` — what the company **is**
> - `02_Offers/01_BluePrint/` — what the product **is**
> - `01_Canon/` — **this folder**: how it is **proven and financed** (finance models, data/AI architecture, operations, compliance, KPIs/gates, investor diligence)
>
> **Naming corrections that override this folder:** **Building Blocks** (not *Academy* / *B_Academy*) · **B_ Partner** (not *White-Label*) · **Dproperty Select** (not *Private Collection*) · **Developer Partnerships** (not *Developer Sales OS*).
>
> **Architecture decision — 2026-09-29 [D]:** BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions.

# Integration and Entitlement Contracts

## Shared platform contract

Each product owns its writable records and tenant permissions. Map organization, user and external object identities explicitly; shared identifiers do not imply a shared writable database. Commercial transactions, legal reviews and approvals remain in the CRM. BluePrint stores sourced observations, management verification, reconciliation and governance records.

## Entitlements

Entitlements answer which modules, limits, brands, inventory, integrations and support an organization receives. Roles answer what a user can do inside those entitlements. Attribute checks add ownership, assignment, jurisdiction, classification, workflow state, NDA/access state and transaction participation.

Minimum entitlement dimensions:

- plan and effective dates;
- enabled modules/features;
- offices/users/storage/AI/transaction limits;
- brand/white-label rights;
- inventory/project access;
- template/jurisdiction packs;
- connectors and data-export rights;
- support/SLA;
- training seats/curricula;
- commercial source and contract/order item.

## Integration contract requirements

For each connector record: provider/account, credential reference, scopes, owner, field ownership, mappings, event types, signature/authentication, idempotency, retry/backoff, rate limits, sync cursor, reconciliation, error severity, alert owner, retention, deletion, data location, subcontractors, cost and exit/export procedure.

## Current adapters

- GoHighLevel/BlankCRM: read-only lifecycle observations and evidence references; no sales-execution writeback.
- LMS/Open edX: identity/SSO, enrollment, completion, certification.
- E-signature: envelope, signer, document version, status and evidence.
- Messaging/email: notifications with secure links; no unnecessary sensitive content.
- AI provider: provider abstraction, model/prompt version, permitted source sets, tool calls, usage and retention.
- Accounting: read authoritative actuals; optional reviewed management classification export only. Commercial invoices/commissions originate in CRM/accounting, not BluePrint sales execution.

## Anti-coupling rules

Use provider adapters, canonical events and exportable data. Do not place business rules solely in vendor automation. Do not expose raw storage keys. Do not rely on one CRM/LMS/model provider for identity. Preserve a tested degraded/manual mode for critical operations.

