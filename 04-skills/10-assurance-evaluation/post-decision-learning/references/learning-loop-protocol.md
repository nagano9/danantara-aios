# Learning loop protocol

Method reference for `post-decision-learning`. Implements step 13 of
`MASTER_ORCHESTRATION_PROTOCOL.md` ("compare expected and actual results; update
skills, references, controls, and institutional memory") and §8 of
`EVALUATION_STRATEGY.md` (production monitoring, realized decision outcomes).

---

## 0. Why this skill previously did not exist

`post-decision-learning` shared a single workflow with eight other assurance
skills, and that workflow is a **generic audit**: *"Define the artifact, workflow,
model, skill, or decision being independently reviewed."*

Audit and learning are different operations with different outputs. **Audit asks
whether the process was followed. Learning asks whether the reasoning was
right.** A decision can pass every audit — correct authority, complete evidence,
minuted approval — and still be built on a thesis that was wrong. Auditing it
again after the outcome finds nothing new, because nothing procedural failed.

`skill-evaluation-runner` and `skill-lifecycle-governor` shared the same audit
workflow. The loop existed as three names running an inspection procedure.

---

## 1. The prediction rule

> **A learning loop without a recorded prediction is storytelling.**

This is the whole discipline. Everything else is mechanics.

Once the outcome is known, hindsight makes it look foreseeable. Reviewers
reconstruct a narrative in which the signals were present all along, and the
"lesson" is whatever the outcome suggests. This is not learning — it is narrative
construction with an audit trail.

**Learning requires a prediction that was falsifiable, recorded, and dated
BEFORE the decision.** Without one, there is nothing to compare the outcome
against, and the honest verdict is **`unlearnable`**.

`unlearnable` is not a failure of this skill. It is a finding about the decision
record — and it is the finding that most improves future decisions, because it is
the one that forces predictions to be written down next time.

### Where the predictions come from

The estate already generates them. Every skill built to the Elite Skill Standard
(`03-templates/ELITE_SKILL_STANDARD.md` §4) states **falsification hooks** — what
would change its verdict — up front:

| Skill | Its recorded prediction |
|---|---|
| `dcf-model-challenger` | *"`fit` flips to `not fit` if TV/EV exceeds 75% and the perpetuity anchor cannot be sourced to long-run nominal GDP."* |
| `investment-mandate-interpreter` | *"This becomes `within mandate` when DOA-04 supplies a threshold above the ticket size, effective after 6 Oct 2025."* |
| `human-approval-orchestrator` | *"`routable` becomes `void` if the approver holds a barred concurrent position."* |

**The falsification hook is the prediction. This skill is where it is settled.**
That is the loop: hooks stated at decision time, tested at review time.

A skill whose hooks are never tested is unfalsifiable in practice, however
rigorous it looks.

### Gap in the workbook

`20_DECISION_LOG` carries `Key Assumptions` (col 12), `Post-Decision Review Date`
(28), and `Outcome / Lessons` (29). It has **no column for a falsifiable
prediction**.

`Key Assumptions` is not a prediction. "We assume demand grows with GDP" cannot be
scored. A prediction is: *"EBITDA ≥ IDR X by Q4 2027; below IDR Y the thesis is
wrong."* One is a belief; the other can be marked right or wrong.

> **RECOMMENDATION(workbook):** add two columns to `20_DECISION_LOG`:
>
> - **`Predicted Outcome / Falsification Trigger`** — the specific, dated,
>   falsifiable claim, populated from the deciding skills' falsification hooks.
> - **`Prediction Verdict`** — scored at `Post-Decision Review Date`:
>   `confirmed` / `refuted` / `unlearnable (no prediction recorded)`.
>
> Without these, `Outcome / Lessons` can only produce narrative, and the loop
> will ratchet self-congratulation while looking like governance.

---

## 2. Resulting — the failure that institutionalises bad process

**Decision quality and outcome quality are different axes.** Judging the first by
the second is known in decision analysis as *resulting*, and it is the dominant
failure mode of institutional learning.

|  | **Good outcome** | **Bad outcome** |
|---|---|---|
| **Good process** | Deserved success — *reinforce* | **Bad break** — *protect the process* |
| **Bad process** | **Dumb luck** — *most dangerous* | Deserved failure — *fix the process* |

Both diagonals are handled correctly by most institutions. The off-diagonals are
where the damage is:

- **Dumb luck** is the most dangerous cell in the matrix. A bad process produced a
  good outcome, so the process gets **praised, repeated, and institutionalised**.
  The organisation learns precisely the wrong lesson and does so confidently. It
  is invisible without a recorded prediction — the only evidence is that the
  reasoning was wrong even though the result was right.
- **Bad break** is where good process gets punished. A sound thesis met a
  genuinely unforeseeable event. If the institution "learns" from it, it degrades
  a process that was working, and teaches its people that rigour is not
  protective.

**Therefore: this skill must score process and outcome separately, and must be
able to return `dumb luck` on a profitable deal.** A learning loop that cannot
criticise a success is not a loop — it is a ratchet of self-congratulation.

> The Danantara-specific edge: capital is **state capital** (UU 1/2025 jo.
> UU 16/2025, Pasal 3G). A `dumb luck` outcome on state capital is not a happy
> accident to be repeated. It is an unpriced exposure that happened not to fire,
> and the institution is now more likely to run it again, larger.

---

## 3. The three arcs

The loop is not one feedback path. It is three, with different clock speeds,
different owners, and different sinks.

### Arc 1 — Decision loop: *was the reasoning right?*
- **Trigger:** `Post-Decision Review Date` (`20_DECISION_LOG` col 28), milestone,
  exit, incident, or restructuring.
- **Input:** the recorded prediction and its falsification trigger.
- **Test:** confirmed / refuted / unlearnable; then process vs outcome (§2).
- **Sink:** `20_DECISION_LOG` · `Outcome / Lessons`; `institutional-memory-capture`.
- **Owner:** the decision's `Risk Owner`.

### Arc 2 — Skill loop: *was the skill right?*
- **Trigger:** a refuted prediction traceable to a skill's method, or the §8
  production-monitoring signals (trigger precision/recall, overrides, escalations,
  unsupported claims, citation failures).
- **Test:** did the skill's discriminating test fail to discriminate? Was a
  threshold wrong? Did a failure mode fire that was not named?
- **Sink:** the skill's `references/` and `## Failure modes`, via
  `skill-lifecycle-governor`; regression cases via `skill-evaluation-runner`.
- **Owner:** `15_SKILL_RACI` · `AI Product Owner`.
- **Rule:** a failure mode that fires **twice** and is still unnamed is a defect
  in the skill, not in the user.

### Arc 3 — Gap loop: *what did we not know?* **(this is what fills the workbook)**
- **Trigger:** every `indeterminate`, `void`, or `stop` verdict.
- **Test:** which named cell was missing, and how many decisions has it blocked?
- **Sink:** `19_IMPLEMENTATION_BACKLOG`.
- **Owner:** the cell's owner from `15_SKILL_RACI`.

**See §4. This arc answers the sequencing question.**

---

## 4. The workbook fills itself — it is neither first nor last

The *Actual Condition Input Workbook* asks for roughly 1,300 cells across 22
sheets. Filling it upfront is not feasible: the charters, delegations, and
policies do not yet exist in retrievable, dated form. Filling it last is worse —
the skills stay `indeterminate` for the entire programme and deliver nothing.

**Neither. It fills by demand, and the `indeterminate` verdict is the collection
mechanism.**

Every honest degradation names exactly one missing cell, its owner, and the
question it answers (Elite Skill Standard §5). That is not a limitation. **It is a
work item, pre-scoped by real demand.** And `19_IMPLEMENTATION_BACKLOG` is already
shaped to receive it:

| Verdict produces | `19_IMPLEMENTATION_BACKLOG` column |
|---|---|
| the skill + verdict that blocked | `Source Gap / Evidence` |
| the missing cell (e.g. `DOA-04` · `Financial / Risk Threshold`) | `Initiative / Action` |
| the question it would answer ("may DIM approve USD 200m alone?") | `Blocker / Decision Needed` |
| owner from `15_SKILL_RACI` | `Accountable Owner` |
| **how many decisions this cell has blocked** | `Priority` |
| pilot the blocked decision belongs to | `Target Wave` |

**The loop:**

```
run a real decision
        │
        ▼
skill returns `indeterminate` — names DOA-04, its owner, the question
        │
        ▼
gap ledger entry -> 19_IMPLEMENTATION_BACKLOG
        │
        ▼
blocking count rises as more decisions hit the same cell
        │
        ▼
Danantara fills THAT ONE cell (clause + effective date + evidence)
        │
        ▼
skill now answers, sourced —— and never asks again
```

**Priority is not decided in a workshop. It is measured.** The cell blocking nine
decisions gets filled before the cell blocking none. Most of the 1,300 cells will
never block anything in Wave 1, and filling them is effort spent on skills nobody
is running yet.

This inverts the sequencing question the programme keeps asking:

| Approach | Effort before first value | Prioritisation | Failure mode |
|---|---|---|---|
| Workbook first | ~1,300 cells | guessed | stalls; cells filled for skills nobody runs; content stale before use |
| Workbook last | 0 | none | skills answer `indeterminate` for the whole programme; no value delivered |
| **By demand** | **~20 cells for the pilot** | **measured by blocking count** | requires running real decisions against `indeterminate` verdicts and tolerating them |

The last row's cost is real and worth naming: **the institution must be willing to
run decisions through a system that says "I cannot answer yet, and here is exactly
what I need."** That takes more nerve than a system that guesses — and it is the
only version that is honest about what it knows.

---

## 5. Failure modes

The middle column is load-bearing: learning fails under *pressure*, not from
ignorance.

| Failure | The pressure that causes it | Correct behaviour |
|---|---|---|
| **Resulting** | The deal made money; nobody wants to review a success | Score process and outcome separately. `dumb luck` on a profitable deal is a legitimate and important verdict. |
| **Constructing a lesson without a prediction** | A review is due and a lesson is expected as the deliverable | `unlearnable`. Naming the absence is the lesson. |
| **Hindsight in the narrative** | The outcome is known and the signals now look obvious | Use only the recorded prediction and the evidence available at decision time. |
| **Blaming execution to protect the thesis** | The thesis owner is senior and still in post | Distinguish thesis error from execution error with evidence. Defaulting to "execution" is how bad theses survive. |
| **Learning from one outcome** | It was vivid, recent, and expensive | One outcome is one sample. Look for the pattern across the ledger before changing a control. |
| **Filing the lesson and changing nothing** | The review is the deliverable, not the change | A lesson with no owner, no artifact, and no date is not a lesson. Arc 2 and Arc 3 must have sinks. |
| **Quietly dropping refuted predictions** | They are embarrassing and the decision is already made | A refuted prediction is the highest-value record in the ledger. |
| **Reviewing only failures** | Successes look like they need no review | Then `dumb luck` is never detected, and the bad process that produced it is institutionalised. |
