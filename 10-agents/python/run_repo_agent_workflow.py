#!/usr/bin/env python3
"""Run the repo agent workflow end to end."""
from __future__ import annotations

import argparse
import asyncio
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from danantara_agents import build_workflow_factory  # noqa: E402


def _print_result(result) -> None:
    outputs = []
    if hasattr(result, "get_outputs"):
        try:
            outputs = list(result.get_outputs())
        except Exception:
            outputs = []
    if outputs:
        for output in outputs:
            print(f"Output: {output}")
        return
    print(getattr(result, "text", result))


async def main() -> int:
    parser = argparse.ArgumentParser(description="Run the Danantara repo workflow.")
    parser.add_argument("--request", required=True, help="Task to route through the agent stack.")
    parser.add_argument("--focus", default="source-layer", help="Optional focus area.")
    args = parser.parse_args()

    factory = build_workflow_factory()
    workflow_path = ROOT / "10-agents" / "workflows" / "repo-agent-loop.yaml"
    workflow = factory.create_workflow_from_yaml_path(workflow_path)
    result = await workflow.run({"request": args.request, "focus": args.focus})
    _print_result(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
