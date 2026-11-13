---
name: nca-mapper
description: Use when resolving Saudi NCA ECC, CSCC, cloud, OTCC, DCC, TCC, or OSMC controls and producing their evidence requirements or cross-framework mappings.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/nca-mapper/SKILL.md
---

# NCA control lookup

Workspace: `/home/youssef/.openclaw/workspace`.
Source workflow: `/home/youssef/.openclaw/workspace/skills/nca-mapper/SKILL.md`.

Resolve the framework family and edition before interpreting an ID. Use `regulatory/saudi-arabia/INDEX.md`, its `nca-*.md` files, and `nca-crosswalks/`.

Return: exact identifier, verified EN/AR title, domain, quoted requirement with source, scope/applicability, mapped controls with rationale, implementation guidance, evidence and review cadence.

The source quick references disagree on some ECC subdomain IDs. Cite the actual published NCA document and distinguish a source quotation from a local crosswalk. Do not invent missing control text from a title.

Use `compliance/posture.json` and live Eramba reads only for the organization's implementation status. If a source document is stale or absent, fetch its official NCA replacement and include edition/date.
