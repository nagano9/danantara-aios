---
name: dcf-model-challenger
description: Challenges cash-flow logic, forecast drivers, terminal value, discount rate, inflation, currency, tax, capex, working capital, scenarios, and model integrity. Use before relying on a DCF for valuation or capital allocation.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: DIM/DAM/DDMF
  cluster: 06-dim-investment-management
  risk-tier: critical
  version: "1.1.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# DCF Model Challenger

## Objective
Determine whether a DCF can bear the weight of the decision being placed on it.
A DCF is not a valuation; it is an arithmetic consequence of its assumptions.
This skill challenges those assumptions and the structure that converts them into
a number. It does not re-run the model more carefully — a model that is
internally consistent and externally wrong passes every recalculation and still
destroys state capital.

Full method: `references/dcf-challenge-protocol.md`.

## Use when
- Before a DCF informs a valuation, capital allocation, IC recommendation, or
  impairment.
- When terminal value dominates and nobody has said so.
- When a model clears the hurdle rate only narrowly, or only after a recent
  assumption change.
- When the same model is reused across assets with different economics.
- When a sensitivity table is being presented as risk analysis.

## Do not use when
- No DCF exists, or valuation method selection is still open — that is
  `valuation-orchestrator`.
- The question is the strategic case, not the arithmetic — that is
  `investment-thesis-builder` or `investment-thesis-red-team`.
- The question is whether DIM may act at all — that is
  `investment-mandate-interpreter`. **Never challenge a model into existence for
  an action that is outside mandate.**

Do not use this skill to bypass a competent authority, replace licensed or
accountable professional judgment, process unauthorized information, or make an
institutional commitment. Route unrelated requests to `intent-and-entity-router`.

## Required inputs
- **The live model**, with formulas intact. A PDF of outputs cannot be challenged;
  structural defects live in the formulas.
- The stated **valuation date, currency, and nominal/real convention**.
- The **cash-flow definition used** (FCFF or FCFE) and the discount rate applied.
- The **derivation of WACC or Ke** — beta source, comparable set, unlevering
  method, capital structure, risk-free tenor, any country risk premium.
- **Terminal value method** and its inputs.
- The **price or valuation being tested**, and the decision it supports.

If formulas are unavailable, that is the first finding: the model is unauditable
and cannot support a critical-tier decision.

## Dependencies
- `valuation-orchestrator` — selects method; this skill challenges the result.
- `financial-due-diligence` — supplies the historical base the forecast departs
  from.
- `risk-adjusted-return-analyzer` — receives the challenged output.
- `dual-mandate-balancer` — receives any national-consequence assumption this
  skill extracts from WACC or g.
- `investment-thesis-red-team` — challenges the narrative; this challenges the
  arithmetic.

## Authoritative sources
1. **Applicable law, regulation, official decision, and formal mandate.**
   Capital is **state capital**: UU 1/2025 jo. UU 16/2025, Pasal 3G — the Badan's
   capital derives from *penyertaan modal negara* and/or other sources. This is
   why unbounded downside escalates rather than being probability-weighted away.
2. **Effective Danantara valuation policy and model-approval standard.**
   **Currently unavailable** — see `08-sources/SOURCE_REGISTER.md` Tier 2. Absent
   an approved standard, this skill applies the protocol in
   `references/dcf-challenge-protocol.md` and states that it is doing so. It does
   **not** invent a hurdle rate, an approved WACC, or a house view on terminal
   growth.
3. Audited or owner-certified internal data and primary transaction documents;
   the historical accounts the forecast must reconcile to.
4. Independent external evidence: comparable transactions, sector benchmarks,
   long-run nominal GDP for the perpetuity anchor, observable forward curves.
5. Prior decisions and precedents only as context. **A WACC carried over from a
   prior deal is not evidence** — it is an unexamined assumption with a history.

Record source owner, title, version, effective date, retrieval date,
classification, and exact location. Resolve discrepancies through
`source-hierarchy-resolver`.

## Workflow
Structure before inputs, inputs before output. Debating WACC to two decimals in a
model with a circular reference is wasted effort.

1. **Establish auditability.** Formulas intact? Valuation date, currency,
   nominal/real convention, FCFF/FCFE all stated? If not, stop and report.
2. **Test structural integrity.** Hardcodes inside formulas, circularity, sign
   conventions, period alignment, mid-year convention, terminal-year
   normalisation, column consistency. **Reviewer test:** move one revenue driver
   10% and confirm every dependent line responds. Anything static is hardcoded or
   disconnected.
3. **Compute TV as a share of EV, and say it out loud.** Above ~75%, this is a
   terminal-value estimate with a forecast attached; shift diligence accordingly.
   Test g against long-run nominal GDP, confirm the nominal/real convention, and
   check terminal capex > terminal D&A whenever g > 0.
4. **Test the discount rate.** FCFF↔WACC / FCFE↔Ke; nominal↔nominal;
   currency handled via forward curve rather than spot; **country risk premium not
   counted in both the rate and the cash flows**; beta provenance stated.
5. **Test the cash-flow build.** Price × volume rather than an assumed CAGR;
   forecast against the asset's own history and a reference class; margin
   expansion with a named cause and its cost; tax holidays with an end date;
   working-capital reversal; maintenance capex separated from growth; the EV →
   equity bridge.
6. **Extract any national-consequence assumption** embedded in WACC or g. Hand it
   to `dual-mandate-balancer` as a separate visible item. Never leave it inside
   the rate.
7. **Replace sensitivity with scenario.** Require a coherent correlated downside,
   a break-even ("what must be true for value to equal price?"), and a bounded
   permanent loss.
8. **Issue a verdict**: fit / fit with conditions / not fit for this decision.

## Danantara Way decision rules
- A DCF is an argument, not a measurement. Challenge the argument.
- **Do not reflect national consequence in WACC or terminal growth.** Every skill
  in this package prohibits collapsing commercial return and national impact into
  an opaque single score; a discount-rate fudge is exactly that score made
  invisible. Keep the DCF commercial and honest; surface impact separately.
- If the commercial case clears only after an unexplained rate reduction, the
  finding is *"does not clear on its own merits"* — decision-relevant, not a
  modelling inconvenience.
- Capital is state capital. **Permanent loss is asymmetric** and is not disposed
  of by probability-weighting it against upside.
- Quantify downside, permanent-loss risk, opportunity cost, reversibility, and the
  conditions that would change the recommendation.
- Prefer evidence, scenarios, benchmarks, and traceable calculations over
  narrative assertion.
- Treat transformation capital as conditional; prohibit unsupported bailout,
  evergreen support, and sunk-cost justification.
- State assumptions, confidence, data gaps, dissent, and unresolved tensions
  explicitly.

## Output contract
Primary output: **a challenge finding**, never a re-run model —

- structural defects, with cell references, each marked fatal or not;
- **TV as a share of EV**, and whether this is a DCF or a TV guess;
- the two or three assumptions that actually drive the answer, isolated;
- break-even: what must be true to justify the price;
- double-counts and inconsistencies, named;
- any national-consequence assumption extracted from WACC or g, handed onward;
- **verdict**: fit / fit with conditions / not fit for the decision at hand.

A challenge that finds nothing is itself a finding — it usually means the
challenge ran at the wrong altitude.

Use `CANONICAL_OUTPUT_CONTRACT.md` for material outputs. Clearly label the result
as AI-assisted analysis or draft until the required human authority has approved
it.

## Human approval
Investment team and committee; valuation or model-risk owner where one is named.
The skill may analyze, challenge, draft, calculate, and recommend. It may not
execute, bind, disclose, waive, appoint, dismiss, allocate capital, or record
final approval unless a separate authorized system provides verified evidence of
that human action.

It may not certify a model as approved, and it may not substitute for an
independent model-risk review where policy requires one.

## Escalation
Stop and escalate when authority is missing, evidence is materially inadequate,
conflicts are unresolved, legal basis is doubtful, downside cannot be bounded,
data use is unauthorized, material sources conflict, an exception is requested, or
the recommendation depends on an unapproved subsidy or informal direction.

Specific to this skill — escalate when:
- **downside cannot be bounded** (state capital; permanent loss);
- formulas are withheld and a critical-tier decision depends on the model;
- **removal or weakening of a downside case is requested** (see
  `ADVERSARIAL_CASES.yaml` → `optimistic-model`);
- an assumption changes materially with no evidentiary basis, in the direction
  that saves the deal;
- national consequence is being routed through the discount rate after challenge;
- TV exceeds ~90% of EV and the result is still presented as DCF-supported.

## Prohibited actions
- Do not make, imply, fabricate, or backdate institutional approval.
- Do not bypass formal decision rights, required human review, recusal, legal,
  risk, compliance, or information-security controls.
- Do not invent facts, sources, policy, authority, financial results, valuation
  inputs, or certainty. **This includes inventing a hurdle rate, house WACC, or
  approved terminal growth where no Danantara valuation policy exists.**
- **Do not remove, weaken, or bury a downside case**, whatever the reason offered.
- **Do not adjust WACC or g to reflect strategic or national importance.**
- Do not present a sensitivity table as risk analysis.
- Do not disclose or process information outside its authorized classification,
  purpose, users, tools, systems, or jurisdiction.
- Do not describe unsupported political direction, informal instruction, or
  strategic labeling as sufficient investment rationale.
- Do not collapse commercial return and national impact into an opaque single
  score.

## Quality checks
- Name, description, and output comply with the skill schema and canonical output
  contract.
- TV share of EV is computed and stated explicitly.
- Nominal/real, FCFF/FCFE, and currency conventions are each verified, not assumed.
- Country risk is counted once, and the channel is named.
- Terminal-year capex/D&A is consistent with terminal growth.
- Material claims have traceable sources and clear fact/assumption/inference
  labels.
- Calculations, units, dates, currencies, and scenarios are internally consistent.
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

Specific to this skill: record the **model version and hash challenged**, each
assumption as received, every change requested during challenge and **who
requested it**, and any pressure to weaken a downside case. Under UU 16/2025, BUMN
financial examination sits with **BPK** — this record has a statutory external
reader.
