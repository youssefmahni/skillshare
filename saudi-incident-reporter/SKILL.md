---
name: saudi-incident-reporter
description: Use when assessing Saudi cyber-incident reporting obligations or drafting coordinated NCA, SAMA, SDAIA/PDPL, CST, or CMA incident notifications and tracking receipts.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/saudi-incident-reporter/SKILL.md
---

# Saudi incident reporting

Workspace: `/home/youssef/.openclaw/workspace`.
Source: `/home/youssef/.openclaw/workspace/skills/saudi-incident-reporter/SKILL.md`.
Procedure: `/home/youssef/.openclaw/workspace/playbooks/saudi/saudi-incident-reporter.md`.

1. Establish the entity's actual regulated activities, incident type, personal-data impact, materiality and detection/awareness times.
2. Verify each applicable authority, current notification trigger and deadline against a primary source or the organization's binding notice. The legacy 1h/2h/72h matrix is a planning reference, not a universal rule.
3. Build a per-authority table of trigger, source, start time, due time, responsible owner and status. Use explicit timezone offsets.
4. Draft consistent technical facts, impact, containment, IOCs, next update and EN/AR executive sections. Identify uncertainty rather than speculating.
5. Save drafts under `compliance/incident-notifications/<incident-id>/`. Follow the source Legal/DPO/Compliance sign-off process for external submissions.
6. After actual delivery, capture submission ID, time, sender, content hash and acknowledgment in `compliance/regulator-log.json` and the incident timeline.

OpenCode does not create reminders or submit notifications by loading this skill. Use configured runtime/channel tools for requested delivery and record their actual outcome.
