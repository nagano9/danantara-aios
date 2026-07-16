---
name: talent-meritocracy-assessor
description: Assesses whether critical roles are filled by people with the competence, integrity, track record, leadership capacity, and mission fit required for the problem. Use for board, executive, transformation, and succession decisions.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: DAM/BPI
  cluster: 05-dam-active-ownership
  risk-tier: critical
  version: "1.0.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# Talent Meritocracy Assessor

## Objective
Assesses whether critical roles are filled by people with the competence, integrity, track record, leadership capacity, and mission fit required for the problem. Use for board, executive, transformation, and succession decisions.

## Use when
Assesses whether critical roles are filled by people with the competence, integrity, track record, leadership capacity, and mission fit required for the problem. Use for board, executive, transformation, and succession decisions.

## Do not use when
Do not use this skill to bypass a competent authority, replace licensed or accountable professional judgment, process unauthorized information, or make an institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
Portfolio-company data; strategy; financials; operations; governance; talent; asset base; market benchmarks; ownership constraints.

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
1. Establish ownership intent, strategic role, baseline performance, and intervention thesis.
2. Diagnose financial, operational, governance, market, talent, technology, and portfolio issues.
3. Quantify value-creation, synergy, restructuring, or rationalization options and their costs.
4. Test parenting advantage, conditionality, management accountability, and alternative ownership paths.
5. Run downside, execution, stakeholder, legal, and independent challenge reviews.
6. Produce a measurable ownership action plan with capital gates, milestones, triggers, and exit criteria.

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
Primary output: Ownership thesis; quantified value-creation or restructuring plan; capital conditionality; management accountability; triggers; exit pathway.

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result as AI-assisted analysis or draft until the required human authority has approved it.

## Human approval
Authorized nomination body. The skill may analyze, challenge, draft, calculate, and recommend. It may not execute, bind, disclose, waive, appoint, dismiss, allocate capital, or record final approval unless a separate authorized system provides verified evidence of that human action.

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
