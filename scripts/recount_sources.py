#!/usr/bin/env python3
"""
recount_sources.py — Update `sources:` in wiki page YAML frontmatter.

Counts every unique `- [[Wikilink]]` bullet anywhere in the page body
and writes the count back to the `sources:` field if it has drifted.

Usage:
    python3 scripts/recount_sources.py                  # scan all wiki/
    python3 scripts/recount_sources.py wiki/entities/X  # specific files
"""

import os
import re
import sys


FRONTMATTER_RE = re.compile(r'^---\n(.*?)\n---\n(.*)', re.DOTALL)
BULLET_LINK_RE = re.compile(r'^[-*]\s*\[\[([^\]|]+)', re.MULTILINE)
SOURCES_LINE_RE = re.compile(r'^sources:\s*\d+', re.MULTILINE)


def recount_file(path: str) -> bool:
    """Recount sources for one file. Returns True if the file was changed."""
    with open(path) as f:
        txt = f.read()

    m = FRONTMATTER_RE.match(txt)
    if not m:
        return False

    fm, body = m.group(1), m.group(2)

    if not SOURCES_LINE_RE.search(fm):
        return False  # no sources field — not a managed wiki page

    bullets = BULLET_LINK_RE.findall(body)
    actual = len(set(bullets))

    new_fm = SOURCES_LINE_RE.sub(f'sources: {actual}', fm)
    if new_fm == fm:
        return False  # no change

    with open(path, 'w') as f:
        f.write('---\n' + new_fm + '\n---\n' + body)
    return True


def collect_paths(args: list[str]) -> list[str]:
    if args:
        return [p for p in args if p.endswith('.md') and os.path.isfile(p)]
    # default: all wiki/ markdown files
    paths = []
    for root, _, files in os.walk('wiki'):
        for f in files:
            if f.endswith('.md'):
                paths.append(os.path.join(root, f))
    return paths


if __name__ == '__main__':
    paths = collect_paths(sys.argv[1:])
    changed = [p for p in paths if recount_file(p)]
    if changed:
        print(f'recount_sources: updated {len(changed)} file(s)')
        for p in changed:
            print(f'  {p}')
    else:
        print('recount_sources: all counts current')
