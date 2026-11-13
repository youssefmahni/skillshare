---
name: ciso-governance
description: Use when synchronizing Eramba GRC risks and controls, running compliance gap analyses (NCA ECC, SAMA CSF, ISO 27001), evaluating FAIR quantitative risk, or processing Saudi PDPL DSRs on ciso-agent-governance.
metadata:
  framework: NIST SP 800-181 Rev 1 (NICE) - Oversight & Governance (OG)
  droplet: ciso-agent-governance (10.30.0.20)
---

# NIST NICE Oversight & Governance (OG) Operations

**Target Environment:** `ciso-agent-governance` (`10.30.0.20` / public `164.92.195.36`)  
**Core NICE Work Roles:**
- `OG-WRL-002`: Cybersecurity Policy and Planning
- `OG-WRL-007`: Executive Cybersecurity Leadership (Board & C-Suite)
- `OG-WRL-008`: Privacy Compliance (SDAIA PDPL / GDPR)
- `OG-WRL-012`: Security Control Assessment
- `OG-WRL-013`: Systems Authorization (ATO & Risk Acceptance)
- `OG-WRL-014`: Systems Security Management (Eramba GRC Master)
- `OG-WRL-016`: Technology Program Auditing

## Operational Workflow

1. **GRC Risk & Control Synchronization:**
   - Call `ciso-governance_governance_eramba_sync` to query active risks, assets, and internal controls from Eramba GRC (`10.30.0.3` / `eramba.darkcoders.com`).
   - Identify risks exceeding risk appetite (residual score $\ge 15/25$) and ensure linked controls are actively verified.

2. **Regulatory Gap Analysis:**
   - Evaluate compliance posture using `ciso-governance_governance_control_gap_analysis` across target frameworks:
     * **NCA ECC-1:2018:** Essential Cybersecurity Controls (114 controls).
     * **SAMA CSF:** Saudi Central Bank Cybersecurity Framework (160 controls).
     * **ISO/IEC 27001:2022:** Information Security Management System (93 controls).
     * **NIST CSF 2.0:** Govern, Identify, Protect, Detect, Respond, Recover.
     * **PDPL:** Saudi Personal Data Protection Law (45 controls).

3. **Quantitative Risk Modeling (FAIR):**
   - Call `ciso-governance_governance_score_fair_risk` to model annualized loss expectancy (ALE) from threat event frequency, vulnerability percentage, and loss ranges in USD.
   - Categorize risk exposure into board-friendly financial tiers.

4. **Saudi PDPL Data Subject Requests (DSR):**
   - Manage incoming data subject requests (access, rectification, erasure, objection) via `ciso-governance_governance_pdpl_dsr_workflow`.
   - Track compliance against the statutory 30-day resolution deadline set by SDAIA.

5. **Bilingual Board Brief Compilation:**
   - Call `ciso-governance_governance_board_brief_compile` to generate executive summaries with synchronized English and Arabic text.
   - Surface key KRIs: mean time to remediate (MTTR), critical vulnerability count, and regulatory adherence percentages.

6. **Node Health:**
   - Verify governance daemon services and worker health via `ciso-governance_governance_node_telemetry`.
