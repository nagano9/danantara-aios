# Skill change protocol

Method reference for `skill-lifecycle-governor`. Closes Arc 2 of the learning loop
(`post-decision-learning` → `references/learning-loop-protocol.md` §3): the arc
where a refuted prediction becomes a changed skill.

---

## 0. The premise

> **A change to a critical skill is a policy change, executed by editing a
> markdown file.**

`dcf-model-challenger` says a DCF whose terminal value exceeds ~75% of enterprise
value is a terminal-value guess with a forecast attached. Move that number to 85%
and deals that would have been challenged now pass. Nothing else changed: no
committee met, no delegation was amended, no policy was reissued. One threshold
moved in a text file, and the institution's revealed risk appetite moved with it.

This is why `skill-lifecycle-governor` is critical-tier. It is not release
management. **It is the control that stops a governance change from happening by
accident, in a pull request, at the altitude of a typo fix.**

The test for any proposed change:

> **Would this change what gets approved? If yes, it is a policy change and it
> needs an owner with the authority to make one.**

---

## 1. Version pinning — a skill change rewrites the past

Every skill carries `metadata.version`. **No skill currently pins that version to
the decision it gated.** That is a defect with a statutory reader.

Consider the sequence:

```
2026-03  dcf-model-challenger v1.1  — TV/EV > 75% -> challenge
2026-03  DEC-014 assessed: TV/EV 80%  -> verdict `not fit`  -> deal rejected
2026-09  dcf-model-challenger v2.0  — threshold moved to 85%
2027-02  BPK examines DEC-014
```

The examiner reads the current method and the old decision. Under v2.0, TV/EV of
80% is unremarkable — so DEC-014 looks like a deal rejected for no reason. Or,
worse, run it the other way: a deal **passed** at 80% under a v2.0 that did not
exist when it was passed, and the record cannot show which method applied.

**Neither the decision nor the skill is wrong. The record is unreadable.**

Therefore:

| Rule | Consequence |
|---|---|
| Every audit record cites the **skill name + version + content hash** that produced it | A decision can be read against the method that actually applied |
| A skill version is **immutable once it has gated a decision** | Editing v1.1 in place retroactively rewrites what past decisions meant |
| Superseding is a **new version**, never an edit to the old one | The old one must remain retrievable for as long as its decisions are auditable |
| A version bump requires a **changelog entry naming what a reader of the old record must know** | "Improved wording" is not a changelog |

Under UU 16/2025, BUMN financial examination sits with **BPK**. "We changed the
method at some point and no longer know which one applied" is not an answer
available to this institution.

---

## 2. Change classes — not all edits are equal

| Class | Examples | Requires |
|---|---|---|
| **Editorial** | typo, formatting, clearer sentence with identical meaning | AI Product Owner; no version bump |
| **Method** | new discriminating test, changed workflow step, new failure mode | version bump + `skill-evaluation-runner` + AI Product Owner |
| **Threshold** | **75% → 85%; any number that gates a verdict** | **policy owner with authority to change risk appetite** + evidence + regression + recorded approval |
| **Governance** | prohibitions, escalation, human-approval boundary, verdict vocabulary | **AI Governance Committee**; propagation review (§3) |
| **Estate** | new skill, merge, deprecate, delete | Governance Committee + registry + workflow-chain update |

**The dangerous class is Threshold**, because it looks editorial. It is one
character. It arrives as "we've been too conservative", usually attached to a live
deal, usually with a deadline. It changes what the institution approves.

**A threshold change may never be justified by a single outcome.** One refuted
prediction is one sample (`post-decision-learning` §5). Patterns change controls;
anecdotes do not. If the evidence for moving a threshold is one deal that got
away, the answer is no.

---

## 3. Kernel propagation — 128 skills share one text

The audit measured **128 of 133 skills with byte-identical `## Prohibited
actions`** and **128 with byte-identical `## Escalation`**.

That has a consequence nobody chose:

- editing the kernel **in one skill** produces silent **drift** — now there are two
  governance regimes and no one declared a second;
- editing it **in all 133** is the only correct action, and it is a governance
  change affecting every decision the estate gates.

**There is no third option, and no small version of this edit.**

Rules:

1. A kernel edit is a **Governance** class change. Always.
2. It propagates to **all** skills carrying that block, in one change, or it does
   not happen.
3. **Drift is a defect, not a variation.** If two skills' prohibitions differ and
   no one recorded a decision to differ, one of them is wrong and neither can be
   trusted.
4. A skill that needs a *different* prohibition needs a recorded reason, an owner,
   and a note in its own file explaining the divergence. Otherwise it is drift
   wearing an intention.

> **RECOMMENDATION(architecture):** extract the kernel to a single referenced
> source (Elite Skill Standard §8 already prohibits paraphrasing it per-skill).
> Until then, every kernel change is a 128-file edit and the drift risk compounds
> with each one.

---

## 4. Who may lower a ratchet floor

`check_skill_depth.py` and `check_reference_coverage.py` carry floors. Their own
docstrings say: raise them as skills are deepened; **never lower one to make a
build pass.**

A floor lowering is not a code change. **It is a decision to accept less
assurance**, and it is exactly the move the floors exist to catch. It arrives with
a good reason and a deadline, which is what makes it work.

| Situation | Correct action |
|---|---|
| Floor blocks a legitimate refactor | **Fix the detector, not the floor.** This already happened once: the verdict-vocabulary check missed `danantara-master-orchestrator` because it encoded one skill's idiom as the general rule. The detector was wrong; the floor was right. |
| A skill is being deliberately retired | Estate-class change. Governance Committee. Floor moves **as a recorded consequence**, not as a fix. |
| The floor was set wrong at the start | Record why, with evidence, and get the Governance Committee to reset it. |
| The build is red and the release is today | **No.** The floor is not the obstacle; the regression is. |

**Lowering a floor to go green is the institutional equivalent of removing the
downside case because it weakens the narrative** — the exact move
`ADVERSARIAL_CASES.yaml` → `optimistic-model` exists to catch, applied to the
assurance system itself.

---

## 5. Deprecation, never deletion

A deleted skill makes its past decisions unreadable. `DEC-014` cites
`dcf-model-challenger v1.1`; if v1.1 is gone, the record now points at nothing and
the decision cannot be reconstructed.

| Action | Meaning |
|---|---|
| **Deprecate** | No longer invoked for new work. Version and content **retained and retrievable**. Registry marks it deprecated with a date and successor. |
| **Archive** | Removed from routing, retained for audit. |
| **Delete** | **Only when the skill has never gated a decision.** Otherwise it is destruction of an audit record with a statutory reader. |

Merging two skills is a deprecation plus a new skill, not a rename. The merged
skill is a new method with a new version; the originals are deprecated with a
successor pointer.

---

## 6. Failure modes

The middle column is load-bearing: lifecycle governance fails under *pressure*,
not from ignorance.

| Failure | The pressure that causes it | Correct behaviour |
|---|---|---|
| **Threshold change treated as editorial** | It is one character, and a live deal needs it | Would it change what gets approved? Then it is a policy change and needs a policy owner. |
| **Editing a version in place** | The skill is "obviously" improved and nobody wants version noise | Immutable once it has gated a decision. Supersede, never edit. |
| **Kernel edited in one skill** | The edit was needed *here* and 133 files is a lot | Drift is a defect. All, or none. |
| **Lowering a floor to go green** | The release is today and the floor "isn't the real issue" | Fix the detector or accept the red. A floor lowering is a decision to accept less assurance. |
| **Deleting a skill** | It is unused and the estate is cluttered | If it ever gated a decision, deletion destroys an audit record. Deprecate. |
| **Version bump without evaluation** | The change is small and the eval suite is slow | A method change with no regression run is an untested policy change. |
| **Changing a threshold on one outcome** | A deal got away and someone is accountable for it | One outcome is one sample. Patterns change controls; anecdotes do not. |
| **Accepting "it's just documentation"** | SKILL.md looks like docs | The markdown **is** the method. There is no separate implementation to protect it. |

---

## 7. The Arc 2 intake

What `post-decision-learning` routes here, and what to do with it:

| Arc 2 finding | Class | Action |
|---|---|---|
| A named failure mode fired and the skill caught it | — | No change. Evidence the skill works. |
| A failure mode fired that was **not** named | Method | Name it, with its pressure. Second occurrence = skill defect, not user error. |
| A discriminating test failed to discriminate | Method | Fix the test or admit it is not discriminating. |
| A threshold was wrong, **with a pattern behind it** | Threshold | Policy owner, evidence, regression, recorded approval. |
| A threshold "felt wrong" on one deal | — | **Reject.** One sample. |
| A prediction was refuted because the world changed | — | Not a skill defect. Record in `institutional-memory-capture`. |
| The skill was right and was overridden | Governance | The finding is about the override, not the skill. Route to assurance. |
