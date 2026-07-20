#!/usr/bin/env python3
"""Bootstrap the Tier 2 source-pack working area.

This script creates the source-layer scaffolding that the repo now expects:

- 08-sources/README.md
- 08-sources/19_IMPLEMENTATION_BACKLOG.md
- 08-sources/TIER2_SOURCE_PACK.md
- 08-sources/tier2/
- tier2 index, template, and placeholder files

It is intentionally conservative: it creates missing files but does not
overwrite existing content unless --force is supplied.
"""
from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "08-sources"
TIER2_ROOT = SOURCE_ROOT / "tier2"

TIER2_FILES = [
    {
        "code": "T2-01",
        "filename": "01_dewan_pengawas_charter.md",
        "title": "BPI Danantara Dewan Pengawas Charter",
        "purpose": "Define supervisory scope, duties, limits, cadence, reporting, and escalation.",
        "backlog": ["IB-001", "IB-012"],
    },
    {
        "code": "T2-02",
        "filename": "02_badan_pelaksana_doa.md",
        "title": "Badan Pelaksana Delegation of Authority Matrix",
        "purpose": "Define who can approve what, at which thresholds, with which limits and conditions.",
        "backlog": ["IB-002"],
    },
    {
        "code": "T2-03",
        "filename": "03_dim_ic_charter.md",
        "title": "DIM Investment Committee Charter",
        "purpose": "Define committee scope, quorum, approval thresholds, voting, and escalation.",
        "backlog": ["IB-003"],
    },
    {
        "code": "T2-04",
        "filename": "04_dam_active_ownership_policy.md",
        "title": "DAM Active Ownership and Transformation Policy",
        "purpose": "Define the intervention logic for active ownership, turnaround, value creation, and transformation capital.",
        "backlog": ["IB-004"],
    },
    {
        "code": "T2-05",
        "filename": "05_ddmf_additionality_policy.md",
        "title": "DDMF Development Finance and Additionality Policy",
        "purpose": "Define catalytic capital use, additionality tests, and public-value thresholds.",
        "backlog": ["IB-005"],
    },
    {
        "code": "T2-06",
        "filename": "06_investment_policy_statement.md",
        "title": "Investment Policy Statement",
        "purpose": "Define eligible assets, exclusions, horizon, concentration, liquidity, and risk appetite.",
        "backlog": ["IB-006"],
    },
    {
        "code": "T2-07",
        "filename": "07_valuation_policy.md",
        "title": "Valuation Policy and Model-Approval Standard",
        "purpose": "Define acceptable valuation methods, review standards, and model governance.",
        "backlog": ["IB-007"],
    },
    {
        "code": "T2-08",
        "filename": "08_conflict_of_interest_policy.md",
        "title": "Conflict-of-Interest and Recusal Policy",
        "purpose": "Define disclosure, recusal, related-party handling, and independence rules.",
        "backlog": ["IB-008"],
    },
    {
        "code": "T2-09",
        "filename": "09_data_classification_policy.md",
        "title": "Data Classification and Approved-AI-Environment Policy",
        "purpose": "Define what data can be used where, with which tools, models, and controls.",
        "backlog": ["IB-009"],
    },
    {
        "code": "T2-10",
        "filename": "10_procurement_integrity_standard.md",
        "title": "Procurement and Integrity Due-Diligence Standard",
        "purpose": "Define counterparty screening, sourcing controls, and integrity checks.",
        "backlog": ["IB-010"],
    },
    {
        "code": "T2-11",
        "filename": "11_whistleblowing_escalation.md",
        "title": "Whistleblowing and Escalation Procedure",
        "purpose": "Define reporting routes, escalation thresholds, and protections.",
        "backlog": ["IB-011"],
    },
    {
        "code": "T2-12",
        "filename": "12_entity_model_map.md",
        "title": "Entity Model Map",
        "purpose": "Define the operative BPI, holding, operating, and oversight entity structure aligned to authenticated instruments.",
        "backlog": ["IB-012"],
    },
]


def render_stub(item):
    backlog = "\n".join(f"- {bid}" for bid in item["backlog"])
    return (
        f"# {item['code']} {item['title']}\n\n"
        "## Status\n\n"
        "Placeholder.\n\n"
        "## Purpose\n\n"
        f"{item['purpose']}\n\n"
        "## Required fields before promotion\n\n"
        "- owner\n"
        "- title\n"
        "- version\n"
        "- effective date\n"
        "- approval body\n"
        "- document location\n"
        "- classification\n\n"
        "## Linked backlog items\n\n"
        f"{backlog}\n"
    )


def render_index():
    rows = "\n".join(
        f"| {item['code']} | `{item['filename']}` | {', '.join(item['backlog'])} | placeholder |"
        for item in TIER2_FILES
    )
    return (
        "# Tier 2 Index\n\n"
        "This index tracks the working drafts that will eventually be replaced by\n"
        "authenticated source documents.\n\n"
        "## Documents\n\n"
        "| Code | Draft file | Linked backlog | Status |\n"
        "|---|---|---|---|\n"
        f"{rows}\n\n"
        "## Use\n\n"
        "- keep the working folder auditable\n"
        "- show which blocked decision each document is meant to unlock\n"
        "- make it obvious which items are still placeholders\n"
    )


def render_template():
    return (
        "# Tier 2 Source Template\n\n"
        "Use this template when replacing a placeholder with an authenticated Danantara\n"
        "policy, delegation, charter, standard, or entity map.\n\n"
        "## Identity\n\n"
        "- code:\n"
        "- title:\n"
        "- owner:\n"
        "- version:\n"
        "- effective date:\n"
        "- approval body:\n"
        "- document location:\n"
        "- classification:\n"
        "- supersedes:\n\n"
        "## Purpose\n\n"
        "State what this source governs and which decision it is meant to unlock.\n\n"
        "## Scope\n\n"
        "State the entities, processes, thresholds, or topics covered by the source.\n\n"
        "## Key rules\n\n"
        "- rule 1:\n"
        "- rule 2:\n"
        "- rule 3:\n\n"
        "## Decision impact\n\n"
        "- affected skills:\n"
        "- linked backlog items:\n"
        "- approval path:\n"
        "- residual gaps:\n\n"
        "## Retrieval note\n\n"
        "Record where an independent reviewer can retrieve the same authenticated\n"
        "document.\n"
    )


def render_source_root_readme():
    return (
        "# Source Layer\n\n"
        "This folder groups the source register, the workbook change request, the\n"
        "implementation backlog, and the Tier 2 source-pack working area.\n\n"
        "## What lives here\n\n"
        "- `SOURCE_REGISTER.md` - authoritative source hierarchy and gaps\n"
        "- `WORKBOOK_CHANGE_REQUEST.md` - open workbook change request CR-001\n"
        "- `19_IMPLEMENTATION_BACKLOG.md` - sink for blocked or indeterminate decisions\n"
        "- `TIER2_SOURCE_PACK.md` - index and folder plan for missing Tier 2 sources\n"
        "- `TIER2_FILL_PLAYBOOK.md` - operating playbook for promoting placeholders\n"
        "- `tier2/` - working folder for Tier 2 source documents\n"
        "- `tier2/INDEX.md` - working index for Tier 2 placeholders\n"
        "- `tier2/TIER2_SOURCE_TEMPLATE.md` - standard template for future authenticated sources\n\n"
        "## Helper script\n\n"
        "- `06-scripts/bootstrap_tier2_source_pack.py` can recreate the source-layer\n"
        "  scaffolding if files are removed.\n\n"
        "## Priority\n\n"
        "The source layer is the highest-leverage part of the operating system because it\n"
        "decides whether downstream skills can answer from real Danantara instruments or\n"
        "only from a generic template.\n"
    )


def render_fill_playbook():
    return (
        "# Tier 2 Fill Playbook\n\n"
        "This playbook explains how to turn the Tier 2 source-layer scaffold into a set\n"
        "of authenticated Danantara policy and delegation documents.\n\n"
        "## Purpose\n\n"
        "- fill the most blocking source gaps first\n"
        "- keep each Tier 2 document tied to a real decision\n"
        "- make every document traceable by owner, effective date, and retrieval location\n"
        "- preserve an audit trail from placeholder to authenticated source\n\n"
        "## Fill order\n\n"
        "Follow the order that blocks the most decisions:\n\n"
        "1. Badan Pelaksana delegation of authority matrix\n"
        "2. DIM Investment Committee charter\n"
        "3. Investment policy statement\n"
        "4. Conflict-of-interest and recusal policy\n"
        "5. Data classification and approved-AI-environment policy\n"
        "6. Entity model map\n\n"
        "Then proceed to:\n\n"
        "7. Dewan Pengawas charter\n"
        "8. DAM active-ownership and transformation policy\n"
        "9. DDMF development-finance and additionality policy\n"
        "10. Valuation policy and model-approval standard\n"
        "11. Procurement and integrity due-diligence standard\n"
        "12. Whistleblowing and escalation procedure\n\n"
        "## Minimum evidence for promotion\n\n"
        "Before a placeholder can be promoted, the source must have:\n\n"
        "- owner\n"
        "- title\n"
        "- version\n"
        "- effective date\n"
        "- approval body\n"
        "- document location\n"
        "- classification\n"
        "- retrieval path that an independent reviewer can follow\n\n"
        "If a document is amended, cite the amended instrument, not the older draft.\n\n"
        "## Promotion workflow\n\n"
        "1. Collect the authenticated document.\n"
        "2. Record the metadata in the Tier 2 template.\n"
        "3. Link the document to the backlog items it unlocks.\n"
        "4. Remove or retire the placeholder entry.\n"
        "5. Update the index and the source register.\n"
        "6. Re-run the Tier 2 scaffold validator.\n\n"
        "## Crosswalk to backlog\n\n"
        "| Tier 2 item | Backlog item(s) |\n"
        "|---|---|\n"
        "| `02_badan_pelaksana_doa.md` | IB-002 |\n"
        "| `03_dim_ic_charter.md` | IB-003 |\n"
        "| `06_investment_policy_statement.md` | IB-006 |\n"
        "| `08_conflict_of_interest_policy.md` | IB-008 |\n"
        "| `09_data_classification_policy.md` | IB-009 |\n"
        "| `12_entity_model_map.md` | IB-012 |\n\n"
        "## Quality checks\n\n"
        "- every promoted document must be independently retrievable\n"
        "- no placeholder may be treated as a source\n"
        "- the source register must stay aligned with the working folder\n"
        "- the backlog must show which decisions the source unlocks\n"
    )


def render_backlog():
    lines = []
    for item in TIER2_FILES:
        lines.append(
            "| {code} | {gap} | {action} | {blocker} | {owner} | {priority} | {wave} | open | {notes} |".format(
                code=item["code"],
                gap={
                    "T2-01": "BPI Danantara Dewan Pengawas charter",
                    "T2-02": "Badan Pelaksana delegation of authority matrix",
                    "T2-03": "DIM Investment Committee charter and quorum rules",
                    "T2-04": "DAM active-ownership and transformation policy",
                    "T2-05": "DDMF development-finance and additionality policy",
                    "T2-06": "Investment policy statement and risk limits",
                    "T2-07": "Valuation policy and model-approval standard",
                    "T2-08": "Conflict-of-interest, related-party, and recusal policy",
                    "T2-09": "Data classification standard and approved-AI-environment policy",
                    "T2-10": "Procurement and integrity due-diligence standard",
                    "T2-11": "Whistleblowing and escalation procedure",
                    "T2-12": "Operative entity model aligned to authenticated PP 19/2026",
                }[item["code"]],
                action={
                    "T2-01": "Retrieve and pin the authenticated charter with effective date",
                    "T2-02": "Retrieve and pin the operative DOA with clause references",
                    "T2-03": "Retrieve and pin the committee charter and threshold matrix",
                    "T2-04": "Retrieve and pin the policy that governs active ownership interventions",
                    "T2-05": "Retrieve and pin the policy that defines additionality and catalytic capital use",
                    "T2-06": "Retrieve and pin mandate limits, concentration, liquidity, and exclusions",
                    "T2-07": "Retrieve and pin the valuation policy, model approval, and review rules",
                    "T2-08": "Retrieve and pin the COI and recusal framework",
                    "T2-09": "Retrieve and pin the data use and environment rules",
                    "T2-10": "Retrieve and pin procurement and due-diligence controls",
                    "T2-11": "Retrieve and pin the escalation route and protections",
                    "T2-12": "Confirm the current holding and operating-entity structure",
                }[item["code"]],
                blocker={
                    "T2-01": "Who supervises what, and with which limits?",
                    "T2-02": "May DIM, DAM, or DDMF act alone on a given threshold?",
                    "T2-03": "Which forum approves which DIM action?",
                    "T2-04": "What intervention path is allowed before ownership action?",
                    "T2-05": "When is intervention additional rather than duplicative?",
                    "T2-06": "Is the opportunity inside the investable universe?",
                    "T2-07": "Which valuation methods are acceptable and who validates them?",
                    "T2-08": "Who must recuse, disclose, or escalate?",
                    "T2-09": "Which data can be processed where, and by whom?",
                    "T2-10": "What sourcing and counterparty checks are mandatory?",
                    "T2-11": "Where do exceptions, leaks, and misconduct go?",
                    "T2-12": "What is the actual entity architecture after amendment?",
                }[item["code"]],
                owner={
                    "T2-01": "Governance owner",
                    "T2-02": "Legal/governance owner",
                    "T2-03": "DIM committee owner",
                    "T2-04": "DAM portfolio owner",
                    "T2-05": "DDMF investment owner",
                    "T2-06": "Portfolio/risk owner",
                    "T2-07": "Finance/model owner",
                    "T2-08": "Compliance owner",
                    "T2-09": "Security/data owner",
                    "T2-10": "Procurement/compliance owner",
                    "T2-11": "Governance/risk owner",
                    "T2-12": "Legal/governance owner",
                }[item["code"]],
                priority=1 if item["code"] in {"T2-01", "T2-02", "T2-03", "T2-06", "T2-08", "T2-09", "T2-12"} else 2,
                wave="Wave 1" if item["code"] in {"T2-01", "T2-02", "T2-03", "T2-04", "T2-05", "T2-06", "T2-08", "T2-09", "T2-12"} else "Wave 2",
                notes={
                    "T2-01": "Required for governance boundary clarity",
                    "T2-02": "Required by mandate and decision-rights skills",
                    "T2-03": "Required by committee memo and approval routing",
                    "T2-04": "Needed for value creation and turnaround work",
                    "T2-05": "Needed for catalytic and blended finance decisions",
                    "T2-06": "Needed for portfolio, return, and risk skills",
                    "T2-07": "Needed for valuation and model challenge skills",
                    "T2-08": "Needed for integrity and independence checks",
                    "T2-09": "Needed before most orchestration workflows can proceed",
                    "T2-10": "Needed for commercial and integrity workflows",
                    "T2-11": "Needed for exception routing and assurance",
                    "T2-12": "Must be resolved before hard-coding entity assumptions",
                }[item["code"]],
            )
        )
    rows = "\n".join(lines)
    return (
        "# 19_IMPLEMENTATION_BACKLOG\n\n"
        "This ledger receives every `indeterminate`, `void`, `stop`, or blocked decision\n"
        "cell that the estate surfaces during real use. It is a work tracker, not a\n"
        "source of authority.\n\n"
        "## Purpose\n\n"
        "- capture the missing cell, its owner, and the question it would answer\n"
        "- rank by blocking pressure, not by workshop opinion\n"
        "- keep work items tied to actual decision failures or missing evidence\n"
        "- provide the sink for Arc 3 of `post-decision-learning`\n\n"
        "## Columns\n\n"
        "| Column | Meaning |\n"
        "|---|---|\n"
        "| `ID` | Stable backlog item identifier |\n"
        "| `Source Gap / Evidence` | The missing document, clause, dataset, or control |\n"
        "| `Initiative / Action` | The concrete action needed to close the gap |\n"
        "| `Blocker / Decision Needed` | The question that cannot be answered yet |\n"
        "| `Accountable Owner` | Named owner of the missing cell |\n"
        "| `Priority` | Relative blocking pressure, not personal urgency |\n"
        "| `Target Wave` | When the item should be addressed |\n"
        "| `Status` | `open`, `in_progress`, `blocked`, or `closed` |\n"
        "| `Notes` | Anything that helps the owner close the item |\n\n"
        "## Seed backlog\n\n"
        "| ID | Source Gap / Evidence | Initiative / Action | Blocker / Decision Needed | Accountable Owner | Priority | Target Wave | Status | Notes |\n"
        "|---|---|---|---|---|---|---|---|---|\n"
        f"{rows}\n\n"
        "## Operating rules\n\n"
        "- Every indeterminate verdict should create or update exactly one backlog item.\n"
        "- A backlog item without an owner is not ready to act on.\n"
        "- Priority is measured by how many decisions the gap blocks.\n"
        "- When the source is real, move it out of backlog and into the source register.\n"
    )


def render_tier2_source_pack():
    return (
        "# Tier 2 Source Pack Skeleton\n\n"
        "This document is the scaffold for the real Danantara policy and delegation layer.\n"
        "It does not contain the authoritative documents themselves. It defines what must\n"
        "exist, how it should be indexed, and what each item must answer.\n\n"
        "## Why this exists\n\n"
        "Every skill in the estate declares Tier 2 authoritative sources, but the source\n"
        "register currently shows that Tier 2 is empty. Until this layer is populated, the\n"
        "skills reason from a generic sovereign-fund model rather than the actual\n"
        "Danantara operating model.\n\n"
        "## Minimum contents\n\n"
        "The source pack should eventually include the following indexed documents:\n\n"
        "| Code | Required document | What it answers |\n"
        "|---|---|---|\n"
        "| T2-01 | BPI Danantara Dewan Pengawas charter | Supervisory scope, duties, and limits |\n"
        "| T2-02 | Badan Pelaksana delegation of authority matrix | What can be decided at each threshold and by whom |\n"
        "| T2-03 | DIM Investment Committee charter | Forum, quorum, thresholds, and approval path |\n"
        "| T2-04 | DAM active-ownership and transformation policy | Intervention logic for portfolio entities |\n"
        "| T2-05 | DDMF development-finance and additionality policy | Catalytic capital, additionality, and public-value thresholds |\n"
        "| T2-06 | Investment policy statement | Eligible assets, exclusions, horizon, concentration, and liquidity limits |\n"
        "| T2-07 | Valuation policy and model-approval standard | Permitted valuation methods and model governance |\n"
        "| T2-08 | Conflict-of-interest and recusal policy | Disclosure, recusal, related-party handling, independence |\n"
        "| T2-09 | Data classification and approved-AI-environment policy | Data handling, access, model use, and environment constraints |\n"
        "| T2-10 | Procurement and integrity due-diligence standard | Counterparty screening, sourcing, and vendor controls |\n"
        "| T2-11 | Whistleblowing and escalation procedure | Reporting routes, escalation thresholds, and protections |\n"
        "| T2-12 | Entity model map aligned to authenticated instruments | The operative BPI / holding / operating structure |\n\n"
        "## Index fields\n\n"
        "Every Tier 2 source entry should carry these fields:\n\n"
        "- code\n"
        "- title\n"
        "- owner\n"
        "- version\n"
        "- effective date\n"
        "- approval body\n"
        "- document location\n"
        "- classification\n"
        "- supersedes\n"
        "- affected skills\n"
        "- related backlog items\n\n"
        "## Suggested folder structure\n\n"
        "```text\n"
        "08-sources/\n"
        "  README.md\n"
        "  TIER2_SOURCE_PACK.md\n"
        "  19_IMPLEMENTATION_BACKLOG.md\n"
        "  tier2/\n"
        "    INDEX.md\n"
        "    TIER2_SOURCE_TEMPLATE.md\n"
        "    01_dewan_pengawas_charter.md\n"
        "    02_badan_pelaksana_doa.md\n"
        "    03_dim_ic_charter.md\n"
        "    04_dam_active_ownership_policy.md\n"
        "    05_ddmf_additionality_policy.md\n"
        "    06_investment_policy_statement.md\n"
        "    07_valuation_policy.md\n"
        "    08_conflict_of_interest_policy.md\n"
        "    09_data_classification_policy.md\n"
        "    10_procurement_integrity_standard.md\n"
        "    11_whistleblowing_escalation.md\n"
        "    12_entity_model_map.md\n"
        "```\n\n"
        "## Rules for promotion into the register\n\n"
        "- The document must be authenticated and date-stamped.\n"
        "- The owner must be named.\n"
        "- The effective date must be explicit.\n"
        "- If the document has been amended, cite the amended form.\n"
        "- If the document cannot be retrieved by an independent reviewer, it does not\n"
        "  qualify for promotion.\n\n"
        "## Immediate next move\n\n"
        "Populate the Tier 2 folder in the order that blocks the most decisions:\n\n"
        "1. delegation of authority matrix\n"
        "2. investment committee charter\n"
        "3. investment policy statement\n"
        "4. conflict-of-interest policy\n"
        "5. data classification policy\n"
        "6. entity model map\n"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="overwrite existing files")
    args = ap.parse_args()

    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    TIER2_ROOT.mkdir(parents=True, exist_ok=True)

    files = {
        SOURCE_ROOT / "README.md": render_source_root_readme(),
        SOURCE_ROOT / "19_IMPLEMENTATION_BACKLOG.md": render_backlog(),
        SOURCE_ROOT / "TIER2_SOURCE_PACK.md": render_tier2_source_pack(),
        SOURCE_ROOT / "TIER2_FILL_PLAYBOOK.md": render_fill_playbook(),
        TIER2_ROOT / "README.md": (
            "# Tier 2 Working Folder\n\n"
            "This folder is the working area for authenticated Danantara policy,\n"
            "delegation, charter, and standard documents.\n\n"
            "## Status\n\n"
            "Placeholder only. These files are not authoritative until they are replaced\n"
            "with authenticated source content that includes owner, version, effective\n"
            "date, and retrieval location.\n\n"
            "## File map\n\n"
            "- `INDEX.md`\n"
            "- `TIER2_SOURCE_TEMPLATE.md`\n"
            "- `01_dewan_pengawas_charter.md`\n"
            "- `02_badan_pelaksana_doa.md`\n"
            "- `03_dim_ic_charter.md`\n"
            "- `04_dam_active_ownership_policy.md`\n"
            "- `05_ddmf_additionality_policy.md`\n"
            "- `06_investment_policy_statement.md`\n"
            "- `07_valuation_policy.md`\n"
            "- `08_conflict_of_interest_policy.md`\n"
            "- `09_data_classification_policy.md`\n"
            "- `10_procurement_integrity_standard.md`\n"
            "- `11_whistleblowing_escalation.md`\n"
            "- `12_entity_model_map.md`\n"
        ),
        TIER2_ROOT / "INDEX.md": render_index(),
        TIER2_ROOT / "TIER2_SOURCE_TEMPLATE.md": render_template(),
    }
    for item in TIER2_FILES:
        files[TIER2_ROOT / item["filename"]] = render_stub(item)

    kept = 0
    created = 0
    updated = 0
    for path, content in files.items():
        existed = path.exists()
        if existed and not args.force:
            kept += 1
            continue
        path.write_text(content, encoding="utf-8")
        if existed:
            updated += 1
        else:
            created += 1

    print(f"Bootstrap complete for {TIER2_ROOT}")
    print(f"  created         : {created}")
    print(f"  updated         : {updated}")
    print(f"  kept existing   : {kept}")
    print("  note: existing source-layer files are not overwritten unless --force is used")


if __name__ == "__main__":
    main()
