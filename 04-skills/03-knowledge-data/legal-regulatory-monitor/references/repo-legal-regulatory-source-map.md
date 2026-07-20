# Repo Legal Regulatory Source Map

Use this file as the repo-native entry point for `legal-regulatory-monitor`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved governance and registry artifacts.
3. Regulatory watch items, policy changes, and precedent signals.
4. Skill-local trigger cases and reference notes.
5. Prior monitoring outputs only as context.

If the question is about policy interpretation, use `policy-knowledge-curator`. If the question is about precedent evidence, use `decision-precedent-retriever`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/AI_CONSTITUTION.md` | Hard governance boundary for monitoring outputs. |
| `02-governance/DANANTARA_WAY.md` | Institutional posture for legal and policy watch. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Escalation thresholds for regulatory changes. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the monitor. |
| `01-registry/workflow_routing_matrix.csv` | Where legal watch enters the workflow. |
| `04-skills/03-knowledge-data/legal-regulatory-monitor/SKILL.md` | Skill scope and monitoring behavior. |
| `04-skills/03-knowledge-data/legal-regulatory-monitor/tests/trigger_cases.yaml` | Trigger examples for monitoring cases. |
| `04-skills/03-knowledge-data/legal-regulatory-monitor/references/README.md` | Local approved reference staging area. |
| `04-skills/03-knowledge-data/policy-knowledge-curator/SKILL.md` | Policy curation pattern for regulatory signals. |
| `04-skills/03-knowledge-data/decision-precedent-retriever/references/repo-precedent-source-map.md` | Precedent-backed monitoring pattern. |

## Usage notes

- Use the source map before stating that a rule changed.
- Keep observed change separate from interpretation.
- Do not present monitoring as legal advice.
