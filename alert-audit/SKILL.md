---
name: alert-audit
description: >
  Audit alerting rules for noise, missing coverage, and misconfiguration. Use when on-call engineers complain about alert fatigue or when setting up a new service.
---

# Alert Audit

## Checklist

- [ ] Every alert has a runbook link
- [ ] No alert fires more than 5×/day without an owner action
- [ ] P0 alerts page immediately; P1 within 5 min; P2 tickets only
- [ ] Thresholds validated against 30-day baseline
- [ ] Dedup/grouping configured (no alert storms)
- [ ] Alerts cover: latency p99, error rate, saturation, traffic (RED method)

## Actions

- Silence or delete alerts with >80% no-action rate
- Add `for:` duration to noisy threshold alerts
- Add missing runbooks (use `runbook-author` skill)
- Review alert-noise-report skill for weekly summary
