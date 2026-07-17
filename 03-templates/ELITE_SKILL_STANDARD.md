# The Elite Skill Standard

What separates a top-decile skill from a top-percentile one. This is the quality
bar for `04-skills/`; `SKILL_TEMPLATE.md` gives the shape, this gives the
substance.

---

## 0. The thesis

**A skill is not a document. It is a decision procedure.**

The test of a skill is not whether it is complete, well-structured, or
governance-compliant. It is whether the skill **can reach a conclusion that
surprises the person who invoked it**.

A skill that can only agree is decoration. It costs tokens, produces prose,
launders a decision that was already made, and adds an audit trail suggesting
challenge occurred. That is worse than no skill: it manufactures assurance.

Measure a skill by one question:

> **What does this skill say NO to, and how would it know?**

If there is no answer, the skill is not ready, regardless of how many required
headings it has.

### Why this package needs the bar stated explicitly

The 2026-07-16 audit measured the estate:

| Metric | Finding |
|---|---|
| Distinct workflows across 133 skills | **17** |
| Skills with a workflow of their own | **7 / 133** |
| Largest shared workflow | **21 skills** |
| Byte-identical `## Prohibited actions` | **128 / 133** |
| `## Objective` copied verbatim from `description` | **106 / 133** |
| Reference files in 133 `references/` directories | **0** |

Every one of those passed `validate_skills.py`, because that validator checks
that sections *exist*, not that they contain anything. **A green build is not
evidence of quality.** It never was.

The failure was not laziness. It was generating 133 skills from ~17 procedure
templates and letting the *description* carry the differentiation. Descriptions
are good (0 high-collision pairs at >0.5 Jaccard). The methods underneath are not
there. `investment-mandate-interpreter` and `dcf-model-challenger` both shipped
with the workflow *"Develop or test the investment thesis using independent
commercial, financial, legal, technical, ESG, integrity, and sector evidence"* —
the wrong method for both.

---

## 1. Discriminating tests, not instructions

**The single highest-leverage property.** An instruction cannot fail. A test can.

| Instruction (generic) | Discriminating test (elite) |
|---|---|
| "Consider terminal value carefully" | "Compute TV/EV. Above 75%, this is a terminal-value estimate with a forecast attached — say so and shift diligence to the perpetuity assumption." |
| "Check the discount rate is reasonable" | "Is country risk in both the rate *and* the downside cash flows? That is a double-count called conservatism. Name one channel." |
| "Ensure growth is conservative" | "Is terminal capex > terminal D&A whenever g > 0? If not, the model grows output forever from a shrinking asset base." |
| "Verify the mandate" | "Does the Tier 1 chain reach this action? Pasal 3E delegates *sebagian* — a part. Outside that part is not Danantara's, however attractive." |
| "Assess conflicts of interest" | "Is the approver barred by the concurrent-position prohibition (UU 16/2025)? An invalid approver voids the approval, not just the optics." |

A discriminating test has three parts:

1. **A computable or checkable condition** — a threshold, a comparison, a
   presence check. Not a mood.
2. **A stated consequence** — what changes when it fails. If nothing changes, the
   test is theatre.
3. **A defensible boundary** — *why* 75% and not 60%. State the reasoning or the
   source. An unexplained threshold is an invented one, which this package
   prohibits.

**Minimum bar: every skill has at least three discriminating tests, at least one
of which can produce a negative verdict on its own.**

> **The reviewer's question:** "Show me an input where this skill returns a
> different answer than the person asking wanted." If you cannot construct one,
> the skill is decoration.

---

## 2. A verdict vocabulary, not prose

Elite skills conclude. They do not narrate.

Every skill declares a **small, fixed set of verdicts**, and the honest
`cannot answer` is always one of them:

- `dcf-model-challenger` → **fit / fit with conditions / not fit**
- `investment-mandate-interpreter` → **within mandate / outside mandate /
  indeterminate pending named document**

Why this matters more than it looks: **prose hides indecision.** "There are some
concerns around the terminal value assumption, though the overall case remains
broadly supportable subject to further work" is a sentence that survives any
outcome. It is unfalsifiable, and therefore unaccountable — precisely what an
audit trail must not contain when BPK is the statutory reader (UU 16/2025).

**`indeterminate` is a first-class verdict, not a failure.** A skill that never
returns it is either omniscient or dishonest. Given Tier 2 is currently empty,
`indeterminate` is the *correct* answer to most real mandate questions today.

---

## 3. Named failure modes — the skill's own

**Elite skills know how they get fooled.** Each skill names the specific ways it
produces a confidently wrong answer, and what to do instead.

This is the property most often missing, because it requires admitting the skill
is fallible — the opposite of how capability is usually marketed.

Generic: *"Be aware of bias."*

Elite (from `investment-mandate-interpreter`):

| Failure | Why it happens | Correct behaviour |
|---|---|---|
| Citing UU 1/2025 alone | It is the famous one and the founding text | Cite `UU 1/2025 jo. UU 16/2025`. The base text is not the operative text. |
| Inferring an approval threshold | The charter is missing and a number is needed to finish | Escalate. **A plausible invented threshold is worse than an absent one: it is wrong *and* unchallenged.** |
| Reading "strategic national interest" as mandate | Political framing arrives with urgency | A label is not a delegation. Require the instrument. |

Note the middle column. **"Why it happens" is the load-bearing part** — it names
the *pressure*, not the mistake. Skills fail under pressure, and the pressure is
usually a deadline, a senior stakeholder, or a missing document that someone
needs filled *now*. A failure mode without its pressure is a warning nobody heeds.

**Minimum bar: at least three named failure modes, each with its pressure and its
correct behaviour.**

---

## 4. Falsification hooks — state what would change the answer

Before concluding, an elite skill states **what evidence would reverse it**. Up
front, not when challenged.

- "This verdict flips to *not fit* if the terminal capex/D&A ratio cannot be
  defended at g = 3%."
- "This becomes *within mandate* the moment DOA-04 supplies a threshold above
  USD 200m with an effective date after 6 Oct 2025."

This does three things at once: it makes the reasoning auditable, it tells the
human exactly what to go get, and it makes the skill **cheap to overturn with
evidence and expensive to overturn with pressure** — which is the entire point of
the governance kernel.

---

## 5. Honest degradation — name the missing cell

**Never "consult the relevant policy."** That is a skill admitting it does not
know what it needs.

When a required input is missing, an elite skill names:

1. **the exact document or workbook cell** — `05_DECISION_RIGHTS_DOA`, row
   `DOA-04`, column `Financial / Risk Threshold`;
2. **the question it would answer** — "may DIM approve USD 200m alone?";
3. **the named owner** — from `15_SKILL_RACI`, column `Business Accountable (A)`;
4. **what the skill can still say without it** — partial answers are valuable;
   silence is not.

This is what makes the *Actual Condition Input Workbook* operational rather than
an archive. A skill that says *"indeterminate — need DOA-04 threshold, owner
[named], and the question is whether DIM may approve alone"* converts a gap into
a work item with an owner. A skill that says *"consult the DoA"* converts it into
nothing.

**The workbook is the Tier 2 source. Skills must cite its IDs (`ENT-xx`,
`DOA-xx`, `COM-xx`, `POL-xx`) the way they cite `UU 16/2025` — with clause,
effective date, and evidence link.** A workbook cell without `Clause / Page` and
`Effective Date` is not a source; it is a claim.

---

## 6. Method that belongs to this skill alone

**If two skills can share a workflow, one of them does not exist.**

This is not a style rule. It is the defect that produced 17 workflows for 133
skills. A shared workflow means the differentiation lives entirely in the
description — which means routing works and reasoning does not. The user gets the
right skill and the wrong method.

Test: **read the workflow with the title covered. Can you name the skill?** If
not, it is a cluster-level procedure wearing a skill's name.

Consequences of failing this test, in order of preference:

1. **Give the skill its real method.** Usually the right answer, and usually
   reveals the skill is more specific than its description suggested.
2. **Merge it** into the skill it duplicates.
3. **Delete it.** 133 is a count, not an achievement. A merged pair that reasons
   well beats two that share a procedure.

The governance *kernel* is meant to be shared — constitution, prohibitions,
escalation. The **method** is not.

---

## 7. Altitude — operate where you can be wrong

A skill must work at the altitude where its answer could be wrong, and stop
there.

- Too high: "ensure robust governance" — unfalsifiable, therefore useless.
- Too low: re-deriving WACC from first principles when the question is whether TV
  dominates — precise about the wrong thing.
- Right: "TV is 82% of EV; the explicit forecast is decoration; the decision rests
  on a perpetuity assumption nobody has defended."

**Symptom of wrong altitude: a challenge that never finds anything.** That is
almost never a sound model — it is a challenge run where the answer was already
safe.

---

## 8. What this standard does NOT ask for

Guarding against the failure mode of standards themselves — that they get
satisfied by addition.

- **Not more sections.** The 133 skills already have 14 headings each. Sections
  were never the constraint.
- **Not more words.** Average SKILL.md is ~779 words and says little. A 400-word
  skill with three real tests beats a 1,200-word skill with none.
- **Not more skills.** See §6.
- **Not more hedging.** "May", "consider", "where appropriate" are how a skill
  avoids being wrong by avoiding being anything.
- **Not novel governance language.** The kernel is settled. Do not paraphrase it
  per-skill; that is how 128 identical blocks drift into 128 subtly different ones.

---

## 9. Acceptance checklist

A skill meets this standard when **all** hold:

- [ ] **≥3 discriminating tests**, each with a threshold/condition, a stated
      consequence, and a defensible boundary
- [ ] **≥1 test can produce a negative verdict alone**
- [ ] **A fixed verdict vocabulary**, including an honest `indeterminate`
- [ ] **≥3 named failure modes**, each with its *pressure* and correct behaviour
- [ ] **Falsification hooks** — what would change the verdict, stated up front
- [ ] **Honest degradation** — missing inputs named to document/cell/row + owner +
      the question they answer
- [ ] **A method no other skill shares** (§6 test: title covered, still nameable)
- [ ] **Correct altitude** — could be wrong, and says how
- [ ] **A worked example** in `references/` a reviewer can check the skill against
- [ ] **Trigger cases in Indonesian and English**, phrased as a user would type,
      with governance tests asserting a *specific* refusal
- [ ] Registry description **byte-identical** (the validator compares exactly)

### What CI can and cannot check

`06-scripts/check_skill_depth.py` enforces the mechanically checkable subset:
workflow uniqueness (§6), `Objective` ≠ `description`, and the presence of a
verdict vocabulary and failure-mode section. It runs as a **ratchet**: floors rise
as skills are deepened and are never lowered to make a build go green.

**It cannot check whether a test is discriminating, whether a boundary is
defensible, or whether the method is right.** Those need a reviewer who knows the
domain. CI catches regression; it does not confer quality. Anyone who reads a
green build as "the skills are good" has repeated the exact mistake that produced
17 workflows for 133 skills.
