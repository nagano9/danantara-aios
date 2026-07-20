# Repo Financial Model Source Map

Use this file as the repo-native entry point for `financial-model-validator`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Modeling logic, assumptions, formulas, and validation rules.
4. Skill-local trigger cases and reference notes.
5. Prior model outputs only as context.

If the question is about capital structure or project finance, use `project-finance-structurer`. If it is about scenario risk, use `scenario-stress-testing`.

## Core repo sources

| File | Use |
|---|---|
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/master_skill_registry.json` | Registry context for model validation. |
| `01-registry/dependency_edges.csv` | Dependency and logic lineage. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk thresholds for model reliance. |
| `04-skills/08-cross-functional/financial-model-validator/SKILL.md` | Skill scope and output contract. |
| `04-skills/08-cross-functional/financial-model-validator/tests/trigger_cases.yaml` | Trigger examples for validation cases. |
| `04-skills/08-cross-functional/financial-model-validator/references/README.md` | Local approved reference staging area. |
| `04-skills/07-ddmf-development-finance/project-finance-structurer/SKILL.md` | Financing model precedent. |
| `04-skills/08-cross-functional/scenario-stress-testing/SKILL.md` | Scenario and stress precedent. |

## Usage notes

- Use the source map before trusting a model output.
- Keep formula correctness, assumption validity, and business interpretation separate.
- Do not accept a polished spreadsheet as proof of correctness.
