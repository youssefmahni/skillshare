---
name: osint-recon
description: Use when researching an authorized organization's public attack surface, certificate transparency, exposed services, brand impersonation, or published threat intelligence.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/osint-recon/SKILL.md
---

# Defensive OSINT

Workspace: `/home/youssef/.openclaw/workspace`.
Detailed source: `/home/youssef/.openclaw/workspace/skills/osint-recon/SKILL.md`.

Establish scope from the task and `compliance/discovery-config.json`. Start with public CT, DNS, RDAP, vendor advisories and existing evidence. Use native webfetch, the fetch MCP, or Chrome DevTools for sources that require a browser.

Record source URL, collection timestamp, target, collection method, findings, confidence and TLP handling. Correlate names/services to actual asset ownership before assigning exposure or a vulnerability.

Vendor APIs such as Shodan, Censys, VT and HIBP are listed as pending in the source; check availability before using them. Recommendations in the source tool catalog are not proof that those programs or API credentials are installed.

Write a scoped report under `memory/osint/` or `compliance/attack-surface/`, with linked evidence and follow-up actions. Use `discovery-engine` for the installed PowerShell pipeline and its documented operational limitations.
