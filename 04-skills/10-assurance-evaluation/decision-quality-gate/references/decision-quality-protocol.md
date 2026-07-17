# Decision quality protocol

Method reference for `decision-quality-gate`. On 7 of the 10 reference workflows,
positioned immediately before `human-approval-orchestrator` — the last assurance
before a human decides.

The skill's 8-step workflow is sound and is not restated. This covers the four
properties the step list does not express.

---

## 1. Gate capture — the structural problem of running last

**The later a gate runs, the more sunk cost pushes against it.**

By the time this gate executes, the diligence is complete, the model is built, the
memo is written, the committee is booked, and the sponsor has told people it is
happening. `RETURN` sends all of that backwards. The gate is therefore under more
pressure than any other control in the estate — **not because it is weaker, but
because of where it sits.**

Gate capture does not announce itself. It looks like:

- verdicts drifting from `RETURN` toward `CONDITIONAL PASS` with conditions nobody
  tracks;
- conditions written vaguely enough to be self-certifying ("management to monitor
  execution risk");
- findings recorded in a section the committee does not read;
- the gate running *after* the decision has been socialised, so its only available
  verdict is agreement.

**Countermeasure — the gate must monitor itself:**

> **A gate that never returns `RETURN` is not a gate.**

Track the gate's own verdict distribution. A 100% pass rate across 20 material
decisions has exactly two explanations: upstream work is perfect, or the gate is a
rubber stamp. **The base rate distinguishes them, and nothing else does.** Report
the distribution to the assurance owner on a defined cycle, not on request.

If the pass rate is 100% and upstream skills have never been revised (see
`skill-lifecycle-governor`), the second explanation is the likely one.

---

## 2. The four findings are four tests, never one score

`20_DECISION_LOG` carries four separate columns — `Commercial Finding` (13),
`Strategic / National Finding` (14), `Governance Finding` (15), `Intergenerational
Finding` (16) — and sheet 20's own rule states they **must be presented
separately** together with evidence, dissent, risk owner, conditions, and
post-decision review.

That is not a formatting preference. It is the ultimate test made structural:

> *Apakah keputusan ini tetap benar secara komersial, strategis, tata kelola, dan
> kepentingan generasi mendatang?*

**Four questions. Four answers. Never averaged.**

| Wrong | Right |
|---|---|
| "Scores 3 out of 4; net positive" | "Passes commercially, strategically, and on governance. **Fails intergenerationally**, on [named evidence]." |
| "Overall attractive with some ESG concerns" | Four findings, four verdicts, the failing one named and unhidden |
| A weighted composite | A tension handed to `dual-mandate-balancer` intact |

**A decision that fails one dimension is not a decision that scored 75%.** It is a
decision with a named failure that a human must decide to accept, in the open,
with their name on it. Averaging removes the human's opportunity to refuse — which
is the only thing the four columns exist to protect.

If the pack presents a blended score, that is `RETURN` on its own. The blending is
the defect; the underlying deal may be fine.

---

## 3. The gate requires the prediction — this is where the loop closes

`post-decision-learning` can only settle a prediction that was **recorded before
the decision**. Without one, its verdict is `unlearnable`, permanently, and the
institution learns nothing from that decision no matter how the outcome lands.

**Nothing downstream can fix this.** After the decision, it is too late by
construction — a prediction written later is hindsight.

**Therefore this gate is where the prediction is required.** It is the last point
at which it can still be demanded.

Before `PASS` or `CONDITIONAL PASS`:

| Requirement | Source |
|---|---|
| A falsifiable, dated predicted outcome | the deciding skills' **falsification hooks** (Elite Skill Standard §4) |
| A trigger that would show the thesis wrong | e.g. *"EBITDA < IDR Y by Q4 2027"* |
| A post-decision review date | `20_DECISION_LOG` col 28 |
| A named `Risk Owner` to settle it | `20_DECISION_LOG` col 23 |

**No recorded prediction → `RETURN`.** Not `CONDITIONAL PASS` — a condition to
"add the prediction later" is precisely the hindsight this prevents.

This makes the gate the hinge of the whole architecture:

```
skills state falsification hooks
        │
        ▼
decision-quality-gate REQUIRES them before PASS   ◄── the loop closes here
        │
        ▼
decision made, prediction recorded
        │
        ▼
post-decision-learning settles it: confirmed / refuted
        │
        ▼
skill-lifecycle-governor changes the method (Arc 2)
```

Remove this requirement and the loop is decorative: hooks are stated, never
recorded, never settled, never fed back.

> **GAP(workbook):** `20_DECISION_LOG` has no column for a falsifiable prediction —
> `Key Assumptions` (12) is a belief, not a scoreable claim. Until
> `Predicted Outcome / Falsification Trigger` exists (see
> `post-decision-learning/references/learning-loop-protocol.md` §1), this gate
> must require the prediction in the evidence pack and record where it sits.

---

## 4. Two silences that are findings

Absence is evidence, and both of these read as "clean" on a checklist.

### Empty dissent

`20_DECISION_LOG` col 18 is `Dissenting View`. On a material decision, an empty
dissent field has two explanations: genuine consensus, or **challenge that was
never invited or never survived**.

The gate cannot tell which from the field alone. It can ask:

- Was the challenge **organisationally** independent of the proposal? A red team
  invoked by, reporting to, and scoped by the proposer is a formality with a token
  cost.
- Did `investment-thesis-red-team` or `dcf-model-challenger` run, and did they
  find **nothing**? A challenge that finds nothing was usually run at the wrong
  altitude (see `dcf-model-challenger` failure modes).
- Is there a record of a dissent that was **resolved**, or only an absence?

**Unanimity on a material decision is a claim requiring evidence, not a default.**

### Unbounded downside

`20_DECISION_LOG` col 17 is `Downside / Max Loss`. If it cannot be bounded, the
verdict is **`STOP`**, not `CONDITIONAL PASS` with a monitoring condition.

Capital is **state capital** (UU 1/2025 jo. UU 16/2025, Pasal 3G — *penyertaan
modal negara*). An unbounded downside on state capital is not a risk to monitor;
it is an exposure nobody has priced and nobody owns. Probability-weighting it
against upside does not bound it — it hides it behind an expected value.

---

## 5. Failure modes

The middle column is load-bearing: this gate fails under *pressure*, not from
ignorance — and it sits where the pressure is highest.

| Failure | The pressure that causes it | Correct behaviour |
|---|---|---|
| **Gate capture** | The work is done, the committee is booked, `RETURN` costs weeks | Position creates the pressure; it does not change the standard. Monitor the gate's own pass rate. |
| **`CONDITIONAL PASS` as a soft `RETURN`** | It lets everyone move while looking rigorous | A condition needs an owner, a date, and a way to fail. "Management to monitor" is not a condition. |
| **Accepting a blended score** | The committee asked for one number | Blending is `RETURN` on its own. Four findings, four verdicts. |
| **Passing without a prediction** | Nobody has ever been asked for one | `RETURN`. After the decision it is hindsight — nothing downstream can fix it. |
| **Reading empty dissent as consensus** | The field is blank and the pack is clean | Unanimity on a material decision is a claim requiring evidence. |
| **Accepting a challenge that found nothing** | The model is polished and the team is credible | Almost always the wrong altitude, not a sound proposal. |
| **Monitoring an unbounded downside** | `STOP` is drastic and the deal is attractive | State capital. Unbounded is `STOP`, not a condition. |
| **Running after socialisation** | The sponsor announced it; the gate is a formality now | Escalate: the gate ran too late to be a gate. |
| **Treating its own PASS as approval** | It is the last check before the human | A quality verdict is not an authority verdict. Route to `human-approval-orchestrator`. |
