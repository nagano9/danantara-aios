# Repo Orchestration Source Map

Use this file as the repo-native entry point for `danantara-master-orchestrator`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Workflow protocol, routing matrix, and canonical chain definitions.
4. Owner-certified evidence, challenge notes, and audit records.
5. Prior plans only as context.

If the request asks for retrieval before classification, analysis before authority, or output without a human gate, the answer is `stop`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | The 13-step lifecycle and the one-way door between planning and retrieval. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Canonical end-to-end chains and where this skill sits. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Formal skill roles and ownership. |
| `01-registry/workflow_routing_matrix.csv` | Which workflows need orchestration and human approval. |
| `02-governance/AI_CONSTITUTION.md` | Authority, evidence, decision rights, and stop conditions. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier thresholds that change the required depth of the chain. |
| `04-skills/02-orchestration/human-approval-orchestrator/references/approval-validity-protocol.md` | The chain must terminate in valid human approval, not just routed approval. |
| `04-skills/10-assurance-evaluation/decision-quality-gate/references/decision-quality-protocol.md` | The pre-decision assurance gate that must close before approval. |
| `04-skills/10-assurance-evaluation/post-decision-learning/references/learning-loop-protocol.md` | The post-decision handoff if the chain continues into learning. |

## Usage notes

- Use the source map before composing the skill chain.
- Do not over-dispatch. Invoke the minimum sufficient set of skills that changes the decision.
- Keep challenge organizationally separate from proposal ownership.
- Preserve unresolved tensions; do not average them away in the orchestration layer.
