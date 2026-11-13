---
name: business-impact-analysis
description: Use when modeling business disruption curves, calculating Maximum Tolerable Downtime (MTD), RTO, and RPO, analyzing single points of failure (SPOF), or evaluating disaster recovery risk across DarkCoders droplets.
metadata:
  frameworks: ISO 22301:2019, NIST SP 800-34 Rev 1, NCA BCM-1:2020
  droplet: ciso-agent-defense (10.30.0.4)
  assigned_personas: BIA-001 (Nasser Al-Mutlaq), BCM-LEAD-001, BCM-001
---

# Business Impact Analysis (BIA) & Continuity Risk Modeling

**Operating Droplet:** `10.30.0.4` (`ciso-agent-defense`)  
**Lead Personas:** `BIA-001` (BIA & Service Continuity Risk Specialist), `BCM-LEAD-001` (Director of Business Continuity), `BCM-001` (Senior BCM Specialist)

## Purpose & Scope
Quantifies the financial, operational, and regulatory damage resulting from unplanned service disruptions, network partition events, or data loss across the estate. Establishes empirical recovery targets to drive infrastructure redundancy and disaster recovery investments.

## Operational Workflow

1. **Critical Service Dependency Mapping:**
   - Map dependencies across all 8 execution droplets, core datastores (PostgreSQL, OpenSearch, MinIO), and authentication nodes (Keycloak, Vault).
   - Identify Single Points of Failure (SPOF) in routing, DNS, or private WireGuard/OpenVPN mesh networks.

2. **Downtime Impact Modeling:**
   - Construct financial disruption curves plotting loss over time (hourly outage cost, regulatory non-compliance penalties under NCA/SAMA, customer SLA credits).
   - Calculate critical operational metrics:
     * **MTD (Maximum Tolerable Downtime):** Maximum period the business can survive without the service.
     * **RTO (Recovery Time Objective):** Targeted duration to restore operational service.
     * **RPO (Recovery Point Objective):** Maximum acceptable data loss expressed in time.

3. **Disaster Recovery Gap Analysis:**
   - Compare actual failover benchmarks and backup restoration test results against designated RTO/RPO objectives.
   - Flag any service where recovery capability lags behind corporate risk appetite.

4. **Integration with Crisis Operations:**
   - Provide empirical disruption curves to `CRISIS-001` to guide emergency incident command decisions during critical outages.
