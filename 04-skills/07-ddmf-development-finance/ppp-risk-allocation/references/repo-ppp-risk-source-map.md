# Repo PPP Risk Allocation Source Map

Use this file as the repo-native entry point for `ppp-risk-allocation`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Risk allocation, project structure, and public-private interface rules.
4. Skill-local trigger cases and reference notes.
5. Prior PPP outputs only as context.

If the question is about project finance structure, use `project-finance-structurer`. If it is about project readiness, use `project-readiness-gate`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for PPP analysis. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Materiality and escalation thresholds. |
| `04-skills/07-ddmf-development-finance/ppp-risk-allocation/SKILL.md` | Skill scope and output contract. |
| `04-skills/07-ddmf-development-finance/ppp-risk-allocation/tests/trigger_cases.yaml` | Trigger examples for PPP cases. |
| `04-skills/07-ddmf-development-finance/ppp-risk-allocation/references/README.md` | Local approved reference staging area. |
| `04-skills/07-ddmf-development-finance/project-finance-structurer/SKILL.md` | Financing structure precedent. |
| `04-skills/07-ddmf-development-finance/project-readiness-gate/SKILL.md` | Readiness precedent before structure. |

## Usage notes

- Use the source map before assigning risks to the public side or private side.
- Keep allocation, pricing, and incentive effects separate.
- Do not call a deal balanced when the downside is only hidden.
