---
title: "Preventable Cyber Attack Impacts io.net DePIN"
type: source
tags: [crypto, technology, depin, power]
created: 2026-04-07
updated: 2026-04-07
sources: 2
raw: "raw/Preventable Cyber Attack Impacts Io.net.md"
source_url: "https://cryptodaily.co.uk/2024/05/preventable-cyber-attack-impacts-ionet"
author: "Crypto Daily"
published: 2024-05-05
---


[Original source](https://cryptodaily.co.uk/2024/05/preventable-cyber-attack-impacts-ionet)

## Summary

Report on a cyber attack on io.net (a Solana-based decentralized GPU compute network) in which ~2 million fake GPUs were used to mimic real GPU signals, earning fraudulent rewards and revealing actual node count misinformation. The $IO token launch was delayed by ~2 weeks as a result. The article uses this to argue for Trusted Execution Environments (TEEs) as the necessary security architecture for DePIN.

## Key Points

- Nearly 2 million fake GPUs inserted into io.net's network during the attack.
- Fake GPUs mimicked signals from real GPUs, earning incentive rewards for fake servers.
- Attack revealed the actual number of real machines was far less than claimed.
- Io.net postponed its $IO token launch by ~2 weeks post-attack.
- CEO Ahmad Shadid: "It will take about two weeks to get back on track."
- Super Protocol (NVIDIA partner) proposed TEEs (Trusted Execution Environments) as the solution.
- TEEs have embedded private keys that are physically unextractable — "impossible to fake."
- TEEs enable an attestation process that proves the authenticity and integrity of the execution environment.
- "Self-sovereign computing is the future of DePIN" — Super Protocol's framing.

## Newsletter Angles

- The attack is the worst-case DePIN failure mode made real: a project raised $1B valuation on a node count that was 97% fake, then got attacked by 2 million fake GPUs exploiting the same architectural vulnerability.
- TEE as the hardware root of trust: the solution proposed (using chips with physically embedded, unextractable private keys) is essentially importing semiconductor manufacturing trust into software networks. This is an interesting convergence of hardware and crypto security.
- The promotional angle: the article is partly a marketing piece for Super Protocol (they're positioning their TEE-based approach as the solution). Caveat accordingly. But the diagnosis is accurate.

## Concepts Mentioned

- [[DePIN]] — the attack exposed a fundamental DePIN security vulnerability
- [[Tokenomics]] — the airdrop incentive created the motivation to fake GPU participation

## Quotes

> "Almost two million fake GPUs were used to mimic the signals sent by genuine GPUs, thus fooling the network into recognizing them as legitimate."

> "TEEs are a fortified island of safety amid the raging and predator-filled sea of Web3."

## Notes

Source has a promotional angle (Super Protocol as the proposed solution). The technical description of TEE hardware is accurate. Companion to the Protos sybil attack article — the two sources together document the io.net disaster from different angles (the discovery phase vs. the attack phase).
