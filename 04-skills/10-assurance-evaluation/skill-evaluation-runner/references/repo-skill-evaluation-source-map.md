# Repo Skill Evaluation Source Map

Use this file as the repo-native entry point for `skill-evaluation-runner`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved assurance artifacts and controlled templates.
3. Skill schema, tests, acceptance criteria, and lifecycle rules.
4. Skill-local trigger cases and reference notes.
5. Prior evaluation outputs only as context.

If the question is about lifecycle governance, use `skill-lifecycle-governor`. If it is about audit evidence, use `audit-trail-packager`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Assurance lifecycle and handoff rules. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the skill. |
| `01-registry/workflow_routing_matrix.csv` | Routing for evaluation work. |
| `02-governance/AI_CONSTITUTION.md` | Authority and evidence boundary. |
| `04-skills/10-assurance-evaluation/skill-evaluation-runner/SKILL.md` | Skill scope and output contract. |
| `04-skills/10-assurance-evaluation/skill-evaluation-runner/tests/trigger_cases.yaml` | Trigger examples for evaluation cases. |
| `04-skills/10-assurance-evaluation/skill-evaluation-runner/references/README.md` | Local approved reference staging area. |
| `04-skills/10-assurance-evaluation/skill-lifecycle-governor/SKILL.md` | Lifecycle governance precedent. |
| `04-skills/10-assurance-evaluation/audit-trail-packager/SKILL.md` | Audit evidence precedent. |

## Usage notes

- Use the source map before judging a skill ready or not.
- Keep test results, policy checks, and lifecycle state separate.
- Do not treat a passing run as permanent approval.
