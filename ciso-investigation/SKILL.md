---
name: ciso-investigation
description: Use when acquiring digital evidence, performing memory forensics, submitting samples to the CAPE sandbox, reconstructing attack timelines, or verifying chain of custody on ciso-agent-investigation.
metadata:
  framework: NIST SP 800-181 Rev 1 (NICE) - Investigate (IN)
  droplet: ciso-agent-investigation (10.30.0.17)
---

# NIST NICE Investigate (IN) Operations

**Target Environment:** `ciso-agent-investigation` (`10.30.0.17` / public `104.248.44.141`)  
**Core NICE Work Roles:**
- `IN-WRL-001`: Cybercrime Investigation (Attribution & Fraud)
- `IN-WRL-002`: Digital Evidence Analysis (Disk & Memory Forensics)
- `PD-WRL-002`: Digital Forensics (Evidence Preservation & Analysis)

## Operational Workflow

1. **Evidence Acquisition & Registration:**
   - Call `ciso-investigation_investigation_acquire_artifact` to register new forensic samples (disk images, memory dumps, PCAPs, logs).
   - The tool automatically computes a cryptographic SHA-256 digest and records provenance targeting the DO Spaces repository `spaces://fra1.digitaloceanspaces.com/ciso-evidence/cases/<case_id>/`.

2. **Malware Sandboxing & Behavioral Triage:**
   - Submit suspicious files, scripts, or URLs via `ciso-investigation_investigation_sandbox_submit`.
   - The sample is analyzed against the private CAPE sandbox (`10.30.0.6`).
   - Extract behavioral indicators: spawned processes, registry persistence keys, C2 beacon IPs, and MITRE ATT&CK techniques.

3. **Memory Forensic Analysis:**
   - Call `ciso-investigation_investigation_memory_analysis` with plugins such as `pslist`, `netscan`, or `malfind`.
   - Detect process hollowing, unmapped executable code, and hidden network sockets.

4. **Timeline Assembly:**
   - Aggregate events across endpoint logs, authentication servers, and firewall streams using `ciso-investigation_investigation_build_timeline`.
   - Generate normalized chronologies formatted in `Asia/Riyadh` (AST) to satisfy regulatory reporting requirements.

5. **Chain of Custody Verification:**
   - Call `ciso-investigation_investigation_verify_chain_of_custody` to validate evidentiary integrity and audit trail completeness per NIST SP 800-86 and ISO 27037 standards.

6. **Node Health:**
   - Inspect forensic worker health and systemd status via `ciso-investigation_investigation_node_telemetry`.
