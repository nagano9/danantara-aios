# Repo Transformation Agenda Source Map

Use this file as the repo-native entry point for `transformation-agenda-orchestrator`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Transformation agenda, program sequencing, and change governance.
4. Skill-local trigger cases and reference notes.
5. Prior transformation outputs only as context.

If the question is about exact sequencing, use `workflow-planner`. If it is about approval, use `human-approval-orchestrator`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Program lifecycle and handoff rules. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Transformation chain structure. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the orchestrator. |
| `01-registry/workflow_routing_matrix.csv` | Where transformation orchestration fits. |
| `02-governance/DANANTARA_WAY.md` | Institutional change posture. |
| `02-governance/AI_CONSTITUTION.md` | Governance boundary for transformation work. |
| `04-skills/04-bpi-control-tower/transformation-agenda-orchestrator/SKILL.md` | Skill scope and output contract. |
| `04-skills/04-bpi-control-tower/transformation-agenda-orchestrator/tests/trigger_cases.yaml` | Trigger examples for transformation cases. |
| `04-skills/04-bpi-control-tower/transformation-agenda-orchestrator/references/README.md` | Local approved reference staging area. |
| `04-skills/02-orchestration/workflow-planner/references/repo-workflow-source-map.md` | Planning and sequencing precedent. |

## Usage notes

- Use the source map before turning a change wish into a program agenda.
- Keep agenda, execution, and approval distinct.
- Do not treat momentum as proof of correctness.
