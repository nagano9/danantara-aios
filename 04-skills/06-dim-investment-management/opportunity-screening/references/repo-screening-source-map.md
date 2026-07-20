# Repo Screening Source Map

Use this file as the repo-native entry point for `opportunity-screening`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Mandate, screening criteria, approval paths, and portfolio limits.
4. Owner-certified internal records and primary transaction or project documents.
5. Prior screening outputs only as context.

If the question is whether the action is in mandate, use `investment-mandate-interpreter`. If it is whether the opportunity is worth pursuing, use `investment-thesis-builder`.

## Core repo sources

| File | Use |
|---|---|
| `04-skills/06-dim-investment-management/investment-mandate-interpreter/references/repo-mandate-source-map.md` | Mandate fit before screening. |
| `04-skills/06-dim-investment-management/investment-thesis-builder/SKILL.md` | Opportunity thesis after screening. |
| `04-skills/01-governance-doctrine/decision-rights-checker/references/repo-governance-source-map.md` | Approval path and decision rights. |
| `02-governance/AI_CONSTITUTION.md` | Governance boundary and refusal rules. |
| `01-registry/workflow_routing_matrix.csv` | Screening placement in the workflow. |

## Usage notes

- Use the source map before screening a pipeline.
- Keep eligibility separate from thesis and approval.
- Do not infer mandate from screening pressure.
