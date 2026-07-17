---
name: human-approval-orchestrator
description: Maps risk-tiered outputs to required reviewers, approvers, recusals, quorum, conditions, and evidence of approval. Use whenever AI analysis may influence capital, governance, legal, personnel, disclosure, or strategic decisions.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: BPI/DAM/DIM/DDMF
  cluster: 02-orchestration
  risk-tier: critical
  version: "1.1.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# Human Approval Orchestrator

## Objective
Answer two questions and refuse to blur them: **who must approve this and are they
permitted to**, and **is the approval being claimed actually valid**.

The second is the one that matters and the one usually skipped. **An invalid
approval is worse than a missing one.** A missing approval blocks the decision and
everyone knows it. An invalid approval carries a name, a date, a forum, and an
audit trail — and is void. It survives until the auditor arrives, which under
UU 16/2025 is **BPK**, by statute.

This skill never obtains, records, or infers approval. Full method:
`references/approval-validity-protocol.md`.

## Use when
- Any material output is about to reach a decision-maker — this skill is on 9 of
  the 10 reference workflows because every chain ends at a human.
- An approval is **asserted** rather than evidenced ("the IC already approved it").
- The approver's eligibility, the forum's authority, or the quorum is unverified.
- A decision sits near a threshold, or the applicable charter predates
  6 Oct 2025 (UU 16/2025).
- `Risk Bearer` is unnamed on a material decision.

## Do not use when
- The question is whether Danantara may act at all — that is
  `investment-mandate-interpreter` or `mandate-authority-interpreter`. **Never
  route an out-of-mandate action to an approver; no approver can cure it.**
- The question is whether the analysis is good enough to decide on — that is
  `decision-quality-gate`, which runs *before* this skill.
- No human decision is implicated.

Do not use this skill to bypass a competent authority, replace licensed or
accountable professional judgment, process unauthorized information, or make an
institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
- **The decision, its materiality, and its size** — the threshold test needs a
  number, not "significant".
- **The claimed approver and forum**, if any is asserted.
- **Any evidence of approval already given**, and the system that produced it.
- **The proposer** — required to test separation of duties.

Missing inputs are a result, not a blocker. Name what is missing and what it
decides.

## Dependencies
- `decision-rights-checker` — supplies who proposes/reviews/approves; this skill
  tests whether that routing is *valid*.
- `conflict-of-interest-gate` — supplies recusal findings.
- `decision-quality-gate` — must pass before routing.
- `audit-trail-packager` — receives the routing record.

## Authoritative sources
1. **Law, regulation, official decision, formal mandate.** UU 1/2025 jo.
   UU 16/2025 (Pasal 3E delegation; concurrent-position prohibition; separation of
   supervisory and operational functions; BPK examination); PP 10/2025 jo.
   PP 19/2026 (organ: Dewan Pengawas + Badan Pelaksana). See
   `08-sources/SOURCE_REGISTER.md` Tier 1.
2. **Danantara delegations and charters** — the *Actual Condition Input Workbook*,
   ingested via `06-scripts/ingest_actual_condition.py`:

   | Question | Cell |
   |---|---|
   | Who approves at this size? | `05_DECISION_RIGHTS_DOA` → `DOA-xx` · `Financial / Risk Threshold` + `Approver` |
   | Who proposed it? | `DOA-xx` · `Proposer` |
   | Who bears the risk? | `DOA-xx` · `Risk Bearer` — **may not be empty for a material decision** (sheet 05's own rule) |
   | Which forum, what quorum? | `DOA-xx` · `Decision Forum` → `06_COMMITTEE_CHARTERS` → `COM-xx` · `Quorum` |
   | Forum's authority ceiling | `COM-xx` · `Approval Authority` + `Thresholds` |
   | Is the delegation current? | `DOA-xx` · `Effective Date` — after 6 Oct 2025? |
   | Named human approver | `15_SKILL_RACI` · `Human Approver` |

   **A cell is a source only with `DoA / Legal Document` + `Clause / Page` +
   `Effective Date`.** Otherwise it is a claim about a delegation; the ingest
   marks it `UNSOURCED` and it must be treated as absent.

   **Status 2026-07-16: every DOA/COM row is empty.** Most routing questions
   therefore resolve to `indeterminate`.
3. Audited or owner-certified records of the approval itself — minutes, resolutions,
   system records with identifiable actor and timestamp.
4. Independent external evidence.
5. Prior decisions as context only. **A precedent that a similar decision was
   approved at this level is not a delegation** — it may be a repeated breach.

Record source owner, title, version, effective date, retrieval date,
classification, and exact location. Resolve discrepancies through
`source-hierarchy-resolver`.

## Workflow
Apply in order. **A failure at any step voids everything downstream.** A validly
constituted forum cannot cure an ineligible approver; a quorum cannot cure a
self-approval.

1. **Establish materiality and size.** Without a number, the threshold test cannot
   run. "Significant" is not a size.
2. **Test that authority exists and is sourced.** Does a `DOA-xx` row reach this
   decision at this size, with `Clause / Page` and `Effective Date`? No, or
   unsourced → **`indeterminate`**; name the cell, its owner, and the question.
3. **Test approver eligibility.** Barred by the concurrent-position prohibition
   (UU 16/2025)? Validly in office? Conflicted without recusal? Any failure →
   **`void`**. An ineligible approver produces *no* approval, not a weak one.
4. **Test separation of duties.** `Proposer` == `Approver` → self-approval →
   **`void`**. `Risk Bearer` empty on a material decision → **`void`** (sheet 05's
   own rule). **Name the organ, not just the person**: two individuals under one
   accountable organ is one organ approving itself.
5. **Test the forum.** Quorum defined and met? Decision within the forum's
   `Approval Authority` ceiling? Above it → escalate per `Escalation Path`.
6. **Test currency.** Charter or DoA effective before 6 Oct 2025 → presumptively
   stale, because UU 16/2025 separated supervisory and operational functions.
   Flag; do not assume it survived.
7. **Test evidence of approval.** Evidenced by an authorized system, or merely
   asserted? Assertion → **`void`**, and do not record.
8. **Issue the verdict** and, where `indeterminate`, state what can still be said.

## Failure modes
The middle column is load-bearing: this skill fails under *pressure*, not from
ignorance.

| Failure | The pressure that causes it | Correct behaviour |
|---|---|---|
| **Routing to a plausible approver** | The DoA is empty, the deadline is real, and someone senior is obviously "the right person" | `indeterminate`. Name `DOA-xx`. A plausible approver is an unauthorised one wearing seniority. |
| **Treating an unsourced cell as a delegation** | The cell is filled, so it looks like evidence | No clause + date → a claim. Treat as absent. |
| **Accepting an ineligible approver "for now"** | The forum met, the decision is made, re-running it is expensive | The approval is **void**, not weak. Sunk process cost is not a cure. |
| **Missing organ-level self-approval** | Two different individual names appear, so it looks separated | Name the organ. Two names under one organ is one organ approving itself. |
| **Recording approval from a claim** | Everyone in the room knows it was approved | Report only what an authorized system evidences. Never record. |
| **Treating non-objection as approval** | Circulation closed and nobody objected | Approval is a positive act unless the charter says otherwise, on its terms. |
| **Using a pre-Oct-2025 charter** | It is the charter on file and looks authoritative | UU 16/2025 separated supervisory and operational functions. Presumptively stale. |
| **Treating precedent as delegation** | "We approved the last one at this level" | That may be a repeated breach, not an authority. |

## Falsification hooks
State up front what would change the verdict.

- *"`indeterminate` becomes `routable` when `DOA-04` supplies a threshold at or
  above this size with `Clause / Page` and an `Effective Date` after 6 Oct 2025,
  `Risk Bearer` is named, and the approver clears the concurrent-position test."*
- *"`routable` becomes `void` if the approver is found to hold a barred concurrent
  position, or if `Proposer` and `Approver` resolve to the same organ."*
- *"Any verdict is void if the evidence of approval turns out to be an assertion
  rather than an authorized system record."*

## Danantara Way decision rules
- **An invalid approval is worse than a missing one.** It manufactures the
  appearance of governance around a decision nobody validly made.
- Eligibility failures **void**; they do not weaken. There is no "note it and
  proceed".
- Approval is a **positive act**, evidenced by an authorized system. Silence,
  seniority, urgency, and precedent are not approval.
- **Name the organ.** Separation of duties is an organ-level property.
- `Risk Bearer` must be named before a material decision reaches a forum. An
  unowned downside is an unowned decision.
- Identify mandate, decision rights, accountable owner, risk owner, conflicts,
  recusals, and required approvals.
- Preserve strategic confidentiality through classification and least-privilege
  access while maintaining an audit trail.
- State assumptions, confidence, data gaps, dissent, and unresolved tensions
  explicitly.

## Output contract
Primary output: **a routing determination** —

- **verdict**: `routable` / `routable with conditions` / `indeterminate pending
  named cell` / **`void`**;
- the approver, forum, and quorum, each with its `DOA-xx` / `COM-xx` citation,
  clause, and effective date;
- the separation-of-duties result, **at organ level**;
- the eligibility result against the concurrent-position prohibition;
- for `indeterminate`: the exact cell, its owner, the question it answers, **and
  what can still be said without it**;
- for `void`: what is void, why, and what would have to happen for a valid
  approval to exist.

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result
as AI-assisted analysis or draft until the required human authority has approved
it.

## Human approval
Authorized approver. The skill may analyze, challenge, draft, calculate, and
recommend. It may not execute, bind, disclose, waive, appoint, dismiss, allocate
capital, or record final approval unless a separate authorized system provides
verified evidence of that human action.

**This is the skill where that boundary is enforced for the whole estate.** It may
not record approval, infer it from silence or seniority, or treat its own routing
determination as an approval. Identifying the correct approver is not approval.

## Escalation
Stop and escalate when authority is missing, evidence is materially inadequate,
conflicts are unresolved, legal basis is doubtful, downside cannot be bounded,
data use is unauthorized, material sources conflict, an exception is requested, or
the recommendation depends on an unapproved subsidy or informal direction.

Specific to this skill — escalate when:
- no sourced `DOA-xx` reaches the decision (**the common case today**);
- the approver is or may be ineligible;
- `Proposer` and `Approver` resolve to one organ;
- `Risk Bearer` is unnamed on a material decision;
- approval is asserted but not evidenced;
- the forum's ceiling is exceeded;
- an approval is requested to be recorded, backdated, or implied.

## Prohibited actions
- **Do not make, imply, fabricate, or backdate institutional approval.** This is
  the package's worst failure: it manufactures the appearance of governance and
  leaves an audit trail suggesting challenge occurred.
- **Do not route to an approver not named in a sourced instrument**, however
  senior, obvious, or willing.
- **Do not treat non-objection, silence, seniority, or precedent as approval.**
- Do not bypass formal decision rights, required human review, recusal, legal,
  risk, compliance, or information-security controls.
- Do not invent facts, sources, policy, authority, financial results, valuation
  inputs, or certainty.
- Do not disclose or process information outside its authorized classification,
  purpose, users, tools, systems, or jurisdiction.
- Do not describe unsupported political direction, informal instruction, or
  strategic labeling as sufficient investment rationale.
- Do not collapse commercial return and national impact into an opaque single
  score.

## Quality checks
- Name, description, and output comply with the skill schema and canonical output
  contract.
- Every approver, forum, and quorum carries a `DOA-xx`/`COM-xx` citation with
  clause and effective date — or the verdict is `indeterminate`.
- Separation of duties was tested at **organ** level, not just by name.
- Eligibility was tested against the concurrent-position prohibition.
- `Risk Bearer` is named, or the decision is held.
- No approval is recorded that an authorized system did not evidence.
- Material claims have traceable sources and clear fact/assumption/inference
  labels.
- Relevant Danantara Way principles and core tensions were explicitly tested.
- Risk owner, decision owner, approvals, conditions, and escalation path are
  identified.
- An independent reviewer could reproduce the reasoning and understand dissent and
  limitations.

## Audit record
Capture request, user and role, purpose, entity, risk tier, data classification,
sources, versions, tool calls, calculations, assumptions, analyses, challenge,
dissent, approvals, conditions, final human decision, execution status, monitoring
results, and post-decision learning.

Specific to this skill: record the **verdict and its basis**, every `DOA-xx` /
`COM-xx` cell relied on with clause and effective date, the organ-level separation
result, the eligibility result, and **any pressure applied to route around an
`indeterminate` or `void` verdict**. Under UU 16/2025 BUMN financial examination
sits with **BPK** — this record has a statutory external reader.
