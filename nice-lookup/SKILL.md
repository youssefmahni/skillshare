---
name: nice-lookup
description: Use when resolving NICE work roles, competency areas, or T/K/S identifiers such as OG-WRL-007, NF-COM-002, T1518, K0007, or S0799 and their relationships.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/nice-lookup/SKILL.md
---

# NICE identifier lookup

Root: `/home/youssef/.openclaw/workspace/nice`.
Source: `/home/youssef/.openclaw/workspace/skills/nice-lookup/SKILL.md`.

1. Classify the identifier as work role, competency area, task, knowledge or skill.
2. For roles, glob `work-roles/<category>/<ID>-*.md`; for competencies use `competency-areas/`.
3. Search exact identifiers in `tks/tasks.csv`, `knowledge.csv`, `skills.csv`, then resolve relationships from `relationships.csv`. Parse CSV fields when commas occur in statements.
4. Use `crosswalks/` for related CSF/ISO/CIS/ATT&CK controls, labeling these mappings as local crosswalks.
5. Return the verbatim statement, type, related roles and source version. The cached baseline is NICE Components v2.1.0; verify currency if the user asks for latest guidance.

Use native read/glob/grep tools or the workspace filesystem MCP. This root is independent of the active project's working directory. TKS identifiers are workforce statements, not equivalent security control requirements.
