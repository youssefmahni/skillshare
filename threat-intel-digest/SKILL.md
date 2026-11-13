---
name: threat-intel-digest
description: Use when preparing tactical, daily, weekly, or strategic threat-intelligence digests using KEV, EPSS, ATT&CK, vendor advisories, and full estate correlation.
metadata:
  workspace: /home/youssef/.openclaw/workspace
  estate: /home/youssef/Desktop/CISO-DarknessEye/02_Estate
---

# Threat Intelligence Digest & Full Estate KEV Triage

**Knowledge Roots:**
- Workspace: `/home/youssef/.openclaw/workspace` (`@openclaw`)
- Estate Documentation: `/home/youssef/Desktop/CISO-DarknessEye/02_Estate` (`@estate`)

## Full Estate Scope for KEV Triage

When executing the KEV workflow (e.g. via `/kev`), the default scope covers the **entire organizational estate**:
1. **DigitalOcean Droplet Fleet:** 57 droplets across 7 regions (FRA1, SFO2, SFO3, NYC1, NYC3, AMS3, SGP1) per `01_Droplet_Inventory.md`.
2. **GoDaddy Domain Portfolio:** 88 active registered domains across 5 brand clusters (`darkcoders.*`, `knighteye.*`, `darknesseye.*`, `aegiryx.*`, `pharohcode.*`) per `compliance/cloud-inventory/domains.txt`.
3. **Exposed Applications & Ingress:** 26+ HTTPS virtual hosts on Caddy (`443`), GitLab CE/EE (`gitlab.darkcoders.com`), Odoo 18 ERP (`erp.knighteye.ai`), n8n (`n8n.knighteye.ai` and `164.92.246.14`), Eramba GRC, Keycloak SSO, and HashiCorp Vault.
4. **Operating Systems & Kernels:** Linux Kernel (`6.8.0-139-generic`, Ubuntu 24.04/22.04 LTS), Windows 7/10 analysis guests.

## Operational Workflow

1. **Feed Retrieval:**
   - Fetch current CISA KEV JSON (`https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`).
   - Query FIRST EPSS API for identified candidate CVEs (`https://api.first.org/data/v1/epss?cve=...`).
   - Retain publication and retrieval timestamps with citations.

2. **Cross-Correlation Against Full Estate:**
   - Match CVE vendor and product against the complete software stack of all 57 droplets and 88 domains.
   - Categorize by exposure level:
     * **P0 / SEV-1 🔴:** Actively exploited KEV entry on an internet-exposed production asset (e.g. GitLab, n8n, public web). SLA: Immediate / <24h.
     * **P1 / SEV-2 🟠:** Actively exploited KEV entry on internal/VPC assets or operating system kernels across the fleet. SLA: <72h.
     * **P2 / SEV-3 🟡:** High-severity vulnerabilities with high EPSS probability without confirmed active exposure. SLA: 7 days.
     * **Clear:** Verified zero presence in both droplet fleet and domain registrations.

3. **Domain Anti-Spoofing Check:**
   - Verify that all dormant/holding GoDaddy domains enforce defensive SPF (`v=spf1 -all`) and DMARC (`p=reject`) to prevent brand weaponization.

4. **Output Requirements:**
   - Prioritized findings table with CVE ID, Product, Affected Droplet / Domain, Severity, EPSS Score, and CISA Due Date.
   - Actionable technical mitigations and operational ownership.
   - Saudi board-facing bilingual executive summaries (English and Arabic).
   - Eramba GRC deep links (`https://eramba.darkcoders.com/risks/add`) for risk registration.
