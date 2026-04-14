# Datagram Network: Red Flag Report
**Compiled from Discord Data | Researcher: Justin Hearn (drinkyouroj)**

---

> **Purpose:** This report catalogs specific findings that, individually or collectively, indicate potential misrepresentation, operational failures, or bad-faith conduct by Datagram's leadership. Each finding includes the date, source channel, and direct evidence (verbatim quotes or statistical data). The researcher (Justin Hearn) has insider context as a former member of the mod team from July 2025 through approximately January 2026.

> **Persons:** BitBender = Jason Brink (CEO), kyleczech = Kyle (Senior Mod), nephilimhoss = Lead Discord Admin, enron_financial_intern = Chris (Mod), devikinbop = Tommy (Mod), drinkyouroj = Justin Hearn (Mod/Researcher). Dr. William Nguyen = board founder / controlling shareholder.

> **⚠️ Flags marked [FLAG FOR REVIEW]** are quotes or findings that I (Justin) flagged as particularly sensitive or notable and recommend you validate against your own inside knowledge before drawing final conclusions.

---

## Category 1: Promises vs. Delivery

---

### RF-1: Mainnet Timeline — Repeated Misses Without Acknowledgment

**First promise date:** ~Aug 2025 (node sale opening period)
**Source channel:** general-chat, mod-discussion, general-log

The mod team publicly stated a mainnet target of "late September – early October 2025" during the August 2025 node sale:

> *"Here is what's to come after your Node purchase. Mainnet is scheduled for late Sept early Oct at this stage."* — devikinbop, Aug 12, 2025 (general-chat)

> *"Our team are eyeing to have it on Late Sept - Early Oct. So stay tuned until then!"* — yusha.nft, Aug 12, 2025 (general-chat)

**Actual delivery:** Mainnet launched November 14, 2025 — six to eight weeks past the stated window.

**Pattern:** At no point in the analyzed data did the team issue a formal acknowledgment that the late September timeline had been missed, or explain why it slipped. The community was simply re-directed to "watch announcements" as dates came and went. This pattern of rolling, un-acknowledged deadline movement appeared to be standard operating procedure.

**Additional context:** In the AMA record, Jason (BitBender) stated "first half of November" for TGE at a date close enough to the actual event that it could read as accurate, but this came after the September timeline had already passed without mention. The later promise matched; the earlier one was simply abandoned.

---

### RF-2: Mod Pay — Promised, Largely Unpaid

**Promise date:** Feb 3, 2025 (server launch; mod team assembled)
**Failure confirmed:** Jan 17, 2026
**Source channels:** mod-discussion (all 3 parts), node-owner-chat

The mod team was assembled with an understanding that they would be compensated. The lead admin (nephilimhoss) set up the shift schedule explicitly for paid work. When Jason departed on January 17, 2026, his message to mods included a payment commitment:

> *"I also want to be explicit that I will make sure all moderators are paid their USDT through…"* — bitbender, Jan 17, 2026 (mod-discussion)

The message was cut off in the extract but confirmed payment intent.

**Reality (per researcher Justin Hearn):** Justin received approximately 1 week's worth of pay for ~7 months of work. The payment came from Jason personally — out of his own pocket — not from the project treasury. No DGRAM was ever received by the mod team.

Jason's January 22, 2026 message confirmed the DGRAM allocation situation:

> *"William has told me that tokens are set aside. He has told me that he has allocated some tokens to give to mods as team members, etc, but as of yet I have not received them."* — bitbender, Jan 22, 2026 (mod-discussion)

As of the data cutoff (April 2026), no DGRAM had been distributed to mods.

**Confirmation from nephilimhoss (server owner), January 27, 2026:**

> *"I built this server. I own it. I was supposed to be paid for my small role in security and discord admin... but like all the mods, I'm still waiting."* — nephilimhoss, Jan 27, 2026 (node-owner-chat)

**Kyle's public statement, January 27, 2026:**

> *"I am literally the only person left offering support here and I'm doing so as a volunteer because William still has not paid a single cent to the mod team, despite the promises he made."* — kyleczech, Jan 27, 2026 (node-owner-chat)

**Severity:** High. The mod team built and sustained the community for up to a year. Their unpaid labor was essential to maintaining investor/user confidence during the node sale. If that labor had not been donated, the project would have faced community collapse during its most commercially critical phase.

---

### RF-3: Jason's Control — CEO Without Treasury Access

**Date revealed:** Jan 17, 2026
**Source channel:** mod-discussion / public announcement

In his resignation announcement, Jason stated:

> *"I do not have the ability to access or move tokens, and I do not control treasury or on chain resources."* — bitbender, Jan 17, 2026

**⚠️ [FLAG FOR REVIEW]:** This statement raises a question that the public data cannot answer: Was this always true, or did Jason lose treasury access at some point before or after TGE? The answer has significant implications. If Jason was always a figurehead CEO without operational control, then his public promises about tokenomics, mod pay, and project direction were promises he was never empowered to keep. If he lost access at some point, then the question is when, why, and whether the community was informed.

Kyle's comment in node-owner-chat adds context:

> *"Unless William and the board make drastic changes to the structure of the project and give Jason the control he was promised in the beginning, it doesn't make sense for him to assume the role of CEO in title only."* — kyleczech, Jan 27, 2026

The phrase "give Jason the control he was promised in the beginning" suggests that Jason entered the CEO role with an expectation of real operational authority that was not honored by the board.

---

### RF-4: Burn-and-Mint Equilibrium — Not Implemented As Described

**Promise date:** Pre-TGE (AMA transcripts and public channels)
**Source channels:** general-chat, node-owner-chat, AMA transcripts

The DGRAM tokenomics were marketed around a "burn-and-mint equilibrium" where demand for network services would burn tokens, creating deflationary pressure that would support the token price. Post-TGE, community members quickly identified that:

1. No meaningful service demand existed (the VPN and UDP services had few real users)
2. Node operators were continuously minting DGRAM through uptime rewards
3. The burn mechanism was not operational

The capsule system was presented as a lock-up that would suppress selling pressure, but the opening of capsules by early holders immediately distributed DGRAM into the market. Kyle noted early on:

> *"We can see from the dashboard that two people already opened their capsules and forfeited the ~90% of unvested DGRAM inside."* — kyleczech, Nov 21, 2025

The price trajectory confirmed the tokenomics were not functioning as described. One community member's analysis:

> *"Price looks like it was artificially kept stable as long as nodes were selling and after boom dump."* — alex97xs, Dec 11, 2025 (node-owner-chat)

**⚠️ [FLAG FOR REVIEW]:** Was the burn mechanism actually built and deployed at any point, or was it only in the whitepaper/marketing? The data shows Kyle answering price questions with generic deflection ("markets go up and down") rather than pointing to any burn activity. If the mechanism was never deployed, that represents a significant promise-delivery gap.

---

### RF-5: Capsule NFT Economics — System Designed to Disadvantage Non-Node-Buyers

**Date:** Nov 14–25, 2025 (TGE week)
**Source channel:** general-chat

The capsule system was promoted as a fair reward mechanism for testnet participants. In practice, it created a system where:

- Testnet runners received capsule NFTs containing DGRAM
- Only Full Core Node owners could "open" (unlock) a capsule
- Testnet runners without a node had to sell their capsule to node owners to access value
- Selling before 12 months of vesting would forfeit a significant percentage of the DGRAM inside
- The transfer fee was small but existed (~0.7 DGRAM from a faucet)

This was not hidden — Kyle explained it openly and often. But the design functionally meant that testnet participants who ran free nodes for months had a monetization path that depended on node buyers being willing to pay a fair price for their capsules.

In a weak token price environment, this created a severe power imbalance. Node owners could offer low prices for capsules knowing that testnet runners needed liquidity. One community member calculated their effective earnings as $5–6 for 60 days of 24/7 node operation.

**Representative quote:**

> *"I ran my laptop for 60 days 24/7, I am getting 5-6 USD but 1 year vesting. Is there any biggest scam like this?"* — rejoan09, Nov 21, 2025

The question raised by several community members — "why not just vest the tokens directly?" — was never directly answered by the team.

---

### RF-6: Node Sale Revenue vs. Team Compensation

**Date:** Jan 2026
**Source channel:** node-owner-chat

Community members attempted to estimate the capital raised:

> *"As far as I know he is even ignoring some of the investors."* — megamind_govps, Jan 29, 2026

> *"As far as I know they have hardly got $1,437,900 from the node sales and maybe $4-5M from investors."* — megamind_govps, Jan 28, 2026

[Note: These are community estimates and unverified.]

If even the lower figure is approximately correct (~$1.4M from node sales), the decision not to pay the mod team — who were essential to maintaining community trust during the sale period — represents a significant and troubling misalignment. The team's labor was leveraged for commercial gain without commensurate compensation.

---

## Category 2: Community Sentiment Shifts

---

### CS-1: TGE Spike and Immediate Sentiment Collapse

**Date:** Jun 12 – Jun 20, 2025 (first TGE event) / Nov 17–26, 2025 (mainnet/token distribution)
**Source channel:** general-chat (statistical data)

The June 12, 2025 TGE event brought 5,490 unique authors to the server in a single day. The negative keyword hit rate on that day was 272/22,656 = 1.2%. By itself this sounds low, but in absolute terms it represented the largest single-day wave of skeptical/negative content the server had ever seen.

The more revealing figure comes from the sustained post-TGE period. After the initial spike, audience bleed was immediate and severe:

| Period | Peak Authors/Day | 30 Days Later |
|--------|-----------------|--------------|
| Jun 12 TGE | 5,490 | ~860 (Jun 30) |
| Nov 17 mainnet | 1,498 | ~250 (Dec 17) |

In both cases, approximately 80–85% of the new audience did not return after the first wave. This is consistent with a community of airdrop farmers and speculative participants who had no long-term stake in the project.

---

### CS-2: November 26, 2025 — Worst Sustained Sentiment Ratio

**Date:** Nov 26, 2025
**Source channel:** general-chat (statistical data)

November 26 recorded 243 negative keyword hits against 4,236 total messages — a 5.7% negative ratio. This is the worst single-day negative ratio for any day with significant traffic volume in the dataset (excluding the ultra-low-traffic collapse period).

This date coincided with the capsule distribution going live and the DGRAM price in active decline. The combination of receiving an asset (the capsule) and immediately discovering its dollar value was far below expectations produced the most concentrated negative sentiment in the project's history.

---

### CS-3: February 3, 2026 — Worst Negative Ratio in Dataset

**Date:** Feb 3, 2026
**Source channel:** general-chat (statistical data)

56 negative hits from 291 total messages = 19.2% negative ratio. This is a nearly 1-in-5 message rate for negative sentiment keywords. Occurring on the one-year anniversary of the server's public launch, with Jason having departed two weeks earlier and William Nguyen non-responsive, this date represents peak disillusionment in the community.

---

### CS-4: Node-Owner-Chat — The Most Concentrated Investor Anger

**Date:** Jan–Feb 2026
**Source channel:** node-owner-chat

The node-owner-chat channel, restricted to people who had actually purchased Full Core Node Licenses (the paying customers), showed the most direct and concentrated expressions of loss and betrayal in the dataset.

Select quotes from this period:

> *"I invest this project 750$ but prices everyday down very disappointed."* — mdmustafizurrahaman, Jan 1, 2026

> *"I want to sell my node 80 usdt."* — 2.00070, Feb 1, 2026 (original purchase price was significantly higher)

> *"Since Jason made me felt down from Datagram node that is the most trusted project, now no more for the node project as well."* — sorchor, Jan 28, 2026

> *"William is saying nothing. Bitbender lead us down this road. I only invested because of him. Now he's gone in the wind. Just like Gala film and music."* — topboy3556, Feb 13, 2026

> *"I officially shutdown all my nodes."* — cydereyesx, Mar 4, 2026

Several members of node-owner-chat identified Datagram in a list of failed node projects alongside GR1D, Rivalz, Gala Film/Music, TWDE, and others — contextualizing their experience within a broader pattern of DePIN node project failures.

---

### CS-5: The Wallet-Tracking Allegation

**Date:** Jan 27, 2026
**Source channel:** node-owner-chat

**⚠️ [FLAG FOR REVIEW]:** A community member (mushufasza) made a specific allegation that warrants closer examination if you have any ability to verify it:

> *"I sugest all of u big believers just look up the dev wallet on BSC and you will find at least 5 wallets involved with the dev wallet sending to Gate in heavy way."*  — mushufasza, Jan 27, 2026

This is a claim that developer/team wallets were selling DGRAM to a CEX (Gate.io) in large quantities. If true, this would be consistent with the "artificially maintained price during node sale / dump after" pattern that multiple community members separately identified.

This is an unverified community allegation. It should be considered as a lead for on-chain verification rather than an established fact. Kyle responded that wallet tracking was not his area and asked clarifying questions without dismissing the claim.

---

## Category 3: Team Behavior and Internal Communications

---

### TB-1: Narrative Management as an Explicit Mod Function

**Date:** Jun 16, 2025
**Source channel:** mod-discussion

On the first day of the public testnet launch, Kyle wrote:

> *"I want to help them get the narrative straight."* — kyleczech, Jun 16, 2025 (mod-discussion)

Taken in isolation this is a normal community management statement. In context, it reflects a team that was actively coordinating what language to use, what to emphasize, and what to de-emphasize. Throughout the dataset, mods routinely:

- Directed users to pre-approved announcements rather than answering directly
- Used scripted responses ("the announcement speaks for itself")
- Deflected unfavorable comparisons to other projects
- Labeled questions as "FUD" and issued warnings

This is not evidence of wrongdoing on the mods' part — they were doing their jobs as instructed. But it means that the community's information environment was substantially filtered by people who had an incentive to present the project positively.

---

### TB-2: Jason's Scripted Response Instruction to Mods — Jan 17, 2026

**Date:** Jan 17, 2026
**Source channel:** mod-discussion

Before making his resignation public, Jason gave explicit instructions to mods:

> *"If you are asked about the situation, please respond with: 'The announcement speaks for itself, and we can't really comment on it.' Please do not speculate, elaborate, or engage in back and forth beyond that within the Datagram server."* — bitbender, Jan 17, 2026 (mod-discussion)

This was standard damage control. However, read in conjunction with Jason's own admission that he had no treasury control, it means the mods were instructed to deflect questions about a situation that Jason himself could not fully explain.

---

### TB-3: "Those Promises Came From Jason" — Kyle's Candid Admission

**Date:** Jun 23, 2025
**Source channel:** mod-discussion

When discussing whether specific promises had been made to the community:

> *"Those promises came from Jason."* — kyleczech, Jun 23, 2025 (mod-discussion)

This statement, made privately among mods, is significant because it establishes that the mod team understood a clear chain of accountability: community commitments originated with Jason, and the mods were responsible for communicating and defending them without having made them themselves. When those commitments failed, the mods were the ones facing community anger while the decision-maker (Jason) was relatively insulated.

---

### TB-4: The Perverse Incentive Structure — Mod Pay Tied to Token

The mod team's promised compensation was partly or fully in DGRAM tokens. This created a situation where:

1. Mods were financially incentivized to present the token positively to protect the value of their own expected payment
2. When the token price declined, the value of their labor compensation declined with it
3. When Jason lost/lacked treasury access, the mods' token compensation became contingent on William Nguyen's cooperation — which never materialized

Justin's January 22 message made the psychological reality explicit:

> *"I'm not going to expect any token payment (it probably wouldn't be worth very much anyway…) but I was hoping to hear that tokens had at least been set aside at TGE to pay mods and you're just unable to access them directly. I'd still like to receive my DGRAM allotment, even if it's only worth a fraction of a percent of what it 'should' be. For me, it's about follow-through more than money."* — drinkyouroj, Jan 22, 2026

This message captures the essence of the mod team's situation: they served in good faith, were promised compensation, and were ultimately left with nothing — not primarily for financial reasons, but because the project's leadership structure failed to honor its word.

---

### TB-5: The Two-CEO Problem — Jason vs. William

**Date:** Jan 17–Mar 2026
**Source channels:** mod-discussion, node-owner-chat

Jason's resignation revealed that Datagram had a split leadership structure that was not publicly disclosed:

- Jason (BitBender) was the public-facing CEO — the person who made community promises, appeared in AMAs, and set expectations
- Dr. William Nguyen was the board-level founder/controlling shareholder who held actual control of the treasury and blockchain resources

The community had been dealing with Jason as if he were the decision-maker. Kyle's post-resignation comments established that this was not the case:

> *"Unless William and the board make drastic changes to the structure of the project and give Jason the control he was promised in the beginning, it doesn't make sense for him to assume the role of CEO in title only."* — kyleczech, Jan 27, 2026

> *"He stopped responding to my DMs on Telegram over a week ago, after making promises to provide you guys with clarity."* — kyleczech, Jan 29, 2026

> *"I have documented conversations where he made promises to show up a couple of days after Jason's announcement of stepping back, and then a long string of messages from me after that that went unanswered."* — kyleczech, Mar 4, 2026

**⚠️ [FLAG FOR REVIEW]:** To what extent were you (Justin) aware during your time as mod that Jason did not have treasury control? And was this known to nephilimhoss, who was the server owner with longest tenure? The answer shapes how we characterize the early promises — were they made in ignorance of the structural constraint, or were they made knowingly by someone who understood he couldn't deliver?

---

### TB-6: Server Infrastructure Owned Independently — Leverage Risk

**Date:** Jan 27, 2026
**Source channel:** node-owner-chat

An important structural fact emerged from nephilimhoss's statement:

> *"I built this server. I own it."* — nephilimhoss, Jan 27, 2026

And separately:

> *"I'll need to talk with a lawyer anyway to make sure I CYA. Anyone scummy enough to take money and never deliver a product should not be trusted to not make predatory lawsuits."* — nephilimhoss, Mar 4, 2026

The Discord server — which was the primary community platform and contained all the archived promises, announcements, and community history — was owned by nephilimhoss personally, not by Datagram as a company. This has two implications:

1. The project relied on volunteer infrastructure it did not own or control
2. The historical record of the project's promises is stored on a platform controlled by someone who may be adversely disposed toward the project's leadership

---

### TB-7: Moderation Spikes as Correlated with Key Events

**Date:** Observed throughout Jun–Nov 2025
**Source channel:** mod-log, admin-log

The mod-log showed a pattern of elevated ban/deletion activity around the TGE launch period (June 2025 and November 2025), consistent with the periods of highest community frustration. While some portion of moderation actions were clearly legitimate (spam, scammers, coordinated raids documented in the data), the elevated activity during frustration peaks warrants examination.

The mod team's own description of their approach:

> *"I'm supper chilled, I don't ban people easily and give warn in advance."* — jj3ss, Jun 15, 2025

> *"We've convinced quite a few to stay."* — kyleczech, Jul 21, 2025

The decision to "convince people to stay" versus allowing them to leave or express frustration freely was an active moderation choice that shaped the public perception of community sentiment.

---

## Summary Assessment

| Category | # Findings | Severity |
|----------|-----------|---------|
| Promises vs. Delivery | 6 | High (RF-2, RF-3) to Medium (RF-4, RF-5) |
| Community Sentiment Shifts | 5 | Documented (statistical) |
| Team Behavior / Internal Comms | 7 | High (TB-2, TB-5) to Low (TB-1, TB-7) |

**Highest-severity individual findings:**
- RF-2 (Mod Pay): Systemic failure to compensate essential team members for documented work
- RF-3 (CEO Without Treasury Access): Public-facing leader made commitments he was structurally unable to honor
- TB-5 (Two-CEO Problem): Leadership structure obscured from public until collapse

**Items requiring insider validation (marked [FLAG FOR REVIEW]):**
- RF-3: Was Jason ever in real operational control? When did he lose it, if so?
- RF-4: Was the burn mechanism ever deployed on-chain?
- CS-5: Were dev wallets actively selling to exchanges during the node sale?
- TB-5: What did the mod team know about Jason's structural limitations during active service?

---

*Document compiled from raw Discord export data, statistical analysis, and verbatim quotes. All quotes include source channel and timestamp. Researcher: Justin Hearn (drinkyouroj). Compiled: April 2026.*
