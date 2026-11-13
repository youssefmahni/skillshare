---
name: weather
description: Use when checking current weather or a near-term forecast for a specified city, region, airport, or travel destination.
metadata:
  source: /home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/weather/SKILL.md
---

# Weather lookup

Source: `/home/youssef/AppData/Roaming/npm/node_modules/openclaw/skills/weather/SKILL.md`.

Resolve the actual location from the request. Query an HTTPS weather endpoint with native webfetch, the fetch MCP, or installed `curl.exe`, for example:

```powershell
curl.exe --fail --silent --show-error --max-time 20 "https://wttr.in/Riyadh?format=j1"
```

Return local observation/forecast time, units, conditions, temperature, precipitation and wind with a source citation. Distinguish observations from forecasts. Use official meteorological alerts for hazardous-weather questions and appropriate specialist sources for aviation, marine or historical data.
