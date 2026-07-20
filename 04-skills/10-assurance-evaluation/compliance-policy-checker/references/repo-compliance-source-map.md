# Repo Compliance Policy Source Map

Use this file as the repo-native entry point for `compliance-policy-checker`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved assurance artifacts and controlled templates.
3. Policy, standard, procedure, and control rules.
4. Skill-local trigger cases and reference notes.
5. Prior compliance outputs only as context.

If the question is about legal sufficiency, use `legal-sufficiency-checker`. If it is about confidentiality, use `confidentiality-leakage-check`.

## Core repo sources

| File | Use |
|---|---|
| `02-governance/AI_CONSTITUTION.md` | Governance boundary and policy hierarchy. |
| `02-governance/DANANTARA_WAY.md` | Institutional posture and compliance intent. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for compliance review. |
| `04-skills/10-assurance-evaluation/compliance-policy-checker/SKILL.md` | Skill scope and output contract. |
| `04-skills/10-assurance-evaluation/compliance-policy-checker/tests/trigger_cases.yaml` | Trigger examples for compliance cases. |
| `04-skills/10-assurance-evaluation/compliance-policy-checker/references/README.md` | Local approved reference staging area. |
| `04-skills/10-assurance-evaluation/skill-lifecycle-governor/SKILL.md` | Lifecycle and policy-governance precedent. |
| `04-skills/08-cross-functional/legal-sufficiency-checker/SKILL.md` | Legal sufficiency precedent. |

## Usage notes

- Use the source map before concluding a policy breach exists.
- Keep policy, procedure, and interpretation separate.
- Do not substitute style compliance for actual compliance.
