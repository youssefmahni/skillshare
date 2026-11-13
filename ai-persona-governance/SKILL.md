---
name: ai-persona-governance
description: Use when auditing autonomous AI personas for prompt drift, verifying system instruction immutability, establishing ethical decision boundaries, or running adversarial jailbreak tests across the 334-persona DarkCoders workforce.
metadata:
  frameworks: NIST AI RMF 1.0, ISO/IEC 42001, SDAIA AI Ethics Principles
  droplet: ciso-agent-governance (10.30.0.20) / ciso-agent-engineering (10.30.0.21)
  assigned_personas: AIGOV-001 (Dr. Noura Al-Dosari), AIGOV-002 (Tariq Al-Ghamdi)
---

# AI Persona Governance & Prompt Drift Oversight

**Operating Droplets:** `10.30.0.20` (`ciso-agent-governance`), `10.30.0.21` (`ciso-agent-engineering`)  
**Lead Personas:** `AIGOV-001` (AI Persona Governance Specialist), `AIGOV-002` (LLM & Foundation Model Governance Specialist)

## Purpose & Scope
Governs the behavioral safety, identity integrity, and prompt boundaries of all 334 autonomous agent personas across DarkCoders. Ensures absolute immutability of core system prompts, adherence to SDAIA AI Ethics Principles, and compliance with the Delegation of Authority (DoA) boundary matrix.

## Operational Workflow

1. **System Prompt Immutability Verification:**
   - Audit target persona YAML/Markdown configurations against their canonical cryptographic SHA-256 signatures stored in HashiCorp Vault (`ciso/data/governance/ai-personas/*`).
   - Flag any unauthorized system prompt modifications, injected override clauses, or behavioral drift.

2. **Adversarial Jailbreak & Alignment Fuzzing:**
   - Coordinate with `AIRSK-001` to execute automated prompt injection resilience tests (direct injection, indirect RAG injection, roleplay bypass).
   - Evaluate model outputs against strict safety guardrails (unauthorized API calls, credential leaks, unapproved financial actions).

3. **Autonomous Boundary Enforcement:**
   - Verify that agent tool use conforms to least-privilege OPA policies (`ciso-opa`).
   - Intercept and block autonomous actions exceeding the assigned persona's operational scope.

4. **Audit Trail & Governance Reporting:**
   - Stream persona alignment scores and audit logs to OpenSearch cluster index `governance-ai-telemetry-*`.
   - Produce bi-weekly AI Workforce Governance Reports for the Board Ethics & Technology Committee.
