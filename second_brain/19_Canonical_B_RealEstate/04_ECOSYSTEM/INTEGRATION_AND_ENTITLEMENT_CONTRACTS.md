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

