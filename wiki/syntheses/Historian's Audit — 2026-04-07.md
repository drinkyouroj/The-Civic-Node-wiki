---
title: "Historian's Audit — 2026-04-07"
type: synthesis
tags: [audit, history, monetary-policy, methodology]
created: 2026-04-07
updated: 2026-04-07
sources: 0
query: "Audit the wiki's historical claims, parallels, and long-arc framing for accuracy and rigor."
---

## Answer

The wiki's historical spine is mostly solid — the Bretton Woods → Nixon Shock → Great Inflation → Volcker arc is accurately drawn, and the Burns pages actually handle the revisionist/conventional tension better than most mainstream coverage does. But there are several sharp problems: one bad date-error on Volcker, a confused framing of the "tariff rate since 1910" claim, a shutdown-longevity claim that needs qualification, a "paradigmatic" Bannon case that leans on a legal mechanism the wiki doesn't actually describe correctly, and a set of missing historical priors — Glass-Steagall for the stablecoin pages, the 1951 Treasury–Fed Accord context for Fed Independence, and the 19th-century wildcat-banking / "free banking" era for the crypto cluster — that would materially change how several concept pages read. The Burns→Powell parallel is the single most load-bearing historical analogy in the wiki, and it is being used carefully in some places and sloppily in others.

Prioritized below.

---

## P0 — Factual errors that should be fixed now

### 1. Volcker's rate peak is dated wrong in `Fed Independence`
`wiki/concepts/Fed Independence.md:16` says Volcker "raised rates to 20% in 1980." The fed funds rate first crossed ~20% in late 1980 under Volcker's Saturday-Night-Special reserve-targeting regime, fell, then peaked at roughly 22.4% in July 1981 before the 1981–82 recession broke the back of inflation. Writing "1980" is close enough to be defensible but collapses the two-phase Volcker tightening (Oct 1979 reserve targeting → 1980 briefly 20% → 1981 re-tightening to ~22% → recession → victory) into a single 1980 data point. `wiki/sources/The Great Inflation.md:25` correctly says "rates spiked to near 20%" and "two recessions (1980; 1981–1982)." Recommend changing the Fed Independence line to "raising rates to roughly 20% between 1980 and 1981" and noting the two-phase tightening.

### 2. "Paul Volcker's Legacy — PBS" file is duplicated
`wiki/sources/Paul Volcker Legacy — PBS.md` and `wiki/sources/Paul Volcker's Legacy — PBS.md` both exist. This is a lint issue more than a historical one, but one of them is orphaned and should be merged.

### 3. The "highest since 1910" tariff framing is being used imprecisely
`wiki/concepts/Tariff-Driven Inflation.md:16` and the Overview both say the 2025 tariff regime raised the US effective rate to "20.6% — highest since 1910." The underlying Yale Budget Lab source (`wiki/sources/State of U.S. Tariffs July 14, 2025.md:19-21`) is more careful: 20.6% is the **pre-substitution** rate (consumer welfare cost); the **post-substitution** rate is 19.7% and is "highest since 1933" — i.e., Smoot-Hawley era. The wiki consistently quotes the more dramatic "since 1910" number but loses the pre/post-substitution distinction that actually makes the number meaningful. The honest comparison for Smoot-Hawley parallels is the 1933 number, not the 1910 number. The 1910 baseline is a Payne–Aldrich-era level that predates the income tax and reflects a fundamentally different federal revenue architecture — the comparison is structurally misleading if not qualified. **Recommend:** on the Tariff-Driven Inflation concept page and in the Overview, use both numbers and note that 1933 is the analytically relevant parallel because that's when an industrialized US last sustained rates at this level.

### 4. "Longest shutdown in U.S. history" needs a qualifier
`wiki/sources/2025 United States federal government shutdown - Wikipedia.md:14` and the Overview both say the 2025 shutdown was "the longest in U.S. history" at 43 days. This is true for a **full** appropriations lapse but worth flagging: the 2018–19 shutdown (35 days) was previously described the same way, and earlier "shutdowns" under Carter/Reagan were partial and handled under different OMB guidance. The wiki's claim is defensible but should specify "longest full-government shutdown" to avoid being trivially rebutted by anyone who brings up the 1976 HEW gap or the pre-1980 shutdowns that didn't actually send workers home. Small fix; high visibility claim.

### 5. The Bannon "paradigmatic case" is described with legal imprecision
`wiki/concepts/Retroactive Executive Protection.md:37-38` says the Trump DOJ "requested SCOTUS vacate the conviction" and "Supreme Court complied without apparent legal re-briefing." `wiki/entities/Steve Bannon.md:25` says "SCOTUS vacated contempt conviction at Trump DOJ request; case sent back to district court for dismissal."

Historically, the mechanism being described is almost certainly a **Munsingwear vacatur** or a GVR (grant-vacate-remand) — a procedural tool SCOTUS has used for decades when the government concedes and mootness or changed circumstances warrant vacating a lower-court judgment. *United States v. Munsingwear* (1950) is the foundational case, and the DOJ-requested vacatur mechanism is not new; what's unusual is the post-sentence-service timing and the political valence, not the procedural vehicle.

The current framing — "SCOTUS complied without apparent legal re-briefing" — implies an unprecedented collapse of judicial review. That's rhetorically strong but historically sloppy: Munsingwear vacaturs are routinely granted on DOJ motion with minimal briefing. The concept page would be stronger if it said: "The procedural mechanism (Munsingwear vacatur on DOJ motion) is not new, but its use to erase a completed sentence for contempt of Congress is the novel element, and what makes the case paradigmatic is the *post-service* erasure of the institutional record, not the procedural vehicle itself." Without this correction, the "first of its kind" framing in `Retroactive Executive Protection.md` is vulnerable to an easy rebuttal.

**This is the single weakest historical claim in the wiki at present.** The underlying point — that the Trump administration is using institutional mechanisms to retroactively delete consequences for allies — is sound. But the current framing overstates the procedural novelty and understates the substantive novelty, which is exactly backwards.

---

## P1 — Parallels that are reaching, and the one that is carrying the weight

### 6. Burns vs. Powell: the most load-bearing analogy, used unevenly
The Burns/Powell/Nixon/Trump analogy is everywhere in the wiki. Three of the pages handle it well; one handles it sloppily.

**Handled well:**
- `wiki/entities/Arthur Burns.md` — explicitly flags the revisionist case at the bottom with a `⚠️ Contradiction` block citing the Meserve essay. Honest about the tension.
- `wiki/sources/Rethinking Arthur Burns the Worst Fed Chair in History.md` — summarizes the revisionist case fairly and notes the author's framing (policy-writer, not academic economist) and the implicit contemporary-moment argument.
- `wiki/concepts/Stagflation.md:29-30` — uses Burns's "all-of-government" approach as a substantive parallel for tariff-driven supply-shock inflation, not just as a rhetorical villain. This is the best use of the Burns frame in the wiki.

**Handled sloppily:**
- `wiki/concepts/Fed Independence.md:20` bullets "Burns kept rates low to help Nixon win reelection; inflation ignited. Ended with stagflation crisis" — this is the potted version the rest of the wiki is actively trying to complicate. The same page at line 34 cites the revisionist Meserve essay, but the bullet at line 20 is doing the opposite work. **Fix:** either drop the villain bullet or add a sentence acknowledging the revisionism the same page already knows about.

**The deeper problem with the Burns/Powell parallel:** the analogy's load-bearing claim is that *political pressure on a central bank during a supply-shock inflation produces the Great Inflation outcome*. But the supply-shock mechanism in 1973 (oil embargo) was genuinely exogenous, whereas in 2025 the supply shock (tariffs) is being **created by the same president pressuring the Fed**. This is structurally different and arguably worse: Nixon didn't cause the oil embargo. Trump did cause the tariffs. The Stagflation page nearly makes this point but doesn't quite land it. The parallel as currently used implies "1970s redux if the Fed folds" — but the real story is "1970s plus endogenous supply shock," which is a *different* and more dangerous configuration. This is a newsletter angle the wiki has not yet articulated cleanly.

### 7. The Nixon Shock / gold-convertibility deficit comparison is being over-read
`wiki/concepts/Nixon Shock.md:30` cites the UFM Market Trends piece: "Average US federal deficit to GDP: 0.6% from 1951–1971; jumped to 3.0% from 1972–2015 — suggesting gold convertibility had functionally constrained deficit spending." The before/after deficit shift is real, but the causal attribution to gold convertibility is contested. The Great Society, the Vietnam War, the post-1971 demographic entitlement buildup, and the Reagan-era tax cuts are at least as plausible as gold convertibility as drivers of the post-1971 fiscal shift. UFM is a libertarian/Austrian-adjacent outfit with a priors-driven reading of the data. The wiki currently presents the correlation as causal. **Fix:** add a one-line caveat noting the source's ideological framing and the alternative causal explanations.

### 8. The Petrodollar → Stablecoin analog is elegant but historically thin
`wiki/concepts/Petrodollar System.md:35-37` and `wiki/concepts/Stablecoin Legislation.md:38-40` both make the argument that the GENIUS Act's 100% T-bill reserve requirement creates a "digital petrodollar" — i.e., a structural captive buyer of Treasuries analogous to 1970s OPEC recycling. The analogy is rhetorically good but it is being asked to carry a lot of weight without the specifics of how 1970s recycling actually worked: the Saudi–Kissinger 1974 agreement to accept US debt, the secret 1974 bilateral, the rise of the eurodollar market, the 1973–74 oil price quadrupling that generated the surplus in the first place. None of this appears in the Petrodollar page — which is 57 lines long and cites only one source. **Fix:** the Petrodollar page needs a real Historical Origins section with Spiro's *The Hidden Hand of American Hegemony* or at minimum a proper 1974 chronology, otherwise the stablecoin comparison is doing all the analytical work without the foundation to support it.

---

## P2 — Missing historical context that changes how clusters read

### 9. Stablecoin cluster has no Glass-Steagall / narrow-banking analog
The GENIUS Act's banking-regulator jurisdiction, exclusion of interest-bearing stablecoins, and 100% reserve requirement are in direct dialogue with historical debates about narrow banking — the Chicago Plan, the post-1933 Glass-Steagall separation, the 1999 Gramm–Leach–Bliley repeal, and the 2010 Dodd-Frank Volcker Rule. None of this appears in the Stablecoin Legislation, GENIUS Act, or CLARITY Act pages. The 100% reserve requirement is **literally narrow banking**, and the debate about whether it's stable or unstable has ~90 years of policy history. `wiki/concepts/Stablecoin Legislation.md` reads as if the 100% reserve mechanism is a 2025 innovation. It isn't. **Newsletter angle (unused):** "Stablecoin regulation is Chicago Plan narrow banking by another name — here's why that matters."

**Specifically missing:** no Glass-Steagall page, no Chicago Plan reference, no Irving Fisher citation, no Minsky reference. The Bailout Risk note at `Stablecoin Legislation.md:86-88` cites Adam Levitin but doesn't place his argument in the narrow-banking tradition where it belongs.

### 10. Crypto cluster has no wildcat-banking / free-banking-era parallel
`wiki/concepts/Bitcoin as Digital Gold.md`, `wiki/concepts/Stablecoin Legislation.md`, and `wiki/concepts/Crypto Fraud and Scam Ecosystem.md` all discuss private monetary issuance as if it were historically novel. The US had almost a century of private note issuance (1837–1863, and arguably earlier) — the Free Banking Era, state-chartered banks issuing their own notes, Suffolk System as a clearing mechanism, the National Banking Acts of 1863–1864 as the federal response. Tether vs. USDC vs. USD1 is recognizably a modern version of the wildcat-bank problem: notes trading at discounts based on issuer credibility, geographic distance, and counterparty risk. The Overview at line 129 gestures at "distributed alternatives" but never grounds the conversation in the 19th-century history that actually produced those alternatives and then destroyed them.

**Specifically missing:** no Free Banking Era concept page, no reference to Hugh Rockoff's quantitative work showing wildcat banking was not as bad as the caricature, no reference to the Suffolk System as a distributed clearing precedent for something like Lightning Network. The Tether-loophole framing in the GENIUS Act pages is exactly the 1840s discount-note problem under a new name and the wiki doesn't say so.

### 11. Fed Independence page is missing the 1951 Treasury–Fed Accord
The 1951 Treasury–Fed Accord is the event that created the modern conception of Fed independence. The Fed Independence page mentions it once in passing at line 12 ("it has been a convention since the 1951 Treasury-Fed Accord") and then moves on. But the historical structure of the argument requires it: Fed independence is roughly ~75 years old, not a constitutional or even a mid-20th-century given, and the Accord itself was produced by a president (Truman) under wartime fiscal pressure who explicitly did not want it. That is the closest structural analog to Trump–Powell and it is not currently in the wiki. **Fix:** add a short Treasury–Fed Accord section to Fed Independence, and consider creating a dedicated concept page for it.

### 12. Missing LBJ–Martin parallel, which is arguably more load-bearing than Nixon–Burns
The canonical pre-Nixon example of direct presidential pressure on a Fed chair is LBJ physically cornering William McChesney Martin at the Texas ranch in December 1965 after Martin raised the discount rate over Johnson's objections. This is documented in Robert Bremner's *Chairman of the Fed* biography and in the FOMC minutes. It's the "Nixon pressures Burns" story minus the capitulation — Martin held the line and was later vindicated. It is the single most relevant historical parallel to Powell holding rates against Trump in 2025, and the wiki does not mention Martin at all. **Fix:** create a William McChesney Martin entity page, add a section to Fed Independence, and use it as a positive counterpart to Burns.

### 13. No 1893 / 1907 banking panic parallel for the crypto cluster's systemic-risk framing
The wiki's handling of stablecoin bailout risk (Levitin), TerraUSD collapse, and Tether opacity would benefit enormously from the 1907 Panic (J.P. Morgan's private intervention as proto-Fed) and the 1893 Panic (silver crisis, Treasury gold reserve run, Cleveland-Morgan bond deal). Both are structurally identical to what Levitin is warning about: private monetary issuers with opaque reserves, no lender of last resort, and a political economy in which the private issuer's credibility is the only thing holding the system together until it isn't. The GENIUS Act's insolvency-priority carveout is an attempt to pre-solve the 1907 problem without creating a lender of last resort. The wiki should say this.

### 14. Watergate / Iran-Contra parallels are conspicuously absent from the power cluster
For a wiki that makes claims about "Retroactive Executive Protection" being "paradigmatic," the total absence of Watergate and Iran-Contra pages is a structural gap. The Nixon pardon (Ford, 1974), the Iran-Contra pardons (Bush Sr., 1992, erasing the Weinberger prosecution Lawrence Walsh was actively pursuing), and the Libby commutation + later pardon (Bush/Trump) are the direct precedents for every "retroactive erasure" claim the wiki is making. The Bush Sr. 1992 pardons are especially relevant because they erased an active special-prosecutor case — which is exactly the mechanism the wiki is flagging around Jack Smith. The current framing makes the Trump-era pattern look unprecedented when the honest historical claim is that it is an *intensification* of an existing pattern, which is actually a stronger argument. **Fix:** Iran-Contra and Watergate concept pages (or at least a single "Presidential Pardons as Accountability Erasure" page tracing the pattern from Nixon–Ford forward).

---

## P2 — Period / temporal framing

### 15. "2025" and "2026" used loosely in several concept pages
The Overview uses dates cleanly. But some concept pages say things like "March 2026: Rate held at 3.5%–3.75%" (`Fed Independence.md:33`) and "By 2025, CISA routinely reported..." (`CISA Jawboning.md:22`) without specifying whether they mean calendar year, fiscal year, or "some point in 2025." For a wiki whose value compounds over time, this ambiguity is going to become a problem fast. The shutdown page is a good example of the right approach: explicit date ranges (Oct 1 – Nov 12, 2025). Recommend adopting that convention project-wide.

### 16. The `Petrodollar System.md` page treats the 1973-74 moment as if it were a single event
Lines 30–33: "1973 oil crisis: OPEC embargo; Nixon-Kissinger negotiated..." then "By mid-1970s: System formalized." This collapses a 3-year process (October 1973 embargo → March 1974 embargo end → June 1974 US–Saudi Joint Commission → 1974 secret Treasury agreement on Saudi Treasury purchases → 1975 formalization) into two bullets. The chronology matters because the Saudi dollar agreement was explicitly contingent on post-embargo price shifts that weren't resolved until 1975. This is minor but the page is already thin and would benefit from a proper timeline.

---

## Supporting Evidence

- `wiki/concepts/Fed Independence.md:16` — Volcker 1980 date issue
- `wiki/concepts/Fed Independence.md:20-34` — Burns framing inconsistency within a single page
- `wiki/concepts/Tariff-Driven Inflation.md:16,29` — "highest since 1910" without pre/post-substitution qualifier
- `wiki/sources/State of U.S. Tariffs July 14, 2025.md:19-21` — correct Yale Budget Lab framing
- `wiki/concepts/Retroactive Executive Protection.md:37-38` — procedurally imprecise Bannon description
- `wiki/entities/Steve Bannon.md:25` — same issue
- `wiki/concepts/Nixon Shock.md:30` — UFM deficit-causation claim without caveat
- `wiki/concepts/Petrodollar System.md` — 57-line page with single source carrying significant analytical weight
- `wiki/concepts/Stablecoin Legislation.md` — no Glass-Steagall, narrow banking, or Chicago Plan references
- `wiki/concepts/Bitcoin as Digital Gold.md` — no wildcat/free-banking context
- Absent files: no `wiki/concepts/Glass-Steagall.md`, no `Treasury-Fed Accord.md`, no `William McChesney Martin.md`, no `Watergate.md`, no `Iran-Contra.md`, no `Free Banking Era.md`

## Caveats & Gaps

- I did not verify every date in every source page. I sampled the concept pages with the heaviest historical claims.
- The Munsingwear vacatur assertion in finding #5 is based on standard federal-procedure knowledge, not a direct reading of the 2026 SCOTUS order in Bannon's case. The exact procedural vehicle should be confirmed before any edit to the Retroactive Executive Protection page.
- I did not read the Political Stress, ADHD Medication Shortage, or NFL clusters — this audit is focused on historical claims in the monetary/political/crypto clusters where historical parallels are load-bearing.
- The wiki's overall historical rigor is above average for this kind of project. The problems above are concentrated in a handful of high-visibility pages.

## Newsletter Application

The most valuable finding for the newsletter is #6 + #14 combined: the Burns/Powell parallel is being used to gesture at 1970s-redux, but the real story is *endogenous supply shock* — a president creating the inflation he's pressuring the Fed to ignore. That's structurally different from Nixon/Burns and more similar to LBJ/Martin (a president demanding accommodation of fiscal stimulus he chose) except with tariffs instead of Vietnam spending. A newsletter piece titled something like "The Fed Chair Who Said No: William McChesney Martin and the Pre-Nixon Precedent Powell Is Actually Following" would let the wiki lean into its best historical material while correcting the sloppiest parallel in its own frame.

Second-best newsletter angle from this audit: #9 — "The 100% Reserve Stablecoin Is Chicago Plan Narrow Banking and Nobody Is Saying So." This is a real gap in the current crypto coverage consensus and the wiki is well-positioned to exploit it.

## Follow-up Questions

- What was the actual procedural vehicle in the 2026 Bannon SCOTUS order? Munsingwear GVR, cert grant with summary disposition, or something else?
- Is there a good primary source for the 1974 US–Saudi Treasury purchase agreement that could anchor a proper Petrodollar page rebuild?
- Who in the current commentariat is drawing the Chicago Plan / narrow-banking parallel for the GENIUS Act? (If nobody, this is a clean newsletter lane.)
- Has any economic historian written a proper Hugh Rockoff-style quantitative comparison of the Tether / USDC / USD1 dollar-discount regime vs. 1840s state bank notes?
- Does Meltzer's *History of the Federal Reserve* have the Martin-LBJ ranch episode in enough detail to anchor a dedicated Martin entity page?
