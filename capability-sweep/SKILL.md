---
name: capability-sweep
description: Use when inventorying every connected MCP server, tool, or permission in OpenCode/OpenClaw — documenting what each tool can read/execute/write, which operations are gated by approval, and producing a read-only capability baseline report. Run on demand; never mutates system state during the sweep.
metadata:
  source: local (created for DarknessEye estate)
---

# Capability sweep (read-only MCP/tool inventory)

Produce a point-in-time, evidence-backed inventory of every connected MCP server and
native tool, classified by capability tier. The sweep itself must be **read-only**:
observing tools, health probes, and version queries only. The only artifacts written
are the report files. Never run tools that mutate state (prints, deletes, writes,
pauses, restarts) during a sweep.

## When to run

- User asks "what can you actually do / see / control?"
- Before or after installing/removing an MCP server
- Periodic baseline (e.g. monthly) to diff against the estate docs
- After an OpenClaw/OpenCode migration or config change

## Step 1 — Discovery from the host side

Start with the authoritative host-side listing, not memory:

```powershell
opencode mcp list
openclaw gateway status --json
openclaw skills check
```

Record: server name, status (connected/failed), tool count per server.

## Step 2 — Probe each server with read-only calls only

Call each server's *cheapest read-only* tool. Never call mutating tools during a sweep.

| Server | Safe probe (read-only) |
|---|---|
| bambu-forge | `health_check` |
| bambu-forge AI | `ai_providers_status` |
| bambu-forge slicer | `slicer_backends_status` |
| ciso-fluentbit | `ciso-fluentbit_get_status` |
| ciso-grafana | `ciso-grafana_user_info` |
| eramba | `eramba_health`, `eramba_list_modules` |
| excellib | `excellib_excellib` (action: status) |
| filesystem | `filesystem_list_allowed_directories` |
| git | run against a known repo, or skip if none |
| memory | `memory_read_graph` (may be large — search instead) |
| time | `time_get_current_time` (Asia/Riyadh) |
| chrome-devtools | `chrome-devtools_list_pages` |
| fetch / webfetch / websearch | skip live fetch; confirm registration via `opencode mcp list` |
| ciso-digitalocean | `ciso-digitalocean_account-get-information` |
| ciso-gitlab | `ciso-gitlab_health_check` |
| ciso-vault | `ciso-vault_list_mounts` |
| ciso-defense | `ciso-defense_defense_node_telemetry` |
| ciso-engineering | `ciso-engineering_engineering_node_telemetry` |
| ciso-governance | `ciso-governance_governance_node_telemetry` |
| ciso-investigation | `ciso-investigation_investigation_node_telemetry` |
| mobbin | registration-only (no zero-cost probe) |

A failed probe is a **finding, not a reason to skip**. Record exact error text.

## Step 3 — Classify every tool by tier

For each advertised tool, assign one tier:

- **R** — Read/observe only (status, list, get, search, health, snapshot)
- **X** — Execute, reversible (open app, navigate, slice, render, run safe command)
- **W** — Write, reversible with notice (create/edit files, patch profiles, create records)
- **G** — Gated: destructive/irreversible OR requires explicit approval
  (print, pause/stop print, delete, apply-fix, guarded writes, external messages,
  purchases, containment actions)

Gating sources to check (list all that apply):
1. OpenCode permission rules (`~/.config/opencode/` project + global config)
2. Tool-level `requires_confirmation` annotations (e.g. bambu-forge motor/G-code tools)
3. Server-side guarded-write flows (eramba dry-run + apply_token; DO tag/enable/disable wrappers)
4. Env disable flags (e.g. `ERAMBA_ENABLE_DELETE=false` disables deletes outright)

## Step 4 — Write the report

Write to `/home/youssef/.openclaw/workspace/reports/capability-sweep/<YYYY-MM-DD>-capability-sweep.md`:

1. **Summary table** — server → connected? → tools → R/X/W/G counts → notable failures
2. **Per-server sections** — tool list with tier, one-line purpose, gate source
3. **Deltas** — vs. previous report and vs. `@estate` baseline (57 droplets, port maps)
4. **Open questions** — servers registered but unprobed, ambiguous gates

Also record a machine-readable summary `<YYYY-MM-DD>-capability-sweep.json` with the
same counts for diffing.

## Rules

- Read-only during the sweep; only report files are written.
- No credentials, tokens, or secret-bearing config in the report — reference paths, not values.
- If a probe requires credentials that would echo secrets, skip it and mark `unprobed:auth-required`.
- Timestamp everything with `Asia/Riyadh` offset.
- A server being slow/unavailable: one retry, then record and move on.
- Never claim a capability you could not verify in this sweep — cite the probe result.
