# End-to-End Orchestration Workflow Chains

Every material workflow starts with the common governance kernel: `danantara-ai-constitution`, `danantara-way-governance`, data classification, mandate and decision rights. Chains below are reference architectures; the master orchestrator may add or remove skills based on risk, evidence, and authority.

## DIM Investment Committee Workflow

**Trigger:** A new or follow-on investment requires formal screening, underwriting, committee decision, or conditional approval.

```text
danantara-master-orchestrator
→ intent-and-entity-router
→ investment-mandate-interpreter
→ opportunity-screening
→ investment-thesis-builder
→ evidence-retrieval-orchestrator
→ commercial-due-diligence
→ financial-due-diligence
→ legal-tax-due-diligence
→ technical-operational-due-diligence
→ esg-impact-due-diligence
→ integrity-counterparty-due-diligence
→ valuation-orchestrator
→ dcf-model-challenger
→ risk-adjusted-return-analyzer
→ portfolio-diversification-analyzer
→ deal-structuring-optimizer
→ co-investment-crowding-in
→ dual-mandate-balancer
→ investment-thesis-red-team
→ investment-committee-memo
→ decision-quality-gate
→ human-approval-orchestrator
→ audit-trail-packager
→ conditions-precedent-tracker
→ post-investment-monitor
```

**Human gate:** DIM Investment Committee or formally delegated authority

## DAM Active Ownership and Value Creation

**Trigger:** A BUMN or portfolio company requires ownership segmentation, performance intervention, transformation capital, or value-creation planning.

```text
danantara-master-orchestrator
→ bumn-portfolio-segmenter
→ corporate-parenting-advantage
→ financial-performance-diagnostic
→ operational-excellence-diagnostic
→ benchmark-intelligence-manager
→ value-creation-plan-builder
→ capital-allocation-reviewer
→ ceo-transformation-challenger
→ talent-meritocracy-assessor
→ management-accountability-contract
→ scenario-stress-testing
→ prudence-and-downside-gate
→ decision-quality-gate
→ human-approval-orchestrator
→ workflow-state-manager
→ post-decision-learning
```

**Human gate:** DAM portfolio committee, shareholder, board, or delegated authority

## DDMF Project Readiness and Bankability

**Trigger:** A national-development or public-infrastructure project needs preparation, bankability improvement, catalytic capital, or financing structure.

```text
danantara-master-orchestrator
→ national-priority-alignment
→ project-readiness-gate
→ document-evidence-extractor
→ technical-operational-due-diligence
→ legal-sufficiency-checker
→ esg-impact-due-diligence
→ bankability-gap-analyzer
→ additionality-assessor
→ project-finance-structurer
→ ppp-risk-allocation
→ blended-finance-designer
→ viability-gap-support-assessor
→ catalytic-capital-optimizer
→ co-investment-crowding-in
→ development-impact-assessor
→ socioeconomic-multiplier-modeler
→ dual-mandate-balancer
→ decision-quality-gate
→ human-approval-orchestrator
→ conditions-precedent-tracker
→ project-delivery-monitor
→ development-outcome-monitor
```

**Human gate:** DDMF investment/project authority and any competent public authority

## Distressed BUMN Turnaround and Conditional Capital

**Trigger:** A portfolio company requests funding, faces liquidity distress, covenant pressure, recurring losses, or potential insolvency.

```text
danantara-master-orchestrator
→ turnaround-triage
→ financial-performance-diagnostic
→ operational-excellence-diagnostic
→ legal-sufficiency-checker
→ enterprise-risk-aggregator
→ restructuring-options-designer
→ scenario-stress-testing
→ conditional-capital-designer
→ management-accountability-contract
→ conflict-of-interest-gate
→ prudence-and-downside-gate
→ bias-and-independence-review
→ decision-quality-gate
→ human-approval-orchestrator
→ workflow-state-manager
→ post-decision-learning
```

**Human gate:** Competent DAM, board, shareholder, creditor, and legal authorities

## Portfolio Rationalization and Corporate Action

**Trigger:** Danantara evaluates merger, consolidation, divestment, liquidation, strategic partnership, or continued ownership.

```text
danantara-master-orchestrator
→ bumn-portfolio-segmenter
→ corporate-parenting-advantage
→ portfolio-rationalization-analyzer
→ merger-consolidation-case
→ divestment-exit-readiness
→ valuation-orchestrator
→ cross-portfolio-synergy-finder
→ national-champion-competitiveness
→ legal-sufficiency-checker
→ scenario-stress-testing
→ stakeholder-communications-planner
→ investment-thesis-red-team
→ decision-quality-gate
→ human-approval-orchestrator
→ post-merger-integration-planner
→ audit-trail-packager
```

**Human gate:** Competent shareholder, corporate bodies, regulators, and transaction authorities

## Board and Supervisory Intelligence

**Trigger:** A board, supervisory board, executive committee, or investment committee needs a decision brief and challenge pack.

```text
danantara-master-orchestrator
→ document-evidence-extractor
→ decision-precedent-retriever
→ mandate-authority-interpreter
→ decision-rights-checker
→ assumption-uncertainty-manager
→ enterprise-risk-aggregator
→ conflict-of-interest-gate
→ red-team-orchestrator
→ executive-board-brief-builder
→ governance-board-paper-reviewer
→ evidence-citation-auditor
→ confidentiality-leakage-check
→ human-approval-orchestrator
→ audit-trail-packager
```

**Human gate:** The competent board, supervisory board, or committee

## Enterprise Digital Sovereignty and Shared Platform

**Trigger:** A major digital, cloud, data, AI, cybersecurity, or enterprise-platform investment is proposed.

```text
danantara-master-orchestrator
→ enterprise-digital-synergy
→ shared-platform-architect
→ data-sovereignty-assessor
→ cybersecurity-by-design
→ technology-transfer-assessor
→ procurement-commercial-strategy
→ capital-allocation-reviewer
→ scenario-stress-testing
→ strategic-national-interest-test
→ prudence-and-downside-gate
→ decision-quality-gate
→ human-approval-orchestrator
→ project-delivery-monitor
```

**Human gate:** Enterprise technology, security, investment, procurement, and competent corporate authorities

## Global Strategic Partnership and Co-investment

**Trigger:** Danantara considers a foreign or domestic strategic partner, joint fund, joint venture, technology partner, or co-investor.

```text
danantara-master-orchestrator
→ integrity-counterparty-due-diligence
→ co-investment-crowding-in
→ technology-transfer-assessor
→ data-sovereignty-assessor
→ strategic-national-interest-test
→ deal-structuring-optimizer
→ legal-tax-due-diligence
→ conflict-of-interest-gate
→ institutional-trust-monitor
→ investment-thesis-red-team
→ decision-quality-gate
→ human-approval-orchestrator
→ conditions-precedent-tracker
```

**Human gate:** Competent investment, partnership, legal, governance, and security authorities

## Enterprise Portfolio Early Warning

**Trigger:** Recurring monitoring detects financial, operational, covenant, market, project, governance, technology, or reputation deterioration.

```text
workflow-state-manager
→ portfolio-knowledge-graph
→ data-quality-and-lineage-checker
→ enterprise-portfolio-synthesizer
→ enterprise-risk-aggregator
→ scenario-stress-testing
→ financial-performance-diagnostic
→ operational-excellence-diagnostic
→ institutional-trust-monitor
→ escalation-and-exception-router
→ executive-board-brief-builder
→ audit-trail-packager
```

**Human gate:** Portfolio, risk, executive, or supervisory authority according to threshold

## Transparency and Public Accountability

**Trigger:** Danantara must communicate performance, material decisions, transformation, impact, risk, or financial information externally.

```text
transparency-disclosure-gate
→ strategic-confidentiality-classifier
→ data-quality-and-lineage-checker
→ evidence-citation-auditor
→ public-accountability-packager
→ vocabulary-and-narrative-guard
→ legal-sufficiency-checker
→ confidentiality-leakage-check
→ institutional-trust-monitor
→ human-approval-orchestrator
→ audit-trail-packager
```

**Human gate:** Authorized disclosure, legal, finance, and executive authority
