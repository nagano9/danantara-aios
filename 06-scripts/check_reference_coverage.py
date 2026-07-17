#!/usr/bin/env python3
"""Track how many skills have real references and real trigger cases.

The 2026-07-16 audit found 133 skills, 133 `references/` directories, and zero
reference files: every directory held the same placeholder README. It also found
133 trigger_cases.yaml files that fed each skill its own name and description
back as the thing that should trigger it — which tests string matching, not
routing.

validate_skills.py cannot see either problem. It checks that sections exist, not
that they contain anything. So both defects passed a green build.

This script is a RATCHET, not a gate. Most skills are still placeholders and
failing on that would block all work. It fails only if coverage goes DOWN — a
deepened skill may not silently revert to a stub. Raise the floors as the estate
is genuinely deepened; never lower them to make a build pass.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "04-skills"

# Raise these as skills are deepened. Lowering one to go green is the exact
# failure this script exists to make visible.
MIN_SKILLS_WITH_REFERENCES = 5
MIN_SKILLS_WITH_REAL_TRIGGERS = 5

PLACEHOLDER_REF_MARKER = "Add only approved, versioned, authoritative references."
PLACEHOLDER_TRIGGER_MARKER = "to support a material Danantara decision."


def has_real_references(skill_dir: Path) -> bool:
    """True if references/ holds anything beyond the placeholder README."""
    refs = skill_dir / "references"
    if not refs.is_dir():
        return False
    for f in refs.iterdir():
        if not f.is_file():
            continue
        if f.name == "README.md":
            if PLACEHOLDER_REF_MARKER in f.read_text(encoding="utf-8"):
                continue  # placeholder; does not count
        return True
    return False


def has_real_triggers(skill_dir: Path) -> bool:
    """True if trigger cases are not the generated name/description echo."""
    tc = skill_dir / "tests" / "trigger_cases.yaml"
    if not tc.is_file():
        return False
    return PLACEHOLDER_TRIGGER_MARKER not in tc.read_text(encoding="utf-8")


skills = sorted(p.parent for p in SKILLS_ROOT.rglob("SKILL.md"))
with_refs = [s for s in skills if has_real_references(s)]
with_triggers = [s for s in skills if has_real_triggers(s)]

total = len(skills)
print(f"Skill estate: {total}")
print(
    f"  with real references   : {len(with_refs):3d} / {total} "
    f"(floor {MIN_SKILLS_WITH_REFERENCES})"
)
for s in with_refs:
    print(f"      + {s.relative_to(SKILLS_ROOT).as_posix()}")
print(
    f"  with real trigger cases: {len(with_triggers):3d} / {total} "
    f"(floor {MIN_SKILLS_WITH_REAL_TRIGGERS})"
)
for s in with_triggers:
    print(f"      + {s.relative_to(SKILLS_ROOT).as_posix()}")

placeholders = total - len(with_refs)
print()
print(
    f"{placeholders} of {total} skills still reason from a generic template with no "
    f"Danantara source attached."
)

errors = []
if len(with_refs) < MIN_SKILLS_WITH_REFERENCES:
    errors.append(
        f"reference coverage regressed: {len(with_refs)} < floor "
        f"{MIN_SKILLS_WITH_REFERENCES}"
    )
if len(with_triggers) < MIN_SKILLS_WITH_REAL_TRIGGERS:
    errors.append(
        f"trigger coverage regressed: {len(with_triggers)} < floor "
        f"{MIN_SKILLS_WITH_REAL_TRIGGERS}"
    )

if errors:
    print("FAILED:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)
print("PASS: coverage at or above floor.")
