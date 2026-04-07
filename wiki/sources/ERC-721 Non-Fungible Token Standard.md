---
title: "ERC-721 Non-Fungible Token Standard"
type: source
tags: [crypto, technology]
created: 2026-04-07
updated: 2026-04-07
sources: 1
raw: "raw/ERC-721 Non-Fungible Token Standard.md"
author: "William Entriken; Dieter Shirley; Jacob Evans; Nastassia Sachs / Ethereum"
published: 2018-01-24
---

## Summary

The EIP-721 standard specification defining non-fungible tokens (NFTs) on the Ethereum blockchain. Establishes the interface (functions, events) that compliant smart contracts must implement to track and transfer unique digital assets. Distinguishes NFTs from fungible ERC-20 tokens by requiring per-token ownership tracking.

## Key Points

- NFTs defined as individually distinct, non-interchangeable digital assets — each has a unique uint256 ID.
- Core functions: `ownerOf()`, `safeTransferFrom()`, `approve()`, `setApprovalForAll()`.
- Optional metadata extension: name, symbol, tokenURI — enables naming and describing each NFT.
- Optional enumeration extension: allows discovering all NFTs and those owned by an address.
- Scale: a contract deployed on testnet tracked 2^128 NFTs — scalability is not a structural limit.
- Design influenced by ERC-20 but fundamentally different: no `allowance` feature (quantity is always 0 or 1); transfer approval per-token or per-operator.
- Early NFT examples: CryptoKitties, CryptoPunks, Decentraland LAND.

## Newsletter Angles

- ERC-721 is the infrastructure layer that made the NFT boom (2021-2022) possible — a technical standard that created an explosion of speculative activity, like TCP/IP creating the dot-com era.
- The `tokenURI` function points off-chain for metadata — meaning most NFTs are backed by a URL that can 404. The "ownership" is of a blockchain entry pointing to an image server, not the image itself. This is a structural fragility rarely discussed in NFT marketing.
- "Deed" as the original intended term for NFT — implies the standard was conceived for property rights tracking, not speculative collectibles. The use cases diverged dramatically from the intent.

## Concepts Mentioned

- [[Tokenomics]] — NFT tokenomics are a specialized case: supply per collection is fixed, but the NFT standard itself imposes no supply limit

## Notes

Technical standard document. Authoritative source. The `tokenURI` off-chain metadata observation is not in the standard but is implied by the spec — implementations store metadata off-chain, creating the dependency.
