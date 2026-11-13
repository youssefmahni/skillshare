---
name: audit-evidence
description: Use when collecting, hashing, validating, packaging, or checking freshness of audit evidence for NCA, ISO 27001, SAMA, SOC 2, PCI DSS, or PDPL controls.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/audit-evidence/SKILL.md
---

# Audit evidence in OpenCode

Workspace: `/home/youssef/.openclaw/workspace`.
Detailed evidence schema and freshness rules: `/home/youssef/.openclaw/workspace/skills/audit-evidence/SKILL.md`.

1. Identify the framework edition, control, source system, requested artifact and destination.
2. Inspect `compliance/evidence/_index.json` before extending it. Store per-control artifacts under `compliance/evidence/<framework>/<control-id>/`.
3. Capture the actual configuration, operational sample, signed attestation or report using the appropriate available tool. Record what was observed, not an inferred implementation state.
4. Calculate SHA-256; record source, capture time with offset, collector, version, validity and framework tags. Preserve previous files and index entries.
5. Use the source freshness rules as local policy: configuration 90 days, operational samples 30 days, policies/attestations one year, third-party reports 14 months unless a governing requirement differs.
6. For packaging, verify hashes and include a manifest. The disabled `ciso-spaces` integration supports new-key uploads and version/hash metadata when activated.

`add`, `freshness`, `package`, and `validate` in the source are workflow labels. Use native file tools, PowerShell hashing/archive commands, and available MCPs to implement them. A read-only attribute or hash alone does not make storage immutable.
