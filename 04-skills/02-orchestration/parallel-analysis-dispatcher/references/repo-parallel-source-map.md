# Repo Parallel Source Map

Use this file as the repo-native entry point for `parallel-analysis-dispatcher`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Workflow blueprints, routing matrices, orchestration protocols, and skill boundaries.
4. Owner-certified internal records and primary transaction or project documents.
5. Prior parallel plans only as context.

If the request needs workflow blueprinting, use `workflow-planner`. If it needs exact skill sequencing, use `skill-chain-composer`. If it needs persistent state, use `workflow-state-manager`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | End-to-end lifecycle boundaries, including where parallel dispatch starts and ends. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Canonical workflows that may include parallel branches and downstream handoffs. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Formal skill roles and ownership. |
| `01-registry/workflow_routing_matrix.csv` | Which workflows require orchestration, planning, or parallel dispatch. |
| `02-governance/AI_CONSTITUTION.md` | Authority, evidence, decision rights, and stop conditions. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier thresholds that change the required depth of the dispatch. |
| `04-skills/02-orchestration/workflow-planner/references/repo-workflow-source-map.md` | The planning layer that defines the blueprint before dispatch. |
| `04-skills/02-orchestration/skill-chain-composer/references/repo-chain-source-map.md` | The sequencing layer that follows routing and avoids duplicate analysis. |
| `04-skills/02-orchestration/workflow-state-manager/references/repo-workflow-source-map.md` | The state layer that persists owners, blockers, and handoffs. |

## Usage notes

- Use the source map before defining parallel workstreams.
- Keep workstreams non-overlapping and explicitly owned.
- Reconcile overlaps, conflicts, and dissent before handoff.
- Do not use this skill as a substitute for planning, sequencing, or state management.
