---
name: ciso-engineering
description: Use when running SAST code reviews, auditing IaC (Terraform, Dockerfile, Cloud-Init) against CIS benchmarks, generating SBOMs, performing STRIDE threat modeling, or issuing Vault PKI certificates on ciso-agent-engineering.
metadata:
  framework: NIST SP 800-181 Rev 1 (NICE) - Design & Develop (DD)
  droplet: ciso-agent-engineering (10.30.0.21)
---

# NIST NICE Design & Develop (DD) Operations

**Target Environment:** `ciso-agent-engineering` (`10.30.0.21` / public `159.89.23.171`)  
**Core NICE Work Roles:**
- `DD-WRL-001`: Cybersecurity Architecture
- `DD-WRL-002`: Enterprise Architecture
- `DD-WRL-003`: Secure Software Development (OWASP Top 10, CWE)
- `DD-WRL-004`: Secure Systems Development (CIS Benchmarks, Hardening)
- `DD-WRL-005`: Software Security Assessment (SAST, DAST, SBOM)
- `DD-WRL-008`: Technology Research & Development
- `DD-WRL-009`: Operational Technology (OT) Cybersecurity Engineering

## Operational Workflow

1. **Static Application Security Testing (SAST):**
   - Call `ciso-engineering_engineering_sast_code_review` to scan code snippets or repositories for security vulnerabilities (CWE-89 SQL injection, CWE-94 command injection, CWE-798 hardcoded credentials).
   - Require remediation for any Critical or High severity findings before code merge.

2. **Infrastructure as Code (IaC) Security Audit:**
   - Audit Terraform manifests (`.tf`), Dockerfiles, and Cloud-Init files using `ciso-engineering_engineering_iac_security_audit`.
   - Validate against CIS Docker Benchmarks (e.g. non-root user enforcement, minimal package layers) and CIS Cloud Provider baselines (restricting open `0.0.0.0/0` ingress to administrative ports 22, 8200, 9200).

3. **Software Bill of Materials (SBOM) Generation:**
   - Call `ciso-engineering_engineering_sbom_generate` to parse package manifests (`package.json`, `requirements.txt`, `composer.json`).
   - Produce CycloneDX v1.5 compliant SBOM inventories and cross-reference with the Open Source Vulnerabilities (OSV) database.

4. **Architectural Threat Modeling:**
   - Call `ciso-engineering_engineering_threat_model` to analyze system components against the STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) and DREAD models.
   - Establish trust boundaries across the DigitalOcean VPC (`10.30.0.0/20`).

5. **Vault PKI Certificate Management:**
   - Call `ciso-engineering_engineering_vault_pki_issue` to issue internal X.509 SSL/TLS certificates through the HashiCorp Vault PKI engine (`3df-pki/` at `10.30.0.7:8200`).
   - Maintain automated key rotation and ensure all internal services enforce mTLS.

6. **Node Health:**
   - Inspect build worker and engineering daemon status with `ciso-engineering_engineering_node_telemetry`.
