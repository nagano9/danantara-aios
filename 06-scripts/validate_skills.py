#!/usr/bin/env python3
from pathlib import Path
import csv, re, sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "04-skills"
REGISTRY = ROOT / "01-registry" / "master_skill_registry.csv"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VALID_RISK = {"low","medium","high","critical"}
REQUIRED_HEADINGS = [
    "# ", "## Objective", "## Use when", "## Do not use when",
    "## Required inputs", "## Authoritative sources", "## Workflow",
    "## Danantara Way decision rules", "## Output contract",
    "## Human approval", "## Escalation", "## Prohibited actions",
    "## Quality checks", "## Audit record"
]

def frontmatter(text):
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    block = text[4:end].splitlines()
    data = {}
    for line in block:
        if line and not line.startswith(" ") and ":" in line:
            k,v = line.split(":",1)
            data[k.strip()] = v.strip().strip('"')
    # simple nested metadata parse
    meta = {}
    in_meta=False
    for line in block:
        if line == "metadata:":
            in_meta=True
            continue
        if in_meta:
            if line.startswith("  ") and ":" in line:
                k,v=line.strip().split(":",1)
                meta[k.strip()]=v.strip().strip('"')
            elif line and not line.startswith(" "):
                in_meta=False
    data["metadata"]=meta
    return data

errors=[]
files=list(SKILLS_ROOT.rglob("SKILL.md"))
if not files:
    errors.append("No SKILL.md files found.")

registry={}
with REGISTRY.open(encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        registry[row["name"]]=row

for path in files:
    text=path.read_text(encoding="utf-8")
    fm=frontmatter(text)
    name=fm.get("name","")
    desc=fm.get("description","")
    risk=fm.get("metadata",{}).get("risk-tier","")
    if not NAME_RE.fullmatch(name) or len(name)>64:
        errors.append(f"{path}: invalid name {name!r}")
    if path.parent.name != name:
        errors.append(f"{path}: directory {path.parent.name!r} does not match name {name!r}")
    if not (1 <= len(desc) <= 1024):
        errors.append(f"{path}: description length {len(desc)}")
    if risk not in VALID_RISK:
        errors.append(f"{path}: invalid risk tier {risk!r}")
    for h in REQUIRED_HEADINGS:
        if h not in text:
            errors.append(f"{path}: missing heading {h}")
    if name not in registry:
        errors.append(f"{path}: missing from registry")
    elif registry[name]["description"] != desc:
        errors.append(f"{path}: description differs from registry")
    if "AI may not" not in text and "It may not" not in text:
        errors.append(f"{path}: human authority boundary not explicit")

for name in registry:
    matches=[p for p in files if p.parent.name==name]
    if len(matches)!=1:
        errors.append(f"Registry skill {name}: found {len(matches)} SKILL.md files")

print(f"Validated {len(files)} skills against {len(registry)} registry entries.")
if errors:
    print(f"FAILED with {len(errors)} issue(s):")
    for e in errors:
        print("-",e)
    sys.exit(1)
print("PASS: schema, name, description, registry, governance sections, and human-boundary checks.")
