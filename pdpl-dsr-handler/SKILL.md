---
name: pdpl-dsr-handler
description: Use when processing a Saudi PDPL data-subject request, defining identity verification and system scope, preparing a bilingual response, or updating DSR case records.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/pdpl-dsr-handler/SKILL.md
---

# PDPL data-subject request workflow

Workspace: `/home/youssef/.openclaw/workspace`.
Source: `/home/youssef/.openclaw/workspace/skills/pdpl-dsr-handler/SKILL.md`.
Detailed procedure: `/home/youssef/.openclaw/workspace/playbooks/saudi/pdpl-dsr-handler.md`.

1. Identify the request, intake date, requested rights and responsible DPO. Inspect existing `compliance/dsr-register.json` before allocating a case ID.
2. Verify identity with the minimum necessary information and determine affected systems and legal-retention exceptions.
3. Validate current PDPL/implementing-regulation article references and applicable deadlines against official SDAIA material. The source's article numbering and SLA quick references require verification.
4. Prepare a system-by-system fulfillment plan using only available integrations. Track pending access, completed extracts, corrections, approved deletions and propagation separately.
5. Produce the appropriate EN/AR response, reasons for exceptions, delivery channel, due dates and escalation contact.
6. Preserve a minimal case audit trail under `compliance/dsr-cases/<id>/`; record actual completion and delivery evidence.

Use the source JSON as a starting schema, adapted to the existing register. Do not describe suggested actions as executed, or store excess verification documents in general-purpose memory.
