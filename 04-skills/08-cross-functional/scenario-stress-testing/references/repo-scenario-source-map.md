# Repo Scenario Stress Source Map

Use this file as the repo-native entry point for `scenario-stress-testing`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Scenario design, stress logic, breakpoints, and management-action rules.
4. Skill-local trigger cases and reference notes.
5. Prior scenario outputs only as context.

If the question is about model assumptions, use `financial-model-validator`. If it is about enterprise risk, use `enterprise-risk-aggregator`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Lifecycle and handoff rules. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `02-governance/DANANTARA_WAY.md` | Stress and resilience posture. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for scenario work. |
| `04-skills/08-cross-functional/scenario-stress-testing/SKILL.md` | Skill scope and output contract. |
| `04-skills/08-cross-functional/scenario-stress-testing/tests/trigger_cases.yaml` | Trigger examples for scenario cases. |
| `04-skills/08-cross-functional/scenario-stress-testing/references/README.md` | Local approved reference staging area. |
| `04-skills/08-cross-functional/financial-model-validator/SKILL.md` | Model validation precedent. |
| `04-skills/08-cross-functional/enterprise-risk-aggregator/SKILL.md` | Enterprise risk precedent. |

## Usage notes

- Use the source map before talking about severe downside.
- Keep assumptions, stress factors, and management actions separate.
- Do not present one scenario as if it were the whole future.
