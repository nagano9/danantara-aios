# Repo BUMN Portfolio Segmentation Source Map

Use this file as the repo-native entry point for `bumn-portfolio-segmenter`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Ownership segments, entity grouping, and intervention logic.
4. Skill-local trigger cases and reference notes.
5. Prior segmentation outputs only as context.

If the question is about ownership actions or capital, use `capital-allocation-reviewer`. If it is about restructuring paths, use `restructuring-options-designer`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/AI_CONSTITUTION.md` | Governance boundary and authority rules. |
| `02-governance/DANANTARA_WAY.md` | Ownership posture and stewardship principles. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/master_skill_registry.json` | Entity and skill registry context. |
| `01-registry/workflow_routing_matrix.csv` | Where segmentation fits in the workflow. |
| `04-skills/05-dam-active-ownership/bumn-portfolio-segmenter/SKILL.md` | Skill scope and output contract. |
| `04-skills/05-dam-active-ownership/bumn-portfolio-segmenter/tests/trigger_cases.yaml` | Trigger examples for segmentation cases. |
| `04-skills/05-dam-active-ownership/bumn-portfolio-segmenter/references/README.md` | Local approved reference staging area. |
| `04-skills/05-dam-active-ownership/capital-allocation-reviewer/SKILL.md` | Ownership review pattern for downstream actions. |

## Usage notes

- Use the source map before grouping entities into a portfolio view.
- Keep segment, thesis, and intervention separate.
- Do not segment only for convenience.
