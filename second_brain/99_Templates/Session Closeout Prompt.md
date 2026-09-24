---
project: B_RealEstate
title: "ChatGPT - Session Closeout Prompt"
type: template
status: Baseline Created
owner: Esteban
last_updated: 2026-07-01
source: ChatGPT baseline vault package
tags: [template, ai]
---

> [!NOTE] Verified against canon 2026-09-23
> Template is active. New notes must use canonical naming, carry a truth label (`[F] [D] [M] [A] [T] [R]`) on material claims, and use the `DRAFT → REVIEW → APPROVED → SUPERSEDED → ARCHIVED` lifecycle.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# ChatGPT - Session Closeout Prompt

Use this at the end of every work session.

```text
I am finishing this work session for the Dproperty OS project. Act as my project closeout assistant.

Based on everything we worked on in this session, generate a clear shutdown checklist so I can save everything properly before disconnecting.

Please include:

1. Session Summary
- What we worked on
- What was created or changed
- The main decisions made
- Any assumptions added or changed

2. Files to Save
- List every document, file, note, spreadsheet, deck, image, or asset created or updated
- For each one, tell me:
  - Recommended file name
  - Recommended folder path in Obsidian
  - Recommended folder path in SharePoint/Drive
  - File type
  - Current status: draft, needs review, needs design, final, archived

3. Obsidian Updates
- Which notes I should create or update
- What should go in the Master Index
- What should go in the Decision Log
- What should go in Open Questions
- What should go in the Source Map
- Which notes should be linked to each other

4. Deliverables Tracker Updates
- Which tracker rows should be updated
- New status for each deliverable
- Owner
- Priority
- Next action
- Due date if relevant
- Dependencies
- File link/location to paste into the tracker

5. External Storage Updates
- Which files should go into SharePoint/Drive instead of Obsidian
- Which files should go into Figma, Canva, PowerPoint, Excel, or another tool
- Which final/heavy files should only be linked from Obsidian

6. Version Control
- What version number each file should have
- Whether anything should be renamed
- Whether an older version should be archived

7. Open Questions
- Questions that remain unresolved
- Questions I need to ask the Dproperty owners, legal advisor, designer, developer, or team

8. Next Session Plan
- The best next task to work on
- What I should open first next time
- What context I should paste back into ChatGPT or Claude
- Any files I should upload next time

9. Final 10-Minute Shutdown Checklist
- A concise checklist I can follow immediately before closing my laptop
- Make it practical and ordered step by step

Return the answer in a format that I can paste directly into Obsidian as:
00_Start_Here/Meeting Notes/YYYY-MM-DD - Work Session Closeout.md

Also include suggested updates for:
- 00_Start_Here/Decision Log.md
- 00_Start_Here/Open Questions.md
- 00_Start_Here/Master Index.md
- Dproperty_OS_Deliverables_Tracker.xlsx
```
