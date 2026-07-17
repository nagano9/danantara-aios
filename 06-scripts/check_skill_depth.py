#!/usr/bin/env python3
"""Enforce the mechanically checkable subset of the Elite Skill Standard.

See 03-templates/ELITE_SKILL_STANDARD.md. The 2026-07-16 audit measured:

    133 skills -> 17 distinct workflows
    7 / 133 skills had a workflow of their own
    21 skills shared a single workflow
    106 / 133 had `## Objective` copied verbatim from `description`

All of it passed validate_skills.py, which checks that sections exist rather
than that they contain anything. This script checks the part of "contains
something" that a machine can actually judge.

WHAT THIS CANNOT DO: it cannot tell whether a test is discriminating, whether a
threshold is defensible, or whether a method is correct. Those need a domain
reviewer. This catches regression; it does not confer quality. A green run here
is not evidence the skills are good — reading it that way is the exact mistake
that produced 17 workflows for 133 skills.

RATCHET, not a gate: most skills are still generated templates and failing on
that would block all work. Raise the floors as skills are genuinely deepened.
Never lower one to make a build pass.
"""
from pathlib import Path
import hashlib
import re
import sys
import collections

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "04-skills"

# Raise as skills are deepened. Lowering one to go green is the failure this
# script exists to make visible.
MIN_SKILLS_WITH_OWN_WORKFLOW = 9
MIN_SKILLS_WITH_VERDICT_VOCAB = 5
MIN_SKILLS_WITH_FAILURE_MODES = 5

# A skill declares a verdict vocabulary by naming mutually exclusive outcomes,
# one of which declines to answer or halts. Two detection routes, because the
# first version of this check assumed every vocabulary looks like
# `indeterminate` and therefore missed danantara-master-orchestrator, whose
# verdicts are dispatch / stop / escalate before proceeding. The heuristic
# encoded one skill's idiom as if it were the general rule.
#
#   1. an explicit `## Verdicts` section — the unambiguous signal;
#   2. a declining verdict named in prose — for skills that state it inline.
#
# Templates contain neither.
VERDICT_SECTION = "Verdicts"
VERDICT_MARKERS = (
    "indeterminate",
    "not fit",
    "outside mandate",
    "escalate before proceeding",
)

FAILURE_MODE_MARKERS = ("failure mode", "how this skill gets fooled", "gets fooled")


def section(text: str, heading: str) -> str:
    m = re.search(rf"^## {re.escape(heading)}\n(.+?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""


def frontmatter_field(text: str, key: str) -> str:
    m = re.search(rf"^{key}: (.+)$", text, re.M)
    return m.group(1).strip() if m else ""


skills = sorted(SKILLS_ROOT.rglob("SKILL.md"))
if not skills:
    print("No SKILL.md found.")
    sys.exit(1)

workflow_owners = collections.defaultdict(list)
objective_copies = []
with_verdict = []
with_failure_modes = []

for path in skills:
    name = path.parent.name
    text = path.read_text(encoding="utf-8")

    wf = section(text, "Workflow")
    if wf:
        key = hashlib.md5(wf.encode()).hexdigest()
        workflow_owners[key].append(name)

    desc = frontmatter_field(text, "description")
    obj = section(text, "Objective")
    if desc and obj and obj.strip() == desc.strip():
        objective_copies.append(name)

    low = text.lower()
    if section(text, VERDICT_SECTION) or any(m in low for m in VERDICT_MARKERS):
        with_verdict.append(name)
    if any(m in low for m in FAILURE_MODE_MARKERS):
        with_failure_modes.append(name)

total = len(skills)
own_workflow = [ns[0] for ns in workflow_owners.values() if len(ns) == 1]
shared = {k: v for k, v in workflow_owners.items() if len(v) > 1}

print(f"Skill estate: {total}")
print(f"  distinct workflows          : {len(workflow_owners)}")
print(
    f"  with a workflow of their own: {len(own_workflow):3d} / {total} "
    f"(floor {MIN_SKILLS_WITH_OWN_WORKFLOW})"
)
print(
    f"  with a verdict vocabulary   : {len(with_verdict):3d} / {total} "
    f"(floor {MIN_SKILLS_WITH_VERDICT_VOCAB})"
)
print(
    f"  with named failure modes    : {len(with_failure_modes):3d} / {total} "
    f"(floor {MIN_SKILLS_WITH_FAILURE_MODES})"
)
print(f"  Objective copied from description: {len(objective_copies)} / {total}")

if shared:
    print()
    print("  Largest shared workflows (Elite Skill Standard §6: if two skills can")
    print("  share a workflow, one of them does not exist):")
    for key, names in sorted(shared.items(), key=lambda kv: -len(kv[1]))[:5]:
        print(f"    {len(names):3d} skills — e.g. {', '.join(sorted(names)[:3])}")

errors = []
if len(own_workflow) < MIN_SKILLS_WITH_OWN_WORKFLOW:
    errors.append(
        f"workflow uniqueness regressed: {len(own_workflow)} < floor "
        f"{MIN_SKILLS_WITH_OWN_WORKFLOW}. A skill lost its own method, or gained "
        f"a twin."
    )
if len(with_verdict) < MIN_SKILLS_WITH_VERDICT_VOCAB:
    errors.append(
        f"verdict vocabulary regressed: {len(with_verdict)} < floor "
        f"{MIN_SKILLS_WITH_VERDICT_VOCAB}"
    )
if len(with_failure_modes) < MIN_SKILLS_WITH_FAILURE_MODES:
    errors.append(
        f"failure-mode coverage regressed: {len(with_failure_modes)} < floor "
        f"{MIN_SKILLS_WITH_FAILURE_MODES}"
    )

print()
if errors:
    print("FAILED:")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)
print("PASS: depth metrics at or above floor.")
print("NOTE: this measures regression, not quality. It cannot judge whether a")
print("      test discriminates or a method is correct. That needs a reviewer.")
