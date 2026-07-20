#!/usr/bin/env python3
"""Report the status of the Tier 2 source-layer scaffold."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "08-sources"
TIER2_ROOT = SOURCE_ROOT / "tier2"


def count_placeholders():
    files = sorted(TIER2_ROOT.glob("[0-9][0-9]_*.md"))
    placeholder = 0
    promoted = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        if "Placeholder." in text:
            placeholder += 1
        elif re.search(r"^## Identity$", text, re.M):
            promoted += 1
    return placeholder, promoted


def count_backlog_rows():
    text = (SOURCE_ROOT / "19_IMPLEMENTATION_BACKLOG.md").read_text(encoding="utf-8")
    return len(re.findall(r"^\| IB-\d{3} \|", text, re.M))


def main():
    placeholder, promoted = count_placeholders()
    backlog_rows = count_backlog_rows()
    scaffold_files = sum(
        1
        for name in ("README.md", "INDEX.md", "TIER2_SOURCE_TEMPLATE.md")
        if (TIER2_ROOT / name).exists()
    )
    total = placeholder + promoted + scaffold_files

    print("Tier 2 source-layer status")
    print(f"  numbered docs        : {placeholder + promoted}")
    print(f"  placeholders         : {placeholder}")
    print(f"  promoted sources     : {promoted}")
    print(f"  scaffold files       : {scaffold_files}")
    print(f"  total markdown files : {total}")
    print(f"  backlog rows         : {backlog_rows}")
    print()
    print("Next priority order:")
    for line in (SOURCE_ROOT / "TIER2_SOURCE_PACK.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("1. ") or line.startswith("2. ") or line.startswith("3. "):
            print(f"  {line}")


if __name__ == "__main__":
    main()
