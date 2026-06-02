---
title: "AI Cost Incidence"
type: concept
tags: [infrastructure, power, ai, politics, monetary-policy]
created: 2026-05-18
updated: 2026-06-02
sources: 10
---

## Definition

AI Cost Incidence names the question of where the cost of the AI buildout actually lands on the income statement of the economy. Hyperscaler capex is the visible side, but the AI buildout is also generating costs that show up in (a) household electricity bills via capacity-market price increases, (b) state-level subsidy and tax-abatement transfers, (c) labor-cost increases at chokepoint supply layers, and (d) ratepayer-funded transmission expansion. The incidence question is who pays for AI infrastructure when the bill arrives, not just who builds it.

## Why it matters for the newsletter

Incidence is the structural complement to the [[AI Windfall Sharing]] concept. Where windfall sharing asks who captures the upside, incidence asks who absorbs the cost. The two together describe the full distributional politics of the AI capex boom — and the cost side is the one already showing up on household statements while the windfall side is still mostly in operating-profit forecasts.

## Evidence & examples

- [[PJM Interconnection]] Q1 2026 capacity-market: combined revenue increase from inclusion of existing+forecast data center load across the 2025/2026 + 2026/2027 + 2027/2028 BRAs was **$23,100,955,341**. Of that, **$13,768,851,483 landed on customer bills** across the 2026/2027 and 2027/2028 BRAs even with the "Agreement" VRR-curve cap in place. Without the Agreement, the impact would have been $26.85B (the cap reduced it by $13.08B). [[Quarterly State of the Market Report for PJM Q1 2026 — Monitoring Analytics - 2026-05-14]]
- [[PJM Interconnection]] Q1 2026 total wholesale power: $77.78/MWh → $136.53/MWh (+75.5% YoY); total PJM gross billing $18.69B → $36.35B (+94.5%). Cost incidence falls on residential and commercial ratepayers, not hyperscalers. [[Quarterly State of the Market Report for PJM Q1 2026 — Monitoring Analytics - 2026-05-14]]
- Maryland: residents projected to pay $1.6B more in power bills due to out-of-state data centers [[US Electric Grid Heading Toward Crisis Data Centers — Common Dreams - 2026-01-02]]
- New York: 1.6 GW grid shortage projected by 2030, largely due to data centers [[US Electric Grid Heading Toward Crisis Data Centers — Common Dreams - 2026-01-02]]
- Bipartisan affordability framing (Sanders and DeSantis) signals that the incidence question crosses partisan lines [[US Electric Grid Heading Toward Crisis Data Centers — Common Dreams - 2026-01-02]]
- Rob Gramlich (Grid Strategies) prediction: 2026 elections will amplify affordability messaging [[US Electric Grid Heading Toward Crisis Data Centers — Common Dreams - 2026-01-02]]
- **Chip-layer incidence — where the labor windfall actually lands (NOT on customers).** The Samsung/[[SK Hynix]] profit-share deals are structured as a percentage *of* operating profit (10.5% / 10%), paid partly in stock and contingent on hitting OP targets — "a distribution of earnings, not an upfront cost burden" [[Samsung Strike Risk Gone Now the Real Test Is HBM — Investing.com - 2026-05-27]]. Because it is a profit-share, not a per-unit cost, it does **not** mechanically inflate marginal cost or flow through to chip prices. Its incidence falls on **shareholders and reinvestment headroom**: SK Hynix's combined shareholder + employee rewards rose ~**+450% YoY to ~100T won** in 2026 while CAPEX + R&D grew only +20–30% — the rewards crowd out the spending "directly tied to future competitiveness" [[SK Hynix 100 Trillion Won Reward Burden — Seoul Economic Daily - 2026-05-05]]. The margin-compression estimate: JPMorgan's Jay Kwon put full union demands at a **7–12% downside to Samsung's 2026 OP** [[Samsung HBM Strike Could Wrench AI Boom — Fortune - 2026-05-17]].

## Tensions & counterarguments

- The hyperscaler defense: capacity-market price increases benefit ratepayers in the long run because they signal scarcity and pull new generation onto the grid. The counter is that the generation lag (multi-year) means ratepayers pay first and benefit (if at all) much later — a regressive timing structure.
- The IMM's own response (Q1 2026 SOM): "This simplistic view ignores the fact that it is the unexpected addition of extraordinarily high levels of data center load (largely based on unsubstantiated forecasts) that have resulted in the supply-demand imbalance." The IMM rejects the "let prices rise, supply will follow" framing as ignoring the forecast-quality problem at the demand layer. [[Quarterly State of the Market Report for PJM Q1 2026 — Monitoring Analytics - 2026-05-14]]
- The IMM's preferred remedy (BYONG — "Bring Your Own New Generation") explicitly addresses incidence: data centers must bring their own generation OR commit to curtailability prior to current demand-side customers. The IMM frames any backstop-auction alternative as risk-shifting from data centers onto residential / commercial / industrial ratepayers. [[Quarterly State of the Market Report for PJM Q1 2026 — Monitoring Analytics - 2026-05-14]]
- A second counter: hyperscaler corporate taxes paid to the same states partly offset the ratepayer transfer. Empirical question of whether the offset is meaningful at the household level (vs. flowing to state general funds). This is an open research question for the wiki.
- Off-grid hyperscaler campuses (see [[Speed to Power]] and Oracle Project Jupiter) bypass the ratepayer-incidence mechanism entirely but raise different incidence questions (local water, air quality, local permitting subsidies).
- **The chip-cost pass-through is a strategic choice, not an accounting flow.** It is tempting to argue the Samsung labor claim is "passed through" to hyperscalers in memory prices — but because the bonus is profit-contingent, nothing forces that. Samsung *could* use its chokepoint pricing power (70% DRAM, HBM sold out) to rebuild the shared margin, and memory contract prices are rising sharply in 2026 (HBM3E +~20%; conventional DRAM +58–63% QoQ) — but those increases are demand-driven (Nvidia/ASIC), not attributable to the labor deal. So any claim that hyperscalers "pay for" the worker bonuses is the writer's inference about pricing-power behavior, and must be named as such — not asserted as a cost flow. This is the chip-layer analog of the electricity-side timing asymmetry above.

## Related concepts

- [[AI Windfall Sharing]] — the upside-distribution companion
- [[AI Buildout Grid Constraint]]
- [[Chokepoint Control]]
- [[Cantillon Effect]] — adjacent monetary-policy framing

## Key sources

- [[Quarterly State of the Market Report for PJM Q1 2026 — Monitoring Analytics - 2026-05-14]] — primary source for all $13.77B / $23.10B / $26.85B figures
- [[AI Data Center Demand 76 Percent Surge East Coast Grid — SOFX - 2026-05-15]]
- [[US Electric Grid Heading Toward Crisis Data Centers — Common Dreams - 2026-01-02]]
- [[SK Hynix 100 Trillion Won Reward Burden — Seoul Economic Daily - 2026-05-05]] — chip-layer incidence: rewards (+450%) crowding out CAPEX/R&D (+20–30%)
- [[Samsung Strike Risk Gone Now the Real Test Is HBM — Investing.com - 2026-05-27]] — the profit-contingent-distribution (not per-unit-cost) structural point
