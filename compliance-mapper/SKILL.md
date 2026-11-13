---
name: compliance-mapper
description: Use when mapping security controls across NCA ECC, NIST CSF, NIST 800-53, ISO 27001, CIS, SAMA, PCI DSS, SOC 2, or ATT&CK, or preparing a control gap analysis.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/compliance-mapper/SKILL.md
---

# Cross-framework mapping

Workspace: `/home/youssef/.openclaw/workspace`.
Detailed source: `/home/youssef/.openclaw/workspace/skills/compliance-mapper/SKILL.md`.

1. Classify the input as control ID, concept, risk, or NICE identifier and confirm editions and entity scope.
2. Search `nice/crosswalks/`, `regulatory/saudi-arabia/nca-crosswalks/`, and `frameworks/` using native grep/glob/read tools.
3. Read the exact cited control text. Source example crosswalks contain inconsistencies, including ECC monitoring versus incident-management numbering; verify them instead of treating examples as authoritative.
4. Return a matrix: source control, target control, relationship (full/partial/supporting), rationale, source citation, implementation guidance, evidence expected and gaps.
5. Use live Eramba control/compliance tools for operational posture. Inspect `compliance/posture.json` if available and label local working data clearly.
6. Record assumptions and missing evidence. Coverage mapping does not establish operating effectiveness or certification.

Use Arabic summaries for Saudi-facing deliverables. Load `nice-lookup` or `nca-mapper` only when the task requires their identifier detail.
