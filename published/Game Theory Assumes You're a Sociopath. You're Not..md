---
title: "Game Theory Assumes You're a Sociopath. You're Not."
source: "https://drinkyouroj.substack.com/p/game-theory-assumes-youre-a-sociopath"
author:
  - "[[Justin Hearn]]"
published: 2026-02-05
created: 2026-04-06
description: "What happens when you give players a choice between shooting strangers and shooting fascist mechs? They pick the mechs. Every time."
tags:
  - "clippings"
---
### What happens when you give players a choice between shooting strangers and shooting fascist mechs? They pick the mechs. Every time.

## The Spark: Designing for Bloodbaths, Getting Cooperation Instead

Last week I bought ARC Raiders expecting a bloodbath. Thirty-minute raids into robot-controlled hellscape, grab loot, extract before you die, murder anyone who gets in your way. Standard extraction shooter economics: your death equals my profit, your corpse equals my payday. Kill or be killed.

Players cooperated anyway.

Not because the game rewarded it. Because the game made killing other humans *optional* while making killer robots *mandatory*. Turns out when you give people a choice between shooting strangers and shooting fascist mechs, they pick the mechs. Every time.

![Armed players in tactical gear working together against large hostile robots in a devastated industrial environment](https://substackcdn.com/image/fetch/$s_!HiSo!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3b85998e-4afa-4170-9aac-d97d99e9bcd0_2048x1168.png)

Murder was profitable. Cooperation happened anyway. Game designers are still confused.

Within weeks of the October 2025 launch, Embark Studios CEO Patrick Soderlund admitted something had broken their model. “We got some figures on how many people have been downed by another player, and they were surprisingly low.” [^1] Surprisingly low. The game financially rewards you for looting player corpses. Resource scarcity creates competition. Extraction points become chokepoints. Every human encounter sets up a prisoner’s dilemma where shooting first means survival.

But the community looked at those incentives and said: nah.

So Embark implemented “aggression-based matchmaking.” [^2] Frequent player-killers get matched with other player-killers. Peaceful looters get matched with other peaceful looters. The system now explicitly creates two parallel games running on the same infrastructure. One game follows the designed mechanics. The other follows actual human behavior despite those mechanics.

This isn’t a bug report about one game. This is observable data about what happens when system designers assume humans default to maximum violence, then give those humans a compelling reason not to.

## The Pattern: What Every Designer Missed About Common Enemies

Game designers spent the last fifteen years manufacturing conflict like it was the only spice in the cabinet. The logic made sense: conflict creates tension, tension creates engagement, engagement creates retention, retention creates revenue. Build scarcity into the world, add anonymity to interactions, watch players tear each other apart. Economics 101 meets Lord of the Flies.

DayZ pioneered this in 2013. Rust refined it. Escape from Tarkov turned it into a doctoral thesis on why trusting strangers gets you killed. These games created laboratories for studying human behavior under specific conditions: limited resources plus zero accountability equals violence. The “kill on sight” meta became dogma. Trust another player? You might as well paint a target on your back and ring a dinner bell.

For years, the data supported this. Rust became famous for toxicity so concentrated it could strip paint. DayZ spawned an entire culture around betrayal montages. The extraction shooter genre evolved to make this even more explicit. Hunt: Showdown (2018) and Tarkov both built progression systems where taking resources from corpses wasn’t just permitted but *necessary*. Zero-sum by design.

Pattern seemed clear: design for predation, get predators. Create zero-sum environments, cooperation dies. Game theory confirmed.

Except the pattern was missing a variable. What those earlier games didn’t include was a threat big enough to make strangers more valuable alive than dead.

In Rust, other players are the only meaningful threat. Buildings decay slowly. Animals are ambient danger. The real game is human versus human because nothing else poses enough risk to justify cooperation. Same with DayZ: zombies exist but they’re mostly set dressing. The danger is other players, so other players become targets.

ARC Raiders changed the equation by accident. The ARCs aren’t ambient danger. They’re genuinely difficult, genuinely lethal, genuinely expensive to fight alone. A well-geared player can handle maybe two or three ARCs solo if they play perfectly. A zone crawling with six or eight ARCs? You need help. The shared threat creates a **focal point** — a concept economist Thomas Schelling identified in 1960 to explain how people coordinate without explicit communication.[^3]

![Split-screen comparison showing player-versus-player combat in Rust on left versus cooperative player teamwork against robots in ARC Raiders on right](https://substackcdn.com/image/fetch/$s_!WTCE!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F84a8384d-c307-4a98-8066-47cd58a61e74_2048x1168.png)

Left: what designers expected. Right: what players actually did.

Focal points work because humans are shockingly good at implicit coordination when context provides an obvious Schelling point. Classic example: if you tell two strangers to meet in New York City tomorrow but don’t specify where or when, most pick Grand Central Terminal at noon. Not because they’re psychic. Because that location and time are *obvious* in a way that stands out from infinite alternatives.

In ARC Raiders, “don’t shoot the other human trying to survive killer robots” becomes the obvious Schelling point. The game gives you room to defect, but cooperation is so clearly efficient that players coordinate on it without explicit agreement. No voice chat needed. No formal alliance system. Just two people who look at a squad of murder-bots and think: yeah, I’d rather not fight those *and* a human simultaneously.

This isn’t even the first time designers have seen this happen. World of Warcraft’s PvP servers created informal truces in 2004 when opposing factions needed to complete difficult raid content. Eve Online’s null-security space regularly spawns temporary alliances against existential threats despite the game’s economy literally running on theft and betrayal. Even Tarkov added “Fence rep” mechanics in 2021 to discourage player-killing after years of community feedback about excessive spawn-camping ruining the experience.

The pattern that keeps surfacing: players don’t naturally default to maximum aggression when cooperation offers better outcomes. They assess costs. They calculate benefits. They build informal social contracts even in systems offering zero mechanical enforcement.

So why do designers keep building systems that assume maximum conflict?

## The Protocol: What Happens When Focal Points Beat Pure Logic

ARC Raiders accidentally generated empirical evidence about mechanism design that matters beyond gaming. Specifically: humans cooperate more than pure game theory predicts when systems give them aligned incentives and room to choose.

Most blockchain protocols operate on cryptographic proof instead of social trust because designers assume maximum adversarial behavior. Bitcoin’s security model assumes miners act selfishly, so it aligns selfish behavior (mining for block rewards) with network security (validating transactions). Ethereum’s proof-of-stake assumes validators will misbehave if profitable, so slashing conditions punish Byzantine faults. These assumptions work. Cryptographic guarantees prevent catastrophic failures.

But they impose massive costs. Computational waste in proof-of-work. Capital lockup in proof-of-stake. Reduced flexibility in smart contract design. We build systems assuming the worst because we’ve been told game theory demands it.

What if that assumption overestimates adversarial behavior in contexts where participants share common goals?

![Infographic diagram comparing traditional adversarial game theory model with prisoner's dilemma on left to cooperative focal point coordination model on right](https://substackcdn.com/image/fetch/$s_!joAf!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F23c57e6e-9c2e-459b-a785-3e893990c0e6_2752x1536.png)

Economists build models assuming you’ll stab your neighbor for a nickel. Humans keep not doing that.

The prisoner’s dilemma models the basic problem: two suspects get interrogated separately, each can defect (snitch) or cooperate (stay silent). Rational self-interest says defect. Both defect, both get medium sentences when they could’ve walked free with mutual cooperation. Classic game theory says this is inevitable without enforcement mechanisms.

But repeated prisoner’s dilemmas, where the same players interact multiple times, produce different results. Tit-for-tat strategies emerge. Reputation matters. Players learn that cooperation today enables cooperation tomorrow. The folk theorem in game theory proves that indefinitely repeated games can sustain cooperative equilibria even when one-shot versions can’t.[^4]

ARC Raiders creates exactly this condition: repeated interactions where today’s cooperation signals future trustworthiness. Kill another player once, you get their loot. Cooperate consistently, you build implicit reputation with the player base, making future raids safer and more profitable.

Now add Schelling’s focal points to this repeated game structure. Focal points are coordination equilibria that stand out from other possibilities because of psychological salience, not mechanical enforcement. In ARC Raiders, “team up against the robots” is salient because the alternative (fight robots AND humans) is obviously worse for everyone except the occasional psychopath who enjoys maximum difficulty.

The combination creates what we might call cooperative focal point equilibrium: a stable strategy where players coordinate on cooperation not through explicit agreement or mechanical force, but through obvious mutual benefit plus repeated interaction building implicit trust.

Look at existing decentralized systems through this lens. Proof-of-stake networks experience significantly less validator misbehavior than security models predict. Most DeFi protocols never see the maximum extractable value attacks their threat models assume. DAOs consistently show higher voter participation and better governance than pure rational-actor models suggest possible.

Not because crypto users are uniquely virtuous. Because they face common enemies: regulators threatening the ecosystem, competing networks trying to capture market share, technical failures that could destroy everyone’s holdings. Shared threat plus repeated interaction creates focal point coordination toward cooperation.

This suggests a design principle: build systems that enable and reward cooperative behavior when participants have aligned goals, while maintaining cryptographic safeguards against the minority who will always defect. Don’t assume maximum aggression as baseline. Assume cooperation is possible when context makes it efficient, and build mechanisms making it the obvious choice.

The extraction shooter genre taught us scarcity plus anonymity equals violence. ARC Raiders teaches us scarcity plus anonymity plus common threat equals cooperation. That third variable changes everything.

![Abstract visualization of decentralized network nodes with blue connections forming defensive coordination pattern against external red threat](https://substackcdn.com/image/fetch/$s_!dpa4!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe0435ce-13dc-484d-8893-7e26d8bc95b9_2048x1168.png)

When the threat is big enough, strangers stop acting like strangers. Cryptography didn’t account for this.

## Personal Code: Institutions Failed, Humans Didn't

I’ve spent most of the last eighteen months rebuilding after cascading system failures. Family, psychiatric, financial, the works. What I learned maps directly onto what’s happening in ARC Raiders: people cooperate when the alternative is worse, even when systems tell them competition is optimal.

When institutions failed me in late 2023, rational strategy said trust nobody. Hoard resources. Assume everyone will defect because that’s what incentives predict. But actual behavior looked different. People offered help without prompting. Strangers shared resources. The common enemy — systems treating humans as interchangeable failure modes — created informal mutual aid networks that had no business existing according to standard models.

ARC Raiders players choosing cooperation despite design pushing them toward PvP feels familiar. They’re running the same calculation I did: immediate payoff from defection (kill another player for loot, refuse help to protect resources) is smaller than long-term benefit from cooperation (take down ARCs together, build informal networks reducing everyone’s risk).

Systems assume we’ll behave like rational sociopaths because that’s the safe assumption for designers. Build for worst case, never be surprised. But that assumption costs us. We get protocols requiring massive energy consumption, governance structures assuming bad faith, social systems enforcing isolation as default.

I don’t know if there’s a better way to build systems enabling cooperation without exploitation by defectors. That’s the hard problem. But our current approach — assume maximum adversarial behavior, design for pure conflict — leaves value on the table. ARC Raiders proved that given good reason to cooperate and room to choose, many people will. Even when systems tell them not to.

Maybe the design principle we’ve been missing: give people a common enemy worth fighting; they’ll build the cooperation the system forgot to include.

1 Like

[^1]: [PC Gamer: Arc Raiders devs uplifted by player cooperation](https://www.pcgamer.com/games/third-person-shooter/arc-raiders-devs-are-uplifted-by-how-kind-players-have-been-to-one-another-but-admit-were-way-worse-people-than-the-community-when-it-comes-to-engaging-in-pvp/)

[^2]: [PC Gamer: Arc Raiders aggression-based matchmaking](https://www.pcgamer.com/games/third-person-shooter/arc-raiders-contentious-aggression-based-matchmaking-isnt-just-smart-but-absolutely-necessary/)

[^3]: [Thomas C. Schelling,](https://www.sackett.net/Strategy-of-Conflict.pdf) *[The Strategy of Conflict](https://www.sackett.net/Strategy-of-Conflict.pdf)* [(Cambridge: Harvard University Press, 1960), 54-58](https://www.sackett.net/Strategy-of-Conflict.pdf)

[^4]: [Drew Fudenberg and Jean Tirole,](https://www.google.com/books/edition/Game_Theory/pFPHKwXro3QC?hl=en&gbpv=0) *[Game Theory](https://www.google.com/books/edition/Game_Theory/pFPHKwXro3QC?hl=en&gbpv=0)* [(Cambridge: MIT Press, 1991), 150-151](https://www.google.com/books/edition/Game_Theory/pFPHKwXro3QC?hl=en&gbpv=0)