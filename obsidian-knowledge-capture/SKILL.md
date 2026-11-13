---
name: obsidian-knowledge-capture
description: >
  Capture knowledge into an Obsidian vault: create or update notes with proper frontmatter, tags, and links. Use when saving research findings, decisions, or technical notes.
---

# Obsidian Knowledge Capture

## Note template

```markdown
---
title: <Title>
date: <YYYY-MM-DD>
tags: [<tag1>, <tag2>]
type: note | decision | research | how-to
status: draft | review | final
---

# <Title>

## Summary
<1-3 sentences>

## Content
...

## Related
- [[<linked-note>]]

## Sources
- [Source](URL)
```

## Conventions

- Filename: `YYYY-MM-DD <Title>.md` or `<Topic>.md` for evergreen notes
- Use `[[WikiLinks]]` for cross-references
- Tags: lowercase, hyphenated (`data-engineering`, `ai-agents`)
- Atomic notes: one idea per note; link to others

## Vault location

Set `OBSIDIAN_VAULT` env var or use default `~/Documents/obsidian-vault/`.
