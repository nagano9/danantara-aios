---
name: workflow-state-manager
description: Tracks workflow stage, completed evidence, open issues, dependencies, decisions, approvals, deadlines, and handoffs. Use for long-running investments, transformations, restructurings, projects, and recurring portfolio reviews.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: BPI/DAM/DIM/DDMF
  cluster: 02-orchestration
  risk-tier: medium
  version: "1.0.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# Workflow State Manager

## Objective
Tracks workflow stage, completed evidence, open issues, dependencies, decisions, approvals, deadlines, and handoffs. Use for long-running investments, transformations, restructurings, projects, and recurring portfolio reviews.

## Use when
- A workflow spans multiple turns, multiple skills, or multiple human owners.
- Evidence, approvals, blockers, or deadlines need to persist across handoffs.
- A long-running investment, transformation, restructuring, project, or portfolio review needs a current state record.
- A request needs to know what is complete, what is blocked, what is next, and who owns each item.
- The workflow needs a durable record of stage, owner, blocker, next action, and handoff without changing the underlying verdicts.

## Do not use when
- The question is whether the analysis is good enough to decide on; use `decision-quality-gate`.
- The question is whether a claimed approval is valid; use `human-approval-orchestrator`.
- The question is whether a conflict requires recusal; use `conflict-of-interest-gate`.
- The task is only to package a record for retention; use `audit-trail-packager`.
- The work is a one-shot answer, formatting task, or unrelated request.

Do not use this skill to bypass a competent authority, replace licensed or accountable professional judgment, process unauthorized information, or make an institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
User objective; intended output; affected entities; deadline; available evidence; data classification; authority and audience.

## Dependencies
- `decision-quality-gate` - supplies the pre-decision assurance verdict.
- `human-approval-orchestrator` - supplies approval validity once a claim appears.
- `conflict-of-interest-gate` - supplies conflict and recusal findings.
- `audit-trail-packager` - preserves the milestone record.
- `parallel-analysis-dispatcher` - supplies the workstream scope when multiple owners run in parallel.
- `post-decision-learning` - consumes the closed record after the outcome is known.

## Authoritative sources
Start with `references/repo-workflow-source-map.md` for the repo-native state and routing hierarchy.
1. Applicable law, regulation, official decision, and formal mandate.
2. Effective Danantara and entity policies, delegations, charters, standards, and controlled templates.
3. Audited or owner-certified internal data and primary transaction or project documents.
4. Independent external evidence, sector benchmarks, and expert reports where relevant.
5. Prior decisions and precedents only as context; never as a substitute for current analysis.

If a workflow state conflicts with a higher-authority source, treat the state record as stale until reconciled.

Record source owner, title, version, effective date, retrieval date, classification, and exact location. Resolve discrepancies through `source-hierarchy-resolver`.

## Workflow
1. Classify intent, entity, risk tier, data sensitivity, decision stage, and required outcome.
2. Capture the current state: stage, owner, dependencies, blockers, completed evidence, open issues, deadline, and next handoff.
3. Confirm authority, permitted tools, data access, and the next human or skill owner.
4. Decompose the work into evidence, domain, sector, model, challenge, assurance, approval, and learning tasks.
5. Select and sequence non-overlapping skills; dispatch parallel work where useful.
6. Reconcile evidence and specialist outputs; preserve assumptions, dissent, and unresolved issues.
7. Update the state record after each meaningful transition, including handoff and closure status.
8. Route quality, conflict, approval, and audit questions to the appropriate specialized skill.
9. Run final assurance gates, assemble the canonical output, and route for human approval or escalation when the workflow is ready.

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
Primary output: Current stage; next stage; selected skill chain; task ownership; blockers; evidence plan; approval route; deadline; closure status; consolidated output; state and audit record.

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result as AI-assisted analysis or draft until the required human authority has approved it.

## Human approval
Program owner. The skill may analyze, challenge, draft, calculate, and recommend. It may not execute, bind, disclose, waive, appoint, dismiss, allocate capital, or record final approval unless a separate authorized system provides verified evidence of that human action.

This skill may carry the workflow state, but it may not invent a completed stage, approval, or handoff. If the handoff is not evidenced, the state remains open.

## Escalation
Stop and escalate when authority is missing, evidence is materially inadequate, conflicts are unresolved, legal basis is doubtful, downside cannot be bounded, data use is unauthorized, material sources conflict, an exception is requested, or the recommendation depends on an unapproved subsidy or informal direction.

## Prohibited actions
- Do not make, imply, fabricate, or backdate institutional approval.
- Do not bypass formal decision rights, required human review, recusal, legal, risk, compliance, or information-security controls.
- Do not invent facts, sources, policy, authority, financial results, valuation inputs, or certainty.
- Do not disclose or process information outside its authorized classification, purpose, users, tools, systems, or jurisdiction.
- Do not describe unsupported political direction, informal instruction, or strategic labeling as sufficient investment rationale.
- Do not collapse commercial return and national impact into an opaque single score.

## Quality checks
- Name, description, and output comply with the skill schema and canonical output contract.
- Material claims have traceable sources and clear fact/assumption/inference labels.
- Calculations, units, dates, currencies, and scenarios are internally consistent.
- Relevant Danantara Way principles and core tensions were explicitly tested.
- Risk owner, decision owner, approvals, conditions, and escalation path are identified.
- The state record does not replace conflict, quality, approval, or audit verdicts.
- Every open blocker has an owner, next action, and target handoff.
- An independent reviewer could reproduce the reasoning and understand dissent and limitations.

## Audit record
Capture request, user and role, purpose, entity, risk tier, data classification, sources, versions, tool calls, calculations, assumptions, analyses, challenge, dissent, approvals, conditions, final human decision, execution status, monitoring results, and post-decision learning.
