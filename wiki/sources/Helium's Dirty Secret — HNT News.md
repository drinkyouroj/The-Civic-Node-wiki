---
title: "Helium's Dirty Secret — HNT News"
type: source
tags: [technology, infrastructure, crypto, depin]
created: 2026-04-07
updated: 2026-04-07
sources: 1
raw: "raw/Helium's Dirty Secret - POC Hacking Explained HNT News Helium Network Blog.md"
author: "Hans"
published: 2021-01-12
---

## Summary

Community blog post documenting the Proof of Coverage (PoC) hacking problem in the Helium network — where bad actors falsely assert hotspot locations to steal token rewards from legitimate miners. The author physically verified one hacking network by driving through the area with a wireless mapper and confirming zero coverage despite claimed rewards.

## Key Points

- PoC hacking: miners falsely assert locations, set up clusters of miners near each other, have them "witness" each other's beacons over short distances (feet, not miles), claim distance-based rewards while providing zero real coverage.
- Hackers collect rewards proportional to the "pie" of HNT distributed monthly — steal from legitimate miners without adding coverage.
- Detection: evenly spaced dots on coverage map (too perfect to be organic); unusual witness patterns.
- Physical verification: author crawled through entire area with wireless mapper, got zero pings from a documented hacking ring.
- Legitimate mining patterns show organic, irregular spacing (neighbors tell neighbors, clusters grow unevenly).
- Seven specific hacker hotspot names documented from one ring in Georgia area.
- Estimated theft: "tens of thousands of HNT coins per month" at the time (~$13,000/month at $1.30/HNT).
- Wireless mapping is the only definitive detection method — expensive and non-scalable.

## Newsletter Angles

- This is the canary in the DePIN mine: if you pay people to provide physical services verified by other participants, you create an attack surface for collusion. Helium never fully solved this.
- The "proof" in Proof of Coverage is much weaker than it sounds — it's peer-to-peer attestation, which is gameable when peers coordinate.
- The physical verification approach (drive around with a wireless mapper) is almost comically analog as a solution to a blockchain security problem.

## Entities Mentioned

- [[Helium Network]] — the network being analyzed

## Concepts Mentioned

- [[DePIN]] — verification problem is core to all DePIN protocols
- [[Tokenomics]] — token reward structure creates the attack incentive

## Notes

Community blog from 2021 — early in Helium's life. The problem has evolved significantly since then; Helium migrated to Solana in 2023 and updated its verification mechanisms. But this piece captures the fundamental attack surface in the clearest terms. Primary source for anyone writing about DePIN verification challenges.
