---
title: "Helium HIP-0143 — Decoupling Service Provider Pricing from Governance"
type: source
tags: [technology, infrastructure, crypto, depin]
created: 2026-04-07
updated: 2026-04-07
sources: 3
raw: "raw/HIP0143-decoupling-service-provider-pricing-from-governance.md at main · heliumHIP.md"
source_url: "https://github.com/helium/HIP/blob/main/0143-decoupling-service-provider-pricing-from-governance.md"
author: "inversioncapital, zer0tweets, Nova Labs, ferebee"
published: 2025-01-29
---


[Original source](https://github.com/helium/HIP/blob/main/0143-decoupling-service-provider-pricing-from-governance.md)

## Summary

Helium Improvement Proposal (HIP) #143 that authorizes Nova Labs (Helium's primary commercial partner) to negotiate data transfer pricing with network operators independently — without going through full Helium governance for each deal. The nominal rate remains $0.50/GB but Nova Labs can adjust the ratio of rewarded vs. unrewarded data for commercial partners.

## Key Points

- Helium Network used by multiple U.S. mobile network operators (offload agreements) plus one in Mexico.
- Nova Labs converts dollar payments from operators into HNT (burned for Data Credits) at $0.50/GB.
- Problem: different operators have different pricing models (per-GB, flat monthly, per-user caps); handling each through governance is too slow.
- Solution: delegate pricing negotiation to Nova Labs, bypassing governance for 1 year.
- Impact: hotspot owners benefit from increased Data Transfer; HNT holders benefit from more utility.

## Newsletter Angles

- This HIP is a fascinating governance case: a DePIN protocol that's supposedly decentralized is delegating its commercial negotiation to a centralized entity (Nova Labs) for operational efficiency. The "DePIN mullet" in action.
- The tension between decentralized governance and enterprise sales speed is exactly what a16z described as the core challenge for DePIN protocols.

## Entities Mentioned

- [[Helium Network]] — the network this governs

## Concepts Mentioned

- [[DePIN]] — governance structure of DePIN protocols
- [[Tokenomics]] — Data Credit burn mechanism

## Notes

Primary governance document. Demonstrates real-world friction between crypto-native governance processes and commercial business needs. The 1-year delegation period suggests this is recognized as a temporary pragmatic fix, not a permanent solution.
