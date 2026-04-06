# Wiki Log

Append-only chronological record of all wiki activity.
Parse recent entries with: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-04-06] update | Cross-links created between essays and research wiki

Created 3 concept pages to bridge essays ↔ research:
- `wiki/concepts/Institutional Gaslighting.md` — evidence control, narrative flooding, federal immunity (spans Minneapolis, Epstein, Trump investigations)
- `wiki/concepts/Leverage Erasure Through Automation.md` — automation erases bargaining power before jobs (robotics, ATM paradox, self-checkout)
- `wiki/concepts/Focal Point Coordination.md` — shared threats enable cooperation without enforcement (game theory, Schelling points, blockchain)

Created 3 entity pages for essay subjects:
- `wiki/entities/Bob Weir.md` — Grateful Dead co-founder; rhythm guitar innovation; 60-year career
- `wiki/entities/Jack Smith.md` — Former special counsel; investigation became subject of investigation
- `wiki/entities/Don Lemon.md` — Journalist arrested covering Minneapolis ICE church protests

Updated 6 article pages with cross-references:
- The Pastor Runs the Gestapo → Institutional Gaslighting, Don Lemon, Federal Immunity
- When Robots Leave the Lab → Leverage Erasure Through Automation
- Game Theory Assumes You're a Sociopath → Focal Point Coordination
- Trump Is Covering Up... → Institutional Gaslighting, Don Lemon
- The False Balance Trap → Jack Smith, Institutional Gaslighting
- The Other One Who Became That Guy → Bob Weir
- The Algorithm Ate My Amygdala → Institutional Gaslighting, Tech-State Conflict

Updated `wiki/index.md`: total pages 39 → 46, entities 14 → 17, concepts 10 → 13.

Result: Essays now integrate bidirectionally with research wiki. Readers can trace from essay → concept → other sources using same concept.

---

## [2026-04-06] ingest | 13 nonfiction essays from 2026 Substack archive

Processed remainder of "Drink Your OJ" published pieces from Jan-Feb 2026. All standalone nonfiction essays (not serialized fiction):

**Sports/Systems Analysis** (6 essays):
- `wiki/articles/Schneider Solved the Salary Cap While Everyone Else Complained.md` (Feb 8) — salary cap as optimization puzzle
- `wiki/articles/Nodes Over Numbers.md` (Jan 27) — NFC Championship game; output ≠ outcome
- `wiki/articles/How to Solve a Rival in Three Games.md` (Jan 18) — learning systems beat static systems
- `wiki/articles/13-3 The Box Score That Ended the Can Seattle'"'"'s Defense Travel? Debate.md` (Jan 4) — 49ers 3-13 Seahawks systematic suffocation
- `wiki/articles/Disguise and Destroy The Macdonald Method That Broke NFL Offenses.md` (Jan 3) — defense transformation through architectural change

**Politics/Geopolitics/Power** (4 essays):
- `wiki/articles/Bad Bunny Just Showed You Where Real Power Lives.md` (Feb 7) — corporate power pivot from domestic to global revenue
- `wiki/articles/The Pastor Runs the Gestapo.md` (Jan 30) — Minneapolis ICE shooting, Don Lemon arrest, federal immunity
- `wiki/articles/Trump Is Covering Up the Minneapolis ICE Shooting (Just Like He'"'"'s Covering Up Epstein).md` (Jan 12) — institutional gaslighting through evidence control
- `wiki/articles/The False Balance Trap.md` (Jan 7) — false equivalence launders authoritarianism

**Technology/Culture** (3 essays):
- `wiki/articles/Game Theory Assumes You'"'"'re a Sociopath. You'"'"'re Not..md` (Feb 5) — focal point coordination; humans cooperate more than game theory predicts
- `wiki/articles/When Robots Leave the Lab.md` (Feb 3) — physical AI mainstream; ownership determines outcomes
- `wiki/articles/The Algorithm Ate My Amygdala.md` (Jan 20) — algorithmic feeds destroyed sustained attention

**Cultural Biography** (1 essay):
- `wiki/articles/The Other One Who Became That Guy.md` (Jan 14) — Bob Weir, rhythm guitar innovation, 31-year solo career

**Key themes emerging**:
1. Systems thinking (information asymmetry, adaptation, optimization)
2. Power dynamics (who owns infrastructure, institutional immunity, distributed verification)
3. Focal points & cooperation (shared threats enable coordination)
4. Leverage erasure (automation kills bargaining power before jobs)
5. Institutional gaslighting (flooding narrative zones with competing truths)

**Newsletter positioning**: Publication has evolved from serialized fiction (HDftS) + nonfiction essays into integrated exploration of systems (sports, politics, technology, culture) with through-line: gap between what systems claim and what they actually do.

Updated: `wiki/index.md` (total pages 26 → 39, articles 6 → 19), preserved all entity/concept links.

---

## [2026-04-06] update | CLAUDE.md revised for actual domain

Updated schema from generic "Substack research" to actual newsletter domain: DePIN / Politics / Monetary Policy / Power. Added newsletter lens table, revised entity types (added country, infrastructure, asset, protocol), added "Newsletter Relevance" sections to page templates, added theme tags. Source page template now includes "Newsletter Angles" section.

---

## [2026-04-06] update | Published articles added; article schema created

Added `wiki/articles/` and `wiki/articles/episodes/` directories. CLAUDE.md updated with article page templates (fiction series, fiction episode, nonfiction). 6 article pages created:
- `wiki/articles/Help Desk for the Singularity — Series.md` — full series tracker: characters, motifs, themes, open questions
- `wiki/articles/episodes/HDftS E01-E04` — one page per episode
- `wiki/articles/This April Fools Article Has 2 Lies and 9 Ugly Truths.md`

**Publication identified**: "Drink Your OJ" (drinkyouroj.substack.com) by Justin Hearn, Michigan. HDftS is a serialized fiction series (4 episodes published, ongoing). Thematic through-line across fiction + nonfiction: the gap between what AI claims to be and what it actually is.

**Noted**: Recurring number 340 across E01 (open tickets), E03 (potholes filled), E04 (forms generated).

---

## [2026-04-06] update | Editorial pivot — removing DePIN as organizing frame

User decided to pivot away from DePIN as the newsletter's primary frame. Going forward, the publication's focus will be defined by what sources the user finds worth reading, not by a preset thesis. CLAUDE.md updated: newsletter lens is now emergent, DePIN removed as a required theme, tags are open-ended, entity types simplified. Existing DePIN-linked pages remain valid but are no longer privileged. Themes to be re-evaluated as sources accumulate.

---

## [2026-04-06] ingest | 3 sources: Iran/oil follow-up, Anthropic/Britain, Healthcare fraud

**Sources ingested**:

### Will blow up everything, take over Iran's oil — Trump says can reach deal by Monday
- Raw: `raw/Will blow up everything, take over Iran's oil Trump says can reach deal by Monday.md`
- New facts: Iran struck Kuwait/UAE/Bahrain energy sites; Iranian military defiance quotes; limited amnesty for negotiators; Trump "take over the oil" threat
- Pages created: `wiki/sources/Will blow up everything...md`, `wiki/concepts/Oil Seizure as Coercion.md`
- Pages updated: `wiki/entities/Iran.md` (sources: 1→2, new strikes + defiance quotes)

### Britain woos Anthropic expansion after US defence clash
- Raw: `raw/Britain woos Anthropic expansion after US defence clash, FT says.md`
- Pages created: `wiki/sources/Britain woos...md`, `wiki/entities/Anthropic.md`, `wiki/entities/Dario Amodei.md`, `wiki/entities/United Kingdom.md`, `wiki/concepts/Tech-State Conflict.md`, `wiki/concepts/AI Sovereignty.md`
- Pages updated: `wiki/concepts/Regulatory Weaponization.md` (new concept, created this session, spans 2 sources)

### 8 arrests in federal crackdown on alleged health care fraud in Southern California
- Raw: `raw/8 arrests made in federal crackdown...md`
- Pages created: `wiki/sources/8 arrests...md`, `wiki/entities/Mehmet Oz.md`
- Note: Low direct relevance to core DePIN themes; filed for political power angle

**Cross-session insight filed in overview**: Pattern emerging — state using regulatory/military tools to coerce control of strategically important infrastructure (energy, AI, healthcare). DePIN thesis is the structural response.

---

## [2026-04-06] ingest | Trump threatens hell on Iran infrastructure if Strait remains blocked

**Source**: Reuters, April 5, 2026. Authors: Bo Erickson, Humeyra Pamuk, Susan Heavey.
**Raw file**: `raw/Trump, on Easter, threatens 'hell' on Iran's infrastructure if Strait remains blocked.md`

**Pages created**:
- `wiki/sources/Trump threatens hell on Iran infrastructure if Strait remains blocked.md`
- `wiki/entities/Donald Trump.md`
- `wiki/entities/Iran.md`
- `wiki/entities/Strait of Hormuz.md`
- `wiki/entities/Iran Revolutionary Guards Corps.md`
- `wiki/entities/Marjorie Taylor Greene.md`
- `wiki/concepts/Chokepoint Control.md`
- `wiki/concepts/Infrastructure Warfare.md`
- `wiki/concepts/War-Driven Inflation.md`
- `wiki/concepts/Coalition Fracture.md`
- `wiki/concepts/Coercive Diplomacy.md`
- `wiki/overview.md` (updated)
- `wiki/index.md` (updated)

**Key takeaways filed**:
1. Trump set April 8 8PM ET deadline: open Strait or face strikes on power plants/bridges
2. US-Iran war began Feb 28, 2026; gas up ~37% (~$3 → $4.11/gal) in 5 weeks
3. Marjorie Taylor Greene broke publicly with Trump — coalition fracture signal

**Newsletter angles identified**: Chokepoint Control as DePIN's structural problem; war-driven inflation as Fed constraint; coalition fracture as political sustainability signal.

---

## [2026-04-06] note | Wiki initialized

Set up directory structure and schema. Files created:
- `CLAUDE.md` — schema and rules for the wiki agent
- `wiki/index.md` — master catalog
- `wiki/log.md` — this file
- `wiki/overview.md` — placeholder
- Directory structure: `raw/`, `raw/assets/`, `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/`

---

## [2026-04-06] ingest | Supreme Court vacates Steve Bannon's contempt conviction

**Source**: USA Today, Apr 6, 2026. Author: Maureen Groppe.
**Raw file**: `raw/Supreme Court clears way for Trump DOJ to wipe out Steve Bannon's conviction.md`

**Pages created**:
- `wiki/sources/Supreme Court clears way for Trump DOJ to wipe out Steve Bannon's conviction.md` — SCOTUS vacated conviction after sentence served; DOJ framing as "interests of justice"; pattern of institutional accommodation
- `wiki/entities/Steve Bannon.md` — Trump strategist; paradoxed protection: 2021 pardon (border wall fraud) + 2026 conviction erasure (contempt of Congress)
- `wiki/concepts/Retroactive Executive Protection.md` — Pattern of Trump erasing consequences through pardons, conviction vacation, prosecution abandonment; Bannon as paradigmatic case; Jack Smith prosecution abandonment as related dynamic

**Key takeaway**: Conviction vacation — erasing a conviction *after* the sentence is served — represents institutional capture distinct from ordinary pardon power. SCOTUS compliance without legal re-briefing suggests federal institutions have normalized accommodation of executive preferences.

**Cross-links**: Steve Bannon entity appears in [[Trump Is Covering Up the Minneapolis ICE Shooting]] (institutional gaslighting pattern); Retroactive Executive Protection relates to [[Federal Immunity Above Constitutional Law]]; Jack Smith entity updated with prosecution abandonment context.

Updated `wiki/index.md`: total pages 46 → 49, sources 4 → 5, entities 17 → 18, concepts 13 → 14.

---
