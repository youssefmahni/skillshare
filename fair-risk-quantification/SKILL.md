---
name: fair-risk-quantification
description: Use when calculating Annualized Loss Expectancy (ALE), running 10,000-iteration Monte Carlo loss simulations, calibrating Beta-PERT probability distributions, or translating technical cyber threats into financial exposure figures.
metadata:
  frameworks: OpenFAIR (O-RA / O-RT), NIST SP 800-30 Rev 1, ISO/IEC 27005
  droplet: ciso-agent-defense (10.30.0.4) / ciso-agent-governance (10.30.0.20)
  assigned_personas: FAIR-001 (Dr. Yasser Al-Qahtani), RA-001, ERM-002
---

# OpenFAIR™ Quantitative Cyber Risk Modeling

**Operating Droplets:** `10.30.0.4` (`ciso-agent-defense`), `10.30.0.20` (`ciso-agent-governance`)  
**Lead Personas:** `FAIR-001` (FAIR Risk Quantification Specialist & Monte Carlo Simulation Analyst), `RA-001` (Senior Risk Assessment Analyst), `ERM-002` (Quantitative Risk Manager)

## Purpose & Scope
Replaces subjective risk matrices (High/Medium/Low) with defensible mathematical distributions of economic exposure. Computes Threat Event Frequency (TEF), Vulnerability (Threat Capability vs. Resistance Strength), Primary Loss, and Secondary Loss to produce Annualized Loss Expectancy (ALE) curves and Value-at-Risk (VaR) percentiles.

## Operational Workflow

1. **Parameter Calibration & Subject Matter Interviews:**
   - Elicit calibrated minimum, most likely, and maximum estimates for TEF and loss magnitudes using 90% confidence intervals.
   - Fit parameters to Beta-PERT distributions to avoid artificial Gaussian tails.

2. **Monte Carlo Stochastic Simulation:**
   - Execute 10,000 to 100,000 simulation trials combining Threat Event Frequency with Loss Magnitude distributions.
   - Generate Loss Exceedance Curves (LEC) showing probability of exceeding specific monetary loss levels ($100k, $1M, $10M).

3. **Financial KRI Generation:**
   - Compute Expected Annual Loss (mean ALE), Mode, and 95th percentile Value-at-Risk (95% VaR).
   - Compare ALE against the enterprise risk tolerance threshold defined by the Board.

4. **Integration with Eramba & Governance:**
   - Feed calibrated dollar figures into Eramba risk records (`ciso-governance_governance_score_fair_risk`).
   - Export financial loss curves to `BRD-GOV-001` for inclusion in quarterly Board Risk Committee briefings.
