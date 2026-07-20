# Agent Layer

This folder defines the repo's agent layer. Skills describe capability; agents
turn those capabilities into operational roles that can route work, curate
source-layer content, and enforce quality gates.

## Why this layer exists

The skill estate is broad, but a repo also needs execution roles that:

- decide where a request should go
- keep source and roadmap artifacts synchronized
- run consistency checks before changes spread
- provide a standard entry point for future workflows

Microsoft Agent Framework fits this design well because it supports:

- code-first agents in Python
- declarative agent definitions in YAML
- multi-agent orchestration patterns such as sequential, concurrent, and
  handoff flows
- human-in-the-loop and checkpoint-friendly workflows

See the official references:

- [Microsoft Agent Framework overview](https://learn.microsoft.com/en-us/agent-framework/overview/)
- [Python quickstart and samples](https://github.com/microsoft/agent-framework/blob/main/python/README.md)
- [Workflows overview](https://learn.microsoft.com/en-us/agent-framework/workflows/)
- [Agent types](https://learn.microsoft.com/en-us/agent-framework/agents/)

## Recommended first agents

1. `danantara-master-orchestrator`
2. `source-layer-curator`
3. `repo-audit-gate`

These three give the repo a practical operating loop:

`master orchestrator -> source curator -> audit gate`

## Workflow

The first end-to-end workflow is defined in
[`workflows/repo-agent-loop.yaml`](./workflows/repo-agent-loop.yaml) and can be
run with [`python/run_repo_agent_workflow.py`](./python/run_repo_agent_workflow.py).

## How they map to the repo

- `danantara-master-orchestrator` uses the orchestration skills already present
  in `02-orchestration/` to decide the right path for a task.
- `source-layer-curator` keeps `08-sources/`, `01-registry/`, and `09-roadmap/`
  aligned when source material or backlog items change.
- `repo-audit-gate` checks consistency across the source layer, backlog,
  roadmap, and build manifest.

## Implementation style

The recommended implementation is code-first in Python, with YAML used as a
versioned blueprint for stable agent roles.

That gives us:

- one source of truth for behavior in code
- readable agent specs for review and governance
- a path to declarative workflows later, when the orchestration becomes more
  complex

## What not to do

- do not duplicate the entire skill catalog as agents
- do not give agents broad write access without a gate
- do not let the agent layer become a second registry that drifts from the skill
  estate

## Next step

Use the Python adapter in `python/danantara_agents.py` as the first runtime
entry point if you want to invoke these roles locally. Use
`06-scripts/check_agent_layer.py` to verify the layer is still wired into the
repo docs after changes.
