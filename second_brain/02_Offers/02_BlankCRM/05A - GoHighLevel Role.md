---
project: B_RealEstate
title: "GoHighLevel Role"
type: crm_note
status: Baseline Created
owner: Esteban
last_updated: 2026-09-29
source: ChatGPT baseline vault package
tags: [crm, gohighlevel]
---

# GoHighLevel Role

> Architecture decision: 2026-09-29 [D]. Precedence: [[00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]].

GoHighLevel is the infrastructure powering the BlankCRM product. BlankCRM is not a channel and is not proprietary CRM technology.

## Execution scope

BlankCRM executes the full commercial lifecycle: lead capture, qualification, legal workflow, approvals, contracts, payment milestones, closing, commissions, post-sale, communications, automation and commercial dashboards. BluePrint is the CRM-agnostic back-office management, governance and intelligence layer: financial health, expected vs actual cash, expenses, budgets, variance, KPI and CRM-usage oversight, process/Glitch monitoring, audit, policies, AI executive roles and management intervention. BlankCRM operates standalone. When connected, BluePrint observes, verifies, governs and recommends; authorized teams execute sales actions in BlankCRM or their chosen CRM.

## Practical implementation boundary

Configure the lead-to-post-sale workflow, departmental tasks, approval routing, document/signature integrations, expected payment milestones, commission calculations and commercial reports in BlankCRM. Test what the platform can enforce; use explicit integrated or human-controlled steps where required. Do not promise native capabilities without validation.

Accounting retains the ledger; bank/payment providers settle funds; legal archives and signature providers retain authoritative evidence. BluePrint reads authorized evidence for management oversight and never substitutes for these systems or executes CRM work.
