---
name: conflict-of-interest-gate
description: Detects actual, potential, and perceived conflicts of interest, related parties, hidden beneficiaries, influence channels, and recusal needs. Use for appointments, procurement, investments, partnerships, restructuring, transactions, and material exceptions.
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

# Conflict Of Interest Gate

## Objective
Detects actual, potential, and perceived conflicts of interest, related parties, hidden beneficiaries, influence channels, and recusal needs. Use for appointments, procurement, investments, partnerships, restructuring, transactions, and material exceptions.

## Use when
- The request needs a conflict check before a material decision, exception, or approval.
- The work involves appointments, procurement, investments, partnerships, restructuring, transactions, or other material exceptions.
- The analysis must identify actual, potential, and perceived conflicts, related parties, hidden beneficiaries, influence channels, and recusal needs.
- The user needs a governance finding about conflict risk, not the final approval or mandate decision.

## Do not use when
- The question is whether Danantara may act at all; use `investment-mandate-interpreter` or `mandate-authority-interpreter`.
- The question is who must approve and whether the approval is valid; use `human-approval-orchestrator`.
- The question is whether the analysis is good enough to decide on; use `decision-quality-gate`.
- The work is purely administrative, formatting, or unrelated to governance risk.

Do not use this skill to bypass a competent authority, replace licensed or accountable professional judgment, process unauthorized information, or make an institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
Decision request; mandate and authority documents; proposal; stakeholder and conflict disclosures; risk and impact information.

## Dependencies
- `decision-rights-checker` - identifies who proposes, reviews, and approves.
- `decision-quality-gate` - confirms the analysis is good enough to route.
- `human-approval-orchestrator` - validates the approval once it is claimed.
- `audit-trail-packager` - receives the governance record when the workflow requires packaging.

## Authoritative sources
Start with `references/repo-conflict-source-map.md` for the repo-native conflict review hierarchy.

1. Applicable law, regulation, official decision, and formal mandate.
2. Effective Danantara and entity policies, delegations, charters, standards, and controlled templates.
3. Workflow routing matrices, approval maps, and orchestration protocols.
4. Audited or owner-certified internal data and primary transaction or project documents.
5. Independent external evidence, sector benchmarks, and expert reports where relevant.
6. Prior decisions and precedents only as context; never as a substitute for current analysis.

Record source owner, title, version, effective date, retrieval date, classification, and exact location. Resolve discrepancies through `source-hierarchy-resolver`.

## Workflow
1. Identify the proposed decision, affected entities, materiality, and intended use.
2. Retrieve applicable mandate, law, policy, delegation, routing, prior decisions, and evidence.
3. Apply the relevant Danantara Way doctrines and challenge questions.
4. Identify actual, potential, and perceived conflicts, hidden beneficiaries, downside, disclosure needs, and long-term consequences.
5. Separate conflict findings from approval validity, mandate, and analysis-quality questions.
6. State unresolved tensions, exceptions, recusal needs, required approvals, and stop conditions.
7. Produce a decision-control record and route to independent review when required.

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
Primary output: Governance finding; applicable principles; authority map; conflicts; related parties; recusal needs; disclosure classification; stop/escalation conditions; approval requirements.

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result as AI-assisted analysis or draft until the required human authority has approved it.

## Human approval
Independent governance reviewer. The skill may analyze, challenge, draft, calculate, and recommend. It may not execute, bind, disclose, waive, appoint, dismiss, allocate capital, or record final approval unless a separate authorized system provides verified evidence of that human action.

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
- Conflict findings are separated from authority, approval, and analysis-quality findings.
- Actual, potential, and perceived conflicts are distinguished explicitly.
- An independent reviewer could reproduce the reasoning and understand dissent and limitations.

## Audit record
Capture request, user and role, purpose, entity, risk tier, data classification, sources, versions, tool calls, calculations, assumptions, analyses, challenge, dissent, approvals, conditions, final human decision, execution status, monitoring results, and post-decision learning.
