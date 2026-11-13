---
name: ai-model-risk
description: Use when assessing AI/LLM model vulnerabilities, measuring hallucination and toxic output rates, auditing model weights and training provenance, or scoring prompt injection exploitability.
metadata:
  frameworks: NIST AI RMF 1.0, ISO/IEC 42001, OWASP Top 10 for LLM Applications
  droplet: ciso-agent-engineering (10.30.0.21)
  assigned_personas: AIRSK-001 (Dr. Muna Al-Subaie), AISFE-002, DE-004
---

# AI Model Risk Management (MRM) & Algorithmic Vulnerability Assessment

**Operating Droplet:** `10.30.0.21` (`ciso-agent-engineering`)  
**Lead Personas:** `AIRSK-001` (AI & LLM Model Risk Specialist), `AISFE-002` (AI Model Risk Specialist & Red-Team Analyst), `DE-004` (Data Asset Risk & Pipeline Exposure Specialist)

## Purpose & Scope
Quantifies and manages the operational, security, and algorithmic risks associated with foundation models, fine-tuned weights, embeddings, and generative AI agents. Evaluates susceptibility to prompt injection, training data poisoning, model inversion, and catastrophic hallucinations.

## Operational Workflow

1. **Model Inventory & Provenance Verification:**
   - Catalog all open-weights models, proprietary API endpoints, and embedding vectors utilized across DarkCoders platforms.
   - Verify cryptographic hashes of downloaded model weights and validate training dataset provenance to prevent supply-chain backdoors.

2. **OWASP LLM Top 10 Red-Teaming:**
   - Execute automated stress tests against the LLM gateway evaluating:
     * LLM01: Prompt Injection (Direct & Indirect)
     * LLM02: Sensitive Information Disclosure
     * LLM03: Supply Chain Vulnerabilities
     * LLM04: Data and Model Poisoning
     * LLM06: Excessive Agency & Unsafe Tool Execution
     * LLM08: Vector and Embedding Weaknesses
     * LLM09: Misinformation & Hallucination Rates

3. **Quantitative Loss & Drift Metrics:**
   - Score hallucination probability across reasoning and retrieval tasks, establishing a hard error budget ($\le 1.2\%$).
   - Monitor embedding drift in vector databases (Qdrant on `10.30.0.16`) and benchmark output degradation over time.

4. **Remediation & Guardrail Tuning:**
   - Recommend structural guardrails, system prompt hardening, and token filtering rules to `AIGOV-001` for policy enforcement.
