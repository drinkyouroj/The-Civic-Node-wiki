---
title: "Compound Finance Governance Documentation"
type: source
tags: [crypto, technology]
created: 2026-04-07
updated: 2026-04-07
sources: 1
raw: "raw/Governance.md"
author: "Compound Finance"
published: 2019-01-01
---

## Summary

Technical documentation of Compound Finance's on-chain governance system using COMP token holders, Governor Bravo, and a Timelock. Proposals require 25,000 COMP delegated; voting lasts 3 days; 400,000 votes minimum for passage; 2-day Timelock delay before execution. Includes a Pause Guardian (multi-sig) for emergency security actions.

## Key Points

- 25,000 COMP required to create a governance proposal (~2.5% of total supply).
- Any address can create an "Autonomous Proposal" by locking 100 COMP; becomes formal if it receives 25,000 delegated COMP.
- Voting: 3-day period; simple majority + 400,000 votes minimum quorum required.
- Timelock: 2-day minimum delay before execution of any proposal.
- Changes to protocol take at least one week (proposal + vote + timelock).
- Pause Guardian (multi-sig): can disable specific functions (Mint, Borrow, Transfer, Liquidate) but cannot unpause or prevent Redeem/Repay — emergency-only one-way gate.
- COMP is ERC-20; delegation is automatic when balance changes.

## Newsletter Angles

- The Pause Guardian mechanic is an interesting governance compromise: decentralized in normal operation but with an emergency brake held by a small multi-sig. This is the DeFi equivalent of a central bank "extraordinary measures" clause.
- The 400,000 vote quorum in practice: COMP is heavily concentrated among early investors and team — governance decisions can pass with relatively few unique voters.
- One-week minimum for protocol changes is a feature, not a bug: in DeFi, speed of governance change is a security surface. The Timelock forces deliberation.

## Concepts Mentioned

- [[Tokenomics]] — COMP governance token distribution determines protocol control
- [[DePIN]] — Compound's governance model is widely copied in DeFi and DePIN protocols

## Notes

Official technical documentation. Compound is one of the pioneering DeFi protocols; its governance model has been widely copied (Governor Bravo is now used by many protocols including Uniswap). The Pause Guardian held by the "Community Multi-Sig" creates a centralization point that is technically justified but governance-problematic.
