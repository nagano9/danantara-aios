---
name: workflow-planner
description: Converts an objective into ordered tasks, dependencies, evidence needs, specialist roles, challenge gates, approvals, and deliverables. Use when work requires multiple analytical steps or coordinated human and AI participation.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: BPI/DAM/DIM/DDMF
  cluster: 02-orchestration
  risk-tier: high
  version: "1.1.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# Workflow Planner

## Objective
Convert an objective into a governed workflow blueprint: ordered tasks, dependencies, evidence needs, specialist roles, challenge gates, approvals, deliverables, and handoff points.

## Use when
- The request needs a plan for work that spans multiple steps or multiple owners.
- The user needs a blueprint for evidence, challenge, approval, and follow-up.
- The work is material enough that planning mistakes would create downstream risk.
- The user wants the next coordinating step before execution or specialist dispatch.

## Do not use when
- The task is a simple one-step answer, formatting, or retrieval.
- The user needs exact skill selection and sequencing for the workflow graph; use `skill-chain-composer`.
- The user needs independent workstreams run in parallel; use `parallel-analysis-dispatcher`.
- The request bypasses authority, authorization, or data classification.

Do not use this skill to bypass a competent authority, replace licensed or accountable professional judgment, process unauthorized information, or make an institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
User objective; intended output; affected entities; deadline; available evidence; data classification; authority and audience.

## Dependencies
- `danantara-master-orchestrator` - for end-to-end orchestration context.
- `skill-chain-composer` - when the plan needs exact skill sequencing.
- `parallel-analysis-dispatcher` - when the plan needs parallel workstreams.
- `workflow-state-manager` - when the plan needs persistent state and handoffs.

## Authoritative sources
Start with `references/repo-workflow-source-map.md` for the repo-native planning hierarchy.

1. Law, regulation, official decision, and formal mandate.
2. Effective Danantara and entity policies, delegations, charters, standards, and controlled templates.
3. Approved workflow chains, routing matrices, and orchestration protocols.
4. Audited or owner-certified internal data and primary transaction or project documents.
5. Independent external evidence, sector benchmarks, and expert reports where relevant.
6. Prior decisions and precedents only as context; never as a substitute for current analysis.

Record source owner, title, version, effective date, retrieval date, classification, and exact location. Resolve discrepancies through `source-hierarchy-resolver`.

## Workflow
1. Classify intent, entity, risk tier, data sensitivity, decision stage, and required outcome.
2. Confirm authority, permitted tools, data access, human owners, and escalation path.
3. Decompose the work into evidence, domain, sector, model, challenge, assurance, approval, execution, and learning tasks.
4. Identify where the workflow needs `skill-chain-composer`, `parallel-analysis-dispatcher`, or `workflow-state-manager`.
5. Select and sequence non-overlapping tasks; avoid duplicate responsibilities and unauthorized tools.
6. Reconcile evidence and specialist outputs; preserve assumptions, dissent, and unresolved issues.
7. Run final assurance gates, assemble the canonical output, and route for human approval or escalation.

## Danantara Way decision rules
- Apply the ultimate test across commercial, strategic, governance, and intergenerational dimensions.
- Separate commercial return, national impact, public-service obligations, and subsidy; do not hide trade-offs.
- Identify mandate, decision rights, accountable owner, risk owner, conflicts, recusals, and required approvals.
- Quantify downside, permanent-loss risk, opportunity cost, reversibility, and conditions that would change the recommendation.
- Prefer evidence, scenarios, benchmarks, traceable calculations, and measurable outcomes over narrative assertion.
- Treat transformation capital as conditional; prohibit unsupported bailout, evergreen support, and sunk-cost justification.
- Preserve strategic confidentiality through classification and least-privilege access while maintaining an audit trail.
- State assumptions, confidence, data gaps, dissent, and unresolved tensions explicitly.

## Output contract
Primary output: workflow plan; selected skill chain; task ownership; evidence plan; approval route; consolidated output; state and audit record; next handoff.

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result as AI-assisted analysis or draft until the required human authority has approved it.

## Human approval
Workflow owner. The skill may analyze, challenge, draft, calculate, and recommend. It may not execute, bind, disclose, waive, appoint, dismiss, allocate capital, or record final approval unless a separate authorized system provides verified evidence of that human action.

## Escalation
Stop and escalate when authority is missing, evidence is materially inadequate, conflicts are unresolved, legal basis is doubtful, downside cannot be bounded, data use is unauthorized, material sources conflict, an exception is requested, or the recommendation depends on an unapproved subsidy or informal direction.

## Prohibited actions
- Do not make, imply, fabricate, or backdate institutional approval.
- Do not bypass formal decision rights, required human review, recusal, legal, risk, compliance, or information-security controls.
- Do not invent facts, sources, policy, authority, financial results, valuation inputs, or certainty.
- Do not disclose or process information outside its authorized classification, purpose, users, tools, systems, or jurisdiction.
- Do not describe unsupported political direction, informal instruction, or strategic labeling as sufficient investment rationale.
- Do not collapse commercial return and national impact into an opaque single score.
- Do not use this skill as a substitute for `skill-chain-composer` or `parallel-analysis-dispatcher` when the request needs those more specific functions.

## Quality checks
- Name, description, and output comply with the skill schema and canonical output contract.
- Material claims have traceable sources and clear fact/assumption/inference labels.
- Calculations, units, dates, currencies, and scenarios are internally consistent.
- Relevant Danantara Way principles and core tensions were explicitly tested.
- Risk owner, decision owner, approvals, conditions, and escalation path are identified.
- The plan distinguishes the planning layer from exact skill composition and parallel dispatch.
- An independent reviewer could reproduce the reasoning and understand dissent and limitations.

## Audit record
Capture request, user and role, purpose, entity, risk tier, data classification, sources, versions, tool calls, calculations, assumptions, analyses, challenge, dissent, approvals, conditions, final human decision, execution status, monitoring results, and post-decision learning.
