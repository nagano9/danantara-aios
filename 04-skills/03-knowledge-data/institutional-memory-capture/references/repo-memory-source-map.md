# Repo Institutional Memory Source Map

Use this file as the repo-native entry point for `institutional-memory-capture`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved registry and assurance artifacts.
3. Lessons learned, post-decision memory, and audit traces.
4. Skill-local trigger cases and reference notes.
5. Prior memory outputs only as context.

If the question is about what should be learned after an action, use `post-decision-learning`. If the question is about evidence packaging, use `audit-trail-packager`.

## Core repo sources

| File | Use |
|---|---|
| `01-registry/master_skill_registry.json` | Registry anchor for captured memory state. |
| `01-registry/dependency_edges.csv` | What memory should link back to. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical catalog for memory capture scope. |
| `04-skills/03-knowledge-data/institutional-memory-capture/SKILL.md` | Skill scope and capture behavior. |
| `04-skills/03-knowledge-data/institutional-memory-capture/tests/trigger_cases.yaml` | Trigger examples for memory cases. |
| `04-skills/03-knowledge-data/institutional-memory-capture/references/README.md` | Local approved reference staging area. |
| `04-skills/10-assurance-evaluation/post-decision-learning/references/repo-learning-source-map.md` | Learning capture precedent. |
| `04-skills/10-assurance-evaluation/audit-trail-packager/references/repo-audit-source-map.md` | Evidence packaging precedent. |
| `04-skills/03-knowledge-data/decision-precedent-retriever/references/repo-precedent-source-map.md` | Precedent lookup precedent. |

## Usage notes

- Use the source map before turning experience into institutional memory.
- Keep memory capture close to the original source trail.
- Do not overwrite a lesson with a later convenience.
