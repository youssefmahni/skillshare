---
name: estate-navigator
description: Use when navigating, querying, or verifying the authoritative CISO Estate documentation (57 droplets, 318 AI workforce personas, port maps, VPC CIDRs, data stores, identity, fleet health, or external attack surface).
metadata:
  source: /home/youssef/Desktop/CISO-DarknessEye/02_Estate/
  reference: "@estate"
---

# CISO Estate Navigator

The authoritative single source of truth for the organization's infrastructure is located at:
`/home/youssef/Desktop/CISO-DarknessEye/02_Estate/` (also accessible as `@openclaw/estate/`).

All agents, playbooks, and commands must treat these 12 files as the ground-truth operational baseline.

## Estate Map & Routing Index

| Inquiry Topic | Target File | Key Content |
|---|---|---|
| **Droplets & Fleet Roster** | `01_Droplet_Inventory.md` | 57 droplets, 7 regions, hardware tiers, pricing, persona worker allocations (121 on defense, 120 on governance, etc.). |
| **Ports & Services** | `02_Service_Catalog.md` | 60+ listening ports on `ciso-openclaw`, 412 systemd units, 1,800+ FastAPI endpoints (port 19000), 26 HTTPS Caddy vhosts. |
| **VPC & Network Ingress/Egress** | `03_Network_and_Exposure.md` | VPC CIDRs (`10.30.0.0/20` in FRA1, `10.120.0.0/20` in SFO2), Tailscale overlay (`100.64.0.0/10`), Cloud Firewalls, public IPs. |
| **Databases & Stores** | `04_Data_Stores.md` | Eramba MySQL 8.4 (`10.30.0.3:3306`), OpenSearch (`10.30.0.8:9200`), Redis (`6379`, `6380`), MinIO/Spaces buckets, Vault KV-v2. |
| **Identity & Access** | `05_Identity_and_Access.md` | Keycloak realms (`darkcoders`, `internal`, `customers`), Authelia OIDC, OPA policy engine (8181), SSH keys. |
| **Application Architecture** | `06_Application_Architecture.md` | FastAPI Framework Engine, Redis BRPOP hot-path queues, Eramba-driven persona workforce orchestration (`Z.91`). |
| **Fleet Health & Timers** | `07_Fleet_Health.md` | 164 systemd timers, failed service diagnostics, Fluent Bit collector pipelines (`2020`), Prometheus metrics. |
| **Deep Service Inspections** | `08_Service_Deep_Inspection.md` | CAPE sandbox worker bindings (`10.30.0.6`), Telethon workers, background daemons. |
| **Core Service Specs** | `09_Core_Service_Inspection.md` | Dedicated profiles for Vault, OpenSearch, Logstash, Grafana, GitLab CE. |
| **Git Repositories & CI/CD** | `10_Source_and_Release_Inspection.md` | GitLab repository hierarchy, `.gitlab-ci.yml` pipeline stages, build provenance. |
| **Deployed Releases & Drift** | `11_Deployed_Release_Inspection.md` | Git commit hashes vs. on-disk filesystem hashes, virtualenv locks, config drift analysis. |
| **Perimeter & Attack Surface** | `12_External_Surface_Inspection.md` | External DNS zones (`darkcoders.com`, `knighteye.ai`), SSL/TLS certs, CDN edge exposure. |

## Investigation Pattern

1. Locate the relevant document from the index above.
2. Search file contents using `grep` or read sections with `read`.
3. Cross-reference the documented baseline against live state:
   - For droplets: `doctl compute droplet get <id>`
   - For remote services: specialized droplet MCP tools (`defense_node_telemetry`, `governance_eramba_sync`, etc.)
   - For database/vault: `ciso-vault` and `ciso-opensearch` tools
4. Cite the exact document number, section header, and timestamp when delivering answers.
