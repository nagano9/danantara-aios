# Repo Source Hierarchy Source Map

Use this file as the repo-native entry point for `source-hierarchy-resolver`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved orchestration artifacts and controlled templates.
3. Explicit source precedence and conflict-resolution rules.
4. Skill-local trigger cases and reference notes.
5. Prior hierarchy outputs only as context.

If the question is about authority, use `decision-rights-checker`. If evidence conflicts, use `evidence-retrieval-orchestrator`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Source precedence in the orchestration lifecycle. |
| `01-registry/PRINCIPLE_SKILL_COVERAGE.md` | Principle-to-skill precedence. |
| `01-registry/workflow_routing_matrix.csv` | Routing order when multiple sources compete. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical skill placement. |
| `04-skills/02-orchestration/source-hierarchy-resolver/SKILL.md` | Skill scope and precedence logic. |
| `04-skills/02-orchestration/source-hierarchy-resolver/tests/trigger_cases.yaml` | Trigger examples for hierarchy cases. |
| `04-skills/02-orchestration/source-hierarchy-resolver/references/README.md` | Local approved reference staging area. |
| `04-skills/01-governance-doctrine/decision-rights-checker/references/repo-governance-source-map.md` | Authority and ownership precedent. |
| `04-skills/02-orchestration/evidence-retrieval-orchestrator/references/repo-evidence-source-map.md` | Evidence precedence and retrieval order. |

## Usage notes

- Use the source map before selecting a source to trust.
- Keep rank order and confidence separate.
- Do not treat volume as authority.
