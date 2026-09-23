# Data Architecture and Canonical Entities

## Recommended baseline

Relational system of record (PostgreSQL), encrypted object storage for file bytes, permission-aware full-text/semantic index, queue/event bus for asynchronous work, immutable audit stream, and an analytics store when history/load justify it. Use stable UUIDs, decimal money with ISO currency, UTC timestamps plus relevant legal local date, explicit state machines, checksums/versioning, policy-driven soft deletion/retention, and namespaced external IDs.

## Core entities

| Domain | Entities | Key relationships |
|---|---|---|
| Identity | User, ExternalIdentity | User has memberships and provider identities |
| Tenancy | Organization, Network, Office, Membership, Role, Entitlement | User can have different role per organization |
| CRM boundary | Party, Consent, Opportunity, SourceAttribution | Qualified opportunity creates/references transaction |
| Supply | Developer, Project, Building/Phase, Property, Unit, InventorySnapshot | Developer owns project; unit/version has freshness |
| Transaction | Transaction, Participant, CommercialTerms, Milestone | Links org, parties, asset, workflow and source |
| Workflow | WorkflowDefinition/Version, Stage, Task, SLA, Exception | Instance locks version; changes are auditable |
| Compliance | Requirement, Evidence, Review, Decision, Override | Applicability and decision cite policy version |
| Content | Document, DocumentVersion, Template, SignatureEnvelope | Bytes immutable; approved-current explicit |
| Approval | ApprovalPolicy, Request, Decision | Artifact/version and assignee/reason/time |
| Finance | CommissionRule/Version, Calculation, Split, Receivable, PayoutStatus | Snapshot inputs and approvals |
| Marketplace | OpportunityListing, AccessPolicy, AccessGrant, NDA, Interest, Allocation | State/expiry/revocation and attribution |
| Learning | Course, Assignment, Completion, Certification | LMS IDs and BluePrint readiness policy |
| Platform | IntegrationAccount, WebhookEvent, OutboxEvent, AuditEvent | Delivery/retry/idempotency and actor/object change |
| AI | KnowledgeSource, SourceVersion, Conversation, Run, Citation, ToolCall, Confirmation | Permission-scoped sources and audited action |

## Tenant isolation

Every tenant-owned row has organization scope or an unambiguous scoped parent. Authorization is enforced server-side and at database/query boundaries. Storage prefixes are tenant-scoped. Platform support is explicit, reasoned, logged and time-bound. Cross-tenant references and benchmarks require a platform-level policy, aggregation/minimization and contract/privacy authority.

## Document/data rules

Never overwrite document bytes; create versions. Store classification, owner, parties, jurisdiction, dates/expiry, checksum, malware result and retention. Use expiring signed URLs. Legal hold overrides purge. High-risk identifiers may require field encryption/tokenization. Structured metadata remains separate from bytes.

