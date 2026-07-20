# Repo Decision Precedent Source Map

Use this file as the repo-native entry point for `decision-precedent-retriever`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved registry and assurance artifacts.
3. Prior decisions, lessons learned, and decision trace records.
4. Skill-local trigger cases and reference notes.
5. Prior retrieval outputs only as context.

If the question is about what the repo learned after a decision, use `post-decision-learning`. If it is about decision quality, use `decision-quality-gate`.

## Core repo sources

| File | Use |
|---|---|
| `01-registry/master_skill_registry.json` | Registry anchor for prior decisions and skill state. |
| `01-registry/dependency_edges.csv` | Linkage between decisions, outputs, and follow-on work. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical catalog for precedent retrieval scope. |
| `04-skills/03-knowledge-data/decision-precedent-retriever/SKILL.md` | Skill intent and retrieval scope. |
| `04-skills/03-knowledge-data/decision-precedent-retriever/tests/trigger_cases.yaml` | Trigger examples for precedent cases. |
| `04-skills/03-knowledge-data/decision-precedent-retriever/references/README.md` | Local approved reference staging area. |
| `04-skills/10-assurance-evaluation/post-decision-learning/references/repo-learning-source-map.md` | Existing learning after decision precedent. |
| `04-skills/10-assurance-evaluation/decision-quality-gate/references/repo-quality-source-map.md` | Decision-quality precedent and checks. |
| `04-skills/10-assurance-evaluation/audit-trail-packager/references/repo-audit-source-map.md` | Traceable evidence packaging precedent. |

## Usage notes

- Use the source map before citing an internal precedent.
- Keep precedent, recommendation, and approval separate.
- Do not confuse frequency with legitimacy.
