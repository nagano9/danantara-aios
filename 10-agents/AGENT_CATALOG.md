# Agent Catalog

This catalog defines the first repo-level agents. They are intentionally small,
because the repository already has deep domain coverage in skills.

## Core agents

| Agent | Purpose | Trigger | Primary inputs | Output |
|---|---|---|---|---|
| `danantara-master-orchestrator` | Route a request to the right skill chain or repo operation | Any ambiguous, multi-step, or cross-folder request | User intent, repo status, source layer state, skill registry context | Routing plan, next agent, required skills, and human gate |
| `source-layer-curator` | Keep source-layer artifacts and roadmap in sync | Source updates, backlog changes, new evidence, or placeholder promotion | `08-sources/`, `01-registry/`, `09-roadmap/`, `06-scripts/` | Suggested edits, consistency notes, and promotion candidates |
| `source-layer-enrichment` | Convert source-layer findings into a concrete enrichment plan artifact | Source audit results, backlog closure, or roadmap updates | Audit report, backlog, roadmap, status snapshot | Generated enrichment plan and follow-up files |
| `repo-audit-gate` | Detect drift, missing artifacts, and consistency gaps | Before merges, after source updates, or after scaffold changes | Manifest, source register, roadmap, status snapshot, script checks | Audit summary, failed checks, and remediation list |

## Workflow pairing

| Workflow | Purpose |
|---|---|
| `repo-agent-loop` | Routes a repo task, curates the source layer, generates an enrichment plan, runs repository checks, and returns a consolidated result |

## Recommended tool scope

| Agent | Safe tools |
|---|---|
| `danantara-master-orchestrator` | Read-only repo inspection, status reporting, audit script execution |
| `source-layer-curator` | Read-only repo inspection, source audit, status reporting |
| `repo-audit-gate` | Audit scripts, repo hygiene checks, manifest checks |
| `source-layer-enrichment` | Read-only repo inspection plus the enrichment plan generator |

## Future agents

These are natural next additions once the first four are stable:

- `knowledge-enrichment-agent` for converting new evidence into source-layer
  updates
- `workflow-state-agent` for tracking long-running repo or program states
- `decision-packager-agent` for generating board-ready or committee-ready
  summaries from the existing skill outputs

## Design rule

If a task can be handled by an existing skill, do not re-encode it as a new
agent. Agents should route and coordinate, not duplicate domain logic.
