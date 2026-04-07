---
title: "LLM Wiki Agent"
type: concept
tags: [technology, ai, knowledge-management]
created: 2026-04-07
updated: 2026-04-07
sources: 1
---

## Definition

An LLM wiki agent is a knowledge management architecture where a language model — not the user — acts as the active maintenance agent for a structured personal knowledge base. Originated by [[Andrej Karpathy]] in a published gist. The core swap: instead of the human tagging, linking, organizing, and retrieving, the LLM does. The human's role shifts to providing raw material and asking questions.

The minimal implementation requires three files:
- **CLAUDE.md** — schema file; defines categories, formatting rules, and standing operating instructions for the agent
- **index.md** — structured knowledge index; maintained and updated by the LLM at the close of every session
- **log.md** — append-only session diary; records what was discussed, what changed, what the system now knows

## Why It Matters for the Newsletter

**Technology & AI**: This is the first practical implementation of [[Vannevar Bush]]'s 1945 Memex concept — an agent maintaining associative trails through a knowledge base on behalf of the user. The concept went from theoretical (1945) → technically possible but human-bottlenecked (1990–2022) → solved by LLMs (2023+).

**Meta**: This wiki operates on exactly this architecture. Every ingest, query, and lint session is an instance of the LLM wiki agent pattern in production.

## Evidence & Examples

- [[Obsidian Was Never the Problem]] — explains the architecture and contrasts it with passive PKM systems (Obsidian, Notion, Building a Second Brain)
- This vault (Substack Research) — production implementation; CLAUDE.md defines schema, index.md catalogs pages, log.md records sessions

## Tensions & Counterarguments

- Requires a capable LLM — the architecture is only as good as the model's ability to maintain consistency across sessions
- Long-term drift: LLMs may introduce inconsistencies in entity names, link targets, or concept definitions without a human periodically auditing
- Context window limits: a very large wiki may exceed what the LLM can hold in one session; the index + log structure mitigates this but doesn't eliminate it
- Dependency risk: the knowledge base is maintained by a proprietary model; if the model degrades or access is lost, the wiki still exists as static files but loses its active maintenance layer

## Related Concepts

- [[PKM Failure Pattern]] — the problem this architecture solves
- [[Tech-State Conflict]] — LLM infrastructure is centralized and proprietary; relevant to who controls the tools

## Key Sources

- [[Obsidian Was Never the Problem]]
