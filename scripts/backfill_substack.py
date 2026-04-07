#!/usr/bin/env python3
"""
backfill_substack.py
====================
Fetches all published posts from drinkyouroj.substack.com and writes them
into published/ as Markdown files with YAML frontmatter matching the vault's
existing clipping format.

Usage:
    python3 scripts/backfill_substack.py [--dry-run]

    --dry-run   Print what would be created/skipped without writing any files.

Dependencies:
    pip install requests html2text
"""

import argparse
import os
import re
import sys
from datetime import datetime, timezone
from typing import Optional

import html2text
import requests

# ── Configuration ─────────────────────────────────────────────────────────────

PUBLICATION    = "drinkyouroj"
BASE_URL       = f"https://{PUBLICATION}.substack.com"
API_URL        = f"{BASE_URL}/api/v1/posts"
AUTHOR_LINK    = "[[Justin Hearn]]"
PUBLISHED_DIR  = os.path.join(os.path.dirname(__file__), "..", "published")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
}

# ── User-defined classification ────────────────────────────────────────────────

# Substack tag slugs that map to vault tags (article series/format markers).
# All other Substack tags are ignored — vault tags are managed by the wiki
# ingest workflow, not by the raw clipping.
TEMPLATE_TAG_SLUGS: dict[str, str] = {
    "system-audit":     "system-audit",
    "the-system-audit": "system-audit",   # Substack sometimes creates both
    "pattern-reporter": "pattern-reporter",
    "triple-connection": "triple-connection",
    "concept-decoder":  "concept-decoder",
    "fiction":          "fiction",
}


def classify_post(post: dict) -> Optional[dict]:
    """
    Return a frontmatter extras dict to include this post, or None to skip.

    Rules:
    - Skip anything that isn't a newsletter (threads, etc.)
    - Skip paywalled posts (audience == "only_paid")
    - Podcasts are skipped for now; when audio transcription is added,
      add: or (post["type"] == "podcast" and has_transcript(post))
    - Map only template/format Substack tags → vault tags; ignore the rest
    - Detect Help Desk for the Singularity by slug prefix "hdfts-"
    """
    if post.get("audience") == "only_paid":
        return None

    if post.get("type") not in ("newsletter",):
        # TODO: add "podcast" here once transcription pipeline exists
        return None

    tags = ["clippings"]

    for tag in post.get("postTags", []):
        vault_tag = TEMPLATE_TAG_SLUGS.get(tag.get("slug", ""))
        if vault_tag and vault_tag not in tags:
            tags.append(vault_tag)

    if post.get("slug", "").startswith("hdfts-"):
        for t in ("fiction", "HDftS"):
            if t not in tags:
                tags.append(t)

    return {"tags": tags}


# ── Fetch ──────────────────────────────────────────────────────────────────────

def fetch_all_posts() -> list[dict]:
    """Paginate through the Substack API and return all posts."""
    posts = []
    limit = 50
    offset = 0

    while True:
        resp = requests.get(
            API_URL,
            params={"limit": limit, "offset": offset},
            headers=HEADERS,
            timeout=15,
        )
        resp.raise_for_status()
        batch = resp.json()

        # API returns a list directly
        if not isinstance(batch, list):
            batch = batch.get("posts", [])

        if not batch:
            break

        posts.extend(batch)
        print(f"  Fetched {len(posts)} posts so far...", end="\r")

        if len(batch) < limit:
            break  # last page
        offset += limit

    print()  # newline after \r
    return posts


# ── Convert ────────────────────────────────────────────────────────────────────

def html_to_markdown(html: str) -> str:
    """Convert Substack's body_html to clean Markdown."""
    converter = html2text.HTML2Text()
    converter.ignore_links = False       # preserve hyperlinks
    converter.ignore_images = False      # keep image alt-text
    converter.body_width = 0            # no line wrapping
    converter.protect_links = True      # don't mangle URLs
    converter.wrap_links = False
    return converter.handle(html).strip()


# ── Filename ───────────────────────────────────────────────────────────────────

def slug_to_filename(title: str) -> str:
    """
    Convert a post title to a safe filename.
    Strips characters that cause problems on macOS/Linux filesystems or
    with Obsidian's wikilink resolution.
    """
    # Remove characters that are illegal or cause Obsidian link issues
    safe = re.sub(r'[\\/*?:"<>|#^[\]]', "", title)
    # Collapse multiple spaces/dots
    safe = re.sub(r"\s+", " ", safe).strip()
    # Trim trailing dots (macOS issue)
    safe = safe.rstrip(".")
    return f"{safe}.md"


# ── Frontmatter ────────────────────────────────────────────────────────────────

def build_frontmatter(post: dict, extra: dict) -> str:
    """Render YAML frontmatter from post metadata + classify_post() output."""
    pub_date = post["post_date"][:10]          # "2026-04-06T..." → "2026-04-06"
    created   = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    source_url = f"{BASE_URL}/p/{post['slug']}"
    description = (post.get("subtitle") or post.get("search_engine_description") or "").strip()
    # Escape quotes in description for safe YAML inline string
    description = description.replace('"', '\\"')

    tags = extra.get("tags", ["clippings"])
    tag_lines = "\n".join(f'  - "{t}"' for t in tags)

    # Start with required fields
    lines = [
        "---",
        f'title: "{post["title"].replace(chr(34), chr(92)+chr(34))}"',
        f'source: "{source_url}"',
        "author:",
        f'  - "{AUTHOR_LINK}"',
        f"published: {pub_date}",
        f"created: {created}",
        f'description: "{description}"',
        f"tags:\n{tag_lines}",
    ]

    # Merge any extra frontmatter fields (article_type, series, etc.)
    skip_keys = {"tags"}  # already handled above
    for key, val in extra.items():
        if key in skip_keys:
            continue
        if isinstance(val, str):
            lines.append(f'{key}: "{val}"')
        else:
            lines.append(f"{key}: {val}")

    lines.append("---")
    return "\n".join(lines)


# ── Deduplication ──────────────────────────────────────────────────────────────

def existing_slugs(published_dir: str) -> set[str]:
    """
    Scan published/ for already-clipped posts.
    Matches on the URL slug embedded in each file's `source:` frontmatter line,
    so renames or reformatted filenames don't cause false duplicates.
    """
    slugs = set()
    slug_re = re.compile(r"source:\s*\"?https?://[^/]+/p/([^/\"]+)")

    if not os.path.isdir(published_dir):
        return slugs

    for fname in os.listdir(published_dir):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(published_dir, fname)
        try:
            with open(fpath, encoding="utf-8") as f:
                for line in f:
                    m = slug_re.search(line)
                    if m:
                        slugs.add(m.group(1))
                        break
        except OSError:
            pass

    return slugs


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Backfill Substack posts into published/")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args()

    published_dir = os.path.abspath(PUBLISHED_DIR)
    os.makedirs(published_dir, exist_ok=True)

    print(f"Fetching posts from {BASE_URL} ...")
    all_posts = fetch_all_posts()
    print(f"Found {len(all_posts)} posts total.\n")

    already_done = existing_slugs(published_dir)
    print(f"Already in published/: {len(already_done)} posts (matched by slug).\n")

    created_count = skipped_existing = skipped_classify = error_count = 0

    for post in all_posts:
        slug  = post.get("slug", "")
        title = post.get("title", "untitled")

        # Skip if already clipped
        if slug in already_done:
            skipped_existing += 1
            continue

        # Run user's classification
        extra = classify_post(post)
        if extra is None:
            skipped_classify += 1
            print(f"  SKIP  {title[:60]}")
            continue

        filename = slug_to_filename(title)
        filepath = os.path.join(published_dir, filename)

        if args.dry_run:
            tags = extra.get("tags", ["clippings"])
            print(f"  WOULD CREATE  {filename}  tags={tags}")
            created_count += 1
            continue

        # Build file content
        try:
            frontmatter = build_frontmatter(post, extra)
            body_html   = post.get("body_html") or ""
            body_md     = html_to_markdown(body_html) if body_html else ""
            content     = f"{frontmatter}\n\n{body_md}\n"

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

            tags = extra.get("tags", [])
            print(f"  CREATED  {filename}  ({len(body_md):,} chars)  tags={tags}")
            created_count += 1

        except Exception as exc:
            print(f"  ERROR   {title[:60]}: {exc}", file=sys.stderr)
            error_count += 1

    print(f"""
Results
───────
  Created:          {created_count}
  Skipped (exists): {skipped_existing}
  Skipped (filter): {skipped_classify}
  Errors:           {error_count}

{'(dry run — no files written)' if args.dry_run else f'Output: {published_dir}'}
""")


if __name__ == "__main__":
    main()
