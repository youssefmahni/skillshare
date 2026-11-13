---
name: browser-automation
description: Use when performing multi-step browser workflows, managing tabs, inspecting login state, filling forms, or recovering from stale elements with Chrome DevTools MCP.
metadata:
  source: /home/youssef/AppData/Roaming/npm/node_modules/openclaw/dist/extensions/browser/skills/browser-automation/SKILL.md
---

# Browser automation in OpenCode

The configured browser is `chrome-devtools`. Source workflow: `/home/youssef/AppData/Roaming/npm/node_modules/openclaw/dist/extensions/browser/skills/browser-automation/SKILL.md`.

1. List pages, select the intended page and reuse an appropriate existing tab.
2. Take an accessibility snapshot before interacting. Use only UIDs from the latest snapshot of that page.
3. Fill related form fields with the multi-field form tool when available. Prefer semantic click/fill actions to page scripts.
4. After navigation, submission, modal changes or stale-element errors, take a fresh snapshot. Retry a stale action once against the new state.
5. Wait for visible state or specific text rather than fixed sleeps. Verify successful completion with the resulting page state.
6. Describe actual login, permission, CAPTCHA or MFA blockers precisely from the visible interface.

OpenClaw `browser(action=...)`, labels such as `t1`, and `profile=user` do not map directly to Chrome DevTools tool parameters. The current server launches an isolated browser; existing personal-browser cookies are not implied. The source Patchright/Playwright entry is separately configured and disabled.
