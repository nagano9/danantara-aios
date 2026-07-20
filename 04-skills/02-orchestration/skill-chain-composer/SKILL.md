---
name: skill-chain-composer
description: Selects and sequences reusable skills into an end-to-end workflow while avoiding duplicated analysis and conflicting mandates. Use after routing when a request requires several domain, sector, governance, or assurance capabilities.
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

# Skill Chain Composer

## Objective
Select and sequence reusable skills into an end-to-end workflow while avoiding duplicated analysis, conflicting mandates, and missing handoff points.

## Use when
- The request already has a route and needs exact skill sequencing.
- Multiple skills must be ordered so each one changes the decision or reduces risk.
- The workflow needs explicit serial versus parallel boundaries.
- The user needs the chain, not the underlying analysis.

## Do not use when
- The task is only to blueprint a workflow; use `workflow-planner`.
- The task is to run independent workstreams in parallel; use `parallel-analysis-dispatcher`.
- The request bypasses authority, authorization, or data classification.
- The request is a simple one-step answer or formatting task.

Do not use this skill to bypass a competent authority, replace licensed or accountable professional judgment, process unauthorized information, or make an institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
User objective; intended output; affected entities; deadline; available evidence; data classification; authority and audience.

## Dependencies
- `workflow-planner` - supplies the workflow blueprint.
- `parallel-analysis-dispatcher` - supplies the parallel segments, when needed.
- `danantara-master-orchestrator` - supplies end-to-end orchestration context.
- `workflow-state-manager` - supplies persistent state and handoffs.

## Authoritative sources
Start with `references/repo-chain-source-map.md` for the repo-native composition hierarchy.

1. Law, regulation, official decision, and formal mandate.
2. Effective Danantara and entity policies, delegations, charters, standards, and controlled templates.
3. Approved workflow chains, routing matrices, orchestration protocols, and skill boundaries.
4. Audited or owner-certified internal data and primary transaction or project documents.
5. Independent external evidence, sector benchmarks, and expert reports where relevant.
6. Prior decisions and precedents only as context; never as a substitute for current analysis.

Record source owner, title, version, effective date, retrieval date, classification, and exact location. Resolve discrepancies through `source-hierarchy-resolver`.

## Workflow
1. Confirm the objective, authority, data classification, and desired outcome.
2. Identify the mandatory skills and the skills that must not be duplicated.
3. Split the workflow into serial and parallel segments.
4. Sequence the serial chain so each skill's output is the next skill's input.
5. Identify handoff points, owners, and the human gate.
6. Preserve unresolved tensions and note where `workflow-state-manager` should track progress.
7. Produce the chain, the rationale, and the dependencies.

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
Primary output: skill chain; ordered skill list; serial versus parallel segments; overlap risks; handoff points; human gate; state and audit record.

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
- Do not use this skill as a substitute for `workflow-planner` when the task is to blueprint the workflow, or for `parallel-analysis-dispatcher` when the task is to run parallel workstreams.

## Quality checks
- The chain is necessary, sufficient, non-duplicative, and mandate-aligned.
- Serial and parallel boundaries are explicit.
- The chain terminates at a human gate.
- Each skill changes the decision or reduces risk in a way that matters.
- The plan distinguishes chain composition from workflow planning and parallel dispatch.
- An independent reviewer could reproduce the reasoning and understand dissent and limitations.

## Audit record
Capture request, user and role, purpose, entity, risk tier, data classification, sources, versions, tool calls, calculations, assumptions, analyses, challenge, dissent, approvals, conditions, final human decision, execution status, monitoring results, and post-decision learning.
