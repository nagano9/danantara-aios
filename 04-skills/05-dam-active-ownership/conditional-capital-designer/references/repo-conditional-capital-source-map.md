# Repo Conditional Capital Source Map

Use this file as the repo-native entry point for `conditional-capital-designer`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Conditional capital design, milestones, covenants, and release logic.
4. Skill-local trigger cases and reference notes.
5. Prior capital design outputs only as context.

If the question is about capital approval, use `capital-allocation-reviewer`. If it is about downside control, use `prudence-and-downside-gate`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/RISK_APPROVAL_MATRIX.md` | Release thresholds and escalation rules. |
| `02-governance/AI_CONSTITUTION.md` | Authority boundary and approval rules. |
| `02-governance/DANANTARA_WAY.md` | Capital discipline and conditionality. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the designer. |
| `01-registry/workflow_routing_matrix.csv` | Where conditional capital work fits. |
| `04-skills/05-dam-active-ownership/conditional-capital-designer/SKILL.md` | Skill scope and design behavior. |
| `04-skills/05-dam-active-ownership/conditional-capital-designer/tests/trigger_cases.yaml` | Trigger examples for conditional capital cases. |
| `04-skills/05-dam-active-ownership/conditional-capital-designer/references/README.md` | Local approved reference staging area. |
| `04-skills/05-dam-active-ownership/capital-allocation-reviewer/references/repo-capital-allocation-source-map.md` | Capital review precedent. |
| `04-skills/01-governance-doctrine/prudence-and-downside-gate/references/repo-prudence-source-map.md` | Downside gate precedent. |

## Usage notes

- Use the source map before defining any release conditions.
- Keep structure, milestones, and approval rights explicit.
- Do not disguise permanent support as temporary support.
