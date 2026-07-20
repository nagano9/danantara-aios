#!/usr/bin/env python3
"""Validate the Tier 2 source-layer scaffold.

This check ensures the source-layer working area stays internally consistent
while Tier 2 documents are still placeholders.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "08-sources"
TIER2_ROOT = SOURCE_ROOT / "tier2"

EXPECTED_ROOT_FILES = {
    SOURCE_ROOT / "README.md",
    SOURCE_ROOT / "19_IMPLEMENTATION_BACKLOG.md",
    SOURCE_ROOT / "TIER2_SOURCE_PACK.md",
    SOURCE_ROOT / "TIER2_FILL_PLAYBOOK.md",
    SOURCE_ROOT / "TIER2_STATUS.md",
}

EXPECTED_TIER2_FILES = {
    TIER2_ROOT / "README.md",
    TIER2_ROOT / "INDEX.md",
    TIER2_ROOT / "TIER2_SOURCE_TEMPLATE.md",
    TIER2_ROOT / "01_dewan_pengawas_charter.md",
    TIER2_ROOT / "02_badan_pelaksana_doa.md",
    TIER2_ROOT / "03_dim_ic_charter.md",
    TIER2_ROOT / "04_dam_active_ownership_policy.md",
    TIER2_ROOT / "05_ddmf_additionality_policy.md",
    TIER2_ROOT / "06_investment_policy_statement.md",
    TIER2_ROOT / "07_valuation_policy.md",
    TIER2_ROOT / "08_conflict_of_interest_policy.md",
    TIER2_ROOT / "09_data_classification_policy.md",
    TIER2_ROOT / "10_procurement_integrity_standard.md",
    TIER2_ROOT / "11_whistleblowing_escalation.md",
    TIER2_ROOT / "12_entity_model_map.md",
}

EXPECTED_BACKLOG_IDS = {
    "IB-001", "IB-002", "IB-003", "IB-004", "IB-005", "IB-006", "IB-007",
    "IB-008", "IB-009", "IB-010", "IB-011", "IB-012", "IB-013",
}

errors = []

missing_root = [p for p in EXPECTED_ROOT_FILES if not p.exists()]
missing_tier2 = [p for p in EXPECTED_TIER2_FILES if not p.exists()]
if missing_root:
    errors.append("missing root source files:\n- " + "\n- ".join(str(p.relative_to(ROOT)) for p in missing_root))
if missing_tier2:
    errors.append("missing tier2 files:\n- " + "\n- ".join(str(p.relative_to(ROOT)) for p in missing_tier2))

index_path = TIER2_ROOT / "INDEX.md"
if index_path.exists():
    text = index_path.read_text(encoding="utf-8")
    for code in [f"T2-{i:02d}" for i in range(1, 13)]:
        if code not in text:
            errors.append(f"INDEX.md missing code {code}")

backlog_path = SOURCE_ROOT / "19_IMPLEMENTATION_BACKLOG.md"
if backlog_path.exists():
    text = backlog_path.read_text(encoding="utf-8")
    for bid in EXPECTED_BACKLOG_IDS:
        if bid not in text:
            errors.append(f"19_IMPLEMENTATION_BACKLOG.md missing {bid}")
    if "Priority is measured by how many decisions the gap blocks." not in text:
        errors.append("19_IMPLEMENTATION_BACKLOG.md missing operating rule about blocking pressure")

pack_path = SOURCE_ROOT / "TIER2_SOURCE_PACK.md"
if pack_path.exists():
    text = pack_path.read_text(encoding="utf-8")
    if "delegation of authority matrix" not in text.lower():
        errors.append("TIER2_SOURCE_PACK.md does not describe the required document set")
    for code in [f"T2-{i:02d}" for i in range(1, 13)]:
        if code not in text:
            errors.append(f"TIER2_SOURCE_PACK.md missing {code}")

playbook_path = SOURCE_ROOT / "TIER2_FILL_PLAYBOOK.md"
if playbook_path.exists():
    text = playbook_path.read_text(encoding="utf-8")
    required_phrases = [
        "## Purpose",
        "## Fill order",
        "## Minimum evidence for promotion",
        "## Promotion workflow",
        "## Crosswalk to backlog",
        "## Quality checks",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"TIER2_FILL_PLAYBOOK.md missing heading {phrase}")

status_path = SOURCE_ROOT / "TIER2_STATUS.md"
if status_path.exists():
    text = status_path.read_text(encoding="utf-8")
    required_phrases = [
        "## Snapshot",
        "## What is live",
        "## What is still missing",
        "## Next priority order",
        "## Validation",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            errors.append(f"TIER2_STATUS.md missing heading {phrase}")

template_path = TIER2_ROOT / "TIER2_SOURCE_TEMPLATE.md"
if template_path.exists():
    text = template_path.read_text(encoding="utf-8")
    required = [
        "## Identity",
        "## Purpose",
        "## Scope",
        "## Key rules",
        "## Decision impact",
        "## Retrieval note",
    ]
    for heading in required:
        if heading not in text:
            errors.append(f"TIER2_SOURCE_TEMPLATE.md missing heading {heading}")

print(f"Checked Tier 2 source-layer scaffold under {SOURCE_ROOT.relative_to(ROOT)}")
if errors:
    print(f"FAILED with {len(errors)} issue(s):")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)
print("PASS: Tier 2 source-layer scaffold is in sync.")
