# Article Outline: The Helium Franchise Architecture

**Status:** Fresh outline, drafted 2026-05-18 from the synthesis at `wiki/syntheses/Helium HIP-143 and the DePIN Franchise Architecture.md`. Treats prior Helium outline and draft work as superseded.

**Publish target:** Friday, May 22, 2026 (4 days from outline date).

**Series position:** Standalone piece following "12 Gigawatts Were Announced. 4 Are Being Built." (merged 2026-05-16). Picks up the broader thread of "who built the thing vs. who controls what it earns" but applies it to a DePIN case rather than a grid case.

**Trigger:** Named Hypocrisy — the proposing entity and one of its co-authors cast 50% of the yes votes for the proposal authorizing the proposing entity's pricing authority. The trigger lands when the reader sees the vote breakdown stated plainly with no editorializing on top of it. The piece earns its dryness; it does not perform it.

**Template:** System Audit (Problem → Analysis → Solutions)

**Timeliness anchor (two beats):**
1. **April 2026 auto-renewal.** HIP-143 carried a 1-year delegation provision. As of the most recent Messari sector report, no superseding HIP has been passed. The structure auto-renewed by inaction around April 2026, weeks before this piece publishes. The vote that handed Nova Labs unilateral pricing authority is now in its second year, without operator participation having been required to extend it.
2. **The 12 Gigawatts pairing.** Last issue named the gap between announced grid capacity and built grid capacity. This issue names a parallel gap inside a DePIN network: the gap between what operators were marketed and what governance documents actually set. Different domains, related move (audit what's announced against what's contractually true).

**Target length:** 1,500–1,600 words

---

## Section 1: The Glitch (~400 words)
*Tone: sardonic precision. Name what's broken without rage. Specific numbers, specific dates.*

- **Open with the auto-renewal beat.** A vote happened in April 2025 that handed one company unilateral pricing authority over a 385,000-hotspot wireless network. The vote had a 1-year sunset. A year passed. The sunset arrived in April 2026. No replacement vote was held. The pricing authority renewed itself by silence. That is the spark.
- Pivot to the operator economics that make this matter. A basic indoor Helium IoT hotspot costs $249. A pro outdoor setup runs to $949. As of August 2025, after the network's halving (the algorithmic cut that reduced new HNT emissions from 15 million a year to 7.5 million), a well-placed urban hotspot earns between $3 and $45 a month, with most operators clustered in the $4–$8 range. The indoor box pays back in 31–62 months at those numbers. The outdoor setup pays back in 10–20 years. Sources: [[Helium Hotspot Earnings 2025 — AMBCrypto]], [[Helium Operator Economics — Bytetree - 2024-03]].
- **Land the analytical move as parallel positive statements (not as a reframe — see voice rule § 3F):** Helium hotspot operators bought a franchise. They were sold a business. The hardware they paid for is theirs. The pricing authority that determines what their hardware earns belongs to Nova Labs.
- Gloss the audience-load vocabulary on first use: DePIN (decentralized physical infrastructure networks — tokenized projects where independent operators deploy hardware that earns rewards), HIP (Helium Improvement Proposal, the network's governance proposal format), PoC (Proof of Coverage, the algorithmic reward for hotspots that prove they cover a geographic area).
- Set up the audit the rest of the piece runs. There are three structural questions an operator can ask about any DePIN project, and Helium answers each one in a way that explains the earnings collapse.
- End on the question Marcus is now positioned to ask: who actually held the pricing authority, and how was that authority granted?
- Sources for this section: [[Helium Hotspot Earnings 2025 — AMBCrypto]], [[Helium Operator Economics — Bytetree - 2024-03]], [[Helium Halving 2025 — Helium Blog - 2025-07-24]], [[State of Helium Q4 2025 — Messari]]

---

## Section 2: The Source Code (~500 words)
*Tone: building analytical weight. Charitable reading first, then audit. Densest section — this is where operational credibility is earned.*

- **Charitable reading of the rule changes.** The reward structure that defined what operators earned was changed through a sequence of defensible-sounding proposals run over three years. HIP-82 capped how much data could earn rewards: $0.50 per gigabyte, up to whatever the subscriber's plan cost divided by $0.50 allows, zero above that. The argument: caps prevent operators from earning indefinitely on subscribers who already maxed out their plan. HIP-138 consolidated the IOT and MOBILE subnetwork tokens into HNT in January 2025. The argument: token consolidation simplified accounting. The August 2025 halving cut emissions and halved PoC rewards in the same step. The argument: emission discipline is what crypto networks do. Each proposal had its own justification. Present them fairly. [[Helium HNT Tokenomics — Tokenomist]], [[Helium Halving 2025 — Helium Blog - 2025-07-24]]
- **The audit.** Run the rule changes for three years and the rewards shifted from coverage to data traffic, then halved what could be earned on the coverage that remained. An operator who built out a rural hex in 2022 created a real public good for the network's IoT ambitions. They were later told it was not the public good that pays. The revenue numbers confirm the picture. The IoT side of the network generates $124.77 a day in real Data Credit burns across the entire 385,000-hotspot deployed base, about $45,000 a year. The mobile side, which routes carrier offload from T-Mobile and AT&T, generates $56,635 a day. One half of the network is the revenue. The other half is the hardware that gives the project something to point at. [[State of Helium Q4 2025 — Messari]], [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]]
- **HIP-143 — the pricing authority handoff.** Voted April 3, 2025. The proposal authorized Nova Labs (the company that operates Helium Mobile and negotiates the carrier offload deals) to set carrier pricing without further Helium governance involvement. The proposal text states the goal in its own words: *"If Nova Labs would be able to move quickly... without involving Helium governance, the authors of this HIP anticipate that the total Data Transfer of the Helium network will rise."* The argument is structurally defensible. Confidential commercial negotiations do not belong on-chain. The carrier wants its rate sheet private. Nova Labs needs negotiating speed. Concede all of it. [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]]
- **The vote breakdown — load-bearing for the trigger.** The proposal passed 90.53% to 9.46% on 763 million veHNT (vote-escrowed HNT, the staked governance token) against a 100 million quorum. The Nova Labs proxy controlled 26.00% of the vote. The ferebee proxy, listed as a co-author of HIP-143, controlled 24.00%. The proposing entity and one of its co-authors together carried 50% of the yes votes for the proposal authorizing the proposing entity's pricing authority. The largest "against" vote came from an anonymous proxy at 8%. State the numbers. The reader does the math. [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- **Proxy concentration as policy, not accident.** The Helium Foundation's own halving blog post (July 2025) recommends operators "set a proxy as a backup to ensure you don't miss out on rewards." The 50-percent concentration that approved HIP-143 is how the system was designed to work. The Foundation publishes guidance that normalizes delegating voting power to large proxies. The vote outcome follows the policy. [[Helium Halving 2025 — Helium Blog - 2025-07-24]]
- **Return to the auto-renewal.** HIP-143's 1-year sunset arrived in April 2026. No superseding HIP was filed. The pricing authority extended itself. Default-rule design is governance design; the structures that survive are the ones that survive operator inattention.
- Sources for this section: [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]], [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]], [[Helium Halving 2025 — Helium Blog - 2025-07-24]], [[State of Helium Q4 2025 — Messari]], [[Helium HNT Tokenomics — Tokenomist]], [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]]

---

## Section 3: The Upgrade (~400 words)
*Tone: measured. Acknowledge trade-offs honestly. No cheerleading and no "imagine if" abstractions.*

- **Start by conceding what's real.** Enterprise sales do require confidentiality. Carrier offload pricing is a competitive variable for T-Mobile and for AT&T. Putting that on-chain in real time would damage both negotiating positions. Nova Labs's structural argument for pricing authority delegation is not invented. It describes a real commercial constraint.
- **The audit's purpose, stated plainly.** The question is not whether DePIN operators should hold pricing authority over commercial contracts they don't negotiate. They probably can't. The question is what an operator needs to know, in writing, before they pay $249 to $949 for a piece of hardware and plug it into someone else's commercial network.
- **A disclosed franchise has four things the Helium operator never received:**
  - A written floor on what triggers a material change to the reward structure, and an operator right to exit at that floor (hardware buyback, migration provision, or refund-of-residual).
  - Aggregate transparency on data-transfer revenue, audited annually, even when individual carrier rate sheets are confidential. The unit economics can stay private. The total revenue split between the operator class and the corporate counterparty cannot.
  - Geographic acknowledgment that rural coverage and urban traffic are different goods. A reward structure that pays both is one product. A reward structure that pays only the dense-urban one is a different product, and the operator deploying in a rural hex needs to know which product they bought.
  - Sunset provisions that require an active re-vote, not auto-renewal by silence. The Helium structure is fixable here. Default rules can be rewritten.
- **Name the honest version of the deal.** "You're buying a revenue-share position, priced by a centralized negotiator, on infrastructure you own and operate. The negotiator's commercial terms are confidential. Your earnings are a function of their negotiations and the network's data traffic, neither of which you control." That sentence is a real product. It just needs to be the sentence in the marketing, not the sentence the operator works out three years later from a Messari sector report.
- **Acknowledge the limit.** None of this catches outright fraud. A project can issue all four disclosures and still be hollow. The audit is the floor, not the ceiling. Section 4 carries the rest.

---

## Section 4: My Debug (~250 words)
*Tone: first person. Direct. The personal anecdote serves the argument; it doesn't replace it.*

- **The frame.** I ran more than twelve Datagram nodes for several weeks. I worked on the project for about seven months without pay. The project collapsed. Earlier pieces I published on DePIN positioned Datagram as the legitimate counter-example, the project doing it differently. That framing was wrong, and I should have caught it earlier. I'm correcting it here.
- **What the audit catches and what it doesn't.** The four-part disclosure standard I just laid out would have caught Helium in 2021. It would not have caught Datagram. A project can publish exit provisions, revenue transparency, geographic acknowledgment, and re-vote sunsets, and still have no business underneath any of it. The structural problem and the fraud problem share an architecture. Both require an operator who deploys capital before the documents that govern what they bought are written.
- **The conclusion that operator due diligence has to carry.** The audit is necessary. It is not sufficient. A rational DePIN operator in 2026 runs the four checks and still treats the deployment itself as a separate decision. The right move, given the stack of failure modes, might be to not deploy first.
- **Closing line — named actor, active verb (per voice rule § 3J).** Candidate: "The next operator who reads a DePIN whitepaper this month does the math before the hardware ships, not after."

---

## Opener Strategy

**Technique:** Analogy That Narrows. Open on the auto-renewal beat (specific, dated, news-pegged), then narrow to the operator and the hardware.

**Proposed prose for the draft (subject to draft-time revision):**

> A vote in April 2025 handed one company unilateral pricing authority over a 385,000-hotspot wireless network. The vote had a 1-year sunset. A year passed. The sunset arrived in April 2026, a few weeks before this piece publishes. No replacement vote was held. The pricing authority renewed itself by silence.
>
> The operators of those 385,000 hotspots paid for the hardware out of their own pockets. A basic indoor box costs $249. A pro outdoor setup runs $949. As of last August, the typical urban hotspot earned $4 to $8 a month. The indoor unit pays back in three to five years. The outdoor one pays back in ten to twenty.
>
> Helium hotspot operators bought a franchise. They were sold a business. The hardware they paid for is theirs. The pricing authority that determines what their hardware earns is not.

**Voice checks applied to the opener:**
- Zero em dashes. Commas, periods, parentheses only.
- The franchise/business move uses parallel positive statements ("bought a franchise / were sold a business"), not the banned negative parallelism pattern ("didn't buy a business, bought a franchise").
- DePIN, HIP, veHNT, PoC, LoRaWAN all need inline gloss the first time the draft uses them. The opener does not require any of them; gloss work shifts to Section 1.
- Mechanism over shorthand: the opener names "pricing authority" as a specific mechanism (the right to set what carriers pay per gigabyte) rather than waving at "control" or "ownership" abstractly.

**Thesis lands by paragraph 3.** The reader who stops reading at paragraph 3 has the argument. The next 1,400 words are evidence.

---

## Close Strategy

- **Callback:** The franchise analogy returns at the end of Section 3 or top of Section 4. The natural callback line: a franchise owner reads the franchise disclosure document before signing. The Helium operator received the equivalent document as a sequence of governance proposals written after the hardware was already plugged in.
- **Reader leaves pondering:** Not whether DePIN is dead. Whether the deployment timing itself is the operator's exposure. The piece is most valuable as a thing the reader does next: pulls up the governance forum of whatever DePIN project they currently run hardware for, and runs the three structural checks (pricing authority, proxy concentration, sunset provisions) before paying the next electricity bill.
- **Closing-line discipline (§ 3J):** The last sentence names a person doing a thing. Candidate above: "The next operator who reads a DePIN whitepaper this month does the math before the hardware ships, not after." Named actor (the next operator), active verb (does the math, ships), specific temporal placement (this month). No abstract noun phrase summarizing the piece's structural concept.

---

## Personal Reflection

- **Anchor:** Justin ran 12+ Datagram nodes for several weeks. Worked on the project for approximately 7 months without pay. The project rugged.
- **What the anecdote serves:** Operational credibility for the operator-economics critique. A reader who has run DePIN hardware reads "I deployed and got it wrong, on a project with better marketing than Helium's" as evidence the writer paid the tuition. The vulnerability earns the right to lay out the audit.
- **What to keep out:** No re-litigation of Datagram's specifics beyond the bare facts. The Datagram material is one paragraph, doing one job: marking the limit of the audit. Anything longer becomes memoir and weakens the structural argument.
- **The prior-piece correction Justin owes the reader:** Earlier DePIN pieces in the newsletter cited Datagram as the legitimate counter-example. That framing is now wrong. Own it in the personal reflection, not in a footnote. Per [[memory: project_datagram_rug]]: never repeat the legitimate-counter-example framing.

---

## Source Set (all in wiki, synthesis-aligned)

- [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]] — the on-chain vote breakdown (Nova Labs proxy 26%, ferebee proxy 24%, 90.53/9.46 final tally, 763M veHNT total)
- [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]] — the proposal text including the "move quickly without involving Helium governance" quote
- [[State of Helium Q4 2025 — Messari]] — $124.77/day IoT revenue, $56,635/day mobile revenue, 385,000 hotspots, no superseding HIP confirms April 2026 auto-renewal
- [[Helium Hotspot Earnings 2025 — AMBCrypto]] — $3–$45/month earnings range, $4–$8 common
- [[Helium Operator Economics — Bytetree - 2024-03]] — hardware costs ($249 indoor, $949 outdoor) and payback periods (2.5–5 years indoor, 10–20 outdoor)
- [[Helium Halving 2025 — Helium Blog - 2025-07-24]] — emissions cut, PoC reward halving, the Foundation's own proxy-delegation recommendation
- [[Helium HNT Tokenomics — Tokenomist]] — HIP-138 token consolidation context
- [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]] — mobile-side revenue context

**Synthesis basis:** [[Helium HIP-143 and the DePIN Franchise Architecture]] (filed 2026-05-18) is the analytical scaffolding. The synthesis names four transferable moves (franchise-vs-business, proxy-concentration audit, auto-renewal-by-inaction, deploy-first-find-out-later); this outline uses each one as a section anchor rather than as a separate framework.

---

## Source Gaps

- **None for the piece as scoped.** All load-bearing facts come from sources already in the wiki.
- **One open question deliberately left open in the prose.** The exact ownership and operating relationship between Nova Labs and ferebee. Public sources document each as a Helium-ecosystem actor. The coordination signal in the HIP-143 vote suggests a closer relationship than the public framing implies. The piece references "the proposing entity and one of its co-authors" without claiming a single corporate identity behind both proxies. Honest framing; the synthesis's Follow-up Question #4 flags this as a documentary gap.

**Status:** Ready to draft. Next step: `tcn-headline` for title alternatives (the locked headline from the prior outline is discarded along with the rest of that work), then `tcn-draft`.

---

## Working title candidates (for tcn-headline, not locked)

1. **The Helium Vote Renewed Itself in April. Nobody Voted.**
2. **You Own the Hotspot. Nova Labs Owns What It Earns.**
3. **Half the Yes Votes Belonged to the Entity the Vote Authorized.**
4. **Helium Operators Built the Network. The Pricing Authority Lives Somewhere Else.**
5. **The Franchise Disclosure Document Arrives After You've Already Bought the Hardware.**

The tcn-headline step will refine. Current preference (subject to that step): a two-clause structure that puts the operator on one side and the corporate counterparty on the other, naming a specific mechanism rather than waving at "control."
