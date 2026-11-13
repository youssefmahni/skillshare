---
name: plugin-wizard
description: Use when operating the Plug & Play Wizard platform at plugins.darkcoders.io (registry, flows, provisioners, activations, console) or debugging a provisioning run.
metadata:
  source: /home/youssef/.config/opencode/openclaw/runtime/customer_v117_routes.py
---

# Plugin Wizard platform

SSO-gated plug-and-play provisioning at `plugins.darkcoders.io` (realm
`customers`, client `plugins-oidc`), engine module
`engine/customer_v117_routes.py`, prefix `/api/v1/v117`.

## Facts
- 7 manifests (outlook, sentinel, sms, lab-agent, +3), wizard state per subject
  in Vault `ciso/data/plugins/wizard/<subject>/<plugin>`, activations under
  `ciso/data/plugins/activations/`.
- Provisioners: Outlook add-in, Sentinel browser guard, SMS personalized
  Shortcut/Tasker, lab-agent with real headscale preauth keys.
- Hardened (W4–W6): `_require_principal` on all mutations, rate limits
  (lab-submit 10/hr, step 120/hr, provision 30/day), telemetry fan-out to
  OpenSearch `ciso-plugin-events-*` and Eramba `security_incidents` type=event.
- Console SPA: `/var/www/plugins/console/index.html` (v3: resume card + health strip).
- Health: `/plugin/health`; resume: `/plugin/wizard/resume`.

## Workflow
1. Health via ciso-labs MCP `plugins_status` or `/plugin/health`.
2. Provisioning debugging: read Vault wizard state, check Eramba event rows
   (`reporter='plugin-wizard'`) and OpenSearch event index for the attempt.
3. Console edits: local file
   `/home/youssef/.config/opencode/openclaw/runtime/plugins-console-index.html`,
   deploy to `/var/www/plugins/console/`.

## Rules
- Mutating endpoints require a real SSO principal; never weaken `_require_principal`.
- Rate-limit files are per-worker flock'd; verify multi-worker behavior after edits.
