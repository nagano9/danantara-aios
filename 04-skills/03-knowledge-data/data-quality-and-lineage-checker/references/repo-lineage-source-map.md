# Repo Data Quality and Lineage Source Map

Use this file as the repo-native entry point for `data-quality-and-lineage-checker`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved registry and blueprint artifacts.
3. Lineage, dependency, quality, and coverage records.
4. Skill-local trigger cases and reference notes.
5. Prior quality outputs only as context.

If the question is about what depends on what, use `dependency_edges.csv`. If the question is about coverage, use `principle_skill_coverage.csv`.

## Core repo sources

| File | Use |
|---|---|
| `01-registry/dependency_edges.csv` | Canonical dependency and lineage graph. |
| `01-registry/master_skill_registry.csv` | Registry records for lineage checks. |
| `01-registry/master_skill_registry.json` | Machine-readable registry state. |
| `01-registry/principle_skill_coverage.csv` | Coverage baseline for quality checks. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical catalog for skill identity. |
| `04-skills/03-knowledge-data/data-quality-and-lineage-checker/SKILL.md` | Skill scope and quality behavior. |
| `04-skills/03-knowledge-data/data-quality-and-lineage-checker/tests/trigger_cases.yaml` | Trigger examples for lineage cases. |
| `04-skills/03-knowledge-data/data-quality-and-lineage-checker/references/README.md` | Local approved reference staging area. |
| `04-skills/03-knowledge-data/decision-precedent-retriever/tests/trigger_cases.yaml` | Adjacent precedent retrieval patterns. |

## Usage notes

- Use the source map before asserting a dataset or registry is clean.
- Keep lineage evidence separate from inferred relationships.
- Do not hide missing provenance inside a completed record.
