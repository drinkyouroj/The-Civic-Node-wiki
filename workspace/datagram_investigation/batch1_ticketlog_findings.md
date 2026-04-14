# Ticket-Log Forensic Analysis
**Source file:** `Datagram - Hidden Server Logs - 🎟︱ticket-log [1346545359853195388].json`  
**Analyzed:** 2026-04-13  
**Analyst note:** This is a Hidden Server Logs channel — users who filed tickets could NOT see it. Only staff could.

---

## Key Statistics

- **Total ticket closure events (messages):** 8,057
- **Total distinct tickets:** ~6,268 (highest ticket ID found: 6268, closed 2026-04-12)
- **Date range:** 2025-03-11 (ticket #4, first in log) to 2026-04-12 (ticket #6268, day before export)
- **Ticket system migration:** The system switched from Helper.gg bot (tickets numbered sequentially by user, e.g. "briansilva0428-ticket-5") to a "ModWise Audit Bot" / "Tickets v2" system around August 2025, coinciding with the node sale launch (ticket #4000+)
- **HTML transcripts preserved:** 100+ individual ticket conversation files in Attachments folder
- **Staff members who handled tickets (identified from transcripts):**
  - `kyleczech` (Kyle Czech, CEO — yes, the CEO personally handled support tickets)
  - `nephilimhoss` (NephilimHoss, Community Manager)
  - `enron_financial_intern` (Justin — the server owner referenced in this investigation)
  - `tradingcoach` (support mod)
  - `jj3ss` (support mod)
  - `devikinbop` (support mod)
  - `supercrunch.alt` / `James` (CTO/technical lead)
  - `444425725655777281` — kyleczech's Discord user ID, appearing as ticket closer in late 2025 posts

---

## Most Revealing Tickets (Verbatim Excerpts)

### TICKET: x8ken8x-g-ticket-3679 | 17/06/2025 | [VAGUE-TECH] [PROMISES]
**User complaint:** Node connected on v1.3.4 but earned zero points for 1 day 7 hours. Updated to v1.3.5 — now cannot connect at all.

**User (x8ken8x):** "so there is no solution? I use version 1.3.4 can connect, but the points do not increase. should I use version 1.3.4 again?"

**jj3ss (staff):** "That's what the dev team has shared with us so far. As soon as we have a new update, we'll let u know"

**User:** "I have done this many times but still can't connect."

**kyleczech (CEO):** "Your points haven't disappeared. Your uptime is hashed permanently on the chain and will be resynced to your account once the dev team has reached a level of network stability that they are comfortable with."

**kyleczech:** "Beyond all this, I encourage you to remember two things: 1) This is the testnet phase of the project. This is the time when things break regularly and we work together to fix them so that the project is fully ready for mainnet. 2) The Datagram team is immensely grateful for your contributions, both in compute resources and in feedback about your experience. As such, we will always prioritize rewarding you over not. We want all of us to win here 🙂"

**User:** "ok I'll see later my point will be updated or not, I have read the announcement from your CEO since the beginning. I understand this problem is complicated. but I am disappointed when you are busy and do not have time to reply to this ticket. your friends do not help to follow up even the purple mod said in general only tickets are answered. even though they do not know the problem."

**CLOSED BY STAFF** without resolution.

---

### TICKET: makaka86-g-ticket-3811 | 17-18/06/2025 | [PROMISES] [VAGUE-TECH]
**User complaint:** Node spinning/not connecting for days on MacBook. Tried all steps.

**makaka86:** "Also, looks like there is no license to link"
**makaka86:** "So no help?"

**kyleczech:** "Hi there! I'm sorry it's taken so long to get back to you! I was waiting to hear back from the tech team about it."
**kyleczech:** "This specific issue is going to be resolved in the next update, coming very soon!"
**kyleczech:** "Please do! If you still have issues after the update, open a new ticket and tag me directly! I will make it a priority to help you first ❤️"

**CLOSED BY STAFF.** "Coming very soon" was a persistent response pattern. No resolution logged.

---

### TICKET: ldldq-g-ticket-3808 | 17/06/2025 | [VAGUE-TECH] [PROMISES]
**User complaint:** Node shows connected but runtime hasn't increased for hours.

**tradingcoach (staff scripted FAQ response):**
> "FAQ: UPTIME/REWARD POINTS
> 1) I've been running my node for a long time. Why are my points not updating?
> There is a display bug for points and uptime. The dev team is working to fix it right now as they improve the stability and synchronization of the network.
> 3) How can I be sure that everything is being tracked?
> No matter what your uptime says in the node software, if you are connected, your uptime is being tracked and saved on the block chain. Once the dev team finishes work with the stability enhancements, those records will be used to make sure everyone receives all the rewards they have earned!"

**Analysis:** This is a pre-written FAQ script deployed repeatedly across dozens of tickets as a deflection. The same word-for-word response appears in at least 15+ tickets. It makes an extraordinary promise — that *all* uptime "is being tracked and saved on the blockchain" — with no mechanism for users to verify this claim. It is inherently unfalsifiable.

---

### TICKET: ashbittech-g-ticket-3309 | 15-16/06/2025 | [FINANCIAL] [VAGUE-TECH]
**User complaint:** Node online and connected (verified via Linux CLI output showing "ONLINE (Running and Connected)") but received zero rewards after 24 hours.

**ashbittech:** "my node is up from yesterday and shows the status: ✅ Datagram Node Status: ONLINE (Running and Connected) but I didn't receive any rewards."
**ashbittech:** "yes according to this I should have got at least 1 reward by now"

**jj3ss (staff):** "Have u read this [link to announcement]?"
**User:** "yes according to this I should have got at least 1 reward by now"

**CLOSED BY USER** (implicitly gave up). No answer given.

---

### TICKET: nephilimhoss-p-report-98 | 11/06/2025 | [INTERNAL — STAFF SOCIALIZING IN TICKET SYSTEM]
This ticket (ID 98, created by NephilimHoss the CM) shows senior staff — kyleczech (CEO), nephilimhoss (CM), enron_financial_intern (Justin, the server owner filing this complaint), and supercrunch.alt (James, CTO) — using the ticket system to share meme emojis, discuss the "rat king," and joke around. NephilimHoss sent a wall of Pepe frog emojis as an apparent test. This demonstrates that the ticket system was not treated as a serious support infrastructure by leadership.

---

### TICKET: nephilimhoss-ticket-2 | 04/03/2025 | [INTERNAL — STAFF ONBOARDING]
This is the earliest staff-side ticket. kyleczech (CEO), nephilimhoss, jj3ss, and tradingcoach are learning how to use the Helper.gg ticket bot. Kyle says "just turned on developer mode." The CEO was learning basic Discord functionality at the start of the project.

---

### TICKET: khan23707-ticket-43 | 30/04/2025 | [CENSOR]
Ambassador applicant khan23707 (Muhammad Usama Khan) applied with a fake/alias name "Falcon Swing." enron_financial_intern (Justin) confronted him:

**enron_financial_intern:** "we didnt ask for an alias, but your actual name."
**enron_financial_intern:** "as we will KYC all our ambassadors and have agreements signed."
**enron_financial_intern:** "why not put that into the typeform? wouldve saved you a lot of time"
**enron_financial_intern:** "odd, only the answers i had to ask you here are missing. i think you just didnt input it."

Notable: Datagram claimed to require real-name KYC for ambassadors. This suggests the project was collecting real identity data. The fact that they KYC'd unpaid ambassadors while running a public token node sale on testnet is a notable asymmetry.

---

### TICKET: x8ken8x-g-ticket-3679 (extended) | 17/06/2025 | [PROMISES] [CENSOR]
In the same ticket thread, user x8ken8x discovers they have **three licenses** on their account (a system bug). Staff never explained why or fixed it. Staff's standard scripted response ("logout, unlink, relink") was deployed repeatedly even though the user had already tried it multiple times before opening the ticket. This is a systemic support failure.

---

### TICKET: kyleczech-g-ticket-3645 | 16/06/2025 | [CENSOR]
A user (roni2021) was banned from the Datagram **Telegram group** for posting a Linux error code. The ban was by an automated bot. The user filed a Discord ticket to get unbanned:

**roni2021:** "I sending error code on telegram that's why ban me"
**kyleczech:** "Yeah, he got banned... I don't know how to unban in TG"

This is damning: users were being auto-banned from the Telegram group for posting **technical error messages** — i.e., the very evidence of the software not working was triggering automated censorship. A user cannot post their error logs without getting banned.

---

### TICKET: briansilva0428-ticket-5 | 14/03/2025 | [CENSOR]
User opened ticket, then left the server. The ticket was closed by staff with only the note "the user that created this ticket has left the guild." No resolution attempted. **"Closed by staff."** This pattern — closing tickets of departed users without any attempt to resolve or document the issue — recurs throughout the log.

---

## Timeline of Complaint Escalation

### Phase 1: March–April 2025 (Tickets 1–25)
- Very few tickets, all routine. Staff (kyleczech, nephilimhoss, jj3ss, tradingcoach) learning the system.
- Early tickets involve partnership solicitations (BitMart listing offer for $20K USDT — declined), admin setup, Discord role management.
- **No financial complaints visible.**

### Phase 2: May–June 2025 (Tickets 26–3811)
- **Massive surge** in ticket volume. The alpha testnet launched in late May/early June 2025 and attracted thousands of users running nodes.
- **Dominant complaint type:** Points/rewards not updating, node not connecting, uptime not being tracked.
- Staff deployed a **scripted FAQ template** to close tickets without resolution: "Your uptime is being tracked on the blockchain." This same script appears verbatim in 15+ tickets.
- The script includes the promise: *"Once the dev team finishes work with the stability enhancements, those records will be used to make sure everyone receives all the rewards they have earned."*
- Users ran nodes for 24–48 hours+ with zero rewards appearing. Staff response: "It's a display bug."
- **Notable pattern:** The CEO himself (kyleczech) handled many tickets and made direct personal promises: "I will make it a priority to help you first ❤️" and "We will always prioritize rewarding you."
- Points were promised to convert to tokens "at TGE" (Token Generation Event). Staff confirmed: "you'll earn airdrop points that will be converted into token at TGE 🙂"
- Users were being auto-banned from Telegram for posting error codes.

### Phase 3: July–August 2025 (Tickets ~3800–4580)
- **NODE SALE LAUNCHED:** August 10, 2025 (confirmed by FAQ dated July 29, 2025 and first ticket #4000 timestamped August 10, 2025).
- Node sale structure: 25,000 node licenses in 3 tiers, sold via USDT/USDC (ERC-20) on Ethereum. Prices not shown in the FAQ, but Tier 2 included a "Capsule" preloaded with DGRAM tokens and Tier 3 included Prime membership.
- NFT licenses were locked to the purchasing wallet for **one year** — meaning buyers could not sell or transfer them.
- The ticket system switched from Helper.gg to "Tickets v2" / "ModWise Audit Bot" around this time, indicating a system rebuild.
- Ticket volume increased dramatically. Most reasons listed as "No reason specified."
- **kyleczech still closing tickets** through at least September 2025 (confirmed: ticket #4577, September 29, 2025, closed by user ID `444425725655777281` = kyleczech).

### Phase 4: September–November 2025 (Tickets ~4577–5742)
- Ticket activity continues but details are sparse (no HTML transcripts for post-August tickets were captured in the Attachments folder — only the raw JSON log entries remain).
- Ticket ratings visible: ticket #4578 closed September 30, 2025 received **5 stars** (suggesting some users still felt supported).
- Close reasons remain "No reason specified" for the vast majority.
- One ticket (December 13, 2025, #5742) has a close reason of "Done - https://capsule-hub.com/faucet/" — indicating node/capsule-related support was still ongoing through December 2025.

### Phase 5: Late 2025–April 2026 (Tickets ~5742–6268)
- Ticket volume appears lower based on ID gaps.
- **February 25, 2026, Ticket #6250:** Close reason entered by `enron_financial_intern` (Justin) reads **"kys"** — "kill yourself." This is an extraordinarily hostile staff response to a support ticket. It suggests severe morale collapse at this point.
- Multiple tickets in February–April 2026 are automatically closed with reason: **"Automatically closed due to user leaving the server"** — indicating mass user departure.
- The ticket system continued operating until at least April 12, 2026 (the day before export), but the server appears to be in a ghost-server state with users leaving and tickets being auto-closed.

---

## Red Flags Found

### [PROMISES]
1. **Uptime-on-blockchain promise (repeated scripted response, June 2025):** "No matter what your uptime says in the node software, if you are connected, your uptime is being tracked and saved on the block chain. Once the dev team finishes work with the stability enhancements, those records will be used to make sure everyone receives all the rewards they have earned!" — This is an unfalsifiable, unverifiable promise. Users were running nodes with no reward appearing and being told to trust invisible blockchain records.

2. **CEO's personal promises in tickets:** kyleczech wrote directly to ticket-filers: "We will always prioritize rewarding you over not. We want all of us to win here 🙂" and "I will make it a priority to help you first ❤️" — These are direct personal assurances that were never fulfilled for the majority of complainants.

3. **"Coming very soon" pattern:** kyleczech responded to at least one user (makaka86, June 18, 2025) that a fix was "coming very soon!" — a phrase that functions as a delay tactic. The ticket was then closed.

4. **TGE promise:** Staff confirmed to users that "you'll earn airdrop points that will be converted into token at TGE." No TGE has occurred as of April 2026.

### [FINANCIAL]
1. **Node sale launched August 10, 2025** accepting USDT/USDC for node licenses. 25,000 licenses at multiple price tiers (Tier 3 = node + Capsule preloaded with DGRAM + Prime membership). Node license NFTs were locked for **one year** to the purchasing wallet, making them illiquid.

2. **Capsule product** (Tier 2/3 node sale bundle): A "Capsule" was pre-loaded with DGRAM tokens. A "capsule-hub.com/faucet" was referenced in a December 2025 ticket close reason. This suggests the Capsule infrastructure existed but DGRAM tokens within it may have had no liquidity or exit pathway.

3. **No refund mechanism found:** Across all reviewed transcripts, there is no ticket showing a user receiving a refund. No close reason ever mentions "refunded." The word "refund" does not appear in any ticket conversation reviewed.

4. **Points with no conversion path:** Users earned "airdrop points" for running nodes. Staff promised these would convert to tokens at TGE. As of April 2026, there is no evidence TGE occurred. Users who ran nodes for months may have earned nothing convertible.

5. **Node rewards not delivered:** Multiple tickets (ashbittech, x8ken8x, ldldq, and the scripted FAQ deployed across 15+ tickets) document that node runners were not receiving rewards. The standard answer was "it's a display bug" and "your uptime is on the blockchain."

### [VAGUE-TECH]
1. **"Display bug" explanation for zero rewards:** Staff consistently attributed missing points to a "display bug" rather than a technical failure. This is an unfalsifiable claim — if points are truly on-chain, why can't users verify them independently? No blockchain explorer link or verification mechanism was ever provided.

2. **Point tracking was entirely centralized:** Despite claims of blockchain storage, users had no way to independently verify their node uptime was being recorded. All verification depended on trusting the Datagram team.

3. **Multiple license bugs:** Many users found themselves with 2–3 licenses on a single account due to "system bugs." Staff's explanation: "we're in alpha phase." The existence of phantom licenses suggests the backend tracking was unreliable.

4. **Node connection issues systemic:** Dozens of tickets document nodes that either never connect, connect and immediately disconnect, or connect without counting uptime. The core product — running a node and earning rewards — did not reliably function during the alpha testnet period when nodes were being pitched for sale.

5. **CEO reference to "stability enhancements" announcement:** kyleczech directed frustrated users to a CEO announcement about stability issues (referenced in the ticket transcript but not reproduced here). The CEO acknowledged the infrastructure was unstable while the node sale was being prepared.

### [CENSOR]
1. **Auto-ban for posting error codes (Telegram):** User roni2021 was automatically banned from the Datagram Telegram group for posting a Linux error message (`failed to read JSON message : failed to get reader : receive close frame : status = StatusInternalError`). The very act of reporting a software problem triggered censorship. kyleczech acknowledged the user "got banned" and admitted he didn't know how to unban in Telegram.

2. **Ticket closed on user departure:** Multiple tickets were closed by staff immediately upon users leaving the server, with no record of the user's complaint or any resolution attempt. This erases the complaint from the record.

3. **Staff closing tickets without answers:** The most common ticket close pattern in the early period (March–June 2025) is "Closed by staff" with no resolution. Users report making tickets, getting no response, and the ticket being silently closed.

4. **"kys" close reason (February 25, 2026, Ticket #6250):** A support ticket was closed by enron_financial_intern (Justin) with the close reason "kys" ("kill yourself"). This represents the complete breakdown of any pretense of professional support operations. By this point the server was operating in a post-collapse state.

5. **Ticket system used for staff socializing:** The ticket channel was used by staff (kyleczech, nephilimhoss, enron_financial_intern, supercrunch.alt) to share memes and jokes (ticket #98, June 11, 2025). This Hidden Server Log — invisible to users — shows staff treated the support infrastructure as a private playground while user complaints went unresolved.

### [PRESSURE]
1. **No direct in-ticket sales pressure identified** in reviewed transcripts. However, the node sale FAQ (published July 29, 2025) was posted in the server, and "Prime" tier node purchasers were promised a 1-year Prime membership with no elaboration on what that meant.

2. **Psychological investment creation:** The scripted FAQ template ("your uptime is being saved on the blockchain, we will make sure everyone receives all rewards they have earned") was designed to prevent users from abandoning the project. By assuring users their past efforts were permanently recorded and would be rewarded, staff incentivized continued node operation — which sustained server metrics and community size during the node sale.

3. **Alpha testnet used as marketing for node sale:** The testnet ran from approximately May/June 2025. The node sale launched August 10–12, 2025. Users who had been promised their testnet activity would be rewarded were also the primary audience for the node sale pitch. The testnet period functioned as audience acquisition for the sale.

### [EXIT]
1. **Capsule token exit pathway unknown:** The node sale included "Capsules" pre-loaded with DGRAM tokens. A December 2025 ticket close reason references "capsule-hub.com/faucet/" — a faucet URL, suggesting DGRAM had test/limited distribution. If DGRAM never launched with real market liquidity, capsule holders would have worthless tokens.

2. **NFT licenses locked 1 year:** All node licenses purchased in the August 2025 sale were locked to the purchasing wallet for one year. Even if a buyer wanted to exit, they could not transfer or sell their license NFT until August 2026. This lock-in structure eliminated the ability to exit the investment.

3. **Mass user departure (late 2025–2026):** Ticket close reason "Automatically closed due to user leaving the server" appears multiple times in February–April 2026, indicating significant user departures. Users filing tickets then immediately leaving the server suggests loss of hope.

4. **Server still running with ghost activity:** Tickets were still being processed through April 12, 2026 (exported date minus one day). The presence of ongoing tickets (and the "kys" close reason in February 2026) suggests the server continued running in a degraded, hostile state long after any legitimate project activity would have ceased.

---

## Structural Analysis

### The Support System as Evidence of a Non-Functional Product
The volume of tickets about basic product failures (node not connecting, points not accruing, rewards not appearing) during the testnet phase — which immediately preceded the node sale — is the most damning evidence in this log. The pattern is:

1. User runs node as instructed.
2. Node either doesn't connect, connects but disconnects immediately, or connects without earning points.
3. User files ticket.
4. Staff deploys scripted response: "display bug, points on blockchain, keep running."
5. Ticket closed — usually by staff, sometimes by frustrated user.
6. No resolution reached.

This pattern repeated across hundreds of tickets in June 2025 — the exact period when the node sale was being prepared and announced (sale FAQ posted July 29, 2025; sale launched August 10, 2025).

**The node sale sold a product that demonstrably did not work during the sales period.**

### Staff Identity
- **kyleczech** = Kyle Czech, CEO. He personally handled support tickets, made personal promises in ticket conversations, and his user ID (`444425725655777281`) appears closing tickets through at least September 2025.
- **enron_financial_intern** = Justin (the person who commissioned this investigation). His presence in tickets is as a staff member handling support and ambassador applications. His "kys" close reason in February 2026 (ticket #6250) suggests he had by then reached a breaking point with the project — which aligns with the reported timeline of his departure and the CEO fleeing.
- **supercrunch.alt / James** = Technical lead or CTO. Handles escalated technical tickets, references the CEO's announcements.
- **nephilimhoss** = NephilimHoss, Community Manager. Active in both ticket handling and server administration.

### Ticket Volume as Fraud Indicator
The ticket system went from ~3,800 tickets in the Helper.gg era (through approximately August 2025) to an additional ~2,400+ tickets in the Tickets v2 era (August 2025 to April 2026). This surge coincides precisely with:
- The alpha testnet launch (May/June 2025)
- The node sale (August 2025)
- The post-sale period when purchased nodes presumably didn't deliver promised returns

The volume of complaints is consistent with a large user base experiencing financial harm from a product that did not function as promised.

---

## Key Evidence Summary for Investigation

| Evidence Item | Date | Red Flag Category | Significance |
|---|---|---|---|
| Scripted "uptime is on blockchain" FAQ deployed to 15+ tickets | June 2025 | [PROMISES] [VAGUE-TECH] | Unfalsifiable promise used to dismiss complaints |
| CEO (kyleczech) personally promising "we will always prioritize rewarding you" | June 2025 | [PROMISES] | Executive-level fraud if promise not kept |
| User auto-banned from Telegram for posting error code | June 2025 | [CENSOR] | Evidence suppression via automated censorship |
| 3-license bug; staff: "we're in alpha phase" | June 2025 | [VAGUE-TECH] | Unreliable tracking = rewards cannot be verified |
| Node sale launched August 10, 2025 (USDT/USDC, 25K licenses) | August 2025 | [FINANCIAL] | Real money exchanged for a non-functional product |
| Node license NFTs locked 1 year to purchasing wallet | August 2025 | [FINANCIAL] [EXIT] | Illiquid investment with no exit mechanism |
| Zero refunds documented across entire ticket history | 2025–2026 | [FINANCIAL] | No consumer protection mechanism |
| "kys" close reason on ticket by staff member (Justin) | February 26, 2026 | [CENSOR] | Morale collapse; hostile operations |
| Mass "user left server" auto-closures | Feb–April 2026 | [EXIT] | Users abandoning project en masse |
| Staff socializing via ticket system (meme ticket #98) | June 2025 | [INTERNAL] | Support not taken seriously by leadership |
| TGE promised but not delivered (as of April 2026) | 2025–2026 | [PROMISES] [EXIT] | Core promise of token conversion never fulfilled |

---

## Notes on Limitations

- HTML transcripts in the Attachments folder cover tickets #1–approximately #3811 (before the node sale). **No HTML transcripts are preserved for node sale era tickets** (#4000+), which are the most financially significant. The JSON log shows ticket closure metadata only for that period — not conversation content.
- Without the transcript content from August 2025 onward, we cannot directly read what users complained about after buying nodes. The metadata (close reasons, ticket openers/closers) tells us the volume but not the content.
- The "kys" close reason (ticket #6250, February 2026) was entered by user ID `758112217999867926` = enron_financial_intern = Justin. This may be relevant context for the broader investigation but should be considered within the full timeline of events.

---

*Report generated from direct analysis of ticket log JSON (573,011 lines) and 100+ HTML transcript files.*
