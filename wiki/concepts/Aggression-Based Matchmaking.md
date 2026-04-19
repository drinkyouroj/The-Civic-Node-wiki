---
title: "Aggression-Based Matchmaking"
type: concept
tags: [technology, game-design, cooperation, algorithmic-governance]
created: 2026-04-17
updated: 2026-04-17
sources: 5
---

## Definition

A matchmaking system that sorts players into lobbies based on their observed propensity toward PvP (player-versus-player combat) versus PvE (player-versus-environment) play. Rather than matching purely on skill (K/D ratio, rank), the system infers a behavioral type from prior match history and attempts to place players with others who share that orientation. Documented production implementation: [[Embark Studios]]' [[Arc Raiders]], confirmed by CEO [[Patrick Söderlund]] in a Games Beat interview and reported in PC Gamer.

## Why It Matters for the Newsletter

Aggression-based matchmaking is a live, shipped example of algorithmic behavioral classification at consumer scale. Embark has built infrastructure that:

1. Observes player behavior continuously
2. Infers a moral-adjacent characteristic (propensity toward violence against other players)
3. Acts on that inference without disclosure or appeal — sorting players invisibly into different lobby pools

That is the architecture of algorithmic governance in miniature. The scale is trivial (game lobbies) but the pattern is the same one that will define consequential domains: insurance, employment, credit, content moderation, immigration. When commentators wave away concerns about behavioral-sorting algorithms as speculative, Arc Raiders is a concrete counterexample — the system exists, it is deployed, and it is working.

It also matters on its own terms for the newsletter's [[Cooperative Game Design]] coverage and for game-theory pieces. Arc Raiders' cooperative player culture exists partly *because* the aggression-based matchmaking funnels predators away from non-predators — the pro-social equilibrium is algorithmically maintained, not organic.

## Evidence & Examples

- **Söderlund confirmation**: "We introduced a system where we also matchmake based on how prone you are to PvP or PvE. So if your preference is to do PvE and you have less conflict with players … you'll get more matched up [with that sort of play]. Obviously, it's not a full science." [[Arc Raiders aggression-based matchmaking — PC Gamer]]
- **Observed effects**: PC Gamer writer Morgan Park, with fewer than 15 kills in 50+ hours, reports "chill and blood-quenched" lobbies; other players describe "cold and bloody" experiences — evidence of behavioral sorting in action.
- **Map-level modulation**: Certain maps (notably Stella Montis) are reported to host more PvP-inclined players — suggesting the sorting interacts with map-level behavior.

## Tensions & Counterarguments

- **No disclosure or appeal**: Players don't see their aggression score; they can't contest it; they can't opt into a different bucket. This is the exact structural problem critics raise about algorithmic governance in higher-stakes domains.
- **Fairness critique**: Some players feel "unfairly judged" or "penalized" for making the valid game-mechanical choice to kill opponents.
- **Sorting vs. suppression**: Is aggression-based matchmaking moderating behavior, or just segregating it? The predators still play predator lobbies — the system contains the dynamic rather than reducing it.

## Related Concepts

- [[Cooperative Game Design]] — broader design philosophy
- [[Algorithmic Sorting]] — behavior-classification systems more broadly
- [[Algorithmic Governance]] — the stakes when this pattern scales

## Key Sources

- [[Arc Raiders aggression-based matchmaking — PC Gamer]]
- [[Arc Raiders devs uplifted by player kindness — PC Gamer]]
