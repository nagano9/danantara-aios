# Repo Workflow Source Map

Use this file as the repo-native entry point for `workflow-state-manager`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Approved workflow chains and routing matrices.
4. Owner-certified internal records and primary transaction or project documents.
5. Prior workflow state only as context.

If the state record conflicts with a higher source, treat the state as stale until reconciled.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | End-to-end lifecycle: intake, classifying, authorizing, planning, retrieving, analyzing, challenging, synthesizing, assuring, approving, executing, learning. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Canonical placement of this skill within full workflow chains. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical trigger language and skill ownership. |
| `01-registry/workflow_routing_matrix.csv` | Which workflows route through this manager and what human authority owns the threshold. |
| `02-governance/AI_CONSTITUTION.md` | Required governance boundary, traceability, and refusal rules. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier expectations that affect state, approvals, and escalation. |

## Usage notes

- Use the source map before updating stage, blocker, or handoff state.
- Preserve the latest known evidence, open issue, owner, and due date.
- If a blocker belongs to authority, evidence, or approval, route it to the appropriate governance skill and keep the state open.
- Do not mark a stage complete without an evidenced handoff or decision.
