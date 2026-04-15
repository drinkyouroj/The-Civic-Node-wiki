---
title: "Hashcash Announcement to Cypherpunks Mailing List 1997 — Adam Back"
type: source
tags: [crypto, bitcoin, technology, cypherpunk]
created: 2026-04-15
updated: 2026-04-15
sources: 5
raw: "raw/hashcash-cypherpunks.md"
source_url: "http://www.hashcash.org/papers/announce.txt"
author: "Adam Back"
published: 1997-03-28
---

[Original source](http://www.hashcash.org/papers/announce.txt)

## Summary

The original March 28, 1997 announcement of Hashcash, posted by Adam Back to the Cypherpunks mailing list (cypherpunks@toad.com). Subject line: "[ANNOUNCE] hash cash postage implementation." This is the primary document confirming both the 1997 date and the invention of the proof-of-work mechanism that Bitcoin's mining system would later adapt. Back was posting from aba@dcs.ex.ac.uk — University of Exeter.

## Key Points

- **Date:** Friday, March 28, 1997. Posted to cypherpunks@toad.com.
- **Author email:** aba@dcs.ex.ac.uk (University of Exeter, UK) — confirms Back was based in England at the time.
- **Core mechanism:** "A partial hash collision based postage scheme." The key asymmetry: collisions "can be made arbitrarily expensive to compute (by choosing the desired number of bits of collision), and yet can be verified instantly." This asymmetry — expensive to produce, cheap to verify — is exactly what Bitcoin's mining inherits.
- **Primary application:** Anti-spam postage. Computing 1,000,000 × 20-bit hashes = "100 MIP years which is going to be more compute than they've got" — making mass spam economically unviable without centralizing identity or payment.
- **Why this matters for Bitcoin:** Satoshi explicitly cited Hashcash in Section 4 of the Bitcoin whitepaper as the inspiration for Bitcoin's proof-of-work mechanism. This post is the origin document of that citation.
- **Cypherpunk context:** The announcement goes to cypherpunks@toad.com — the same mailing list where Bitcoin's intellectual precursors (b-money, bit gold, reusable proof-of-work) were developed and debated. Back was posting to the exact same community from which Satoshi would later emerge.
- **Anti-surveillance framing:** Back positioned Hashcash as keeping "net culture of free discourse" — a Cypherpunk value framing, not just a technical framing.
- Back's post includes working code (compile instructions, usage examples), SHA1 implementation, double-spending protection database — not just a concept paper.

## Newsletter Angles

- This post is proof that in March 1997, Adam Back was an active contributor to the exact intellectual community from which Bitcoin emerged — sending working code to the same mailing list where Satoshi later announced the whitepaper.
- The "expensive to compute, instantly verifiable" asymmetry Back described in 1997 is the essential Bitcoin mining mechanism. The conceptual bridge from Hashcash to Bitcoin is not circumstantial — it's a direct citation with working code.
- Back's University of Exeter email confirms his British identity at the time — consistent with Satoshi's documented British spelling patterns ("bloody," "favour," etc.) noted in the NYT investigation.

## Entities Mentioned

- [[Adam Back]] — author; inventor of Hashcash; posting from University of Exeter; member of Cypherpunks mailing list
- [[Satoshi Nakamoto]] — not present in this source, but cited Hashcash in the Bitcoin whitepaper 11 years later
- [[Bitcoin]] — the later system that built on Hashcash's proof-of-work mechanism

## Concepts Mentioned

- [[Cypherpunk Movement]] — the mailing list this was posted to; the intellectual community connecting Hashcash to Bitcoin
- [[Bitcoin Origin Mystery]] — this post is evidence that Back was active and technically capable in the exact community and period relevant to Satoshi's identity

## Quotes

> "A partial hash collision based postage scheme... they can be made arbitrarily expensive to compute (by choosing the desired number of bits of collision), and yet can be verified instantly." — Adam Back, March 28, 1997

## Notes

Primary source — the original post. Hosted permanently at hashcash.org. Published 11 years before the Bitcoin whitepaper. The date (March 28, 1997) is embedded in the email header. Back's email suffix (@dcs.ex.ac.uk) places him at the University of Exeter's Department of Computer Science in 1997. This is the definitive citation for "In 1997 he invented Hashcash" — not a retrospective account but the contemporaneous announcement.
