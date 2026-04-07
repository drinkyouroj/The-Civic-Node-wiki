---
title: "Focal Point Coordination"
type: concept
tags: [game-theory, cooperation, systems-design, incentives]
created: 2026-04-06
updated: 2026-04-06
sources: 1
---

## Definition

Coordination equilibrium that emerges when participants face a shared threat and repeated interaction, creating a salient ("focal") strategy that stands out psychologically as the obvious choice without explicit agreement or mechanical enforcement.

Identified by economist Thomas Schelling (1960): people coordinate on solutions not because they're contractually obligated but because the context makes coordination so obviously efficient that it becomes the default.

## Why It Matters for the Newsletter

**Game theory assumed maximum adversarial behavior.** Humans cooperate more than pure game theory predicts when facing common threats. This applies to:
- Protocol design (DeFi assumes worst-case Byzantine behavior; empirically less validator misbehavior occurs)
- Organizational design (teams with shared external threats show higher cooperation than predicted)
- Systems resilience (shared threat creates focal point for coordination better than most enforcement mechanisms)

## Evidence & Examples

### The Classic Example: Schelling Points in Cities

**The Setup**: Two strangers are told to meet in New York City tomorrow but given no other instructions. No phone, no prior agreement, no enforcement mechanism.

**The Reality**: Most pick Grand Central Terminal at noon.

**Why**: Not because it's physically central (it isn't) or because they're psychic. Because that location + time are psychologically salient. They stand out as obvious from infinite alternatives.

### ARC Raiders (October 2025)

**The Setup**: Extraction shooter (kill-on-sight economy, zero-sum resource scarcity). Game financially rewards you for looting player corpses.

**The Prediction**: Maximum PvP conflict (like Rust, DayZ, Tarkov—extraction shooters with toxicity so concentrated it could strip paint).

**The Reality**: Players cooperate. Embark Studios CEO: "We got some figures on how many people have been downed by another player, and they were surprisingly low."

**Why**: ARCs (killer robots) are threatening enough that "don't shoot the human trying to survive ARCs" becomes the salient solution. Alternative (fight robots + humans simultaneously) is obviously worse. Cooperation emerges without explicit agreement.

**The Mechanic**: Aggression-based matchmaking (frequent killers matched with killers, peaceful looters with peaceful looters) made the focal point explicit. Two different games running on same infrastructure—one following designed mechanics, one following human behavior.

### World of Warcraft PvP Servers (2004)

**The Setup**: Enemy factions can kill each other. Difficult raid content requires cooperation.

**The Reality**: Informal truces emerged (shared threat = focal point for temporary alliance).

### Eve Online Null-Sec (2003-present)

**The Setup**: Economy runs on theft, betrayal, piracy. Paradoxically, existential threats to the region create coalitions.

**The Pattern**: When external threat emerges, rivals form alliances despite the economic structure rewarding betrayal. Shared threat creates focal point stronger than individual incentives.

## How This Works in Design

**Three requirements**:
1. **Repeated interaction**: One-shot prisoner's dilemmas don't produce cooperation. Repeated games reward reputation-building strategies (tit-for-tat).
2. **Shared threat**: Something worse than mutual defection. ARCs worse than other players. Raid bosses worse than PvP death. External regulator worse than internal cheating.
3. **Psychological salience**: Solution must be obvious (not require explicit negotiation). "Team up against the robots" is salient. "Form coalition 3.7" is not.

**Focal point beats pure logic**: Analytics models say defect. Context says cooperate. Context wins.

## Tensions & Counterarguments

**Defense (game theory)**: Assumes worst-case. Better to be safe.

**Counter**: Overestimating adversarial behavior in cooperation-aligned contexts imposes massive costs. Proof-of-work energy waste, smart contract brittleness, organizational exhaustion from assuming bad faith. Focal point coordination suggests designing for shared goals first, cryptographic safeguards for the minority who defect.

**Defense**: Shared threats are temporary. Once threat disappears, cooperation collapses.

**Counter**: True for manufactured threats. Less true for structural threats (regulators, competing networks, technical failures). Crypto protocols face permanent adversarial pressure. That creates permanent focal point for cooperation among participants with aligned interests.

## Related Concepts

- [[published/Game Theory Assumes You're a Sociopath. You're Not.]] — detailed exploration
- [[Cooperative Equilibrium]] — stable strategy where repeated interaction + focal point sustains cooperation
- [[Shared Threat as Coordination Mechanism]] — how external pressure enables implicit agreements

## Key Sources

- [[published/Game Theory Assumes You're a Sociopath. You're Not.]] — comprehensive framework
- Thomas C. Schelling, *The Strategy of Conflict* (1960)
