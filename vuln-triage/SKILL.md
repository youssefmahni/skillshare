---
name: vuln-triage
description: Use when prioritizing a CVE using verified affected versions, CVSS, FIRST EPSS, CISA KEV, asset exposure, patch availability, compensating controls and remediation SLAs.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/vuln-triage/SKILL.md
---

# Vulnerability triage

Workspace: `/home/youssef/.openclaw/workspace`.
Local scoring formula and SLA table: `/home/youssef/.openclaw/workspace/skills/vuln-triage/SKILL.md`.

Fetch the vendor advisory/NVD record, CISA KEV catalog and FIRST EPSS record. Record retrieval dates and distinguish CVSS versions/vectors. Validate the asset's version, configuration and exposure rather than inferring applicability from a product name.

Use the source score only when its asset criticality/count and exposure inputs are known; label it as a local prioritization model. A KEV match on a confirmed affected asset is P0 under this local policy. Missing data should yield provisional priority and explicit follow-up.

Return CVE, affected assets, severity/vector, EPSS, KEV inclusion/date, applicability evidence, patch availability, priority, applicable SLA, owner, mitigation and verification steps, citations and related risk/incident record URLs.

Use `risk-register`, `incident-tracker`, or `audit-evidence` for requested follow-up. Patch completion requires verification. The source's heartbeat and automatic push behavior requires the OpenClaw gateway and actual delivery confirmation.
