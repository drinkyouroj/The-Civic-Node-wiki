#!/usr/bin/env python3
"""
scrape_sources.py
=================
Extracts all footnote citations from published/ articles, fetches each unique
URL, and writes the content to raw/ as Markdown clippings ready for wiki ingest.

Usage:
    python3 scripts/scrape_sources.py [--dry-run] [--limit N] [--delay SECS]

    --dry-run     Show what would be fetched without writing files
    --limit N     Process only N URLs (for testing)
    --delay SECS  Seconds between requests (default: 1.0)

Dependencies:
    pip install requests trafilatura lxml_html_clean pdfminer.six
"""

import argparse
import logging
import os
import re
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeout
from datetime import datetime, timezone
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse

import requests
import trafilatura

try:
    from pdfminer.high_level import extract_text as pdf_extract_text
    HAS_PDFMINER = True
except ImportError:
    HAS_PDFMINER = False

# ── Configuration ──────────────────────────────────────────────────────────────

PUBLISHED_DIR = os.path.join(os.path.dirname(__file__), "..", "published")
RAW_DIR       = os.path.join(os.path.dirname(__file__), "..", "raw")
LOG_FILE      = os.path.join(os.path.dirname(__file__), "scrape_sources.log")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

# Domains whose content is not useful to scrape
SKIP_DOMAINS: Set[str] = {
    # Social / video
    "x.com", "twitter.com", "facebook.com", "fb.com",
    "instagram.com", "linkedin.com", "youtube.com", "t.co",
    "truthsocial.com", "streamable.com", "tiktok.com",
    # Image / asset CDNs
    "substackcdn.com", "images.unsplash.com",
    # Substack (self-links already in published/)
    "substack.com",
}


# ── Citation extraction ────────────────────────────────────────────────────────

# Matches both citation formats:
#   Format 1 (API-backfilled): [Title](<URL>) or [Title](URL)
#   Format 2 (manually clipped): [^N]: *[Title](URL)*
CITATION_PAT = re.compile(r'\[([^\]]+)\]\(<?(https?://[^>)\s]+)>?\)')


def extract_citations(content: str) -> List[Tuple[str, str]]:
    """Return list of (link_text, url) for every markdown link in content."""
    return CITATION_PAT.findall(content)


# ── URL classification ─────────────────────────────────────────────────────────

def skip_reason(url: str) -> Optional[str]:
    """Return a reason string if URL should be skipped, else None."""
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    # Strip www. and any port
    bare = re.sub(r"^www\.", "", domain).split(":")[0]

    if bare in SKIP_DOMAINS or any(s in bare for s in ("substack.com",)):
        return f"skip-domain ({bare})"
    if not parsed.path.strip("/"):
        return "bare home page"
    return None


def is_pdf_url(url: str) -> bool:
    return urlparse(url).path.lower().endswith(".pdf")


# ── Deduplication ──────────────────────────────────────────────────────────────

def existing_raw_urls(raw_dir: str) -> Set[str]:
    """
    Scan raw/ for source: URLs already present, so re-runs skip them.
    Matches on the exact URL in each file's frontmatter.
    """
    urls: Set[str] = set()
    pat = re.compile(r'source:\s*["\']?(https?://[^\s"\']+)')
    if not os.path.isdir(raw_dir):
        return urls
    for fname in os.listdir(raw_dir):
        if not fname.endswith(".md"):
            continue
        try:
            with open(os.path.join(raw_dir, fname), encoding="utf-8") as f:
                for line in f:
                    m = pat.search(line)
                    if m:
                        urls.add(m.group(1).rstrip("\"'"))
                        break
        except OSError:
            pass
    return urls


# ── Filename ───────────────────────────────────────────────────────────────────

def title_to_filename(title: str, url: str) -> str:
    """Sanitize title into a safe filename, falling back to domain+path."""
    if not title or len(title.strip()) < 4:
        parsed = urlparse(url)
        title = (parsed.netloc + parsed.path).replace("/", " ").strip()
    safe = re.sub(r'[\\/*?:"<>|#^[\]]', "", title)
    safe = re.sub(r"\s+", " ", safe).strip().rstrip(".")
    if len(safe) > 120:
        safe = safe[:120].rstrip()
    return f"{safe}.md"


def unique_filepath(raw_dir: str, filename: str, url: str) -> str:
    """If filename already exists, append the domain to disambiguate."""
    path = os.path.join(raw_dir, filename)
    if not os.path.exists(path):
        return path
    domain = urlparse(url).netloc.replace("www.", "")
    base = filename[:-3]
    return os.path.join(raw_dir, f"{base} [{domain}].md")


# ── Frontmatter ───────────────────────────────────────────────────────────────

def build_frontmatter(title: str, url: str, link_text: str,
                      author: str = "", published: str = "") -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    domain = urlparse(url).netloc.replace("www.", "")

    def esc(s: str) -> str:
        return s.replace('"', '\\"')

    lines = [
        "---",
        f'title: "{esc(title)}"',
        f'source: "{url}"',
        f'link_text: "{esc(link_text[:200])}"',
        f'domain: "{domain}"',
    ]
    if author:
        lines.append(f'author: "{esc(author)}"')
    if published:
        lines.append(f'published: "{published}"')
    lines += [
        f'fetched: {today}',
        'tags: ["clippings"]',
        "---",
    ]
    return "\n".join(lines)


# ── Fetch & extract ────────────────────────────────────────────────────────────

def _do_get(url: str, timeout: int) -> requests.Response:
    """Inner GET — runs in a thread so we can enforce a hard wall-clock limit."""
    return requests.get(url, headers=HEADERS, timeout=timeout,
                        allow_redirects=True)


def fetch_html(url: str, timeout: int = 15) -> Tuple[int, Optional[str]]:
    """
    Return (status_code, html) or (0, None) on error.

    Uses a ThreadPoolExecutor to impose a hard wall-clock deadline of
    timeout+5 seconds, preventing servers that trickle data from hanging
    the process indefinitely (requests' built-in timeout is per-read-chunk,
    not total).
    """
    wall_limit = timeout + 5
    try:
        with ThreadPoolExecutor(max_workers=1) as ex:
            future = ex.submit(_do_get, url, timeout)
            resp = future.result(timeout=wall_limit)
        return resp.status_code, resp.text if resp.ok else None
    except FuturesTimeout:
        return 0, None
    except requests.RequestException:
        return 0, None


def extract_article(html: str, url: str) -> Tuple[str, str, str, str]:
    """
    Return (title, body_markdown, author, published_date) using trafilatura.
    Falls back gracefully if metadata is unavailable.
    """
    meta = trafilatura.extract_metadata(html, default_url=url)
    title = (meta.title or "").strip() if meta else ""
    author = (meta.author or "").strip() if meta else ""
    published = (meta.date or "").strip() if meta else ""

    body = trafilatura.extract(
        html,
        url=url,
        include_comments=False,
        include_tables=True,
        output_format="markdown",
        favor_precision=True,
        with_metadata=False,
    ) or ""

    return title, body.strip(), author, published


def fetch_pdf(url: str, timeout: int = 20) -> Tuple[int, Optional[str]]:
    """Fetch a PDF and extract its text content."""
    if not HAS_PDFMINER:
        return 0, None
    try:
        wall_limit = timeout + 5
        with ThreadPoolExecutor(max_workers=1) as ex:
            future = ex.submit(_do_get, url, timeout)
            resp = future.result(timeout=wall_limit)
        if not resp.ok:
            return resp.status_code, None
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            f.write(resp.content)
            tmp_path = f.name
        try:
            text = pdf_extract_text(tmp_path)
            return resp.status_code, text.strip() if text else None
        except Exception:
            return resp.status_code, None
        finally:
            os.unlink(tmp_path)
    except (FuturesTimeout, requests.RequestException):
        return 0, None


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Scrape article sources from published/ into raw/"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without writing files")
    parser.add_argument("--limit", type=int, default=0,
                        help="Process only N URLs (0 = all)")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="Seconds between requests (default: 1.0)")
    args = parser.parse_args()

    published_dir = os.path.abspath(PUBLISHED_DIR)
    raw_dir = os.path.abspath(RAW_DIR)
    os.makedirs(raw_dir, exist_ok=True)

    # Configure logging to file + stderr for errors
    logging.basicConfig(
        filename=os.path.abspath(LOG_FILE),
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    log = logging.getLogger()

    # ── Step 1: Extract all citations ─────────────────────────────────────────
    print("Scanning published/ for citations...")
    seen: Dict[str, str] = {}  # url → first link_text encountered
    for fname in sorted(os.listdir(published_dir)):
        if not fname.endswith(".md"):
            continue
        try:
            content = open(os.path.join(published_dir, fname),
                           encoding="utf-8").read()
        except OSError:
            continue
        for link_text, url in extract_citations(content):
            if url not in seen:
                seen[url] = link_text

    print(f"  {len(seen)} unique URLs found across all published articles")

    # ── Step 2: Filter ────────────────────────────────────────────────────────
    already_fetched = existing_raw_urls(raw_dir)
    skip_counts: Dict[str, int] = {}
    queue: List[Tuple[str, str]] = []  # (url, link_text)

    for url, link_text in seen.items():
        reason = skip_reason(url)
        if reason:
            skip_counts[reason] = skip_counts.get(reason, 0) + 1
            log.info(f"SKIP [{reason}] {url}")
            continue
        if url in already_fetched:
            skip_counts["already in raw/"] = skip_counts.get("already in raw/", 0) + 1
            continue
        queue.append((url, link_text))

    pdf_count = sum(1 for url, _ in queue if is_pdf_url(url))
    print(f"  Skipping {sum(skip_counts.values())} URLs:")
    for reason, count in sorted(skip_counts.items(), key=lambda x: -x[1]):
        print(f"    {count:4d}  {reason}")
    print(f"  Queue: {len(queue)} URLs ({pdf_count} PDFs, "
          f"{len(queue) - pdf_count} HTML)")

    if args.limit:
        queue = queue[: args.limit]
        print(f"  (limited to first {args.limit})")

    print()

    if args.dry_run:
        print("Dry run — would fetch:")
        for url, link_text in queue[:40]:
            tag = "[PDF]" if is_pdf_url(url) else "     "
            print(f"  {tag} {link_text[:55]:<55}  {url[:70]}")
        if len(queue) > 40:
            print(f"  ... and {len(queue) - 40} more")
        return

    # ── Step 3: Fetch ─────────────────────────────────────────────────────────
    counts = {"created": 0, "failed": 0, "empty": 0}

    for i, (url, link_text) in enumerate(queue, 1):
        label = link_text[:52]
        print(f"  [{i:3d}/{len(queue)}] {label:<52}", end=" ", flush=True)

        if is_pdf_url(url):
            status, text = fetch_pdf(url)
            title = link_text
            body = text or ""
            author = published = ""
        else:
            status, html = fetch_html(url)
            if html:
                title, body, author, published = extract_article(html, url)
                if not title:
                    title = link_text
            else:
                title = link_text
                body = author = published = ""

        if status == 0:
            print("ERR (connection)")
            log.warning(f"FAIL [connection] {url}")
            counts["failed"] += 1
        elif status != 200:
            print(f"ERR (HTTP {status})")
            log.warning(f"FAIL [HTTP {status}] {url}")
            counts["failed"] += 1
        elif not body.strip():
            print("EMPTY")
            log.warning(f"EMPTY {url}")
            counts["empty"] += 1
        else:
            filename = title_to_filename(title, url)
            filepath = unique_filepath(raw_dir, filename, url)
            frontmatter = build_frontmatter(title, url, link_text,
                                            author, published)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"{frontmatter}\n\n{body}\n")
            short_name = os.path.basename(filepath)[:45]
            print(f"OK  {len(body):>7,}c → {short_name}")
            log.info(f"OK {url} → {os.path.basename(filepath)}")
            counts["created"] += 1

        if i < len(queue):
            time.sleep(args.delay)

    print(f"""
Results
───────
  Created:  {counts['created']}
  Failed:   {counts['failed']}
  Empty:    {counts['empty']}

Log: {os.path.abspath(LOG_FILE)}
Output: {raw_dir}
{'(dry run — no files written)' if args.dry_run else ''}
""")


if __name__ == "__main__":
    main()
