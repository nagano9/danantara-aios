# Repo Post Investment Source Map

Use this file as the repo-native entry point for `post-investment-monitor`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Thesis, KPI, covenant, risk, liquidity, and intervention rules.
4. Skill-local trigger cases and reference notes.
5. Prior monitoring outputs only as context.

If the question is about value creation after monitoring, use `value-creation-plan-builder`. If it is about stress, use `scenario-stress-testing`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for ownership monitoring. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `04-skills/06-dim-investment-management/post-investment-monitor/SKILL.md` | Skill scope and output contract. |
| `04-skills/06-dim-investment-management/post-investment-monitor/tests/trigger_cases.yaml` | Trigger examples for monitoring cases. |
| `04-skills/06-dim-investment-management/post-investment-monitor/references/README.md` | Local approved reference staging area. |
| `04-skills/05-dam-active-ownership/value-creation-plan-builder/SKILL.md` | Value-creation follow-through precedent. |
| `04-skills/08-cross-functional/scenario-stress-testing/SKILL.md` | Stress-testing precedent. |

## Usage notes

- Use the source map before concluding the asset is on track.
- Keep thesis, monitoring, trigger, and response separate.
- Do not treat a green dashboard as a green investment.
