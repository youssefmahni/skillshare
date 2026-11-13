---
name: exploratory-qa-hunter
description: Automated exploratory bug hunting, click-path auditing, error interception, and high-precision Jira bug ticket filing protocol for enterprise web applications.
---

# Exploratory QA Hunter Protocol

## 1. When to Use
Use this skill when auditing a running deployment (e.g. `https://proseed.darkcoders.com/`) for runtime defects, broken user interactions, visual regression, unhandled API rejections, and server-side exceptions.

## 2. The 4-Layer Inspection Routine

### Layer 1: Visual & Layout Integrity
- Inspect touch target sizes ($\ge 44\text{px}$ on interactive elements).
- Check contrast against background in both light (`#f6f9fc`) and dark (`#0e1326`) modes.
- Verify Argon DS v2 token usage: borders must be subtle (`var(--color-border-default)`), cards must have generous padding, empty states must render `.empty-icon` and supportive copy.
- Detect horizontal overflow, clipped text, or broken mobile viewports.

### Layer 2: Interactive Click-Paths & Forms
- Probe form submissions with edge cases:
  - Empty required inputs
  - Extreme numerical boundaries (e.g., negative leave balance, 99999 overtime hours)
  - Long strings and multi-byte Arabic Unicode characters (e.g., "تجربة تعديل البيانات الشخصية")
  - Rapid double-clicks to verify button disable/loading states and idempotency.

### Layer 3: Network & API Health
- Verify HTTP response status codes:
  - Client errors: `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`
  - Server crashes: `500 Internal Server Error`, `502 Bad Gateway`, `504 Gateway Timeout`
- Inspect API payloads for schema compliance (OpenAPI contract match).
- Measure response latency; flag endpoints exceeding $800\text{ms}$.

### Layer 4: Runtime Exception Interception
- **Client Console:** Intercept `ChunkLoadError`, React Hydration Mismatch, and unhandled Promise rejections.
- **Server Journal:** Tail systemd logs (`journalctl -u proseed -n 100`) for Next.js Invariant errors, MongoDB query timeouts, or uncaught Node.js exceptions.

## 3. Deduplication & Jira Ticket Creation Rules
1. **Search Before Filing:** Run JQL `project = PSEED AND status != Done AND summary ~ "keyword"` to ensure the defect is not already in progress or reported.
2. **Standard Issue Type:** Always file as `Bug`.
3. **Structured Ticket Schema:**
   - **Summary:** `[Module] Specific failure symptom` (e.g., `[Services] Salary Certificate download returns 500 when employee has no national ID`)
   - **Environment:** Live URL, authenticated role (`hr_admin` vs `employee`), viewport.
   - **Steps to Reproduce:** Numbered, deterministic steps from login to failure.
   - **Expected vs Actual:** Exact contrast of intended vs broken behavior.
   - **Evidence:** Browser console error stack or server journal snippet.
   - **Assignee Routing:**
     - UI/Visual/Responsive → Linda Vega (`APP-BUILDER`)
     - Backend/API/Mongo/Calculations → Service Builder (`SERVICE-BUILDER`)
     - Auth/RBAC/Security → Christine Padilla (`CISO-OFF-003`)
