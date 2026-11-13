---
name: estate-asset-sync
description: Use when syncing the discovered DarkCoders estate (DO droplets, platform services, DNS) into Eramba assets and business-unit links, or auditing asset/BU coverage.
metadata:
  source: /home/youssef/.config/opencode/openclaw/runtime/
---

# Estate asset sync

Eramba is the GRC source of truth. This skill keeps its asset register aligned
with the live estate discovered via the DigitalOcean API and platform modules.

## Facts
- Eramba MySQL: `10.30.0.3`, db `docker`, root creds from Vault `ciso/data/eramba/db-root`.
- Table `assets` uses column `name` (not asset_name); BU linking is the
  `assets_business_units` join table; `asset_label_id=1` (CISO Infrastructure);
  `asset_media_type_id`: 4 Hardware, 5 Software, 6 IT Service, 7 Network.
- 57 DO droplets are registered as `[DO:Droplet] <name>`; platform assets use
  `[Platform:<kind>] <name>`.
- BU ids of note: 33 SOC, 26 Platform Engineering, 35 Threat Intel, 68 Malware
  Analysis Lab, 39 CISO Office, 27 SRE, 28 DevOps, 34 Detection Eng.

## Workflow
1. Inventory live estate: `GET /api/v1/v118/labs/inventory` (ciso-labs MCP
   `labs_inventory`) or the DO API via Vault PAT `ciso/data/digitalocean/pat`.
2. Compare with `SELECT id, name FROM assets WHERE deleted=0`.
3. Run the idempotent sync script (runs on the bastion):
   ```powershell
   node C:\Users\DarknessEye\.config\opencode\openclaw\runtime\deploy-estate.mjs
   ```
   or push `runtime/eramba-sync-assets.py` to the bastion and run it with the
   engine venv python.
4. Verify: `orphan_assets_remaining` should be ≤ 8 (pre-program legacy assets).

## Rules
- Never delete or rename existing assets; only add and link.
- BU links are additive; use `INSERT ... WHERE NOT EXISTS` semantics.
- A scan absence is not proof of completeness: re-run the DO inventory.
- Record sync runs in the session summary; Eramba row ids are the proof.
