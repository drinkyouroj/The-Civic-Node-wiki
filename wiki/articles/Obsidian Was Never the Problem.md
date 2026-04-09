---
title: "Obsidian Was Never the Problem"
type: article
article_type: nonfiction
tags: [technology, ai, knowledge-management]
published: 2026-04-06
created: 2026-04-07
updated: 2026-04-07
source: "published/Obsidian Was Never the Problem.md"
source_url: "https://drinkyouroj.substack.com/p/obsidian-was-never-the-problem"
---


[Read on Substack](https://drinkyouroj.substack.com/p/obsidian-was-never-the-problem)

## What It Is

A nonfiction essay arguing that PKM systems (Obsidian, Notion, Building a Second Brain) fail not because of bad design but because humans are structurally bad at being their own maintenance agents. [[Andrej Karpathy]]'s LLM wiki agent concept — CLAUDE.md schema + LLM as active maintenance agent — is presented as the architecture that finally solves the retrieval problem [[Vannevar Bush]] identified in 1945.

**Meta note**: This essay describes the exact system operating this wiki. The vault you are reading is built on the architecture described here.

## The Argument

1. **The failure is structural, not philosophical.** PKM systems don't die because the concept is broken. They die because every system positions the user as the maintenance agent, and humans cannot sustain maintenance indefinitely. Capture is easy. Retrieval requires something alive on the other end.

2. **Bush identified the problem in 1945.** The Memex was designed for retrieval through associative trails — with an active linking mechanism. We built the storage (computers, Obsidian) and skipped the agent. We told humans they were the machine.

3. **The Karpathy swap changes everything.** CLAUDE.md (schema) + index.md (structured knowledge) + log.md (session diary). The LLM reads the schema at session start, maintains the index, and logs what changed. The user provides raw material. The agent does the rest.

4. **The system proves itself when it knows what you forgot.** The inflection point isn't when you build it — it's when the agent surfaces context from two weeks ago and applies it correctly to a new question. That's the gap every passive PKM system fails to close.

## Structure

- **The Glitch** — introduces the abandoned Obsidian vault and the PKM industry's structural problem
- **The Source Code** — Bush's 1945 Memex; why every PKM collapses; the cognitive overhead that compounds daily
- **The Upgrade** — Karpathy's three-file implementation; how to set it up in Claude Code; the agent as partner
- **My Debug** — personal frame shop story (organizing as childhood practice; entropy as the default; the agent as the thing that changes the default)

## Cross-References

- [[LLM Wiki Agent]] — the central concept; operational foundation of this wiki
- [[PKM Failure Pattern]] — the problem the essay diagnoses
- [[Vannevar Bush]] — intellectual ancestor; 1945 Memex concept
- [[Andrej Karpathy]] — originator of the LLM wiki agent architecture

## Personal Code

The frame shop thread: Justin organized his father's frame shop as a kid, found deep satisfaction in working systems, and learned that systems fail not from bad design but from maintenance entropy. The Karpathy method solved the same problem the frame shop couldn't: it put an agent on the other end of the system.

## Newsletter Relevance

- **Technology**: Clear entry point for readers who've tried and abandoned note-taking systems — the audience is large and the frustration is universal
- **Practical**: Rare essay that ends with an actual implementation prompt the reader can copy
- **Meta-credibility**: The essay is written by someone actively running the system it describes — the wiki itself is evidence

## What It Leaves Open

- Does the LLM wiki architecture scale? (Large vaults, many sessions, context window limits)
- What does the failure mode look like when it eventually fails?
- What happens to the wiki if Claude's API access changes or the model degrades?
- Is Karpathy's original gist still the canonical reference, or has the community evolved the architecture?

## Sourcing

- Andrej Karpathy LLM wiki agent gist
- Vannevar Bush, "As We May Think," The Atlantic, July 1945
- Tiago Forte, *Building a Second Brain* (methodology reference)
