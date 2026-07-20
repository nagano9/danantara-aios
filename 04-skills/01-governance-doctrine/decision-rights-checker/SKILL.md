---
name: decision-rights-checker
description: Identifies who proposes, reviews, recommends, approves, executes, monitors, and bears accountability for a decision. Use before issuing recommendations, commitments, capital allocations, corporate actions, disclosures, or binding instructions.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: BPI/DAM/DIM/DDMF
  cluster: 01-governance-doctrine
  risk-tier: critical
  version: "1.0.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# Decision Rights Checker

## Objective
Identifies who proposes, reviews, recommends, approves, executes, monitors, and bears accountability for a decision. Use before issuing recommendations, commitments, capital allocations, corporate actions, disclosures, or binding instructions.

## Use when
- A request needs a decision-rights map: who proposes, reviews, recommends, approves, executes, monitors, and bears accountability.
- A proposal may affect capital, corporate action, disclosure, exception handling, or a binding instruction.
- The user is asking whether a path is routable at all, or whether the named decision owner is actually authorized.
- A downstream approval workflow depends on knowing the correct decision owner, risk owner, and escalation path.

## Do not use when
Do not use this skill to bypass a competent authority, replace licensed or accountable professional judgment, process unauthorized information, or make an institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
Decision request; mandate and authority documents; proposal; stakeholder and conflict disclosures; risk and impact information.

## Dependencies
mandate-authority-interpreter

## Authoritative sources
Start with `references/repo-governance-source-map.md` for the repo-native source hierarchy.
1. Applicable law, regulation, official decision, and formal mandate.
2. Effective Danantara and entity policies, delegations, charters, standards, and controlled templates.
3. Audited or owner-certified internal data and primary transaction or project documents.
4. Independent external evidence, sector benchmarks, and expert reports where relevant.
5. Prior decisions and precedents only as context; never as a substitute for current analysis.

If a mandate, delegation, charter, or source is not in the approved register or is not current, treat it as absent authority until a human owner resolves it.

Record source owner, title, version, effective date, retrieval date, classification, and exact location. Resolve discrepancies through `source-hierarchy-resolver`.

## Workflow
1. Identify the proposed decision, affected entities, materiality, and intended use.
2. Retrieve applicable mandate, law, policy, delegation, prior decisions, and evidence.
3. Apply the relevant Danantara Way doctrines and challenge questions.
4. Identify conflicts, hidden beneficiaries, downside, disclosure needs, and long-term consequences.
5. State unresolved tensions, exceptions, required approvals, and stop conditions.
6. Produce a decision-control record and route to independent review when required.

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
Primary output: Governance finding; applicable principles; authority map; conflicts; disclosure classification; stop/escalation conditions; approval requirements.

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result as AI-assisted analysis or draft until the required human authority has approved it.

## Human approval
Authorized decision owner. The skill may analyze, challenge, draft, calculate, and recommend. It may not execute, bind, disclose, waive, appoint, dismiss, allocate capital, or record final approval unless a separate authorized system provides verified evidence of that human action.

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
