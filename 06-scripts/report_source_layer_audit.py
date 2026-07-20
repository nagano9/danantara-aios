#!/usr/bin/env python3
"""Report cross-artifact consistency for the source layer."""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "08-sources"
TIER2_ROOT = SOURCE_ROOT / "tier2"

ROOT_FILES = [
    "README.md",
    "WORKBOOK_CHANGE_REQUEST.md",
    "19_IMPLEMENTATION_BACKLOG.md",
    "TIER2_SOURCE_PACK.md",
    "TIER2_FILL_PLAYBOOK.md",
    "TIER2_STATUS.md",
    "SOURCE_LAYER_AUDIT.md",
]


def read_text(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


def count_tier2_docs():
    files = sorted(TIER2_ROOT.glob("[0-9][0-9]_*.md"))
    placeholder = 0
    promoted = 0
    for path in files:
        text = read_text(path)
        if "Placeholder." in text:
            placeholder += 1
        elif re.search(r"^## Identity$", text, re.M):
            promoted += 1
    return len(files), placeholder, promoted


def count_backlog_rows():
    text = read_text(SOURCE_ROOT / "19_IMPLEMENTATION_BACKLOG.md")
    return len(re.findall(r"^\| IB-\d{3} \|", text, re.M))


def has_phrase(path, phrase):
    return phrase in read_text(path)


def display_path(path):
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def parse_status_snapshot():
    text = read_text(SOURCE_ROOT / "TIER2_STATUS.md")
    result = {}
    for key, pattern in {
        "numbered_docs": r"^- numbered docs: (\d+)$",
        "placeholders": r"^- placeholders: (\d+)$",
        "promoted_sources": r"^- promoted sources: (\d+)$",
        "scaffold_files": r"^- scaffold files: (\d+)$",
        "total_markdown_files": r"^- total markdown files under `08-sources/tier2/`: (\d+)$",
        "backlog_rows": r"^- backlog rows: (\d+)$",
    }.items():
        match = re.search(pattern, text, re.M)
        result[key] = int(match.group(1)) if match else None
    return result


def render_markdown(summary):
    lines = [
        "# Source Layer Audit",
        "",
        "Snapshot date: 2026-07-20",
        "",
        "This report cross-checks the source register, Tier 2 scaffold, backlog,",
        "roadmap, workbook change request, and ingest bridge. It is a report, not",
        "a source of authority.",
        "",
        "## Checks",
        "",
        "| Check | Status | Evidence |",
        "|---|---|---|",
    ]
    for row in summary["checks"]:
        lines.append(f"| {row['check']} | {row['status']} | {row['evidence']} |")
    lines.extend(
        [
            "",
            "## Snapshot",
            "",
            f"- Tier 2 docs: {summary['tier2_docs']} placeholders, {summary['promoted_sources']} promoted",
            f"- Tier 2 scaffold files: {summary['scaffold_files']}",
            f"- Backlog rows: {summary['backlog_rows']}",
            f"- Open workbook change requests: {summary['open_change_requests']}",
            "",
            "## Open Gaps",
            "",
        ]
    )
    for gap in summary["gaps"]:
        lines.append(f"- {gap}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--markdown-out",
        type=Path,
        default=None,
        help="Write a markdown audit report to this path.",
    )
    args = ap.parse_args()

    tier2_docs, placeholders, promoted = count_tier2_docs()
    backlog_rows = count_backlog_rows()
    snapshot = parse_status_snapshot()

    checks = []

    present_root = [name for name in ROOT_FILES if (SOURCE_ROOT / name).exists()]
    checks.append(
        {
            "check": "Root source-layer artifacts",
            "status": "PASS" if len(present_root) == len(ROOT_FILES) else "FAIL",
            "evidence": f"{len(present_root)}/{len(ROOT_FILES)} present",
        }
    )

    checks.append(
        {
            "check": "Tier 2 status snapshot matches current counts",
            "status": "PASS"
            if snapshot["numbered_docs"] == tier2_docs
            and snapshot["placeholders"] == placeholders
            and snapshot["promoted_sources"] == promoted
            and snapshot["scaffold_files"] == 3
            and snapshot["total_markdown_files"] == 15
            and snapshot["backlog_rows"] == backlog_rows
            else "FAIL",
            "evidence": (
                f"snapshot={snapshot['numbered_docs']}/{snapshot['placeholders']}/{snapshot['promoted_sources']}"
                f"; actual={tier2_docs}/{placeholders}/{promoted}"
            ),
        }
    )

    checks.append(
        {
            "check": "Backlog includes IB-013",
            "status": "PASS" if "IB-013" in read_text(SOURCE_ROOT / "19_IMPLEMENTATION_BACKLOG.md") else "FAIL",
            "evidence": "IB-013 present",
        }
    )

    checks.append(
        {
            "check": "Workbook change request still open",
            "status": "PASS" if has_phrase(SOURCE_ROOT / "WORKBOOK_CHANGE_REQUEST.md", "CR-001") else "FAIL",
            "evidence": "CR-001 referenced",
        }
    )

    checks.append(
        {
            "check": "Ingest bridge supports markdown summaries",
            "status": "PASS" if has_phrase(ROOT / "06-scripts" / "ingest_actual_condition.py", "--markdown-out") else "FAIL",
            "evidence": "--markdown-out flag present",
        }
    )

    checks.append(
        {
            "check": "Source register acknowledges scaffold state",
            "status": "PASS"
            if has_phrase(SOURCE_ROOT / "SOURCE_REGISTER.md", "scaffold is now in place")
            and has_phrase(SOURCE_ROOT / "SOURCE_REGISTER.md", "repository now includes the Tier 2 source pack")
            else "FAIL",
            "evidence": "Tier 2 scaffold wording present",
        }
    )

    checks.append(
        {
            "check": "Roadmap acknowledges scaffold and ingestion bridge",
            "status": "PASS"
            if has_phrase(ROOT / "09-roadmap" / "README.md", "Tier 2 scaffold, fill playbook, status snapshot, and backlog sink now")
            and has_phrase(ROOT / "09-roadmap" / "README.md", "promote authenticated source documents into the Tier 2 scaffold")
            else "FAIL",
            "evidence": "roadmap updated",
        }
    )

    checks.append(
        {
            "check": "README mentions audit/report tooling",
            "status": "PASS"
            if has_phrase(SOURCE_ROOT / "README.md", "report_source_layer_audit.py")
            and has_phrase(SOURCE_ROOT / "README.md", "report_tier2_status.py")
            else "FAIL",
            "evidence": "README tooling references present",
        }
    )

    checks.append(
        {
            "check": "Tier 2 status tracks the audit report",
            "status": "PASS"
            if has_phrase(SOURCE_ROOT / "TIER2_STATUS.md", "source-layer audit report exists")
            else "FAIL",
            "evidence": "audit report referenced in Tier 2 status",
        }
    )

    open_crs = 1 if has_phrase(SOURCE_ROOT / "WORKBOOK_CHANGE_REQUEST.md", "Status: **open**") else 0
    gaps = [
        "Authenticated Tier 2 source documents are still missing.",
        "The external workbook is intentionally not committed to the repository.",
        "The source-layer audit report should be regenerated after any Tier 2 scaffold change.",
    ]

    summary = {
        "checks": checks,
        "tier2_docs": placeholders,
        "promoted_sources": promoted,
        "scaffold_files": 3,
        "backlog_rows": backlog_rows,
        "open_change_requests": open_crs,
        "gaps": gaps,
    }

    print("Source layer audit")
    for row in checks:
        print(f"  {row['check']:<45} {row['status']}  {row['evidence']}")
    print()
    print(f"Tier 2 docs      : {placeholders} placeholders, {promoted} promoted")
    print(f"Backlog rows     : {backlog_rows}")
    print(f"Open change reqs : {open_crs}")
    if args.markdown_out is not None:
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_out.write_text(render_markdown(summary), encoding="utf-8")
        print(f"Wrote {display_path(args.markdown_out)}")


if __name__ == "__main__":
    main()
