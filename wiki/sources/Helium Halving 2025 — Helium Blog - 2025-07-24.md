---
title: "Helium Halving 2025 — Helium Blog"
type: source
tags: [technology, infrastructure, crypto, depin, governance]
created: 2026-05-16
updated: 2026-05-16
sources: 5
raw: "raw/Helium Halving 2025 What It Means for Hotspot Operators, HNT Holders, and Network Governance.md"
source_url: "https://blog.helium.com/helium-halving-2025-8ecaa1fff464"
author: "Helium🎈 (Helium Foundation)"
published: 2025-07-24
---

[Original source](https://blog.helium.com/helium-halving-2025-8ecaa1fff464)

## Summary

First-party Helium Foundation explainer on the August 1, 2025 halving — the third in network history. Confirms that PoC rewards were directly halved while data transfer rewards were unaffected. Also documents the **veHNT delegation reset on August 1, 2025**: all delegations made before July 1 were reset, and operators who didn't re-delegate AND assign a proxy lost reward eligibility. Important first-party documentation of how governance mechanics force operator participation in voting they may not understand.

## Key Points

**Halving mechanics:**
- Date: August 1, 2025 (genesis anniversary; third halving)
- Annual emissions: 15M HNT → 7.5M HNT
- Daily HNT issuance: 20,548 HNT/day after halving
- Established by HIP-20 (November 18, 2020) — fixed maximum supply + 2-year halvings

**Impact on Hotspot operators:**
- **PoC rewards:** "directly impacted...halved, however be aware that the actual earnings rate may be reduced by more or less than half depending on additional network factors"
- **Data transfer rewards:** "unaffected by the halving...if a Mobile Hotspot was earning the HNT equivalent of $0.50 per gigabyte of data transferred before the halving, it will still earn roughly $0.50 worth of HNT per GB transferred"
- Net effect: rural and low-traffic hotspots (PoC-dependent) lose half their already-minimal earnings; urban traffic-routing hotspots are unaffected

**veHNT governance mechanics:**
- veHNT = vote-escrowed HNT; voting power scales with lock duration
- 1 HNT locked 1 year = 25 veHNT
- 1 HNT locked 4 years = 100 veHNT (4× lock = 4× voting power)
- Current emissions split: ~75% Mobile / ~25% IoT (based on delegation totals)

**The August 1 delegation reset (operator-facing requirement):**
- **All delegations made before July 1, 2025 reset on August 1, 2025**
- Operators must (a) re-delegate veHNT to a sub-network and (b) assign a voting proxy
- If neither is done, no rewards earned regardless of hardware deployment
- "Your rewards now also depend on your participation — not just where you delegate. This decoupling encourages voting based on what's best for the network, not personal yield."

**Proxy voting endorsement:**
- The blog explicitly recommends operators delegate their vote to "a trusted community member or group" as a proxy
- Stated rationale: "ensuring you remain eligible for rewards even if you miss a proposal"
- The Helium Foundation is recommending that operators surrender voting power to proxies as a default — which directly enables the kind of vote concentration seen in the HIP-143 results

## Newsletter Angles

- **The "actual earnings rate may be reduced by more or less than half depending on additional network factors" sentence is operationally honest:** halving is the floor, not the ceiling. The combination of halving + density crowding + Lone Wolf rule means many operators' PoC rewards dropped by more than 50% on August 1.
- **The proxy-voting recommendation is the structural cause of HIP-143's voter concentration:** when the Foundation tells operators "set a proxy as a backup to ensure you don't miss out on rewards," it normalizes the surrender of voting power. Two large proxies (Nova Labs + ferebee) then controlled 50% of HIP-143's yes votes.
- **The decoupling of rewards from yield optimization** (your rewards depend on participation, not just where you delegate) is described as protecting the network from self-interested voters. The same mechanism makes it harder for operators to *exit* via abstention without losing their hardware-investment returns.
- **PoC vs Data Transfer asymmetry** under the halving formalizes what HIP-82 began: urban/traffic-routing hotspots are economically privileged; coverage-only hotspots are economically exited. This is now first-party language from the Helium Foundation, not third-party critique.

## Entities Mentioned

- [[Helium Network]] — protocol undergoing the halving
- [[Helium Foundation]] — author/explainer
- [[Nova Labs]] — implied; operates Helium Mobile and core protocol

## Concepts Mentioned

- [[DePIN]] — operator economics under emissions reduction
- [[Tokenomics]] — halving as supply mechanic; veHNT governance

## Notes

First-party document from the Helium Foundation. Operationally honest about the asymmetric impact of the halving (PoC halved, data transfer unaffected) — does not pretend the impact is uniform. Useful as a citation when arguing that "the network is rewarding traffic-routing, not coverage" because the network itself is now saying so.

The proxy-voting recommendation matters for the article's HIP-143 argument: Foundation policy directly encourages the proxy concentration that enabled the HIP-143 vote outcome.
