# Repo Mandate Source Map

Use this file as the repo-native entry point for `investment-mandate-interpreter`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Mandate delegations, investment criteria, approval paths, and entity boundaries.
4. Owner-certified internal records and primary transaction or project documents.
5. Prior mandate interpretations only as context.

If the question is who may sign, use `decision-rights-checker`. If the question is how to reconcile commercial return and national consequence after mandate is confirmed, use `dual-mandate-balancer`. If the question is whether the opportunity itself is worth pursuing, use `investment-thesis-builder`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | End-to-end lifecycle and where authority must be established before screening. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Canonical placement of mandate interpretation in the workflow. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical skill role and ownership. |
| `01-registry/workflow_routing_matrix.csv` | Which workflows require mandate interpretation and downstream handoff. |
| `02-governance/AI_CONSTITUTION.md` | Governance boundary, traceability, and refusal rules. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier thresholds that affect the depth of mandate review. |
| `04-skills/01-governance-doctrine/decision-rights-checker/references/repo-governance-source-map.md` | The approval path once mandate is confirmed. |
| `04-skills/01-governance-doctrine/dual-mandate-balancer/SKILL.md` | The post-mandate commercial/national trade-off analysis. |
| `04-skills/06-dim-investment-management/investment-thesis-builder/SKILL.md` | The downstream opportunity thesis, which should only run after mandate fit. |
| `08-sources/SOURCE_REGISTER.md` | Source tiering and citation expectations. |

## Usage notes

- Use the source map before interpreting any DIM mandate question.
- Keep Tier 1 and Tier 2 separate; do not infer Tier 2 from Tier 1.
- If the delegation or charter is missing, treat the answer as indeterminate and escalate.
- Do not use this skill to decide who signs, only whether the action is in mandate.
