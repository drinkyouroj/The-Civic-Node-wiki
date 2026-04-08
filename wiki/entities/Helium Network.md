---
title: "Helium Network"
type: entity
entity_type: infrastructure
tags: [technology, infrastructure, crypto, depin]
created: 2026-04-07
updated: 2026-04-07
sources: 7
---

## Overview

Helium is a decentralized wireless network — a [[DePIN]] protocol — that crowdsources the deployment of IoT (LoRaWAN) and 5G wireless coverage. Individuals buy and operate Helium hotspots, earning HNT tokens for providing network coverage. By 2024, Helium had deployed over 1 million hotspots globally, making it one of the largest DePIN networks by physical footprint. Helium's Proof of Coverage (PoC) mechanism — the system for verifying hotspots actually provide real coverage — was the subject of significant fraud (PoC hacking), exposing a core vulnerability in DePIN verification.

## Key Facts

- Protocol: LoRaWAN IoT network + 5G mobile coverage.
- Native token: HNT (Helium Network Token).
- Total supply: 223 million HNT; circulating ~184 million (82.67% unlocked as of 2026). [[Helium HNT Tokenomics — Tokenomist]]
- Allocation: Data Transfer (36%), Founders/Investors (32.6%), Proof of Coverage (25.4%), Consensus (6%).
- Fully unlocked (no remaining vesting cliff).
- FDV: ~$223 million.
- Hotspots deployed: 1 million+ by 2024. [[What is DePIN — OSL]]
- Migrated from its own L1 blockchain to Solana in 2023.
- PoC hacking: Bad actors falsely assert hotspot locations to steal token rewards from legitimate miners. Documented as a systemic problem — dozens of fake mining rings identified, stealing tens of thousands of HNT/month. [[Helium's Dirty Secret — HNT News]]

## The Proof of Coverage Problem

Helium's incentive design contains an inherent attack surface: miners earn tokens by claiming to provide wireless coverage, but coverage is hard to verify trustlessly. Hackers:
1. Buy multiple miners, assert false locations in same geographic cluster.
2. Miners "witness" each other's beacons over short distance (feet, not miles).
3. Claim distance-based PoC rewards while providing zero real coverage.
4. Pattern: evenly spaced dots on coverage map (too perfect to be organic).

This illustrates the fundamental verification challenge in DePIN: how to prove physical service delivery on a blockchain. Wireless mapping — physically driving to check coverage — is the only definitive verification method, which is expensive and non-scalable.

## Newsletter Relevance

Helium is the canonical DePIN success story and cautionary tale simultaneously. It proved that token incentives can deploy physical infrastructure at scale with no central capex. It also proved that those same incentives attract sophisticated fraud. The PoC hacking problem is not unique to Helium — any DePIN with location-based rewards faces this attack surface. For a newsletter covering power and infrastructure, Helium asks: can decentralized ownership of critical infrastructure actually work?

## Connections

- [[DePIN]] — concept page; Helium is the leading case study
- [[Render Network]] — other major DePIN (GPU compute)
- [[Gala Games]] — DePIN for gaming (GalaChain nodes)

## Source Appearances

- [[Helium HNT Tokenomics — Tokenomist]] — supply/vesting data
- [[Helium's Dirty Secret — HNT News]] — PoC hacking documentation
- [[What is DePIN — OSL]] — included as key DePIN example
- [[Why DePIN Matters — a16z crypto]] — cited as proof-of-concept for DePIN capex model

## Open Questions

- Has the migration to Solana resolved the PoC hacking problem, or just shifted it?
- What is Helium's actual active coverage vs. nominal hotspot count?
- Can 5G Helium compete with T-Mobile/Verizon for real consumer use?
- What does the token allocation to "Founders and Investors" (32.6%) mean for long-term decentralization?
