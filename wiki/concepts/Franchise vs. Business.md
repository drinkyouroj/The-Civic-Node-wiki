---
title: "Franchise vs. Business"
type: concept
tags: [depin, governance, operator-economics, franchise, dao, chokepoint, monetary-policy]
created: 2026-05-21
updated: 2026-05-21
sources: 14
---

## Definition

The franchise-vs-business test is an analytical move for evaluating any system in which individual operators deploy real-world capital into a shared network and earn through tokens, rewards, or rate-card payouts. The question it answers is: **who holds the pricing authority over the revenue the operators are paid out of, and how is that authority changed?**

- A **business** is a structure in which operators retain the rights that determine what their deployed capital earns. Those rights include the pricing of the service the network sells, the rules that distribute revenue to operators, and the ability to change either without unilateral counterparty consent. Operators share in upside because they hold the levers that produce it.
- A **franchise** is a structure in which a corporate counterparty (or a tightly-coordinated bloc inside a DAO that performs the corporate-counterparty role) holds the pricing authority. The hardware is the operator's. The token may be the operator's. The pricing rules that determine what the hardware earns are not. Operators pay capex and ongoing costs and receive whatever the franchisor's pricing-and-rewards rule leaves on the table after the franchisor's economics are satisfied.

The test is structural, not rhetorical. It does not depend on how the project markets itself. A project that calls itself a "decentralized network of operator-owners" can be a franchise; a project that calls itself a "platform" can be a business. The test is whether operators hold the pricing-and-revenue-distribution authority, or someone else does.

## Why It Matters for the Newsletter

**DePIN evaluation becomes legible.** Without this test, DePIN coverage tends to collapse into either uncritical hype (token incentives align everyone!) or uncritical dismissal (it's all rug-pulls). The franchise-vs-business test gives a structural rubric that survives both framings: the project's marketing language doesn't change the answer; the proxy voting record does.

**The "deploy first, find out what you bought later" pattern is named.** The franchise architecture is partly temporal: operators deploy capital, then the governance documents that define what they bought are written, voted on, and re-voted. The right evidence base for any DePIN operator-due-diligence is "the docs you signed before deploying," not the docs the project currently points at. The franchise test is what makes that timing visible.

**Monetary policy framing.** The franchise architecture is a wage-share story dressed up in DAO language. The operator who deploys a hotspot is in roughly the position of a franchisee of a fast-food chain. The disclosure obligations that protect franchisees under federal franchise law (FTC's Franchise Rule, 16 CFR Part 436) do not attach to token-incentivized networks even when the structural relationship is identical. The franchise-vs-business test makes that absence load-bearing.

**Adjacent applications outside DePIN.** The same test applies to gig-economy platforms (do drivers hold pricing authority?), creator-economy platforms (does the creator hold pricing authority?), and increasingly to AI-data-center deals where landowner-operators are recruited to host equipment under terms they did not draft. The test transfers; the worked examples differ.

## Evidence & Examples

### The Helium worked example (cleanest documented case)

The reference case is documented in [[Helium HIP-143 and the DePIN Franchise Architecture]]. The structural sequence:

1. **Operators deployed capital first.** Hotspot hardware ranges from $249 (basic indoor IoT) to $949 (pro outdoor). Operators built out ~385,000 IoT hotspots and ~121,000 Mobile hotspots before the governance changes that defined what they bought were finalized. [[Helium Operator Economics — Bytetree - 2024-03]]
2. **Governance changes redefined the rewards retroactively.** HIP-82 capped rewardable data per subscriber (defensibly). HIP-138 consolidated subDAO tokens into HNT. HIP-143 authorized [[Nova Labs]] to set the price carriers pay for hotspot data without governance involvement. HIP-148 reallocated 20% of HNT emissions previously earmarked for Mobile Mapping rewards — operators who'd been earning HNT for mapping data were moved to gift-card credits (Cloud Points). Each step had a local justification. Together they shifted the operator's position from "share in network upside" to "earn whatever the pricing-authority holder leaves on the table." [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]], [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]
3. **The pricing-authority counterparty held the governance proxy.** Nova Labs proxy 26% + ferebee proxy (HIP-143 co-author) 24% = 50% of yes votes on HIP-143. Nova Labs proxy 26% + ferebee proxy 31% = 57% of total vote on HIP-148. The entity authorizing itself cast the largest single bloc each time. The concentration is documented on-chain — not inferred. [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]], [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
4. **The structural test confirmed at the operator level.** Hotspots that were marketed as earning "hundreds of dollars a month" in 2021 earned $3–$45/month by August 2025, with most operators clustered at $4–$8. Payback on the indoor box: 2.5–5 years; on the outdoor setup: 10–20. [[Helium Hotspot Earnings 2025 — AMBCrypto]] Operators bear the capex; the corporate counterparty holds the pricing authority over what the capex earns. The test resolves: franchise.

### The pre-concentration baseline (2022–2024)

The franchise architecture became visible in the Helium vote receipts between November 2024 (HIP-138) and April 2025 (HIP-143). On HIP-138 (closed November 22, 2024), the top voter was an anonymous wallet at 15%, with no labeled proxies in the top 12. On HIP-143 (April 3, 2025), Nova Labs and ferebee appear as the top two labeled proxies at 50% of yes votes. The inflection is recent and documentable. [[Helium HIP-138 Vote Results — Helium Vote - 2024-11-22]]

The pre-concentration period is meaningful because it shows the structure isn't an inherent property of token-incentivized networks. The franchise architecture got installed in the Helium DAO at a specific moment, through specific votes, with specific proxy concentrations. Other DePIN projects may or may not have undergone the same installation. The test is empirical, not categorical.

### The Datagram correction (fraud-as-franchise)

Two earlier newsletter pieces ([[DePIN More Than Hype]], [[Everyone's Farming DePIN Tokens. Almost Nobody's Checking If the Hardware Exists]]) cited Datagram as a DePIN counter-example that "did it differently." Datagram turned out to be a rug; the project collapsed. The honest correction: the operator due-diligence checklist that worked for Helium (who holds pricing? has governance changed rewards mid-deployment?) was not enough to catch Datagram, which was outright fraud. The structural problems (franchise architecture) and the fraud problems (nothing-to-build) share an architecture: both require an operator who deploys capital before the documents governing what they bought are written. The franchise test catches one; it does not catch the other.

## Tensions & Counterarguments

- **"All capital deployment involves trusting a counterparty."** True. The franchise test is not about whether to trust; it's about which specific authority the counterparty holds and whether the operator has any procedural recourse. The test is binary on the pricing-authority question; the trust question is downstream of the answer.
- **"DAO governance is the recourse."** DAO governance is recourse on paper. The proxy-concentration evidence on HIP-143 and HIP-148 shows that recourse is structurally captured when the proposing entity holds the largest voting bloc. The [[Proxy Concentration Audit]] is the procedural test that surfaces this; the franchise test is what the audit serves.
- **"Pricing authority is operationally necessary."** The HIP-143 proposal text argues that confidentiality of carrier deals is structurally necessary for negotiating posture. This is plausible. The franchise test is not whether pricing authority should exist somewhere; it's about whether the operators who bear the cost have any procedural rights when that authority is exercised. The two questions are separable.
- **"Operators chose to participate."** The franchise architecture is partly temporal — operators deploy capital before the documents that define what they bought are finalized. Consent at deployment is consent to a moving target. The objection to the franchise architecture is not that consent didn't happen; it's that the documents defining the consent were rewritten retroactively through governance the operators were recommended to delegate to proxies.
- **"Some franchise-shaped relationships are net-positive for operators."** Possibly. Federal franchise law (FTC Franchise Rule, 16 CFR Part 436) exists because franchise-shaped relationships have a long history of asymmetric outcomes that warrant disclosure. The argument is for the disclosure regime to extend to token-incentivized networks, not against the network shape itself.

## Related Concepts

- [[Proxy Concentration Audit]] — the procedural test that surfaces franchise architectures from on-chain vote receipts
- [[Auto-Renewal by Inaction]] — the default-rule design pattern that lets franchise authority re-arm without operator participation
- [[Chokepoint Control]] — the franchise architecture is a chokepoint at the protocol layer; pricing authority is the chokepoint the franchisor holds
- [[DePIN]] — the broader category the test lives inside
- [[Operator View of Crypto Regulation]] — the regulatory-asymmetry framing that connects franchise architecture to franchise-disclosure law

## Key Sources

- [[Helium HIP-143 and the DePIN Franchise Architecture]] — the synthesis page that names this concept
- [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]] — the proposal text where the franchise architecture is documented in the proposing entity's own language
- [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]] — the on-chain receipt of the proxy concentration that passed it
- [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]] — the second-instance proof of the pattern; HNT-to-gift-cards substitution makes the franchise structure unambiguous
- [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]] — proxy concentration at 57% (more concentrated than HIP-143)
- [[Helium HIP-138 Vote Results — Helium Vote - 2024-11-22]] — pre-concentration baseline (no labeled proxies in top 12)
- [[State of Helium Q4 2025 — Messari]] — network revenue asymmetry that frames the franchise gap ($56,635/day Mobile-side; $124.77/day IoT-side)
- [[Helium Hotspot Earnings 2025 — AMBCrypto]] — operator-side economics under the franchise architecture
- [[Helium Operator Economics — Bytetree - 2024-03]] — hardware costs and payback periods that quantify the operator's stake
