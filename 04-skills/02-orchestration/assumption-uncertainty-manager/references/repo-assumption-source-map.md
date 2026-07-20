# Repo Assumption Uncertainty Source Map

Use this file as the repo-native entry point for `assumption-uncertainty-manager`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved orchestration artifacts and controlled templates.
3. Explicit assumptions, unresolved uncertainty, and decision dependencies.
4. Skill-local trigger cases and reference notes.
5. Prior uncertainty logs only as context.

If the question is about workflow state after an unresolved assumption, use `workflow-state-manager`. If approval is needed, use `human-approval-orchestrator`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Orchestration lifecycle and handoff rules. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Chain structure when assumptions affect flow. |
| `00-blueprint/workflow_chains.json` | Machine-readable chain topology. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Where uncertainty handling enters the workflow. |
| `04-skills/02-orchestration/assumption-uncertainty-manager/SKILL.md` | Skill scope and intended behavior. |
| `04-skills/02-orchestration/assumption-uncertainty-manager/tests/trigger_cases.yaml` | Trigger examples for uncertainty cases. |
| `04-skills/02-orchestration/assumption-uncertainty-manager/references/README.md` | Local approved reference staging area. |
| `04-skills/02-orchestration/workflow-state-manager/references/repo-workflow-source-map.md` | State tracking when assumptions remain open. |
| `04-skills/02-orchestration/human-approval-orchestrator/references/repo-approval-source-map.md` | Approval routing for unresolved assumptions. |

## Usage notes

- Use the source map before converting a guess into a committed workflow step.
- Keep assumptions explicit and named.
- Do not bury uncertainty inside a confident answer.
