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

# Knowledge Ingestion, Permissions, and Retention

## Ingestion pipeline

Source registration → ownership/rights check → malware/content-type validation → classification → metadata and organization scope → extract/OCR → chunk with structural context → version/checksum → human approval → permission-aware index → quality test → publish → expiry/review → supersede/archive/purge.

## Required source metadata

Title, source ID, version, owner, organization, jurisdiction, language, document type, authority level, truth label, effective/review/expiry dates, confidentiality, data classes, permitted audiences, legal basis/contract rights, source URL/file, related entities, supersedes/is superseded by, and checksum.

## Approved knowledge classes

- Public/marketing approved.
- Internal operating.
- Customer/tenant confidential.
- Transaction restricted.
- Legal/compliance privileged or restricted.
- HR/finance highly restricted.
- Security secrets—never indexed in general retrieval.

## Retention

Retention is policy/jurisdiction/object specific. Store policy version and disposal date; legal hold suspends purge. Deletion requests trigger identity verification, applicable-law/contract analysis, dependency search, processor notification, audit and completion evidence. Backups follow documented expiry rather than immediate ad hoc deletion.

## AI use rules

Only approved source versions enter production retrieval. Customer content is not used to train global models without explicit authority. Provider retention/training settings and subprocessors are recorded. Citations resolve to the exact source/version, not merely a filename. Superseded or expired material is excluded by default but remains available to authorized auditors.

## Quality review

Sample retrieval by role/tenant; stale/superseded exclusion; citation resolution; sensitive-data leakage; duplicate/conflicting source detection; missing owner/review date; answer completeness; and false authority. Failed records are quarantined until corrected.

