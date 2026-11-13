---
name: lab-portal
description: Use when operating the malware/observables lab (CAPE, MobSF, IntelOwl), MISP/OpenCTI intel platforms, headscale nodes, or triaging a lab submission.
metadata:
  source: /home/youssef/.config/opencode/openclaw/runtime/customer_v118_routes.py
---

# Lab portal & threat platforms

Read-only estate API at `/api/v1/v118` (Bearer token in Vault
`ciso/data/labs/mcp-token`), surfaced locally as the ciso-labs MCP.

## Services
| Service | Host | Probe |
|---|---|---|
| IntelOwl | 10.30.0.19:80 | http 200 |
| CAPE | 10.30.0.6:8000 | /apiv2/ |
| MobSF | 10.30.0.6:8765 | 401 = alive |
| MISP | 10.30.0.14:443 | https 200 |
| OpenCTI | 10.30.0.13:8080 | http 200 |
| headscale | 10.30.0.18:8080 | 404 = alive |
| vpn-mcp | vpn-mcp.darkcoders.io | 401 = alive |

## Workflow
1. Health: ciso-labs MCP `labs_health`.
2. Searches: `misp_search(value, type)`, `opencti_search(text)` (both read-only;
   keys auto-resolved from Vault `ciso/data/misp/*`, `ciso/data/opencti/*`).
3. CAPE detonation: `cape_task(id)`; full submissions via the wizard lab engine
   (`/api/v1/v117/plugin/lab/submit`, principal + rate-limited).
4. IntelOwl ops: compose stack in `/opt/IntelOwl/docker` on ciso-intelowl with
   files `default.yml` + `postgres.override.yml` + `redis.override.yml` +
   `nginx.override.yml`; containers `intelowl_{nginx,uwsgi,daphne,postgres,redis,
   celery_beat,celery_worker_default}`. If nginx crash-loops: `host not found in
   upstream "uwsgi"` means uwsgi is down (OOM exit 137 → start container, watch
   memory); if beat crash-loops, check postgres is running.

## Rules
- Do not detonate samples outside CAPE; log hashes of anything submitted.
- MISP/OpenCTI search results are TLP-scoped data — treat as sensitive.
