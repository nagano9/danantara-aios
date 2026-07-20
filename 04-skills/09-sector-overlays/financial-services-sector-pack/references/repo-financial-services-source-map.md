# Repo Financial Services Sector Source Map

Use this file as the repo-native entry point for `financial-services-sector-pack`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Sector market, regulation, technology, risk, and valuation rules.
4. Skill-local trigger cases and reference notes.
5. Prior sector-pack outputs only as context.

If the question is about risk aggregation or controls, use `enterprise-risk-aggregator`. If it is about model validation, use `financial-model-validator`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/DANANTARA_AIOS_BLUEPRINT.md` | System-level context for sector overlays. |
| `02-governance/AI_CONSTITUTION.md` | Governance boundary and evidence rules. |
| `02-governance/DANANTARA_WAY.md` | Institutional posture for financial-services analysis. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the sector pack. |
| `01-registry/workflow_routing_matrix.csv` | Routing for sector-pack work. |
| `04-skills/09-sector-overlays/financial-services-sector-pack/SKILL.md` | Skill scope and output contract. |
| `04-skills/09-sector-overlays/financial-services-sector-pack/tests/trigger_cases.yaml` | Trigger examples for financial-services cases. |
| `04-skills/09-sector-overlays/financial-services-sector-pack/references/README.md` | Local approved reference staging area. |
| `04-skills/08-cross-functional/enterprise-risk-aggregator/SKILL.md` | Risk aggregation precedent. |
| `04-skills/08-cross-functional/financial-model-validator/SKILL.md` | Model validation precedent. |

## Usage notes

- Use the source map before making a sector call.
- Keep regulation, competition, and balance-sheet strength separate.
- Do not treat financial depth as automatic resilience.
