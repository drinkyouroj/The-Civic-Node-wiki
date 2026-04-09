#!/usr/bin/env python3
"""
add_article_urls.py

For each wiki/articles/**/*.md file:
  1. Reads the `source:` frontmatter field to find the corresponding published/ file.
  2. Extracts the `source:` URL (Substack URL) from that published file's frontmatter.
  3. Inserts `source_url: "URL"` into the wiki/articles/ frontmatter (after `source:`).
  4. Prepends `[Read on Substack](URL)\n\n` before the first `## ` heading.

Run from the project root:
    python3 scripts/add_article_urls.py
"""

import os
import re
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_ARTICLES = os.path.join(PROJECT_ROOT, "wiki", "articles")
PUBLISHED_DIR = os.path.join(PROJECT_ROOT, "published")


def _normalize_quotes(s):
    """Normalize macOS typographic (curly) quotes to straight for filename matching."""
    return (s
        .replace("\u2018", "'").replace("\u2019", "'")
        .replace("\u201c", '"').replace("\u201d", '"'))


def _build_index(directory):
    """Return {normalized-filename: actual-filename} for .md files in directory."""
    return {
        _normalize_quotes(f): f
        for f in os.listdir(directory)
        if f.endswith(".md")
    }


def split_frontmatter(content):
    """Split into (frontmatter_text, body). Returns (None, content) if none found."""
    if not content.startswith("---"):
        return None, content
    end = content.find("\n---", 3)
    if end == -1:
        return None, content
    frontmatter = content[4:end]
    body = content[end + 4:]
    if body.startswith("\n"):
        body = body[1:]
    return frontmatter, body


def get_yaml_value(frontmatter, key):
    """Extract a scalar value from raw YAML text. Handles quoted/unquoted values."""
    pattern = rf'^{re.escape(key)}:\s*["\']?(.*?)["\']?\s*$'
    match = re.search(pattern, frontmatter, re.MULTILINE)
    if match:
        value = match.group(1).strip().strip("\"'")
        value = value.replace('\\"', '"')
        return value if value else None
    return None


def collect_article_files(base_dir):
    """Yield all .md files from wiki/articles/ and wiki/articles/episodes/."""
    for entry in os.scandir(base_dir):
        if entry.is_file() and entry.name.endswith(".md"):
            yield entry.path
        elif entry.is_dir():
            for sub in os.scandir(entry.path):
                if sub.is_file() and sub.name.endswith(".md"):
                    yield sub.path


def main():
    published_index = _build_index(PUBLISHED_DIR)

    files = sorted(collect_article_files(WIKI_ARTICLES))
    total = len(files)
    updated = 0
    skipped_already_done = 0
    skipped_no_published = 0
    skipped_no_url = 0
    errors = []

    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if "source_url:" in content:
            skipped_already_done += 1
            continue

        frontmatter, body = split_frontmatter(content)
        if frontmatter is None:
            errors.append(f"No frontmatter: {os.path.basename(filepath)}")
            continue

        source_value = get_yaml_value(frontmatter, "source")
        if not source_value:
            errors.append(f"No source: field in {os.path.basename(filepath)}")
            continue

        # source_value is like "published/filename.md"
        pub_basename = os.path.basename(source_value)
        actual_name = (published_index.get(pub_basename)
                       or published_index.get(_normalize_quotes(pub_basename)))
        if not actual_name:
            skipped_no_published += 1
            print(f"  [WARN] Published file not found: {source_value}")
            continue

        pub_filepath = os.path.join(PUBLISHED_DIR, actual_name)
        with open(pub_filepath, "r", encoding="utf-8") as f:
            pub_content = f.read()

        pub_frontmatter, _ = split_frontmatter(pub_content)
        if pub_frontmatter is None:
            errors.append(f"No frontmatter in published file: {actual_name}")
            continue

        substack_url = get_yaml_value(pub_frontmatter, "source")
        if not substack_url:
            skipped_no_url += 1
            print(f"  [WARN] No source URL in published file: {actual_name}")
            continue

        # 1. Insert source_url into frontmatter after the source: line
        new_frontmatter = re.sub(
            r'(source:\s*"published/[^"]*")',
            rf'\1\nsource_url: "{substack_url}"',
            frontmatter,
            count=1,
        )

        # 2. Add visible link before the first ## heading
        link_line = f"[Read on Substack]({substack_url})\n\n"
        first_heading = re.search(r'^## ', body, re.MULTILINE)
        if first_heading:
            pos = first_heading.start()
            new_body = body[:pos] + link_line + body[pos:]
        else:
            new_body = link_line + body

        new_content = f"---\n{new_frontmatter}\n---\n\n{new_body}"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

        updated += 1

    print(f"\nDone. ({total} files scanned)")
    print(f"  Updated:                {updated}")
    print(f"  Already had URL:        {skipped_already_done}")
    print(f"  Missing published file: {skipped_no_published}")
    print(f"  Missing source URL:     {skipped_no_url}")
    print(f"  Errors:                 {len(errors)}")
    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  - {e}")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
