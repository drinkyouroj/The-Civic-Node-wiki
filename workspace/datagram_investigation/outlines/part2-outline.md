# Part 2: The Gap Between the Map and the Territory

**Working title**: "William Did One Thing and Andy Tried to Make Sense of It All"
*(from Kyle's Jan 2 meeting: "we need to get dev all working in lockstep with each other, rather than William doing one thing and Andy trying to make sense of it all")*

**Template**: System Audit — Section 2 "The Source Code" (root causes of the gap)
**Target length**: 1,500–1,600 words
**Tone**: More analytical than Part 1. Still grounded in specific events, but pulling back to show the pattern.

---

## The Core Argument

The gap between Datagram's public narrative and its internal reality wasn't a failure of communication — it was a structural feature. The mods were the buffer. They were told enough to answer questions, not enough to ask the right ones. And when they ran into the ceiling of what they knew, they were handed a script.

---

## Section 1: The Glitch (~400 words)

### The VPN Pivot

The original Datagram pitch was decentralized real-time communication — video conferencing, AI workloads, gaming infrastructure. At some point, without a public product announcement or community vote, the project became primarily about a VPN product.

Walk through what this looked like from the outside:
- Community members started asking why a "stealth app upgrade" had made VPN mandatory
- Quote from general chat: *"why this stealth app upgrade that made VPN mandatory, i don't want VPN on my node, why i can't turned off?"*
- The mod team found out about VPN through the same public-facing documents as the community

Kyle's Jan 2 meeting with Justin is the key source here. This was a 45-minute meeting on January 2, 2026 — two weeks before Jason's departure — in which Kyle was trying to build a VPN FAQ. The transcript reveals what the mods actually knew:

> "I'm fifty percent certain of just about everything I'm doing these days."

> "There's a lot of [William and Andy] going on right now behind the scenes... we're supposed to kind of prepare to ship this product and I don't really have any sort of bearing on what the timing will be, how it's going to work exactly."

> "Chris's knee-jerk, quote-unquote, marketing efforts are probably creating a lot more problems for us down the line with the community than they solved."

The mods were being asked to educate a community about a product they themselves only half understood, based on documents William had written, while William and Andy were internally fighting over whether to build it correctly or cheaply.

**SOURCE**: Kyle/Justin meeting transcript (Jan 2, 2026), general-chat Discord logs (VPN complaints)

### ⚠️ SOURCING GAP — Needs interview:
- **Jason**: When exactly did he learn about the VPN pivot? Was he consulted? Did he push back?
- **Kyle**: What specifically was he told about the VPN in the team meeting he references? Who was in that meeting?

---

## Section 2: The Source Code (~500 words)

### The Chain of Information (and Where It Broke)

Reconstruct the actual information flow: William → Jason → Chris/Kyle → Mods → Community.

At each step, something was lost or withheld:

**William → Jason**: Jason had theoretical authority over the product roadmap. In practice, William would receive Jason's plans and implement something different — or announce something entirely new. The VPN is one example. The accent-judging AI that Kyle mentions in the Jan 2 transcript is another: *"him running off and using forty percent of dev resources to build out an AI that judges your accent."* Jason had to spend significant energy, per Kyle, "making sure William doesn't run with scissors" — *"curtailing his worst impulses... making sure he's got a knuckle-white grip on the bungee cord."*

**Jason → Chris/Kyle**: By January 2, Kyle knew the project was in financial trouble but couldn't say how bad. He was explicitly told the mods would be taken care of — *"I've been told in the sincerest of ways that we will be taken care of"* — but couldn't give specifics because he didn't have them.

**Chris/Kyle → Mods**: The mod team received instructions to handle community frustration, answer questions with available materials, and not speculate. When the capsule disaster happened on Thanksgiving, the instruction was: *"make it clear that our hands are tied and we CANNOT manually change this."* When Jason stepped back in January, the instruction was: *"The announcement speaks for itself, and we can't really comment on it."*

**Mods → Community**: The community received whatever the mods knew, filtered through whatever the mods were allowed to say.

### The "Finance Overlords"

The payment timeline for moderators is a microcosm of this structure. Chris processed payments to mods, but he was dependent on an unnamed "finance" layer above him. His own messages to the mod team show the pattern:

- April 1, 2025: *"submitting payments tmrw, expect it to be done in 72ish"*
- April 5: *"Was submitted, still at finance. Will ping everyone once I send the final payments"*
- April 8: *"I'm awaiting for finance to transmit payments to me so I can disperse them to you"*
- April 8: *"Don't beat me, the finance overlords are at fault"*
- May 10: *"yes I know payments are late, I'm sorry for that pushing finance... Outside of my control, we live at the mercy of the finance overlords"*

Chris collected, submitted, and dispersed. He did not control. Above him was "finance." That layer has now been identified: **Richard Han** (also known as Yu te Han), affiliated with **Vina Capital**, the firm that invested in Datagram. Chris confirmed in April 2026 that Richard held no formal title at Datagram but was functionally the highest decision-making authority — and that Jason had no power over payments whatsoever. *"All payments were handled by Richard."*

Richard is not named in any public-facing Datagram document. He does not appear in the whitepaper, the announcements channel, or any community update. He was entirely invisible to the community while controlling the money.

**SOURCE**: Mod-discussion logs (payment timeline), Kyle/Justin meeting transcript, Chris DM (April 2026 — both sets of follow-up answers)

### ⚠️ SOURCING GAPS — Needs interview:
- **Jason**: Confirm the pattern of submitting plans that William then ignored. Specific examples beyond VPN and accent AI.
- ~~**Chris**: Who exactly is "finance"? Is that Richard? What was Richard's actual title/role?~~ ✅ RESOLVED — Richard Han / Yu te Han, Vina Capital, no formal title
- **Kyle**: Who was in the team meeting he references on Jan 2? What specifically was said about finances?

---

## Section 3: The Upgrade (Withheld — "The Script") (~400 words)

### What the Mods Were Told to Say

This section documents the gap between internal knowledge and public-facing language — the specific moments when the mod team was given a script.

Three documented instances:

**1. The Thanksgiving Capsule Disaster (November 28, 2025)**
Korean mod jini_8002 reports that the claiming window had already closed before 48 hours elapsed, and that a bug had been running the entire time. Kyle's instruction to the mod team that morning:
> *"Work with the announcement that Jason made to communicate the situation and to make it clear that our hands are tied and we CANNOT manually change this."*

Jason's public statement: *"For those of you that missed it, that is unfortunate but this is an automated process and not something we can manually influence."*

**2. The VPN FAQ (January 2, 2026)**
Kyle and Justin's meeting reveals that the mods were trying to build community education materials about a product they themselves only partially understood, based on a document William had written. Kyle: *"I'm fifty percent sure about just about everything I'm thinking."*

**3. The Departure (January 17, 2026)**
Jason's message to the mod team at 7:38 AM, before posting his public community update:
> *"If you are asked about the situation, please respond with: 'The announcement speaks for itself, and we can't really comment on it.' Please do not speculate, elaborate, or engage in back and forth beyond that within the Datagram server."*

The public community update was posted at 7:48 AM, ten minutes later.

**SOURCE**: Mod-discussion logs (all three instances), Kyle/Justin meeting transcript

### ⚠️ SOURCING GAPS — Needs interview:
- **Justin (you)**: What did it feel like to be handed a script? Did you ever push back or ask for more information?
- **Kyle**: Were there other instances of being given explicit messaging instructions that aren't captured in the Discord logs?

---

## Section 4: My Debug (~200–250 words)

### The January 2 Meeting

Return to the meeting itself as a scene. Two weeks before Jason's departure, Kyle is trying to build a VPN FAQ for a community asking about a product that was barely working, while knowing the project is in financial trouble but not being able to say so.

He tells Justin: *"I don't have any more specific information about payments, about compensation... No matter how it turns out, I've been told in the sincerest of ways that we will be taken care of."*

This is the texture of working inside the gap. Kyle believed it. He passed it on because he believed it. And two weeks later, Jason sent the mod team a script.

Close with the forward-looking question for Part 3: if the mods couldn't see past the layer above them, and Jason couldn't control the layer above him — who could?

---

## Structural Notes

**Section headers (draft)**
1. "Fifty Percent"
2. "The Finance Overlords"
3. "The Announcement Speaks for Itself"
4. "Two Weeks Before"

**Key quotes already in hand**
- Kyle: *"I'm fifty percent certain of just about everything I'm doing these days"* (Jan 2 transcript)
- Kyle: *"making sure William doesn't run with scissors"* (Jan 2 transcript)
- Kyle: *"William doing one thing and Andy trying to make sense of it all"* (Jan 2 transcript)
- Kyle: *"forty percent of dev resources to build an AI that judges your accent"* (Jan 2 transcript)
- Chris: *"The finance overlords are at fault"* (mod-discussion, April 8, 2025)
- Jason: *"The announcement speaks for itself"* (mod-discussion, Jan 17, 2026)
- Kyle to Korean mod: *"our hands are tied and we CANNOT manually change this"* (mod-discussion, Nov 28, 2025)

**Footnotes needed**
- Kyle/Justin meeting transcript (Jan 2, 2026)
- Mod-discussion payment logs (April–May 2025)
- Mod-discussion Jan 17, 2026
- Mod-discussion Nov 28, 2025

---

## ⚠️ MASTER SOURCING GAPS FOR PART 2

| Gap | Source needed | Priority | Status |
|-----|--------------|----------|--------|
| When Jason learned of VPN pivot and whether he was consulted | Jason interview | HIGH | Open |
| What specifically the "team meeting" Kyle references covered | Kyle interview | HIGH | Open |
| ~~Who "Richard" is and his exact role/authority~~ | ~~Chris interview~~ | ~~HIGH~~ | ✅ RESOLVED: Richard Han, VP at VinaCapital Ventures (confirmed team page + LinkedIn: linkedin.com/in/hanrichard/). Deal-level portfolio manager on the Quickom investment. Public-facing partner for that deal is Hoang Duc Trung. |
| Specific plans Jason submitted that William ignored | Jason interview | HIGH | Open |
| Whether Chris knew in April that payments were structurally broken | Chris interview | MEDIUM | Open |
| Other scripted messaging moments not in Discord logs | Kyle interview | MEDIUM | Open |
