---
name: ciso-console
description: Use when handling the migrated CISO dashboard, risks, assets, incidents, controls, compliance, morning/evening brief, posture, or source Telegram-style slash commands inside OpenCode.
metadata:
  source: /home/youssef/.openclaw/workspace/COMMANDS.md
---

# CISO console in OpenCode

Source routing: `/home/youssef/.openclaw/workspace/COMMANDS.md`.
Workspace: `/home/youssef/.openclaw/workspace`.

Use available Eramba tools for current GRC data and exact record/deep-link URLs. Follow the source's deep-link workflow for changes; use local working records only with clearly labeled provenance. Source tool names are conceptual until confirmed in the active tool inventory.

| Command | Workflow |
|---|---|
| ciso | Dashboard: summary counts, top five risks, open incidents, actual schedule status |
| risks / risk_new | Ranked risks / draft a new risk and link to the supported Eramba create flow |
| assets / asset_new | Asset inventory / prepare an asset-registration deep link |
| incident / incidents | Prepare an incident record / list open incidents with status and evidence |
| controls / compliance | Current security controls / packages, scope, coverage and evidence gaps |
| kev / kev_check | On-demand CISA KEV lookup and verified inventory matching; no forced cron run |
| recon | Load osint-recon; for installed pipeline operations also load discovery-engine |
| posture | Board-facing EN/AR posture using observed data and explicit gaps |
| brief_am / brief_pm | On-demand EN/AR brief; for PM compare actual morning evidence and decisions |
| vuln | Load vuln-triage for the requested CVE |
| phish | Analyze supplied content/IOCs with the phishing-response playbook and available tools |
| audit | Summarize actual OpenCode metadata audit or the specifically requested OpenClaw log |
| rag / rag_search | Search CISO sovereign knowledge base (NCA ECC, SAMA, estate baselines, SDLC) via ciso_rag_search |
| frameworks / playbooks | Read the corresponding workspace INDEX.md and relevant entries |
| help_cis | Explain these commands with practical examples |

Use normal OpenCode Markdown, source citations, appropriate severity, owners and actionable next steps. The source's Telegram MarkdownV2 escaping and message menus are specific to actual Telegram delivery. A brief in this chat does not automatically send a Telegram message.

If Eramba or a feed is unavailable, report that failure and distinguish cached data from current state. Do not convert a failed query into zero risks/incidents. Check actual governing sources before asserting legal reporting deadlines.
