# Repo Data Classification Source Map

Use this file as the repo-native entry point for `data-classification-router`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved orchestration artifacts and controlled templates.
3. Data class, confidentiality level, and handling route.
4. Skill-local trigger cases and reference notes.
5. Prior classification outputs only as context.

If the question is about sensitive information, use `strategic-confidentiality-classifier`. If the issue is about workflow placement, use `workflow-state-manager`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/AI_CONSTITUTION.md` | Confidentiality boundary and handling rules. |
| `02-governance/DANANTARA_WAY.md` | Institutional posture for handling data. |
| `01-registry/workflow_routing_matrix.csv` | Classification-driven routing path. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the router. |
| `04-skills/02-orchestration/data-classification-router/SKILL.md` | Skill scope and routing intent. |
| `04-skills/02-orchestration/data-classification-router/tests/trigger_cases.yaml` | Trigger examples for classification cases. |
| `04-skills/02-orchestration/data-classification-router/references/README.md` | Local approved reference staging area. |
| `04-skills/01-governance-doctrine/strategic-confidentiality-classifier/references/repo-confidentiality-source-map.md` | Confidentiality classification precedent. |
| `04-skills/02-orchestration/workflow-state-manager/references/repo-workflow-source-map.md` | Stateful routing after classification. |

## Usage notes

- Use the source map before moving data into a new route.
- Keep class, audience, and retention separate.
- Do not default to the broadest classification without evidence.
