> [!IMPORTANT] Reconciled 2026-09-23 — read the precedence note first
> [[../../18_Ecosystem/18 - Canonical Reconciliation and Precedence|18 - Canonical Reconciliation and Precedence]] controls the vault. This folder is **one of three canonical layers**, not the sole authority:
>
> - `18_Ecosystem/` — what the company **is**
> - `04_Product/BluePrint/` — what the product **is**
> - `19_Canonical_B_RealEstate/` — **this folder**: how it is **proven and financed** (finance models, data/AI architecture, operations, compliance, KPIs/gates, investor diligence)
>
> **Naming corrections that override this folder:** **Academy** (not *Building Blocks*) · **B_ Partner** (not *White-Label*) · **Dproperty Select** (not *Private Collection*) · **Developer Partnerships** (not *Developer Sales OS*).
>
> **BluePrint is both halves:** the transaction/commission spine from qualified opportunity **and** the management-control layer (budgets, variance, process assurance, Glitches, period close). It never owns property/unit inventory, listings or MLS.

# Integration and Entitlement Contracts

## Shared platform contract

Every module reuses identity, organization, membership, role, entitlement, project/property/unit, party, transaction, document, task, approval, event, audit and analytics primitives. A module may extend these entities but may not create a second customer, organization or transaction identity without an approved architecture decision.

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

- GoHighLevel/BlankCRM: early pipeline and status writeback.
- LMS/Open edX: identity/SSO, enrollment, completion, certification.
- E-signature: envelope, signer, document version, status and evidence.
- Messaging/email: notifications with secure links; no unnecessary sensitive content.
- AI provider: provider abstraction, model/prompt version, permitted source sets, tool calls, usage and retention.
- Accounting/export: approved closing/commission/invoice data only; no hidden accounting authority.

## Anti-coupling rules

Use provider adapters, canonical events and exportable data. Do not place business rules solely in vendor automation. Do not expose raw storage keys. Do not rely on one CRM/LMS/model provider for identity. Preserve a tested degraded/manual mode for critical operations.

