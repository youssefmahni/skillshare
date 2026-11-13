---
name: openclaw-operations
description: Use when inspecting or maintaining the OpenClaw-to-OpenCode integration, gateway, MCP mappings, model catalog, memory access, cron schedules, or native skill discovery.
metadata:
  source: /home/youssef/.openclaw/workspace/TOOLS.md
---

# OpenClaw integration operations

Configuration: `/home/youssef/.config/opencode/opencode.json`.
Migration guide and audit: `/home/youssef/.config/opencode/openclaw/README.md` and `AUDIT.md`.
Shared knowledge/records: `/home/youssef/.openclaw/workspace`.

Useful checks:
```powershell
openclaw config validate
openclaw gateway status --json
openclaw skills check
opencode mcp list
opencode models ollama
node /home/youssef/.config/opencode/openclaw/runtime/verify.mjs
node /home/youssef/.config/opencode/openclaw/runtime/verify-live-mcps.mjs
node /home/youssef/.config/opencode/openclaw/runtime/probe-backends.mjs --services-only
node /home/youssef/.config/opencode/openclaw/runtime/verify-fluentbit.mjs
```

Core MCPs are native stdio processes, independent of the OpenClaw gateway. The user-requested 2026-09-13 repair enabled and authenticated all six remote CISO integrations using pinned runtimes and protected local credential loading. OpenSearch/Vault use private SSH relays; OpenSearch validates CA/hostname. A subsequent request added `ciso-fluentbit`, a six-tool read-only adapter for the installed Windows collector's API at 127.0.0.1:2020. Current verified native inventory: **19 connected, zero failed, three disabled**, out of 22 definitions. Consult the dated repair reports and recheck live state; source enablement/credentials are historical inputs, not the current native operational state.

For Eramba's private endpoint, connect the user-scoped OpenVPN GUI profile `fares-mcp` (server 139.59.152.129:1194/UDP, client 10.8.0.78). Run `opencode mcp list` before standalone OAuth verification so native authentication can refresh its cache. DigitalOcean/GitLab tokens expire 2026-12-12.

The channel bridge is `openclaw mcp serve --claude-channel-mode off` and requires a healthy gateway. Enabling that MCP does not start the gateway. Gateway startup can run BOOT.md and resume 11 cron jobs; include those effects when the user requests service activation.

Cron inventory is `/home/youssef/.openclaw/cron/jobs.json`; live status uses `openclaw cron list --all --json`. Inspect an existing job before editing or running it; preserve its ID and Asia/Riyadh schedule. A job run can send messages and execute recon.

Historical memory remains in the workspace and OpenClaw's memory index. Use native searches or `openclaw memory search --query "topic" --max-results 10` as appropriate. The OpenCode knowledge graph is a separate persistent file under `openclaw/data/`; it is not a converted copy of the old memory database.

OpenClaw OAuth profiles are runtime-specific. OpenCode uses its own provider authentication; source profile presence is not proof of usable OpenCode credentials. Five local Ollama models are available as explicit selections.

After configuration-time changes, quit and restart OpenCode. Use `customize-opencode` for schema or loader changes.
