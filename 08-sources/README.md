# Source Layer

This folder groups the source register, the workbook change request, the
implementation backlog, and the Tier 2 source-pack workspace.

## What lives here

- `SOURCE_REGISTER.md` - authoritative source hierarchy and gaps
- `WORKBOOK_CHANGE_REQUEST.md` - open workbook change request CR-001
- `19_IMPLEMENTATION_BACKLOG.md` - sink for blocked or indeterminate decisions
- `TIER2_SOURCE_PACK.md` - index and folder plan for missing Tier 2 sources
- `TIER2_FILL_PLAYBOOK.md` - the operating playbook for promoting placeholders
- `TIER2_STATUS.md` - current status snapshot for the Tier 2 working area
- `SOURCE_LAYER_AUDIT.md` - cross-artifact consistency audit for the source layer
- `SOURCE_LAYER_ENRICHMENT_PLAN.md` - tracked enrichment plan generated from
  source-layer findings
- `DECISION_PACKAGE.md` - consolidated handoff package from the agent loop
- `tier2/` - working folder for Tier 2 source documents
- `tier2/INDEX.md` - working index for Tier 2 placeholders
- `tier2/TIER2_SOURCE_TEMPLATE.md` - standard template for future authenticated sources

## Helper script

- `06-scripts/bootstrap_tier2_source_pack.py` can recreate the source-layer
  scaffolding if files are removed.
- `06-scripts/check_tier2_source_pack.py` validates that the Tier 2 scaffold is
  still internally consistent.
- `06-scripts/ingest_actual_condition.py` can ingest the external workbook and
  emit `tier2_index.json` plus an optional markdown status summary.
- `06-scripts/report_source_layer_audit.py` cross-checks the source register,
  roadmap, backlog, and Tier 2 status into a single audit view.
- `06-scripts/report_tier2_status.py` prints a quick status summary for the
  Tier 2 working area.
- `10-agents/python/danantara_agents.py` can generate
  `SOURCE_LAYER_ENRICHMENT_PLAN.md` from the current audit, backlog, and
  roadmap state.
- `10-agents/python/danantara_agents.py` can also generate
  `DECISION_PACKAGE.md` from the current workflow outputs.

## Priority

The source layer is the highest-leverage part of the operating system because it
decides whether downstream skills can answer from real Danantara instruments or
only from a generic template.
