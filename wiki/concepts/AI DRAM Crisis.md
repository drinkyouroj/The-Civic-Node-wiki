---
title: "AI DRAM Crisis"
type: concept
tags: [technology, ai, infrastructure, supply-chain, power]
created: 2026-04-12
updated: 2026-04-12
sources: 27
---

## Definition
The AI DRAM Crisis is the global memory shortage that emerged in late 2025 when [[OpenAI]] signed simultaneous non-binding letters of intent (LOIs) with [[Samsung]] and [[SK Hynix]] for approximately 900,000 DRAM wafer starts per month — roughly 40% of global supply. Neither supplier knew about the other's deal. Combined LOI value was estimated by analysts at $71.3 billion over four years. The market treated these non-binding signals as binding demand, triggering a supply panic: competitors rushed to lock in multi-year contracts at peak prices, producers shifted capacity toward DRAM and HBM, and prices spiked 171% year-over-year. The original demand signal was subsequently abandoned — OpenAI cut compute spending by 57%, cancelled Stargate, and shuttered Sora — but the contracts signed during the panic run through 2027–2028, sustaining elevated prices despite collapsed demand. The crisis is not merely a supply-demand imbalance; it is the result of information asymmetry in a three-firm oligopoly responding to a signal that was never meant to be permanent.

## Why It Matters for the Newsletter
The AI DRAM Crisis sits at the intersection of every theme this wiki covers. It is simultaneously a story about market power (three companies control 91.5% of global DRAM; a single buyer can move the entire market), monetary policy (prices for a commodity embedded in every consumer device tripled in under a year), infrastructure (AI buildout is now structurally competing with consumer computing for the same physical production capacity), and political economy (the costs of AI infrastructure speculation are being borne by ordinary PC buyers and small businesses, not by the hyperscalers who triggered the panic). The mechanism — non-binding LOI creating binding downstream effects through panic — is a case study in how signals propagate through concentrated markets and why "non-binding" is often a legal fiction when the counterparty is large enough.

## Evidence & Examples

### The Trigger
- [[OpenAI]] signed simultaneous LOIs with [[Samsung]] and [[SK Hynix]] around October 1, 2025 for ~900,000 DRAM wafer starts/month — see [[OpenAI Stargate 900K DRAM Wafers — TrendForce]], [[OpenAI Orders 71B in Korean Memory Chips — Light Reading]]
- Neither supplier knew the other had received an LOI — classic information asymmetry in a seller-competition dynamic
- Analyst estimate: $71.3 billion in combined contract value over four years — this figure was extrapolated from wafer volume; actual binding commitment was $0 at signing

### Price Impact
- 171% YoY DRAM price surge by Q3 2025 — see [[DRAM Prices Surge 171 Percent YoY — Toms Hardware]]
- 64GB DDR5 kit: $180 (May 2025) → $710 (December 2025) — a 294% increase in 7 months
- 32GB DDR5 kit: under $90 (April 2025) → $400 (April 2026) — see [[Toms Hardware RAM Price Index 2026]]
- HP reported memory now constitutes 35% of PC build cost, up from 15–18% historically — see [[HP Memory Costs 35 Percent of PC Build — Toms Hardware]]

### Downstream Consumer Damage
- Gartner projects the sub-$500 PC market segment will effectively disappear by 2028 — see [[Gartner Memory Costs Reduce PC Smartphone Shipments 2026]]
- IDC projects global PC market contraction of 5–8.9% and smartphone market contraction of 3–5.2%; describes this as "the end of an era of cheap memory" — see [[IDC Global Memory Shortage Crisis Market Analysis 2026]]
- [[Micron]] exited its Crucial consumer brand entirely (December 2025), removing the only US-headquartered competitor from the consumer memory segment — see [[Micron Killing Crucial SSDs and Memory — Toms Hardware]]

### Producer Windfall
- [[Samsung]] Q1 2026 profit: 57.2 trillion won ($37.92B), 8.5x year-over-year; approximately 95% from chips — see [[Samsung Flags Eightfold Jump in Q1 Profit — Reuters]]
- [[Samsung]] became [[Apple]]'s largest DRAM supplier; Apple locked into 2–3 year binding contracts at peak prices — see [[Apple Executives Booking Extended Hotel Stays for DRAM LTA — WCCFTech]]

### Demand Signal Collapse
- February 2026: OpenAI cut compute spending from $1.4T to $600B — a 57% reduction — see [[OpenAI Massively Cuts Spending Plan as Reality Closes In — Futurism]]
- March 2026: [[Stargate]] data center expansion cancelled — see [[Stargate Data Center Expansion Cancelled — Oracle and OpenAI]]
- March 2026: [[Sora]] shuttered — see [[OpenAI Pulls the Plug on Its Sora AI Video App]]
- Samsung shifted 80,000 wafer starts from HBM back to DDR5 in December 2025, possibly signaling internal awareness of demand collapse ahead of public announcements — see [[Samsung HBM DDR5 DRAM Capacity Shift — Digitimes]]

### Relief Timeline
- Structural relief from new fab capacity: mid-2027 at earliest
- Full market correction: 2028, when [[CXMT]] and [[YMTC]] (Chinese DRAM entrants) reach scale and introduce meaningful competition
- Contracts signed at peak prices during the panic run through 2027–2028, sustaining elevated prices even as spot demand collapses

### Published Synthesis
- [[The $71 Billion Bluff]] (The Civic Node, April 11, 2026) — the definitive published synthesis of this crisis; coins the "non-binding LOI → binding downstream panic" framing

## Tensions & Counterarguments

**Intent vs. effect.** OpenAI likely did not intend to create a market panic. The LOIs may have reflected genuine demand projections at the time of signing. But in a three-firm oligopoly with no excess capacity, even earnest signals carry manipulative effects — the market cannot distinguish a sincere projection from a strategic feint. The absence of intent does not reduce the damage.

**Samsung's early knowledge.** Samsung's shift of 80,000 wafer starts from HBM back to DDR5 in December 2025 occurred months before OpenAI publicly announced demand cuts. This could indicate that Samsung had early intelligence about OpenAI's retreating demand — and continued to accept new binding contracts from other customers anyway. If true, this would reframe the crisis as partly a knowing exploitation of information asymmetry rather than a shared mistake.

**Jevons Paradox risk.** Google's TurboQuant paper (March 2026) demonstrated 6x memory compression for LLM inference. This is a demand-side force that could accelerate the price correction — but it could also enable more AI deployments at lower per-unit memory cost, potentially sustaining total demand even as per-model memory needs fall. The net effect on DRAM demand is genuinely uncertain.

**Non-binding ≠ non-consequential.** The legal structure of the LOIs gave OpenAI no binding obligation, but the market's response was binding. This is a structural feature of concentrated markets: in a three-firm oligopoly with long capital planning cycles, a non-binding LOI from a buyer of OpenAI's scale is functionally indistinguishable from a binding order — suppliers must act as if it is real or risk being locked out.

## Related Concepts
- [[Chokepoint Control]] — the three-firm DRAM oligopoly is itself a chokepoint; the crisis illustrates how control of concentrated supply enables both windfall and vulnerability
- [[Chokepoint Economics]] — the mechanism by which market concentration turns information asymmetry into price power
- [[Infrastructure Warfare]] — the AI buildout and the DRAM crisis demonstrate how competition for critical infrastructure components can damage civilian computing as collateral
- [[Jevons Paradox]] — the risk that memory efficiency gains (Google TurboQuant) enable more AI deployments rather than reducing total demand
- [[Semiconductor Supply Chain]] — DRAM is one node in a larger supply chain; the crisis reveals how demand shocks in one segment (AI HBM) propagate to all others (consumer DDR5)

## Key Sources
- [[OpenAI Stargate 900K DRAM Wafers — TrendForce]]
- [[OpenAI Orders 71B in Korean Memory Chips — Light Reading]]
- [[DRAM Prices Surge 171 Percent YoY — Toms Hardware]]
- [[Toms Hardware RAM Price Index 2026]]
- [[HP Memory Costs 35 Percent of PC Build — Toms Hardware]]
- [[Gartner Memory Costs Reduce PC Smartphone Shipments 2026]]
- [[IDC Global Memory Shortage Crisis Market Analysis 2026]]
- [[Micron Killing Crucial SSDs and Memory — Toms Hardware]]
- [[Samsung Flags Eightfold Jump in Q1 Profit — Reuters]]
- [[Apple Executives Booking Extended Hotel Stays for DRAM LTA — WCCFTech]]
- [[OpenAI Massively Cuts Spending Plan as Reality Closes In — Futurism]]
- [[Stargate Data Center Expansion Cancelled — Oracle and OpenAI]]
- [[OpenAI Pulls the Plug on Its Sora AI Video App]]
- [[Samsung HBM DDR5 DRAM Capacity Shift — Digitimes]]
- [[TrendForce DRAM Market Share Q3 2025]]
- [[Memory Shortage Driving Higher Costs — Sourceability]]
- [[The $71 Billion Bluff]]
- [[Sam Altman's Dirty DRAM Deal]]
- [[The Letter That Moved a Market — Medium]]
