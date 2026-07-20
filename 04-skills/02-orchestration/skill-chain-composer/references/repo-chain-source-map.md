# Repo Chain Source Map

Use this file as the repo-native entry point for `skill-chain-composer`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Workflow blueprints, routing matrices, and orchestration protocols.
4. Owner-certified internal records and primary transaction or project documents.
5. Prior chains only as context.

If the request needs workflow blueprinting, use `workflow-planner`. If it needs parallel workstreams, use `parallel-analysis-dispatcher`. If it needs persistent state, use `workflow-state-manager`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/WORKFLOW_CHAINS.md` | Canonical downstream chains and handoffs. |
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Lifecycle boundaries and the one-way door between planning and retrieval. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Skill roles and ownership. |
| `01-registry/workflow_routing_matrix.csv` | Which workflows require chain composition and where they terminate. |
| `02-governance/AI_CONSTITUTION.md` | Authority, evidence, decision rights, and stop conditions. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier thresholds that affect chain depth. |
| `04-skills/02-orchestration/workflow-planner/references/repo-workflow-source-map.md` | The planning layer the chain composer consumes. |
| `04-skills/02-orchestration/parallel-analysis-dispatcher/references/README.md` | The boundary for parallel workstreams. |
| `04-skills/02-orchestration/danantara-master-orchestrator/references/repo-orchestration-source-map.md` | End-to-end orchestration context. |

## Usage notes

- Use the source map before sequencing skills.
- Avoid duplicate analysis or conflicting mandates.
- Split serial and parallel segments explicitly.
- Preserve the handoff to human approval.
