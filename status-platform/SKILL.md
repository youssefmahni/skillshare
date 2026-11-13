---
name: status-platform
description: Use when operating status.darkcoders.com (components, incidents, maintenance, subscribers, badges) or diagnosing a probe/service state.
metadata:
  source: /home/youssef/.config/opencode/openclaw/runtime/customer_v34_routes.py
---

# Status platform

SSO-gated observability platform at `status.darkcoders.com`.

## Layout
- Engine: `darknesseye-framework-engine` (`/srv/framework-engine`, uvicorn
  `0.0.0.0:19000`), routes in `engine/customer_v34_routes.py`, prefix
  `/api/v1/v34`.
- Probe data: `/var/lib/ciso/status-probes/` on the engine droplet; timers every 60s.
- Ops facts: components, auto-incident state machine (PATCH
  `/status/incidents/{id}`), maintenance windows, subscribers (Brevo SMTP),
  badges `/status/badge/{service}.svg`, feed, Grafana dashboard, OpenSearch
  `ciso-status-probes-*`, Eramba incident sync + asset links.
- Key routes: `/status/components`, `/status/incidents`, `/status/uptime/{service}`,
  `/status/history`.

## Workflow
1. Health via ciso-labs MCP `labs_health` (key `status-engine`) or:
   ```
   curl https://status.darkcoders.com/api/v1/v34/status/components
   ```
2. Incident lifecycle via PATCH with SSO principal; verify Eramba
   `security_incidents` sync after every state change.
3. New estate service = add a component entry in v34 (id, name, probe spec,
   owner BU), deploy module, restart engine, confirm OpenSearch index starts.

## Rules
- Probes are authenticated via SSO where public paths are gated; do not bypass.
- Timestamps in reports: `Asia/Riyadh` with explicit UTC offset.
