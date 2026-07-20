# Development Roadmap

This roadmap turns the current Danantara AIOS draft into an operating system
that can carry real mandates, real sources, real approvals, and real learning.

## Current state

The repository already has a strong structural base:

- 133 skills across 10 clusters
- governance doctrine, orchestration, evaluation, schemas, and source registry
- schema and governance validation passing
- workflow chains defined for the major mission areas

The most important gaps are not in volume. They are in operational grounding:

- the authenticated Tier 2 source layer is still empty, so most skills reason
  from a generic model
- the Tier 2 scaffold, fill playbook, status snapshot, and backlog sink now
  exist, but they still need authenticated source content
- only 7 skills currently have real references and trigger cases
- the implementation backlog sink `19_IMPLEMENTATION_BACKLOG` is now present as
  an explicit repo artifact, but it still needs real intake
- the entity model still needs to be aligned and pinned against the operative
  authenticated instruments

## What we should build next

### Wave 1: Make authority real

Priority: highest

Build the source and mandate layer first, because every downstream skill depends
on it.

- populate Tier 2 with actual charters, delegations, policies, and limits
- create a visible implementation backlog for every indeterminate or blocked
  mandate question
- promote authenticated source documents into the Tier 2 scaffold and retire
  the corresponding placeholders
- confirm the operative entity model and approval hierarchy
- map source ownership, effective dates, and document locations for the pilot
  set

Success looks like this:

- mandate questions stop defaulting to generic answers
- blocked questions are routed to named owners
- approval paths are grounded in instruments, not assumptions

### Wave 2: Turn the pilot skills into real products

Priority: very high

The first skills to mature should be the ones that unlock everything else.

Recommended pilot set:

- `danantara-master-orchestrator`
- `investment-mandate-interpreter`
- `decision-rights-checker`
- `human-approval-orchestrator`
- `decision-quality-gate`
- `post-decision-learning`
- `skill-lifecycle-governor`
- `dcf-model-challenger`
- `valuation-orchestrator`
- `investment-committee-memo`

For each pilot skill, add:

- real source references
- richer trigger and anti-trigger cases
- golden outputs
- failure modes that reflect actual Danantara pressure points

Success looks like this:

- the pilot skills can handle real cases without retreating to template language
- evaluation becomes discriminative, not only structural
- regression tests protect the estate from drift

### Wave 3: Connect the skills to operating workflows

Priority: high

The architecture becomes useful when it supports day-to-day decisions.

Build operational paths for:

- DIM investment screening and committee packs
- DAM performance intervention and value creation planning
- DDMF readiness, bankability, and catalytic capital
- board and supervisory intelligence
- enterprise early warning and escalation
- disclosure and public accountability

Success looks like this:

- a request can move from intake to approval-ready output through a single
  governed chain
- workflow state, conditions, and audit trail stay attached end to end

### Wave 4: Institutionalize learning and monitoring

Priority: high

The system should improve with use, not just produce outputs.

- add a formal prediction field to the decision log
- connect post-decision learning to the skill lifecycle process
- track which missing cells block the most decisions
- monitor trigger precision, escalation quality, citation failures, and outcome
  accuracy
- assign recertification cycles for critical skills

Success looks like this:

- a decision can be revisited against a recorded prediction
- refuted predictions update the estate instead of being forgotten
- the backlog is ranked by real blocking pressure

## Recommended build order

If we want maximum leverage with minimum fragmentation, build in this order:

1. Tier 2 source pack
2. implementation backlog artifact
3. approval and decision-rights grounding
4. pilot workflow skills with real references
5. decision log and learning loop
6. operational connectors and monitoring

## What not to do yet

- do not expand the skill estate further before the source layer is grounded
- do not add more thematic skills if the existing ones still lack real evidence
- do not treat validator passes as proof of operational readiness
- do not fill the backlog with speculative ideas that have no blocked decision

## Practical next deliverables

The next three deliverables that would change the most are:

- a populated Tier 2 source register from actual Danantara documents
- a structured implementation backlog with blocker, owner, and priority fields
- a pilot release of the mandate and approval workflow stack with real trigger
  cases

The new agent layer is the companion deliverable to those three items. Once the
source layer is grounded, the first operational agents should be:

- a master orchestrator that routes requests into the right skill chain
- a source-layer curator that keeps the registry, backlog, and status aligned
- a source-layer enrichment agent that turns audit findings into a tracked plan
- a repo audit gate that catches drift before it spreads into downstream work

The first workflow should be a repo maintenance loop that routes a task,
curates the source layer, generates an enrichment plan, runs the repo checks,
and returns a consolidated audit decision.
