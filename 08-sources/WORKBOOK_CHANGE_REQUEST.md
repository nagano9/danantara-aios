# Workbook change request — CR-001

Target: **Danantara AIOS — Actual Condition Input Workbook** (`*_Input_Template_v1.xlsx`)
Raised: 2026-07-17 · Status: **open** · Blocks: `decision-quality-gate`, `post-decision-learning`

---

## CR-001 — add a falsifiable prediction to `20_DECISION_LOG`

### Why this blocks the estate

`decision-quality-gate` (critical, on 7 of 10 chains) now requires a recorded
prediction before it will issue `PASS`. Today the workbook has nowhere to put one,
so the gate will correctly return **`RETURN` on every material decision**. The gate
is working; the workbook cannot yet receive what it asks for.

The reason it asks is structural, not stylistic:

> **`post-decision-learning` can only settle a prediction recorded *before* the
> decision. Without one its verdict is `unlearnable`, permanently — and nothing
> downstream can fix it, because a prediction written after the outcome is
> hindsight by construction.**

`decision-quality-gate` is the **last point at which a prediction can still be
required**. Miss it and that decision is unlearnable forever, whatever the outcome.

### Why `Key Assumptions` is not sufficient

`20_DECISION_LOG` already has `Key Assumptions` (col 12). It is not a prediction.

| | Example | Can it be marked right or wrong? |
|---|---|---|
| **Assumption** (col 12, exists) | "Demand grows in line with GDP" | No. It is a belief. |
| **Prediction** (missing) | "EBITDA ≥ IDR 480bn by Q4 2027; below IDR 400bn the thesis is refuted" | **Yes.** Dated, specific, falsifiable. |

Without the second, `Outcome / Lessons` (col 29) can only produce narrative — and
the loop ratchets self-congratulation while looking like governance.

### The change

Sheet **`20_DECISION_LOG`**, backed by Excel Table **`DecisionLogTable`**
(current ref `A7:AC107`, 29 columns).

Add **two columns** after `Outcome / Lessons` (currently col 29 = `AC`):

| New col | Header (exact) | Fill |
|---|---|---|
| **AD** | `Predicted Outcome / Falsification Trigger` | yellow (Danantara input) |
| **AE** | `Prediction Verdict` | yellow (Danantara input) |

**Apply it in Excel, not with a script.** Click any cell inside `DecisionLogTable`
and type the new header in `AD7`; Excel extends the Table ref to `A7:AE107`,
adds the `tableColumn` entry, and carries the header formatting automatically.
Repeat for `AE7`.

> **Do not round-trip this workbook through openpyxl to make this change.** Tested
> 2026-07-17: openpyxl preserves the 59 data validations and 21 conditional-format
> rules, but **silently drops `xl/drawings/charts/chart1.xml`** — the
> `01_DASHBOARD` chart. Excel handles the Table ref and formatting correctly;
> a script does not.

### Column definitions

**`AD` — Predicted Outcome / Falsification Trigger** *(free text, mandatory for
material decisions)*

Populated from the deciding skills' **falsification hooks**
(`03-templates/ELITE_SKILL_STANDARD.md` §4). Those hooks are already generated at
decision time — this column is where they are recorded rather than lost.

Must contain a claim that is **specific, dated, and refutable**:

> *"EBITDA ≥ IDR 480bn by Q4 2027. Below IDR 400bn the commercial thesis is
> refuted. Source: dcf-model-challenger v1.1 base case, 2026-07-17."*

Not acceptable: "we expect strong performance", "management is confident",
"in line with plan".

**`AE` — Prediction Verdict** *(dropdown, scored at `Post-Decision Review Date`)*

Add to `99_LOOKUPS` as a new list column, matching the existing pattern (header in
row 1, values below), then apply Data Validation → List to `AE8:AE107`:

| Value | Meaning |
|---|---|
| `Not Yet Due` | review date not reached |
| `Confirmed` | outcome met the prediction as written |
| `Refuted` | trigger fired — **the highest-value record in the ledger** |
| `Unlearnable` | no falsifiable prediction was recorded before the decision |

`Refuted` must never be quietly deleted. `Unlearnable` is honest and expected for
decisions recorded before this CR lands.

### Acceptance

Verified by `06-scripts/ingest_actual_condition.py`, which checks `20_DECISION_LOG`
for both headers and reports `CR-001 OPEN` until they exist. The same script can
also emit `tier2_index.json` and an optional markdown summary of the workbook
shape. The requirement is machine-checked so it cannot quietly lapse.

```
python 06-scripts/ingest_actual_condition.py <workbook.xlsx>
```

### Related, not blocking

`19_IMPLEMENTATION_BACKLOG` already has the right shape to receive Arc 3 gap items
(`Source Gap / Evidence`, `Blocker / Decision Needed`, `Accountable Owner`,
`Priority`). No change requested — every `indeterminate` verdict maps onto it as
it stands. See
`04-skills/10-assurance-evaluation/post-decision-learning/references/learning-loop-protocol.md`
§4.
