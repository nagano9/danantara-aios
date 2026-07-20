# Repo Escalation and Exception Source Map

Use this file as the repo-native entry point for `escalation-and-exception-router`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved orchestration artifacts and controlled templates.
3. Exception thresholds, escalation paths, and exception ownership.
4. Skill-local trigger cases and reference notes.
5. Prior escalation logs only as context.

If the question is about who must approve, use `human-approval-orchestrator`. If the question is about ownership, use `decision-rights-checker`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/RISK_APPROVAL_MATRIX.md` | Escalation threshold and approval level. |
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Lifecycle behavior for exception handling. |
| `01-registry/workflow_routing_matrix.csv` | Exception routing in the workflow. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the router. |
| `04-skills/02-orchestration/escalation-and-exception-router/SKILL.md` | Skill scope and response behavior. |
| `04-skills/02-orchestration/escalation-and-exception-router/tests/trigger_cases.yaml` | Trigger examples for exceptions. |
| `04-skills/02-orchestration/escalation-and-exception-router/references/README.md` | Local approved reference staging area. |
| `04-skills/02-orchestration/human-approval-orchestrator/references/repo-approval-source-map.md` | Approval escalation precedent. |
| `04-skills/01-governance-doctrine/decision-rights-checker/references/repo-governance-source-map.md` | Ownership and delegation precedent. |
| `04-skills/02-orchestration/workflow-state-manager/references/repo-workflow-source-map.md` | Post-exception state handling. |

## Usage notes

- Use the source map before deciding to bypass normal flow.
- Keep exception handling separate from exception justification.
- Do not treat every delay as an exception.
