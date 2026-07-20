# Repo Workflow Source Map

Use this file as the repo-native entry point for `workflow-planner`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Workflow protocols, routing matrices, and orchestration chain references.
4. Owner-certified internal records and primary transaction or project documents.
5. Prior plans only as context.

If the request needs exact skill sequencing, use `skill-chain-composer`. If it needs parallel workstreams, use `parallel-analysis-dispatcher`. If it needs persistent workflow state, use `workflow-state-manager`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | End-to-end lifecycle and the one-way door between planning and retrieval. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Canonical chains and downstream handoffs. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Formal skill roles and ownership. |
| `01-registry/workflow_routing_matrix.csv` | Which workflows require orchestration, planning, or parallel dispatch. |
| `02-governance/AI_CONSTITUTION.md` | Authority, evidence, decision rights, and stop conditions. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier thresholds that change the required depth of the plan. |
| `04-skills/02-orchestration/danantara-master-orchestrator/references/repo-orchestration-source-map.md` | End-to-end orchestration context. |
| `04-skills/02-orchestration/skill-chain-composer/references/README.md` | Boundary for exact skill sequencing. |
| `04-skills/02-orchestration/parallel-analysis-dispatcher/references/README.md` | Boundary for parallel analysis dispatch. |

## Usage notes

- Use the source map before drafting the plan.
- Keep the planning layer distinct from exact execution sequencing.
- Identify where the plan hands off to composition, parallel dispatch, or workflow state.
- Preserve unresolved tensions; do not average them away in the planning layer.
