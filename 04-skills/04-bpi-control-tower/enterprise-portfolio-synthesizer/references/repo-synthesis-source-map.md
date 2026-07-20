# Repo Enterprise Portfolio Source Map

Use this file as the repo-native entry point for `enterprise-portfolio-synthesizer`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Portfolio aggregation rules, synthesis logic, and enterprise framing.
4. Skill-local trigger cases and reference notes.
5. Prior synthesis outputs only as context.

If the question is about exact sequencing, use `workflow-planner`. If the question is about how multiple inputs fit together, use `skill-chain-composer`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/DANANTARA_AIOS_BLUEPRINT.md` | System-level framing for enterprise synthesis. |
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Orchestration and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the synthesizer. |
| `01-registry/PRINCIPLE_SKILL_COVERAGE.md` | Coverage of enterprise principles. |
| `01-registry/workflow_routing_matrix.csv` | Where synthesis sits in the workflow. |
| `02-governance/DANANTARA_WAY.md` | Enterprise posture and tradeoff framing. |
| `04-skills/04-bpi-control-tower/enterprise-portfolio-synthesizer/SKILL.md` | Skill scope and output contract. |
| `04-skills/04-bpi-control-tower/enterprise-portfolio-synthesizer/tests/trigger_cases.yaml` | Trigger examples for synthesis cases. |
| `04-skills/04-bpi-control-tower/enterprise-portfolio-synthesizer/references/README.md` | Local approved reference staging area. |
| `04-skills/02-orchestration/skill-chain-composer/references/repo-chain-source-map.md` | Composition precedent for merged outputs. |

## Usage notes

- Use the source map before turning multiple portfolio items into one narrative.
- Keep aggregation and judgment separate.
- Do not smooth away tension that matters to decision rights.
