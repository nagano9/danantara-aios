#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
targets = list((ROOT/"04-skills").rglob("*.md")) + list((ROOT/"00-blueprint").rglob("*.md"))

restricted = {
    "proyek titipan": "Use formal mandate, strategic-national-interest, and evidence-based rationale.",
    "penyelamatan tanpa syarat": "Use conditional capital, turnaround milestones, accountability, and exit criteria.",
    "evergreen support": "Require time-bound conditionality and exit criteria.",
    "sunk-cost justification": "Use forward-looking viability and opportunity-cost analysis.",
}
warnings=[]
for p in targets:
    text=p.read_text(encoding="utf-8").lower()
    for phrase,guidance in restricted.items():
        for m in re.finditer(re.escape(phrase), text):
            # Allowed in explicit prohibited/avoid context
            context=text[max(0,m.start()-80):m.end()+80]
            if not any(k in context for k in ["avoid","prohibit","do not","tanpa","restricted","must not","larang"]):
                warnings.append(f"{p}: restricted phrase '{phrase}'. {guidance}")

print(f"Scanned {len(targets)} markdown files.")
if warnings:
    print(f"WARNINGS: {len(warnings)}")
    print("\n".join("- "+w for w in warnings))
    sys.exit(2)
print("PASS: no unrestricted disallowed vocabulary detected.")
