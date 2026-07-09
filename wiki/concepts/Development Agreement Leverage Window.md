---
title: "Development Agreement Leverage Window"
type: concept
tags: [infrastructure, energy, legal, ai]
created: 2026-06-09
updated: 2026-06-09
sources: 8
---

## Definition

The decision a community makes about a data center is split across two venues that decide different things on different timelines.

The **local body** (city council, county commission, redevelopment commission) decides whether the project gets built — through zoning, tax abatement, water and sewer service, and the development agreement. The **state utility commission** decides who pays for the grid the project needs — through the rate case, often a year or more later.

The community's leverage is concentrated in the first venue and nearly absent in the second. The development agreement is the one document where a locality can attach enforceable cost protections, because approval is conditional and the developer needs it. Once the local body votes yes, the cost-allocation question moves to a venue where the town has no standing beyond petitioning to intervene, and where it is one voice in a proceeding it does not run.

The window is the gap between the local approval and the rate case. Cost protections attached before the vote can be made binding; the same protections sought after the vote depend on a regulator the town does not control. The mechanism generalizes beyond formal "development agreements" to any discretionary local approval (a rezoning, a tax-abatement vote) where the build decision precedes the cost decision and lives in a different room.

## Why It Matters for the Newsletter

This is the procedural reason data-center cost fights feel rigged to the people paying for them. The venue that decides their bill is the state rate case, which they cannot see and do not attend. The venue they *can* influence — the local council meeting — decides the build, not the bill. By the time the cost lands on the ratepayer, the leverage that could have blocked it is already spent.

For a TCN reader, this reframes [[AI Cost Incidence]] from a pricing question into a timing-and-venue question. "Who pays for AI's grid buildout" is settled less by whether the rules are fair than by *when and where* the rules get written, and whether anyone with leverage was in the room. It also explains why plain-English disclosure at the local level is load-bearing rather than a courtesy: it is the only thing that lets a council use its leverage while it still holds it. A disclosure that arrives after the vote informs residents about a decision they can no longer shape — the same timing failure that defines [[Toothless Transparency Laws]], in a different register.

The newsletter angle: a piece that follows a single local approval through to the rate case it triggers, showing the town go from holding the one card the developer wants to becoming just another name on the rate roll.

## Evidence & Examples

- **[[El Paso Electric]] / Meta "bridge period"** — Meta pays the incremental cost of its 366 MW gas plant for 1–5 years, then the cost shifts to ratepayers. A cost protection negotiated at the front end but written to expire. The leverage window closed with a deal that handed costs back downstream. [[El Paso Electric Filings on Meta $10B Data Center — El Paso Matters - 2026-03-29]]
- **[[AEP Ohio]] / Meta New Albany** — the data-center large-load arrangement (pay for reserved capacity whether used or not, with exit fees) runs through the Ohio commission (PUCO), not New Albany's council. The cost structure Justin cited in the field as the "good" outcome was set at the *state* venue. A local body could not have replicated it on its own.
- **[[Virginia SB 253]]** — the cost-allocation question handled entirely at the state level: the legislature plus the State Corporation Commission moving distribution and capacity costs onto the data-center (GS5) rate class, reaching existing load through 2033. The locality is not the decider; the state is. [[Bill Would Put More Energy Costs on Data Centers — Virginia Mercury - 2026-02-10]]
- **Michigan / [[DTE Energy]]** — [[Saline Township Data Center (The Barn)]] (>1 GW, ~25% of DTE peak) was approved locally well before the MPSC rate case that decides whether its revenue offsets household bills. The build venue and the cost venue ran on separate clocks, exactly as the model predicts. [[Michigan Data Centers Could Hike Your Power Bill — Planet Detroit - 2025-10-16]]

## Tensions & Counterarguments

- **The window is not a hard zero after the vote.** Localities can sometimes petition to intervene in rate cases, and state AGs (Dana Nessel in Michigan) fight cost-shifting at the commission after the fact. Post-approval leverage is much weaker, not nonexistent. Don't overclaim "the town has no recourse."
- **Inter-locality competition bounds the leverage.** A town that demands too much in the development agreement can push the project to a friendlier jurisdiction. The leverage is real but capped by the developer's option to build elsewhere — the same dynamic that lets hyperscalers extract tax abatements.
- **By-right builds skip the window entirely.** Where a data center can be built on existing industrial zoning without a discretionary approval, there is no leverage window to use. The model assumes a discretionary local gate.
- **[[Speed to Power]] bypasses both venues.** Behind-the-meter / off-grid builds skip the interconnection queue *and* the rate case, which removes even the downstream check. There the local approval may be the only venue that ever scrutinizes the project at all.

## Related Concepts

- [[AI Cost Incidence]] — parent concept; this is the venue-and-timing structure underneath the who-pays question.
- [[Toothless Transparency Laws]] — disclosure that exists but arrives after the decision point; the same timing failure in a statutory register.
- [[Speed to Power]] — the build pattern that bypasses both venues, removing the rate-case check.
- [[Regulatory Weaponization]] / [[Institutional Capture]] — adjacent governance dynamics that shape who is in the room when the cost rules get written.

## Key Sources

- [[Bill Would Put More Energy Costs on Data Centers — Virginia Mercury - 2026-02-10]]
- [[El Paso Electric Filings on Meta $10B Data Center — El Paso Matters - 2026-03-29]]
- [[Michigan Data Centers Could Hike Your Power Bill — Planet Detroit - 2025-10-16]]
- [[DTE Ties Future Rate Freeze to Data Centers — Planet Detroit - 2026-04-24]]
