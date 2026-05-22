# You Own the Hotspot. Nova Labs Owns What It Earns.

### A vote sold as a 1-year sunset gave Nova Labs pricing authority over 385,000 hotspots. Its text auto-extends if nobody overrides. Nobody overrode it.

A pro outdoor Helium hotspot costs $949. As of last August, after the network's halving, a well-placed urban unit earned between $4 and $8 a month. At $8 a month, the hardware pays itself off in ten years. At $4 a month, in twenty.

The pricing that determines what those hotspots earn is set by Nova Labs, the company that operates Helium Mobile and negotiates carrier offload deals with AT&T and other partners. That authority was granted by a governance vote in April 2025. The vote's text gave Nova Labs the authority for one year, and another year after that if no overriding HIP passed. In April 2026, the initial year ended. No overriding HIP passed. The authority extended itself.

Helium hotspot operators bought a franchise. They were sold a business. The hardware they paid for is theirs. The pricing authority that determines what their hardware earns is not.

---

## The Glitch: The vote that renewed itself in April

The vote was [HIP-143](https://github.com/helium/HIP/blob/main/0143-decoupling-service-provider-pricing-from-governance.md), a Helium Improvement Proposal, the governance mechanism Helium uses to change protocol rules. Passed April 3, 2025: it authorized Nova Labs to negotiate carrier pricing for the Helium Mobile network without routing each deal through the governance process. Carrier deals are confidential. Governance is slow. The commercial rationale was real. The proposal came with a 1-year initial term and a clause embedded in its detailed explanation: the authority would "be extended for one additional year if no HIP is passed by Helium governance that determines otherwise."

In April 2026, [the initial year ended and no superseding HIP was filed](https://messari.io/report/state-of-helium-q4-2025). The auto-extension clause triggered as written. The pricing authority now runs through April 2027, covering [385,000 deployed hotspots](https://messari.io/report/state-of-helium-q4-2025) and every operator running one.

Those operators paid for the hardware themselves. A [basic indoor Helium IoT box costs $249](https://eng.ambcrypto.com/how-much-can-you-really-earn-with-helium-hotspots-in-2025/). A [pro outdoor unit is $949](https://eng.ambcrypto.com/how-much-can-you-really-earn-with-helium-hotspots-in-2025/). After the [August 2025 halving](https://blog.helium.com/helium-halving-2025-8ecaa1fff464), a well-placed urban hotspot [earns $4 to $8 a month](https://eng.ambcrypto.com/how-much-can-you-really-earn-with-helium-hotspots-in-2025/). The halving was the algorithmic cut that reduced new HNT (Helium's native token) emissions from 15 million per year to 7.5 million. The outdoor unit pays back in ten years at the high end. Twenty at the low end.

Helium is a DePIN project (decentralized physical infrastructure networks, where independent operators deploy hardware that earns token rewards for coverage the network provides). Operators own the hardware. The governance audit is what the payback model skips.

Two HIPs got the pricing authority where it ended up. Six months apart. Same proposing entity. The second more concentrated than the first.

---

## The Source Code: Two votes, six months, concentration up

Three rule changes shaped the network before either of those votes landed. [HIP-53](https://github.com/helium/HIP/blob/main/0053-mobile-dao.md), passed July 25, 2022, established the Mobile subDAO and set the data transfer rate at $0.50 per gigabyte. [HIP-138 "Return to HNT"](https://github.com/helium/HIP/blob/main/0138-return-to-hnt.md), passed November 22, 2024, consolidated the IoT and Mobile subnetwork tokens into a single HNT. The [August 2025 halving](https://blog.helium.com/helium-halving-2025-8ecaa1fff464) cut new emissions in half. Each change had its own stated rationale. All three had a defensible rationale at the time.

The revenue split is where the rationales run dry. The IoT side of the network, all 385,000 hotspots, generates [$124.77 per day in actual data transfer revenue](https://messari.io/report/state-of-helium-q4-2025). The Mobile side, running carrier offload for AT&T and other partners plus Helium Mobile's own subscriber traffic, generates [$56,635 per day](https://messari.io/report/state-of-helium-q4-2025). One half of the network is the revenue. The other half is the hardware that gives the project something to point at.

[HIP-143's proposal text](https://github.com/helium/HIP/blob/main/0143-decoupling-service-provider-pricing-from-governance.md) explains the delegation rationale directly: "If Nova Labs would be able to move quickly and aligned with overall network goals, without involving Helium governance, the authors of this HIP anticipate that the total Data Transfer of the Helium network will rise." The commercial case holds. Carrier deals belong in a boardroom.

The [vote results](https://heliumvote.com/hnt/proposals/4EemLuZhTgtv6SFNogMByCTEx4DFtBKc32qEhDKL9iaZ) show something else. HIP-143 passed 90.53% on 763 million veHNT cast (vote-escrowed HNT, the staked governance token that determines voting weight). The Nova Labs proxy held 26.00% of the vote. The ferebee proxy, one of four named co-authors on HIP-143 (alongside Inversion Capital, zer0tweets, and Nova Labs itself), held 24.00%. Together: 50% of the yes votes that authorized the proposing entity's pricing authority.

Six months later, [HIP-148](https://github.com/helium/HIP/blob/main/0148-reallocate-mobile-mapping-rewards.md) voted October 3–10, 2025. It eliminated Mobile Mapping rewards, the 20% of Mobile network HNT emissions that subscribers had been earning by sharing location data from their phones. The proposal's text states the outcome plainly: "To simplify technical implementation, we propose to emit the full allocation available from Service Provider Rewards and Oracle Operator Rewards to the single Service Provider Nova Labs..." The Service Provider Pool went from 10% of Mobile emissions to 24%, all of it flowing directly to Nova Labs. Subscribers who had been mapping for HNT got Cloud Points instead (gift-card credits redeemable for eGift cards or charity donations).

The [HIP-148 vote](https://heliumvote.com/hnt/proposals/2PEJVC3nc2EncXMeyAzwYexRQmBSv6JyvBCJqNWHg76v) passed 96.72% on 902 million veHNT cast, 18% more participation than HIP-143. The ferebee proxy held 31.00% of the total vote, up from 24% on HIP-143. Nova Labs held 26.00%, flat in percentage but up 21% in absolute veHNT. Combined: 57% of the total vote for the proposal consolidating 24% of emissions to one of the two of them. A third labeled proxy, Jay M., voted yes at 5.00% on both HIP-143 and HIP-148. The top three controlled 62% of HIP-148.

ferebee was also a co-author of HIP-138 alongside @JMF and @abhay. The JMF initials match the Jay M. proxy label. Two of the top three HIP-148 proxies overlap the HIP-138 author list.

Keith Rettig voted against. He held 1.00% of the total vote.

Between the two votes, [ferebee's veHNT holdings grew from 183.85 million to 285.92 million](https://heliumvote.com/hnt/proposals/2PEJVC3nc2EncXMeyAzwYexRQmBSv6JyvBCJqNWHg76v), up 55.5% in six months. The total network's participation grew 18.2% in the same period. The proposing-entity co-author accumulated voting power at three times the network average while proposing changes that consolidated revenue to the proposing entity. The top single voter share rose accordingly: 15% on HIP-138 (anonymous wallet), 26% on HIP-143 (Nova Labs), 31% on HIP-148 (ferebee). The architecture has a trajectory. Each future HIP starts from a more concentrated baseline than the last.

In April 2026, [HIP-143's auto-extension activated](https://messari.io/report/state-of-helium-q4-2025) with no superseding HIP filed. The [Helium Foundation's own guidance](https://blog.helium.com/helium-halving-2025-8ecaa1fff464) recommends that operators "set a proxy as a backup to ensure you don't miss out on rewards." Ferebee and Nova Labs were the proxies most operators were pointed toward. Both had been accumulating.

---

## The Upgrade: What four disclosures would have caught

Nova Labs's case for pricing authority delegation is structurally sound. Carrier negotiations with T-Mobile and AT&T are confidential. Rate sheets belong in a boardroom. Putting commercial terms on-chain in real time would hand negotiating leverage to competitors. That constraint is real.

Before paying $249 to $949 for hardware and plugging into someone else's commercial network, an operator needs four things in writing. The Helium operator received none of them.

A written floor on what triggers a material change to the reward structure, plus an operator right to exit at that floor: a hardware buyback, migration provision, or refund of residual. HIP-148 is the test case: a 20% Mobile-emissions category was eliminated, a subscriber-labor category was substituted for gift cards, and no exit provision existed for the operators running hardware that had been earning from that category.

Aggregate disclosure on data-transfer revenue, even when individual carrier rate sheets stay confidential. The total revenue split gets disclosed, audited annually. The carrier-by-carrier rate sheets stay private.

Geographic acknowledgment that rural coverage and urban traffic are different goods. The operator who deployed in a rural area in 2022 built real coverage for the network's IoT use case. If the reward structure pays only for dense-urban carrier offload traffic, that operator bought a different product than they thought. They need to know which one before the hardware ships.

Sunset provisions that require an active re-vote before the authority extends. HIP-143's text does the opposite: the authority extends by default unless an overriding HIP passes. The four co-authors wrote it that way. The fix is a sunset clause that runs only when the network actively votes "yes again."

McDonald's franchisees read a Franchise Disclosure Document before signing. Federal law requires it. The Helium operator received the equivalent document as a sequence of HIPs written after the hardware was already plugged in.

Here's the honest version of the deal, in plain language:

You're buying a revenue-share position, priced by Nova Labs, on infrastructure you own and operate. Nova Labs's commercial terms are confidential. Your earnings are a function of their carrier negotiations and the network's data traffic, neither of which you control.

That's a real product. It just needs to be the sentence in the marketing. Right now it's the sentence the operator works out three years later from a Messari sector report.

The audit is the floor. It doesn't catch fraud.

---

## My Debug: The audit caught Helium. It missed my project.

I ran more than twelve Datagram nodes for a few months. I moderated their community for seven. Without pay. The project collapsed.

Earlier pieces I published on DePIN positioned Datagram as the legitimate counter-example, the project doing decentralized infrastructure differently. That framing was wrong, and I should have caught it earlier.

The four-part standard above would have caught Helium in 2021. Before any hotspot shipped, it would have revealed that pricing authority didn't belong to the operator class, that the reward structure had no exit provisions, and that no audit of the rural/urban split was built into the governance documents.

The four-part standard would not have caught Datagram. A project can publish exit provisions, revenue disclosure, geographic acknowledgment, and re-vote sunsets, and still have no business underneath any of it. I read Datagram's documents. They passed. What the documents couldn't tell me was whether the software was doing what they described. The code was closed-source.

My own system stats would have told me nothing real was running. I didn't watch them closely enough. I knew the alpha testnet figures were off and told myself the company needed a compelling story before exchanges committed. That was the rationalization. That's the debug.

The next operator who reads a DePIN whitepaper this month does the math before the hardware ships.
