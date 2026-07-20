# Repo Financial Performance Source Map

Use this file as the repo-native entry point for `financial-performance-diagnostic`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Financial performance, trend, variance, and diagnostic rules.
4. Skill-local trigger cases and reference notes.
5. Prior diagnostic outputs only as context.

If the question is about capital action, use `capital-allocation-reviewer`. If it is about operational root causes, use `operational-excellence-diagnostic`.

## Core repo sources

| File | Use |
|---|---|
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/master_skill_registry.csv` | Registry context for diagnostics. |
| `01-registry/master_skill_registry.json` | Machine-readable registry context. |
| `01-registry/dependency_edges.csv` | Downstream effects and related dependencies. |
| `02-governance/DANANTARA_WAY.md` | Value discipline and stewardship lens. |
| `04-skills/05-dam-active-ownership/financial-performance-diagnostic/SKILL.md` | Skill scope and output contract. |
| `04-skills/05-dam-active-ownership/financial-performance-diagnostic/tests/trigger_cases.yaml` | Trigger examples for diagnostic cases. |
| `04-skills/05-dam-active-ownership/financial-performance-diagnostic/references/README.md` | Local approved reference staging area. |
| `04-skills/05-dam-active-ownership/value-creation-plan-builder/SKILL.md` | Value creation linkage after diagnosis. |

## Usage notes

- Use the source map before stating a performance issue.
- Keep diagnosis, cause, and remedy separate.
- Do not let one quarter define the whole story.
