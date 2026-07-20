# Repo Project Readiness Source Map

Use this file as the repo-native entry point for `project-readiness-gate`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Readiness, feasibility, approvals, and stage-gate rules.
4. Skill-local trigger cases and reference notes.
5. Prior readiness outputs only as context.

If the question is about delivery tracking, use `project-delivery-monitor`. If it is about finance, use `project-finance-structurer`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for readiness gating. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Materiality and escalation thresholds. |
| `04-skills/07-ddmf-development-finance/project-readiness-gate/SKILL.md` | Skill scope and output contract. |
| `04-skills/07-ddmf-development-finance/project-readiness-gate/tests/trigger_cases.yaml` | Trigger examples for readiness cases. |
| `04-skills/07-ddmf-development-finance/project-readiness-gate/references/README.md` | Local approved reference staging area. |
| `04-skills/07-ddmf-development-finance/project-finance-structurer/SKILL.md` | Financing and structuring precedent. |
| `04-skills/07-ddmf-development-finance/development-impact-assessor/SKILL.md` | Impact and readiness linkage. |

## Usage notes

- Use the source map before saying a project is ready.
- Keep technical, legal, commercial, and sponsor readiness separate.
- Do not collapse partial readiness into full readiness.
