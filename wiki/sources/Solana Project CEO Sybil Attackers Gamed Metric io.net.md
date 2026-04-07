---
title: "Solana Project CEO Sybil Attackers Gamed Metric io.net"
type: source
tags: [crypto, technology, depin]
created: 2026-04-07
updated: 2026-04-07
sources: 1
raw: "raw/Solana project CEO says 'sybil attackers' gamed metric hoping for airdrop.md"
author: "Mark Toon / Protos"
published: 2024-04-29
---

## Summary

Report on io.net CEO Ahmad Shadid's post-mortem after critics (including Martin Shkreli) challenged the DePIN project's claimed GPU node count. Io.net had claimed 500,000+ nodes; post-mortem found only 12,000 "clusterable, verifiably active and real GPUs" after removing sybil attackers gaming the airdrop incentive.

## Key Points

- Io.net initial claimed: 500,000+ nodes on the network.
- Post-mortem: only 120,000 verified nodes initially; that number also gamed; final count ~12,000 real GPUs.
- Sybil attack: bad actors used virtualized GPUs and exploited a user ID leak to display fake nodes on the explorer.
- Motivation: gaming airdrop eligibility by making it appear they were contributing to the network.
- Io.net raised $30M at a $1B valuation before the incident.
- CEO quote: "We move fast, and sometimes we break things."
- Martin Shkreli (disgraced pharma executive-turned-crypto figure) was vocal in pointing out the metric manipulation.
- Tim Copeland (The Block editor) flagged manipulation of news on X related to the project.

## Newsletter Angles

- The 500K-to-12K collapse: io.net's headline stat — the "half a million GPUs" claim that justified its $1B valuation — turned out to be off by 97%. This is the DePIN Potemkin Village problem in its most extreme form.
- Sybil attacks as an inherent DePIN vulnerability: the airdrop incentive creates rational behavior to fake participation. Unless there's hardware attestation (TEEs), any DePIN can be gamed this way.
- The $1B valuation on false data: io.net raised money at a billion-dollar valuation while having 12,000 real GPUs. The venture capital due diligence question here is significant.

## Entities Mentioned

- [[Helium Network]] — comparison: Helium had a similar Proof-of-Coverage gaming problem; io.net's sybil attack is the compute equivalent

## Concepts Mentioned

- [[DePIN]] — sybil attacks are a core DePIN security problem; hardware attestation is the proposed solution
- [[Tokenomics]] — airdrop mechanics created the incentive to fake participation

## Notes

Source is Protos (credible crypto journalism). Martin Shkreli's involvement is noted — his critique was correct on the metrics, but his motives may have been adversarial (potential competitor or short position). The io.net situation directly informed discussions about hardware attestation in DePIN design.
