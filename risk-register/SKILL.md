---
name: risk-register
description: Use when reading, scoring, creating, updating, accepting, closing, or presenting cybersecurity risks and their owners, treatments, review dates, and residual exposure.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/risk-register/SKILL.md
---

# Risk register operations

Workspace: `/home/youssef/.openclaw/workspace`.
Source model: `/home/youssef/.openclaw/workspace/skills/risk-register/SKILL.md`.

Eramba is the operational system of record. Read live risk records when available and return their URLs; use supported deep links for creates/edits per `COMMANDS.md`.

For explicitly requested local working-register operations:
1. Read `risk/register.json`. Its current shape is an object containing `risks`, `organizations`, and metadata, not the bare array described in the old skill.
2. Identify the existing risk or allocate a unique ID. Preserve unrelated fields and all history.
3. Record asset, threat/vulnerability, likelihood, impact, evidence, existing/recommended controls, owner, treatment, review date and residual risk.
4. Use FAIR ranges in SAR only when grounded in inputs. Label scoring scales as local policy. An unimplemented recommendation does not reduce residual risk.
5. Append a change record to `risk/changelog.jsonl` when changing the local register. Preserve accepted/closed risks and the actual signer's decision.
6. Return a concise ranked summary with provenance and unverified assumptions.

The source's `add`, `update`, `chart` and `export` are workflow labels, not CLI tools. Do not use the legacy recon auto-merger to close risks after a partial or failed scan.
