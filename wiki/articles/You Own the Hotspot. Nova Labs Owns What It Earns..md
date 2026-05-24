---
title: "You Own the Hotspot. Nova Labs Owns What It Earns."
type: article
article_type: nonfiction
tags: [depin, helium, governance, franchise, crypto, accountability, power]
published: 2026-05-21
created: 2026-05-24
updated: 2026-05-24
source: "published/You Own the Hotspot. Nova Labs Owns What It Earns..md"
source_url: "https://drinkyouroj.substack.com/p/you-own-the-hotspot-nova-labs-owns-what-it-earns"
---

[Read on Substack](https://drinkyouroj.substack.com/p/you-own-the-hotspot-nova-labs-owns-what-it-earns)

## The Argument

[[Helium Network]] operators bought a franchise; they were sold a business. The hardware they paid for ($249 indoor, $949 outdoor) is theirs. The pricing authority that determines what their hardware earns is not — it was granted to [[Nova Labs]] by [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance|HIP-143]] (April 2025), and HIP-143's text contains an auto-extension clause that re-armed the authority in April 2026 with no operator participation, no superseding HIP, and no signer required. Two HIPs (HIP-143, HIP-148) — six months apart, same proposing-entity bloc, second more concentrated than the first — got the pricing authority where it ended up. The fix isn't to forbid commercial flexibility (carrier-deal confidentiality is structurally legitimate). The fix is four written disclosures any operator-based protocol owes its operators *before* hardware ships: (1) a written floor with an exit right, (2) aggregate revenue disclosure even when carrier rate sheets stay confidential, (3) geographic-good acknowledgment (rural coverage ≠ urban traffic), (4) active-re-vote sunsets instead of inaction-default extensions. The article closes with a self-correction: the same four-component standard would have caught Helium in 2021 but would not have caught [[Datagram]] — Datagram passed the documentary tests and still had no business underneath the docs. The audit is the floor. It doesn't catch fraud.

## The Five-Section Structure

The piece is a five-section essay using the prior-piece-established Glitch / Source Code / Upgrade / My Debug template from the "Cheaper AI Won't Use Less of Anything" / debugging-vocabulary cluster:

1. **The Glitch — The vote that renewed itself in April**: HIP-143 + auto-extension clause; April 2026 trigger; 385,000 deployed hotspots; $4–$8/month earnings on $949 hardware = 10–20 year payback.
2. **The Source Code — Two votes, six months, concentration up**: HIP-53 (July 2022; subDAO + $0.50/GB) → HIP-138 (Nov 2024; HNT consolidation, anonymous 15% top voter) → halving (Aug 2025) → HIP-143 (Apr 2025; 50% of yes votes from Nova Labs proxy 26% + ferebee proxy 24%) → HIP-148 (Oct 2025; 57% of total vote from Nova Labs proxy 26% + ferebee proxy 31%, Jay M./@JMF proxy 5%). The IoT-side $124.77/day revenue vs. the Mobile-side $56,635/day revenue is named (the hardware that gives the project something to point at vs. the actual revenue). ferebee's veHNT grew +55.5% between HIP-143 and HIP-148 while network participation grew 18.2% — the franchise architecture is self-reinforcing through the lock-up mechanism.
3. **The Upgrade — What four disclosures would have caught**: The four-component standard (floor + exit, aggregate-revenue disclosure, geographic acknowledgment, active-re-vote sunsets) explicitly framed against the McDonald's Franchise Disclosure Document analogy: "McDonald's franchisees read a Franchise Disclosure Document before signing. Federal law requires it. The Helium operator received the equivalent document as a sequence of HIPs written *after* the hardware was already plugged in." The plain-language version of the deal: "You're buying a revenue-share position, priced by Nova Labs, on infrastructure you own and operate. Nova Labs's commercial terms are confidential. Your earnings are a function of their carrier negotiations and the network's data traffic, neither of which you control."
4. **My Debug — The audit caught Helium. It missed my project.**: The Datagram self-correction. "Earlier pieces I published on DePIN positioned Datagram as the legitimate counter-example, the project doing decentralized infrastructure differently. That framing was wrong, and I should have caught it earlier." The four-component standard would have caught Helium in 2021; it would not have caught Datagram (closed-source software, alpha-testnet stats the author told himself were off because the company "needed a compelling story before exchanges committed"). "The audit is the floor. It doesn't catch fraud."
5. **The closer-to-next-piece tag**: References [[Atlanta Passed a Sanctuary Resolution. The Vendor Contract Didn't.]] as the prior procurement-workaround case, signals the next piece (May 29) will document the same procurement-workaround pattern at the federal level — running through [[CISA]], [[Age Verification]] vendors, and [[BetterHelp]].

## Key Sources Cited

- [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]] — primary proposal text, auto-extension clause, commercial rationale
- [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]] — 90.53% pass; Nova Labs proxy 26% + ferebee proxy 24% = 50% of yes votes; 763M veHNT
- [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]] — proposal text: "emit the full allocation... to the single Service Provider Nova Labs"
- [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]] — 96.72% pass; Nova Labs proxy 26% + ferebee proxy 31% = 57% of total vote; 902M veHNT; ferebee veHNT +55.5% in 6 months
- [[Helium HIP-53 Vote Results — Helium Vote - 2022-07-25]] — MOBILE subDAO + $0.50/GB rate; Joey Padden et al. authors (not Nova Labs)
- [[Helium HIP-138 Vote Results — Helium Vote - 2024-11-22]] — HNT consolidation; anonymous wallet 15% top voter (no labeled proxies in top 12)
- [[State of Helium Q4 2025 — Messari]] — confirms no HIP superseded HIP-143 as of Q4 2025; HIP-143 auto-renewal April 2026; $124.77/day IoT vs $56,635/day Mobile revenue split
- [[Helium Halving 2025 — Helium Blog - 2025-07-24]] — proxy-delegation guidance, halving mechanics
- [[Helium Hotspot Earnings 2025 — AMBCrypto]] — $4–$8/month earnings at $249–$949 hardware costs; 10–20 year payback math
- [[Helium Operator Economics — Bytetree - 2024-03]] — payback period framing
- Author's prior pieces: [[Beyond "Crypto Week"]] (the framework piece), [[Everyone's Farming DePIN Tokens. Almost Nobody's Checking If the Hardware Exists.]] (the prior Datagram-positive framing now being corrected), [[Atlanta Passed a Sanctuary Resolution. The Vendor Contract Didn't.]] (the procurement-workaround precedent piece)

## What It Leaves Open

- **The federalism question**: McDonald's franchisees are protected by the FTC Franchise Rule (16 CFR Part 436). The piece names the analogy but does not propose a specific regulatory framework or jurisdiction. Whether U.S. state attorneys general can apply existing franchise-disclosure law to DePIN protocols is the next-step legal question.
- **The ferebee identity question**: The piece names the Nova Labs + ferebee proxy concentration as the operative pattern but does not resolve whether ferebee is a distinct entity, an aligned investor coordinated with Nova Labs, or a corporate shell. The [[Nova Labs]] entity page flags this as an open question; the article does not engage it directly.
- **The HIP-148 authorship trail (`madninja`)**: The October 2025 HIP authored by GitHub user `madninja` is not named in the article — the proxy-vote facts carry the argument without needing to resolve the authorship attribution. Worth following up in a future synthesis on the franchise architecture's author-chain.
- **The transferability question**: The closing line ("the next operator who reads a DePIN whitepaper this month does the math before the hardware ships") gestures toward the broader DePIN sector but does not work through specific protocols. [[Render Network]], [[io.net]], [[Filecoin]], [[Hivemapper Foundation]] are all candidates for the same audit; none are named.
- **The 2026 IoT-vs-Mobile revenue gap mechanism**: The $124.77/day IoT vs $56,635/day Mobile revenue figure carries enormous analytical weight — it's the "one half of the network is the revenue, the other half is the hardware that gives the project something to point at" framing. The piece does not develop *why* IoT revenue stayed so low (limited LoRaWAN traffic? limited enterprise customer adoption? structural underpricing?). That is a next-piece angle.

## Connections to the Research Wiki

- [[Helium Network]] — the protocol; this article is the popular-form synthesis of the entity page's franchise-architecture findings
- [[Nova Labs]] — the corporate counterparty; this article is the first newsletter use of the entity page
- [[Helium HIP-143 and the DePIN Franchise Architecture]] — the prior synthesis page; this article is its popular-form distillation
- [[Franchise vs. Business]] — the concept page; this article is the worked example named in the concept page's "Why It Matters" section
- [[Proxy Concentration Audit]] — the analytical method; this article applies the audit to HIP-143 and HIP-148 in publication form
- [[Auto-Renewal by Inaction]] — the design-pattern concept; this article is the worked example
- [[Chokepoint Control]] — the master frame applied to the DePIN-protocol layer
- [[Datagram Network]] / [[Datagram]] entity page — the self-correction reference (closed-source, alpha-testnet stats author rationalized)
- [[Atlanta Passed a Sanctuary Resolution. The Vendor Contract Didn't.]] — the prior procurement-workaround case the closer links to
- [[Beyond "Crypto Week"]] — the framework piece the wiki/articles/ entry already documents
- [[Everyone's Farming DePIN Tokens. Almost Nobody's Checking If the Hardware Exists.]] — the prior piece whose Datagram-positive framing this article corrects
- [[I Had the Wrong Bottom of the Stack]] (backstage, paid) — adjacent self-correction backstage piece (different topic, same analytical genre of named-author-correction)

## Voice and Craft Notes

- **The McDonald's analogy carries the four-component spec**: The single most accessible move in the piece is collapsing the four-component disclosure spec into the FDD comparison. "Federal law requires it" does the comparative work in five words. The wiki's CLAUDE.md voice rule ("prefer mechanism over shorthand") shows up here in its strongest form — the mechanism is the regulatory regime, not a label.
- **The self-correction is the structural payoff**: The "audit caught Helium, missed my project" reframe is the piece's emotional and analytical center. It does two things at once: (a) demonstrates the limits of the four-component standard the piece just spent four sections building (intellectual honesty), and (b) re-anchors the author's authority on DePIN by way of named failure (the credibility move from [[Institutional Gaslighting]]'s structural section). The combination is what makes the piece land as analysis rather than rant.
- **The opener is the franchise-vs-business inversion**: "You Own the Hotspot. Nova Labs Owns What It Earns." is the title and the opening paragraph's compressed argument. The title doubles as the article's first sentence's setup. The piece earns the title by section 2's vote-concentration evidence rather than by rhetorical assertion.
- **The published date (2026-05-21) is one day earlier than the wiki's working assumption** (Friday May 22 flagship slot). The wiki overview and prior log entries treated this as the May 22 flagship. The published date is Thursday May 21 — flag for future content-calendar tracking.
