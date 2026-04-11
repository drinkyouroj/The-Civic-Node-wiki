# The Civic Node — Research Wiki

The research vault and knowledge base behind [The Civic Node](https://wiki.hearn.me) newsletter. Built with [Quartz](https://quartz.jzhao.xyz/) and maintained as a structured Obsidian vault.

**Live site**: [wiki.hearn.me](https://wiki.hearn.me)

---

## What This Is

An accumulating knowledge base that tracks sources, entities, concepts, and editorial syntheses across the newsletter's coverage areas: politics, power, monetary policy, technology, and infrastructure. The wiki grows with every source ingested — themes emerge from the material rather than being imposed in advance.

Current scale: **806 pages**, **423 source documents**, **81 published pieces**.

---

## Repository Structure

```
/
├── raw/                   ← Source documents (immutable — never edited)
│   └── *.md               ← Clipped articles, papers, transcripts
├── wiki/
│   ├── index.md           ← Master catalog of all wiki pages
│   ├── log.md             ← Append-only chronological event log
│   ├── overview.md        ← High-level synthesis of the full wiki
│   ├── sources/           ← One summary page per source document
│   ├── entities/          ← People, orgs, countries, protocols, assets
│   ├── concepts/          ← Ideas, themes, patterns, dynamics
│   ├── syntheses/         ← Analyses, editorial sweeps, query outputs
│   └── articles/          ← Summaries of published newsletter pieces
├── published/             ← Published Substack pieces (immutable)
├── quartz/                ← Quartz static site generator
├── scripts/               ← Utility scripts
├── CLAUDE.md              ← LLM agent schema and workflow rules
├── quartz.config.ts       ← Site configuration
└── quartz.layout.ts       ← Site layout
```

---

## How the Wiki is Maintained

The wiki is managed with an LLM agent following the schema defined in [`CLAUDE.md`](./CLAUDE.md). Four core workflows:

| Workflow | Trigger | What it does |
|---|---|---|
| **INGEST** | New file in `raw/` | Creates source summary, updates entity/concept pages, updates index |
| **QUERY** | User question | Synthesizes an answer from wiki, optionally files it to `wiki/syntheses/` |
| **LINT** | Health check | Reports contradictions, orphans, stubs, gaps, stale claims |
| **INSIGHT_SWEEP** | Editorial sweep | Three-agent pass: patterns, contradictions, underexplored angles → top 5 hooks |

Every operation appends to `wiki/log.md`. Every new page is registered in `wiki/index.md`.

---

## Local Development

This site is built with [Quartz v4](https://quartz.jzhao.xyz/).

```bash
npm install
npx quartz build --serve    # build and serve locally
```

The Obsidian vault (`.obsidian/`) is checked in — open the repo root as a vault in Obsidian to browse and edit with full graph view and wikilink resolution.

---

## Coverage Areas

Themes observed across accumulated sources (updated as the wiki grows):

- **Politics** — Who holds power? How is it being exercised, contested, or lost?
- **Monetary Policy / Finance** — Central banks, sanctions, currency dynamics, stablecoins
- **Power & Infrastructure** — Who controls critical systems? What happens when that control is weaponized?
- **Technology & State** — Governments and tech companies colliding over AI, data, and infrastructure
- **Crypto / DePIN** — Decentralized physical infrastructure networks, token economics, regulatory capture

---

## Key Pages

- [`wiki/overview.md`](./wiki/overview.md) — start here for the full picture
- [`wiki/index.md`](./wiki/index.md) — complete page catalog
- [`wiki/log.md`](./wiki/log.md) — recent activity
