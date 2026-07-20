# Repo Tension Resolution Source Map

Use this file as the repo-native entry point for `tension-resolution-engine`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved orchestration artifacts and controlled templates.
3. Competing priorities, tension framing, and resolution rules.
4. Skill-local trigger cases and reference notes.
5. Prior tension outputs only as context.

If the question is about a direct challenge to a decision, use `red-team-orchestrator`. If the question is about workflow ordering, use `workflow-planner`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Resolution lifecycle and handoff rules. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Chain structure for resolving tensions. |
| `01-registry/TENSION_SKILL_COVERAGE.md` | What tension categories are covered by which skill. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the engine. |
| `01-registry/workflow_routing_matrix.csv` | Routing when priorities collide. |
| `04-skills/02-orchestration/tension-resolution-engine/SKILL.md` | Skill intent and resolution scope. |
| `04-skills/02-orchestration/tension-resolution-engine/tests/trigger_cases.yaml` | Trigger examples for tension cases. |
| `04-skills/02-orchestration/tension-resolution-engine/references/README.md` | Local approved reference staging area. |
| `04-skills/02-orchestration/red-team-orchestrator/references/repo-red-team-source-map.md` | Challenge precedent. |
| `04-skills/02-orchestration/workflow-planner/references/repo-workflow-source-map.md` | Priority sequencing precedent. |

## Usage notes

- Use the source map before collapsing competing instructions.
- Keep value tension explicit instead of hiding it.
- Do not force false harmony where tradeoffs remain.
