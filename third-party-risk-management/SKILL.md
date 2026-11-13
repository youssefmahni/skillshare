---
name: third-party-risk-management
description: Use when assessing vendor and supplier risk tiers (Tier 1–4), evaluating SOC 2 Type II / ISO 27001 audit reports, mapping fourth-party supply chain concentration, or monitoring continuous vendor breach signals.
metadata:
  frameworks: NIST SP 800-161r1 (C-SCRM), ISO/IEC 27036, NCA TCA-1:2020
  droplet: ciso-agent-governance (10.30.0.20)
  assigned_personas: TPCYB-001 (Abdulaziz Al-Shehri), TPRM-LEAD-001, TPRM-001
---

# Third-Party & Supply Chain Cyber Risk Management (TPRM / C-SCRM)

**Operating Droplet:** `10.30.0.20` (`ciso-agent-governance`)  
**Lead Personas:** `TPCYB-001` (Third-Party Cyber Risk & Fourth-Party Supply Chain Specialist), `TPRM-LEAD-001` (Director of Third-Party Risk), `TPRM-001` (Senior Vendor Risk Manager)

## Purpose & Scope
Governs and monitors the entire lifecycle of external technology vendors, SaaS providers, open-source dependencies, and hosting partners. Enforces strict compliance with the National Cybersecurity Authority Third-Party Cybersecurity Standard (NCA TCA-1:2020) and identifies hidden fourth-party supply chain risks.

## Operational Workflow

1. **Vendor Inherent Risk Tiering:**
   - Classify all 30+ enterprise suppliers into 4 tiers based on access to confidential data, production systems, and business criticality:
     * **Tier 1 (Critical):** Cloud providers (DigitalOcean, AWS), IdP (Keycloak), payment gateways.
     * **Tier 2 (High):** SaaS software with PII/source code access (GitLab, Slack).
     * **Tier 3 (Medium):** Development contractors, non-production tools.
     * **Tier 4 (Low):** COTS software without network integration.

2. **Security Assurance & Due Diligence:**
   - Audit external supplier SOC 2 Type II reports, ISO 27001 certificates, and penetration testing summaries.
   - Enforce mandatory contractual security clauses (mandatory 24h breach notification, right to audit, data sovereignty).

3. **Fourth-Party Dependency Mapping:**
   - Map downstream subcontractor concentration (e.g., DNS, CDN, and payment sub-processors) to identify systemic single points of failure.
   - Cross-check against OpenSearch threat feeds for compromised supplier credentials or active third-party CVEs.

4. **Continuous Monitoring & Offboarding:**
   - Track supplier risk rating changes and automate reassessment workflows upon contract renewal or major supplier architectural changes.
