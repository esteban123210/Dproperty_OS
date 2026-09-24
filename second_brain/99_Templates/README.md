---
project: B_RealEstate
title: "99_Templates — Reusable Scaffolds"
type: folder_readme
status: Active
owner: Esteban
last_updated: 2026-09-23
tags: [readme, navigation]
---

> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation]] · Architecture: [[../00_Start_Here/Vault Architecture Map]]

# 99_Templates — Reusable Scaffolds

**The question this folder answers:** *What scaffold do I start from?*

## What lives here

| Template | Use for |
|---|---|
| `New Note Template` | Any new note — gives you the standard frontmatter |
| `Meeting Note Template` | Meetings and working sessions |
| `Deliverable Control Note Template` | Tracking a deliverable's version and status |
| `Session Closeout Prompt` | Running a `close working session` |
| `Record Templates` | Canonical record, decision, experiment, source and AI-handoff records |

## Standard frontmatter

```yaml
---
project: B_RealEstate
title: ""
type: ""
status: ""       # DRAFT | REVIEW | APPROVED | SUPERSEDED | ARCHIVED
owner: Esteban
last_updated: YYYY-MM-DD
tags: []
---
```

## Versioning

`v0.1` rough · `v0.5` structured · `v0.9` ready for review · `v1.0` approved · `v1.1` small update · `v2.0` major revision

## Truth labels

`[F] Fact` · `[D] Decision` · `[M] Model` · `[A] Assumption` · `[T] Target` · `[R] Required evidence`

Use one on every material claim.
