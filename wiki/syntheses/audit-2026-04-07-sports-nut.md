---
title: "NFL Cluster Audit — 2026-04-07 (Sports Nut)"
type: synthesis
tags: [nfl, seahawks, audit, quality-control, meta]
created: 2026-04-07
updated: 2026-04-07
sources: 0
query: "Audit the NFL/Seahawks cluster for football accuracy, dynasty framing, coaching-tree analysis, game-recap consolidation, cross-cluster coherence, and Super Bowl LX sourcing."
---

## Answer

The NFL cluster is large (~50 sources, 2 concept pages, 7 entity pages) and internally impressive-looking, but it has real problems a football-literate reader will catch immediately. The biggest: **the wiki asserts the Seahawks won Super Bowl LX but contains no Super Bowl LX game recap.** The championship is implied through context — the latest event actually sourced is the Jan 26, 2026 NFC Championship. Every "Super Bowl LX champion" claim in the wiki is therefore running ahead of its raw material.

On top of that, two concept pages contradict each other on basic defensive rankings, the Schneider "zero holdovers" claim is directly contradicted by the wiki's own sources, the "3-Buzz" technical description is wrong, the coaching-tree "natural experiment" has a load of confounders the wiki waves past, the bracket has an internal contradiction (49ers playing in the Divisional Round despite not being a seeded playoff team per the Wikipedia source the wiki cites), and the game-recap consolidation work was undone — at least two games now have 3 separate source files each. The overall "organizational continuity as master variable" framing is defensible but is mostly asserted rather than tested; the football cluster functions more as illustrative fan material than as a rigorous case study.

---

## Findings (prioritized)

### P0 — Factual contradictions and sourcing gaps

**P0-1. Super Bowl LX has no game-recap source.** Every wiki claim that "Seahawks won Super Bowl LX" traces back to either (a) the pre-game Schneider profile (Feb 6, 2026, before kickoff — `wiki/sources/Super Bowl LX — Homegrown GM John Schneider at the Peak of Powers.md:10`), (b) the NFC Championship recap (`wiki/sources/NFC Championship — Seahawks 31 Rams 27.md:10`), or (c) the Wikipedia playoffs entry (`wiki/sources/2025-26 NFL Playoffs Wikipedia.md:15`). There is no raw source for Super Bowl LX itself — not in `raw/` (see Glob of `raw/*Super Bowl*` and `raw/*Bowl LX*`), not in `wiki/sources/`. Entity pages (`wiki/entities/Seattle Seahawks.md:13`, `wiki/entities/John Schneider.md:18`, `wiki/entities/Sam Darnold.md:13`, `wiki/entities/Mike Macdonald.md:13`) all assert the Super Bowl win as fact. The overview (`wiki/overview.md:94, 100`) treats it as closed. **The centerpiece event of the cluster is unsourced.** If the goal is to use the NFL cluster as a test case for organizational continuity, it has to actually contain the thing it's building to.

**P0-2. The Macdonald "25th → 2nd in one season" claim is wrong by the wiki's own sources.**
- `wiki/entities/Mike Macdonald.md:18` says: "took a 25th-ranked defense to 2nd-ranked in one season."
- `wiki/entities/Seattle Seahawks.md:20` says: "defense improved from 25th to 11th in points allowed" in 2024 (Year 1).
- `wiki/sources/How Macdonald Is Authoring a New Chapter of Seahawks Defensive Dominance.md:23` says: "Seahawks ranked 25th (2023) → 11th (2024) → 7th through Week 8, 2025."
- `wiki/articles/Disguise and Destroy The Macdonald Method That Broke NFL Offenses.md:26` correctly says "25th to 11th (2024) to 2nd (2025)" — **two seasons**, and with the Year 2 "2nd" rank itself only loosely supported (the best stat available from `wiki/sources/Where Seahawks Defense Ranks Among League's Best.md:19-26` as of Week 12 is 3rd in points allowed / 1st in DVOA / 2nd in YPP).

The "one season" framing on the Macdonald entity page (`wiki/entities/Mike Macdonald.md:18`) is flatly contradicted by every other source in the cluster. Fix: either rewrite to "25th (2023) → 11th (Year 1, 2024) → top-3 (Year 2, 2025)" or scope the claim to the Ravens (where the single-season 19th → 3rd jump is actually supported).

**P0-3. "Zero player or coaching holdovers" is directly contradicted.** `wiki/sources/Super Bowl LX — Homegrown GM John Schneider at the Peak of Powers.md:19` quotes: "First GM ever to lead a team to the Super Bowl with zero holdovers from any previous roster (player or coaching staff)." This is repeated in four places: `wiki/entities/Seattle Seahawks.md:22`, `wiki/entities/John Schneider.md:19`, `wiki/concepts/Organizational Continuity.md:22`, `wiki/overview.md:96`.

But `wiki/sources/Seahawks Are Biggest Threat to Overthrow the NFC.md:24` explicitly states: **"9 of the Seahawks' 2023 defensive starters still on the 2025 roster."** The "zero holdovers" claim cannot be true if 9 of 11 defensive starters are holdovers. The original source is pre-SB team PR ("WBAY profile") and should be treated as marketing language, not fact. The wiki should flag this contradiction with the `⚠️ Contradiction` marker required by `CLAUDE.md:#6`. It doesn't.

This matters more than it looks: "zero holdovers" is the single most cited data point in the Schneider-as-systems-thinker narrative. If it's wrong, the "complete rebuild in one offseason" framing collapses into something much more mundane — same core defense plus a QB swap plus a WR swap.

**P0-4. The Darnold "5th QB" factoid is contradictory.**
- `wiki/entities/Sam Darnold.md:22`: "5th QB in NFL history with multiple 14-win seasons (Brady, Mahomes, Manning, Montana)."
- `wiki/sources/How Sam Darnold's Time in Carolina Paved the Way for Career Resurgence.md:24`: "only the fifth QB in NFL history to win 13+ games in consecutive seasons — alongside Brady, Favre, Manning, Rodgers."

The two statements describe different groups, different thresholds (14+ vs. 13+), different company. Neither is clearly sourced — both are team-media factoids. Both are also likely to fail a fact check (Mahomes has clearly had multiple 14-win seasons; Favre had multiple 13-win years but not multiple 14-win years; "consecutive" is doing a lot of work). The entity page appears to be paraphrasing from memory. Fix: drop the "5th QB" claim entirely unless a non-team source can be pinned to it.

---

### P1 — Football-accuracy problems a film watcher will catch

**P1-1. The "3-Buzz" description is wrong.** `wiki/concepts/Defensive Scheme Architecture.md:31` says: "The 3-Buzz concept: Macdonald's signature zone shell — looks like one coverage pre-snap, rotates to another post-snap." `wiki/sources/Inside Mike Macdonald's Seahawks Defense Philosophy.md:22` describes it as "a zone shell that disguises coverages pre-snap and rotates post-snap."

That is not what 3-Buzz is. **3-Buzz is a specific coverage**: Cover 3 with a safety "buzzing" down into an underneath zone (typically hook/curl or seam), creating a 3-deep/4-under shell instead of the traditional 3-deep/3-under. It's typically shown from a two-high presnap look and rotates to single-high at the snap, and it exists to defend crossers and seam routes against spread formations. It is *one coverage inside the broader disguise system*, not the disguise system itself.

The wiki is using "3-Buzz" as a marketing synonym for "Macdonald's scheme." This is parroted from the Cody Alexander piece — the source is a schematic deep-dive that introduces 3-Buzz as *one of* Macdonald's favored calls, but the wiki has promoted it to the whole architecture. A football-literate reader will flag this instantly. Fix: describe 3-Buzz as a specific coverage variant within the Macdonald system (which is more accurately described as an aggressive MOF-disguise, 2-high-to-1-high-rotation, simulated-pressure scheme).

**P1-2. "Scheme over personnel" is asserted, not tested, for Year 1.** `wiki/concepts/Defensive Scheme Architecture.md:29` says "Seahawks Year 1 (2024): Defense improved from 21st in points allowed (first half) to tied 3rd (second half) — the scheme was installing in real time." There are two problems:
1. "21st in first half, 3rd in second half" is a common-sense sign of scheme installation but is also the kind of split that can arise from opponent quality and personnel injuries. The wiki never checks schedule strength of first-half vs. second-half opponents — which is the standard way of distinguishing "scheme kicked in" from "easier schedule kicked in." For a piece that keeps claiming "architecture beats talent," this is the obvious control the wiki doesn't run.
2. The whole "same players, different scheme" framing rests on the claim that the roster was substantially unchanged from 2023 to 2024. That needs at least a line about offseason roster churn (which was real — Adams/Diggs/Wagner were all gone, Witherspoon was in Year 2, etc.). The wiki assumes continuity of personnel to prove discontinuity of scheme, but never demonstrates that assumption.

**P1-3. The "coaching tree control group" claim is not a control group.** `wiki/concepts/Defensive Scheme Architecture.md:28` and `wiki/sources/Seahawks Are Biggest Threat to Overthrow the NFC.md:22-24` both lean heavily on "Macdonald's former assistants at Baltimore, Miami, Tennessee all failing simultaneously = structural/scheme evidence." The Seaside Joe source, written in Week 4, lists Ravens 32nd in points allowed, Dolphins 30th, Titans 26th.

This is not a control group. Problems a football-literate reader should notice:
- **Personnel is not controlled.** The Ravens lost multiple starters off Macdonald's 2023 unit (Patrick Queen to Pittsburgh, Geno Stone to Cincinnati, Jadeveon Clowney gone, etc.). Miami lost Bradley Chubb to injury multiple years running, has cap-constrained personnel, and Jalen Ramsey situations. Tennessee is in an organizational free-fall on offense that affects defensive time-on-field dramatically. None of this is mentioned.
- **Schedule strength is not controlled.** The AFC North is a murderers' row; the Ravens playing without Queen against Burrow/Mahomes/Jackson divisional opponents isn't the same assignment as the Seahawks playing Bryce Young and Geno Smith.
- **Time-in-role is not controlled.** Orr is a first-time DC; Weaver is in Year 2 at a different org; Wilson is in Year 1. Pete Carroll as a first-year HC went 7-9; then won a Super Bowl four years later. Year 1 DC data is noisy.
- **The sample is Week 4.** The wiki's own source is dated Sept 29, 2025 — the "coaching tree all failing" claim is drawn from four games. By Week 17 the Ravens had recovered meaningfully (this would need to be verified from later sources). Using an early-season snapshot as evidence that scheme is the master variable is post-hoc pattern-matching.

The underlying intuition — that Macdonald is the differential variable — may well be correct. But the wiki presents it as "natural experiment" / "control group" evidence, which it isn't. This is correlation-dressed-as-causation, and the wiki's own concept page (`wiki/concepts/Defensive Scheme Architecture.md:28`) leans on it as its single strongest piece of evidence. Fix: frame it as suggestive, list the confounders, and stop calling it a control group.

**P1-4. "Comp picks + restructured contracts" is not distinctive Schneider tradecraft.** `wiki/concepts/Salary Cap Optimization.md` frames the Schneider method as: cheap rookie deals, comp picks, strategic veteran signings, "never restructure to defer" (also `wiki/entities/John Schneider.md:26`). Two problems:
1. Every competently-run NFL front office does this. Howie Roseman (Eagles), Brett Veach (Chiefs), Les Snead (Rams, though they're the counterexample), Bob Quinn in Detroit, Joe Douglas (back when he was functional): all of them treat comp picks and rookie-deal leverage as central. There is nothing distinctive about "maximizing comp picks" as a 2026 philosophy — it's table stakes. Schneider's distinctive move, if there is one, is the combination of long tenure + clean cap sheets + not chasing his own mistakes by restructuring. The wiki should say that explicitly rather than listing standard practice as if it were Schneider's secret sauce.
2. The "never restructure to defer" line in the Schneider entity page (`wiki/entities/John Schneider.md:26`) would need to actually be true to be a thesis. Schneider has used restructures (the specifics require a separate check), and `wiki/sources/Is the NFL Salary Cap Real or a Mirage.md` itself presents restructures as a neutral tool, not a moral failing. The wiki has imported a fan-narrative about Schneider's "discipline" without evidence.

**P1-5. Darnold's Carolina arc is heavily sanitized.** `wiki/sources/How Sam Darnold's Time in Carolina Paved the Way for Career Resurgence.md` is explicitly team-produced content (Seahawks.com, flagged in the source's own Notes at line 46). The "4-2 in final 6 games, threw 7 TDs and 3 INTs" framing in `wiki/entities/Sam Darnold.md:21` comes from that source and skips over: the 2021 injury year, the 2022 Baker Mayfield benching, the overall Panthers record during his starts, his career completion% and QBR during those years, and the fact that the "4-2 finishing stretch" happened against a soft schedule in games that had no playoff implications. The entity page (`wiki/entities/Sam Darnold.md:21`) says "Jets (2018-2020, failure) → Panthers (2021-2022, adversity, 4-2 in final 6 games)" — that's the team-media arc, not the actual trajectory. A football-literate reader will notice the Panthers years are being written up as "adversity that built him" when they were largely "replacement-level QB the team kept benching."

The wiki should keep the Darnold-Carolina source for documentation purposes but note in the `sources:` field that it's team-produced, and the entity page should reference non-team sources (ESPN, PFF, Football Outsiders) for performance claims. Currently there are none.

---

### P2 — Consolidation, coherence, and internal-bracket problems

**P2-1. Game-recap consolidation was undone.** The wiki intended to consolidate multi-source game coverage into single files, and the consolidation pages exist (e.g., `wiki/sources/Seahawks 38-37 OT Comeback Over Rams — Multiple Perspectives.md` which says it consolidates 7 raw files; `wiki/sources/Seahawks 13-3 Win Over 49ers — NFC West Title Clincher.md` which consolidates 6). But the atomic per-outlet files were never removed from the index. For the Week 16 Rams OT game we now have:
- `wiki/sources/Seahawks 38-37 OT Comeback Over Rams — Multiple Perspectives.md` (the "consolidated" page)
- `wiki/sources/Seahawks OT Win Over Rams — December 2025.md` (single ESPN recap)
- `wiki/sources/Seahawks OT Win Over Rams — Regular Season Trilogy Context.md` (aggregated trilogy context)

For the Week 18 49ers 13-3 game we now have:
- `wiki/sources/Seahawks 13-3 Win Over 49ers — NFC West Title Clincher.md` (consolidated, 6 raw files)
- `wiki/sources/Seahawks Clinch NFC West — 13-3 Win Over 49ers.md` (single ESPN score page)
- `wiki/sources/Seahawks Beat 49ers Week 18 — 4 Takeaways.md` (Fox Sports)

For the NFC Championship:
- `wiki/sources/NFC Championship — Seahawks 31 Rams 27.md`
- `wiki/sources/Rams Fall to Seahawks 31-27 in NFC Championship.md`
- `wiki/sources/NFC Championship — ESPN Game Analysis.md`
- `wiki/sources/Sam Darnold Seahawks Advance to Super Bowl — Fox Sports.md`

Four files for one game is defensible if they're each contributing different angles (ESPN technical analysis is legitimately different from an AP wire recap), but `wiki/index.md:403-405` lists them all as separate entries without noting the overlap. Fix: merge the redundant recap pages, keep the "ESPN Game Analysis" and one wire-service recap as distinct artifacts, and mark the rest as superseded. This matters because `sources:` counters on concept pages are being inflated by the fragmentation — `wiki/concepts/Defensive Scheme Architecture.md` claims 9 sources but several are duplicates of the same games.

**P2-2. Bracket contradiction: phantom 49ers playoff game.** `wiki/sources/2025-26 NFL Playoffs Wikipedia.md:19` lists the NFC seeds as Seahawks (1), Bears (2), Eagles (3), Panthers (4), Rams (5). The 49ers are not in the bracket. But `wiki/sources/Seahawks 41-6 Divisional Win Over 49ers.md` (raw file `raw/Seahawks 41-6 49ers (Jan 17, 2026) Final Score - ESPN.md`) describes a Jan 17, 2026 Divisional Round game, 41-6, against the 49ers. This is impossible under the bracket as sourced: the 49ers aren't in the playoffs.

Either (a) the Wikipedia source is wrong/incomplete and the 49ers were actually seeded, (b) the 41-6 game is from a different round or a fabricated/misattributed raw file, or (c) the 41-6 game is the Week 18 13-3 rematch mis-dated. The wiki never notices this contradiction and the overview.md explicitly references "41-6 divisional rematch" as if it happened (`wiki/overview.md:100`). **This is exactly the kind of error the `⚠️ Contradiction` marker exists for, and it's nowhere flagged.** A reader will catch it in thirty seconds.

**P2-3. AFC champion is the Patriots.** `wiki/sources/2025-26 NFL Playoffs Wikipedia.md:20` has the Patriots as AFC champions in 2026. The 2025-26 Patriots are a rebuilding team two years removed from the Belichick era and there is no accompanying raw material anywhere in the cluster supporting a Patriots Super Bowl run. Combined with the absence of any Super Bowl LX game recap (P0-1), this suggests parts of this cluster are operating as **near-future / alt-history projection masquerading as sourced fact**. That's fine as a creative exercise, but it should be flagged in the source pages — currently these are presented as encyclopedic reference material with the normal `type: source` frontmatter, and downstream pages (entities, concepts, overview) treat them as fact.

**P2-4. "Road record 10-1 under Macdonald since 2024 (best in NFL over that span)" is presented as a brag but is a weird cut of data.** `wiki/entities/Seattle Seahawks.md:23` and `wiki/sources/How Macdonald Is Authoring a New Chapter of Seahawks Defensive Dominance.md:26` both cite it. "Best in NFL since 2024" is a fine marketing stat but is sensitive to cutoff — measuring a two-year record where the team went 10-7 then 14-3 is an arbitrary window and a small sample (at most ~17 road games). Not wrong, but the wiki treats it as meaningful evidence of Macdonald's impact when it's mostly a consequence of the Year 2 team being very good.

---

### P3 — Framing, coherence, and what the cluster is actually for

**P3-1. The "12-14 true dynasties" claim is undefended and potentially inflated.** `wiki/concepts/NFL Dynasty.md:12` asserts "Roughly 12-14 true dynasties exist in NFL history across 100 years." The concept page then lists six (Bears 40-46, Dolphins/Steelers 70s, Cowboys 90s, two Patriots eras, 2012-15 Seahawks "mini-dynasty," 2026 Seahawks). That's nowhere near 12-14. Where are the Packers of the 60s (inarguable top-2 dynasty ever), 49ers 80s–90s (4 SBs, Walsh/Seifert continuity), Cowboys 60s-70s, Raiders late 70s-early 80s, Chiefs 2019-present (3 SBs, 5 appearances — the wiki skips this entirely because the cluster is about continuity-as-master-variable and the Chiefs are a strong counter-case: they're personnel-first, Mahomes-centered)?

The omission of the current Chiefs from a dynasty-framework page in 2026 is a tell. The Chiefs are the single most recent and most relevant comparison to the 2026 Seahawks claim, and a dynasty list that ends in a celebration of the Seahawks without engaging with Mahomes-Reid is advocacy, not analysis. The cluster is working backward from "Seahawks are the new model" and pruning evidence that complicates it.

Also: the "Brady-Belichick benchmark (6 SBs)" framing in `wiki/overview.md:99` actually *does* engage with the strongest case — good — but the dynasty concept page then rates the 2026 Seahawks alongside historical dynasties after one Super Bowl win. That's not a dynasty. A dynasty requires sustained multi-year dominance; the Seahawks have two SB wins across two eras twelve years apart with a different coach, QB, and GM between them. The wiki keeps sliding between "potential dynasty window" (defensible) and "dynasty" (not yet supported).

**P3-2. "Organizational continuity is the master variable" is post-hoc.** `wiki/overview.md:126` frames the NFL cluster as a "test case" for organizational continuity as the master variable of sustained dominance. But the cluster doesn't test that thesis — it illustrates it with confirming examples. Missing:
- **Disconfirming cases**: teams with long organizational continuity that have *not* won (Bengals under Mike Brown, Lions pre-2023, the entire Carolina organization). The thesis should at least address why continuity doesn't work there.
- **Counterexamples**: teams that won *without* continuity (Giants 2007 and 2011 — Eli and Coughlin, yes, but the surrounding organization was turbulent; Broncos 2015 — a dying Manning plus one great defensive year; Buccaneers 2020 — Brady at 43 literally just showed up).
- **The Chiefs**: continuity exists (Reid + Mahomes + Veach) but the wiki doesn't analyze them.
- **The failure mode** of continuity: Carroll's 2021-23 decline is mentioned at `wiki/concepts/Organizational Continuity.md:26` but only as a concessional footnote, not as a test of the thesis.

The thesis is worth keeping — it's probably directionally correct — but the wiki should at least note that it's doing case-selection, not hypothesis-testing.

**P3-3. The cross-cluster coherence claim mostly works but needs to earn it.** `wiki/overview.md:126-136` argues the NFL cluster connects to the broader wiki via "chokepoint control" and "infrastructure as master variable" (the cap and scheme as analogues to the Strait of Hormuz and the Fed). This is cute but mostly metaphorical. The concrete connection that *does* work is the Schelling-focal-point mirror in `wiki/overview.md:136`: Macdonald's pre-snap ambiguity as the defensive version of exploiting/denying focal coordination. That's a real analytical link. The rest ("dynasty-building is chokepoint control") is more forced. Fix: keep the Schelling link, downgrade the chokepoint metaphor elsewhere.

---

## Specific page-level errata to fix

- `wiki/entities/Mike Macdonald.md:18` — "25th-ranked defense to 2nd-ranked in one season" is wrong per every other source. Rewrite.
- `wiki/entities/Mike Macdonald.md:24` — "Baltimore fell from 1st to 32nd in points allowed" conflicts with `wiki/concepts/Defensive Scheme Architecture.md:27` ("1st to 30th") and with `wiki/sources/Seahawks Are Biggest Threat to Overthrow the NFC.md:22` ("1st to 9th to 32nd"). Pick one; ideally cite the specific season.
- `wiki/entities/Seattle Seahawks.md:22` / `wiki/entities/John Schneider.md:19` / `wiki/concepts/Organizational Continuity.md:22` / `wiki/overview.md:96` — remove or qualify "zero player or coaching holdovers"; it's directly contradicted by `wiki/sources/Seahawks Are Biggest Threat to Overthrow the NFC.md:24`.
- `wiki/entities/Sam Darnold.md:22` — "5th QB in NFL history with multiple 14-win seasons (Brady, Mahomes, Manning, Montana)" — conflicts with its own cited source and is almost certainly wrong. Drop or fact-check against a non-team source.
- `wiki/concepts/Defensive Scheme Architecture.md:31` — "The 3-Buzz concept: Macdonald's signature zone shell" — wrong. 3-Buzz is a specific coverage, not the architecture. Rewrite to describe it as a representative call within a broader MOF-disguise/simulated-pressure system.
- `wiki/concepts/Defensive Scheme Architecture.md:28` — downgrade "coaching tree as control group" from "evidence" to "suggestive indicator, with confounders listed."
- `wiki/concepts/NFL Dynasty.md:22-28` — the list is missing the 1960s Packers, 1980s-90s 49ers, and current Chiefs; add them or explain the omissions.
- `wiki/overview.md:94-101` — the NFL section should (a) flag that Super Bowl LX itself is unsourced, (b) drop the "41-6 divisional rematch" claim until the bracket contradiction is resolved, (c) soften "dynasty" language to "potential window."
- Index (`wiki/index.md:393-428`) — collapse the duplicate Rams-OT and 49ers-Week-18 entries into the consolidated pages; either delete or mark the single-outlet versions as "superseded."

---

## Supporting Evidence

- Super Bowl sourcing gap: `raw/` glob for `*Super Bowl*` returns only the pre-game Schneider profile, Bad Bunny halftime coverage, and the NFC Championship recap. No post-game Super Bowl LX raw file exists.
- Schneider "zero holdovers" contradicted: compare `wiki/sources/Super Bowl LX — Homegrown GM John Schneider at the Peak of Powers.md:19` with `wiki/sources/Seahawks Are Biggest Threat to Overthrow the NFC.md:24`.
- Macdonald ranking contradiction: `wiki/entities/Mike Macdonald.md:18` vs. `wiki/entities/Seattle Seahawks.md:20` vs. `wiki/sources/How Macdonald Is Authoring a New Chapter of Seahawks Defensive Dominance.md:23`.
- Bracket contradiction: `wiki/sources/2025-26 NFL Playoffs Wikipedia.md:19` (NFC seeds do not include 49ers) vs. `wiki/sources/Seahawks 41-6 Divisional Win Over 49ers.md:10-15` (49ers in Divisional Round on Jan 17, 2026).
- Recap duplication: `wiki/sources/Seahawks 38-37 OT Comeback Over Rams — Multiple Perspectives.md`, `wiki/sources/Seahawks OT Win Over Rams — December 2025.md`, `wiki/sources/Seahawks OT Win Over Rams — Regular Season Trilogy Context.md` all cover the Dec 18 game.

---

## Caveats & Gaps

- I did not re-check the actual real-world 2025 NFL season. The wiki's internal contradictions are the focus — whether the wiki corresponds to reality is a separate question that this audit only touches in P2-3 (the Patriots / Super Bowl LX sourcing gaps suggest the cluster may be partly speculative or projected).
- I did not spot-check every concept-page evidence bullet — a deeper pass would likely find more stat miscites (the Week 8 / Week 12 / full-season conflation is a recurring pattern).
- The "Baltimore fell from 1st to 30th/32nd" claim requires actual verification against the real 2024-25 Ravens; the wiki cites Seaside Joe (a fan outlet) and never corroborates with a mainstream source.

## Newsletter Application

If the newsletter wants to use this cluster as a case study, the cleanup order is:
1. **Source the Super Bowl.** Without a Super Bowl LX game recap, the cluster's centerpiece is a plot hole.
2. **Fix the "zero holdovers" claim** — it's in four places and it's wrong. The real Schneider story (long tenure, clean cap sheets, aligned philosophy with his HC) is actually a better story than the false one.
3. **Reframe the dynasty claim** — "window opened" is defensible; "dynasty achieved" is not, by the wiki's own 12-14 criterion.
4. **Acknowledge the Chiefs.** Any credible 2026 NFL dynasty discussion has to engage with Reid-Mahomes-Veach.
5. **Strip the marketing language** — "3-Buzz as scheme," "coaching tree as control group," "zero holdovers," "never restructures" — replace with things you can actually defend to a reader who watched the games.

## Follow-up Questions

- Did Super Bowl LX actually happen in sourced reality, or is this cluster partly speculative? If speculative, separate projected from sourced material with different `type:` markers.
- Real-world check: are Macdonald's former Ravens assistants actually having the seasons the wiki claims? How did the Ravens' defense finish 2025?
- Real-world check: were the Seahawks really 14-3? The wiki is confident about it; a simple corroboration against a second non-team source would resolve the speculation question.
- Has any Schneider source outside team-adjacent media actually quantified his cap "discipline" vs. peers? If not, that's a whole essay to write — or to drop.
- What's the 2026 Chiefs season? If they made the SB and lost, the wiki should own that. If they missed the playoffs, that's itself a major data point for the "dynasty ending / continuity insufficient" thesis.
