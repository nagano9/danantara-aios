# Repo Conflict Source Map

Use this file as the repo-native entry point for `conflict-of-interest-gate`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Workflow routing matrices, approval maps, and orchestration protocols.
4. Owner-certified internal records and primary transaction or project documents.
5. Prior conflict findings only as context.

If the question is who may propose, review, or approve, use `decision-rights-checker`. If the question is who must approve and whether that approval is valid, use `human-approval-orchestrator`. If the question is whether the analysis is good enough to decide on, use `decision-quality-gate`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | End-to-end lifecycle and where conflict review sits before approval. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Canonical chains that include governance, recusal, and approval gates. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Formal skill roles and ownership. |
| `01-registry/workflow_routing_matrix.csv` | Which workflows require conflict review and what thresholds matter. |
| `02-governance/AI_CONSTITUTION.md` | Authority, evidence, decision rights, and stop conditions. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier thresholds that change the depth of conflict review. |
| `04-skills/01-governance-doctrine/decision-rights-checker/references/repo-governance-source-map.md` | The routing layer for proposer, reviewer, and approver roles. |
| `04-skills/02-orchestration/human-approval-orchestrator/references/repo-approval-source-map.md` | The validity layer for approvals already claimed. |
| `04-skills/10-assurance-evaluation/decision-quality-gate/references/repo-quality-source-map.md` | The analysis-quality gate that runs before approval routing. |

## Usage notes

- Use the source map before evaluating recusal, related parties, or hidden beneficiaries.
- Treat conflicts as governance findings, not assumptions to be ignored.
- Separate actual, potential, and perceived conflicts.
- Do not use this skill to cure a mandate, authority, or approval defect.
