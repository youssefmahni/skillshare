#!/usr/bin/env python3
"""
Apple Human Interface Guidelines corpus sync.

Crawls the official HIG markdown endpoints, stores a raw snapshot, produces
cleaned markdown for the DarkCoders RAG server, and optionally uploads changed
pages.

Usage:
  ./hig_sync.py                     # crawl + build local corpus
  ./hig_sync.py --upload            # crawl + upload changed pages
  ./hig_sync.py --upload --force    # re-upload every page
  ./hig_sync.py --verify            # check RAG ledger + test queries
  ./hig_sync.py --limit 5 --upload  # smoke test
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import hashlib
import json
import os
import re
import shutil
import sys
import threading
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = "https://developer.apple.com"
HIG_ROOT = "/design/human-interface-guidelines"
INDEX_PATH = HIG_ROOT
DEFAULT_OUT = Path("~/.config/opencode/knowledge/apple-hig").expanduser()
SKILL_REFS = Path("~/.config/opencode/skills/apple-hig/references").expanduser()
DEFAULT_RAG_BASE = "https://framework.darkcoders.com/api/v1/rag"
USER_AGENT = "DarkCoders-HIG-Sync/1.0 (+internal design knowledge sync)"
ROOTS = ["getting-started", "foundations", "patterns", "components", "inputs", "technologies"]
COMPONENT_CATEGORIES = [
    "content",
    "layout-and-organization",
    "menus-and-actions",
    "navigation-and-search",
    "presentation",
    "selection-and-input",
    "status",
    "system-experiences",
]
PRETTY = {
    "getting-started": "Getting started",
    "foundations": "Foundations",
    "patterns": "Patterns",
    "components": "Components",
    "inputs": "Inputs",
    "technologies": "Technologies",
    "ios": "iOS",
    "ipados": "iPadOS",
    "macos": "macOS",
    "tvos": "tvOS",
    "visionos": "visionOS",
    "watchos": "watchOS",
    "ui": "UI",
    "sf": "SF",
}

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": USER_AGENT,
    "Accept": "text/markdown, text/plain, */*",
})


def log(msg: str) -> None:
    print(msg, flush=True)


def pretty(slug: str) -> str:
    words = slug.replace("--", "/").replace("-", " ").split()
    small = {"and", "of", "the", "for", "to", "in", "on"}
    rendered = []
    for index, word in enumerate(words):
        key = word.lower()
        if index > 0 and key in small:
            rendered.append(key)
        else:
            rendered.append(PRETTY.get(key, word.capitalize()))
    return " ".join(rendered)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def url_for(path: str) -> str:
    return BASE + path


def md_url(path: str) -> str:
    return url_for(path) + ".md"


def normalize_link(link: str) -> str | None:
    link = link.strip()
    if not link or link.startswith("#"):
        return None
    parsed = urllib.parse.urlparse(link)
    if parsed.netloc and parsed.netloc != "developer.apple.com":
        return None
    path = parsed.path.lower().rstrip("/")
    if path.endswith(".md"):
        path = path[:-3]
    if not path.startswith(HIG_ROOT):
        return None
    return path


def extract_links(markdown: str) -> list[str]:
    found: list[str] = []
    for match in re.findall(r"\[[^\]]*\]\(([^)\s]+)", markdown):
        path = normalize_link(match)
        if path and path not in found:
            found.append(path)
    return found


def slug_for(path: str) -> str:
    suffix = path[len(HIG_ROOT):].strip("/")
    return suffix or "index"


def fetch_markdown(path: str) -> tuple[str | None, str | None]:
    """Fetch a HIG page as markdown, resolving Apple's HTML redirects."""
    for attempt in range(3):
        try:
            response = SESSION.get(md_url(path), timeout=40)
            if response.status_code == 200 and "markdown" in response.headers.get("content-type", ""):
                return response.text, path
            if response.status_code == 404 or "markdown" not in response.headers.get("content-type", ""):
                html = SESSION.get(url_for(path), timeout=40, allow_redirects=True)
                final = urllib.parse.urlparse(html.url).path.lower().rstrip("/")
                if final != path:
                    retry = SESSION.get(md_url(final), timeout=40)
                    if retry.status_code == 200 and "markdown" in retry.headers.get("content-type", ""):
                        return retry.text, final
            if response.status_code >= 500:
                time.sleep(1 + attempt)
                continue
            return None, None
        except requests.RequestException:
            time.sleep(1 + attempt)
    return None, None


def parse_metadata(markdown: str) -> dict:
    match = re.match(r"^\s*<!--\s*(\{.*?\})\s*-->\s*", markdown, re.S)
    if not match:
        return {}
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return {}


def title_from(markdown: str, meta: dict) -> str:
    if meta.get("title"):
        return meta["title"]
    match = re.search(r"^#\s+(.+)$", markdown, re.M)
    return match.group(1).strip() if match else "Untitled"


def heading_count(markdown: str) -> int:
    return len(re.findall(r"^#{2,4}\s+\S", markdown, re.M))


def clean_markdown(raw: str, url: str, section: str, snapshot: str) -> str:
    """Produce RAG-friendly markdown with provenance and no image URLs."""
    text = re.sub(r"^\s*<!--\s*\{.*?\}\s*-->\s*", "", raw, count=1, flags=re.S)
    text = re.sub(r"<img\b[^>]*>", "", text, flags=re.I)
    text = re.sub(r"<picture\b.*?</picture>", "", text, flags=re.I | re.S)

    def image_repl(match: re.Match) -> str:
        alt = match.group(1).strip()
        return f"[Image: {alt}]" if alt else "[Image]"

    text = re.sub(r"!\[(.*?)\]\([^()]*\)", image_repl, text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    provenance = f"> Source: {url}\n> Section: {section}\n> Snapshot: {snapshot}\n"
    match = re.search(r"^#\s+.+$", text, re.M)
    if match:
        insert_at = match.end()
        text = text[:insert_at] + "\n\n" + provenance + text[insert_at:]
    else:
        text = provenance + "\n" + text

    return text.rstrip() + "\n"


def crawl(workers: int) -> dict[str, dict]:
    pages: dict[str, dict] = {}
    queue: list[str] = [INDEX_PATH]
    seen: set[str] = set()
    lock = threading.Lock()

    def worker(path: str):
        raw, final_path = fetch_markdown(path)
        return path, final_path, raw

    pending = {INDEX_PATH}
    while pending:
        batch = sorted(pending)
        pending = set()
        with futures.ThreadPoolExecutor(max_workers=workers) as pool:
            results = list(pool.map(worker, batch))
        for requested, final_path, raw in results:
            if raw is None:
                log(f"  !! failed: {requested}")
                continue
            path = final_path or requested
            with lock:
                if path in seen:
                    continue
                seen.add(path)
                meta = parse_metadata(raw)
                title = title_from(raw, meta)
                pages[path] = {
                    "path": path,
                    "slug": slug_for(path),
                    "url": url_for(path),
                    "title": title,
                    "role": meta.get("role", ""),
                    "raw": raw,
                    "headings": heading_count(raw),
                    "bytes": len(raw.encode()),
                }
                for link in extract_links(raw):
                    if link not in seen:
                        pending.add(link)
        log(f"  crawled {len(seen)} pages (batch {len(batch)})")
    return pages


def build_sections(pages: dict[str, dict], workers: int) -> dict[str, str]:
    section_of: dict[str, str] = {INDEX_PATH: "Overview"}
    for root in ROOTS:
        path = f"{HIG_ROOT}/{root}"
        if path not in pages:
            continue
        label = PRETTY[root]
        section_of.setdefault(path, label)
        children = [p for p in extract_links(pages[path]["raw"]) if p != path]
        if root == "components":
            for category in children:
                category_label = f"{label} / {pretty(slug_for(category))}"
                section_of.setdefault(category, category_label)
                if category in pages:
                    for child in extract_links(pages[category]["raw"]):
                        if child != category:
                            section_of.setdefault(child, category_label)
        else:
            for child in children:
                section_of.setdefault(child, label)
    for path in pages:
        section_of.setdefault(path, "Other")
    return section_of


def build_corpus(pages: dict[str, dict], sections: dict[str, str], out_dir: Path) -> list[dict]:
    snapshot = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    raw_dir = out_dir / "pages"
    rag_dir = out_dir / "rag"
    raw_dir.mkdir(parents=True, exist_ok=True)
    rag_dir.mkdir(parents=True, exist_ok=True)

    entries: list[dict] = []
    for path in sorted(pages):
        page = pages[path]
        section = sections.get(path, "Other")
        slug = page["slug"]
        flat = slug.replace("/", "--")
        raw_file = raw_dir / f"{flat}.md"
        rag_file = rag_dir / f"apple-hig__{flat}.md"

        raw_bytes = page["raw"].encode()
        raw_file.write_bytes(raw_bytes)
        cleaned = clean_markdown(page["raw"], page["url"], section, snapshot)
        rag_bytes = cleaned.encode()
        rag_file.write_bytes(rag_bytes)

        entries.append({
            "slug": slug,
            "path": path,
            "url": page["url"],
            "title": page["title"],
            "section": section,
            "role": page.get("role", ""),
            "headings": page.get("headings", 0),
            "bytes": len(raw_bytes),
            "sha256": sha256_bytes(raw_bytes),
            "raw_file": str(raw_file.relative_to(out_dir)),
            "rag_file": str(rag_file.relative_to(out_dir)),
            "rag_sha256": sha256_bytes(rag_bytes),
            "last_uploaded_sha256": None,
            "last_uploaded_at": None,
        })

    manifest_path = out_dir / "manifest.json"
    previous: dict[str, dict] = {}
    if manifest_path.exists():
        try:
            previous = {p["slug"]: p for p in json.loads(manifest_path.read_text()).get("pages", [])}
        except Exception:
            previous = {}
    for entry in entries:
        old = previous.get(entry["slug"])
        if old and old.get("rag_sha256") == entry["rag_sha256"]:
            entry["last_uploaded_sha256"] = old.get("last_uploaded_sha256")
            entry["last_uploaded_at"] = old.get("last_uploaded_at")

    removed = sorted(set(previous) - {e["slug"] for e in entries})
    manifest = {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": BASE + HIG_ROOT,
        "snapshot": snapshot,
        "page_count": len(entries),
        "total_bytes": sum(e["bytes"] for e in entries),
        "removed_since_last_run": removed,
        "pages": entries,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2))

    write_index(out_dir, manifest)
    write_platform_map(out_dir, entries, pages)
    if SKILL_REFS.parent.exists():
        SKILL_REFS.mkdir(parents=True, exist_ok=True)
        shutil.copy2(out_dir / "index.md", SKILL_REFS / "index.md")
        shutil.copy2(out_dir / "platform-map.md", SKILL_REFS / "platform-map.md")
    return entries


def write_index(out_dir: Path, manifest: dict) -> None:
    lines = [
        "# Apple Human Interface Guidelines — Corpus Index",
        "",
        f"Snapshot: {manifest['snapshot']}  ",
        f"Pages: {manifest['page_count']}  ",
        f"Source: {manifest['source']}",
        "",
    ]
    grouped: dict[str, list[dict]] = {}
    for entry in manifest["pages"]:
        grouped.setdefault(entry["section"], []).append(entry)
    order = ["Overview", "Getting started", "Foundations", "Patterns", "Components", "Inputs", "Technologies", "Other"]
    for section in order + sorted(s for s in grouped if s not in order):
        items = grouped.get(section)
        if not items:
            continue
        lines.append(f"## {section}")
        lines.append("")
        for entry in sorted(items, key=lambda e: e["title"].lower()):
            lines.append(f"- [{entry['title']}]({entry['url']}) — `{entry['slug']}` · {entry['bytes']//1024} KB")
        lines.append("")
    (out_dir / "index.md").write_text("\n".join(lines))


def write_platform_map(out_dir: Path, entries: list[dict], pages: dict[str, dict]) -> None:
    platforms = {
        "iOS": ["ios", "iphone"],
        "iPadOS": ["ipados", "ipad"],
        "macOS": ["macos", "mac"],
        "tvOS": ["tvos", "apple tv"],
        "visionOS": ["visionos", "vision pro"],
        "watchOS": ["watchos", "apple watch"],
        "Liquid Glass": ["liquid glass"],
    }
    lines = [
        "# HIG Platform Map",
        "",
        "Pages with a platform-specific heading, a platform-specific title, or at least four mentions.",
        "",
    ]
    for label, needles in platforms.items():
        hits = []
        for entry in entries:
            raw = pages[entry["path"]]["raw"]
            title = entry["title"].lower()
            headings = " ".join(re.findall(r"^#{2,4}\s+(.+)$", raw, re.M)).lower()
            body = raw.lower()
            mentions = sum(body.count(needle) for needle in needles)
            if any(n in title for n in needles) or any(n in headings for n in needles) or mentions >= 4:
                hits.append(entry)
        lines.append(f"## {label} ({len(hits)} pages)")
        lines.append("")
        for entry in sorted(hits, key=lambda e: e["title"].lower()):
            lines.append(f"- [{entry['title']}]({entry['url']})")
        lines.append("")
    (out_dir / "platform-map.md").write_text("\n".join(lines))


def upload(entries: list[dict], out_dir: Path, rag_base: str, changed_only: bool, workers: int) -> None:
    endpoint = rag_base.rstrip("/") + "/api/v1/ingest/upload"
    queue = []
    for entry in entries:
        if changed_only and entry.get("last_uploaded_sha256") == entry["rag_sha256"]:
            continue
        queue.append(entry)

    log(f"Upload: {len(queue)} page(s) to {endpoint}")
    if not queue:
        return

    manifest_path = out_dir / "manifest.json"
    lock = threading.Lock()
    stats = {"indexed": 0, "skipped": 0, "failed": 0}
    by_slug = {e["slug"]: e for e in entries}

    def push(entry: dict):
        path = out_dir / entry["rag_file"]
        filename = f"apple-hig__{entry['slug'].replace('/', '--')}.md"
        last_error = None
        for attempt in range(4):
            try:
                with path.open("rb") as handle:
                    response = requests.post(
                        endpoint,
                        files={"file": (filename, handle, "text/markdown")},
                        data={"domain": "hig", "framework": "APPLE_HIG", "classification": "INTERNAL"},
                        timeout=180,
                    )
                if response.status_code == 200:
                    payload = response.json()
                    return entry, payload, None
                last_error = f"HTTP {response.status_code}: {response.text[:200]}"
            except Exception as exc:  # noqa: BLE001
                last_error = str(exc)
            time.sleep(2 ** attempt)
        return entry, None, last_error

    with futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for entry, payload, error in pool.map(push, queue):
            with lock:
                if error:
                    stats["failed"] += 1
                    log(f"  FAIL {entry['slug']}: {error}")
                    continue
                live = by_slug[entry["slug"]]
                live["last_uploaded_sha256"] = live["rag_sha256"]
                live["last_uploaded_at"] = datetime.now(timezone.utc).isoformat()
                if payload.get("indexed"):
                    stats["indexed"] += 1
                    log(f"  ok   {entry['slug']} ({payload.get('file_name', '?')})")
                else:
                    stats["skipped"] += 1
                    log(f"  skip {entry['slug']} (unchanged)")
                if (stats["indexed"] + stats["skipped"] + stats["failed"]) % 10 == 0:
                    write_manifest(manifest_path, entries)

    write_manifest(manifest_path, entries)
    log(f"Upload summary: {stats['indexed']} indexed, {stats['skipped']} skipped, {stats['failed']} failed")


def write_manifest(path: Path, entries: list[dict]) -> None:
    try:
        manifest = json.loads(path.read_text())
    except Exception:
        return
    manifest["pages"] = entries
    manifest["page_count"] = len(entries)
    manifest["total_bytes"] = sum(e["bytes"] for e in entries)
    path.write_text(json.dumps(manifest, indent=2))


def verify(rag_base: str) -> None:
    base = rag_base.rstrip("/")
    health = requests.get(base + "/api/health", timeout=30).json()
    log(f"RAG health: {json.dumps(health)}")
    docs = requests.get(base + "/api/v1/documents", timeout=60).json().get("documents", [])
    hig = [d for d in docs if str(d.get("file_name", "")).startswith("apple-hig__")]
    log(f"HIG documents: {len(hig)} | chunks: {sum(int(d.get('chunk_count', 0)) for d in hig)}")
    for query in [
        "Liquid Glass material and hierarchy",
        "tab bar navigation iOS",
        "macOS menu bar",
        "visionOS windows ornaments",
        "Dynamic Type accessibility",
    ]:
        response = requests.post(
            base + "/api/v1/search",
            json={"query": query, "domain": "hig", "framework": "APPLE_HIG", "limit": 3, "rerank": True},
            timeout=60,
        ).json()
        log(f"Query: {query}")
        for item in response.get("results", []):
            log(f"  {item['score']:.3f} {item['file_name']} > {item['header_path'][:70]}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync Apple HIG into the DarkCoders RAG.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="Corpus output directory")
    parser.add_argument("--rag-base", default=DEFAULT_RAG_BASE, help="RAG API base URL")
    parser.add_argument("--upload", action="store_true", help="Upload changed pages")
    parser.add_argument("--changed-only", action="store_true", default=False, help="Skip pages whose hash was already uploaded")
    parser.add_argument("--force", action="store_true", help="Upload every page regardless of hash")
    parser.add_argument("--verify", action="store_true", help="Verify RAG ledger and run test queries")
    parser.add_argument("--workers", type=int, default=4, help="Concurrent crawl/upload workers")
    parser.add_argument("--limit", type=int, default=0, help="Limit pages (smoke test)")
    args = parser.parse_args()

    out_dir = Path(args.out).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.verify and not args.upload:
        verify(args.rag_base)
        return 0

    log(f"Crawling {BASE + HIG_ROOT} ...")
    pages = crawl(max(1, args.workers))
    if args.limit:
        keep = [INDEX_PATH] + [p for p in sorted(pages) if p != INDEX_PATH][: args.limit - 1]
        pages = {p: pages[p] for p in keep if p in pages}
    log(f"Crawled {len(pages)} markdown pages, {sum(p['bytes'] for p in pages.values())} bytes")

    sections = build_sections(pages, max(1, args.workers))
    entries = build_corpus(pages, sections, out_dir)
    log(f"Wrote {len(entries)} raw + cleaned pages to {out_dir}")

    if args.upload:
        changed_only = args.changed_only and not args.force
        upload(entries, out_dir, args.rag_base, changed_only, max(1, min(args.workers, 4)))
        verify(args.rag_base)

    return 0


if __name__ == "__main__":
    sys.exit(main())
