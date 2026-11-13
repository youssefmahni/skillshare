---
name: taskflow-inbox-triage
description: Use when triaging supplied or accessible inbox items into business actions, personal notifications and deferred summaries while tracking ownership and pending replies.
metadata:
  source: /home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/taskflow-inbox-triage/SKILL.md
---

# Inbox triage workflow

Source: `/home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/taskflow-inbox-triage/SKILL.md`.

Use `taskflow` for the checkpoint lifecycle. Establish the inbox source, batch boundary and routing rules. Only retrieve items through an actually configured connector or user-supplied content.

Classify items into business actions, personal notifications and deferred summaries. Preserve source item IDs and minimal context to prevent duplicate processing. Draft replies or actions, track the responsible owner, and record sent/waiting/done states from actual tool results.

The source's Slack routing is an example; Slack is disabled in this OpenClaw configuration. Use the configured destination for a requested send. A classification result alone must not trigger an outbound message or claim a background reply-watcher exists.

Return the triage summary, urgent items, drafts, pending replies and next checkpoint.
