---
project: B_RealEstate
title: "BluePrint Chat-First AI Operating Model"
type: ai_product_spec
status: Canonical v1.0
owner: Esteban
last_updated: 2026-09-29
tags: [blueprint, ai, chat, copilot]
---

> [!IMPORTANT] Architecture corrected 2026-09-29 [D]
> BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions. See [[00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]].
>
> **Boundary in one line:** BluePrint owns the management verification record, policies and oversight; the CRM owns deal execution and commercial records.

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
