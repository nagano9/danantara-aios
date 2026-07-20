# Repo Enterprise Risk Source Map

Use this file as the repo-native entry point for `enterprise-risk-aggregator`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Enterprise risk taxonomy, aggregation, and double-count prevention rules.
4. Skill-local trigger cases and reference notes.
5. Prior risk outputs only as context.

If the question is about a specific legal issue, use `legal-sufficiency-checker`. If it is about scenario testing, use `scenario-stress-testing`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/AI_CONSTITUTION.md` | Governance boundary and authority rules. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Materiality and escalation thresholds. |
| `02-governance/DANANTARA_WAY.md` | Stewardship posture for aggregated risk. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Where enterprise risk review fits. |
| `04-skills/08-cross-functional/enterprise-risk-aggregator/SKILL.md` | Skill scope and output contract. |
| `04-skills/08-cross-functional/enterprise-risk-aggregator/tests/trigger_cases.yaml` | Trigger examples for enterprise risk cases. |
| `04-skills/08-cross-functional/enterprise-risk-aggregator/references/README.md` | Local approved reference staging area. |
| `04-skills/08-cross-functional/scenario-stress-testing/SKILL.md` | Scenario testing precedent. |
| `04-skills/08-cross-functional/legal-sufficiency-checker/SKILL.md` | Legal risk precedent. |

## Usage notes

- Use the source map before aggregating multiple specialist risks.
- Keep overlap, correlation, and double counting separate.
- Do not average away a severe issue in one domain.
