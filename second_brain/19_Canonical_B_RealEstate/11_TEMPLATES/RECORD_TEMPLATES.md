# Record Templates

## Product record

```markdown
# [Product]
Owner / approver / status / effective date / review date
## Executive definition
## Customer and JTBD
## In scope / out of scope
## Workflow and system-of-record boundary
## Business model canvas and pricing
## Data, permissions and AI
## Metrics and unit economics
## Roadmap and acceptance
## Risks, dependencies and kill criteria
## Sources and decisions
```

## Decision record

```markdown
# DEC-[ID] — [Decision]
Date / owner / approver / status / effective date
Context and decision required
Options and evidence
Decision and rationale
Financial, customer, legal, data, security and operating impact
Downstream records to update
Reversal/review trigger
```

## Experiment record

```markdown
# EXP-[ID] — [Hypothesis]
Owner / dates / budget / segment
Hypothesis and riskiest assumption
Method and controls
Primary metric, threshold and sample
Observed results and raw evidence
Decision: proceed / iterate / stop
Learning and next action
```

## Source note

```markdown
# SRC-[ID] — [Title]
Source owner/publisher, URL/file ID, version/date, retrieved date
Authority and permitted use
Summary (paraphrased)
Claims supported and limitations
Related decisions/records
Expiry/review date
```

## AI handoff

Use the schema in `08_DATA_AI/AI_HANDOFF_PROTOCOL.md`. A handoff is incomplete without authority, exact source versions, truth labels, missing evidence, approver, writeback target, idempotency key and result/audit ID.

## Monthly model change log

```markdown
Model/version and date
Actual period closed
Inputs changed and evidence
Formula/structure changes
Base/downside/upside impact
Runway and funding impact
Approver
Prior version retained at
```

