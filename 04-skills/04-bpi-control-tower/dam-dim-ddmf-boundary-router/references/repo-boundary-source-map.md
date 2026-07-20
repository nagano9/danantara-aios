# Repo DAM DIM DDMF Boundary Source Map

Use this file as the repo-native entry point for `dam-dim-ddmf-boundary-router`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Mandate boundary, workstream ownership, and routing separation.
4. Skill-local trigger cases and reference notes.
5. Prior routing outputs only as context.

If the question is about exact responsibility, use `decision-rights-checker`. If the question is about sequencing, use `workflow-planner`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | One-way door between planning and execution. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the router. |
| `01-registry/workflow_routing_matrix.csv` | DAM/DIM/DDMF routing lines. |
| `02-governance/AI_CONSTITUTION.md` | Governance boundary and escalation rules. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier thresholds that affect routing. |
| `04-skills/04-bpi-control-tower/dam-dim-ddmf-boundary-router/SKILL.md` | Skill scope and routing intent. |
| `04-skills/04-bpi-control-tower/dam-dim-ddmf-boundary-router/tests/trigger_cases.yaml` | Trigger examples for boundary cases. |
| `04-skills/04-bpi-control-tower/dam-dim-ddmf-boundary-router/references/README.md` | Local approved reference staging area. |
| `04-skills/02-orchestration/workflow-planner/references/repo-workflow-source-map.md` | Workflow boundary precedent. |
| `04-skills/01-governance-doctrine/decision-rights-checker/references/repo-governance-source-map.md` | Authority and delegation precedent. |

## Usage notes

- Use the source map before moving work across domain boundaries.
- Keep mandate, workflow, and accountability separate.
- Do not infer authority from proximity to the work.
