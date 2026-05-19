# Detailed Outline: The Helium Franchise Architecture

**Trigger:** Named Hypocrisy
**Template:** System Audit (Problem → Analysis → Solutions)
**Timeliness:** HIP-143's 1-year sunset arrived in April 2026, weeks before publication — the pricing authority renewed itself by operator inaction.
**Target length:** 1,500–1,600 words

---

## OPENER APPROACH MAP

**Analogy to use:** The opener isn't a metaphor — it's a sequence of dated facts that enacts the franchise thesis without naming it. The broad thing: governance authority that renews itself by default. The specific thing: the exact pricing authority over a 385,000-hotspot wireless network. The bridging property: silence-as-design (the absence of a replacement vote IS the governance outcome). The narrowing: from the vote/sunset/renewal system-level fact, to the individual operators who paid $249–$949 for hardware, to the thesis. No traditional analogy-as-metaphor is deployed; the opener IS the argument assembled before it's named.

**Paragraph structure:**

¶1 — Establishes the auto-renewal beat as a news event: specific date (April 2025), specific mechanism (1-year sunset), specific outcome (renewed by silence). The hook is the paradox: governance authority that extends itself by governance inaction. No throat-clearing, no scene-setting. Opens mid-fact.

¶2 — Grounds the system-level finding in operator-scale economics. $249/$949 hardware costs, $4–$8/month earnings, 31–62 month / 10–20 year payback periods. The reader who knows anything about business math gets the picture before the thesis lands.

¶3 — The thesis lands in four parallel positive statements. "Helium hotspot operators bought a franchise. They were sold a business. The hardware they paid for is theirs. The pricing authority that determines what their hardware earns is not." (The fourth sentence breaks the pattern; the asymmetry is the argument.)

**Marcus 30-second test:** Passes. The opener is specific (named date, named mechanism, named company), the economics are concrete ($249 hardware, $4–$8/month), and the thesis is a precision gift: "bought a franchise / were sold a business" is the framing Marcus was circling but couldn't articulate. He's primed for the audited evidence Section 2 will deliver.

**What to avoid:**
- Do NOT use "governance" as an abstract noun in ¶1 without anchoring it immediately to the specific vote date and mechanism.
- Do NOT add a fourth paragraph previewing what the piece will cover. Thesis lands at paragraph 3 and Section 1 starts.
- Do NOT interpret "pricing authority" at the opener stage. Let it sit as a technical term; Section 2 will unpack it with primary-source quotes.

---

## The Glitch: The vote that renewed itself in April

Word target: ~400 words | Tone: sardonic precision — name what's broken without rage
Argument job: The opener delivered the thesis; this section delivers the mechanism — what happened, to whom, and why the numbers make it matter. Marcus needs to understand what's at stake for an operator before he'll credit the analysis in Section 2.

---

**¶1 — Concretize the auto-renewal mechanism for a reader who just absorbed the thesis**

Facts to deploy (in order):
- HIP-143 voted April 3, 2025. The proposal authorized Nova Labs to set carrier pricing without further Helium governance involvement.
  Source: [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]]
- The vote carried a 1-year sunset provision.
  Source: [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]]
- April 2026: sunset arrived. No superseding HIP was filed. Pricing authority extended itself by inaction.
  Source: [[State of Helium Q4 2025 — Messari]] (confirms no superseding HIP through Q4 2025)
- Network scale: 385,000 hotspots.
  Source: [[State of Helium Q4 2025 — Messari]]

Argument move: Concretizes the auto-renewal mechanism. The opener stated the finding; this paragraph names the specific vote date, the specific company, the specific sunset mechanism, and the specific outcome (extension by inaction).

Grounding plan: "April 3, 2025" (date), "Nova Labs" (named entity), "1-year sunset" (mechanism), "April 2026" (date), "385,000 hotspots" (count). Concrete throughout — no extra grounding needed.

Statistic framing: 385,000 hotspots embeds in "the scale of the network whose pricing authority extended by silence" — not a decoration, but evidence that this is a live deployed network, not a whitepaper.

Key sentence to land: The sentence that makes silence feel like a design decision: "No replacement vote was held." Three words; the pause after it is the argument.

---

**¶2 — Ground the governance stakes in operator economics**

Facts to deploy (in order):
- Basic indoor Helium IoT hotspot: $249
  Source: [[Helium Operator Economics — Bytetree - 2024-03]]
- Pro outdoor setup: $949
  Source: [[Helium Operator Economics — Bytetree - 2024-03]]
- As of August 2025, after the network's halving (the algorithmic cut that reduced new HNT emissions from 15 million a year to 7.5 million), a well-placed urban hotspot earns $3–$45/month; most operators $4–$8/month.
  Source: [[Helium Hotspot Earnings 2025 — AMBCrypto]]
- Indoor payback: 31–62 months at $4–$8/month.
- Outdoor payback: 10–20 years at $4–$8/month.
  Source: [[Helium Operator Economics — Bytetree - 2024-03]]

Argument move: Converts the governance abstract into the operator's economic reality. The governance question (who holds pricing authority?) becomes visceral when the reader does the payback math.

Grounding plan: "$249" (number), "$949" (number), "$4 to $8 a month" (number range), "31–62 months" and "10–20 years" (payback ranges). Concrete throughout.

Statistic framing:
- "$249/$949" — the operator's sunk cost before a single reward is earned.
- "$4–$8/month" — the mechanism: these numbers produce the payback math directly. At $8/month, the indoor unit pays back in 31 months; at $4/month, 62 months. Outdoor at $8/month: 10 years; at $4/month: nearly 20.
- "15 million → 7.5 million HNT/year" embeds in "the algorithmic cut that happened while operators were holding hardware they bought at different reward expectations."

Key sentence to land: The payback math stated without commentary. The outdoor unit at $949 paying $4–$8/month. Let Marcus do the arithmetic himself — the close of the paragraph just states the numbers without a verdict.

---

**¶3 — Land the franchise/business analytical move + vocabulary glosses**

Facts to deploy (in order):
- Franchise thesis (four parallel positive statements): Helium hotspot operators bought a franchise. They were sold a business. The hardware they paid for is theirs. The pricing authority that determines what their hardware earns belongs to Nova Labs.
- DePIN: decentralized physical infrastructure networks — tokenized projects where independent operators deploy hardware that earns rewards.
- HIP: Helium Improvement Proposal, the network's governance proposal format.
- PoC: Proof of Coverage, the algorithmic reward for hotspots that prove they cover a geographic area.

Argument move: Executes the thesis move from the opener in the body of the piece. The parallel positive statements are the analytical move; the vocabulary glosses are inline, brief, and invisible to the Marcus reader (who skips them) while onboarding the adjacent reader.

Grounding plan: "Nova Labs" (named entity), "pricing authority" (mechanism named specifically), the hardware referenced from ¶2 ($249/$949). The glosses themselves ground the abstract terms.

Statistic framing: None in this paragraph.

Key sentence to land: The four parallel statements. The fourth one ("The pricing authority that determines what their hardware earns belongs to Nova Labs") must land as a precise factual claim, not a verdict — because Section 2 is about to prove it with primary-source documents.

💡 [RHETORICAL SUGGESTION — USE OR SKIP]
Type: Structural move (anaphoric parallelism)
Location: The four-sentence franchise thesis block
Suggestion: The four sentences as written already have anaphoric potential. The draft could tighten the structure so each sentence starts with "The" — "The operators bought a franchise. The hardware is theirs. The earnings are not. The pricing authority that determines what those earnings are belongs to Nova Labs." Different rhythm than the outline's version; worth comparing on the page.
Example shape: Four sentences, each beginning with "The" or a named noun, the fourth breaking the noun pattern to land the named entity (Nova Labs).
Why it might work: The tight parallel form followed by the break on "Nova Labs" makes the entity's name feel like the answer to a setup question.
Why it might not: The outline's version ("Helium hotspot operators bought a franchise. They were sold a business.") has more human texture — "they were sold" has a passive-voice bite that "the operators bought" doesn't. Keep the outline version if that bite matters.

---

**¶4 — Set up Section 2: the two-vote progression Marcus is about to receive**

Facts to deploy (in order):
- The franchise architecture isn't a single event — it's a sequence of governance changes, vote by vote.
- Section 2 walks two of those votes: HIP-143 (April 2025) and HIP-148 (October 2025). Eighteen months apart. Same proposing-entity proxy structure. The second more concentrated than the first.

Argument move: Transition paragraph. Signals what Section 2 will deliver without over-explaining it. The question "who held the pricing authority across those two votes, and how was it granted?" is the interrogative setup that makes the Section 2 answer satisfying.

Grounding plan: "April 2025" and "October 2025" (dates), "HIP-143" and "HIP-148" (named proposals). Brief concrete anchors in an otherwise transitional paragraph.

Statistic framing: None.

Key sentence to land: "Section 2 walks two of those votes — eighteen months apart, same proposing entity, the second more concentrated than the first." The word "concentrated" is the teaser that earns Section 2.

---

## The Source Code: Two votes, eighteen months, concentration up

Word target: ~550 words | Tone: building analytical weight — charitable reading first, then the audit
Argument job: Where Section 1 established what's broken, Section 2 establishes WHY — and shows that the pattern has a documented trajectory, not just a single incident.

---

**¶1 — Charitable reading of the earlier rule changes (HIP-82, HIP-138, the halving)**

Facts to deploy (in order):
- HIP-82: capped data rewards at $0.50 per gigabyte, up to (subscriber plan cost ÷ $0.50), zero above that. Rationale: prevents operators from earning indefinitely on subscribers who've maxed out their plan.
  Source: [[Helium HNT Tokenomics — Tokenomist]]
- HIP-138: consolidated IOT and MOBILE subnetwork tokens into HNT, January 2025. Rationale: simplified accounting.
  Source: [[Helium HNT Tokenomics — Tokenomist]]
- August 2025 halving: cut emissions from 15M to 7.5M HNT/year, halved PoC rewards. Rationale: emission discipline.
  Source: [[Helium Halving 2025 — Helium Blog - 2025-07-24]]

Argument move: The "charitable reading first" move. The official justifications for the three earlier rule changes are presented without dismissal labels. This earns the analytical credibility for the audit that follows — you can't call something broken without having first taken the opposing case seriously.

Grounding plan: "HIP-82" (named proposal), "$0.50 per gigabyte" (specific mechanism price), "HIP-138" (named proposal), "January 2025" (date), "August 2025" (date), "15M to 7.5M HNT" (halving figures). Concrete throughout.

Statistic framing:
- "$0.50 per gigabyte" embeds in the cap mechanism: the number defines the ceiling a subscriber's plan imposes on operator earnings. It's not a decoration; it's the pricing rule.
- "15M → 7.5M HNT/year" embeds in supply compression: this is the mechanism that halved the reward floor while operators held hardware bought at different earnings expectations.

Key sentence to land: The deadpan closer of the charitable reading: "Each proposal had its own justification. Present them fairly." (Two sentences. The second one — directed inward — signals that the audit is about to start and earns Marcus's patience for ¶2's harder numbers.)

---

**¶2 — The revenue audit: the IoT/Mobile asymmetry as evidence**

Facts to deploy (in order):
- IoT side of the network: $124.77/day in real Data Credit burns across the entire 385,000-hotspot base ≈ $45,000/year total.
  Source: [[State of Helium Q4 2025 — Messari]]
- Mobile side (routes carrier offload from T-Mobile and AT&T): $56,635/day ≈ $20.7M/year.
  Source: [[State of Helium Q4 2025 — Messari]], [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]]
- An operator who built out a rural hex in 2022 created a real public good for the network's IoT ambitions. They were later told it was not the public good that pays.

Argument move: "Proves by contrast." The three earlier rule changes looked defensible in isolation; run them for three years and the revenue split reveals where the economic logic actually landed. One half of the network generates the revenue; the other half is the hardware that gives the project something to point at.

Grounding plan: "$124.77/day" (specific number), "385,000 hotspots" (named count), "$56,635/day" (specific number), "T-Mobile and AT&T" (named carriers), "a rural hex in 2022" (concrete scene — a specific geographic operator deployment with a date). The rural hex is the human-scale grounding for the IoT/Mobile abstract asymmetry.

Statistic framing:
- "$124.77/day IoT" and "$56,635/day Mobile" — the numbers embed in the asymmetry argument. Don't state the ratio explicitly; let the reader do the math. State the raw figures and let them sit next to each other.
- "385,000 hotspots" embeds in "$124.77/day across 385,000 operators" — that's $0.0003/operator/day from the IoT side, before costs. The number makes the coverage/revenue gap visceral without spelling it out.

Key sentence to land: The pivot sentence that collapses the audit: "One half of the network is the revenue. The other half is the hardware that gives the project something to point at." (Two short declarative sentences. The symmetry of the construction is intentional — it mirrors the IoT/Mobile split.)

---

**¶3 — HIP-143: the pricing-authority handoff and the proposal text**

Facts to deploy (in order):
- HIP-143 voted April 3, 2025.
  Source: [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- The proposal authorized Nova Labs (the company that operates Helium Mobile and negotiates the carrier offload deals) to set carrier pricing without further Helium governance involvement.
  Source: [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]]
- Direct quote from proposal text: "If Nova Labs would be able to move quickly... without involving Helium governance, the authors of this HIP anticipate that the total Data Transfer of the Helium network will rise."
  Source: [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]]
- The structural argument for this delegation is defensible: confidential commercial negotiations don't belong on-chain; carriers want rate sheets private; Nova Labs needs negotiating speed. Concede all of it.

Argument move: Introduces HIP-143 by leading with its stated rationale. The concession is genuine — the proposal has a real structural case. The direct quote establishes the primary source baseline; the concession earns the right to run the vote breakdown in ¶4.

Grounding plan: "April 3, 2025" (date), "Nova Labs" (named entity), "Helium Mobile" (named product), the direct quote (primary source — the most grounded sentence possible). The direct quote is the primary grounding device.

Statistic framing: No statistics in this paragraph. The load-bearing element is the direct quote.

Key sentence to land: The direct quote itself. "If Nova Labs would be able to move quickly... without involving Helium governance, the authors of this HIP anticipate that the total Data Transfer of the Helium network will rise." In context — immediately after the revenue asymmetry has landed — the quote does its own work without commentary.

---

**¶4 — HIP-143 vote breakdown: the Named Hypocrisy trigger**

Facts to deploy (in order):
- Passed 90.53% to 9.46%.
  Source: [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- Total veHNT cast: 763 million. veHNT = vote-escrowed HNT, the staked governance token. Minimum quorum: 100 million.
  Source: [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- Nova Labs proxy: 26.00% of the vote.
  Source: [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- ferebee proxy (listed as a co-author of HIP-143): 24.00% of the vote.
  Source: [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- Together: 50% of the yes votes for the proposal authorizing the proposing entity's pricing authority.
  Source: [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- Largest "against" vote: anonymous proxy at 8%.
  Source: [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]

Argument move: The Named Hypocrisy trigger landing. State the numbers. No editorial commentary. The reader does the math. veHNT gets its inline gloss on first use here.

Grounding plan: "90.53%" (percentage), "763 million veHNT" (count with inline gloss), "Nova Labs" (named entity), "26.00%" (percentage), "ferebee" (named entity), "24.00%" (percentage), "50% of the yes votes" (derived figure). Named entities plus specific percentages. Concrete throughout.

Statistic framing:
- "763 million veHNT" embeds in "this was the total governance stake that approved the handoff" — establishes that this was not a low-turnout technicality.
- "50% of the yes votes" embeds in the Named Hypocrisy: the proposing entity and a listed co-author cast exactly half the votes that authorized the proposing entity's commercial authority.
- Note: the "largest against vote from an anonymous proxy at 8%" is load-bearing as contrast for the Keith Rettig figure in ¶6 — name the anonymous opposition here so that Keith Rettig's named dissent on HIP-148 lands as a deliberate contrast.

Key sentence to land: State the numbers. The reader does the math. The prose should not add "which means" or "this reveals" — the numbers are the paragraph's last word.

---

**¶5 — HIP-148: the substitution, the proposal text, and the Cloud Points switch**

Facts to deploy (in order):
- Eighteen months after HIP-143. HIP-148 voted October 3–10, 2025.
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- The proposal eliminated the Mobile Mapping rewards category — 20% of HNT emissions that subscribers had been earning by sharing location data from their phones.
  Source: [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]
- Redirected: 10% to Service Provider Pool, 10% to Data Transfer Pool; 4% Oracle Operator allocation folded in.
  Source: [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]
- Service Provider Pool now 24% of Mobile emissions.
  Source: [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]
- Direct quote from proposal text: "To simplify technical implementation, we propose to emit the full allocation available from Service Provider Rewards and Oracle Operator Rewards to the single Service Provider Nova Labs."
  Source: [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]
- Subscribers who had been earning HNT for mapping data now earn Cloud Points — gift-card credits redeemable for eGift cards or charity donations.
  Source: [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]
- The proposal's own motivation section concedes mapping data was "not very useful": "carrier offload locations are a much higher quality signal of where to deploy than mapping data."
  Source: [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]

Argument move: HIP-148 is the second instance of the pattern, with a new dimension HIP-143 didn't have: an explicit emissions-to-corporate substitution (tokens → gift cards, 20% emissions category → Nova Labs direct allocation). The direct quote from the proposal does the analytical work.

Grounding plan: "eighteen months later" (temporal), "October 3–10, 2025" (dates), "20% of HNT emissions" (specific allocation), "Nova Labs" (named entity), the direct quote (primary source), "Cloud Points" (named mechanism, glossed inline as "gift-card credits redeemable for eGift cards or charity donations"), "24% of Mobile emissions" (specific allocation figure).

Statistic framing:
- "20% of HNT emissions" embeds in "this was the subscriber reward category that existed before this proposal."
- "24% of Mobile emissions" (up from 10% Service Provider Pool pre-HIP-148) embeds in "this is what Nova Labs now receives directly after the consolidation." The delta from 10% to 24% is the finding; state both figures.
- Cloud Points: the inline gloss IS the statistic framing — a named product category (gift cards) substituting for a token with a market price is the mechanism. No number needed; the substitution is the evidence.

Key sentence to land: The direct quote from the proposal — "...emit the full allocation available from Service Provider Rewards and Oracle Operator Rewards to the single Service Provider Nova Labs." The document writes the argument. No commentary needed after it.

---

**¶6 — HIP-148 vote breakdown: the pattern repeated, more concentrated; Keith Rettig as named dissent**

Facts to deploy (in order):
- Passed 96.72% to 3.27%.
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- Total veHNT cast: 902 million (18% more participation than HIP-143's 763 million).
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- ferebee proxy: 31.00% of total vote (up from 24% on HIP-143).
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- Nova Labs proxy: 26.00% of total vote (unchanged in percentage; +21% in absolute veHNT, 199.79M → 241.87M).
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- ferebee + Nova Labs = 57% of total vote (up from 50% of yes votes on HIP-143).
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- Keith Rettig: 13.98 million veHNT, 1.00% of total vote, voted Against. Largest named "Against" vote in the top 12.
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- Every other named proxy in the top 12 voted For.
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]

Argument move: The pattern repeated, more concentrated. This paragraph mirrors ¶4 structurally (vote breakdown with combined concentration finding) but the numbers are worse — 57% vs. 50%, concentration grew even as total participation grew, and a named human dissenter makes the abstract proxy-concentration finding feel like something a real person opposed.

Grounding plan: "96.72%" (percentage), "902 million veHNT" (count), "ferebee" (named entity, 31%), "Nova Labs" (named entity, 26%), "57%" (combined), "Keith Rettig" (named person), "13.98 million veHNT / 1.00%" (specific count and percentage). Named entities and numbers throughout. Concrete.

Statistic framing:
- "902 million veHNT" and "+18% vs. HIP-143" — embeds in "more of the network's governance stake was cast, and the concentration was higher." More participation did not dilute concentration; it intensified it.
- "57%" (vs. 50%) — the progression finding. State both numbers; let the direction do the work.
- "13.98 million veHNT / 1.00%" — embeds in Keith Rettig as the human-scale figure: this is what a meaningful individual stake looks like as a share of total governance power. The number makes the futility visible without editorializing on it.

Key sentence to land: "Keith Rettig" named, his veHNT stated, the comparison to "every other named proxy in the top 12 voted For" stated. No verdict added. The list structure does the work.

😬 [HUMOR LOCATION]
Situation: The paragraph has just laid out a governance vote where the proposing-entity proxies held 57% of the total vote on a proposal consolidating 24% of emissions to themselves. Keith Rettig opposed it with 1.00%.
Register: deadpan — Thompson detonation rhythm (setup, floor blows out)
Rough target: Keith Rettig's 1% as the moment of recognizable human futility. The joke should land on the gap between having a meaningful stake in nominal terms and having no meaningful power in practice. Do not explain the joke. Do not name the irony.
Model sentence rhythm: "Turns out I wasn't paranoid. I was just early." — credible setup, floor blows out, lands somewhere you didn't expect but can trace. One sentence about Keith Rettig's position; one short sentence after it. That's it.

---

**¶7 — Trajectory + auto-renewal capstone: the pattern is not static**

Facts to deploy (in order):
- ferebee veHNT: 183.85M (HIP-143, April 2025) → 285.92M (HIP-148, October 2025) = +55.5% in 6 months.
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- Nova Labs veHNT: 199.79M → 241.87M = +21% in the same period.
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- Network total veHNT cast: 763.5M → 902.3M = +18.2%.
  Source: [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- ferebee grew veHNT holdings at 3x the rate of the total network in those 6 months.
  (Derived: 55.5% vs. 18.2%)
- HIP-143's 1-year sunset: arrived April 2026. No superseding HIP filed. Pricing authority extended.
  Source: [[State of Helium Q4 2025 — Messari]]
- Helium Foundation's own guidance recommends operators "set a proxy as a backup to ensure you don't miss out on rewards."
  Source: [[Helium Halving 2025 — Helium Blog - 2025-07-24]]

Argument move: Section 2's capstone. The two-vote progression established the pattern; this paragraph establishes that the pattern is intensifying — and that the mechanism (proxy delegation encouraged by the Foundation) is design, not accident. The auto-renewal callback closes the section with the news peg.

Grounding plan: "183.85M → 285.92M" (specific counts), "+55.5%" (derived percentage), "ferebee" (named entity), "+18.2%" (network total for comparison), "April 2026" (date), the Foundation's direct recommendation quote. All concrete.

Statistic framing:
- "+55.5% vs. +18.2% network total" — the comparison embeds in "the proposing-entity proxy accumulated veHNT at 3x the network average rate." Stating the ratio (3x) may serve the reader better than leaving the arithmetic; the draft can decide.
- "April 2026" embeds in the auto-renewal mechanism: this is the specific month the clock expired without a vote.

Key sentence to land: "The architecture is not a snapshot. It is a trajectory." (Two declarative sentences. Avoids the banned "not X, it's Y" pattern by making each assertion its own independent sentence rather than a reframe.)

---

## The Upgrade: What four disclosures would have caught

Word target: ~400 words | Tone: measured — acknowledge trade-offs honestly; no cheerleading
Argument job: Where Section 2 established why the system is broken, this section names what a disclosed franchise would look like. Not utopian — four specific structural features, each grounded in a documented Helium failure.

---

**¶1 — Concede the real commercial constraint**

Facts to deploy (in order):
- Carrier offload pricing is a competitive variable for T-Mobile and AT&T.
- Confidential commercial negotiations don't belong on-chain.
- Nova Labs needs negotiating speed with carriers.
- The structural argument for delegating pricing authority is not invented.

Argument move: Continues the "charitable reading first" posture from Section 2. Before the four-part disclosure standard lands, the piece credits the opposing case. This is what earns the right to name what's actually missing.

Grounding plan: "T-Mobile" and "AT&T" (named carriers), "Nova Labs" (named entity). The concession is grounded in specific named parties rather than abstract "enterprises."

Statistic framing: None in this paragraph.

Key sentence to land: "Nova Labs's structural argument for pricing authority delegation is not invented. It describes a real commercial constraint." (Two declarative sentences. The concession is genuine, not performative.)

---

**¶2 — The audit's purpose + the four-part disclosure framework**

Facts to deploy (in order):
- The question is what an operator needs to know, in writing, before paying $249–$949 for hardware and plugging into someone else's commercial network.
- Four things a disclosed franchise has that the Helium operator never received:
  1. A written floor on what triggers a material change to the reward structure, plus an operator right to exit at that floor (hardware buyback, migration provision, or refund-of-residual). HIP-148 is the case: 20% of emissions was reallocated, a subscriber-labor category was substituted for gift cards, no exit provision existed.
  2. Aggregate transparency on data-transfer revenue, audited annually, even when individual carrier rate sheets are confidential. The unit economics can stay private. The total revenue split cannot.
  3. Geographic acknowledgment that rural coverage and urban traffic are different goods. One reward structure that pays both is one product. A reward structure that pays only the dense-urban traffic is a different product — the operator deploying in a rural hex needs to know which one they bought.
  4. Sunset provisions that require an active re-vote, not auto-renewal by silence. The Helium structure is fixable here.

Argument move: The densest paragraph in Section 3. The four bullets ARE the Upgrade — what the system could do differently. Each is grounded in a specific Helium failure mode. The HIP-148 parenthetical for bullet 1 connects the framework directly to the Section 2 evidence.

Grounding plan: "$249–$949" (hardware cost callback from Section 1), "HIP-148" (named proposal for bullet 1's parenthetical), "20% of emissions" (specific allocation), "gift cards" (concrete substitution mechanism), "rural hex" (concrete geographic type, callback from Section 2 ¶2), "April 2026 auto-renewal" (named event, callback from Sections 1 and 2). Concrete throughout via named callbacks.

Statistic framing:
- "$249–$949" embeds in "this is the sunk cost before a single reward rule can change."
- "20% emissions" embeds in bullet 1's parenthetical — this was the category eliminated without an exit provision.

Key sentence to land: The framing sentence before the four bullets. **Draft-time flag:** avoid the "not X, the question is Y" construction (banned negative parallelism). Lead with the positive: "Before paying $249 to $949 for a piece of hardware and plugging into someone else's commercial network, an operator needs four things in writing. The Helium operator received none of them." (Or similar — the point is to state the positive claim directly without negating a prior framing first.)

---

**¶3 — Name the honest version of the deal**

Facts to deploy (in order):
- The honest version of the Helium operator agreement, stated in plain language: "You're buying a revenue-share position, priced by a centralized negotiator (Nova Labs), on infrastructure you own and operate. The negotiator's commercial terms are confidential. Your earnings are a function of their negotiations and the network's data traffic, neither of which you control."
- That sentence is a real product. It just needs to be the sentence in the marketing, not the sentence the operator works out three years later from a Messari sector report.

Argument move: Collapses all of Section 2's evidence into a single paragraph that could live at the top of an operator onboarding page. The franchise analogy from the opener returns here — not as a callback, but as a deliverable: here is the franchise disclosure document you didn't receive.

Grounding plan: "Nova Labs" (named entity — must appear here, not just "a centralized negotiator"), "Messari sector report" (named source type — concrete enough to be grounding). **Draft-time flag:** name "Nova Labs" inside the disclosure paragraph rather than leaving it at "centralized negotiator" for entity-level grounding.

Statistic framing: None in this paragraph. The argument is the disclosure text itself.

Key sentence to land: "That sentence is a real product. It just needs to be the sentence in the marketing, not the sentence the operator works out three years later from a Messari sector report." (The deadpan finish — no abstract noun phrase, just a location (marketing) and a time lag (three years later).)

💡 [RHETORICAL SUGGESTION — USE OR SKIP]
Type: Structural callback (franchise analogy from opener)
Location: Opening of ¶3 or transition from ¶2 to ¶3
Suggestion: A McDonald's franchisee reads a Franchise Disclosure Document before signing — federal law requires it (the FDD is the FTC's term of art). The Helium operator received the equivalent document as a sequence of HIPs written after the hardware was already plugged in. This callback converts the opener's franchise analogy from metaphor to structural parallel: there is an actual regulatory standard for what disclosures a disclosed franchise requires, and Helium's governance sequence is measurable against it.
Example shape: One sentence naming the FDD as a real regulatory document; one sentence noting the Helium operator's equivalent arrived post-hardware. Then directly into the "honest version of the deal" paragraph.
Why it might work: The FDD reference gives the four-part framework a real regulatory anchor and makes "disclosed franchise" sound like a standard rather than a wishlist.
Why it might not: The FDD callback here means the close can't use it again. Decide whether the franchise analogy callback belongs in Section 3 or in the close — it works in either location but shouldn't appear in both.

---

**¶4 — Acknowledge the limit: the audit is the floor, not the ceiling**

Facts to deploy (in order):
- None of the four disclosures catches outright fraud.
- A project can issue all four disclosures and still be hollow.
- The audit is the floor, not the ceiling.

Argument move: Transition paragraph. Sets up Section 4 by naming where the framework fails. Without this, the personal reflection is a non-sequitur. With it, the audit limitation IS the setup.

Grounding plan: "Outright fraud" (concrete failure mode), "hollow" (concrete descriptor — a project with no business underneath the disclosure). This paragraph is intentionally brief (2–3 sentences). The implication of "outright fraud" is what earns the reader's attention for Section 4.

Statistic framing: None.

Key sentence to land: "The audit is the floor, not the ceiling." (Short declarative. The period is load-bearing.)

---

## My Debug: The audit caught Helium. It missed my project.

Word target: ~250 words | Tone: first person, direct — the personal anecdote serves the argument
Argument job: Personal vulnerability that marks the limit of the preceding audit. The four-part framework would have caught Helium in 2021; it would not have caught Datagram. This section earns the closing recommendation by showing the writer paid the tuition.

---

**¶1 — The frame: Datagram, 12+ nodes, 7 months, the rug, the prior-piece correction**

Facts to deploy (in order):
- Justin ran more than twelve Datagram nodes for several weeks.
- He worked on the project for about seven months without pay.
- The project collapsed.
- Earlier pieces in this newsletter positioned Datagram as the legitimate counter-example, the DePIN project doing it differently.
- That framing was wrong. He's correcting it here.

Argument move: Opens the personal section by staking the credibility claim — Justin didn't observe DePIN operator failure from the outside. He paid the tuition. The prior-piece correction is owned in the first paragraph, not buried in a footnote.

Grounding plan: "twelve Datagram nodes" (specific count), "seven months" (duration), "without pay" (concrete condition), "Datagram" (named entity), "earlier pieces in this newsletter" (named context). Concrete throughout.

Statistic framing:
- "twelve nodes" and "seven months" are the tuition figures. They embed in "this is what the operator-level investment looked like before the project failed."

Key sentence to land: The prior-piece correction: "Earlier pieces I published on DePIN positioned Datagram as the legitimate counter-example, the project doing it differently. That framing was wrong, and I should have caught it earlier." (No hedging, no passive voice on the ownership.)

😬 [HUMOR LOCATION]
Situation: Justin has just laid out a four-part disclosure framework (Section 3) and is now admitting he didn't run that framework on his own deployment. He ran twelve nodes for seven months and got rugged.
Register: self-deprecating deadpan
Rough target: The gap between the four-part audit Justin just offered Marcus and the fact that Justin didn't run it himself. This is the pressure-valve moment — the personal section is heavy; the joke is the release.
Model sentence rhythm: Short setup, floor blows out. One sentence about the framework's theoretical utility. One sentence about what the writer did instead. No explanation. No name-the-irony. The reader completes it themselves.

---

**¶2 — What the audit catches and what it doesn't: Datagram as proof of the limit**

Facts to deploy (in order):
- The four-part disclosure standard from Section 3 would have caught Helium in 2021: it would have revealed before any hardware deployed that pricing authority didn't belong to the operator class.
- It would NOT have caught Datagram. A project can publish exit provisions, revenue transparency, geographic acknowledgment, and re-vote sunsets, and still have no business underneath any of it.
- The structural problem (governance design) and the fraud problem share an architecture: both require an operator who deploys capital before the documents that govern what they bought are written.

Argument move: The analytical capstone of Section 4. The audit has a verified limit, demonstrated by a personal case. This earns the closing recommendation — because the recommendation comes from someone who ran both the framework AND the hardware.

Grounding plan: "Helium in 2021" (named entity + year), "Datagram" (named entity), "exit provisions / revenue transparency / geographic acknowledgment / re-vote sunsets" (named elements from Section 3). Concrete throughout via named callbacks.

Statistic framing: None in this paragraph.

Key sentence to land: "The structural problem and the fraud problem share an architecture." (Short declarative. Preceded by two grounded sentences naming Helium and Datagram — this is the abstraction sentence, but it arrives after the named examples, so it lands as compression rather than hand-waving.)

---

**¶3 — The conclusion: necessary but not sufficient, and the named-actor closing line**

Facts to deploy (in order):
- A rational DePIN operator in 2026 runs the four checks and still treats the deployment itself as a separate decision.
- The right move, given the stack of failure modes, might be to not deploy first.
- Closing line: "The next operator who reads a DePIN whitepaper this month does the math before the hardware ships, not after."

Argument move: The piece's conclusion. The first sentence states the audit's limits honestly; the second is the most direct claim the piece makes; the closing line is the named-actor sentence per § 3J — a person doing a thing, with a specific time constraint.

Grounding plan: "DePIN operator in 2026" (named actor, specific year), "a DePIN whitepaper" (named document type), "the hardware ships" (named event). The closing line is concrete throughout.

Statistic framing: None.

Key sentence to land: "The next operator who reads a DePIN whitepaper this month does the math before the hardware ships, not after." Named actor (the next operator). Active verb (does the math). Time constraint (this month). No abstract noun phrase summarizing the piece's structural concept.

---

## CLOSE APPROACH MAP

**Callback:** The franchise analogy from the opener returns at the Section 3 / Section 4 hinge. The opener said: "Helium hotspot operators bought a franchise." Section 3's "honest version of the deal" paragraph rewrites what that franchise document should have said. Section 4's personal reflection shows what happens when the audit framework exists but you didn't run it. The franchise analogy can land either in Section 3 ¶3 (as the FDD structural callback) or in the Section 4 transition — but not both. Decide at draft time which location serves the argument better.

**New element:** The close adds the "necessary but not sufficient" move — the audit catches governance failures; it doesn't catch fraud. This is the one thing the body doesn't establish until Section 4. Sections 1 and 2 proved the franchise architecture is real and intensifying. Section 3 named the four fixes. Section 4 names the ceiling above the fixes. The closing line converts all of that into one person doing one action.

**Cover Test:** If you cover the last paragraph, do you already have the ending? No — the "necessary but not sufficient" claim appears only in Section 4 ¶2, and without the closing paragraph it lands as a dead end rather than a recommendation. The named-actor closer adds "who does this apply to" and "by when." Without it, the close ends on the abstraction ("both require an operator who deploys capital before the documents are written"). With the closing line, it ends on a person who hasn't deployed yet.

**Final sentence goal:** Leave the reader with a specific action (do the math) before a specific event (the hardware ships) at a specific time (this month). The reader who has hardware on order and hasn't checked the governance forum is the exact target. They should feel the temporal pressure — "this month" is now, not someday.

---

## ACCESSIBILITY PRE-CHECK

**1. Grounding coverage — Every paragraph block names where abstraction touches ground, or marks itself as "concrete throughout."**

Assessment: All 11 paragraph blocks have grounding plans populated. Two items requiring draft-time attention:
- Section 3 ¶2: The four-part framework bullet list risks three consecutive abstract bullets before the HIP-148 parenthetical grounds bullet 1. The draft should interleave specific Helium callbacks within each bullet rather than listing all four at once.
- Section 3 ¶3: "centralized negotiator" should name "Nova Labs" in the draft for entity-level grounding consistency.

**2. Statistic framing — Every number in "Facts to deploy" has its mechanism noted.**

Assessment: All load-bearing numbers have mechanism notes. Summary:
- $249/$949 → sunk cost before any reward rule applies
- $3–$45/month, $4–$8/month → payback period mechanism
- 15M→7.5M HNT/year → supply compression mechanism
- $124.77/day IoT, $56,635/day Mobile → revenue asymmetry evidence
- 763M veHNT (HIP-143) → governance scale (not a low-turnout technicality)
- 50% combined yes votes → Named Hypocrisy trigger
- 902M veHNT (HIP-148) → participation growth context for concentration finding
- 57% combined total vote → concentration intensification
- +55.5% ferebee veHNT / +18.2% network total → trajectory finding (3x rate)
- 13.98M veHNT / 1.00% → Keith Rettig human-scale figure
No naked numbers found.

**3. Paragraph length intention — Sections at risk of length-flat rhythm:**

- Section 1: 4 paragraphs for ~400 words = ~100 words each. At ceiling. Draft should vary: ¶1 (auto-renewal beat) and ¶4 (setup for Section 2) should be the shortest; ¶2 (economics) the longest.
- Section 2: 7 paragraphs for ~550 words = ~79 words each. Good variation room. ¶1 (charitable reading) and ¶7 (trajectory) should be the shortest; ¶5 (HIP-148 proposal) the longest.
- Section 3: 4 paragraphs for ~400 words = ~100 words each. At ceiling. ¶2 (four-part framework) will naturally run ~150 words; compensate with ¶1 and ¶4 at ~50 words each.
- Section 4: 3 paragraphs for ~250 words = ~83 words each. Good variation room.

**4. Reader address — "You" usage:**

Assessment: "You" appears in the Section 3 ¶3 "honest version of the deal" paragraph: "You're buying a revenue-share position, priced by a centralized negotiator (Nova Labs), on infrastructure you own and operate." This is the correct location per voice-rules.md — the "you" places the operator inside the system the piece is describing. It must not appear before this point in the article, and must not be used again after it. Confirmed per § 1.3 of voice-rules.md.

**5. Anaphora opportunities:**

Assessment: Section 1 ¶3 (the four parallel franchise-thesis statements) has an anaphora opportunity flagged in the rhetorical suggestion. Section 2 ¶7 ("The architecture is not a snapshot. It is a trajectory.") has anaphoric potential if extended to three sentences — the draft can decide. No other locations require explicit flagging.

Verdict: **Ready for tcn-draft.** Two draft-time grounding flags (name Nova Labs in Section 3 ¶3; interleave Helium callbacks in Section 3 ¶2's bullet list). Paragraph length variation needed in Section 1 and Section 3 to avoid length-flat rhythm.

---

## MARCUS PRE-ASSESSMENT

**1. Signal test — Does this deliver at least one thing Marcus couldn't have found easily himself?**

Assessment: Yes. The primary-source direct quote from HIP-148 ("...emit the full allocation... to the single Service Provider Nova Labs") and the vote breakdown screenshots establishing ferebee +55.5% veHNT accumulation against +18.2% network growth. The trajectory finding — concentration is intensifying at a documented rate, not static — is the piece's strongest signal beyond any secondary source. Messari paraphrased HIP-143; this piece cites both HIPs from primary sources with the vote-breakdown data. The combination is not available anywhere without doing the source work.

**2. Patience test — Would Marcus still be reading at paragraph 3?**

Assessment: Yes, but Section 2 ¶1 (the charitable reading of HIP-82, HIP-138, and the halving) is the paragraph most likely to lose him. It's mechanism-dense with three proposal names in sequence. The draft should keep it tight (under 80 words) and close with the deadpan self-instruction ("Each proposal had its own justification. Present them fairly.") — that two-sentence close signals to Marcus that the audit is about to start and earns his patience for ¶2's revenue numbers.

**3. Depth test — Does this feel like the writer operates in the thing they're writing about?**

Assessment: Yes. Three credibility signals: (1) the primary-source vote portal citations (not just Messari summaries), (2) the specific hotspot payback math at the post-halving earnings levels, (3) the Section 4 disclosure that Justin ran nodes and got rugged on a project he called the legitimate counter-example. Marcus can tell the difference between a journalist who read the Messari report and someone who has deployed hardware.

**4. Save test — Would Marcus save or forward?**

Assessment: Forward. Named Hypocrisy trigger → System Audit template → forward to one specific person in his DePIN Discord. "The proposing entity and co-author cast 57% of the votes for a proposal consolidating 24% of emissions to themselves" is the formulation Marcus was circling but couldn't articulate. He forwards it to prove he was right.
Secondary save: The four-part disclosure standard in Section 3 has reference value — Marcus may save it to cite the criteria when evaluating a new DePIN project. The "framework to reuse" element grafts a save-trigger onto what is otherwise a forward-first piece.

**5. Accumulation test — Does this raise or maintain the signal floor?**

Assessment: Raises. This is the second consecutive piece applying the same analytical move (audit what was announced against what was contractually true) to a different domain. The first piece was 12 Gigawatts (grid capacity vs. built capacity). This piece is Helium (operator promises vs. governance documents). Two consecutive pieces showing the move working in different domains is worth more than one strong piece — Marcus reads this as: the writer has a framework, not a hot take.

Verdict: **Ready to write.** The signal test (primary-source data unavailable in secondary coverage + trajectory finding) is the strongest individual score. The patience test flags Section 2 ¶1 as the highest-risk paragraph for Marcus attrition — keep it tight.

---

## SOURCE GAPS

No source gaps for the piece as scoped. All load-bearing facts have confirmed wiki sources:

- HIP-143 proposal text and vote breakdown: [[Helium HIP-0143 — Decoupling Service Provider Pricing from Governance]], [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]]
- HIP-148 proposal text (GitHub): [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]]
- HIP-148 vote breakdown (screenshots): [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
- Operator economics and earnings: [[Helium Operator Economics — Bytetree - 2024-03]], [[Helium Hotspot Earnings 2025 — AMBCrypto]]
- IoT/Mobile revenue split: [[State of Helium Q4 2025 — Messari]], [[Helium Mobile Revenue and Carrier Offload — Sarson Funds - 2025]]
- Halving details and proxy-delegation guidance: [[Helium Halving 2025 — Helium Blog - 2025-07-24]]
- HNT tokenomics / HIP-82 / HIP-138: [[Helium HNT Tokenomics — Tokenomist]]
- No superseding HIP confirmation: [[State of Helium Q4 2025 — Messari]]

**One open editorial question (not blocking):** the relationship of HIP-148 author `madninja` to the ferebee proxy and Nova Labs. The piece's current framing ("the proposing entity and one of its co-authors") holds without resolution. Not required before drafting.

**Status: Ready to write.**
