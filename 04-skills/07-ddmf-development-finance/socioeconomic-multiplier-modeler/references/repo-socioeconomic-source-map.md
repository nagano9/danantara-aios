# Repo Socioeconomic Multiplier Source Map

Use this file as the repo-native entry point for `socioeconomic-multiplier-modeler`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Multiplier logic, attribution, and spillover measurement rules.
4. Skill-local trigger cases and reference notes.
5. Prior multiplier outputs only as context.

If the question is about development impact, use `development-impact-assessor`. If it is about readiness, use `project-readiness-gate`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for multiplier analysis. |
| `02-governance/DANANTARA_WAY.md` | Value and public-interest posture. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `04-skills/07-ddmf-development-finance/socioeconomic-multiplier-modeler/SKILL.md` | Skill scope and output contract. |
| `04-skills/07-ddmf-development-finance/socioeconomic-multiplier-modeler/tests/trigger_cases.yaml` | Trigger examples for multiplier cases. |
| `04-skills/07-ddmf-development-finance/socioeconomic-multiplier-modeler/references/README.md` | Local approved reference staging area. |
| `04-skills/07-ddmf-development-finance/development-impact-assessor/SKILL.md` | Development impact precedent. |

## Usage notes

- Use the source map before estimating a multiplier effect.
- Keep direct, indirect, and induced effects separate.
- Do not double count the same benefit in multiple channels.
