# Repo Capital Allocation Source Map

Use this file as the repo-native entry point for `capital-allocation-reviewer`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Capital gates, hurdle logic, and ownership alternatives.
4. Skill-local trigger cases and reference notes.
5. Prior allocation outputs only as context.

If the question is about opportunity entry, use `opportunity-screening`. If it is about downside or stress, use `prudence-and-downside-gate`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/AI_CONSTITUTION.md` | Authority and approval boundary. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Materiality and escalation thresholds. |
| `02-governance/DANANTARA_WAY.md` | Capital stewardship and value discipline. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the reviewer. |
| `01-registry/workflow_routing_matrix.csv` | Where capital review fits in the flow. |
| `04-skills/05-dam-active-ownership/capital-allocation-reviewer/SKILL.md` | Skill scope and output contract. |
| `04-skills/05-dam-active-ownership/capital-allocation-reviewer/tests/trigger_cases.yaml` | Trigger examples for allocation cases. |
| `04-skills/05-dam-active-ownership/capital-allocation-reviewer/references/README.md` | Local approved reference staging area. |
| `04-skills/06-dim-investment-management/opportunity-screening/references/repo-screening-source-map.md` | Entry-screening precedent. |
| `04-skills/01-governance-doctrine/prudence-and-downside-gate/references/repo-prudence-source-map.md` | Downside control precedent. |

## Usage notes

- Use the source map before allocating scarce capital.
- Keep return, risk, and strategic necessity separate.
- Do not approve on narrative momentum alone.
