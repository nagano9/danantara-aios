# Repo Lifecycle Source Map

Use this file as the repo-native entry point for `skill-lifecycle-governor`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Skill estate registry, workflow routing matrix, and evaluation strategy.
4. Decision-feedback findings from `post-decision-learning`.
5. Prior skill changes only as context.

If a proposed change would change what gets approved, it is not editorial. If a skill has gated a decision, its version is immutable and must be superseded.

## Core repo sources

| File | Use |
|---|---|
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical skill ownership, role, and classification. |
| `01-registry/workflow_routing_matrix.csv` | Which workflows depend on the skill estate and where changes propagate. |
| `02-governance/AI_CONSTITUTION.md` | Governance boundary, evidence discipline, and stop rules. |
| `03-templates/ELITE_SKILL_STANDARD.md` | The quality bar and method requirements skills must not regress. |
| `04-skills/10-assurance-evaluation/post-decision-learning/references/learning-loop-protocol.md` | Arc 2 findings and the learning loop that can force a skill change. |
| `05-evaluations/EVALUATION_STRATEGY.md` | Trigger, functional, governance, adversarial, and regression evaluation expectations. |
| `04-skills/10-assurance-evaluation/skill-lifecycle-governor/references/skill-change-protocol.md` | The method itself. |

## Usage notes

- Use the source map before classifying a change.
- Threshold changes require a pattern, not a single outcome.
- Kernel edits propagate to all carriers or do not happen.
- Never lower a floor to make a build pass.
