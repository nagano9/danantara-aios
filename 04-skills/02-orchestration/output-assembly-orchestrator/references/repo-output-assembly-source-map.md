# Repo Output Assembly Source Map

Use this file as the repo-native entry point for `output-assembly-orchestrator`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved orchestration artifacts and controlled templates.
3. Assembly sequence, output packaging, and delivery format.
4. Skill-local trigger cases and reference notes.
5. Prior assembled outputs only as context.

If the question is about chain composition, use `skill-chain-composer`. If the question is about stateful handoff, use `workflow-state-manager`.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | Output assembly lifecycle and handoff rules. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Assembly chain structure. |
| `00-blueprint/workflow_chains.json` | Machine-readable chain topology. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the assembler. |
| `01-registry/workflow_routing_matrix.csv` | Where assembly enters the workflow. |
| `04-skills/02-orchestration/output-assembly-orchestrator/SKILL.md` | Skill scope and package assembly behavior. |
| `04-skills/02-orchestration/output-assembly-orchestrator/tests/trigger_cases.yaml` | Trigger examples for assembly cases. |
| `04-skills/02-orchestration/output-assembly-orchestrator/references/README.md` | Local approved reference staging area. |
| `04-skills/02-orchestration/skill-chain-composer/references/repo-chain-source-map.md` | Chain composition precedent. |
| `04-skills/02-orchestration/workflow-state-manager/references/repo-workflow-source-map.md` | State handoff precedent. |

## Usage notes

- Use the source map before packaging a final answer.
- Keep assembly order explicit.
- Do not merge disjoint evidence into one neat output.
