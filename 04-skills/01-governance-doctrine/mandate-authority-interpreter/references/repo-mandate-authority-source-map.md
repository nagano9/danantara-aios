# Repo Mandate Authority Source Map

Use this file as the repo-native entry point for `mandate-authority-interpreter`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Delegation, authority boundaries, and approval routing.
4. Skill-local trigger cases and reference notes.
5. Prior mandate interpretations only as context.

If the question is about whether a person or unit can decide, use `decision-rights-checker`. If approval is needed, use `human-approval-orchestrator`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/AI_CONSTITUTION.md` | Non-negotiable authority boundary. |
| `02-governance/DANANTARA_WAY.md` | Mandate framing and decision posture. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Approval routing and risk thresholds. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical placement of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Where authority checks enter the workflow. |
| `04-skills/01-governance-doctrine/mandate-authority-interpreter/SKILL.md` | Skill intent and interpretation scope. |
| `04-skills/01-governance-doctrine/mandate-authority-interpreter/tests/trigger_cases.yaml` | Trigger examples for authority questions. |
| `04-skills/01-governance-doctrine/mandate-authority-interpreter/references/README.md` | Local approved reference staging area. |
| `04-skills/01-governance-doctrine/decision-rights-checker/references/repo-governance-source-map.md` | Existing decision-rights precedent. |
| `04-skills/02-orchestration/human-approval-orchestrator/references/repo-approval-source-map.md` | Approval routing and escalation precedent. |

## Usage notes

- Use the source map before answering who can authorize what.
- Separate delegated authority from practical influence.
- Do not treat a signature chain as proof of mandate.
