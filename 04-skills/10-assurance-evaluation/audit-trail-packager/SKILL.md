---
name: audit-trail-packager
description: Packages request, evidence, versions, analysis, assumptions, tool actions, challenges, approvals, decisions, conditions, and follow-up into a tamper-evident audit record. Use at every material workflow milestone.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: BPI/DAM/DIM/DDMF
  cluster: 10-assurance-evaluation
  risk-tier: high
  version: "1.0.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# Audit Trail Packager

## Objective
Packages request, evidence, versions, analysis, assumptions, tool actions, challenges, approvals, decisions, conditions, and follow-up into a tamper-evident audit record. Use at every material workflow milestone.

## Use when
- The workflow reaches a material milestone and the record must be preserved with evidence, versions, and decision context.
- A request, analysis, approval, decision, condition, or follow-up needs a tamper-evident audit record.
- The record must preserve request, evidence, versions, assumptions, tool actions, challenges, approvals, decisions, and remediation.
- The user needs packaging of the record, not a fresh decision about quality, conflict, or approval validity.

## Do not use when
- The question is whether the analysis is good enough to decide on; use `decision-quality-gate`.
- The question is whether a claimed approval is valid; use `human-approval-orchestrator`.
- The question is whether a conflict requires recusal; use `conflict-of-interest-gate`.
- The task is purely formatting, retrieval, or unrelated administrative work.

Do not use this skill to bypass a competent authority, replace licensed or accountable professional judgment, process unauthorized information, or make an institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
Complete artifact or workflow record; source evidence; model files; policies; approvals; logs; prior review findings.

## Dependencies
- `decision-quality-gate` - supplies the pre-decision assurance verdict.
- `human-approval-orchestrator` - supplies the approval validity verdict.
- `conflict-of-interest-gate` - supplies conflict and recusal findings.
- `workflow-state-manager` - supplies the current workflow state when packaging a milestone.
- `post-decision-learning` - supplies the learning record after the decision outcome is known.

## Authoritative sources
Start with `references/repo-audit-source-map.md` for the repo-native audit hierarchy.

1. Applicable law, regulation, official decision, and formal mandate.
2. Effective Danantara and entity policies, delegations, charters, standards, and controlled templates.
3. Decision records, evidence packs, approval records, challenge notes, and review records.
4. Audited or owner-certified internal data and primary transaction or project documents.
5. Independent external evidence, sector benchmarks, and expert reports where relevant.
6. Prior decisions and precedents only as context; never as a substitute for current analysis.

Record source owner, title, version, effective date, retrieval date, classification, and exact location. Resolve discrepancies through `source-hierarchy-resolver`.

## Workflow
1. Define the artifact, workflow, model, skill, or decision being independently reviewed.
2. Obtain the complete evidence, versions, assumptions, calculations, challenges, and approval record.
3. Test against applicable laws, policies, Danantara Way, methodology, data, security, and quality criteria.
4. Identify errors, omissions, bias, unsupported claims, conflicts, leakage, or control failures.
5. Separate findings from assertions, and separate packaging from judgment about quality or validity.
6. Rate severity, require remediation, assign owners, and determine whether the workflow must stop or escalate.
7. Issue an independent assurance result and preserve an auditable record.

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
Primary output: Independent assurance opinion; findings by severity; required remediation; stop/go/escalate recommendation; audit evidence; record completeness status.

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result as AI-assisted analysis or draft until the required human authority has approved it.

## Human approval
Records and audit owner. The skill may analyze, challenge, draft, calculate, and recommend. It may not execute, bind, disclose, waive, appoint, dismiss, allocate capital, or record final approval unless a separate authorized system provides verified evidence of that human action.

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
- The record keeps evidence, findings, approvals, and follow-up separate.
- Packaging does not invent or repair missing evidence, approval, conflict, or quality findings.
- An independent reviewer could reproduce the reasoning and understand dissent and limitations.

## Audit record
Capture request, user and role, purpose, entity, risk tier, data classification, sources, versions, tool calls, calculations, assumptions, analyses, challenge, dissent, approvals, conditions, final human decision, execution status, monitoring results, and post-decision learning.
