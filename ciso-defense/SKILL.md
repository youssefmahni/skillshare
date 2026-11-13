---
name: ciso-defense
description: Use when handling SOC detection, alert correlation, CISA KEV/EPSS vulnerability triage, threat intelligence reputation checks, or automated containment on the ciso-agent-defense droplet.
metadata:
  framework: NIST SP 800-181 Rev 1 (NICE) - Protect & Defend (PD)
  droplet: ciso-agent-defense (10.30.0.4)
---

# NIST NICE Protect & Defend (PD) Operations

**Target Environment:** `ciso-agent-defense` (`10.30.0.4` / public `207.154.235.217`)  
**Core NICE Work Roles:**
- `PD-WRL-001`: Defensive Cybersecurity (SOC & SIEM Operations)
- `PD-WRL-003`: Incident Response (Triage, Containment, Eradication)
- `PD-WRL-004`: Infrastructure Support (Host & Network Security)
- `PD-WRL-005`: Insider Threat Analysis (Behavioral Anomalies, UEBA)
- `PD-WRL-006`: Threat Analysis (Tactical Cyber Threat Intelligence)
- `PD-WRL-007`: Vulnerability Analysis (Prioritization, EPSS/KEV Mapping)

## Operational Workflow

1. **Alert Triage:**
   - Call `ciso-defense_defense_soc_alerts` to retrieve active security alerts from the OpenSearch SIEM indices on `10.30.0.8`.
   - Filter by severity (`critical`, `high`, `medium`) and look for anomalous logon spikes, port scans, or persistence triggers.

2. **Vulnerability Prioritization:**
   - Call `ciso-defense_defense_triage_cve` passing the target CVE identifier (e.g. `CVE-2024-3400`).
   - Check if the vulnerability is listed in the CISA Known Exploited Vulnerabilities (KEV) catalog and review the FIRST EPSS probability.
   - Enforce remediation SLAs: P0 (<24h for active KEV on internet-exposed assets), P1 (<72h), P2 (<7d).

3. **Threat Intelligence & Reputation:**
   - Call `ciso-defense_defense_ioc_reputation` to inspect IP addresses, domains, or file hashes.
   - Correlate with known threat actor TTPs (e.g. APT29, Sandworm) mapped to MITRE ATT&CK enterprise tactics.

4. **Detection Engineering:**
   - Test and validate Sigma detection rules with `ciso-defense_defense_run_sigma_rule`.
   - Confirm log categories (`process_creation`, `network_connection`, `authentication`) before production ingestion.

5. **Containment & Response:**
   - For confirmed threats, use `ciso-defense_defense_containment_action` to simulate or enforce containment (IP block, network isolation, or process termination).
   - Ensure all containment decisions are recorded with an associated incident ID and logged in the immutable audit trail.

6. **Node Health:**
   - Check systemd daemons (`darknesseye-agent-loop`, `darknesseye-persona-worker`), Tailscale, and Fluent Bit using `ciso-defense_defense_node_telemetry`.
