# DCF challenge protocol

Method reference for `dcf-model-challenger`. This is technique, not authority: it
does not establish what DIM may do (see `investment-mandate-interpreter`), only
whether a DCF can bear the weight of the decision being placed on it.

**Premise.** A DCF is not a valuation. It is an *arithmetic consequence of its
assumptions*. Challenging it means challenging the assumptions and the structure
that turns them into a number — never re-running the same model more carefully.
A model that is internally consistent and externally wrong will pass every
recalculation and still destroy state capital.

**Order matters.** Work 1 → 6. Structure before inputs, inputs before output.
Debating WACC to two decimals in a model with a circular reference or a hardcode
buried in a formula is wasted effort.

---

## 1. Structural integrity — before any input is discussed

If the model does not compute what it claims, its inputs are irrelevant.

| Check | Failure signature | Why it matters |
|---|---|---|
| **Hardcodes inside formulas** | `=C14*1.08+250` — a constant welded into a calculation | Invisible to sensitivity analysis. The single most common way a model lies while appearing live. |
| **Circular references / iterative calc** | Interest ← debt ← cash ← interest, with iteration enabled | Converges to a number with no economic meaning; often unstable across scenarios. |
| **Sign conventions** | Capex positive in one block, negative in another | Silent double-count or cancellation. |
| **Period alignment** | Stub period ignored; cash flow discounted a full year when six months away | Systematic overstatement of discount, or understatement if reversed. |
| **Mid-year convention** | Year-end discounting for cash flows arriving evenly | Understates value ~4–5% at a 9% rate. Not wrong per se — **wrong if undeclared** or applied inconsistently between explicit period and terminal value. |
| **Terminal year normalisation** | Terminal year carries a one-off (a working-capital release, a tax holiday, a peak-capex trough) | Capitalises a transient into perpetuity. Small error, enormous consequence. |
| **Formula consistency across columns** | Row breaks pattern at one column | Usually a manual override someone forgot. |

**Reviewer test:** change one revenue driver by 10% and confirm every dependent
line moves. Anything that does not move is either hardcoded or disconnected.

---

## 2. Terminal value — where DCFs are usually decided

Compute **TV as a share of enterprise value**. Then state it out loud.

| TV share of EV | Reading |
|---|---|
| < 50% | Explicit forecast is doing the work |
| 50–75% | Normal for a growing asset; scrutinise g and the normalisation |
| **> 75%** | **The "DCF" is a terminal-value estimate with a forecast attached.** Say so plainly. Diligence effort should shift to the perpetuity assumption. |
| > 90% | The explicit forecast is decoration. Do not present this as a DCF-supported value. |

**Perpetuity growth (g) discipline:**

- **g cannot exceed long-run nominal GDP growth** of the operating economy in
  perpetuity — an asset growing faster forever eventually *becomes* the economy.
  State the nominal GDP anchor used and its source.
- **g must be nominal if cash flows are nominal.** A "conservative" real g of 2%
  silently applied to nominal cash flows understates value; the reverse
  overstates it. Name the convention.
- **The g/WACC spread is the real driver.** TV ∝ 1/(WACC − g). At WACC 10%,
  moving g from 2% → 3% raises TV by ~14%. Moving 3% → 4% raises it another ~17%.
  **Sensitivity to g is not linear** — it accelerates as g approaches WACC. Any
  spread under ~4 points deserves explicit defence.
- **Cross-check with an exit multiple.** If perpetuity-g TV and exit-multiple TV
  disagree by more than ~20%, one of them encodes an assumption nobody has stated.
  Reconcile; do not average.

**Terminal-year internal consistency** — the check most often skipped:

- If **g > 0** in perpetuity, the asset base must grow, so **terminal capex must
  exceed terminal depreciation**. Capex ≈ D&A with g = 3% is arithmetically
  incoherent: it grows output forever from a shrinking real asset base.
  A defensible first approximation: `capex/D&A ≈ 1 + g/(depreciation rate)`.
- **Terminal working capital must scale with revenue.** A terminal year with zero
  working-capital investment but positive growth is free financing from nowhere.
- **Terminal margin must be defensible against competition.** Perpetual
  above-industry margin is a claim about a perpetual moat. Make it a stated claim.

---

## 3. Discount rate — and the double-count that hides in it

| Check | Failure signature |
|---|---|
| **FCFF ↔ WACC, FCFE ↔ Ke** | Unlevered cash flows discounted at cost of equity, or levered at WACC. Fatal and common. |
| **Nominal ↔ nominal, real ↔ real** | Nominal cash flows at a real rate inflates value by roughly the inflation rate, compounding. |
| **Currency consistency** | IDR cash flows discounted at a USD rate. Either discount IDR at an IDR rate, or convert at the **forward curve** (interest-rate parity) and discount at USD. Converting at spot and discounting at USD double-counts the differential. |
| **Country risk premium double-count** | **CRP added to the discount rate *and* the same risk modelled in downside cash flows.** Penalises the asset twice, then gets called "conservative". Pick one channel and say which. |
| **Beta provenance** | Comparable set, unlevering formula, target vs current capital structure, and measurement window all stated? A beta with no stated derivation is an opinion with a decimal point. |
| **Target capital structure** | WACC weights at target structure but debt schedule at current, with no path between |
| **Risk-free tenor** | Short-tenor risk-free against a long-lived asset |

> **The Danantara-specific failure.** The tempting way to reflect *national
> consequence* in a DCF is to nudge WACC down (strategic asset, so cheaper
> capital) or nudge g up (national priority, so faster growth). **Both are
> prohibited.** Every SKILL.md in this package forbids collapsing commercial
> return and national impact into an opaque single score — and a discount-rate
> fudge is exactly that score, made invisible.
>
> Keep the DCF **commercial and honest**, and let the national consequence appear
> as a **separate, quantified, visible** item for `dual-mandate-balancer`. If the
> commercial case only clears the hurdle after an unexplained 150bp WACC
> reduction, the finding is *"commercial case does not clear on its own merits"* —
> which is decision-relevant information, not a modelling inconvenience.

---

## 4. Cash flow construction

- **Revenue build**: price × volume, with each independently evidenced. A revenue
  CAGR assumed directly is not a build — it is the conclusion in the input cell.
- **Optimism bias**: compare the forecast to the asset's own history and to a
  reference class of comparable projects. Forecasts that show an immediate
  inflection at t=0 after a flat history need a mechanism, not an explanation.
- **Margin path**: expansion must have a named cause (scale, mix, pricing power,
  cost programme) with a cost of achieving it in the model. Margin expansion with
  no corresponding capex or opex is a wish.
- **Tax**: marginal vs effective rate; NOL carry-forwards and their expiry;
  incentive holidays and their **end date** — a holiday that never expires in the
  model is a permanent subsidy nobody approved. Do not double-count the interest
  tax shield in both FCFF and WACC.
- **Working capital**: driven off revenue/COGS with stated days; check the
  terminal-year reversal.
- **Capex**: maintenance separated from growth. Only growth capex should
  accompany growth.
- **Value bridge**: EV → equity value. Net debt at the right date, minorities,
  associates, pensions, provisions, options/dilution, and any leakage. The bridge
  is where a defensible EV quietly becomes an indefensible equity price.

---

## 5. Scenarios — sensitivity is not risk analysis

**A ±10% sensitivity table is not a downside case.** It shows model mechanics, not
the world. It moves one variable while holding correlated variables fixed —
precisely the correlation that hurts in a real downturn (volume falls *and*
price falls *and* working capital builds *and* refinancing tightens, together).

Require instead:

- **A coherent downside**: a named scenario with correlated movements and a
  mechanism, not a haircut.
- **A break-even analysis**: what must be true for value to equal price? Then ask
  whether *that* is plausible. This reframes "is the model right" into "what does
  this price require" — a far harder question to fudge.
- **Bounded permanent loss**: capital is **state capital** (UU 1/2025 jo.
  UU 16/2025, Pasal 3G — capital from *penyertaan modal negara*). Downside that
  cannot be bounded is an escalation trigger, not a probability-weighted line item.
- **Asymmetry stated**: probability-weighting a permanent loss against an upside
  hides that the two are not symmetric for a state investor.

---

## 6. Output of a challenge

Produce a **challenge finding**, never a re-run model:

1. **Structural defects** — with cell references, and whether each is fatal.
2. **TV share of EV**, and whether the model is a DCF or a TV guess.
3. **The two or three assumptions that actually drive the answer**, isolated.
4. **Break-even**: what must be true to justify the price.
5. **Double-counts or inconsistencies**, named.
6. **Any national-consequence assumption smuggled into WACC or g**, extracted and
   handed to `dual-mandate-balancer` as a separate visible item.
7. **Verdict**: can this model bear the decision? *Fit / fit with conditions /
   not fit.* "Not fit" is a legitimate and useful answer.

**A challenge that finds nothing is itself a finding** — it usually means the
challenge was run at the wrong altitude, not that the model is sound.
