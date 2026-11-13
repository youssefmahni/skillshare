---
name: discovery-engine
description: Use when operating or reviewing the configured OpenClaw external/internal discovery scripts, comparing recon runs, or reconciling attack-surface findings with the risk register.
metadata:
  source: /home/youssef/.openclaw/workspace/skills/discovery-engine/SKILL.md
---

# Discovery workflow

Workspace: `/home/youssef/.openclaw/workspace`.
Source: `/home/youssef/.openclaw/workspace/skills/discovery-engine/SKILL.md`.

Read `compliance/discovery-config.json` and the relevant script before running it. Establish the requested organization and operation from the user's task and the recorded ROE. Internal discovery is configured disabled.

Actual script invocations, with the shell tool's workdir set to the workspace:

```powershell
pwsh -NoProfile -File scripts/external-recon.ps1 -OrgId darkcoders -SkipBruteforce
pwsh -NoProfile -File scripts/findings-diff.ps1 -NoPush
pwsh -NoProfile -File scripts/internal-recon.ps1 -DryRun
```

Important implementation facts:
- Actual external output is `compliance/attack-surface/runs/<timestamp>/<org>/`, with `all-findings.json` in the run directory. The older skill documents a different layout.
- `-SkipBruteforce` still performs HTTP/TLS probes. It is not a passive-only or TLS/DNS-only mode.
- The external script also prunes old runs. Review that behavior when operating on evidence histories.
- `findings-diff.ps1 -NoPush` writes a diff while suppressing outbound messages.
- `risk-register-merge.ps1` writes the local register and closes absent findings across all organizations. A partial/single-org/failed run must not be fed into that auto-close logic.
- Internal scanner configuration currently uses `T2`, while the script prefixes `-T`; correct the resulting `-TT2` issue before enabling scans. Greenbone, NetBox and SNMP sections are stubs.

Reconcile differences against run completeness and Eramba. Preserve uncertain findings as unverified. Cron execution remains owned by OpenClaw; use `openclaw-operations` for schedules.
