---
title: "Building a DAO Framework Aragon CTO Interview"
type: source
tags: [crypto, technology]
created: 2026-04-07
updated: 2026-04-07
sources: 2
raw: "raw/Building a DAO Framework Interview with Aragon's CTO Aragon Resource Library.md"
source_url: "https://www.aragon.org/how-to/building-a-dao-framework-interview-with-aragons-cto"
author: "Aragon"
published: 2020-12-22
---


[Original source](https://www.aragon.org/how-to/building-a-dao-framework-interview-with-aragons-cto)

## Summary

Interview with Aragon's CTO Carlos explaining the architecture of Aragon OSx, a modular DAO (Decentralized Autonomous Organization) framework. The framework separates DAO treasury (simple, immutable core) from governance logic (modular plugins), allowing organizations to upgrade governance without migrating treasuries.

## Key Points

- Aragon OSx has two layers: core contracts (DAO vault + permission manager) and framework contracts (factories, registry, plugin manager).
- Core principle: keep the treasury contract minimal and immutable; all logic goes in plugins that can be swapped.
- Plugins are permissioned external contracts that can be added, removed, or upgraded without redeploying the DAO.
- Permission management: oracles can encode off-chain conditions (e.g., "only on Tuesdays") into governance logic.
- Use cases: multisig voting, ERC-20 token voting, NFT voting, delegated governance.
- Account abstraction: DAO can function as a smart wallet with conditional spending limits.
- Anyone can build plugins without approval; no API key required.
- Goal: "Anything can be a DAO" — any organization that needs to manage resources collectively.

## Newsletter Angles

- The plugin model as a governance abstraction layer — DAOs can theoretically upgrade their decision-making rules without a political rupture, just a technical transaction. This is the governance promise of Web3, in code form.
- The contrast with traditional organizations: a corporation must amend its charter and get legal approval to change governance structures; a DAO can do it in a block.
- Limits: this assumes the permission manager itself is trusted. The "simplicity is security" argument works only if the core contract is actually simple enough to audit and trust.

## Concepts Mentioned

- [[Tokenomics]] — DAO treasury management is the application of token-based governance to resource allocation
- [[DePIN]] — DAOs are the governance layer for DePIN networks (Helium, Render, etc. all have governance mechanisms)

## Notes

Promotional content from Aragon (not independent analysis). Published 2020 — the DAO space has evolved significantly since then. The conceptual framework remains relevant for understanding DAO governance design.
