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
| `04-skills/01-governance-doctrine/conflict-of-interest-gate/references/repo-conflict-source-map.md` | Conflict and recusal findings that may keep the state open. |
| `04-skills/02-orchestration/human-approval-orchestrator/references/repo-approval-source-map.md` | Approval routing and validity findings that may keep the state open. |
| `04-skills/02-orchestration/parallel-analysis-dispatcher/references/repo-parallel-source-map.md` | Parallel workstream ownership that the state record must track. |
| `04-skills/10-assurance-evaluation/audit-trail-packager/references/repo-audit-source-map.md` | The audit record that should capture state transitions at material milestones. |
| `04-skills/10-assurance-evaluation/decision-quality-gate/references/repo-quality-source-map.md` | The quality verdict that may determine whether the workflow advances. |
| `04-skills/10-assurance-evaluation/post-decision-learning/references/repo-learning-source-map.md` | The post-decision outcome and learning loop that closes the state record. |

## Usage notes

- Use the source map before updating stage, blocker, or handoff state.
- Preserve the latest known evidence, open issue, owner, and due date.
- If a blocker belongs to authority, evidence, conflict, quality, or approval, route it to the appropriate skill and keep the state open.
- Do not mark a stage complete without an evidenced handoff, decision, or closure record.
- Do not use this source map to replace the underlying verdicts; it only tracks where the workflow stands.
