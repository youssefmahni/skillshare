---
name: healthcheck
description: Use when diagnosing OpenClaw host health, gateway availability, configuration validation, listening services, or a specifically requested Windows security-posture review.
metadata:
  source: /home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/healthcheck/SKILL.md
---

# OpenClaw health checks

Source: `/home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/healthcheck/SKILL.md`.

Start with the user's reported issue and read-only checks:

```powershell
openclaw config validate
openclaw gateway status --json
openclaw skills check
opencode mcp list
```

For a requested security review, use `openclaw security audit --deep --json` and relevant Windows checks such as `Get-NetTCPConnection` or `Get-NetFirewallProfile`. Correlate findings to the actual access path, service state and configuration; do not infer health from a registered scheduled task alone.

Keep OpenClaw application fixes distinct from OS/service changes. Apply changes within the requested scope, preserving a usable access path and documenting rollback for material changes. Use supported CLI options verified with `--help`.

Report evidence, root cause, changes, verification and remaining dependencies. Use `openclaw-operations` for the migration-specific paths and gateway/channel mapping.
