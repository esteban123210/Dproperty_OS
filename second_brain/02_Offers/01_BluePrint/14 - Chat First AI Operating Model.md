---
project: B_RealEstate
title: "BluePrint Chat-First AI Operating Model"
type: ai_product_spec
status: Canonical v1.0
owner: Esteban
last_updated: 2026-09-23
tags: [blueprint, ai, chat, copilot]
---

> [!IMPORTANT] Amended 2026-09-23 — transaction spine reinstated
> [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] controls this folder. BluePrint's system of record now **begins at qualified opportunity** and includes the transaction file, compliance evidence, approvals, closing and **commission calculation**. The *property/project/unit inventory, listing and MLS* retirement from 2026-09-20 **stands permanently**.
>
> **Boundary in one line:** BluePrint owns *the deal as a governed management object*; it does not own *the property as inventory*.

# Chat-First AI Operating Model

## Principle

**Chat is the interface; structured records are the product.**

The administrator should be able to say:
- “Upload this invoice.”
- “Where is Juan’s NDA?”
- “Record this problem.”
- “Prepare the monthly report.”
- “Why are we over budget?”
- “What do I need to do before tomorrow’s meeting?”

BluePrint interprets the request and performs a governed workflow.

## Execution pipeline

Natural language/file → intent → relevant object/process → required fields → source/evidence check → permission check → duplicate check → classification → confirmation when needed → structured write → audit event → downstream updates.

## AI authority

### May do automatically
- retrieve and summarize authorized information;
- classify low-risk records;
- suggest process/SOP links;
- draft management commentary;
- detect anomalies/recurrence;
- prepare reports;
- prepare low-risk structured actions.

### Requires human confirmation
- classification with financial consequence;
- budget exception;
- policy/process change;
- sensitive HR actions;
- material record correction;
- period-close adjustment.

### Never autonomous in MVP
- move money;
- sign contracts;
- make legal/accounting judgments;
- waive controls;
- delete audit evidence;
- approve its own exception.

## UX principle

Users should not need to know the database taxonomy. The assistant knows the operating standard and asks only for missing facts/evidence.

## Differentiator

The AI is valuable because it operates over a governed company/process graph and verified multi-source data, not because it is a general chatbot.
