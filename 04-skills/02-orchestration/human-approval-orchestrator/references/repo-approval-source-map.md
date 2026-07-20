# Repo Approval Source Map

Use this file as the repo-native entry point for `human-approval-orchestrator`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Workflow chains, routing matrices, and orchestration protocols.
4. Owner-certified internal records and primary transaction or project documents.
5. Prior approval claims only as context.

If the question is whether Danantara may act at all, use `investment-mandate-interpreter` or `mandate-authority-interpreter`. If the question is whether the analysis is good enough to decide on, use `decision-quality-gate`. This skill is only for who must approve and whether the approval is valid.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | End-to-end lifecycle and the handoff into approval. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Canonical workflow endings that require a human gate. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Formal skill roles and ownership. |
| `01-registry/workflow_routing_matrix.csv` | Which workflows require approval routing and what thresholds matter. |
| `02-governance/AI_CONSTITUTION.md` | Authority, evidence, decision rights, and stop conditions. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier thresholds that affect approver depth and quorum. |
| `04-skills/01-governance-doctrine/decision-rights-checker/references/repo-governance-source-map.md` | The proposer/reviewer/approver routing layer. |
| `04-skills/10-assurance-evaluation/decision-quality-gate/references/repo-quality-source-map.md` | The analysis-quality gate that runs before approval routing. |
| `08-sources/SOURCE_REGISTER.md` | The catalog of source tiers, including statutory and charter evidence. |

## Usage notes

- Use the source map before naming approvers or forums.
- Require sourced authority, not plausible seniority.
- Distinguish indeterminate routing from void approval.
- Never record approval from a claim, silence, or precedent.
