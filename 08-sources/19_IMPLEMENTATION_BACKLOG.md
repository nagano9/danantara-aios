# 19_IMPLEMENTATION_BACKLOG

This ledger receives every `indeterminate`, `void`, `stop`, or blocked decision
cell that the estate surfaces during real use. It is a work tracker, not a
source of authority.

## Purpose

- capture the missing cell, its owner, and the question it would answer
- rank by blocking pressure, not by workshop opinion
- keep work items tied to actual decision failures or missing evidence
- provide the sink for Arc 3 of `post-decision-learning`

## Columns

| Column | Meaning |
|---|---|
| `ID` | Stable backlog item identifier |
| `Source Gap / Evidence` | The missing document, clause, dataset, or control |
| `Initiative / Action` | The concrete action needed to close the gap |
| `Blocker / Decision Needed` | The question that cannot be answered yet |
| `Accountable Owner` | Named owner of the missing cell |
| `Priority` | Relative blocking pressure, not personal urgency |
| `Target Wave` | When the item should be addressed |
| `Status` | `open`, `in_progress`, `blocked`, or `closed` |
| `Notes` | Anything that helps the owner close the item |

## Seed backlog

| ID | Source Gap / Evidence | Initiative / Action | Blocker / Decision Needed | Accountable Owner | Priority | Target Wave | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| IB-001 | BPI Danantara Dewan Pengawas charter | Retrieve and pin the authenticated charter with effective date | Who supervises what, and with which limits? | Governance owner | 1 | Wave 1 | open | Required for governance boundary clarity |
| IB-002 | Badan Pelaksana delegation of authority matrix | Retrieve and pin the operative DOA with clause references | May DIM, DAM, or DDMF act alone on a given threshold? | Legal/governance owner | 1 | Wave 1 | open | Required by `mandate-authority-interpreter` and `decision-rights-checker` |
| IB-003 | DIM Investment Committee charter and quorum rules | Retrieve and pin the committee charter and threshold matrix | Which forum approves which DIM action? | DIM committee owner | 1 | Wave 1 | open | Required by `investment-committee-memo` and `human-approval-orchestrator` |
| IB-004 | DAM active-ownership and transformation policy | Retrieve and pin the policy that governs active ownership interventions | What intervention path is allowed before ownership action? | DAM portfolio owner | 2 | Wave 1 | open | Needed for value creation and turnaround work |
| IB-005 | DDMF development-finance and additionality policy | Retrieve and pin the policy that defines additionality and catalytic capital use | When is intervention additional rather than duplicative? | DDMF investment owner | 2 | Wave 1 | open | Needed for catalytic and blended finance decisions |
| IB-006 | Investment policy statement and risk limits | Retrieve and pin mandate limits, concentration, liquidity, and exclusions | Is the opportunity inside the investable universe? | Portfolio/risk owner | 1 | Wave 1 | open | Needed for portfolio, return, and risk skills |
| IB-007 | Valuation policy and model-approval standard | Retrieve and pin the valuation policy, model approval, and review rules | Which valuation methods are acceptable and who validates them? | Finance/model owner | 2 | Wave 2 | open | Needed for valuation and model challenge skills |
| IB-008 | Conflict-of-interest, related-party, and recusal policy | Retrieve and pin the COI and recusal framework | Who must recuse, disclose, or escalate? | Compliance owner | 1 | Wave 1 | open | Needed for integrity and independence checks |
| IB-009 | Data classification standard and approved-AI-environment policy | Retrieve and pin the data use and environment rules | Which data can be processed where, and by whom? | Security/data owner | 1 | Wave 1 | open | Needed before most orchestration workflows can proceed |
| IB-010 | Procurement and integrity due-diligence standard | Retrieve and pin procurement and due-diligence controls | What sourcing and counterparty checks are mandatory? | Procurement/compliance owner | 2 | Wave 2 | open | Needed for commercial and integrity workflows |
| IB-011 | Whistleblowing and escalation procedure | Retrieve and pin the escalation route and protections | Where do exceptions, leaks, and misconduct go? | Governance/risk owner | 2 | Wave 2 | open | Needed for exception routing and assurance |
| IB-012 | Operative entity model aligned to authenticated PP 19/2026 | Confirm the current holding and operating-entity structure | What is the actual entity architecture after amendment? | Legal/governance owner | 1 | Wave 1 | open | Must be resolved before hard-coding entity assumptions |
| IB-013 | Falsifiable prediction field in the decision log workbook | Add workbook columns and validation for recorded predictions | How will post-decision learning score the decision? | Workbook owner | 1 | Wave 1 | open | External workbook change request CR-001 |

## Operating rules

- Every indeterminate verdict should create or update exactly one backlog item.
- A backlog item without an owner is not ready to act on.
- Priority is measured by how many decisions the gap blocks.
- When the source is real, move it out of backlog and into the source register.

