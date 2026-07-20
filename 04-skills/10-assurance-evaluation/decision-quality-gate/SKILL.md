---
name: decision-quality-gate
description: Applies mandatory commercial, strategic, governance, impact, execution, evidence, downside, authority, long-term, and auditability tests before a material recommendation proceeds. Use as the final pre-decision assurance gate.
license: Proprietary-Danantara
compatibility: Claude Agent Skills in an approved Danantara environment; use only authorized data, repositories, models, connectors, and tools.
metadata:
  owner: BPI/DAM/DIM/DDMF
  cluster: 10-assurance-evaluation
  risk-tier: critical
  version: "1.0.0"
  status: draft
  review-cycle: annual-or-on-material-change
  tool-policy: least-privilege
---

# Decision Quality Gate

## Objective
Provide the final independent assurance gate before a material Danantara recommendation reaches the competent human authority.

**This gate runs last, which is a structural weakness, not a strength.** By the time it executes, the diligence is complete, the memo is written, the committee is booked, and the sponsor has told people it is happening. `RETURN` sends all of that backwards. It is therefore under more pressure than any other control in the estate, not because it is weaker, but because of where it sits.

Two consequences follow, and both are load-bearing:

- A gate that never returns `RETURN` is not a gate. It monitors its own verdict distribution.
- This is the last point at which a prediction can still be required. Without one, `post-decision-learning` returns `unlearnable` forever and nothing downstream can fix it.

Full method: `references/decision-quality-protocol.md`.

## Use when
- The decision is material and about to reach a human authority.
- A recommendation needs the final assurance check on commercial, strategic, governance, impact, execution, and auditability.
- The pack must prove that downside is bounded, dissent is captured, and a falsifiable prediction exists.
- The user asks whether a decision is ready to proceed, return, stop, or escalate.

## Do not use when
Do not treat a pass as institutional approval. The gate evaluates decision quality and control completeness; the competent human body still decides.

## Required inputs
Complete decision artifact; evidence register; models; assumptions; alternatives; risk register; conflict declarations; independent challenge; legal and policy review; authority map; approval route; conditions; monitoring plan.

## Authoritative sources
Start with `references/repo-quality-source-map.md` for the repo-native assurance hierarchy.
Applicable law and policy; formal mandate and delegation; primary evidence; validated models; approved risk appetite; independent specialist reviews; Danantara Way; canonical output contract.

If the pack does not separate the four findings, or does not include a dated prediction with a named `Risk Owner`, treat it as incomplete and return it.

## Workflow
1. Verify the decision requested, authority, process stage, and completeness of the record.
2. Test commercial logic, valuation, risk-adjusted return, capital preservation, and downside.
3. Test strategic-national interest, measurable impact, additionality, resilience, capability, and sovereignty.
4. Test governance, integrity, conflicts, transparency, confidentiality, decision rights, and audit trail.
5. Test alternatives, counterfactual, scenario coverage, reversibility, opportunity cost, and long-term value.
6. Verify independent challenge, dissent, model validation, legal sufficiency, and source traceability.
7. Assess execution readiness, owners, milestones, conditions, risk triggers, and consequences.
8. Require the prediction. Is a falsifiable, dated predicted outcome recorded, with a trigger that would show the thesis wrong, a post-decision review date, and a named `Risk Owner` to settle it? Source it from the deciding skills' falsification hooks. No prediction means `RETURN`, never `CONDITIONAL PASS`.
9. Apply the ultimate test four times separately and issue the verdict.
10. If any finding is blended, missing, or unsupported, return the pack instead of laundering it into a single score.

## Verdicts
| Verdict | Meaning |
|---|---|
| `PASS` | All four dimensions answered separately; prediction recorded; downside bounded. |
| `CONDITIONAL PASS` | Proceeds with conditions that each have an owner, a date, and a way to fail. |
| `RETURN` | Sent back. Blended score, missing prediction, unnamed risk owner, or unevidenced unanimity. |
| `STOP` | Downside cannot be bounded, or a stop condition is met. Not a monitoring condition. |
| `ESCALATE` | Cannot be resolved at this altitude. |

The ultimate test is four tests, never one score. `20_DECISION_LOG` carries `Commercial Finding` (13), `Strategic / National Finding` (14), `Governance Finding` (15), and `Intergenerational Finding` (16) as separate columns, and sheet 20's own rule requires them presented separately.

> A decision that fails one dimension is not a decision that scored 75%. It is a decision with a named failure that a human must decide to accept, in the open, with their name on it. Averaging removes the human's opportunity to refuse.

**A blended score is `RETURN` on its own.** The blending is the defect; the underlying deal may be fine.

## Failure modes
The middle column is load-bearing: this gate fails under pressure, not from ignorance, and it sits where the pressure is highest.

| Failure | The pressure that causes it | Correct behaviour |
|---|---|---|
| Gate capture | The work is done, the committee is booked, `RETURN` costs weeks | Position creates the pressure; it does not change the standard. Monitor the gate's own pass rate. |
| `CONDITIONAL PASS` as a soft `RETURN` | It lets everyone move while looking rigorous | A condition needs an owner, a date, and a way to fail. |
| Accepting a blended score | The committee asked for one number | Blending is `RETURN`. Four findings, four verdicts. |
| Passing without a prediction | Nobody has ever been asked for one | `RETURN`. After the decision it is hindsight; nothing downstream can fix it. |
| Reading empty dissent as consensus | The field is blank and the pack looks clean | Unanimity on a material decision is a claim requiring evidence, not a default. |
| Accepting a challenge that found nothing | The model is polished and the team is credible | Almost always the wrong altitude, not a sound proposal. |
| Monitoring an unbounded downside | `STOP` is drastic and the deal is attractive | State capital. Unbounded is `STOP`, not a condition. |
| Running after socialisation | The sponsor announced it; the gate is now a formality | Escalate: it ran too late to be a gate. |
| Treating its own `PASS` as approval | It is the last check before the human | A quality verdict is not an authority verdict. |

## Falsification hooks
- `PASS` becomes `RETURN` if the four findings turn out to have been blended into a composite anywhere in the pack.
- `CONDITIONAL PASS` becomes `RETURN` if any condition lacks an owner, a date, or a way to fail.
- `PASS` becomes `STOP` if the recorded `Downside / Max Loss` is shown to be unbounded rather than merely large.
- This gate's own verdicts are suspect if its pass rate is 100% across 20 material decisions while no upstream skill has been revised.

## Danantara Way decision rules
A material recommendation cannot pass if:
- authority or legal basis is absent
- material evidence is fabricated, stale without justification, or irreconcilably inconsistent
- conflicts or hidden beneficiaries are unresolved
- downside or permanent-loss risk is not bounded
- commercial weakness is concealed by strategic language
- national impact lacks measurable outcomes and attribution
- transformation capital lacks conditionality and exit criteria
- confidentiality is used to avoid accountability
- independent challenge is absent or not independent
- execution ownership, conditions, and monitoring are missing

## Output contract
Return:
- gate result and severity
- blocking findings
- conditional findings and remediation
- commercial, strategic, governance, intergenerational test results
- authority and approval completeness
- evidence and model assurance
- dissent and unresolved tensions
- recommendation to proceed, return, stop, or escalate
- audit reference
- prediction status, review date, and named Risk Owner

## Human approval
The independent assurance owner signs the gate result; the competent authority makes the decision. AI may not approve, waive findings, or mark remediation complete without verified evidence.

The gate may not be converted into a soft endorsement. `PASS` means the pack is ready for human decision, not that the decision is approved.

## Escalation
Immediately escalate suspected illegality, corruption, hidden beneficiary, material misstatement, data breach, sanctions concern, market abuse, authority bypass, or attempted suppression of dissent.
Escalate `STOP` when downside cannot be bounded or when the pack tries to hide a critical issue behind a condition.

## Prohibited actions
- Do not downgrade findings to meet a deadline.
- Do not accept "strategic" or "sesuai arahan" as sufficient evidence.
- Do not close findings based only on sponsor assurance.
- Do not remove downside or dissent from the final record.
- Do not fabricate approval or remediation evidence.
- Do not average the four findings into a single score.
- Do not accept a missing prediction as a condition to add later.

## Quality checks
- Reviewer independence is documented.
- Every canonical output field is present or justified as not applicable.
- All blockers have owners and objective closure evidence.
- The result is reproducible from the audit record.
- Commercial, strategic, governance, and intergenerational tests are separate.
- Final status is consistent with finding severity.

## Audit record
Retain artifact versions, evidence, models, reviewer identity, independence declaration, tests performed, findings, sponsor responses, remediation evidence, gate status, escalation, human decision, and subsequent outcomes.
