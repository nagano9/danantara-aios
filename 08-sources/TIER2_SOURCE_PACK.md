# Tier 2 Source Pack Skeleton

This document is the scaffold for the real Danantara policy and delegation layer.
It does not contain the authoritative documents themselves. It defines what must
exist, how it should be indexed, and what each item must answer.

## Why this exists

Every skill in the estate declares Tier 2 authoritative sources, but the source
register currently shows that Tier 2 is empty. Until this layer is populated, the
skills reason from a generic sovereign-fund model rather than the actual
Danantara operating model.

## Minimum contents

The source pack should eventually include the following indexed documents:

| Code | Required document | What it answers |
|---|---|---|
| T2-01 | BPI Danantara Dewan Pengawas charter | Supervisory scope, duties, and limits |
| T2-02 | Badan Pelaksana delegation of authority matrix | What can be decided at each threshold and by whom |
| T2-03 | DIM Investment Committee charter | Forum, quorum, thresholds, and approval path |
| T2-04 | DAM active-ownership and transformation policy | Intervention logic for portfolio entities |
| T2-05 | DDMF development-finance and additionality policy | Catalytic capital, additionality, and public-value thresholds |
| T2-06 | Investment policy statement | Eligible assets, exclusions, horizon, concentration, and liquidity limits |
| T2-07 | Valuation policy and model-approval standard | Permitted valuation methods and model governance |
| T2-08 | Conflict-of-interest and recusal policy | Disclosure, recusal, related-party handling, independence |
| T2-09 | Data classification and approved-AI-environment policy | Data handling, access, model use, and environment constraints |
| T2-10 | Procurement and integrity due-diligence standard | Counterparty screening, sourcing, and vendor controls |
| T2-11 | Whistleblowing and escalation procedure | Reporting routes, escalation thresholds, and protections |
| T2-12 | Entity model map aligned to authenticated instruments | The operative BPI / holding / operating structure |

## Index fields

Every Tier 2 source entry should carry these fields:

- code
- title
- owner
- version
- effective date
- approval body
- document location
- classification
- supersedes
- affected skills
- related backlog items

## Suggested folder structure

```text
08-sources/
  README.md
  TIER2_SOURCE_PACK.md
  TIER2_FILL_PLAYBOOK.md
  TIER2_STATUS.md
  19_IMPLEMENTATION_BACKLOG.md
  tier2/
    INDEX.md
    TIER2_SOURCE_TEMPLATE.md
    01_dewan_pengawas_charter.md
    02_badan_pelaksana_doa.md
    03_dim_ic_charter.md
    04_dam_active_ownership_policy.md
    05_ddmf_additionality_policy.md
    06_investment_policy_statement.md
    07_valuation_policy.md
    08_conflict_of_interest_policy.md
    09_data_classification_policy.md
    10_procurement_integrity_standard.md
    11_whistleblowing_escalation.md
    12_entity_model_map.md
```

## Rules for promotion into the register

- The document must be authenticated and date-stamped.
- The owner must be named.
- The effective date must be explicit.
- If the document has been amended, cite the amended form.
- If the document cannot be retrieved by an independent reviewer, it does not
  qualify for promotion.

## Immediate next move

Populate the Tier 2 folder in the order that blocks the most decisions:

1. delegation of authority matrix
2. investment committee charter
3. investment policy statement
4. conflict-of-interest policy
5. data classification policy
6. entity model map
