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

# Data Architecture and Canonical Entities

## Recommended baseline

Relational system of record (PostgreSQL), encrypted object storage for file bytes, permission-aware full-text/semantic index, queue/event bus for asynchronous work, immutable audit stream, and an analytics store when history/load justify it. Use stable UUIDs, decimal money with ISO currency, UTC timestamps plus relevant legal local date, explicit state machines, checksums/versioning, policy-driven soft deletion/retention, and namespaced external IDs.

## Core entities and ownership

| Owner | Entities | Rule |
|---|---|---|
| Each product | Organization, User, Membership, Role, Entitlement | Tenant-scoped access; explicit external identity mapping |
| BlankCRM / chosen CRM | Contact, Consent, Opportunity, Transaction, CommercialTask, LegalReview, Approval, Contract, PaymentMilestone, Closing, CommissionRule/Calculation, PostSaleCase | Writable commercial execution; never BluePrint-owned |
| BluePrint | SourceObservation, EvidenceReference, Verification, ReconciliationException | External source/version/time, evidence, reviewer and independent management status |
| BluePrint | ExpectedCash, ActualCashObservation, Expense, Budget, Forecast, Variance, LiabilityObservation | Management view; accounting and bank actuals retain authority |
| BluePrint | KPI, Process, SOP, Policy, Glitch, CorrectiveAction, ManagementDecision, ReportPeriod, AuditEvent | Governance and intelligence; no commercial stage commands |
| BluePrint | KnowledgeSource, AIRun, Citation, Recommendation, ManagementReview | Permission-scoped CEO/CFO/COO/CMO analysis and proposals |
| Source providers | SignatureEnvelope, LegalDocument, Settlement, LedgerEntry | Authoritative provider record; BluePrint stores authorized references |
| Other products | Inventory, Listing, Match, LearningCompletion | Developer/VAULTED/LMS authority |
| Integration layer | IntegrationAccount, WebhookEvent, ImportBatch, Retry, IdempotencyKey | Read-only commercial ingestion; no blind bidirectional sync |

## Tenant isolation

Every tenant-owned row has organization scope or an unambiguous scoped parent. Authorization is enforced server-side and at database/query boundaries. Storage prefixes are tenant-scoped. Platform support is explicit, reasoned, logged and time-bound. Cross-tenant references and benchmarks require a platform-level policy, aggregation/minimization and contract/privacy authority.

## Document/data rules

Never overwrite document bytes; create versions. Store classification, owner, parties, jurisdiction, dates/expiry, checksum, malware result and retention. Use expiring signed URLs. Legal hold overrides purge. High-risk identifiers may require field encryption/tokenization. Structured metadata remains separate from bytes.

