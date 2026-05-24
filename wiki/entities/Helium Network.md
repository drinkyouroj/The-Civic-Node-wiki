---
title: "Helium Network"
aliases: ["Helium"]
type: entity
entity_type: infrastructure
tags: [technology, infrastructure, crypto, depin]
created: 2026-04-07
updated: 2026-05-24
sources: 16
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

## Operator Economics (updated 2026-05-16)

- **Peak earnings (2021):** Hotspots marketed as earning "hundreds of dollars daily"; network grew 14K → 450K hotspots in 12 months.
- **Current earnings (2025):** Most operators earn **$3–$45/month**; common range is $4–$8/month. Urban hotspots in dense hexes earn $0.10–$1.50/day.
- **"Lone Wolf" rule:** Hotspots with no neighboring hotspot within LoRaWAN range earn **zero HNT from PoC**. Rural/isolated deployments have been economically exited from the PoC reward system.
- **Real utility baseline (March 2024):** Only $87 in IoT data credits burned in a 24-hour period; total daily network revenue ~$3,307. IoT genuine data credit burns were "less than $2,000/month" during Aug–Oct 2022 when 600K hotspots were deployed. [[Helium Operator Economics — Bytetree - 2024-03]]
- **August 2025 halving:** New HNT minted per year cut from 15M to 7.5M on Aug 1 2025. PoC rewards halved. Data Transfer rewards scale with usage, not halving.
- **HIP-138 (Jan 2025):** IoT Hotspots stopped earning IOT tokens; Mobile Hotspots stopped earning MOBILE token. All rewards now in HNT.
- **Network contraction:** Peak ~1M hotspots (Q1 2023) → ~350K–400K active by 2025 (60% contraction). Active count stabilized around 350K–370K. [[Helium Hotspot Earnings 2025 — AMBCrypto]]

## Network Revenue (2025) — Messari Q4 2025 data

- **Annualized network revenue (ex-discretionary burns):** $11.0 million
- **December 2025 monthly revenue:** $1.9 million ($22.4M annualized run-rate)
- **Average daily Data Credit burns (Q4):** $56,760 (83.6% QoQ growth)
- **Mobile vs IoT share of daily burns:** Mobile $56,635 (99.8%); **IoT just $124.77 (0.2%)**
- **Mobile Offloading share of Mobile burns:** 43.9% ($24,883/day)
- **Discretionary burn experiment (Aug 2025 – Jan 2 2026):** Helium Mobile routed 100% of subscriber revenue to HNT purchases on open market. Q4 produced $2.9M in artificial buying pressure. Suspended Jan 2 2026 by CEO Amir Haleem.
- **Carrier offload (Q4 2025):** 4,388 TB (60.7% QoQ); cumulative 9,839 TB since inception
- **Carrier partners:** T-Mobile (MVNO backbone), AT&T (April 2025), Movistar (Telefónica), Google Orion, Wefi, Mambo WiFi (Brazil, Dec 2025)
- **Helium Mobile signups (end Q4 2025):** 595,800 (29.1% QoQ); 1,815 daily new signups
- **Daily active users (Q4):** 1.6M average; peak 2.5M Dec 20 2025
- **Average daily mobile paid traffic:** 49.6 TB (52.9% QoQ)
- **Mobile Hotspots total:** 121,138 (+8.5% QoQ); 29.5% Helium-branded, 70.5% Helium Plus
- **IoT Hotspots:** ~385,000 total; only 0.9% QoQ growth
- **HNT price Q4:** $2.44 → $1.37 (-43.9% QoQ); market-cap rank 128th → 136th
- [[State of Helium Q4 2025 — Messari]], [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]]

## Helium Mobile Plans (2025–2026)

- **Zero:** $0/month — 1 GB Nationwide + 2 GB Helium Hotspot
- **Sprout (Kids):** $5/month — 3 GB
- **Air:** $15/month — 10 GB
- **Infinity:** $30/month — Unlimited

All plans earn Cloud Points redeemable for eGift cards or charity donations.

## Key HIPs Governing Operator Economics

- **HIP-52 (IoT subDAO):** Created the IoT subDAO and restructured reward pools between PoC and data transfer.
- **HIP-82 (2023):** Introduced rewardable data caps for Helium Mobile service. Cap formula: $subscription_cost / $0.50 GB = max rewardable GB per subscriber per billing cycle. Operators earn nothing on data above this cap. [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]]
- **HIP-129:** Further adjustments to rewardable data rules.
- **HIP-138 (Nov 2024, implemented Jan 2025):** Single HNT token; IOT and MOBILE subDAO tokens retired.
- **HIP-143 (vote: April 3, 2025):** Authorized Nova Labs to negotiate carrier pricing without governance approval for 1 year (auto-renews). **Vote result: 90.53% for / 9.46% against** (763.5M veHNT cast, against a 100M quorum). **The Nova Labs proxy controlled 26% of the vote; the ferebee proxy (co-author) controlled 24%. Together, the proposing entity and its co-author cast 50% of the yes votes for the proposal authorizing Nova Labs's pricing authority.** As of Q4 2025 (Messari report), no superseding HIP had been passed — auto-renewal would occur around April 2026. [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]], [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- **HIP-148 (vote: October 3–10, 2025; passed 96.72% for / 3.27% against on 902.3M veHNT):** Eliminated Mobile Mapping rewards (the proposal text cites gaming behavior, <5% verification-mapping rate, and "carrier offload locations are a much higher quality signal of where to deploy than mapping data"). Redirected the 20% of HNT emissions previously earmarked for Mobile Mapping rewards: 10% to the Service Provider Pool, 10% to the Data Transfer Pool. **In a bundled change, repealed HIP-87's proportional Service Provider formula and rolled the 4% Oracle Operator allocation into the Service Provider Pool — making the Service Provider Pool 24% of Mobile emissions, emitted directly to a single named recipient: Nova Labs.** Subscribers who previously earned HNT for mapping data now earn Cloud Points (gift-card credits redeemable for eGift cards or charity donations) instead. **Proxy concentration: ferebee 31.00% + Nova Labs 26.00% = 57% of total vote** (60.5% of yes votes) — more concentrated than HIP-143's 50%. ferebee's absolute veHNT grew 55.5% between the two votes (183.85M → 285.92M) while Nova Labs grew 21% — the proposing-entity proxies are accumulating veHNT faster than the network. Single named "Against" voter: Keith Rettig at 1.00% (13.98M veHNT). Second governance-changes-economics-after-deployment event in 18 months. [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]], [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]], [[State of Helium Q4 2025 — Messari]]
- **HIP-20 (Nov 18, 2020):** Established 223M HNT max supply and 2-year halving cadence on August 1 (genesis anniversary). The August 2025 halving was the third. [[Helium Halving 2025 — Helium Blog - 2025-07-24]]

## veHNT Governance Mechanics

- **Lock duration scales voting power:** 1 HNT locked 1 year = 25 veHNT; 1 HNT locked 4 years = 100 veHNT.
- **Emissions delegation:** veHNT holders split daily emissions between Mobile and IoT subDAOs by delegation; current split ~75% Mobile / ~25% IoT.
- **Aug 1 2025 reset:** All delegations made before July 1, 2025 reset on August 1, 2025. Operators who did not re-delegate AND assign a proxy lost reward eligibility regardless of hardware deployment.
- **Foundation-endorsed proxy voting:** Helium Foundation explicitly recommends operators delegate their vote to "a trusted community member or group" as a default — directly enabling the proxy concentration seen in HIP-143. [[Helium Halving 2025 — Helium Blog - 2025-07-24]]

## Open Questions

- **HIP-143 auto-renewal:** The 1-year provision should have auto-renewed around April 2026. No superseding HIP appears in the Q4 2025 record. Status as of May 2026: presumed still in effect via auto-renewal — no governance action to override.
- Has the migration to Solana resolved the PoC hacking problem, or just shifted it?
- What does an operator in a dense urban area with real Helium Mobile carrier offload traffic actually earn per month? Per Q4 2025: $0.50/GB nominal rate, subject to HIP-82 rewardable data cap. A $30 Infinity subscriber generates max 60 GB/month rewardable across all hotspots that serve them.
- What is the actual revenue split between Nova Labs and the carriers on offload contracts? Not disclosed (per HIP-143).
- Can 5G Helium compete with T-Mobile/Verizon for real consumer use?

## Source Appearances

- [[Helium HNT Tokenomics — Tokenomist]] — supply/vesting data
- [[Helium's Dirty Secret — HNT News]] — PoC hacking documentation
- [[What is DePIN — OSL]] — included as key DePIN example
- [[Why DePIN Matters — a16z crypto]] — cited as proof-of-concept for DePIN capex model
- [[Helium Operator Economics — Bytetree - 2024-03]] — operator economics collapse; $87/day IoT data
- [[Helium Hotspot Earnings 2025 — AMBCrypto]] — 2025 earnings ranges; Lone Wolf rule
- [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]] — 2025 network revenue and carrier offload data
- [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]] — vote tally + proxy concentration; Nova Labs + ferebee = 50% of yes votes
- [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]] — primary proposal text; eliminates mapping rewards, consolidates 24% of Mobile emissions directly to Nova Labs
- [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]] — primary-source vote screenshots; 96.72% for / 3.27% against on 902.3M veHNT; **ferebee 31% + Nova Labs 26% = 57% of total vote**; ferebee's veHNT +55.5% absolute between HIP-143 and HIP-148
- [[State of Helium Q4 2025 — Messari]] — Q4 2025 revenue, burns, hotspot counts, HIP-148
- [[Helium Halving 2025 — Helium Blog - 2025-07-24]] — Aug 2025 halving mechanics; veHNT reset and proxy recommendation

## Published Synthesis

- [[You Own the Hotspot. Nova Labs Owns What It Earns.]] (Substack flagship, published 2026-05-21) — first popular-form newsletter article making the [[Franchise vs. Business]] / [[Proxy Concentration Audit]] / [[Auto-Renewal by Inaction]] argument legible at the public level, using the Helium worked example. The piece names the IoT-vs-Mobile revenue split ($124.77/day vs $56,635/day) as the load-bearing finding; the HIP-143 + HIP-148 proxy concentration as the structural pattern; the four-component disclosure standard (floor + exit, aggregate revenue disclosure, geographic acknowledgment, active-re-vote sunsets) as the proposed audit framework; the FTC Franchise Rule / 16 CFR Part 436 FDD as the federal-disclosure-regime analogy; and a Datagram self-correction as the demonstration of the framework's limit.
