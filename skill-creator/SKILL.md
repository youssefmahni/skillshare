---
name: skill-creator
description: Use when creating, improving, or migrating reusable agent workflow skills into OpenCode SKILL.md format with clear triggers, references, and executable examples.
metadata:
  source: /home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/skill-creator/SKILL.md
---

# Native OpenCode skills

Original workflow-design reference: `/home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/skill-creator/SKILL.md`.

For OpenCode configuration or skill registration details, load the built-in `customize-opencode` skill. Use the current schema and actual loader behavior.

Create `skills/<lowercase-hyphenated-name>/SKILL.md` with required `name` and a concise `description` explaining both capability and trigger. Global location: `/home/youssef/.config/opencode/skills`.

Keep the operational workflow in the body, put detailed reference material alongside it or at explicit existing paths, and include runtime prerequisites and verified commands. Optional metadata must be a string-to-string map. Do not carry OpenClaw-only `requires`, `install`, `user-invocable`, environment injection or unsupported tool names into native metadata.

Verify frontmatter, folder/name agreement, source paths, examples, unique names and discovery with `opencode debug skill`. Restart OpenCode after adding or modifying skills.
