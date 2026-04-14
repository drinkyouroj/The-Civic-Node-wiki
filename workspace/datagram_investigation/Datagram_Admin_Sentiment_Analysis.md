# Datagram Network — Admin/Mod Logs & Community Sentiment Analysis
**Phases 2–4: Deep Dive + Synthesis**  
**Sources:** mod-log (8,907 events), general-log (152,129 events across 9 parts), mod-discussion (23,475 messages), mod-news (180 messages), mod-bot-commands, general-chat-datagram (46 parts, ~400k+ messages), node-owner-chat (2,865 messages), dss-chat, offtopic-discussion  
**Date range:** Jun 2024 – Apr 2026  
**Analysis date:** April 13, 2026

---

## TABLE OF CONTENTS
1. [Phase 2: Mod-Log Spike Analysis](#phase-2-mod-log-spike-analysis)
2. [Phase 2: General-Log — Server Membership Curve](#phase-2-general-log--server-membership-curve)
3. [Phase 2: Mod-Discussion — Internal Team Dynamics](#phase-2-mod-discussion--internal-team-dynamics)
4. [Phase 3: Community Sentiment Curve](#phase-3-community-sentiment-curve)
5. [Phase 3: Node-Owner-Chat — Post-Launch Disillusionment](#phase-3-node-owner-chat--post-launch-disillusionment)
6. [Phase 4: Cross-Reference Synthesis](#phase-4-cross-reference-synthesis)
7. [Key Finding Summary](#key-finding-summary)

---

## PHASE 2: Mod-Log Spike Analysis

The mod-log records automated enforcement actions (bans, kicks, timeouts, warnings, bulk deletes). Total: **8,907 events** over ~11 months (Feb 2025 – Feb 2026).

### Spike Calendar with Context

| Date | Events | Interpretation |
|------|--------|----------------|
| **2025-02-17** | 118 | Early mass ban wave — automated bot accounts joining after initial marketing push. Dyno bulk-banning obvious fake accounts (random character usernames like `kfi732l4e6zsvtc`, `hfghfghdffgdfss`). Normal early-growth pattern. |
| **2025-02-18** | 360 | Second bot-ban wave. Still automated noise from rapid Discord growth. |
| **2025-02-25** | 413 | Third major bot-ban wave. Server growing fast, attracting scam/airdrop farming bots. |
| **2025-03-20** | 112 | Moderate spike — no obvious triggering event identified. Routine enforcement. |
| **2025-04-24–25** | 43+27 | Minor cluster. Community management activities. |
| **2025-05-20–21** | 589+709 | **MASSIVE SPIKE — largest pre-testnet event.** Near-simultaneous mass bans. Likely an organized bot raid (bot army targeting the server) + manual ban sweep. May coincide with some pre-testnet announcement. |
| **2025-05-31** | 286 | Follow-on enforcement activity. |
| **2025-06-11–15** | 104/73/163/82/28 | **Testnet launch wave.** Cascading bans as 14,000+ users joined in 24 hours. Mods and bots under extreme load. |
| **2025-07-19** | 61 | Minor spike around node sale activity. |
| **2025-08-28** | 122 | Spike coinciding with late August roadmap release period. |
| **2025-10-20** | 45 | Pre-TGE enforcement. |
| **2025-11-17** | **558** | **SECOND-LARGEST SPIKE — TGE day / Binance Alpha launch.** Confirmed: nephilimhoss banned "a few hundred obvious bot accounts" that voted in a server poll. Jason (BitBender) had announced a community vote, bots immediately flooded it for Option 1. Mass ban + reaction purge executed. "Weapons free on bans and timeouts" (Jason, Nov 18). |
| **2025-11-18** | **306** | TGE aftermath. Scammers pivoting tactics (IP redirect links, X.com fake links). enron_financial_intern: "do i get a medal for banning 100+ people today." |
| **2025-11-26** | 213 | Post-TGE volatility period. Community increasingly negative on price. |
| **2025-11-28–29** | 141+181 | Sustained enforcement. Likely price FUD and scammer activity. |
| **2025-11-30–12-03** | 110+70+55+66 | Continued high enforcement through late November / early December. |

### Key Moderation Tactics Observed

**Bulk delete** operations visible in Nov logs:
- Nov 14: Multiple `Bulk Delete in #general-chat-datagram` events — 4 messages, 26 messages, 4 messages, 5 messages deleted in rapid succession
- Pattern: mods clearing FUD threads or off-topic spam in real-time

**Message deletions captured in general-log** reveal what was being suppressed:
- Nov 14: `"MAINNET is live / crosschaun bridge to chain 56 (bsc) is ready"` — deleted from general-chat. A new account had all its messages deleted and removed within minutes of joining. (Account given then stripped of all roles.)
- Nov 14: `"does anyone dare to buy my capsules for $150 bro"` — deleted
- Nov 14: `"can the capsules sell for $150"` — deleted twice from same user
- Nov 14: `"supply 10b ya?"` — deleted (presumably a valid question)
- Nov 14: `"Point distribution update" [a copied announcement-style message]` — deleted
- Nov 14: `"who wants to buy my account? 167612 points"` — deleted

**Narrative management signals:** Deletions on Nov 14 show mods removing both scam attempts AND legitimate skeptical questions (capsule price questions, tokenomics questions). The "supply 10b ya?" deletion is notable — this is factual and publicly stated tokenomics info.

---

## PHASE 2: General-Log — Server Membership Curve

The general-log (152,129 automated events) captures Discord's server activity log — joins, role assignments, voice channel events, message deletions. This creates a proxy membership/activity curve.

### Quantified Activity Curve (Messages per Day in General-Log)

**Phase 1 — Pre-testnet baseline (Feb–May 2025):** 20–200 events/day  
**Phase 2 — Testnet launch explosion (Jun 11–19):** 1,594 → **14,852** → 6,822 → 4,824 → 3,704 → 2,301 → 1,908 → 1,745 → 1,428  
**Phase 3 — Testnet plateau (Jun 20–Jul 20):** 765–2,660/day, with notable secondary spike Jul 1 (2,660) and Jul 11 (3,011)  
**Phase 4 — Node sale slow fade (Jul 21–Aug 12):** 1,397 → 615 → declining toward 172–261  
**Phase 5 — TGE recovery spike (Oct 25–Nov 20):** 291 → 332 → ... → 2,226 → 1,745 → 496  
**Phase 6 — Post-TGE decay (Nov 21–Jan 2026):** 100–580/day  
**Phase 7 — Terminal decline (Jan–Apr 2026):** 50–100/day, trending toward 1–19 by March–April

### Critical Inflection Points

**Jun 11–12:** Server exploded from ~40/day to 14,852. This is when testnet went live and the broader crypto community discovered Datagram. The scale implies a coordinated marketing push that worked — but the sheer volume of accounts (most airdrop farmers) would poison community quality.

**Jul 11:** Secondary spike to 3,011. Likely correlated with node sale announcement or major AMA. Users re-engaging.

**Aug 13–17:** Precipitous volume drop — 328, 246, 196, 172, 177. This is where the daily activity halved and never recovered. Corresponds to late-August roadmap period but no positive event triggered recovery.

**Oct 25–26:** Mini-recovery spike (291, 332). Likely TGE anticipation / Binance Alpha announcement on Oct 25.

**Nov 14–18:** TGE launch spike — 580 → 796 → 926 → **2,226** → 1,745. Second-largest event in server history. Driven by Binance Alpha listing, MEXC listing, Gate listing on Nov 18.

**Post-Nov 20:** Server never recovered. Activity dropped to 100–200/day by late November, ~50–100 by January 2026, and ~1–19 by March–April 2026.

---

## PHASE 2: Mod-Discussion — Internal Team Dynamics

The mod-discussion (23,475 messages, Feb 2025 – Jan 2026) is the unfiltered private channel for the moderation team. Key personnel: nephilimhoss (lead mod/server admin), kyleczech (senior mod, "Kyle"), drinkyouroj (Justin Hearn — the author of this document, confirmed by username; also a mod), jj3ss (Jess — senior mod), devikinbop (Tommy), enron_financial_intern (Chris), aetrna1405 (Aety), yusha.nft.

**Note on drinkyouroj:** This is Justin Hearn (the researcher compiling this document), not BitBender/Jason Brink. Justin joined the mod team in July 2025 (after testnet launched), reviewed community content, created capsule explainer videos and decision trees, and participated in shift coordination. He was promised payment in crypto but received approximately one week's worth of pay — a partial personal payment from Jason out of pocket — for roughly seven months of work.

### Key Narrative Management Moments

**Feb 3–4, 2025 (Server founding):** nephilimhoss sets up mod schedule, promises mods will "be paid for the hours you covered" (Google Sheets schedule linked). Kyle (kyleczech) is from day one. The mod team is the founding community layer. Justin (drinkyouroj) joined later in July 2025.

**Feb 4:** Kyle asks for simplified explanations of the whitepaper to help community understand tokenomics. Shows early awareness that the product is complex and hard to explain.

**Jun 6, 2025:** Mod-discussion spike of 174 messages. This is just before testnet launch — likely intensive prep coordination.

**Jun 11–12:** Mod-discussion hits 206 then **877** messages. The testnet launch hit them hard. Mods scrambling. Extreme load.

**Nov 16:** Devikinbop shares Binance Alpha announcement — mods see it in the Discord channel before official announcement. Kyle notices Gate article inaccurate ("posted that testnet operators were going to get 7.5M DGRAM total"). enron_financial_intern confirms: "theyll have to change that" and "upped it to 45." (This implies timeouts or bans of 45 problematic accounts, or the minutes limit for messages was changed.)

**Nov 17 (TGE day):**
- Jason (BitBender) in mod-discussion at 4:19 AM: "Can you guys check wallet connect to see if it works? It should." — Jason personally testing the node purchase flow minutes after TGE.
- Devikinbop and aetrna1405 report: cannot connect wallets, getting node purchase errors.
- nephilimhoss announces mass bot ban: "a few hundred obvious bot accounts joined the server over the hours after Jason announced the vote. I banned obvious bots, and ran a reaction purge."
- nephilimhoss removed direct role-manage permissions from mods, citing security: "Manage Roles is the highest risk permission in Discord... it's 100% a matter of Murphy's Law."
- Kyle (11:01 PM): "I now give this plan a 7% likelihood of people understanding it here."

**Nov 18:**
- enron_financial_intern: "do i get a medal for banning 100+ people today"
- Jason/BitBender (11:01 AM): **"Absolutely weapons free on bans and timeouts."** — Jason explicitly orders open-ended banning during TGE launch day.
- Kyle: "We've seen at least 15 tickets come through with people claiming they bought a node and it turned out they did the stupid thing and paid money to have their testnet node hosted" — NaaS providers caused significant community confusion.
- enron_financial_intern: "TGE day almost over. Things are okay-ish. Not too bad."

**Nov 20 onwards:** Mod-discussion volume drops sharply. 100 messages Nov 20, then trending down to 10–35/day by December. Mods still on shift but conversations thinner. Jan 2026: barely 4–24 messages/day.

**Jan 5, 2026:** 120-message spike (the largest since November) — but content is entirely about game moderation (Stumble Guys, Smash Karts bounty). No substantive project discussion. **The mod team has completely shifted from project community management to running mini-games.** Three days after the Kyle meeting ($5,500 budget, zero salaries), the mod team is planning video game tournaments.

### Tone Analysis — Mod Team Over Time

| Period | Tone | Key Signal |
|--------|------|------------|
| Feb–May 2025 | Enthusiastic, optimistic | "Getting excited," whitepaper discussion, team-building |
| Jun 2025 | Frantic, high-energy | 877 messages/day, testnet chaos, lots of "help" |
| Jul–Aug 2025 | Workmanlike, stable | Node sale management, FAQ updates, shift coordination |
| Sep–Oct 2025 | Quieter, routine | Lower message counts, fewer crises |
| Nov 17–18 2025 | Crisis mode | Bots, scammers, "weapons free," "okay-ish," exhaustion |
| Nov 19–Dec 2025 | Subdued, mechanical | Shift handoffs, minimal project discussion |
| Jan 2026 | Disconnected from project | Mini-game planning dominates; no discussion of nodes, roadmap, or finance |

---

## PHASE 3: Community Sentiment Curve

### General-Chat Volume as Sentiment Proxy

Using general-chat message volume (400k+ messages across 46 parts) as an activity proxy, with targeted sampling at inflection points:

**Jun 11–12 (Testnet Launch) — FOMO euphoria:**
> "It's going ok! I am so so so so so so so so so happy I left my last job and started this." — Jason (BitBender), Jun 12 00:11

Community tone: pure excitement, confusion about setup, many new users asking basic questions. Engagement-farming behavior visible. High volume but low signal quality.

**Jul 11 (Secondary spike ~3,011):** Node sale announcement period. Community re-engaged, excited about purchasing. Mods managing FAQ load.

**Aug 14–17 (Volume collapse to ~172/day):** No specific event triggered this. The general-chat volume drop from 3,000+/day to under 200/day in less than a month is the clearest signal of organic community disengagement. The airdrop farmers had gotten what they came for (or realized there was nothing to farm yet) and left.

**Oct 25–26 (Minor recovery):** Binance Alpha / TGE proximity driving re-engagement.

**Nov 17–18 (TGE day — 2,226 peak):**
- Dominated by capsule questions, scammers, node purchase errors
- Binance Alpha launch specifically mentioned
- Community asking about circulating supply (jj3ss: "I'm not answering the circulating supply question because I do not know the answer")
- "80% of accounts were dead at capsule claim time" — the team used this as justification in public

**Nov–Dec 2025 Tone Samples (Dec 26 – Feb 5 part):**
> "Still dumping lol haha" — alex97xs, Dec 26
> "when claim airdrop?" — ekir299, Dec 26
> "the bottom of the abyss is right there" — tak09786, Dec 28
> "wish i knew they weretn charging yet before i bought tokens" — bellumlee, Dec 28

**Apr 2026 (final part, 1,632 messages covering Feb 5 – Apr 12):** Activity so thin that a 2-month period generates fewer messages than a single June 12 morning. The server is functionally dead.

---

## PHASE 3: Node-Owner-Chat — Post-Launch Disillusionment

The node-owner-chat (Dec 8, 2025 – Apr 9, 2026, 2,865 messages) is the most important sentiment channel for paid node operators — people who spent $150–$750 buying node licenses. This is the population with actual financial skin in the game.

### Key Themes

**Reward confusion and declining payouts:**
> "My node reward today is 222 dgrams" — nqpikaa1308, Dec 11
> "3 days ago 2800, yesterday 2400, now 1700" — alex97xs, Dec 11 (rewards down 40% in 3 days)
> "wow rewards went down by 50 datagram per node!" — western_monk, Dec 11
> "Haha! Could it be that today's node rewards have been reduced by 50% again?" — felix1688, Dec 12
> "reward avr is 391 today" — western_monk, Dec 16
> "Rewards falling harder each day" — western_monk, Dec 14

Kyle's explanation (Dec 11): "It looks like a lot of nodes experienced stability issues... our dev team is investigating the cause." No official post-mortem published.

**Price collapse anxiety:**
> "Price - 60% in 3 days. Going for pennies per node" — alex97xs, Dec 11
> "Price looks like it was artificially kept stable as long as nodes were selling and after boom dump" — alex97xs, Dec 11
> "Will dgram be only inflationary?" — alex97xs, Dec 11
> "Nobody buying dgram? Will there be any demand for it?" — alex97xs, Dec 15
> "One node gets you less than 100k dgram per year probably. 100k tokens is 160$" — alex97xs, Dec 15
> "Is more profitable to buy the token haha" — alex97xs, Dec 15
> "My liquidation price is 0.0027" — alex97xs, Dec 11

**"Looks ruggy, but it isn't"** — alex97xs, Dec 11. The community is beginning to use rug-pull language even while trying to dismiss it.

**Demand questions that expose product gaps:**
> "Nodes should've been bought with DGRAM and burned when bought. It would've helped the price." — alex97xs, Dec 11 (fundamental tokenomics critique)
> "What will happen with DGRAM used to buy nodes on 15 December? Burned?" — alex97xs, Dec 10
> "When nodes will purchase at DGRAM?" — nazmulnoyan, Dec 15
> "I wonder if we can receive the prices won in $ worth in DGRAM tokens?" — western_monk, Dec 16

**Uptime transparency:**
> "Ever since uptime percentage was removed, we haven't been able to make any sense of the uptime-sharing rewards at all" — nazmulnoyan, Dec 12. The team removed uptime percentage display from the dashboard — node operators lost visibility into their own earnings calculation.

**Kyle's consistent pattern:** Deflect individual concerns with "the dev team is investigating" or "this is normal" while acknowledging anomalies. "Whatever your rewards were today, this is likely not the trend." He never provides a written root-cause analysis in public.

---

## PHASE 4: Cross-Reference Synthesis

### 1. What Was Promised → What Was Delivered

| Promise | Delivery Status |
|---------|-----------------|
| Governance voting for node operators | Never delivered |
| AI inference enabled for node operators | Never re-enabled after testnet disability |
| 7.5% operator bonus from node sale | Confirmed undelivered as of Jan 2, 2026 (Kyle meeting) |
| VPN beta: "you got it for a year" | Internally acknowledged as false — "demo only" |
| Stable, growing node rewards | 40–50% reward drop within weeks of mainnet launch |
| Uptime percentage dashboard transparency | Removed, not restored |
| Datagram services creating DGRAM demand | No measurable demand materializing per community discussion |

### 2. What the Team Said Privately → What They Said Publicly

| Private (Mod-Discussion) | Public (Announcements/AMAs) |
|--------------------------|----------------------------|
| Kyle: "7% likelihood of people understanding" the reward plan | Announcements presented as clear and straightforward |
| enron_financial_intern: "Things are okay-ish. Not too bad." (TGE day) | TGE presented as triumphant launch |
| Jason orders "weapons free on bans and timeouts" Nov 18 | No mention of mass banning in public |
| Nephilimhoss bans "a few hundred" bot accounts that voted in poll | Community sees the poll results but not the manipulation |
| Gate article inaccurately described operator rewards — mods flagged it | Correction made quietly, no public clarification |
| enron_financial_intern: "Mhm. TGE day almost over." (exhausted tone) | TGE Stream broadcast as celebration |
| Jan 5, 2026: mod team planning Stumble Guys tournaments | Project claiming active development and roadmap progress |

### 3. When Community Sentiment Broke → What Event Triggered It

| Sentiment Break | Trigger | Evidence |
|-----------------|---------|----------|
| **Aug 13–17:** Daily volume 328 → 172 | No single event — organic exit of airdrop farmers who found no immediate reward | Node sale had been running ~3 weeks; no TGE yet. Farmers left. |
| **Nov 22 onwards:** Post-TGE crash | TGE price discovery — token listed and immediately dumped. Node rewards simultaneously dropped 40–50%. | "Price -60% in 3 days," "bottom of the abyss" |
| **Dec 2025:** Node-owner disengagement | Sustained price decline + reward decline + no dev updates | "Rewards falling harder each day," "will DGRAM be only inflationary?" |
| **Jan–Apr 2026:** Server effectively dead | Kyle meeting ($5,500 budget) represents the internal moment project is acknowledged as failing; community reflects this | Activity falls to <20 events/day by March |

### 4. Whether Moderation Activity Spiked at Sentiment Breaking Points (Censorship Indicator)

**Yes — with nuance:**

The Nov 17–18 spike (558+306 events) coincides with TGE day, when community was both most excited AND most negative about price/capsule value. BitBender issued "weapons free" ban authority on exactly the day community sentiment was most fragile. The bulk deletions on Nov 14 included suppression of:
- Questions about capsule selling price ("can the capsules sell for $150")
- Account selling ("who wants to buy my account? 167,612 points")
- Tokenomics questions ("supply 10b ya?")
- A premature "MAINNET is live" announcement (possibly true, deleted regardless)

**The "MAINNET is live" deletion — a social engineering attempt.** On Nov 14 at 4:10 AM, a newly-joined account posted "MAINNET is live / crosschaun bridge to chain 56 (bsc) is ready / explorer.datagram.network" and had all its messages immediately deleted. This was a scammer who had socially engineered Kyle into briefly posting a fraudulent announcement — the deletion was the correct moderation response to a live scam in progress, not suppression of accurate information. It does, however, illustrate the sophistication of the attack surface the team was managing in the days before TGE.

**The May 20–21 spike (589+709 events)** has no confirmed public trigger. This is the largest pre-testnet moderation spike and occurred during a period of heavy server growth. Likely a coordinated bot raid, but the absence of a documented public event makes it worth flagging.

---

## KEY FINDING SUMMARY

### The Five Most Significant Findings

**1. Jason (BitBender) was an active participant in the mod channel throughout — and Justin Hearn (the researcher) was a mod who was never meaningfully paid.**
Jason participated in mod-discussion, tested the node purchase flow personally on TGE day, and issued "weapons free on bans" authority. Justin (drinkyouroj) joined in July 2025, created community-facing content (capsule explainer videos, decision trees), and ran moderation shifts for approximately seven months. He received roughly one week's worth of pay — a partial personal payment from Jason out of his own pocket — and nothing from the project treasury. This is consistent with the Kyle meeting disclosure that zero team members had been paid since launch, and that the promised mod compensation (set up in the founding Google Sheets schedule in Feb 2025) was largely unfulfilled. The researcher has first-hand knowledge of the internal dynamics documented here.

**2. The community was functionally dead before the Kyle meeting.**
General-log shows the server declining from 14,852 events/day at testnet peak to <100 by January 2026. The Kyle meeting ($5,500 budget, zero salaries) was not the cause of collapse — it was the *documentation* of a collapse that the community data shows had been in progress since August 2025.

**3. TGE was managed under "weapons free" censorship.**
On the project's most important public day, the lead operator of the Discord issued open-ended ban authority to suppress negative commentary. The combination of a community vote poll + bot accounts flooding it + mass ban + reaction purge shows active manipulation of the community's expressed preferences.

**4. Node operator rewards declined within weeks of mainnet.**
The node-owner-chat documents 40–50% reward drops in December 2025 — while the team was still claiming the network was functioning normally. Uptime percentage transparency was removed during this period, preventing operators from auditing their own earnings. Kyle's response pattern was consistently "the devs are investigating" with no follow-up documentation.

**5. The 7.5% operator bonus erasure was known to the mod team before the Kyle meeting.**
On Nov 16, mods flagged that Gate.io published inaccurate operator reward figures. The correction of public-facing reward information, combined with the Jan 2, 2026 admission that the 7.5% bonus had never been distributed and they "don't know where it is," suggests this was an ongoing discrepancy that the mod team was aware of and managing around rather than resolving.

---

### Activity Timeline with Moderation Correlation

```
Feb 2025:     Server founded. Mods onboarded. Shift schedule established. Paid in crypto.
Feb 17–25:    Mass bot ban waves (300–413 events/day). Rapid server growth.
May 20–21:    UNEXPLAINED SPIKE (589+709 events). Largest pre-testnet moderation event.
Jun 11–12:    Testnet launch. General-log: 14,852 events Jun 12. Mod-discussion: 877 msgs.
              Euphoria phase. Jason (BitBender): "I am so happy I left my last job."
Jul 11:       Secondary spike (3,011 gen-log). Node sale hype.
Jul 21:       Node sale kickoff AMA. 25,000 nodes for sale.
Aug 13–17:    FIRST SENTIMENT BREAK. Volume collapses: 328 → 172/day. No recovery.
Oct 25–26:    Binance Alpha pre-announcement. Mini-recovery (332 gen-log events).
Nov 14–18:    TGE WEEK. General-log peaks at 2,226 (Nov 17). Mod-log peaks at 558 (Nov 17).
              Jason issues "weapons free" ban order. Community vote botted.
              Gate article inaccurately describes operator rewards — flagged internally.
              enron_financial_intern: "Things are okay-ish."
Nov 22+:      SECOND SENTIMENT BREAK. Price -60%. Rewards -40-50%. Server declining.
Dec 2025:     Node-owner-chat: "looks ruggy," "bottom of the abyss," "only inflationary?"
Jan 2, 2026:  Kyle meeting: $5,500 budget. Zero salaries. 7.5% bonus "don't know where it is."
Jan 5, 2026:  Mod team plans Stumble Guys tournament. 120 mod-discussion messages.
Mar–Apr 2026: General-log: 1–19 events/day. Server functionally abandoned.
```

---

*Sources: Datagram admin logs dump + Discord dump, analyzed April 13, 2026.*  
*Total data processed: ~700,000 Discord messages + 8,907 mod-log events.*
