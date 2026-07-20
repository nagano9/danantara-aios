# Danantara AIOS — Enterprise AI Ecosystem Blueprint

Version: 1.0 draft  
Generated: 2026-07-16

## Purpose
Create a governed, modular, auditable AI operating system for BPI Danantara, Danantara Asset Management, Danantara Investment Management, Danantara Development Management Fund, portfolio entities, and authorized partners.

## Design premise
Danantara requires more than a conventional sovereign-wealth-fund copilot. The operating model combines strategic control, active ownership and corporate transformation, risk-adjusted investment, catalytic development finance, national capability building, and public accountability.

## Seven layers
1. Security, identity, access, data classification, and AI governance
2. Controlled enterprise knowledge, data products, lineage, and institutional memory
3. Intent routing, planning, skill orchestration, state management, and escalation
4. Cross-functional and sector-specialist analysis
5. BPI, DAM, DIM, and DDMF mission workflows
6. Independent challenge, assurance, compliance, and audit
7. Human decision, execution, monitoring, and accountability

## Skill estate
The package contains 133 Claude Skills across 10 clusters. Each skill has a valid Agent Skills name, a description below 1,024 characters, risk tier, entity ownership, human approval requirement, structured workflow, Danantara Way rules, quality checks, and evaluation cases.

## Governing logic
The Danantara Way is implemented as a common governance kernel and as specialized gates:
- mandate and decision rights
- integrity and conflicts
- transparency and strategic confidentiality
- prudence and permanent-loss protection
- commercial return and national consequence
- long-term value
- additionality, bankability, and crowding-in
- active ownership, measurable transformation, and rational exit
- sovereignty, capability transfer, and enterprise digital synergy
- independent challenge and auditability

## Core tensions
The system must expose and escalate, not conceal:
1. commercial return versus national mandate
2. professional independence versus political direction
3. long-term value versus short-term intervention
4. transformation capital versus bailout
5. transparency versus strategic confidentiality

## Deployment model
- **Foundation:** constitution, taxonomy, access controls, knowledge hierarchy, evaluation harness
- **Pilot:** DIM investment committee, DAM transformation, DDMF bankability, board intelligence, portfolio early warning
- **Scale:** sector overlays, portfolio integrations, recurring workflows, shared platforms
- **Institutionalize:** lifecycle governance, outcome monitoring, model risk, audit, continuous learning

## Agent layer
The repository now adds a small agent stack above the skill estate. The agent
layer is the operational interface that routes work, curates source-layer
enrichment, and performs repository quality gates without replacing the skills
themselves.

Recommended first agents:
- `danantara-master-orchestrator`
- `source-layer-curator`
- `source-layer-enrichment`
- `decision-packager`
- `repo-audit-gate`

Recommended orchestration pattern:
`danantara-master-orchestrator` -> `source-layer-curator` -> `source-layer-enrichment` -> `decision-packager` -> `repo-audit-gate`

First workflow:
`repo-agent-loop` stitches the five agents together with the repo audit and
repo hygiene scripts as supporting functions.

## Production prerequisites
This package is build-ready but not automatically production-authorized. Before deployment, Danantara must map actual laws, policies, delegations, committee charters, data classifications, repositories, systems, tool permissions, retention rules, model hosting, incident procedures, and named human owners.
