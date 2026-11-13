---
name: ear-minio
description: Upload/download evidence artefacts to MinIO WORM buckets, verify object lock status, and generate manifests. Use for all EAR evidence storage operations.
metadata:
  openclaw:
    requires:
      env: [MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY]
---

# EAR MinIO Skill

Manage WORM evidence buckets on the EAR MinIO instance.

## Environment

| Var | Description |
|---|---|
| `MINIO_ENDPOINT` | MinIO URL (e.g. `https://minio.knighteye.ai`) |
| `MINIO_ACCESS_KEY` | Access key |
| `MINIO_SECRET_KEY` | Secret key |

## Configure mc Client

```bash
mc alias set ear "$MINIO_ENDPOINT" "$MINIO_ACCESS_KEY" "$MINIO_SECRET_KEY"
```

## Upload Evidence File (WORM)

```bash
mc cp <local-file> ear/<bucket>/<path>
```

## Verify Object Lock (WORM status)

```bash
mc retention info ear/<bucket>/<object>
# Expected: COMPLIANCE mode, retention date in the future
```

## List Bucket Contents

```bash
mc ls ear/<bucket>/ --recursive
```

## Generate Manifest (SHA256 of all objects)

```bash
mc ls ear/<bucket>/ --recursive --json \
  | python3 -c "
import sys, json
for line in sys.stdin:
    obj = json.loads(line)
    print(obj.get('key'), obj.get('etag',''))
"
```

## Download Evidence File

```bash
mc cp ear/<bucket>/<path> <local-dest>
```

## Check Bucket WORM Policy

```bash
mc retention info ear/<bucket>
```

## Sync Reports Path Convention

`sync-reports/{date}/{time}_{trigger}_{sha}.json`

```bash
mc ls ear/sync-reports/$(date +%Y-%m-%d)/
```

## Execute-Verify-Report

After every upload:
1. Confirm `mc retention info` shows COMPLIANCE lock
2. Verify etag matches expected SHA256
3. Report: "Uploaded <file> to <bucket>/<path>, WORM lock confirmed"
