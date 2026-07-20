# Repo Dual Mandate Source Map

Use this file as the repo-native entry point for `dual-mandate-balancer`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Mandate scope, approval rights, and competing-obligation handling.
4. Skill-local trigger cases and reference notes.
5. Prior dual-mandate outputs only as context.

If the question is about balancing two mandates, use `decision-rights-checker`. If the question is about mandate scope itself, use `investment-mandate-interpreter`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/AI_CONSTITUTION.md` | Non-negotiable governance boundary and refusal rules. |
| `02-governance/DANANTARA_WAY.md` | Priority framing when mandates compete. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Escalation and approval thresholds. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical skill role in the repo. |
| `01-registry/PRINCIPLE_SKILL_COVERAGE.md` | Principle-to-skill mapping for mandate conflicts. |
| `01-registry/workflow_routing_matrix.csv` | Where this skill sits in the workflow. |
| `04-skills/01-governance-doctrine/dual-mandate-balancer/SKILL.md` | Skill intent and operating boundaries. |
| `04-skills/01-governance-doctrine/dual-mandate-balancer/tests/trigger_cases.yaml` | Trigger examples for dual-mandate cases. |
| `04-skills/01-governance-doctrine/dual-mandate-balancer/references/README.md` | Where approved local references belong. |
| `04-skills/01-governance-doctrine/decision-rights-checker/references/repo-governance-source-map.md` | Existing decision-rights precedent. |
| `04-skills/06-dim-investment-management/investment-mandate-interpreter/references/repo-mandate-source-map.md` | Mandate interpretation pattern. |

## Usage notes

- Use the source map before merging two obligations into one answer.
- Keep approval authority separate from mandate interpretation.
- Do not infer authority from urgency.
