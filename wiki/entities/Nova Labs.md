---
title: "Nova Labs"
type: entity
entity_type: organization
tags: [depin, helium, governance, franchise, crypto, technology]
created: 2026-05-21
updated: 2026-05-24
sources: 18
---

## Overview

Nova Labs is the for-profit company that operates [[Helium Network]]'s consumer mobile service ([[Helium Mobile]]) and negotiates the carrier offload deals with [[T-Mobile]], [[AT&T]], and other carriers that route traffic onto the operator-built Helium network. It is also the corporate counterparty named in the wallet labels of the largest single voting bloc in Helium governance — a 26% proxy that, combined with the co-author "ferebee" proxy, cast 50% of yes votes on [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance|HIP-143]] (the proposal authorizing Nova Labs's unilateral pricing authority) and 57% of the total vote on [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards|HIP-148]] (the proposal directing 24% of Mobile emissions to a single named recipient: Nova Labs).

Nova Labs is the worked example at the center of the [[Franchise vs. Business]] analytical framework documented in [[Helium HIP-143 and the DePIN Franchise Architecture]]. The corporate role and the governance-proxy role are not formally distinguished in public Helium materials. The combined role is what made the franchise architecture passable through DAO governance without operator participation.

## Key Facts

- **Corporate role**: Designs and sells the consumer mobile service ([[Helium Mobile]]) that monetizes the operator-built Helium 5G network. Negotiates carrier-offload contracts (T-Mobile MVNO backbone, AT&T April 2025, Movistar/Telefónica, Google Orion, Wefi, Mambo WiFi). Pricing terms with carriers are confidential per HIP-143's framing. [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]]
- **Governance role — HIP-143 vote (April 3, 2025)**: Listed as co-author with "Inversion Capital, zer0tweets, ferebee". The Nova Labs proxy controlled 26.00% of the vote; the ferebee proxy controlled 24.00%; together 50% of yes votes on the proposal authorizing Nova Labs's pricing authority. [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- **Governance role — HIP-148 vote (October 3–10, 2025)**: The Nova Labs proxy controlled 26.00% (241.87M veHNT, +21% absolute since HIP-143). The ferebee proxy grew to 31.00% (285.92M veHNT, +55.5% absolute). Combined 57% of total vote; 60.5% of yes votes. The proposal directed the consolidated 24% Service Provider Pool of Mobile emissions to Nova Labs as the single named recipient. [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- **Recipient-by-name in HIP-148 proposal text**: "To simplify technical implementation, we propose to emit the full allocation available from Service Provider Rewards and Oracle Operator Rewards to the single Service Provider Nova Labs, allowing Nova to use the pool as needed for protocol development, operations including Oracles, and subscriber incentives." [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]
- **Not the author of every HIP that built the franchise**: HIP-53 (the proposal that created the MOBILE subDAO and set the $0.50/GB data transfer rate that anchors all subsequent operator economics) was authored by `@nrnrsdwsrk, @kjake-vmcc, @gabreyem2367, @asknsy, Joey Padden` — Nova Labs is not listed. The franchise architecture extends across multiple HIPs with different authorship; the structural pattern is consistent, but the corporate fingerprint is not on every step. [[Helium HIP-53 Vote Results — Helium Vote - 2022-07-25]]
- **veHNT accumulation rate**: The Nova Labs proxy grew +21% in absolute veHNT between HIP-143 (April 2025) and HIP-148 (October 2025). The ferebee proxy grew +55.5% over the same window. Both substantially faster than network average. The franchise architecture compounds: future HIPs will be progressively easier to pass without operator participation.

## Newsletter Relevance

Nova Labs is the cleanest documented instance of the [[Franchise vs. Business]] structure in the DePIN sector — the corporate counterparty that benefits from a governance change is also the proxy that cast the largest vote bloc to pass it. This pattern is the analytical anchor for any future DePIN piece that needs to test whether operators bought a business (where they share in upside) or a franchise (where the corporate counterparty extracts ongoing rents through governance the operators are recommended to delegate). It is also the substrate for the [[Proxy Concentration Audit]] move — the procedural test that surfaces these structures from on-chain vote receipts before they get framed as "community consensus" by the secondary press.

The May 21, 2026 flagship piece *[[You Own the Hotspot. Nova Labs Owns What It Earns.]]* (published) is the first newsletter article to make the corporate counterparty + governance proxy collapse legible at the public level. The piece names the IoT-vs-Mobile revenue gap as the load-bearing finding, lays out the HIP-143 + HIP-148 proxy concentration sequence, proposes a four-component disclosure standard (floor + exit, aggregate revenue disclosure, geographic acknowledgment, active-re-vote sunsets), and closes with a Datagram self-correction. (Note: the article was published Thursday May 21, not the wiki's earlier-assumed Friday May 22 — flag for content-calendar tracking.)

## Connections

- [[Helium Network]] — the protocol Nova Labs operates and governs as the largest single bloc
- [[Helium Mobile]] — the consumer-facing mobile service Nova Labs designs and sells (Zero / Sprout / Air / Infinity plans, Cloud Points loyalty mechanic)
- **ferebee** — the second-largest governance proxy. HIP-143 lists "ferebee" among the authors; the relationship between ferebee and Nova Labs is not disclosed publicly. The two proxies have voted in alignment on every documented governance change since HIP-143. *(Entity page deferred until raw materials on ferebee's identity are captured.)*
- [[Franchise vs. Business]] — the analytical move; Nova Labs is the worked example
- [[Proxy Concentration Audit]] — the procedural test; Nova Labs + ferebee = the pattern the test surfaces
- [[Auto-Renewal by Inaction]] — HIP-143's 1-year delegation re-armed in April 2026 with no operator participation, extending Nova Labs's pricing authority by default
- [[Chokepoint Control]] — Nova Labs holds the pricing-authority chokepoint at the protocol layer; the synthesis [[Helium HIP-143 and the DePIN Franchise Architecture]] extends [[Chokepoint Control]] to the DePIN-protocol layer
- [[DePIN]] — the category the franchise architecture lives inside

## Source Appearances

- [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]] — Nova Labs named as co-author; the proposal text argues confidentiality of carrier deals is structurally necessary; Nova Labs framed as the entity that can "move quickly without involving Helium governance"
- [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]] — Nova Labs proxy 26% + ferebee proxy 24% = 50% of yes votes; the on-chain receipt that made the proposing-entity-carries-the-vote pattern visible
- [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]] — Nova Labs named as the single recipient of the consolidated 24% Service Provider Pool of Mobile emissions; HNT-to-Cloud-Points subscriber substitution
- [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]] — Nova Labs proxy 26% + ferebee proxy 31% = 57% of total vote; the proxy concentration the franchise architecture had pushed further by Q4 2025
- [[State of Helium Q4 2025 — Messari]] — confirms no HIP superseding HIP-143 had been passed as of Q4 2025; auto-renewal would occur around April 2026
- [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]] — Mobile-side revenue Nova Labs monetizes
- [[Helium Hotspot Earnings 2025 — AMBCrypto]] — operator-side economics that frame the franchise gap ($3–$45/month current earnings vs. 2021 marketing claims of "hundreds per day")
- [[Helium Operator Economics — Bytetree - 2024-03]] — hardware costs ($249 indoor, $949 outdoor) and 2.5–20 year payback periods
- [[Helium Halving 2025 — Helium Blog - 2025-07-24]] — Foundation policy recommending operators delegate votes to proxies, the mechanism that normalizes the concentration Nova Labs benefits from
- [[Helium HIP-143 and the DePIN Franchise Architecture]] — the synthesis that names the corporate-counterparty / governance-proxy collapse as the franchise pattern
- [[You Own the Hotspot. Nova Labs Owns What It Earns.]] — the published flagship article (Substack, 2026-05-21) translating the wiki's franchise-architecture findings into popular form

## Open Questions

- **What is the ownership and operating relationship between Nova Labs and ferebee?** Public sources document each as a Helium-ecosystem actor; the proxy voting alignment on HIP-143 and HIP-148 suggests closer coordination than the public framing implies. Resolving this question would either (a) confirm a single coordinated bloc carries 50–57% of Helium governance, or (b) document a public-private alignment that doesn't require formal coordination. Either answer materially changes the franchise-architecture diagnosis.
- **Who authored HIP-148?** The GitHub handle `madninja` is listed; the relationship to the HIP-143 authors (Nova Labs, ferebee, Inversion Capital, zer0tweets) is undisclosed. If `madninja` maps to one of the named authors, the franchise architecture is more concentrated than the public authorship suggests. If `madninja` is independent, then the architecture is being propagated by third-party authors voted in by the proposing-entity proxies. Both readings are unflattering; the choice between them matters for accurately naming who designed the HNT-to-Cloud-Points substitution.
- **What does Nova Labs actually pay carriers per gigabyte vs. what flows through to operators?** Confidentiality per HIP-143. Aggregate utility revenue ($56,635/day Q4 2025 Mobile-side; $124.77/day IoT-side) is in [[State of Helium Q4 2025 — Messari]]. The unit economics are not. The opacity is structural, not incidental.
- **Has Nova Labs received any private commitments from carrier counterparties tied to specific governance outcomes?** Not knowable from public sources. Worth flagging as a hypothesis the public materials cannot rule in or out.
- **What is the corporate parent / ownership stack above Nova Labs?** The Helium Foundation is a separate entity that publishes the operator guidance recommending proxy delegation. The relationship between Nova Labs and the Foundation, and whether either has private investors with veto rights, is not part of the public Helium documentation.
