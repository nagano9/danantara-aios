# Repo Portfolio Knowledge Graph Source Map

Use this file as the repo-native entry point for `portfolio-knowledge-graph`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Relationship, dependency, ownership, and stakeholder rules.
4. Skill-local trigger cases and reference notes.
5. Prior graph outputs only as context.

If the question is about policy ownership or versioning, use `policy-knowledge-curator`. If it is about source quality, use `data-quality-and-lineage-checker`.

## Core repo sources

| File | Use |
|---|---|
| `01-registry/master_skill_registry.json` | Canonical entity and skill relationships. |
| `01-registry/dependency_edges.csv` | Dependency graph backbone. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `02-governance/AI_CONSTITUTION.md` | Authority boundary and evidence rules. |
| `02-governance/DANANTARA_WAY.md` | Stewardship and portfolio posture. |
| `04-skills/03-knowledge-data/portfolio-knowledge-graph/SKILL.md` | Skill scope and output contract. |
| `04-skills/03-knowledge-data/portfolio-knowledge-graph/tests/trigger_cases.yaml` | Trigger examples for graph cases. |
| `04-skills/03-knowledge-data/portfolio-knowledge-graph/references/README.md` | Local approved reference staging area. |
| `04-skills/03-knowledge-data/policy-knowledge-curator/SKILL.md` | Policy and metadata precedent. |
| `04-skills/03-knowledge-data/data-quality-and-lineage-checker/SKILL.md` | Quality and lineage precedent. |

## Usage notes

- Use the source map before asserting a hidden dependency.
- Keep relationship, ownership, and evidence separate.
- Do not infer causality from a single edge.
