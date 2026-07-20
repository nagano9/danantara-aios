# Repo Red Team Orchestrator Source Map

Use this file as the repo-native entry point for `red-team-orchestrator`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved orchestration artifacts and controlled templates.
3. Stress-test criteria, counterarguments, and failure modes.
4. Skill-local trigger cases and reference notes.
5. Prior red-team outputs only as context.

If the question is about the quality of a decision, use `decision-quality-gate`. If it is about what should be learned after the fact, use `post-decision-learning`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Stress-test placement in the lifecycle. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the red team. |
| `01-registry/PRINCIPLE_SKILL_COVERAGE.md` | Principle coverage for challenge and dissent. |
| `01-registry/workflow_routing_matrix.csv` | Where the red team enters the workflow. |
| `04-skills/02-orchestration/red-team-orchestrator/SKILL.md` | Skill scope and challenge behavior. |
| `04-skills/02-orchestration/red-team-orchestrator/tests/trigger_cases.yaml` | Trigger examples for red-team cases. |
| `04-skills/02-orchestration/red-team-orchestrator/references/README.md` | Local approved reference staging area. |
| `04-skills/10-assurance-evaluation/decision-quality-gate/references/repo-quality-source-map.md` | Existing decision-quality precedent. |
| `04-skills/10-assurance-evaluation/post-decision-learning/references/repo-learning-source-map.md` | Post-decision learning precedent. |
| `04-skills/01-governance-doctrine/long-term-value-test/references/repo-long-term-value-source-map.md` | Long-horizon downside precedent. |

## Usage notes

- Use the source map before validating an apparently strong proposal.
- Keep challenge evidence separate from the final judgment.
- Do not let dissent become performative.
