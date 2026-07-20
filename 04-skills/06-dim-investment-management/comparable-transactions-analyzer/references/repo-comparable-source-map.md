# Repo Comparable Transactions Source Map

Use this file as the repo-native entry point for `comparable-transactions-analyzer`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Comparable-company and precedent-transaction selection and normalization rules.
4. Skill-local trigger cases and reference notes.
5. Prior comparable outputs only as context.

If the question is about thesis or screening, use `investment-thesis-builder` or `opportunity-screening`. If it is about valuation, use `valuation-orchestrator`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for valuation work. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `04-skills/06-dim-investment-management/comparable-transactions-analyzer/SKILL.md` | Skill scope and output contract. |
| `04-skills/06-dim-investment-management/comparable-transactions-analyzer/tests/trigger_cases.yaml` | Trigger examples for comparable cases. |
| `04-skills/06-dim-investment-management/comparable-transactions-analyzer/references/README.md` | Local approved reference staging area. |
| `04-skills/06-dim-investment-management/valuation-orchestrator/SKILL.md` | Valuation precedent. |
| `04-skills/06-dim-investment-management/investment-thesis-builder/SKILL.md` | Thesis precedent. |

## Usage notes

- Use the source map before selecting comparables.
- Keep business model, control, timing, and geography adjustments explicit.
- Do not let a convenient peer set bias the valuation.
