---
name: data-stewardship-governance
description: Use when cataloging enterprise data assets, classifying information sensitivity under Saudi NDMO / PDPL, validating data lineage, or managing retention and archival lifecycles across DarkCoders data stores.
metadata:
  frameworks: Saudi NDMO Interim Regulations, Saudi PDPL M/19, DAMA-DMBOK
  droplet: ciso-agent-governance (10.30.0.20)
  assigned_personas: DATA-GOV-001 (Reem Al-Harbi), DE-004 (Data Governance Architect)
---

# Enterprise Data Stewardship & NDMO Compliance

**Operating Droplet:** `10.30.0.20` (`ciso-agent-governance`)  
**Lead Personas:** `DATA-GOV-001` (Enterprise Data Steward & Information Architect), `DE-004` (Data Quality & Classification Governance Specialist)

## Purpose & Scope
Maintains the enterprise data catalog, authoritative taxonomy, and metadata classification schema across all relational databases, OpenSearch clusters, MinIO buckets, and document stores. Enforces compliance with National Data Management Office (NDMO) standards and the Saudi Personal Data Protection Law (PDPL).

## Operational Workflow

1. **Asset Classification & Schema Tagging:**
   - Classify all data repositories into 4 regulatory tiers: `PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, and `RESTRICTED`.
   - Ensure every customer, employee, or financial database field is tagged with appropriate sensitivity and retention policies.

2. **PDPL Data Retention & Archival Enforcement:**
   - Track data asset lifecycle from creation to statutory expiration (enforcing minimum and maximum retention periods).
   - Coordinate with DPO (`DPO-001`) to automate data erasure workflows across MinIO and PostgreSQL upon verified DSR request.

3. **Metadata & Lineage Auditing:**
   - Scan OpenSearch indexes, ClickHouse tables, and Eramba asset registers for untagged or orphaned schemas.
   - Cross-check data flows to ensure restricted PII does not cross unapproved network boundaries or leave sovereign jurisdiction.

4. **NDMO Governance Reporting:**
   - Compile enterprise data maturity assessments and compliance metrics for executive management and regulatory audit packs.
