---
name: node-connect
description: Use when troubleshooting an OpenClaw mobile/desktop node's gateway route, pairing request, setup code, authentication, or connection failure.
metadata:
  source: /home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/node-connect/SKILL.md
---

# OpenClaw node connectivity

Detailed diagnosis map: `/home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/node-connect/SKILL.md`.

Establish the intended topology: same machine, local network, tailnet or remote gateway. Read the exact client error and use `openclaw gateway status --json`, `openclaw devices list`, and `openclaw nodes status` as applicable.

The audited gateway is configured loopback-only at `127.0.0.1:18789`; this endpoint is only reachable on the local host. A remote node needs the actual configured route, not a copied localhost URL.

Resolve routing before pairing/authentication. If pairing is requested, inspect the specific pending device and its identity before approving it. If setup-code generation is needed, use the supported `openclaw qr` flow; setup codes and embedded authentication material are secrets and should not be reproduced in diagnostic logs.

Return one evidence-based diagnosis and the concrete next step. Verify connectivity after an authorized configuration change.
