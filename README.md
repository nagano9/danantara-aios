# Danantara AIOS Claude Skills v1.0 — Draft Build Package

This package contains a governed enterprise Skills architecture for BPI Danantara, DAM, DIM, DDMF, portfolio entities, and authorized partners.

## Package contents
- **00-blueprint/** — AI ecosystem, orchestration, architecture, deployment model
- **01-registry/** — master registry in CSV and JSON, dependency edges, cluster summary
- **02-governance/** — Danantara Way, AI Constitution, risk and approval matrix
- **03-templates/** — canonical decision output and reusable SKILL.md template
- **04-skills/** — 133 skill directories, each with SKILL.md, references, and trigger tests
- **05-evaluations/** — portfolio-wide evaluation strategy and test scenarios
- **06-scripts/** — schema and governance validator
- **07-schemas/** — registry and decision-output schemas
- **08-sources/** — authoritative source register
- **09-roadmap/** — prioritized build plan, backlog themes, and next-release waves
- **10-agents/** — code-first and declarative agent layer for orchestration, enrichment, and audit

## Installation concept
For Claude Code, approved skills can be copied into the relevant `.claude/skills/` scope. Do not bulk-enable all critical skills without access control, tool restrictions, source configuration, human approval routing, and evaluation.

## Key design rule
This package is build-ready, not automatically production-authorized. Replace generic entity owners and source categories with actual Danantara policies, delegations, committee charters, named roles, systems, data classifications, tools, and review cycles.

## Validation status
The included validator checks:
- Agent Skills name pattern and directory match
- description length of 1–1024 characters
- required YAML fields
- required governance sections
- risk-tier values
- prohibited decision language
- registry consistency

Run:
```bash
python 06-scripts/validate_skills.py
```

## Development roadmap
The repository is structurally sound, but the next phase should focus on making
the operating system real rather than merely complete on paper.

See [`09-roadmap/README.md`](./09-roadmap/README.md) for the prioritized build
plan.

The agent layer in [`10-agents/`](./10-agents/) is the operational companion to
the skill layer. Skills define domain capability; agents turn those capabilities
into routable, inspectable, and reusable execution roles.

## Version
Draft 1.0.0, generated 2026-07-16.
