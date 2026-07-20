# Repo Document Evidence Source Map

Use this file as the repo-native entry point for `document-evidence-extractor`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved registry and blueprint artifacts.
3. Primary documents, extractable evidence, and source provenance.
4. Skill-local trigger cases and reference notes.
5. Prior extraction outputs only as context.

If the question is about prior decisions, use `decision-precedent-retriever`. If the output needs auditability, use `audit-trail-packager`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Evidence extraction lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of document evidence extraction. |
| `01-registry/workflow_routing_matrix.csv` | Where document extraction fits in the workflow. |
| `04-skills/03-knowledge-data/document-evidence-extractor/SKILL.md` | Skill scope and extraction behavior. |
| `04-skills/03-knowledge-data/document-evidence-extractor/tests/trigger_cases.yaml` | Trigger examples for extraction cases. |
| `04-skills/03-knowledge-data/document-evidence-extractor/references/README.md` | Local approved reference staging area. |
| `04-skills/03-knowledge-data/decision-precedent-retriever/SKILL.md` | Related precedent-backed extraction pattern. |
| `04-skills/10-assurance-evaluation/audit-trail-packager/references/repo-audit-source-map.md` | Packaging and traceability precedent. |
| `04-skills/10-assurance-evaluation/decision-quality-gate/references/repo-quality-source-map.md` | Quality control for extracted evidence. |

## Usage notes

- Use the source map before extracting a fact from a document.
- Keep extraction separate from interpretation.
- Do not present an extract as if it were the whole file.
