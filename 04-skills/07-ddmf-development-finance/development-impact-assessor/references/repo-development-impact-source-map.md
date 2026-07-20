# Repo Development Impact Source Map

Use this file as the repo-native entry point for `development-impact-assessor`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Outcome logic, attribution, baselines, and impact measurement rules.
4. Skill-local trigger cases and reference notes.
5. Prior impact outputs only as context.

If the question is about project readiness or finance, use `project-readiness-gate` or `project-finance-structurer`. If it is about socioeconomic effects, use `socioeconomic-multiplier-modeler`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for development-finance review. |
| `02-governance/DANANTARA_WAY.md` | National value and stewardship posture. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `04-skills/07-ddmf-development-finance/development-impact-assessor/SKILL.md` | Skill scope and output contract. |
| `04-skills/07-ddmf-development-finance/development-impact-assessor/tests/trigger_cases.yaml` | Trigger examples for impact cases. |
| `04-skills/07-ddmf-development-finance/development-impact-assessor/references/README.md` | Local approved reference staging area. |
| `04-skills/07-ddmf-development-finance/socioeconomic-multiplier-modeler/SKILL.md` | Multiplier and attribution precedent. |
| `04-skills/07-ddmf-development-finance/project-readiness-gate/SKILL.md` | Readiness precedent before impact claims. |

## Usage notes

- Use the source map before labeling an outcome as impact.
- Keep baseline, attribution, and forecast separate.
- Do not let a good story outrun measurable change.
