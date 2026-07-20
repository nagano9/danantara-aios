# Repo Project Finance Source Map

Use this file as the repo-native entry point for `project-finance-structurer`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Project cash flow, debt, reserve, covenant, and risk allocation rules.
4. Skill-local trigger cases and reference notes.
5. Prior project finance outputs only as context.

If the question is about bankability gaps, use `bankability-gap-analyzer`. If it is about public outcome, use `development-impact-assessor`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for project finance work. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Materiality and escalation thresholds. |
| `04-skills/07-ddmf-development-finance/project-finance-structurer/SKILL.md` | Skill scope and output contract. |
| `04-skills/07-ddmf-development-finance/project-finance-structurer/tests/trigger_cases.yaml` | Trigger examples for project finance cases. |
| `04-skills/07-ddmf-development-finance/project-finance-structurer/references/README.md` | Local approved reference staging area. |
| `04-skills/07-ddmf-development-finance/bankability-gap-analyzer/SKILL.md` | Bankability gap precedent. |
| `04-skills/07-ddmf-development-finance/ppp-risk-allocation/SKILL.md` | Risk allocation precedent. |

## Usage notes

- Use the source map before building a financing stack.
- Keep cash flow, security, and policy support separate.
- Do not let a debt model disguise a weak project.
