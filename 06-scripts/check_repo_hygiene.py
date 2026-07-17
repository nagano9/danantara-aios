#!/usr/bin/env python3
"""Structural guards for the danantara-aios repository.

validate_skills.py checks that skills are well-formed. This checks that the
repository carrying them is well-formed. Both failures found during the
2026-07-16 audit were invisible to the skill validator:

  - a 642 KB zip of this tree, committed inside the tree it snapshots
  - a nested .git in 04-skills/, which turns the entire skill estate into an
    unpopulated gitlink and silently removes 133 skills from the repository

Run from anywhere; paths resolve against the repository root.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

# The skill estate is the reason this repository exists. If this count drifts,
# something structural ate the skills — which is exactly what a stray nested
# .git does, quietly and without any validator noticing.
EXPECTED_SKILL_COUNT = 133

MAX_FILE_BYTES = 1_000_000

errors = []


def git(*args):
    """Run a git plumbing command from ROOT; return stdout lines."""
    out = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if out.returncode != 0:
        return None
    return [ln for ln in out.stdout.splitlines() if ln.strip()]


entries = git("ls-files", "-s")
if entries is None:
    print("SKIP: not a git checkout; structural guards need git metadata.")
    sys.exit(0)

# --- 1. No gitlinks -----------------------------------------------------------
# Mode 160000 means git recorded a commit pointer, not the directory contents.
for line in entries:
    meta = line.split("\t")[0].split()
    if meta and meta[0] == "160000":
        path = line.split("\t", 1)[1] if "\t" in line else line
        errors.append(
            f"gitlink (nested repository) tracked at: {path}\n"
            f"    A nested .git makes git record a commit pointer instead of the\n"
            f"    files. Remove the inner .git directory, then re-add the path."
        )

# --- 2. No build artifacts committed -----------------------------------------
tracked = [line.split("\t", 1)[1] for line in entries if "\t" in line]
for path in tracked:
    low = path.lower()
    if low.endswith((".zip", ".tar.gz", ".tgz", ".rar", ".7z")):
        errors.append(
            f"archive committed: {path}\n"
            f"    Build distributables from a tagged commit and attach them to a\n"
            f"    GitHub Release. Do not commit an archive of this tree into it."
        )

# --- 2b. No classified intake workbook committed ------------------------------
# The Actual Condition Input Workbook may carry Confidential, Market-Sensitive,
# or Sovereign-Sensitive content (its own 99_LOOKUPS offers all three). This
# repository has no classification boundary. .gitignore covers the accident;
# this covers `git add -f` and anything that slips past it.
for path in tracked:
    if path.lower().endswith((".xlsx", ".xlsm")):
        errors.append(
            f"spreadsheet committed: {path}\n"
            f"    A filled intake workbook may be Sovereign-Sensitive and this repo\n"
            f"    has no classification boundary. Keep it outside and ingest via\n"
            f"    06-scripts/ingest_actual_condition.py."
        )

# --- 3. No unreviewably large files ------------------------------------------
for path in tracked:
    fp = ROOT / path
    if fp.is_file():
        size = fp.stat().st_size
        if size > MAX_FILE_BYTES:
            errors.append(
                f"file exceeds {MAX_FILE_BYTES:,} bytes: {path} ({size:,})\n"
                f"    Large binaries cannot be reviewed in a diff."
            )

# --- 4. No CR in tracked text -------------------------------------------------
# validate_skills.py compares SKILL.md descriptions against the registry CSV as
# exact strings. One CR on either side breaks that for every skill at once.
# .gitattributes should prevent this; this guard proves it did.
for path in tracked:
    if not path.lower().endswith((".md", ".csv", ".json", ".yaml", ".yml", ".py", ".mmd")):
        continue
    blob = subprocess.run(
        ["git", "show", f":{path}"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if blob.returncode == 0 and b"\r\n" in blob.stdout:
        errors.append(
            f"CRLF stored in index: {path}\n"
            f"    Fix with: git add --renormalize {path}"
        )

# --- 5. Skill estate is intact ------------------------------------------------
skill_files = [p for p in tracked if p.endswith("SKILL.md")]
if len(skill_files) != EXPECTED_SKILL_COUNT:
    errors.append(
        f"tracked SKILL.md count is {len(skill_files)}, expected "
        f"{EXPECTED_SKILL_COUNT}.\n"
        f"    If this change intentionally adds or removes skills, update\n"
        f"    EXPECTED_SKILL_COUNT in this script and the registry together."
    )

print(f"Checked {len(tracked)} tracked files; found {len(skill_files)} skills.")
if errors:
    print(f"FAILED with {len(errors)} issue(s):")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)
print("PASS: no gitlinks, archives, oversized files, CRLF, or missing skills.")
