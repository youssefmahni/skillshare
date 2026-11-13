---
name: dns-governance
description: Use when operating the dual-provider DNS reconciler (DigitalOcean + GoDaddy), adding/auditing darkcoders domains records, or reconciling DNS with estate assets.
metadata:
  source: /home/youssef/.config/opencode/openclaw/runtime/ciso-dns-reconciler.py
---

# DNS governance

## Facts
- `darkcoders.com` + `darkcoders.io` zones live in DigitalOcean (PAT in Vault
  `ciso/data/digitalocean/pat`). GoDaddy API key covers `darkcoders.io` and ~90
  other domains; it was invalid for `darkcoders.com` (verified).
- Reconciler: `runtime/ciso-dns-reconciler.py` on the engine droplet, daily timer;
  `ciso-signupcom-watcher.timer` flips the engine when a record resolves.
- Read all records via ciso-labs MCP `dns_records` or `/api/v1/v118/labs/dns`.

## Workflow
1. Audit current records: ciso-labs `dns_records`.
2. Changes go through the reconciler script, never manual `doctl` one-offs.
3. After any A/CNAME change, wait one TTL and verify resolution from the bastion
   (`getent hosts <name>`) and note the resolver used.
4. Sync new public hostnames into Eramba as assets (skill `estate-asset-sync`).

## Rules
- Keep TTLs at 600 unless a change requires lower.
- Evidence: record the API response id per record change in the session report.
