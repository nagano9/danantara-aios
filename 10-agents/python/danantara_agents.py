#!/usr/bin/env python3
"""Code-first Danantara agent stack.

This module provides a small local agent layer for the repo.

The recommended use is:
1. master orchestrator for routing
2. source-layer curator for enrichment and alignment
3. repo audit gate for consistency checks

Install:
    pip install agent-framework

Environment:
    OPENAI_API_KEY or another supported provider configuration
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path
import asyncio

ROOT = Path(__file__).resolve().parents[2]


def _run_command(args: list[str]) -> str:
    """Run a safe repo-local command and return combined output."""
    proc = subprocess.run(
        args,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    if not output.strip():
        output = f"(exit code {proc.returncode})"
    return output.strip()


def get_repo_status() -> str:
    """Return a short git status snapshot for the repo."""
    return _run_command(["git", "status", "--short", "--branch"])


def run_source_layer_audit() -> str:
    """Run the source-layer audit script."""
    return _run_command([sys.executable, str(ROOT / "06-scripts" / "report_source_layer_audit.py")])


def run_repo_hygiene() -> str:
    """Run the repo hygiene guard."""
    return _run_command([sys.executable, str(ROOT / "06-scripts" / "check_repo_hygiene.py")])


def read_repo_file(relative_path: str) -> str:
    """Read a text file inside the repo root."""
    candidate = (ROOT / relative_path).resolve()
    if ROOT not in candidate.parents and candidate != ROOT:
        return "Refused: path escapes repository root."
    if not candidate.exists():
        return f"Missing file: {relative_path}"
    return candidate.read_text(encoding="utf-8")


def list_agent_files() -> str:
    """List the agent layer files."""
    agent_root = ROOT / "10-agents"
    if not agent_root.exists():
        return "Missing agent layer."
    files = sorted(
        str(path.relative_to(ROOT)).replace("\\", "/")
        for path in agent_root.rglob("*")
        if path.is_file()
    )
    return "\n".join(files)


def _chat_client():
    from agent_framework.openai import OpenAIChatClient

    return OpenAIChatClient()


def build_master_orchestrator():
    """Create the master routing agent."""
    from agent_framework import Agent

    return Agent(
        name="DanantaraMasterOrchestrator",
        client=_chat_client(),
        instructions=(
            "Route Danantara requests to the right skill chain or repo operation. "
            "Use the source-layer curator for enrichment tasks and the repo audit "
            "gate for consistency checks. Keep outputs concise, evidence-aware, "
            "and approval-aware."
        ),
        tools=[get_repo_status, list_agent_files, run_source_layer_audit, run_repo_hygiene, read_repo_file],
    )


def build_source_layer_curator():
    """Create the source-layer curator agent."""
    from agent_framework import Agent

    return Agent(
        name="SourceLayerCurator",
        client=_chat_client(),
        instructions=(
            "Curate the source layer, backlog, and roadmap. Focus on keeping "
            "08-sources, 01-registry, 09-roadmap, and the audit artifacts aligned. "
            "Prefer small, traceable updates over speculative expansion."
        ),
        tools=[get_repo_status, list_agent_files, run_source_layer_audit, read_repo_file],
    )


def build_repo_audit_gate():
    """Create the repository audit gate agent."""
    from agent_framework import Agent

    return Agent(
        name="RepoAuditGate",
        client=_chat_client(),
        instructions=(
            "Check the repo for drift and consistency issues. Use the audit script "
            "and repo hygiene guard to validate changes before they are promoted."
        ),
        tools=[get_repo_status, run_source_layer_audit, run_repo_hygiene, read_repo_file],
    )


def build_agent_stack() -> dict[str, object]:
    """Build the default repo agent stack."""
    return {
        "master": build_master_orchestrator(),
        "curator": build_source_layer_curator(),
        "audit": build_repo_audit_gate(),
    }


def build_workflow_factory():
    """Create a workflow factory wired to the local repo agents and tools."""
    from agent_framework.declarative import WorkflowFactory

    return (
        WorkflowFactory()
        .register_agent("DanantaraMasterOrchestrator", build_master_orchestrator())
        .register_agent("SourceLayerCurator", build_source_layer_curator())
        .register_agent("RepoAuditGate", build_repo_audit_gate())
        .register_tool("run_source_layer_audit", run_source_layer_audit)
        .register_tool("run_repo_hygiene", run_repo_hygiene)
    )


async def main() -> int:
    parser = argparse.ArgumentParser(description="Run a Danantara repo agent locally.")
    parser.add_argument(
        "--agent",
        choices=("master", "curator", "audit"),
        default="master",
        help="Which agent to run.",
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="Task prompt for the selected agent.",
    )
    args = parser.parse_args()

    stack = build_agent_stack()
    agent = stack[args.agent]
    result = await agent.run(args.prompt)
    print(getattr(result, "text", result))
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
