---
title: "io.net"
type: entity
entity_type: organization
tags: [technology, crypto, depin]
created: 2026-04-07
updated: 2026-04-07
sources: 2
---

## Overview

io.net is a Solana-based decentralized GPU compute network (a [[DePIN]] protocol) that allows GPU owners to contribute compute capacity and earn the $IO token. Founded by Ahmad Shadid, it raised $30 million at a $1 billion valuation in early 2024. It attracted scrutiny when critics pointed out its claimed 500,000+ GPU node count was fabricated; a post-mortem found only ~12,000 real GPUs. A subsequent cyber attack used nearly 2 million fake GPU signals to earn fraudulent rewards, delaying the $IO token launch.

## Key Facts

- Raised $30M at $1B valuation (early 2024).
- Originally claimed 500,000+ GPU nodes; post-mortem settled on ~12,000 verifiable real GPUs.
- Sybil attackers gamed the network by using virtualized GPUs and exploiting a user ID leak.
- Motivation for sybil attacks: gaming anticipated $IO token airdrop eligibility.
- CEO Ahmad Shadid post-mortem quote: "We move fast, and sometimes we break things."
- Second attack (May 2024): ~2 million fake GPUs injected to earn incentive rewards; $IO token launch delayed ~2 weeks.
- Martin Shkreli was among the first to publicly challenge io.net's GPU count claims.
- Proposed solution: Trusted Execution Environments (TEEs) — hardware with physically embedded private keys that cannot be faked.

## Newsletter Relevance

io.net is the clearest case study of [[DePIN]] 's core vulnerability: token incentives for contributing resources create rational incentives to fake those resources. The $1B valuation on fraudulent metrics is a cautionary tale for the entire DePIN sector. The TEE solution (hardware attestation) is the most technically rigorous proposed fix, but it requires infrastructure partners (NVIDIA, chip manufacturers) to cooperate — centralizing trust back into hardware manufacturers.

## Connections

- [[DePIN]] — io.net is a GPU compute DePIN
- [[Helium Network]] — comparison: Helium had Proof-of-Coverage gaming; io.net had GPU sybil attacks
- [[Tokenomics]] — airdrop incentive design created the motivation to cheat

## Source Appearances

- [[Solana Project CEO Sybil Attackers Gamed Metric io.net]] — CEO post-mortem on fake GPU count
- [[Preventable Cyber Attack Impacts io.net DePIN]] — May 2024 attack details; TEE solution proposed

## Open Questions

- Did the $IO token ultimately launch after the delay? What is its current price/market cap?
- Has io.net implemented TEE-based verification?
- Is the $1B valuation still being maintained despite the revelations about real GPU count?
