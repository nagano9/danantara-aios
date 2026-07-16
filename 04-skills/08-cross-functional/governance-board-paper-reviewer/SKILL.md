---
name: governance-board-paper-reviewer
description: Reviews board and committee papers for decision clarity, authority, evidence, alternatives, risks, conflicts, dissent, financial impact, conditions, and auditability. Use before circulation or meeting submission.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: BPI/DAM/DIM/DDMF
  cluster: 08-cross-functional
  risk-tier: high
  version: "1.0.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# Governance Board Paper Reviewer

## Objective
Reviews board and committee papers for decision clarity, authority, evidence, alternatives, risks, conflicts, dissent, financial impact, conditions, and auditability. Use before circulation or meeting submission.

## Use when
Reviews board and committee papers for decision clarity, authority, evidence, alternatives, risks, conflicts, dissent, financial impact, conditions, and auditability. Use before circulation or meeting submission.

## Do not use when
Do not use this skill to bypass a competent authority, replace licensed or accountable professional judgment, process unauthorized information, or make an institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
Decision context; specialist documents and data; applicable standards; stakeholder inputs; assumptions; requested level of assurance.

## Dependencies
None mandatory beyond the common governance kernel; invoke additional skills according to context.

## Authoritative sources
1. Applicable law, regulation, official decision, and formal mandate.
2. Effective Danantara and entity policies, delegations, charters, standards, and controlled templates.
3. Audited or owner-certified internal data and primary transaction or project documents.
4. Independent external evidence, sector benchmarks, and expert reports where relevant.
5. Prior decisions and precedents only as context; never as a substitute for current analysis.

Record source owner, title, version, effective date, retrieval date, classification, and exact location. Resolve discrepancies through `source-hierarchy-resolver`.

## Workflow
1. Define the functional question, decision context, scope, materiality, and governing standards.
2. Collect approved data, documents, benchmarks, and stakeholder inputs with lineage.
3. Perform the specialist analysis and quantify implications under base and downside conditions.
4. Map dependencies with commercial, strategic, governance, impact, technology, and execution objectives.
5. Identify controls, exceptions, accountable owners, approvals, and independent review needs.
6. Produce a decision-ready specialist module using the canonical output contract.

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
Primary output: Specialist analysis module; scenarios; risks and controls; recommendations; exceptions; approval and assurance requirements.

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result as AI-assisted analysis or draft until the required human authority has approved it.

## Human approval
Company secretary/governance owner. The skill may analyze, challenge, draft, calculate, and recommend. It may not execute, bind, disclose, waive, appoint, dismiss, allocate capital, or record final approval unless a separate authorized system provides verified evidence of that human action.

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
- An independent reviewer could reproduce the reasoning and understand dissent and limitations.

## Audit record
Capture request, user and role, purpose, entity, risk tier, data classification, sources, versions, tool calls, calculations, assumptions, analyses, challenge, dissent, approvals, conditions, final human decision, execution status, monitoring results, and post-decision learning.
