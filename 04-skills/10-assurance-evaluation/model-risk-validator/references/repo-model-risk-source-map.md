# Repo Model Risk Source Map

Use this file as the repo-native entry point for `model-risk-validator`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved assurance artifacts and controlled templates.
3. Model design, calibration, limitation, and validation rules.
4. Skill-local trigger cases and reference notes.
5. Prior model-risk outputs only as context.

If the question is about formulas, use `financial-model-validator`. If it is about scenario behavior, use `scenario-stress-testing`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Assurance lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for model-risk review. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Materiality and escalation thresholds. |
| `04-skills/10-assurance-evaluation/model-risk-validator/SKILL.md` | Skill scope and output contract. |
| `04-skills/10-assurance-evaluation/model-risk-validator/tests/trigger_cases.yaml` | Trigger examples for model-risk cases. |
| `04-skills/10-assurance-evaluation/model-risk-validator/references/README.md` | Local approved reference staging area. |
| `04-skills/08-cross-functional/financial-model-validator/SKILL.md` | Financial model precedent. |
| `04-skills/08-cross-functional/scenario-stress-testing/SKILL.md` | Stress-testing precedent. |

## Usage notes

- Use the source map before relying on a model in a decision.
- Keep design, calibration, and limitation separate.
- Do not accept accuracy claims without validation scope.
