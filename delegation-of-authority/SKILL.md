---
name: delegation-of-authority
description: Use when validating corporate signing limits, encoding multi-signature approval rules, auditing decision rights, or compiling Open Policy Agent (OPA) Rego policies for automated transaction gates.
metadata:
  frameworks: Saudi Companies Law, Corporate Governance Regulations, COSO Internal Control
  droplet: ciso-agent-governance (10.30.0.20)
  assigned_personas: DOA-001 (Faisal Al-Otaibi), BD-OPS-001, GOV2-003
---

# Delegation of Authority (DoA) & Decision Rights

**Operating Droplet:** `10.30.0.20` (`ciso-agent-governance`)  
**Lead Personas:** `DOA-001` (DoA & Decision Rights Specialist), `BD-OPS-001` (Corporate Secretary), `GOV2-003` (Governance Framework Architect)

## Purpose & Scope
Codifies institutional decision-making authorities, monetary thresholds, procurement approval matrices, and board-reserved powers into executable policy gates. Eliminates single-person bypass risks and guarantees institutional accountability across all operational and financial commitments.

## Operational Workflow

1. **DoA Matrix Maintenance:**
   - Maintain the authoritative Delegation of Authority matrix across spending tiers, contract executions, cloud asset provisioning, and residual risk acceptance.
   - Map roles to explicit financial caps (e.g., Team Lead $\le \$10k$, Director $\le \$100k$, CISO/CFO $\le \$500k$, CEO $\le \$2M$, Board $> \$2M$).

2. **OPA Rego Policy Compilation:**
   - Compile human-readable DoA rules into formal Rego policies loaded by Open Policy Agent (`ciso-opa`).
   - Wire automated approval gates into CI/CD pipelines, Terraform deployments, and financial disbursement endpoints.

3. **Multi-Signature Escalation Routing:**
   - Coordinate with Keycloak to enforce multi-factor cryptographic dual-authorization for actions exceeding individual persona mandates.
   - Escalate policy override requests to the Board Secretariat (`BRD-GOV-001`).

4. **DoA Conformance Auditing:**
   - Reconcile approved Eramba risk treatments and purchase orders against authorized signatory logs in Vault.
