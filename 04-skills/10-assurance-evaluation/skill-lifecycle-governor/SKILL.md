---
name: skill-lifecycle-governor
description: Controls skill ownership, approval, versioning, dependencies, release, monitoring, incidents, retraining references, deprecation, archival, and periodic recertification. Use for enterprise management of the Danantara skill estate.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: BPI
  cluster: 10-assurance-evaluation
  risk-tier: critical
  version: "1.1.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# Skill Lifecycle Governor

## Objective
Stop a governance change from happening by accident, in a pull request, at the
altitude of a typo fix.

**A change to a critical skill is a policy change, executed by editing a markdown
file.** `dcf-model-challenger` says a DCF whose terminal value exceeds ~75% of
enterprise value is a terminal-value guess with a forecast attached. Move that to
85% and deals that would have been challenged now pass. No committee met, no
delegation was amended, no policy was reissued — one threshold moved in a text
file, and the institution's revealed risk appetite moved with it.

This is not release management. Full method:
`references/skill-change-protocol.md`.

**The test for any proposed change:** *would this change what gets approved?* If
yes, it is a policy change and needs an owner with authority to make one.

## Use when
- Any change to a skill is proposed — including one described as "just wording".
- `post-decision-learning` routes an Arc 2 finding (a refuted prediction traceable
  to a method).
- A **threshold** that gates a verdict is being moved.
- Anything in the shared governance kernel is being edited (128 of 133 skills
  carry byte-identical `## Prohibited actions` and `## Escalation`).
- A **CI ratchet floor** is proposed to be lowered.
- A skill is to be merged, deprecated, archived, or deleted.
- Periodic recertification of a critical-tier skill falls due.

## Do not use when
- The question is whether a *decision* was right — that is
  `post-decision-learning`, which supplies findings to this skill.
- The question is whether a skill *passes* its evaluations — that is
  `skill-evaluation-runner`, which supplies evidence to this skill.
- No skill is changing.

Do not use this skill to bypass a competent authority, replace licensed or
accountable professional judgment, process unauthorized information, or make an
institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
- **The proposed change, and the current version of the skill.**
- **Whether it would change what gets approved** — the classifying question.
- The evidence behind it: a **pattern**, not a single outcome.
- Regression results from `skill-evaluation-runner`, for Method class and above.
- Whether the skill has ever gated a decision (determines immutability and
  deletion eligibility).

## Dependencies
- `post-decision-learning` — supplies Arc 2 findings.
- `skill-evaluation-runner` — supplies regression and adversarial evidence.
- `decision-precedent-retriever` — supplies the pattern behind a proposed
  threshold change.
- `human-approval-orchestrator` — routes Threshold, Governance, and Estate class
  changes to a valid approver.

## Authoritative sources
1. **Law, regulation, official decision, formal mandate.** Under UU 16/2025 BUMN
   financial examination sits with **BPK**. A skill estate that cannot say which
   method applied to a past decision is not auditable by a statutory reader.
2. **Danantara AI governance policy and the AI Governance Committee charter.**
   **Currently unavailable** — `08-sources/SOURCE_REGISTER.md` Tier 2 is empty.
   `12_AI_GOV_CONTROLS` and `06_COMMITTEE_CHARTERS` (`COM-xx`) in the *Actual
   Condition Input Workbook* are the intended source. Until a `COM-xx` row names
   the AI Governance Committee with `Charter / Legal Source` and `Effective Date`,
   **Governance and Estate class changes are `hold`** — there is no identified body
   with authority to approve them.
3. `03-templates/ELITE_SKILL_STANDARD.md` — the quality bar a change must not
   regress.
4. Independent external evidence and reference classes.
5. Prior skill changes as pattern, not as precedent for correctness.

## Workflow
1. **Classify the change.** Editorial / Method / **Threshold** / Governance /
   Estate. Classify by *effect*, never by diff size. One character that moves a
   verdict boundary is a Threshold change.
2. **Apply the test.** Would it change what gets approved? Yes → it needs a policy
   owner, not a reviewer.
3. **Check immutability.** Has this version ever gated a decision? Then it may not
   be edited in place — supersede with a new version. Editing it retroactively
   rewrites what past decisions meant.
4. **Check evidence.** Threshold changes require a **pattern** from
   `decision-precedent-retriever`. One refuted prediction is one sample →
   **reject**.
5. **Check kernel propagation.** Does the edit touch a block shared across the
   estate? Then it propagates to **all** carriers in one change, or it does not
   happen. Drift is a defect, not a variation.
6. **Require regression.** Method class and above: `skill-evaluation-runner` must
   run, including `ADVERSARIAL_CASES.yaml`.
7. **Route for approval** by class, via `human-approval-orchestrator`.
8. **Issue the verdict**, and record the changelog entry in terms of *what a
   reader of the old record must know*. "Improved wording" is not a changelog.

## Verdicts
| Verdict | Meaning |
|---|---|
| `release` | Classified, evidenced, regression-clean, approved at the right level. |
| `release with conditions` | Proceeds with named conditions and a review date. |
| `hold` | Missing class evidence, pattern, regression, or an identified approver. **The default when Tier 2 is empty.** |
| `rollback` | In production and causing harm; revert to the last version that gated cleanly. |
| `deprecate` | Withdrawn from routing. **Version and content retained and retrievable.** |

**`hold` is a complete output.** A change that cannot name its approver is not
ready, however small it looks.

## Failure modes
The middle column is load-bearing: lifecycle governance fails under *pressure*,
not from ignorance.

| Failure | The pressure that causes it | Correct behaviour |
|---|---|---|
| **Threshold change treated as editorial** | It is one character, and a live deal needs it | Would it change what gets approved? Then it is policy. |
| **Editing a version in place** | The skill is obviously improved; nobody wants version noise | Immutable once it has gated a decision. Supersede. |
| **Kernel edited in one skill** | The edit was needed *here*, and 133 files is a lot | Drift is a defect. All, or none. |
| **Lowering a ratchet floor to go green** | The release is today and the floor "isn't the real issue" | Fix the detector or accept the red. A floor lowering is a decision to accept less assurance. |
| **Deleting a skill** | It is unused and the estate is cluttered | If it ever gated a decision, deletion destroys an audit record. Deprecate. |
| **Version bump without evaluation** | The change is small; the suite is slow | An untested method change is an untested policy change. |
| **Changing a threshold on one outcome** | A deal got away and someone is accountable | One sample. Patterns change controls; anecdotes do not. |
| **Accepting "it's just documentation"** | SKILL.md looks like docs | The markdown **is** the method. There is no separate implementation protecting it. |

## Falsification hooks
- *"`hold` becomes `release` when a `COM-xx` row names the AI Governance Committee
  with charter and effective date, and the change carries regression evidence."*
- *"`release` becomes `rollback` if a production decision is gated by a method
  whose version cannot be reconstructed from the audit record."*
- *"An Editorial classification is void if the change moves any number that gates a
  verdict."*

## Danantara Way decision rules
- A change to a critical skill is a policy change. Classify by effect, not by diff
  size.
- **A skill version that has gated a decision is immutable.** Superseding is a new
  version; editing rewrites the past.
- **The audit record must cite the skill name, version, and content hash that
  produced it.** Otherwise a change silently rewrites the meaning of every past
  decision, and BPK reads the new method against the old record.
- Drift is a defect. Shared text changes everywhere or nowhere.
- **A ratchet floor may not be lowered to make a build pass.** That is the
  institutional form of removing the downside case because it weakens the
  narrative.
- Patterns change controls; anecdotes do not.
- Deprecate, do not delete. A deleted skill makes its past decisions unreadable.
- State assumptions, confidence, data gaps, dissent, and unresolved tensions
  explicitly.

## Output contract
Primary output: **a change determination** —

- the change, and its **class** with the reason for that classification;
- whether it changes what gets approved;
- immutability finding: has this version gated a decision?
- evidence: the pattern, or a statement that only one sample exists;
- kernel propagation scope: how many skills carry the edited text;
- regression result, or its absence;
- the approver required for this class, routed via `human-approval-orchestrator`;
- **verdict**: `release` / `release with conditions` / `hold` / `rollback` /
  `deprecate`;
- **changelog written for a reader of the old record**, not for the author.

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result
as AI-assisted analysis or draft until the required human authority has approved
it.

## Human approval
By class: AI Product Owner (Editorial, Method); **policy owner with authority over
risk appetite** (Threshold); **AI Governance Committee** (Governance, Estate).

The skill may analyze, challenge, draft, calculate, and recommend. It may not
execute, bind, disclose, waive, appoint, dismiss, allocate capital, or record
final approval unless a separate authorized system provides verified evidence of
that human action.

**It may not approve its own class assignment**, and it may not release a change
whose approver cannot be identified in a sourced `COM-xx` row.

## Escalation
Stop and escalate when authority is missing, evidence is materially inadequate,
conflicts are unresolved, legal basis is doubtful, downside cannot be bounded,
data use is unauthorized, material sources conflict, an exception is requested, or
the recommendation depends on an unapproved subsidy or informal direction.

Specific to this skill — escalate when:
- a Threshold change is presented as Editorial;
- a **ratchet floor is proposed to be lowered** for any reason;
- a version that has gated a decision is being edited in place;
- kernel text is being changed in fewer than all carriers;
- a skill that has gated decisions is proposed for deletion;
- a change is urgent because of a live transaction;
- **no `COM-xx` row identifies a body with authority to approve this class** (the
  common case today).

## Prohibited actions
- **Do not classify by diff size.** One character that moves a verdict boundary is
  a Threshold change.
- **Do not edit a version that has gated a decision.** Supersede.
- **Do not release a kernel change to a subset of its carriers.**
- **Do not lower a ratchet floor to make a build pass**, and do not treat a red
  build as the obstacle.
- **Do not delete a skill that has ever gated a decision.**
- Do not change a threshold on a single outcome.
- Do not make, imply, fabricate, or backdate institutional approval.
- Do not invent facts, sources, policy, authority, financial results, valuation
  inputs, or certainty.
- Do not disclose or process information outside its authorized classification,
  purpose, users, tools, systems, or jurisdiction.
- Do not collapse commercial return and national impact into an opaque single
  score.

## Quality checks
- The change is classified by **effect**, with the classification reasoned.
- The immutability question is answered explicitly.
- Threshold changes cite a **pattern**, not an anecdote.
- Kernel propagation scope is counted, not assumed.
- Regression ran for Method class and above, including adversarial cases.
- The approver is named from a sourced instrument, or the verdict is `hold`.
- The changelog is written for a reader of the **old** record.
- Material claims have traceable sources and clear fact/assumption/inference
  labels.
- An independent reviewer could reproduce the reasoning and understand dissent and
  limitations.

## Audit record
Capture request, user and role, purpose, entity, risk tier, data classification,
sources, versions, tool calls, calculations, assumptions, analyses, challenge,
dissent, approvals, conditions, final human decision, execution status, monitoring
results, and post-decision learning.

Specific to this skill: record the **skill name, version, and content hash before
and after**; the class and its reasoning; the evidence pattern; the propagation
scope; the regression result; the named approver; and **any pressure applied to
reclassify a change downward or to lower a floor**. Under UU 16/2025 BUMN
financial examination sits with **BPK** — this record is how the institution
answers "which method applied when that decision was made".
