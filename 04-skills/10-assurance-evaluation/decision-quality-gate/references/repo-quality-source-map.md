# Repo Quality Source Map

Use this file as the repo-native entry point for `decision-quality-gate`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Decision pack evidence, models, challenge notes, and review records.
4. Independent specialist reviews and red-team outputs.
5. Prior decisions only as context.

If the pack blends findings, omits a dated prediction, or hides a blocker behind a condition, treat it as incomplete.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | End-to-end flow and the point where this gate sits. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Which workflows require this gate before approval. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the gate in the skill estate. |
| `01-registry/workflow_routing_matrix.csv` | Workflows that depend on this gate for routing. |
| `02-governance/AI_CONSTITUTION.md` | Required governance boundary, traceability, and refusal rules. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier implications for review depth and escalation. |
| `04-skills/02-orchestration/human-approval-orchestrator/references/approval-validity-protocol.md` | What happens after quality is good enough: approval validity remains separate. |
| `04-skills/10-assurance-evaluation/post-decision-learning/references/learning-loop-protocol.md` | Why a recorded prediction is mandatory before decision. |

## Usage notes

- Use the source map before drafting the verdict.
- Keep the four findings separate; never compress them into a single score.
- If the pack lacks a falsifiable prediction, return it.
- If downside is unbounded, stop or escalate instead of conditioning the risk.
