---
project: B_RealEstate
title: "AI Layer Notes"
type: product_note
status: "Supporting implementation notes v1.0"
owner: Esteban
last_updated: 2026-08-16
source: BluePrint Product Constitution
tags: [product, blueprint, ai, copilot]
---

# BluePrint Copilot — AI Layer Notes

> **Control:** [[BluePrint Product Constitution]] §10 defines the Copilot promise, AI-0 to AI-4 permission levels, guardrails and economics. [[BluePrint Golden Workflow - Wireframe and Validation]] defines its stage-by-stage context and acceptance tests.

The Copilot is included from MVP, after the minimum authorized data, templates and knowledge sources needed for each tested capability exist. It is a hyperfocused BluePrint assistant—not a general chatbot.

## MVP capabilities

- Explain how to use BluePrint and how to follow an approved procedure, with citations.
- Find approved templates, policies, manual sections and authorized records.
- Summarize a transaction, evidence set, document package or reporting period.
- Identify missing information and explain blockers.
- Draft documents from approved versioned templates and structured inputs.
- Draft internal summaries, reports, checklists and requests for information.
- Prepare low-risk tasks/status changes for explicit user confirmation.
- Explain deterministic KPIs and commission calculations using their governed definitions/results.

## Authority

- AI-0 retrieval/explanation and AI-1 governed summaries may run immediately.
- AI-2 output is always a draft.
- AI-3 shows an action preview and requires explicit confirmation.
- AI-4 remains human-only: approval, signature, payment, publication, control waivers and regulated decisions.

## Architecture rules

- Enforce tenant, role and record authorization before retrieval, prompt construction or tool calls.
- Use retrieval over authorized sources and expose citations.
- Use domain services for calculations, states, permissions, filing and audit.
- Record model, tools, sources, output status, confirmation and cost.
- Keep model/provider routing replaceable; current direction is approved GPT APIs with cost-efficient routing.
- Meter usage by tenant, include plan allowances and price controlled overage.
- Evaluate factual grounding, permission leakage, template fidelity, action safety, corrections and cost per successful task.

## Prohibited behavior

- Inventing data, clauses, assumptions, evidence or citations.
- Cross-tenant retrieval or learning from customer content without an approved program.
- Free-form commission/projection/KPI arithmetic where a governed service exists.
- Autonomous legal, compliance, investment or financial decisions.
- Sending external communications or documents without required confirmation/approval.
- Claiming an action succeeded without a returned system result.
