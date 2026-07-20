# Repo Bias and Independence Source Map

Use this file as the repo-native entry point for `bias-and-independence-review`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved assurance artifacts and controlled templates.
3. Independence, bias, dissent, and reviewer-quality rules.
4. Skill-local trigger cases and reference notes.
5. Prior review outputs only as context.

If the question is about decision quality, use `decision-quality-gate`. If it is about evidence handling, use `evidence-citation-auditor`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Assurance lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for assurance review. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `02-governance/DANANTARA_WAY.md` | Independence and stewardship posture. |
| `04-skills/10-assurance-evaluation/bias-and-independence-review/SKILL.md` | Skill scope and output contract. |
| `04-skills/10-assurance-evaluation/bias-and-independence-review/tests/trigger_cases.yaml` | Trigger examples for bias cases. |
| `04-skills/10-assurance-evaluation/bias-and-independence-review/references/README.md` | Local approved reference staging area. |
| `04-skills/10-assurance-evaluation/decision-quality-gate/SKILL.md` | Decision quality precedent. |
| `04-skills/10-assurance-evaluation/evidence-citation-auditor/SKILL.md` | Evidence citation precedent. |

## Usage notes

- Use the source map before calling a review independent.
- Keep bias, independence, and severity separate.
- Do not treat agreement as proof of independence.
