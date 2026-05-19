# Article Outline (v2): The Helium Franchise Architecture

**Status:** Revision of v1 (`01-outline.md`, drafted 2026-05-18, committed in `ab350ec`). The structural questions raised by the HIP-148 primary-source ingest (commit `08b936a`, 2026-05-19) are resolved below in the Revision Notes section.

**Publish target:** Friday, 2026-05-22 (3 days from this revision).
**Series position:** Standalone piece following [[12 Gigawatts Were Announced. 4 Are Being Built.]] (merged 2026-05-16). Same recurring analytical move (audit what was promised against what was contractually true), different domain (DePIN governance instead of grid capacity).
**Template:** System Audit (Problem → Analysis → Solutions) — unchanged from v1.
**Trigger:** Named Hypocrisy. The proposing entity and one of its co-authors cast 57% of the total vote on a proposal consolidating 24% of Mobile network emissions to the proposing entity itself, while the only named voter who opposed it held 1.00% of the vote.
**Target length:** 1,500–1,600 words.

---

## Revision Notes (v1 → v2)

The four structural questions the HIP-148 ingest raised, with the call for each one and the reasoning.

### Q1: Opener — auto-renewal vs Keith Rettig

**Call:** Keep the auto-renewal opener. Move Keith Rettig to Section 2 as the named-human anchor for the HIP-148 vote breakdown.

**Reasoning:** The synthesis itself uses the April 2026 auto-renewal as its primary anchor and doesn't mention Keith Rettig (the synthesis predates the screenshot ingest). The System Audit template's Section 1 ("The Glitch") asks the writer to "open with the most concrete manifestation — a specific event, number, or quote that makes the problem tangible." The auto-renewal *is* the structural finding (silence-as-design); making it the opener lets the structural argument lead. Keith Rettig is a character who works best as a Section 2 anchor — a named human carrying the HIP-148 vote breakdown — rather than as a thesis-level figure. Opening on Keith Rettig would tilt the piece from "audit a system" toward "profile a dissenter," which the System Audit template specifically pushes against. The auto-renewal opener also has a stronger news peg: April 2026 is weeks before publish; the HIP-148 vote was October 2025 (six months stale by publish date).

### Q2: HIP-148 — sub-beat or progression spine?

**Call:** Restructure Section 2 around the HIP-143 → HIP-148 progression. Both votes get parallel beat-level treatment.

**Reasoning:** The synthesis treats HIP-143 as "the worked example" of a transferable analytical move (the proxy-concentration audit). With HIP-148 now sourced at primary level, the audit move has been applied twice — and the second application is *more concentrated* than the first (57% vs 50% of total vote). One vote is an anecdote; two votes showing the same pattern with worsening concentration is a structure. Treating HIP-143 and HIP-148 as parallel beats inside Section 2 lets the section's analytical weight come from the *progression* itself rather than from a single vote's anomaly. The article's working title is "The Franchise Architecture" — a structure, not an event — and Section 2 needs to deliver structural evidence. Two votes do that; one vote plus a footnote doesn't.

### Q3: veHNT-accumulation as its own beat?

**Call:** Fold the trajectory finding into Section 2 as its closing beat (beat 5 of the restructured 6-beat section), not a separate section.

**Reasoning:** The +55.5% veHNT growth for ferebee in 6 months is structurally tied to the HIP-143 → HIP-148 progression — it explains why the pattern intensified between the two votes. Separating it into its own section would force the reader to track a third structural move on top of franchise architecture (Section 1) and the two-vote progression (Section 2). At 1,500–1,600 words with four sections already, there isn't room for a fifth. The trajectory finding works best as Section 2's capstone: "Section 2 showed the current state — the trajectory is worse." This sets up Section 3's "what disclosure would have caught" argument with appropriate urgency.

### Q4: Closer

**Call:** Keep v1's closer: "The next operator who reads a DePIN whitepaper this month does the math before the hardware ships, not after."

**Reasoning:** The v1 closer is a clean named-actor sentence per voice rule § 3J. It points the reader at action (do the math before the hardware ships) rather than restating the piece's structural conclusions. With the trajectory beat now in Section 2, the reader arrives at the closer already understanding that the franchise architecture is intensifying — the closer's "before the hardware ships" temporal framing lands harder because of it, without needing to explicitly restate the trajectory. Adding a trajectory-flavored closing clause would be redundant with the Section 2 capstone and would weaken the closer's tight named-actor structure.

---

## Section 1: The Glitch — The Vote That Renewed Itself in April (~400 words)

*Tone: sardonic precision. Name what's broken without rage. Specific numbers, specific dates. Subheadline candidate above; tcn-headline step finalizes.*

- **Open with the auto-renewal beat.** A vote happened in April 2025 that handed one company unilateral pricing authority over a 385,000-hotspot wireless network. The vote had a 1-year sunset. A year passed. The sunset arrived in April 2026, a few weeks before this piece publishes. No replacement vote was held. The pricing authority renewed itself by silence.
- Pivot to the operator economics that make this matter. A basic indoor Helium IoT hotspot costs $249. A pro outdoor setup runs to $949. As of August 2025, after the network's halving (the algorithmic cut that reduced new HNT emissions from 15 million a year to 7.5 million), a well-placed urban hotspot earns between $3 and $45 a month, with most operators clustered in the $4–$8 range. The indoor box pays back in 31–62 months at those numbers. The outdoor setup pays back in 10–20 years. Sources: [[Helium Hotspot Earnings 2025 — AMBCrypto]], [[Helium Operator Economics — Bytetree - 2024-03]].
- **Land the analytical move as parallel positive statements (per voice rule § 3F):** Helium hotspot operators bought a franchise. They were sold a business. The hardware they paid for is theirs. The pricing authority that determines what their hardware earns belongs to Nova Labs.
- Gloss the audience-load vocabulary on first use: DePIN (decentralized physical infrastructure networks — tokenized projects where independent operators deploy hardware that earns rewards), HIP (Helium Improvement Proposal, the network's governance proposal format), PoC (Proof of Coverage, the algorithmic reward for hotspots that prove they cover a geographic area).
- Set up the audit Section 2 runs. The franchise architecture isn't a single event. It's a sequence of governance changes that the reader can walk through, vote by vote, until the picture is the picture. Section 2 walks two of those votes — eighteen months apart, same proposing entity, the second more concentrated than the first.
- End on the question Marcus is now positioned to ask: who actually held the pricing authority across those two votes, and how was that authority granted?
- Sources for this section: [[Helium Hotspot Earnings 2025 — AMBCrypto]], [[Helium Operator Economics — Bytetree - 2024-03]], [[Helium Halving 2025 — Helium Blog - 2025-07-24]], [[State of Helium Q4 2025 — Messari]]

**Voice notes for Section 1:**
- The "three structural questions" framing from v1 is removed. The audit framework arrives in Section 3, not Section 1. Section 1 sets up Section 2 (the two-vote progression), not Section 3.
- Vocabulary gloss is unchanged. Cloud Points doesn't appear until Section 2's HIP-148 beat — don't pre-gloss it in Section 1.

---

## Section 2: The Source Code — Two Votes, Eighteen Months, Concentration Up (~550 words)

*Tone: building analytical weight. Charitable reading first, then audit. Densest section — operational credibility is earned here. Subheadline candidate above; tcn-headline step finalizes.*

### Beat 1 — Charitable reading of the earlier rule changes (~80 words)

- The reward structure that defined what operators earned was changed through a sequence of defensible-sounding proposals run over three years. HIP-82 capped how much data could earn rewards: $0.50 per gigabyte, up to whatever the subscriber's plan cost divided by $0.50 allows, zero above that. The argument: caps prevent operators from earning indefinitely on subscribers who already maxed out their plan. HIP-138 consolidated the IOT and MOBILE subnetwork tokens into HNT in January 2025; the argument was simplified accounting. The August 2025 halving cut emissions and halved PoC rewards in the same step; the argument was emission discipline. Each proposal had its own justification. Present them fairly. [[Helium HNT Tokenomics — Tokenomist]], [[Helium Halving 2025 — Helium Blog - 2025-07-24]]

### Beat 2 — The revenue audit (~80 words)

- Run the rule changes for three years and the rewards shifted from coverage to data traffic, then halved what could be earned on the coverage that remained. An operator who built out a rural hex in 2022 created a real public good for the network's IoT ambitions; they were later told it was not the public good that pays. The revenue numbers confirm the picture. The IoT side of the network generates $124.77 a day in real Data Credit burns across the entire 385,000-hotspot deployed base — about $45,000 a year. The mobile side, which routes carrier offload from T-Mobile and AT&T, generates $56,635 a day. One half of the network is the revenue; the other half is the hardware that gives the project something to point at. [[State of Helium Q4 2025 — Messari]], [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]]

### Beat 3 — HIP-143 (April 2025): the pricing-authority handoff (~120 words)

- The proposal authorized Nova Labs (the company that operates Helium Mobile and negotiates the carrier offload deals) to set carrier pricing without further Helium governance involvement. The proposal text states the goal in its own words: *"If Nova Labs would be able to move quickly... without involving Helium governance, the authors of this HIP anticipate that the total Data Transfer of the Helium network will rise."* The argument is structurally defensible. Confidential commercial negotiations don't belong on-chain. The carrier wants its rate sheet private. Nova Labs needs negotiating speed. Concede all of it. [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]]
- **The vote breakdown — load-bearing for the trigger.** The proposal passed 90.53% to 9.46% on 763 million veHNT (vote-escrowed HNT, the staked governance token) against a 100 million quorum. The Nova Labs proxy controlled 26.00% of the vote. The ferebee proxy, listed as a co-author of HIP-143, controlled 24.00%. The proposing entity and one of its co-authors together carried 50% of the yes votes for the proposal authorizing the proposing entity's pricing authority. The largest "against" vote came from an anonymous proxy at 8%. State the numbers. The reader does the math. [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]

### Beat 4 — HIP-148 (October 2025): the substitution (~140 words)

- Eighteen months later. The proposal eliminated the Mobile Mapping rewards category — 20% of HNT emissions that subscribers had been earning by sharing location data from their phones — and redirected those emissions: 10% to the Service Provider Pool, 10% to the Data Transfer Pool. The 4% Oracle Operator allocation got folded in too. The proposal text names the recipient directly: *"To simplify technical implementation, we propose to emit the full allocation available from Service Provider Rewards and Oracle Operator Rewards to the single Service Provider Nova Labs."* The Service Provider Pool, now 24% of Mobile emissions, is emitted directly to Nova Labs. [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]
- **The substitution operators got.** Subscribers who had been earning HNT for sharing mapping data now earn Cloud Points — gift-card credits redeemable for eGift cards or charity donations. A category of subscriber labor previously compensated in a token with a market price is now compensated in gift cards. The proposal's own motivation section concedes that mapping data was "not very useful" because "carrier offload locations are a much higher quality signal." The 20% emissions category that operators had been told to compete for was an experiment Helium concluded had failed; the redirected upside went to Nova Labs. [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]
- **The vote breakdown — the pattern repeated, more concentrated.** The proposal passed 96.72% to 3.27% on 902 million veHNT cast (18% more participation than HIP-143). The ferebee proxy controlled **31.00%** of the vote (up from 24%). The Nova Labs proxy controlled 26.00% (unchanged in percentage; +21% in absolute veHNT). Together: **57% of the total vote**, up from 50% on HIP-143. **Keith Rettig** — the single named voter who opposed it, holding 13.98 million veHNT (1.00%) — was the largest named "Against" vote in the entire breakdown. Every other named proxy in the top 12 voted For. [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]

### Beat 5 — The trajectory beat (~80 words)

- The proxy concentration was 50% in April 2025. It was 57% in October 2025. ferebee's absolute veHNT holdings grew from 183.85 million to 285.92 million in those six months — a 55.5% increase against a network total that grew far less. The proposing-entity proxies are accumulating veHNT faster than the rest of the network. The architecture isn't a static finding; it's a trajectory. By the next consequential HIP, the proxies that control the vote will control more of it.

### Beat 6 — Return to the auto-renewal (~50 words)

- HIP-143's 1-year sunset arrived in April 2026, weeks before this piece publishes. No superseding HIP was filed. The pricing authority extended itself. Default-rule design is governance design; the structures that survive are the ones that survive operator inattention. The Helium Foundation publishes guidance recommending operators set a proxy as a backup so they "don't miss out on rewards" — proxy concentration is policy, not accident. [[Helium Halving 2025 — Helium Blog - 2025-07-24]]

**Sources for this section:**
- [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]]
- [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]] (NEW in v2)
- [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]] (NEW in v2)
- [[Helium Halving 2025 — Helium Blog - 2025-07-24]]
- [[State of Helium Q4 2025 — Messari]]
- [[Helium HNT Tokenomics — Tokenomist]]
- [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]]

**Voice notes for Section 2:**
- Cloud Points gets its inline gloss on first use (Beat 4): "gift-card credits redeemable for eGift cards or charity donations."
- The 50% → 57% comparison should be stated plainly with the raw figures. No reframing language ("not stable; intensifying" is for revision notes, not draft prose).
- Keith Rettig is named, his veHNT is stated, and the comparison to "every other named proxy in the top 12 voted For" is stated. The reader draws the implication.
- The trajectory beat avoids speculation ("by 2027, X percent") and stays on the documented six-month delta.

---

## Section 3: The Upgrade — What Disclosure Would Have Caught (~400 words)

*Tone: measured. Acknowledge trade-offs honestly. No cheerleading and no "imagine if" abstractions. Unchanged from v1; carried forward verbatim in structure with one minor adjustment noted below.*

- **Start by conceding what's real.** Enterprise sales do require confidentiality. Carrier offload pricing is a competitive variable for T-Mobile and for AT&T. Putting that on-chain in real time would damage both negotiating positions. Nova Labs's structural argument for pricing authority delegation is not invented. It describes a real commercial constraint.
- **The audit's purpose, stated plainly.** The question is not whether DePIN operators should hold pricing authority over commercial contracts they don't negotiate. They probably can't. The question is what an operator needs to know, in writing, before they pay $249 to $949 for a piece of hardware and plug it into someone else's commercial network.
- **A disclosed franchise has four things the Helium operator never received:**
  - A written floor on what triggers a material change to the reward structure, and an operator right to exit at that floor (hardware buyback, migration provision, or refund-of-residual). *(HIP-148 case in point: 20% of emissions was reallocated and a subscriber-labor category was substituted for gift cards, with no exit provision available to the operators whose deployment had been priced around the old structure.)*
  - Aggregate transparency on data-transfer revenue, audited annually, even when individual carrier rate sheets are confidential. The unit economics can stay private. The total revenue split between the operator class and the corporate counterparty cannot.
  - Geographic acknowledgment that rural coverage and urban traffic are different goods. A reward structure that pays both is one product. A reward structure that pays only the dense-urban one is a different product, and the operator deploying in a rural hex needs to know which product they bought.
  - Sunset provisions that require an active re-vote, not auto-renewal by silence. The Helium structure is fixable here. Default rules can be rewritten.
- **Name the honest version of the deal.** "You're buying a revenue-share position, priced by a centralized negotiator, on infrastructure you own and operate. The negotiator's commercial terms are confidential. Your earnings are a function of their negotiations and the network's data traffic, neither of which you control." That sentence is a real product. It just needs to be the sentence in the marketing, not the sentence the operator works out three years later from a Messari sector report.
- **Acknowledge the limit.** None of this catches outright fraud. A project can issue all four disclosures and still be hollow. The audit is the floor, not the ceiling. Section 4 carries the rest.

**Adjustment from v1:** the first bullet under the four-part framework gets a parenthetical that connects it to the HIP-148 substitution (the Cloud Points move is a concrete instance of "no operator-class exit provision when a material reward category changes"). The other three bullets are unchanged. The total section length stays at ~400 words.

---

## Section 4: My Debug — When the Audit Misses the Fraud (~250 words)

*Tone: first person. Direct. The personal anecdote serves the argument; it doesn't replace it. Unchanged from v1.*

- **The frame.** I ran more than twelve Datagram nodes for several weeks. I worked on the project for about seven months without pay. The project collapsed. Earlier pieces I published on DePIN positioned Datagram as the legitimate counter-example, the project doing it differently. That framing was wrong, and I should have caught it earlier. I'm correcting it here.
- **What the audit catches and what it doesn't.** The four-part disclosure standard I just laid out would have caught Helium in 2021. It would not have caught Datagram. A project can publish exit provisions, revenue transparency, geographic acknowledgment, and re-vote sunsets, and still have no business underneath any of it. The structural problem and the fraud problem share an architecture. Both require an operator who deploys capital before the documents that govern what they bought are written.
- **The conclusion that operator due diligence has to carry.** The audit is necessary. It is not sufficient. A rational DePIN operator in 2026 runs the four checks and still treats the deployment itself as a separate decision. The right move, given the stack of failure modes, might be to not deploy first.
- **Closing line — named actor, active verb (per voice rule § 3J).** Candidate (unchanged from v1): "The next operator who reads a DePIN whitepaper this month does the math before the hardware ships, not after."

---

## Opener Strategy

**Technique:** Analogy That Narrows. Open on the auto-renewal beat (specific, dated, news-pegged), then narrow to the operator and the hardware. Unchanged from v1.

**Proposed prose for the draft (subject to draft-time revision):**

> A vote in April 2025 handed one company unilateral pricing authority over a 385,000-hotspot wireless network. The vote had a 1-year sunset. A year passed. The sunset arrived in April 2026, a few weeks before this piece publishes. No replacement vote was held. The pricing authority renewed itself by silence.
>
> The operators of those 385,000 hotspots paid for the hardware out of their own pockets. A basic indoor box costs $249. A pro outdoor setup runs $949. As of last August, the typical urban hotspot earned $4 to $8 a month. The indoor unit pays back in three to five years. The outdoor one pays back in ten to twenty.
>
> Helium hotspot operators bought a franchise. They were sold a business. The hardware they paid for is theirs. The pricing authority that determines what their hardware earns is not.

**Voice checks applied to the opener:**
- Zero em dashes. Commas, periods, parentheses only.
- The franchise/business move uses parallel positive statements ("bought a franchise / were sold a business"), not the banned negative parallelism pattern ("didn't buy a business, bought a franchise").
- DePIN, HIP, veHNT, PoC, LoRaWAN all need inline gloss the first time the draft uses them. The opener does not require any of them; gloss work shifts to Section 1. Cloud Points gets its gloss in Section 2 (Beat 4), where it first appears.
- Mechanism over shorthand: the opener names "pricing authority" as a specific mechanism (the right to set what carriers pay per gigabyte) rather than waving at "control" or "ownership" abstractly.

**Thesis lands by paragraph 3.** The reader who stops reading at paragraph 3 has the argument. The next 1,400 words are evidence.

---

## Close Strategy

- **Callback:** The franchise analogy returns at the end of Section 3 or top of Section 4. The natural callback line: a franchise owner reads the franchise disclosure document before signing. The Helium operator received the equivalent document as a sequence of governance proposals written after the hardware was already plugged in.
- **Reader leaves pondering:** Not whether DePIN is dead. Whether the deployment timing itself is the operator's exposure, and whether the architecture they're auditing is *intensifying* (the Section 2 trajectory beat sets this up). The piece is most valuable as a thing the reader does next: pulls up the governance forum of whatever DePIN project they currently run hardware for, and runs the three structural checks (pricing authority, proxy concentration, sunset provisions) on the most recent governance vote before paying the next electricity bill.
- **Closing-line discipline (§ 3J):** The last sentence names a person doing a thing. Candidate (unchanged from v1): "The next operator who reads a DePIN whitepaper this month does the math before the hardware ships, not after." Named actor (the next operator), active verb (does the math, ships), specific temporal placement (this month). No abstract noun phrase summarizing the piece's structural concept.

---

## Personal Reflection

- **Anchor:** Justin ran 12+ Datagram nodes for several weeks. Worked on the project for approximately 7 months without pay. The project rugged.
- **What the anecdote serves:** Operational credibility for the operator-economics critique. A reader who has run DePIN hardware reads "I deployed and got it wrong, on a project with better marketing than Helium's" as evidence the writer paid the tuition. The vulnerability earns the right to lay out the audit.
- **What to keep out:** No re-litigation of Datagram's specifics beyond the bare facts. The Datagram material is one paragraph, doing one job: marking the limit of the audit. Anything longer becomes memoir and weakens the structural argument.
- **The prior-piece correction Justin owes the reader:** Earlier DePIN pieces in the newsletter cited Datagram as the legitimate counter-example. That framing is now wrong. Own it in the personal reflection, not in a footnote. Per [[memory: project_datagram_rug]]: never repeat the legitimate-counter-example framing.

---

## Source Set (all in wiki, synthesis-aligned)

### Load-bearing (cited in body)

- [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]] — the April 2025 on-chain vote breakdown (Nova Labs proxy 26%, ferebee proxy 24%, 90.53/9.46 final tally, 763M veHNT total)
- [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]] — the proposal text including the "move quickly without involving Helium governance" quote
- **[[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]] (NEW in v2)** — the October 2025 on-chain vote breakdown (ferebee 31%, Nova Labs 26%, 96.72/3.27 final tally, 902M veHNT total, Keith Rettig as named 1% Against voter)
- **[[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]] (NEW in v2)** — the proposal text including the "emit the full allocation... to the single Service Provider Nova Labs" quote
- [[State of Helium Q4 2025 — Messari]] — $124.77/day IoT revenue, $56,635/day mobile revenue, 385,000 hotspots
- [[Helium Hotspot Earnings 2025 — AMBCrypto]] — $3–$45/month earnings range, $4–$8 common
- [[Helium Operator Economics — Bytetree - 2024-03]] — hardware costs ($249 indoor, $949 outdoor) and payback periods
- [[Helium Halving 2025 — Helium Blog - 2025-07-24]] — emissions cut, PoC reward halving, the Foundation's own proxy-delegation recommendation

### Supporting (context only)

- [[Helium HNT Tokenomics — Tokenomist]] — HIP-138 token consolidation context
- [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]] — mobile-side revenue context

**Synthesis basis:** [[Helium HIP-143 and the DePIN Franchise Architecture]] (filed 2026-05-18) is the analytical scaffolding. The synthesis names four transferable moves (franchise-vs-business, proxy-concentration audit, auto-renewal-by-inaction, deploy-first-find-out-later); this outline uses each one as a structural anchor — and adds a fifth move surfaced post-synthesis: **the proxy-veHNT-accumulation trajectory finding** (the proposing-entity proxies gaining voting power faster than the network, making future HIPs progressively easier to pass without operator participation).

---

## Source Gaps

- **None for the piece as scoped.** All load-bearing facts come from sources already in the wiki, including the two new HIP-148 source pages committed today (`08b936a`).
- **One open question deliberately left open in the prose.** The exact ownership and operating relationship between Nova Labs and ferebee — and the relationship of HIP-148's author `madninja` to either. Public sources document each as a Helium-ecosystem actor. The coordination signal in both vote breakdowns suggests a closer relationship than the public framing implies, but the piece references "the proposing entity and one of its co-authors" without claiming a single corporate identity behind both proxies. Honest framing; the synthesis's Follow-up Question #4 flags this as a documentary gap.

**Status:** Ready to draft. Next step (per orchestrator): tcn-outline-more (paragraph-level expansion + Marcus pre-assessment + accessibility pre-check), then tcn-headline.

---

## Working title candidates (for tcn-headline, not locked)

The v1 candidates are carried forward. v2 adds two candidates that lean on the trajectory finding and the HIP-148 substitution.

**v1 carryover:**
1. The Helium Vote Renewed Itself in April. Nobody Voted.
2. You Own the Hotspot. Nova Labs Owns What It Earns.
3. Half the Yes Votes Belonged to the Entity the Vote Authorized.
4. Helium Operators Built the Network. The Pricing Authority Lives Somewhere Else.
5. The Franchise Disclosure Document Arrives After You've Already Bought the Hardware.

**v2 additions (HIP-148 / trajectory leaning):**
6. Fifty Percent in April. Fifty-Seven in October. The Pattern Is Accelerating.
7. The Mapping Rewards Got Substituted for Gift Cards. The Vote Passed 96.72%.

The tcn-headline step will refine across the full pool. v2 preference (subject to that step): a two-clause structure that names a specific mechanism rather than waving at "control," with bonus credit for headlines that hint at the trajectory finding (the pattern is intensifying) rather than treating the franchise as static.
