# Repo Data Sovereignty Source Map

Use this file as the repo-native entry point for `data-sovereignty-assessor`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Sovereignty, residency, access, and cross-border handling rules.
4. Skill-local trigger cases and reference notes.
5. Prior sovereignty outputs only as context.

If the question is about security controls, use `cybersecurity-by-design`. If the question is about legal sufficiency, use `legal-sufficiency-checker`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/AI_CONSTITUTION.md` | Authorization and data-use boundary. |
| `02-governance/DANANTARA_WAY.md` | Institutional posture for sovereign data. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for sovereignty review. |
| `04-skills/08-cross-functional/data-sovereignty-assessor/SKILL.md` | Skill scope and output contract. |
| `04-skills/08-cross-functional/data-sovereignty-assessor/tests/trigger_cases.yaml` | Trigger examples for sovereignty cases. |
| `04-skills/08-cross-functional/data-sovereignty-assessor/references/README.md` | Local approved reference staging area. |
| `04-skills/08-cross-functional/cybersecurity-by-design/SKILL.md` | Security precedent for controlled data. |
| `04-skills/08-cross-functional/legal-sufficiency-checker/SKILL.md` | Legal handling precedent. |

## Usage notes

- Use the source map before moving data across borders or domains.
- Keep ownership, residency, and permission separate.
- Do not assume internal data is automatically usable everywhere.
