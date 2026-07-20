# Repo Legal Sufficiency Source Map

Use this file as the repo-native entry point for `legal-sufficiency-checker`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Legal sufficiency, authority, delegation, and interpretation rules.
4. Skill-local trigger cases and reference notes.
5. Prior legal outputs only as context.

If the question is about a broader policy review, use `compliance-policy-checker`. If it is about decision rights, use `decision-rights-checker`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/AI_CONSTITUTION.md` | Legal authority and evidence boundary. |
| `02-governance/DANANTARA_WAY.md` | Institutional posture for lawful action. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Escalation and approval thresholds. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for legal review. |
| `04-skills/08-cross-functional/legal-sufficiency-checker/SKILL.md` | Skill scope and output contract. |
| `04-skills/08-cross-functional/legal-sufficiency-checker/tests/trigger_cases.yaml` | Trigger examples for legal sufficiency cases. |
| `04-skills/08-cross-functional/legal-sufficiency-checker/references/README.md` | Local approved reference staging area. |
| `04-skills/01-governance-doctrine/decision-rights-checker/references/repo-governance-source-map.md` | Decision-rights precedent. |
| `04-skills/10-assurance-evaluation/compliance-policy-checker/references/repo-compliance-source-map.md` | Compliance precedent. |

## Usage notes

- Use the source map before calling something legally sufficient.
- Keep authority, interpretation, and process compliance separate.
- Do not treat procedural comfort as legal certainty.
