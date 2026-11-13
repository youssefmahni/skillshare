---
name: coding-agent
description: Use when explicitly coordinating coding-agent delegation, dividing a coding task among specialists, or adapting an OpenClaw coding-agent workflow to OpenCode.
metadata:
  source: /home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/coding-agent/SKILL.md
---

# Coding-agent coordination

Source: `/home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/coding-agent/SKILL.md`.

Use native OpenCode read/search/edit/shell tools for normal coding. Establish repository instructions and current worktree state, then implement and run checks appropriate to the change.

When delegation is explicitly requested or required by applicable instructions, use OpenCode's native task/subagent tool with a bounded objective, relevant paths, acceptance criteria, write/research scope and verification command. Avoid overlapping writes and integrate verified findings.

The source's PTY, `background:true`, `process.poll`, `sessions_spawn`, and permission-bypass flags belong to other runtimes. Do not emulate them by launching nested interactive OpenCode sessions. Do not copy its unconditional background/delegation behavior or automatic Telegram completion messages.

Use `taskflow` for persisted checkpoints when requested work must be resumable. Report what was implemented and verified, including unresolved failures.
