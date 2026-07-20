# Repo Audit Source Map

Use this file as the repo-native entry point for `audit-trail-packager`. It is an index, not an authority by itself.

## Source order

1. Law, regulation, official decision, and formal mandate.
2. Approved Danantara governance artifacts and controlled templates.
3. Decision records, evidence packs, approval records, challenge notes, and review records.
4. Independent assurance findings and remediation records.
5. Prior audit trails only as context.

If the record is missing evidence, omits a dated decision, or mixes findings with assertions, treat the pack as incomplete.

## Core repo sources

| File | Use |
|---|---|
| `00-blueprint/MASTER_ORCHESTRATION_PROTOCOL.md` | End-to-end lifecycle and where material evidence must be captured. |
| `00-blueprint/WORKFLOW_CHAINS.md` | Which workflows require a packaged audit record at the handoff. |
| `01-registry/MASTER_SKILL_CATALOG.md` | Canonical role of the packaging skill in the estate. |
| `01-registry/workflow_routing_matrix.csv` | Workflows that depend on audit packaging and record retention. |
| `02-governance/AI_CONSTITUTION.md` | Required governance boundary, traceability, and refusal rules. |
| `02-governance/RISK_APPROVAL_MATRIX.md` | Risk-tier implications for record depth and escalation. |
| `04-skills/01-governance-doctrine/conflict-of-interest-gate/references/repo-conflict-source-map.md` | Conflict findings that may need to be captured in the record. |
| `04-skills/02-orchestration/human-approval-orchestrator/references/repo-approval-source-map.md` | The approval validity record that must not be fabricated. |
| `04-skills/10-assurance-evaluation/decision-quality-gate/references/repo-quality-source-map.md` | The pre-decision assurance verdict that may feed the audit trail. |
| `04-skills/10-assurance-evaluation/post-decision-learning/references/repo-learning-source-map.md` | The downstream learning record that closes the loop. |
| `04-skills/10-assurance-evaluation/skill-lifecycle-governor/references/repo-lifecycle-source-map.md` | The rule for versioned skill changes when audit findings imply a defect. |

## Usage notes

- Use the source map before packaging a material milestone.
- Keep evidence, assumptions, challenges, approvals, and conditions separate.
- The packaging skill does not cure missing approval, conflict, or quality defects.
- If the record is incomplete, say so rather than filling gaps.
