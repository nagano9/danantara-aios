# Repo Upstream Energy Sector Source Map

Use this file as the repo-native entry point for `upstream-energy-sector-pack`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Sector market, reserve, contracting, financing, and risk rules.
4. Skill-local trigger cases and reference notes.
5. Prior sector-pack outputs only as context.

If the question is about transition assets, use `energy-transition-sector-pack`. If it is about risk, use `scenario-stress-testing`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/DANANTARA_AIOS_BLUEPRINT.md` | System-level context for sector overlays. |
| `02-governance/AI_CONSTITUTION.md` | Governance boundary and evidence rules. |
| `02-governance/DANANTARA_WAY.md` | Institutional posture for upstream energy. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the sector pack. |
| `01-registry/workflow_routing_matrix.csv` | Routing for sector-pack work. |
| `04-skills/09-sector-overlays/upstream-energy-sector-pack/SKILL.md` | Skill scope and output contract. |
| `04-skills/09-sector-overlays/upstream-energy-sector-pack/tests/trigger_cases.yaml` | Trigger examples for upstream-energy cases. |
| `04-skills/09-sector-overlays/upstream-energy-sector-pack/references/README.md` | Local approved reference staging area. |
| `04-skills/09-sector-overlays/energy-transition-sector-pack/SKILL.md` | Transition precedent. |
| `04-skills/07-ddmf-development-finance/project-finance-structurer/SKILL.md` | Financing precedent. |

## Usage notes

- Use the source map before mixing legacy and transition logic.
- Keep reserves, cost, fiscal exposure, and strategy distinct.
- Do not assume upstream scale is automatically defensible.
