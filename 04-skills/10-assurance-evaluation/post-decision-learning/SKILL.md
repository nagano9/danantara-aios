---
name: post-decision-learning
description: Compares expected and actual outcomes, identifies thesis or execution errors, captures lessons, updates controls, and assigns corrective actions. Use after milestones, exits, incidents, restructurings, and material decisions.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: BPI/DAM/DIM/DDMF
  cluster: 10-assurance-evaluation
  risk-tier: high
  version: "1.2.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# Post-Decision Learning

## Objective
Settle the prediction that was recorded before the decision, and score process and outcome separately.

A learning loop without a recorded prediction is storytelling. Once the outcome is known, hindsight makes it look foreseeable and reviewers reconstruct a narrative in which the signals were present all along. That is narrative construction with an audit trail, not learning.

This skill audits nothing. Audit asks whether the process was followed; learning asks whether the reasoning was right. A decision can pass every audit and still rest on a thesis that was wrong.

Full method: `references/learning-loop-protocol.md`.

## Use when
- A `Post-Decision Review Date` falls due (`20_DECISION_LOG` col 28).
- A milestone, exit, incident, restructuring, or condition-precedent deadline passes.
- A falsification trigger stated by a deciding skill has fired.
- A decision succeeded. Reviewing only failures guarantees `dumb luck` is never detected.

## Do not use when
- The question is whether process was followed - that is `compliance-policy-checker` or `evidence-citation-auditor`.
- The decision has not yet been made - falsification hooks are set by the deciding skill, not here.
- The question is whether a skill needs changing - this skill supplies the finding; `skill-lifecycle-governor` makes the change.

Do not use this skill to bypass a competent authority, replace licensed or accountable professional judgment, process unauthorized information, or make an institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
- The prediction recorded before the decision, with its date and falsification trigger. Its absence is the finding.
- The decision record: `20_DECISION_LOG` - `Key Assumptions`, `Commercial Finding`, `Downside / Max Loss`, `Dissenting View`, `Conditions / CPs`, `Risk Owner`.
- The falsification hooks stated by the deciding skills.
- The actual outcome, with its source and effective date.
- The evidence available at decision time - required to score process without hindsight.

## Dependencies
- `institutional-memory-capture` - receives confirmed lessons.
- `skill-lifecycle-governor` - receives Arc 2 findings (skill defects).
- `skill-evaluation-runner` - receives regression cases from refuted predictions.
- `decision-precedent-retriever` - supplies the pattern across prior decisions.

## Authoritative sources
Start with `references/repo-learning-source-map.md` for the repo-native learning hierarchy.
1. Law, regulation, official decision, formal mandate. Capital is state capital: UU 1/2025 jo. UU 16/2025, Pasal 3G.
2. Danantara policy and the decision record. `20_DECISION_LOG` is the ledger.
3. Audited or owner-certified outcome data, with owner and effective date.
4. Independent external evidence and reference classes.
5. Prior decisions as pattern, not as precedent for correctness. A repeated decision is not a validated one.

If the recorded prediction is missing, or appears to have been written after the outcome, return `unlearnable`.

## Workflow
1. Locate the prediction. Was a falsifiable, dated claim recorded before the decision? If not -> verdict `unlearnable`. Stop.
2. Settle it against the trigger. Use the prediction as written, not a restatement improved by knowing the outcome.
3. Score the process using only evidence available at decision time.
4. Score the outcome independently.
5. Place it on the matrix. Both off-diagonals are the point of the exercise.
6. Separate thesis error from execution error, with evidence.
7. Check the pattern. One outcome is one sample. Query `decision-precedent-retriever` before changing any control.
8. Route the three arcs, each with an owner and a date:
   - Arc 1 -> `20_DECISION_LOG` - `Outcome / Lessons`; `institutional-memory-capture`
   - Arc 2 -> `skill-lifecycle-governor` (a failure mode that fires twice and is still unnamed is a skill defect, not a user error)
   - Arc 3 -> `19_IMPLEMENTATION_BACKLOG` (every `indeterminate`/`void`/`stop` names a missing cell; the blocking count sets priority)

## Verdicts
Process and outcome are different axes. Judging the first by the second is resulting, and it is the dominant failure mode of institutional learning.

|  | Good outcome | Bad outcome |
|---|---|---|
| Good process | `deserved success` - reinforce | `bad break` - protect the process |
| Bad process | `dumb luck` - most dangerous | `deserved failure` - fix the process |

Plus: `unlearnable` - no falsifiable prediction was recorded before the decision.

`dumb luck` is the most dangerous cell. A bad process produced a good outcome, so the process gets praised, repeated, and institutionalised.

`bad break` is where good process gets punished. Learning from it degrades a process that was working and teaches the organisation that rigour is not protective.

This skill must be able to return `dumb luck` on a profitable deal. A loop that cannot criticise a success is not a loop - it is a ratchet of self-congratulation.

## Failure modes
The middle column is load-bearing: learning fails under pressure, not from ignorance.

| Failure | The pressure that causes it | Correct behaviour |
|---|---|---|
| Resulting | The deal made money; nobody wants to review a success | Score process and outcome separately. `dumb luck` on a profitable deal is legitimate and important. |
| Constructing a lesson without a prediction | A review is due and a lesson is the expected deliverable | `unlearnable`. Naming the absence is the lesson. |
| Hindsight in the narrative | The outcome is known and the signals now look obvious | Use only the recorded prediction and evidence available at decision time. |
| Blaming execution to protect the thesis | The thesis owner is senior and still in post | Distinguish thesis from execution error with evidence. |
| Learning from one outcome | It was vivid, recent, and expensive | One outcome is one sample. Find the pattern before changing a control. |
| Filing the lesson and changing nothing | The review is the deliverable, not the change | A lesson with no owner, artifact, and date is not a lesson. |
| Quietly dropping refuted predictions | They are embarrassing; the decision is already made | A refuted prediction is the highest-value record in the ledger. |
| Reviewing only failures | Successes look like they need no review | Then `dumb luck` is never detected. |

## Falsification hooks
- `deserved success` becomes `dumb luck` if the recorded prediction was refuted and the outcome arrived through a mechanism the thesis did not identify.
- `deserved failure` becomes `bad break` if the process is shown to have priced the risk that fired, and the loss fell within the recorded downside.
- Any verdict other than `unlearnable` is void if the prediction was written or amended after the outcome was known.

> GAP(workbook): `20_DECISION_LOG` has `Key Assumptions` (12), `Post-Decision Review Date` (28), and `Outcome / Lessons` (29) - but no column for a falsifiable prediction. `Key Assumptions` is a belief; a prediction is scoreable.
>
> Recommend adding: `Predicted Outcome / Falsification Trigger`, populated from the deciding skills' falsification hooks; and `Prediction Verdict` (`confirmed` / `refuted` / `unlearnable`), scored at the review date.
>
> Until then this skill will return `unlearnable` for most decisions - which is the honest answer, and the one that gets the columns added.

## Danantara Way decision rules
- A learning loop without a recorded prediction is storytelling.
- Process quality and outcome quality are different axes. Never infer one from the other.
- A good outcome does not validate a decision. State capital makes `dumb luck` an unpriced exposure that happened not to fire.
- A refuted prediction is the highest-value record in the ledger; protect it.
- One outcome is one sample. Patterns change controls; anecdotes do not.
- Prefer evidence, scenarios, benchmarks, and traceable calculations over narrative assertion.
- State assumptions, confidence, data gaps, dissent, and unresolved tensions explicitly.

## Output contract
Primary output: a settled prediction and a scored decision -

- the prediction as recorded, with its date and trigger - or `unlearnable`;
- `confirmed` / `refuted`, against the trigger as written;
- process score, using only decision-time evidence;
- outcome score;
- matrix verdict: `deserved success` / `bad break` / `dumb luck` / `deserved failure` / `unlearnable`;
- thesis error vs execution error, with evidence;
- the pattern across prior decisions, or a statement that this is a single sample;
- three routed arcs, each with owner and date: decision (Arc 1), skill (Arc 2), gap (Arc 3).

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result as AI-assisted analysis or draft until the required human authority has approved it.

## Human approval
The independent assurance owner and the decision's `Risk Owner`. The skill may analyze, challenge, draft, calculate, and recommend. It may not execute, bind, disclose, waive, appoint, dismiss, allocate capital, or record final approval unless a separate authorized system provides verified evidence of that human action.

It may not close a lesson, mark remediation complete, or amend a skill - Arc 2 findings are routed to `skill-lifecycle-governor`, which owns that change.

## Escalation
Stop and escalate when authority is missing, evidence is materially inadequate, conflicts are unresolved, legal basis is doubtful, downside cannot be bounded, data use is unauthorized, material sources conflict, an exception is requested, or the recommendation depends on an unapproved subsidy or informal direction.

Specific to this skill - escalate when:
- a prediction appears to have been written or amended after the outcome;
- a `dumb luck` verdict is resisted because the deal was profitable;
- the same failure mode has fired twice and remains unnamed in the skill;
- a refuted prediction is being removed from the record;
- the realised loss exceeds the recorded `Downside / Max Loss`;
- a lesson is requested where no prediction exists.

## Prohibited actions
- Do not construct a lesson where no prediction was recorded. Return `unlearnable`.
- Do not infer decision quality from outcome quality, in either direction.
- Do not restate a prediction to fit the outcome, or score against a restatement.
- Do not delete, soften, or quietly drop a refuted prediction.
- Do not attribute a thesis error to execution without evidence.
- Do not make, imply, fabricate, or backdate institutional approval.
- Do not invent facts, sources, policy, authority, financial results, valuation inputs, or certainty.
- Do not disclose or process information outside its authorized classification, purpose, users, tools, systems, or jurisdiction.
- Do not collapse commercial return and national impact into an opaque single score.

## Quality checks
- The prediction is quoted as recorded, with its date, not as restated.
- Process was scored using only evidence available at decision time.
- The matrix verdict is stated, and off-diagonals were genuinely considered.
- `dumb luck` was tested for on successful outcomes, not only on failures.
- Every lesson has an owner, an artifact, and a date - or it is not a lesson.
- All three arcs are routed, or their absence is stated.
- Material claims have traceable sources and clear fact/assumption/inference labels.
- Relevant Danantara Way principles and core tensions were explicitly tested.
- An independent reviewer could reproduce the reasoning and understand dissent and limitations.

## Audit record
Capture request, user and role, purpose, entity, risk tier, data classification, sources, versions, tool calls, calculations, assumptions, analyses, challenge, dissent, approvals, conditions, final human decision, execution status, monitoring results, and post-decision learning.

Specific to this skill: record the prediction as it stood before the decision, and any attempt to amend it after, the matrix verdict with both scores, and the three routed arcs with owners. Under UU 16/2025 BUMN financial examination sits with BPK - a ledger showing only successes has a statutory external reader.
