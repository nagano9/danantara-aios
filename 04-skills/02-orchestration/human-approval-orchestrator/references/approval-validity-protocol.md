# Approval validity protocol

Method reference for `human-approval-orchestrator`. Used by 9 of the 10 reference
workflows — the most reused skill in the estate — because every chain ends at a
human decision.

**Premise.** This skill does not obtain approval. It answers two questions and
refuses to blur them:

1. **Who must approve this, and are they permitted to?**
2. **Is the approval being claimed actually valid?**

The second question is the one that matters and the one usually skipped. **An
invalid approval is worse than a missing one.** A missing approval blocks the
decision and everybody knows it. An invalid approval *looks* like authority: it
carries a name, a date, a forum, and an audit trail — and it is void. It will
survive until the auditor arrives, which under UU 16/2025 is **BPK**, by statute.

---

## 1. The four tests

Apply in order. **A failure at any step voids everything downstream.** A validly
constituted forum cannot cure an ineligible approver, and a quorum cannot cure a
self-approval.

| # | Test | Fails when | Verdict |
|---|---|---|---|
| 1 | **Authority exists and is sourced** | No `DOA-xx` row reaches this decision at this size, or the row lacks `Clause / Page` + `Effective Date` | `indeterminate` |
| 2 | **Approver is eligible** | Approver barred by the concurrent-position prohibition (UU 16/2025), not validly in office, or conflicted without recusal | **`void`** |
| 3 | **Separation of duties holds** | `Proposer` == `Approver`, or `Risk Bearer` is empty on a material decision | **`void`** |
| 4 | **Evidence of approval is verified** | Approval is asserted rather than evidenced by an authorized system | **`void`** — and never record it |

---

## 2. Workbook mapping — where each answer lives

The *Actual Condition Input Workbook* is the Tier 2 source. Cite its IDs with the
same discipline as a statute: ID, column, clause, effective date.

| Question | Workbook cell |
|---|---|
| Who approves at this size? | `05_DECISION_RIGHTS_DOA` → `DOA-xx` · `Financial / Risk Threshold` + `Approver` |
| Who proposed it? | `DOA-xx` · `Proposer` |
| **Who bears the risk?** | `DOA-xx` · `Risk Bearer` — **may not be empty for a material decision** (the workbook's own rule, sheet 05 R2) |
| Which forum? | `DOA-xx` · `Decision Forum` → `06_COMMITTEE_CHARTERS` → `COM-xx` |
| Quorum? | `COM-xx` · `Quorum` |
| Forum's authority ceiling? | `COM-xx` · `Approval Authority` + `Thresholds` |
| What if it exceeds the ceiling? | `DOA-xx` · `Exceptions / Escalation`; `COM-xx` · `Escalation Path` |
| Is the delegation current? | `DOA-xx` · `Effective Date` — **after 6 Oct 2025?** (UU 16/2025 separated supervisory and operational functions) |
| Named human approver for this skill | `15_SKILL_RACI` · `Human Approver`, `Business Accountable (A)` |

**A cell is a source only with `DoA / Legal Document` + `Clause / Page` +
`Effective Date`.** A row naming an approver and a threshold but no clause and no
date is a *claim about* a delegation. `ingest_actual_condition.py` marks it
`UNSOURCED` and does not promote it. Treat it as absent — routing a real decision
to an approver named in an unsourced cell is inventing authority with extra steps.

---

## 3. Self-approval — computable, and usually invisible

Sheet 05 separates `Proposer`, `Reviewer`, `Recommender`, `Approver`, `Executor`,
`Monitor`, and `Risk Bearer` into distinct columns. That structure makes a control
failure **mechanically detectable**:

```
IF   DOA-xx.Proposer == DOA-xx.Approver          -> self-approval        -> void
IF   DOA-xx.Approver == DOA-xx.Risk Bearer  AND  the decision is material
                                                  -> no independent check -> escalate
IF   DOA-xx.Risk Bearer is empty  AND  material   -> workbook rule breach -> void
```

Self-approval rarely appears as one person signing their own memo. It appears as:

- the same **organ** proposing and approving through two named individuals who
  both report to it;
- a **recommender** whose recommendation is treated as the decision because the
  approver never met;
- an **executor** who set the terms proposing the approval of those terms.

**Name the organ, not just the person.** Two different names under one accountable
organ is still one organ approving itself.

---

## 4. Eligibility — the test that voids rather than delays

Per the BPK abstract of **UU 16/2025** (verified 2026-07-16; see
`08-sources/SOURCE_REGISTER.md` Tier 1), the amendment covers:

- **prohibition on BUMN organs holding concurrent positions**, including minister
  and deputy minister (*larangan organ BUMN merangkap jabatan*);
- **separation of supervisory and operational functions**;
- State **Series A Dwiwarna** shares with special rights;
- **BUMN financial examination by BPK**.

Consequences this skill must apply:

1. **An ineligible approver does not produce a weak approval. It produces no
   approval.** The decision is unapproved, whatever the minutes say. Route it as
   `void` and escalate — do not "note the concern and proceed".
2. **Supervisory organs approving operational matters** may breach the separation
   introduced by UU 16/2025. Where a `COM-xx` charter predates 6 Oct 2025, its
   allocation of who-approves-what is **presumptively stale**. Flag it.
3. **A Dwiwarna consent is a separate gate.** An approval valid on ordinary
   shareholder economics may still be incomplete. Do not infer Dwiwarna consent
   from an equity majority.

> TODO(legal): these follow the BPK abstract. The accountable legal owner must pin
> each to its pasal/ayat in the authenticated text and record the article number
> in `SOURCE_REGISTER.md`. This protocol deliberately does not guess article
> numbers it has not read.

---

## 5. Evidence of approval — the line that must never move

The skill **may not record, imply, or infer approval.** It may only report
approval that an authorized system has evidenced.

| Not evidence | Why |
|---|---|
| "The IC approved this last week" | Assertion. Which forum, which date, what quorum, minuted where? |
| A draft memo whose header says *Approved* | The document is the claim, not the evidence. |
| Silence after circulation | Non-objection is not approval unless the charter says so — and then only on the charter's terms. |
| A senior stakeholder saying it is fine | Not an instrument. Pasal 3E delegates to the Badan through its organs. |
| The absence of a recorded objection | Approval is a positive act. |

**Failure here is the package's worst outcome.** A fabricated approval does not
merely make a wrong decision — it manufactures the *appearance* of governance
around it, and the audit trail will show that challenge occurred. See
`ADVERSARIAL_CASES.yaml` → `fabricated-approval`.

---

## 6. Degrade honestly

When Tier 2 is missing — **the state today: every DOA/COM row is empty** — do not
say "route to the appropriate authority". Say:

> **`indeterminate`.** Cannot route a USD 200m commitment. Requires
> `05_DECISION_RIGHTS_DOA` row `DOA-04` (`Financial / Risk Threshold`, `Approver`,
> `Risk Bearer`) with `Clause / Page` and an `Effective Date` after 6 Oct 2025.
> Owner: [`15_SKILL_RACI` · `Business Accountable (A)`]. The question it answers:
> may DIM approve at this size alone, or does it escalate to Badan Pelaksana?
>
> **What can still be said without it:** the decision is material; `Risk Bearer`
> must be named before any forum considers it; and the approver must be checked
> against the concurrent-position prohibition regardless of which forum is chosen.

The first converts a gap into a shrug. The second converts it into a work item
with an owner, a cell, and a question. **That difference is the whole value of
this skill in the current state of the estate.**

---

## 7. Failure modes

| Failure | The pressure that causes it | Correct behaviour |
|---|---|---|
| Routing to a *plausible* approver | The DoA is empty, the deadline is real, and someone senior is obviously "the right person" | `indeterminate`. Name `DOA-xx`. A plausible approver is an unauthorised one wearing seniority. |
| Treating an unsourced cell as a delegation | The cell is filled, so it looks like evidence | No clause + date → a claim, not a delegation. Treat as absent. |
| Accepting an ineligible approver "for now" | The forum met, the decision is made, re-running it is expensive | The approval is **void**, not weak. Sunk process cost is not a cure. |
| Missing organ-level self-approval | Two different individual names appear, so it looks separated | Name the **organ**. Two names under one organ is one organ approving itself. |
| Recording approval from a claim | Everyone in the room knows it was approved | Report only what an authorized system evidences. Never record. |
| Treating non-objection as approval | Circulation closed and nobody objected | Approval is a positive act unless the charter says otherwise, on its terms. |
| Using a pre-Oct-2025 charter | It is the charter on file and looks authoritative | UU 16/2025 separated supervisory and operational functions. Pre-amendment allocations are presumptively stale. |
