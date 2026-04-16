# Part 3: The Structure of Control

**Working title**: "Theoretical Authority"
*(from Jason's April 2026 DM: "I did have control over the THEORETICAL tokenomics, but never had operational control over how they were implemented.")*

**Template**: System Audit — full audit of the power structure
**Target length**: 1,500–1,600 words
**Tone**: This is the most structurally analytical piece in the series. Less personal narrative, more forensic. The emotional weight comes from the gap between what was promised and what existed.

---

## The Core Argument

Datagram was not structured as a project where the public-facing leader had real authority. Whether this was intentional from the start or evolved over time is a question this piece will hold open — but the architecture of control is documentable regardless of intent. Jason had the title, the community trust, and the tokenomics theory. He did not have the wallet keys, the development team, or the board.

---

## Section 1: The Glitch (~400 words)

### What "Control" Actually Meant

Open with Jason's own words from his April 2026 DM to Justin — the clearest summary of his position:

> *"I did have control over the THEORETICAL tokenomics, but never had operational control over how they were implemented. There were numerous times where I would write up a whole plan, give it to William, be told it would be implemented, and then something else entirely would happen."*

> *"I was promised that I could run the product roadmap and have control over the org, but never received it. He would handle the development. I learned he was building all sorts of non-Datagram shit with his engineers and that Datagram was supporting them."*

And from his Jan 17 departure message to the mod team:

> *"I do not have the ability to access or move tokens, and I do not control treasury or on chain resources."*

He's stepping back, he says, *"until there is a change at the board level that enables real authority and alignment."*

This is the map: Jason Brink, public face, tokenomics architect, community figurehead. The territory: no wallet access, no operational control, no enforcement mechanism for his own plans.

The question Part 3 tries to answer is: who did have control?

**SOURCE**: Jason DMs (April 2026), mod-discussion Jan 17, 2026

---

## Section 2: The Source Code (~500 words)

### Layer 1: The Multisig

Jason's account of the wallet structure, from his April 2026 DM:

> *"I never had the ability to move tokens. That was all in a multisig that I was theoretically part of (I don't actually know because I don't think I ever had to sign anything — I think I might have for one bridge transaction, but I could be wrong). I heard from other people that while it was a multisig, he actually controlled all the signing wallets."*

A multisig wallet is designed to require multiple parties to authorize any transaction — the distributed control mechanism that gives DePIN projects their "decentralized" credibility. If one person controls all the signing wallets, it is functionally a single-signature wallet with extra steps. The decentralization is cosmetic.

Jason adds: *"That said, I never WANTED control. Nobody should ever have full control over wallets."*

The tokens Jason did move — paying ambassadors, setting up allocations for Rodebrecht's CapsuleHub — he bought himself off the market. The treasury wasn't his to access.

### Layer 2: The Development Team

William controlled the engineers. Jason's plans went to William. What came back, if anything, was William's interpretation of those plans — or something else entirely.

Kyle's characterization from the Jan 2 meeting:
> *"A lot of Jason's efforts — and frankly an unfair amount of Jason's efforts — go into kind of making sure that William doesn't run with scissors... Curtailing his worst impulses... making sure he's got a knuckle-white grip on the bungee cord... you just leave him alone for five minutes, and he comes back and he's had seven conversations that completely changed the trajectory of the project."*

Specific documented examples of unilateral William decisions:
- The VPN pivot (announced without community consultation, implemented in a way that divided the dev team — Andy wanted to do it correctly, William wanted to cut corners)
- The accent-detecting AI (*"forty percent of dev resources"*, per Kyle, never publicly announced but made it to the website)
- The BSC bridge: *"they just kinda didn't tell anybody"* (Kyle, Jan 2 transcript)
- Any tokens Jason paid out came from his own purchases, not the treasury

### Layer 3: The Board and Richard

This is the least visible layer — and the most important. It has now been partially identified.

What is confirmed:
- Jason explicitly frames his departure as being contingent on *"a change at the board level"* — meaning the board was the decision-making authority above him
- Chris named "Richard" in his April 2026 DM to Justin as the person who controlled payments and made direct hiring decisions (he hired Tiffany)
- **Richard has been identified as Richard Han (also known as Yu te Han), affiliated with Vina Capital, the VC that invested in Datagram** — confirmed by Chris in April 2026 follow-up
- Richard held no formal title at Datagram. Chris: *"I would call him William's handler."*
- William would only act if Richard instructed him to. Richard was the effective decision-making ceiling.
- Richard was most active until approximately TGE (November 18, 2025), after which he went radio silent — consistent with when payments collapsed and William went dark in December
- The earliest documented reference to Tiffany is June 12, 2025, when mod supercrunch.alt mentions: *"This was requested by Tiffany in the call earlier"* — indicating she had operational authority over mod workflows before most mods knew who she was
- Chris's payment chain ran: mods → Chris → "finance" (Richard/Vina Capital) → back to Chris → mods

**Additional nuance from Chris**: Chris believes William was himself deceived by Richard, rather than being the primary bad actor. *"I think William is not 100% guilty — he rather got deceived by Rich, but that doesn't redeem him in my book."* This complicates the two-villain framing: it may be that the deception chain ran Richard → William → Jason/community, with William as an intermediary rather than an architect.

**NEW PRIMARY SOURCE — VinaCapital/Quickom press release (March 6, 2024):**
A public press release establishes the corporate lineage. VinaCapital Ventures led a **$1.5M seed round** in **Quickom** — Dr. William H. Nguyen's video conferencing company, founded 2021 in Vietnam. Quickom's described technology (decentralized peer-hosted network, unused bandwidth extraction, U.S. patents) is word-for-word the Datagram pitch. Datagram was the Web3/node-sale layer built on top of Quickom's underlying infrastructure. The named VinaCapital partner in the press release is **Hoang Duc Trung**, not Richard Han — see flag below.

What is still NOT confirmed:
- The board's full composition and formal governance structure
- **Richard Han is confirmed on the VinaCapital Ventures team page** as Vice President (LinkedIn title: Partner, Principal Investment VC). Hoang Duc Trung is the Partner who took the public quote in the press release — Richard Han is the deal-level investment manager who would have handled the hands-on portfolio company relationship. This is consistent with Chris's description of him as the day-to-day "handler." His background: Baruch College (MS/BBA), ABN AMRO M&A, Masan Group strategy, VinaCapital since 2018. LinkedIn: linkedin.com/in/hanrichard/. Note: "Yu te Han" yields no public records — "Richard Han" is the confirmed public identity.
- Whether Jason ever had a formal equity stake or was entirely at the board's discretion
- The precise legal relationship between Quickom (the VinaCapital investee) and Datagram Network (the token/node entity)

**SOURCE**: Jason DMs (April 2026), Kyle/Justin meeting (Jan 2, 2026), Chris DM (April 2026 — both sets), mod-discussion payment logs, supercrunch.alt reference (June 12, 2025), VinaCapital/Quickom press release (March 6, 2024)

### ⚠️ SOURCING GAPS — Critical for this section:
- **Jason**: Who specifically is "the board" beyond Richard? Did Jason have any equity? What was he told his authority would be when he first joined?
- **Jason**: Specific examples of plans he submitted that were ignored (beyond VPN and accent AI) — dates and documentation if possible
- ~~**Chris**: Richard's full identity and role. What was the relationship between Richard and William? Who had final authority?~~ ✅ RESOLVED — Richard Han / Yu te Han, Vina Capital; William only acted on Richard's direction; Richard held no formal title
- ~~**Carth**: Jason mentioned Carth shared his suspicions about the rug theory. What specifically did Carth observe about the control structure?~~ ✅ NOTE: Carth (Carthaphilus in Datagram Discord) = Chris (enron_financial_intern). Already interviewed. His view: William was deceived by Richard, not a primary architect — but not redeemed.
- **Research**: Vina Capital — can Richard Han's background and other investments be established from public sources?

---

## Section 3: The Upgrade (Withheld — "The Ultimatums") (~400 words)

### When Jason Tried to Use Leverage He Didn't Have

Jason's account, from April 2026:

> *"So, I gave him some ultimatums. He eventually missed those, and I had to step back."*

He could not elaborate publicly because the legal risk was too high. But the structure of this section is the pattern itself — a person with apparent authority discovers the limits of that authority through conflict, then through failure.

Document what is known about the timeline:
- By January 2, 2026 (Kyle meeting), Jason was already pushing William on an "uptime tracking overhaul" that Kyle describes as detailed and ambitious — and which showed no signs of being implemented
- Kyle's characterization of Jason's role at this point: primarily managing William rather than building
- By January 17, the ultimatums had been missed

Hold the specific content of the ultimatums as a gap — and name it explicitly. This is what the reader should understand is still unknown.

Also here: the "rug" theory. Jason raised it unsolicited in April 2026:

> *"I think the whole thing was set up to be a rug by Dr. William and the main VC guy behind it and they wanted to pin the whole thing on me. I obviously didn't cooperate because I don't do that sort of shit, and so I kinda ruined their plans. The issue is that I can't PROVE it."*

Present this as what it is: an allegation from an insider who was positioned to observe but cannot prove. Note that Jason cited fear for his family's safety as a reason for caution. Note that he identified Carth as sharing similar suspicions. **NOTE: Carth = Chris (Carthaphilus was his Datagram Discord username; enron_financial_intern is his standard Discord handle).** Chris has now been interviewed and his view is consistent with Jason's framing: Richard was the primary bad actor, William a compromised middleman.

This is not a verdict. It is testimony — and the reader has enough context by now to weigh it.

**SOURCE**: Jason DMs (April 2026), Kyle/Justin meeting transcript (Jan 2, 2026)

### ⚠️ SOURCING GAPS:
- **Jason**: What specifically were the ultimatums? What were the deadlines and what happened when they were missed?
- **Jason**: Who is "the main VC guy"? (He may not be willing to name publicly — explore anonymous sourcing)
- ~~**Carth**: What specifically did Carth observe that aligns with Jason's suspicions? (Direct outreach needed)~~ ✅ RESOLVED: Carth = Chris. Interviewed. His view aligns with Jason's suspicion: Richard (Vina Capital) was the primary bad actor; William was deceived but still culpable.
- **Chris**: Does Chris believe the rug theory? His departure statement — "done with the madness bestowed upon us by the leadership" — suggests he saw something. What?

---

## Section 4: My Debug (~200–250 words)

### What You Knew vs. What You Couldn't Know

As a moderator, you were inside a system that had a very specific information horizon. You could see what the mods discussed. You could see what the community discussed. You could not see the board, the dev team, or the treasury.

Reflect briefly on what it was like to be a trusted community member who was, structurally, also kept in the dark. Not maliciously — you don't know that — but functionally. You got what Kyle got: "in the sincerest of ways, we will be taken care of."

Close with the bridge to Part 4: The structure of control is the context for the unraveling. Payments didn't stop because someone forgot. They stopped because the person responsible for paying didn't control the money, the person above him controlled it for reasons nobody below could see, and when the whole structure collapsed, everyone was surprised except possibly the people at the top.

---

## Structural Notes

**Section headers (draft)**
1. "Theoretical Authority"
2. "Who Actually Held the Keys"
3. "The Ultimatums"
4. "What You Can't See From Inside"

**Key quotes already in hand**
- Jason: *"I did have control over the THEORETICAL tokenomics, but never had operational control"* (April 2026 DM)
- Jason: *"I never had the ability to move tokens... I heard he actually controlled all the signing wallets"* (April 2026 DM)
- Jason: *"I think the whole thing was set up to be a rug... I can't PROVE it"* (April 2026 DM)
- Jason: *"I will make sure all moderators are paid their USDT through today... I do not have the ability to access or move tokens"* (Jan 17, 2026)
- Kyle: *"making sure William doesn't run with scissors"* (Jan 2, 2026)
- Kyle: *"forty percent of dev resources to build an AI that judges your accent"* (Jan 2, 2026)
- supercrunch.alt: *"This was requested by Tiffany in the call earlier"* (June 12, 2025)

**Footnotes needed**
- Jason April 2026 DM
- Jason Jan 17, 2026 mod-discussion message
- Kyle/Justin Jan 2, 2026 meeting transcript
- Mod-discussion June 12, 2025 (Tiffany reference)

---

## ⚠️ MASTER SOURCING GAPS FOR PART 3

| Gap | Source needed | Priority | Status |
|-----|--------------|----------|--------|
| ~~Richard's full identity, role, and relationship to William~~ | ~~Chris interview~~ | ~~CRITICAL~~ | ✅ RESOLVED: Richard Han, VP at VinaCapital Ventures (LinkedIn: linkedin.com/in/hanrichard/). Confirmed on team page. Not named in press release — Hoang Duc Trung is the public-facing Partner. Richard was the deal-level manager, consistent with Chris's "handler" description. |
| The specific ultimatums Jason gave William | Jason interview | CRITICAL | Open |
| ~~Who "the main VC guy" is~~ | ~~Jason interview~~ | ~~CRITICAL~~ | ✅ RESOLVED: Richard Han, VP at VinaCapital Ventures. Confirmed via team page and Chris's account. |
| ~~Carth's specific observations about control structure~~ | ~~Carth outreach~~ | ~~HIGH~~ | ✅ RESOLVED: Carth = Chris (Carthaphilus = enron_financial_intern). Already interviewed. |
| Board composition and voting authority | Jason/Chris | HIGH | Open |
| Whether Jason had equity or was purely salaried/contracted | Jason | HIGH | Open |
| The full timeline of when Jason realized his authority was nominal | Jason | HIGH | Open |
| ~~Whether Chris believes the rug theory~~ | ~~Chris~~ | ~~MEDIUM~~ | ✅ PARTIAL: Chris believes William was deceived by Richard, not a primary bad actor — but doesn't redeem him |
| Tiffany's full role and when she was brought in | Chris | MEDIUM | Open |
| Richard Han / Vina Capital — public background and other investments | Web research | HIGH | PARTIAL: Press release (March 2024) names Hoang Duc Trung as VinaCapital Ventures partner on Quickom deal. Richard Han not named. Need to verify Richard Han's role against VinaCapital team page. |
| Quickom → Datagram corporate structure — are they separate legal entities? What is the relationship between Quickom equity and Datagram treasury? | Research / Jason | HIGH | Open |
| Enterprise client claims in VinaCapital press release vs. Jason's departure statement ("could not be substantiated") — are these the same representations? | Research / Jason | HIGH | Open |
| Chat3 — William's parallel project pre-dating Datagram node sale. Was dev team split between Quickom, Chat3, and Datagram simultaneously? | Research / Kyle | MEDIUM | Open |
