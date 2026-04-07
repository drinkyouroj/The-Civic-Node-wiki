---
title: "Uniswap Governance Overview"
type: source
tags: [crypto, technology]
created: 2026-04-07
updated: 2026-04-07
sources: 1
raw: "raw/Overview Uniswap.md"
author: "Uniswap"
published: 2026-01-01
---

## Summary

Technical documentation of Uniswap's on-chain governance system using UNI token holders, a Governor Bravo module, and a Timelock contract. Governance proposals require 2.5M UNI delegated (0.25% of supply) to propose, 7-day voting period, simple majority with 40M "For" votes quorum, and 2-day Timelock delay before execution.

## Key Points

- UNI holders with 2.5M delegated tokens (0.25% of 1B total supply) can create proposals.
- 7-day voting period; simple majority + quorum of 40M "For" votes required.
- Timelock: 2-day minimum delay after vote before execution; major upgrades up to 30 days.
- Delegates can receive voting rights from other holders.
- Executable code is included in proposals — not just signals.
- Governor Bravo is the governance module.

## Newsletter Angles

- On-chain governance as a power architecture: Uniswap's governance structure means large UNI holders (venture firms, early contributors) have disproportionate control. The 2.5M threshold to propose is high enough to effectively require institutional backing.
- The 40M quorum requirement: in practice, voter turnout is often low in DeFi governance, meaning major UNI holders can pass proposals with relatively few votes.
- Timelock as a safeguard: the 2-day minimum delay gives the community time to notice and respond to malicious proposals. This is a governance security feature absent in most traditional corporate governance.

## Concepts Mentioned

- [[Tokenomics]] — UNI token distribution determines governance power; concentration creates plutocracy risk
- [[DePIN]] — similar governance models are used in DePIN protocols

## Notes

Technical governance documentation. The Governor Bravo referenced is a now-updated version; the docs note some reference material may be out of date. Key reference for understanding DeFi governance mechanics.
