---
name: taskflow
description: Use when organizing resumable multi-step work with explicit state, waits, ownership and checkpoints, or inspecting an existing OpenClaw durable TaskFlow.
metadata:
  source: /home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/taskflow/SKILL.md
---

# Resumable task workflows

Source lifecycle reference: `/home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/taskflow/SKILL.md`.

For work performed in OpenCode:
1. Track actionable steps with native todos and maintain one current step.
2. When persistence is required, keep a small task-specific checkpoint in the agreed project/artifacts directory: task ID, owner, goal, current step, status, revision, completed artifacts, wait reason, next action and timestamps.
3. Read and verify the checkpoint revision before updating it; preserve a clear history of meaningful transitions.
4. On resume, verify external facts/artifacts before marking any step complete. Report genuine waiting/blocked state.
5. Delegate only when requested or required by applicable instructions.

For existing OpenClaw jobs, use `openclaw tasks list --json`, `openclaw tasks flow --help`, and their supported inspect commands. Its SQLite TaskFlow registry and `api.runtime.tasks.flow` API belong to OpenClaw's runtime.

OpenCode todos/checkpoint files do not create detached workers, automatic wakeups or durable scheduling. If the requested workflow needs those facilities, use the existing OpenClaw runtime explicitly and verify its status.
