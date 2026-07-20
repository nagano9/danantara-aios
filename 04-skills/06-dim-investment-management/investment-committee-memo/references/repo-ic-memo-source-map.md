# Repo IC Memo Source Map

Use this file as the repo-native entry point for `investment-committee-memo`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Thesis, assurance, approval, and audit protocols.
4. Owner-certified internal records and primary transaction or project documents.
5. Prior committee memos only as context.

If the question is whether the thesis holds, use `investment-thesis-builder`. If it is whether approval is valid, use `human-approval-orchestrator`.

## Core repo sources

| File | Use |
|---|---|
| `04-skills/06-dim-investment-management/investment-thesis-builder/SKILL.md` | Input thesis and recommendation. |
| `04-skills/10-assurance-evaluation/decision-quality-gate/references/repo-quality-source-map.md` | Pre-committee assurance. |
| `04-skills/02-orchestration/human-approval-orchestrator/references/repo-approval-source-map.md` | Approval validity and routing. |
| `04-skills/10-assurance-evaluation/audit-trail-packager/references/repo-audit-source-map.md` | Committee record and evidence retention. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Where the committee memo sits in the chain. |

## Usage notes

- Use the source map before drafting the committee memo.
- Keep memo writing separate from mandate and approval.
- Do not overwrite dissent with polished prose.
