# Repo Benchmark Intelligence Source Map

Use this file as the repo-native entry point for `benchmark-intelligence-manager`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved registry and blueprint artifacts.
3. Benchmark frames, comparison rules, and canonical registry state.
4. Skill-local trigger cases and reference notes.
5. Prior benchmark outputs only as context.

If the question is about canonical repository state, use `master_skill_registry.json`. If the question is about portfolio-style comparison, use `portfolio-knowledge-graph`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/DANANTARA_AIOS_BLUEPRINT.md` | Overall repo framing for benchmark comparisons. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical catalog for what exists. |
| `01-registry/master_skill_registry.json` | Machine-readable canonical registry. |
| `01-registry/master_skill_registry.csv` | Tabular registry view for comparison. |
| `01-registry/PRINCIPLE_SKILL_COVERAGE.md` | Coverage baseline used in benchmarking. |
| `04-skills/03-knowledge-data/benchmark-intelligence-manager/SKILL.md` | Skill intent and benchmark scope. |
| `04-skills/03-knowledge-data/benchmark-intelligence-manager/tests/trigger_cases.yaml` | Trigger examples for benchmark cases. |
| `04-skills/03-knowledge-data/benchmark-intelligence-manager/references/README.md` | Local approved reference staging area. |
| `04-skills/03-knowledge-data/portfolio-knowledge-graph/SKILL.md` | Related comparison and knowledge-linking pattern. |

## Usage notes

- Use the source map before comparing against any alleged baseline.
- Keep benchmark criteria explicit and versioned.
- Do not compare unlike things as if they were equivalent.
