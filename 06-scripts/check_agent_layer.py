#!/usr/bin/env python3
"""Structural checks for the repo-level agent layer."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

errors = []


def read(path: str) -> str:
    fp = ROOT / path
    if not fp.exists():
        errors.append(f"missing file: {path}")
        return ""
    return fp.read_text(encoding="utf-8")


def require(text: str, needle: str, file: str, message: str) -> None:
    if needle not in text:
        errors.append(f"{file}: missing '{needle}' ({message})")


readme = read("10-agents/README.md")
catalog = read("10-agents/AGENT_CATALOG.md")
master_yaml = read("10-agents/agents/danantara-master-orchestrator.yaml")
curator_yaml = read("10-agents/agents/source-layer-curator.yaml")
enrichment_yaml = read("10-agents/agents/source-layer-enrichment.yaml")
packager_yaml = read("10-agents/agents/decision-packager.yaml")
state_yaml = read("10-agents/agents/workflow-state-agent.yaml")
audit_yaml = read("10-agents/agents/repo-audit-gate.yaml")
workflow_yaml = read("10-agents/workflows/repo-agent-loop.yaml")
workflow_runner = read("10-agents/python/run_repo_agent_workflow.py")
python_adapter = read("10-agents/python/danantara_agents.py")
enrichment_plan = read("08-sources/SOURCE_LAYER_ENRICHMENT_PLAN.md")
decision_package = read("08-sources/DECISION_PACKAGE.md")
workflow_state = read("08-sources/WORKFLOW_STATE.md")
root_readme = read("README.md")
blueprint = read("00-blueprint/DANANTARA_AIOS_BLUEPRINT.md")
roadmap = read("09-roadmap/README.md")

require(readme, "Microsoft Agent Framework", "10-agents/README.md", "framework reference")
require(readme, "danantara-master-orchestrator", "10-agents/README.md", "core agent list")
require(catalog, "danantara-master-orchestrator", "10-agents/AGENT_CATALOG.md", "catalog entry")
require(catalog, "source-layer-curator", "10-agents/AGENT_CATALOG.md", "catalog entry")
require(catalog, "source-layer-enrichment", "10-agents/AGENT_CATALOG.md", "catalog entry")
require(catalog, "decision-packager", "10-agents/AGENT_CATALOG.md", "catalog entry")
require(catalog, "workflow-state-agent", "10-agents/AGENT_CATALOG.md", "catalog entry")
require(catalog, "repo-audit-gate", "10-agents/AGENT_CATALOG.md", "catalog entry")
require(master_yaml, "kind: Prompt", "10-agents/agents/danantara-master-orchestrator.yaml", "prompt agent template")
require(master_yaml, "outputSchema:", "10-agents/agents/danantara-master-orchestrator.yaml", "structured output")
require(curator_yaml, "source-layer curator", "10-agents/agents/source-layer-curator.yaml", "role wording")
require(enrichment_yaml, "SourceLayerEnrichment", "10-agents/agents/source-layer-enrichment.yaml", "agent name")
require(packager_yaml, "DecisionPackager", "10-agents/agents/decision-packager.yaml", "agent name")
require(state_yaml, "WorkflowStateAgent", "10-agents/agents/workflow-state-agent.yaml", "agent name")
require(audit_yaml, "RepoAuditGate", "10-agents/agents/repo-audit-gate.yaml", "agent name")
require(workflow_yaml, "repo-agent-loop", "10-agents/workflows/repo-agent-loop.yaml", "workflow name")
require(workflow_yaml, "RepoAuditGate", "10-agents/workflows/repo-agent-loop.yaml", "audit gate step")
require(workflow_yaml, "SourceLayerEnrichment", "10-agents/workflows/repo-agent-loop.yaml", "enrichment step")
require(workflow_yaml, "DecisionPackager", "10-agents/workflows/repo-agent-loop.yaml", "decision packaging step")
require(workflow_yaml, "WorkflowStateAgent", "10-agents/workflows/repo-agent-loop.yaml", "workflow state step")
require(workflow_runner, "build_workflow_factory", "10-agents/python/run_repo_agent_workflow.py", "workflow factory wiring")
require(workflow_runner, "repo-agent-loop.yaml", "10-agents/python/run_repo_agent_workflow.py", "workflow path")
require(python_adapter, "build_master_orchestrator", "10-agents/python/danantara_agents.py", "master factory")
require(python_adapter, "run_source_layer_audit", "10-agents/python/danantara_agents.py", "audit tool")
require(python_adapter, "generate_source_layer_enrichment_plan", "10-agents/python/danantara_agents.py", "enrichment tool")
require(python_adapter, "generate_decision_package", "10-agents/python/danantara_agents.py", "decision package tool")
require(python_adapter, "generate_workflow_state", "10-agents/python/danantara_agents.py", "workflow state tool")
require(python_adapter, "asyncio.run(main())", "10-agents/python/danantara_agents.py", "async entrypoint")
require(enrichment_plan, "Source Layer Enrichment Plan", "08-sources/SOURCE_LAYER_ENRICHMENT_PLAN.md", "enrichment artifact")
require(decision_package, "Decision Package", "08-sources/DECISION_PACKAGE.md", "decision package artifact")
require(workflow_state, "Workflow State", "08-sources/WORKFLOW_STATE.md", "workflow state artifact")
require(root_readme, "10-agents/", "README.md", "package contents")
require(blueprint, "Agent layer", "00-blueprint/DANANTARA_AIOS_BLUEPRINT.md", "agent layer section")
require(blueprint, "decision-packager", "00-blueprint/DANANTARA_AIOS_BLUEPRINT.md", "decision packager mention")
require(blueprint, "workflow-state-agent", "00-blueprint/DANANTARA_AIOS_BLUEPRINT.md", "workflow state mention")
require(roadmap, "agent layer", "09-roadmap/README.md", "agent layer mention")
require(roadmap, "decision packager", "09-roadmap/README.md", "decision packager mention")
require(roadmap, "workflow-state agent", "09-roadmap/README.md", "workflow state mention")

if errors:
    print(f"FAILED with {len(errors)} issue(s):")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("PASS: agent layer scaffolding is present and wired into the repo docs.")
