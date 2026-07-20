# Repo Intent and Entity Source Map

Use this file as the repo-native entry point for `intent-and-entity-router`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved orchestration artifacts and controlled templates.
3. Intent labels, entity labels, and routing rules.
4. Skill-local trigger cases and reference notes.
5. Prior routing outputs only as context.

If the question is about a classification or content class, use `data-classification-router`. If the question is about downstream assembly, use `output-assembly-orchestrator`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Router lifecycle and handoff rules. |
| `01-registry/workflow_routing_matrix.csv` | Intent/entity-driven routing path. |
| `01-registry/master_skill_registry.json` | Canonical skill metadata and labels. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the router. |
| `04-skills/02-orchestration/intent-and-entity-router/SKILL.md` | Skill scope and routing intent. |
| `04-skills/02-orchestration/intent-and-entity-router/tests/trigger_cases.yaml` | Trigger examples for intent/entity cases. |
| `04-skills/02-orchestration/intent-and-entity-router/references/README.md` | Local approved reference staging area. |
| `04-skills/02-orchestration/data-classification-router/references/repo-data-classification-source-map.md` | Classification precedent. |
| `04-skills/02-orchestration/output-assembly-orchestrator/references/repo-output-assembly-source-map.md` | Downstream assembly precedent. |

## Usage notes

- Use the source map before turning language into routeable labels.
- Keep intent, entity, and confidence separate.
- Do not collapse ambiguity into a false match.
