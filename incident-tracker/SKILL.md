---
name: incident-tracker
description: Use when opening, updating, closing, or reporting a cybersecurity incident, maintaining its evidence timeline, or tracking containment and regulatory notification status.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/incident-tracker/SKILL.md
---

# Incident tracking

Workspace: `/home/youssef/.openclaw/workspace`.
Full incident template: `/home/youssef/.openclaw/workspace/skills/incident-tracker/SKILL.md`.

1. Establish the incident ID, known facts, SEV, detection time, affected systems/data and current response phase.
2. Use available Eramba incident tools for authoritative records and deep links for edits. Maintain local working timelines in `memory/incidents/` and evidence in `compliance/evidence/incidents/<id>/`.
3. Inspect the existing incident index and allocate a non-colliding ID. Append timestamped events; preserve earlier statements and mark corrections explicitly.
4. Record containment, eradication, recovery, confidence, IOCs, ATT&CK techniques, owner, next action and evidence hashes.
5. For regulator-facing work, load `saudi-incident-reporter` and verify current source requirements. The local templates cite legacy NIST 800-61r2; identify the edition used and consult current guidance as needed.
6. Close with the required owner acknowledgment, root cause, lessons, actions and verified remediation evidence.

The source's `open`, `append`, `notify`, and `close` are workflow labels, not installed commands. Notification templates do not send a message or start a timer. Record delivery only after a successful channel/tool response; source SEV-1/2 closure requires the principal's acknowledgment.
