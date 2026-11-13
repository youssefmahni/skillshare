---
name: ciso-stack
description: Use when reviewing or operating the OpenClaw CISO infrastructure stack, including Docker Compose, Grafana, OpenSearch, Fluent Bit, Logstash, Vault, GitLab, or Spaces evidence storage.
metadata:
  source: /home/youssef/.openclaw-stack/docker-compose.yml
---

# CISO infrastructure integration

Source stack: `/home/youssef/.openclaw-stack` (`@openclaw-stack`).
Read the migration audit at `/home/youssef/.config/opencode/openclaw/AUDIT.md` before relying on its wiring.

Identify whether the task concerns the local Compose stack or the separately configured remote service. Compare actual service state, endpoint and credential method to the current configuration.

Native MCP mappings: six authenticated remote integrations plus the local collector adapter, enabled on 2026-09-13:
- DigitalOcean: official `@digitalocean/mcp`; a dedicated PAT is loaded from `DIGITALOCEAN_API_TOKEN_FILE`.
- GitLab: maintained `@zereight/mcp-gitlab`; HTTPS API and a working `GITLAB_PERSONAL_ACCESS_TOKEN_FILE` override the old source placeholder.
- Grafana: official native Windows `mcp-grafana`; HTTPS endpoint and `GRAFANA_CREDENTIALS_FILE`, with service-account-token support.
- OpenSearch: official `opensearch-mcp-server-py` in Ubuntu WSL, using a private SSH relay and verified CA/hostname. Windows Application Control blocks an upstream NumPy dependency in Windows; credentials pass through WSLENV and the SSH key stays in Windows.
- Vault: official native Windows `vault-mcp-server` 0.2.0, private SSH relay and a protected `VAULT_TOKEN_FILE` containing the verified existing server token.
- Spaces: local AWS-SDK MCP for bucket/object listing, metadata, new-key evidence uploads and non-overwriting downloads.
- Local Fluent Bit: `ciso-fluentbit` connects to the existing Windows 3.2.7 monitoring API at `http://127.0.0.1:2020`. Six read-only tools cover status, JSON/Prometheus metrics, buffering, redacted disk configuration, reload count and sampled delivery deltas. Use `get_pipeline` for the actual `AppData/Local/DarkCoders/fluent-bit/fluent-bit.conf` pipeline; the Compose file describes another deployment.

Read `mcp-repairs.json`, `mcp-live-validation.json` and `mcp-private-validation.json` under `/home/youssef/.config/opencode/openclaw/` for dated evidence; verify current reachability before relying on it. DigitalOcean/GitLab PATs expire 2026-12-12. Use local credential files or environment overrides; never paste tokens into commands, reports or native configuration. Standalone OAuth checks use cached tokens, so run `opencode mcp list` first to refresh native authentication.

Local collector evidence is in `fluentbit-validation.json` in the same directory. Fluent Bit health covers a recent window; cumulative dropped-record/retry-failure counters and `sample_delivery` cover different time scopes. At the 2026-09-13 check the HTTP output had historical losses despite health `ok`. Report both observations and verify downstream acceptance before claiming delivery success.

Known source deployment issues include duplicate host port 9600, missing password-variable forwarding, datasource UID drift, audit-log path drift and multiline JSON ingestion mismatch. Treat local definitions as configuration evidence, not proof of a running or healthy deployment. Validate before a requested deployment/restart.
