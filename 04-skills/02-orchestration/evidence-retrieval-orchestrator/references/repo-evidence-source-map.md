# Repo Evidence Retrieval Source Map

Use this file as the repo-native entry point for `evidence-retrieval-orchestrator`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved orchestration artifacts and controlled templates.
3. Evidence hierarchy, retrieval order, and provenance tracking.
4. Skill-local trigger cases and reference notes.
5. Prior retrieval outputs only as context.

If the question is about document-backed proof, use `document-evidence-extractor`. If the question is about prior decisions, use `decision-precedent-retriever`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Evidence retrieval lifecycle and handoff rules. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Retrieval flow placement. |
| `00-blueprint/workflow_chains.json` | Machine-readable chain topology. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the orchestrator. |
| `01-registry/workflow_routing_matrix.csv` | Where evidence retrieval fits in workflow. |
| `04-skills/02-orchestration/evidence-retrieval-orchestrator/SKILL.md` | Skill intent and retrieval boundaries. |
| `04-skills/02-orchestration/evidence-retrieval-orchestrator/tests/trigger_cases.yaml` | Trigger examples for evidence retrieval. |
| `04-skills/02-orchestration/evidence-retrieval-orchestrator/references/README.md` | Local approved reference staging area. |
| `04-skills/03-knowledge-data/document-evidence-extractor/SKILL.md` | Document extraction pattern. |
| `04-skills/03-knowledge-data/decision-precedent-retriever/SKILL.md` | Precedent retrieval pattern. |

## Usage notes

- Use the source map before treating a file as evidence.
- Keep source provenance attached to the retrieved payload.
- Do not flatten multiple evidence tiers into one claim.
