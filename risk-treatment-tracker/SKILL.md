---
name: risk-treatment-tracker
description: Use when tracking enterprise risk treatment decisions across the 4 options (Mitigate, Transfer, Accept, Avoid), enforcing risk acceptance signing limits under DoA, or tracking Corrective and Preventive Actions (CAPA).
metadata:
  frameworks: ISO/IEC 27005:2022, NIST SP 800-30 Rev 1, COSO ERM 2017
  droplet: ciso-agent-governance (10.30.0.20)
  assigned_personas: RSK-TRT-001 (Layla Al-Amri), ERM-001, RA-002
---

# Enterprise Risk Treatment & Remediation Lifecycle

**Operating Droplet:** `10.30.0.20` (`ciso-agent-governance`)  
**Lead Personas:** `RSK-TRT-001` (Risk Treatment & Remediation Manager), `ERM-001` (Principal Enterprise Risk Specialist), `RA-002` (Risk Remediation Specialist)

## Purpose & Scope
Orchestrates and tracks the formal treatment strategy for every identified vulnerability and scenario recorded in Eramba GRC. Enforces organizational separation between identifying/quantifying risk and formally accepting or mitigating exposure.

## Operational Workflow

1. **Treatment Strategy Allocation:**
   - Assign each validated risk to one of the 4 canonical treatment paths:
     * **Mitigate:** Deploy technical/procedural controls to reduce likelihood or impact.
     * **Transfer:** Offload risk through cyber insurance policies or third-party indemnification.
     * **Avoid:** Decommission the vulnerable asset, protocol, or unapproved service.
     * **Accept:** Formally tolerate residual risk within approved risk appetite limits.

2. **Delegation of Authority (DoA) Risk Acceptance Gate:**
   - Enforce cryptographic multi-party sign-off for risk acceptance based on Annualized Loss Expectancy (ALE):
     * $\le \$50,000$ ALE: Business Unit Owner + CISO (`CISO-001`).
     * $\$50,001$ – $\$250,000$ ALE: CISO + Chief Risk Officer (`CRO`).
     * $\$250,001$ – $\$1,000,000$ ALE: Chief Executive Officer (`CEO-001`).
     * $> \$1,000,000$ ALE: Board Audit & Risk Committee approval mandatory.
   - Any unapproved acceptance attempt triggers immediate OPA gate rejection.

3. **CAPA & Remediation Action Tracking:**
   - Track implementation milestones for corrective action plans linked to Eramba risk records.
   - Monitor remediation SLA compliance (Critical: 7 days, High: 30 days, Medium: 90 days).

4. **Residual Risk Recalculation:**
   - Recalculate residual exposure following control validation; ensure residual score falls below the enterprise risk appetite ceiling ($\le 12/25$).
