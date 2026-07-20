# Repo Governance Board Paper Source Map

Use this file as the repo-native entry point for `governance-board-paper-reviewer`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved board and governance artifacts.
3. Board-paper structure, evidentiary standard, and decision clarity rules.
4. Skill-local trigger cases and reference notes.
5. Prior board papers only as context.

If the question is about board briefing for a specific decision, use `executive-board-brief-builder`. If it is about disclosure, use `transparency-disclosure-gate`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Decision lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for governance papers. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `02-governance/DANANTARA_WAY.md` | Governance posture and board context. |
| `04-skills/08-cross-functional/governance-board-paper-reviewer/SKILL.md` | Skill scope and output contract. |
| `04-skills/08-cross-functional/governance-board-paper-reviewer/tests/trigger_cases.yaml` | Trigger examples for board-paper cases. |
| `04-skills/08-cross-functional/governance-board-paper-reviewer/references/README.md` | Local approved reference staging area. |
| `04-skills/04-bpi-control-tower/executive-board-brief-builder/SKILL.md` | Executive brief precedent. |
| `04-skills/01-governance-doctrine/transparency-disclosure-gate/SKILL.md` | Disclosure precedent. |

## Usage notes

- Use the source map before calling a paper board-ready.
- Keep completeness, clarity, and approval separate.
- Do not let formatting substitute for decision quality.
