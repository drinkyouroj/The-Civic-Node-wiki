#!/usr/bin/env python3
"""
add_source_urls.py

For each wiki/sources/*.md file:
  1. Reads the `raw:` frontmatter field to find the corresponding raw/ file.
  2. Extracts the `source:` URL from that raw file's frontmatter.
  3. Inserts `source_url: "URL"` into the wiki/sources/ frontmatter (after `raw:`).
  4. Prepends `[Original source](URL)\n\n` before the first `## Summary` heading.

Run from the project root:
    python3 scripts/add_source_urls.py
"""

import os
import re
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_SOURCES = os.path.join(PROJECT_ROOT, "wiki", "sources")
RAW_DIR = os.path.join(PROJECT_ROOT, "raw")

# Normalize typographic (curly) quotes to straight quotes for filename matching.
# macOS apps often write curly quotes in filenames while YAML frontmatter stores straight ones.
def _normalize_quotes(s):
    return (s
        .replace("\u2018", "'").replace("\u2019", "'")   # curly single quotes → '
        .replace("\u201c", '"').replace("\u201d", '"'))  # curly double quotes → "

# Build a lookup: normalized-filename → actual-filename for raw/
_raw_index = {
    _normalize_quotes(f): f
    for f in os.listdir(RAW_DIR)
    if f.endswith(".md")
}


def split_frontmatter(content):
    """Split a markdown file into (frontmatter_text, body).
    Returns (None, content) if no frontmatter found."""
    if not content.startswith("---"):
        return None, content
    end = content.find("\n---", 3)
    if end == -1:
        return None, content
    frontmatter = content[4:end]  # skip opening '---\n'
    body = content[end + 4:]      # skip closing '\n---'
    if body.startswith("\n"):
        body = body[1:]
    return frontmatter, body


def get_yaml_value(frontmatter, key):
    """Extract a scalar value from raw YAML text for a given key.
    Handles both quoted and unquoted values, and YAML-escaped inner quotes."""
    pattern = rf'^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$'
    match = re.search(pattern, frontmatter, re.MULTILINE)
    if match:
        value = match.group(1).strip().strip("\"'")
        # Unescape YAML-escaped inner double quotes (\" → ")
        value = value.replace('\\"', '"')
        return value if value else None
    return None


def main():
    files = sorted(
        f for f in os.listdir(WIKI_SOURCES) if f.endswith(".md")
    )
    total = len(files)
    updated = 0
    skipped_already_done = 0
    skipped_no_raw = 0
    skipped_no_url = 0
    errors = []

    for filename in files:
        filepath = os.path.join(WIKI_SOURCES, filename)

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Skip if already processed
        if "source_url:" in content:
            skipped_already_done += 1
            continue

        frontmatter, body = split_frontmatter(content)
        if frontmatter is None:
            errors.append(f"No frontmatter: {filename}")
            continue

        # Get the raw file path (may be quoted or unquoted)
        raw_value = get_yaml_value(frontmatter, "raw")
        if not raw_value:
            skipped_no_raw += 1
            print(f"  [WARN] No raw: field in {filename}")
            continue

        raw_basename = os.path.basename(raw_value)
        # Try exact match first, then normalize curly quotes for macOS compat
        actual_name = _raw_index.get(raw_basename) or _raw_index.get(_normalize_quotes(raw_basename))
        if not actual_name:
            skipped_no_raw += 1
            print(f"  [WARN] Raw file not found: {raw_value}")
            continue
        raw_filepath = os.path.join(RAW_DIR, actual_name)

        with open(raw_filepath, "r", encoding="utf-8") as f:
            raw_content = f.read()

        raw_frontmatter, _ = split_frontmatter(raw_content)
        if raw_frontmatter is None:
            errors.append(f"No frontmatter in raw file: {raw_value}")
            continue

        source_url = get_yaml_value(raw_frontmatter, "source")
        if not source_url:
            skipped_no_url += 1
            print(f"  [WARN] No source URL in raw file: {raw_value}")
            continue

        # 1. Insert source_url into frontmatter after the raw: line
        new_frontmatter = re.sub(
            r'(raw:\s*.*)',
            rf'\1\nsource_url: "{source_url}"',
            frontmatter,
            count=1,
        )

        # 2. Add visible link before ## Summary
        link_line = f"[Original source]({source_url})\n\n"
        if "## Summary" in body:
            new_body = body.replace("## Summary", link_line + "## Summary", 1)
        else:
            # No Summary section — prepend to body
            new_body = link_line + body

        # Reconstruct the file
        new_content = f"---\n{new_frontmatter}\n---\n\n{new_body}"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        updated += 1

    print(f"\nDone.")
    print(f"  Updated:              {updated}")
    print(f"  Already had URL:      {skipped_already_done}")
    print(f"  Missing raw file:     {skipped_no_raw}")
    print(f"  Missing source URL:   {skipped_no_url}")
    print(f"  Errors:               {len(errors)}")
    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  - {e}")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
