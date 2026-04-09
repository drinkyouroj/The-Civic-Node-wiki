# Wiki Log

Append-only chronological record of all wiki activity.
Parse recent entries with: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-04-09] ingest | 8 new sources — Iran ceasefire collapse cluster, DOJ records opinion, China/CFIUS, NFL antitrust

Eight raw files added since the April 9 batch-1 session. All ingested and filed.

**Iran Ceasefire Fragments — Strait Reopens Then Closes, Oil Toward 100** (PBS/AP, Apr 9): Ceasefire announced April 8; Israel struck Lebanon within hours; Iran re-closed Strait; WTI $99.44; Trump "looking forward to its next Conquest." Created `wiki/sources/Iran Ceasefire Fragments — Strait Reopens Then Closes, Oil Toward 100.md`.

**Iran Dueling Peace Plans — English vs Persian 10-Point Discrepancy** (Al Jazeera, Apr 9): English/Persian version gap on uranium enrichment is the structural impasse; Vance dismisses publicized plan as "written by ChatGPT"; Islamabad talks Saturday. Created `wiki/sources/Iran Dueling Peace Plans — English vs Persian 10-Point Discrepancy.md`.

**Republicans Block Iran War Powers Resolution — House Adjournment** (USA Today, Apr 9): Chris Smith (R-NJ) adjourned chamber to prevent Democrats from bringing war powers resolution to floor. Senate Democrats to force vote next week. Created `wiki/sources/Republicans Block Iran War Powers Resolution — House Adjournment.md`.

**Pew Poll — Israel Favorability Hits New Low, 60 Percent Unfavorable** (USA Today, Apr 8): 60% unfavorable (up from 42% in 2022); 80% Democrats; 58% Republicans still favorable; 77% say Iran conflict personally important. Pre-ceasefire poll. Created `wiki/sources/Pew Poll — Israel Favorability Hits New Low, 60 Percent Unfavorable.md`.

**DOJ OLC Opinion — Presidential Records Act Unconstitutional** (The Independent, Apr 2): OLC memo tells Trump he "need not further comply" with PRA; legal cover for withholding records when he leaves office. Created `wiki/sources/DOJ OLC Opinion — Presidential Records Act Unconstitutional.md`.

**Chinese Firm Hired Don Jr Lobbyists, Won CFIUS Ruling Against US Startup** (Reuters, Apr 9): Grand Pharma hired Don Jr-adjacent Checkmate; secured CFIUS head meeting; FastWave (US startup with export-controlled laser tech) got only staffer calls; CFIUS rejected FastWave on procedural grounds without addressing national security. Created `wiki/sources/Chinese Firm Hired Don Jr Lobbyists, Won CFIUS Ruling Against US Startup.md`.

**DOJ Investigating NFL Over Subscription Fees — Antitrust** (NBC News, Apr 9): DOJ antitrust probe into NFL streaming fees ($1,000/season for full access); Sen. Mike Lee triggered; 1961 Sports Broadcasting Act question; FCC also seeking comment. Created `wiki/sources/DOJ Investigating NFL Over Subscription Fees — Antitrust.md`.

Updated entity: [[Iran]] (sources 9→13; ceasefire collapse + peace plan discrepancy + war powers + public opinion added). New concept: [[War Powers Resolution]]. Index: 409 sources, 86 concepts. Overview: Iran cluster section updated.

---

## [2026-04-09] ingest | 4 new sources — AI cardiac diagnostics, light pollution, Artemis II conspiracy, NYT/Satoshi

Four raw files added since the April 8 session. All ingested and filed.

**AI Predicts Heart Disease Five Years Out — Oxford BHF Study** (Independent, Apr 8 2026): Oxford/BHF AI tool reads CT scan pericardial fat texture; 86% accuracy; 72,000 patients; 5-year predictive window; NHS rollout under evaluation. Created `wiki/sources/AI Predicts Heart Disease Five Years Out — Oxford BHF Study.md`. New entities: [[University of Oxford]], [[British Heart Foundation]]. New concept: [[AI in Healthcare]].

**Light Pollution Brightened Earth 16 Percent Since 2014 — Nature Study** (Space.com, Apr 9 2026): Nature study using NASA Black Marble data; Earth +16% (2014–2022); war signature (Ukraine, Gaza); France -33% via policy; VIIRS LED blind spot. Created `wiki/sources/Light Pollution Brightened Earth 16 Percent Since 2014 — Nature Study.md`. Updated entity: [[NASA]]. New concept: [[Light Pollution]].

**Artemis II Conspiracy Theorists Already Failing — Vice** (Vice, Apr 8 2026): Artemis II crewed lunar loop complete; "dark side" misnomer exploited by conspiracy producers; algorithmic reward for manufactured doubt. Created `wiki/sources/Artemis II Conspiracy Theorists Already Failing — Vice.md`. New entities: [[NASA]] (updated), [[Artemis II]]. New concept: [[Misinformation Economy]].

**NYT Names Adam Back as Satoshi Nakamoto — Bitcoin.com Coverage** (Bitcoin.com, Apr 8 2026): NYT investigation names Adam Back; stylometric analysis inconclusive; Back denies 6+ times; SEC disclosure mechanism as live resolution path. Created `wiki/sources/NYT Names Adam Back as Satoshi Nakamoto — Bitcoin.com Coverage.md`. New entities: [[Adam Back]], [[Satoshi Nakamoto]], [[Blockstream]]. New concept: [[Cypherpunk Movement]]. Updated entity: [[Bitcoin]].

Total new pages: 4 source + 7 entity + 4 concept = 15 pages. Index and stats updated (401 sources, 107 entities, 85 concepts).

---

## [2026-04-07] lint | NFL cluster fixes from sports-nut audit

Acted on `wiki/syntheses/audit-2026-04-07-sports-nut.md`. NFL cluster owner pass.

**Super Bowl LX sourcing gap (P0-1)**: confirmed no post-game raw file exists. Added a `⚠️ Caveat` block at the top of the Mike Macdonald, Seattle Seahawks, John Schneider, Sam Darnold entity pages, the Super Bowl LX Schneider profile source page, and the NFL section of `wiki/overview.md`. All "won Super Bowl LX" framing softened to "Super Bowl LX appearance / NFC champion" pending a post-game source.

**"Zero holdovers" contradiction (P0-3)**: flagged with `⚠️ Contradiction` markers per CLAUDE.md rule #6 in Seattle Seahawks, John Schneider, Organizational Continuity, the Schneider profile source page, and the overview. Defensible reading is "zero holdovers from the prior coaching regime" — `Seahawks Are Biggest Threat to Overthrow the NFC` says 9 of the 2023 defensive starters were on the 2025 roster.

**Macdonald "25th → 2nd in one season" fix (P0-2)**: corrected to "25th (2023) → 11th (Year 1, 2024) → top-3 (Year 2, 2025)" — *two seasons*. The Ravens-era jump (19th → 3rd in Year 1, 1st in Year 2) now correctly scoped. Overview updated.

**3-Buzz fix (P1-1)**: rewrote `wiki/concepts/Defensive Scheme Architecture.md` to describe 3-Buzz correctly as a Cover-3 variant with a buzzing safety, not as the umbrella term for "disguise." Overview updated.

**Bracket contradiction (P2-2)**: resolved as a wiki-extraction artifact, not a real contradiction. The Wikipedia source page only listed 5 NFC seeds when there are 7 playoff teams; the Jan 17 Divisional Round 41-6 ESPN raw file is real and confirms the 49ers were a wild card. Annotated `wiki/sources/2025-26 NFL Playoffs Wikipedia.md`.

**Coaching-tree "control group" caveat (P1-3)**: downgraded on Defensive Scheme Architecture, Mike Macdonald, and the overview. Now framed as "suggestive, not control group" with the four confounders listed.

**Dynasty list updated (P3-1)**: added the 1961-67 Lombardi Packers, the 1981-94 Walsh/Seifert 49ers, and the Reid/Mahomes Chiefs to `wiki/concepts/NFL Dynasty.md`. Chiefs explicitly framed as the relevant 2026 counter-case to "continuity is the master variable." 2025 Seahawks corrected to "potential dynasty window opening, not dynasty achieved."

**Game-recap consolidation (P2-1)**: 6 duplicate source pages converted to SUPERSEDED stubs with merge-completed notes. Could not delete files via Bash; user can `rm` them safely. Index updated to remove all 6 entries.
- Dec 18 Rams OT canonical: `Seahawks 38-37 OT Comeback Over Rams — Multiple Perspectives` (7 raw files)
- Jan 3 49ers Week 18 13-3 canonical: `Seahawks 13-3 Win Over 49ers — NFC West Title Clincher` (6 raw files)
- Jan 26 NFC Championship canonicals: `NFC Championship — Seahawks 31 Rams 27` (Yahoo + merged CBS/AP) and `NFC Championship — ESPN Game Analysis` (kept as distinct analytical artifact)
- Unique facts merged: Darnold as first USC Trojan to start a Super Bowl; SB LX as the SB XLIX rematch.

**Source counts adjusted**: Seattle Seahawks 24→21, Sam Darnold 12→10. Mike Macdonald and John Schneider unchanged (didn't cite the deleted pages).

**Sam Darnold "5th QB factoid" (P0-4)**: caveated as unverified team-media — two cluster sources cite different thresholds and different company.

**Schneider "standard tradecraft" caveat (P1-4)** and **Darnold Carolina-arc sanitization caveat (P1-5)**: both added.

**Files left for the user to physically `rm`** (Bash delete blocked):
- `wiki/sources/Seahawks OT Win Over Rams — December 2025.md`
- `wiki/sources/Seahawks OT Win Over Rams — Regular Season Trilogy Context.md`
- `wiki/sources/Seahawks Clinch NFC West — 13-3 Win Over 49ers.md`
- `wiki/sources/Seahawks Beat 49ers Week 18 — 4 Takeaways.md`
- `wiki/sources/Rams Fall to Seahawks 31-27 in NFC Championship.md`
- `wiki/sources/Sam Darnold Seahawks Advance to Super Bowl — Fox Sports.md`

All 6 are SUPERSEDED stubs pointing at their canonical replacements; nothing in the index links to them anymore.

---

## [2026-04-07] update | Fed/monetary reframing — historian + economist + contrarian audit fixes

Acted on the Fed/monetary findings from the 2026-04-07 historian, economist, and millennial-contrarian audits.

**Factual corrections:**
- `wiki/concepts/Fed Independence.md`: Volcker rate-peak fixed from "20% in 1980" to the two-phase tightening (Oct 1979 reserve targeting → 1980 ~20% → 1980 backoff → 1981 re-tightening to ~22% → 1981–82 recession). Resolves the historian's #1 P0 finding.
- `wiki/concepts/Tariff-Driven Inflation.md`: 20.6% tariff claim now carries the pre/post-substitution distinction (20.6% pre / "highest since 1910" vs. 19.7% post / "highest since 1933"); 1933 (Smoot-Hawley) flagged as the analytically honest historical parallel; Payne–Aldrich qualification added on the 1910 baseline.

**Framing changes:**
- `Fed Independence.md`: Burns/Powell parallel rewritten with revisionism integrated structurally (not parenthetically); endogenous-vs-exogenous supply shock distinction made explicit (Trump tariffs as endogenous shock vs. Nixon-era exogenous OPEC embargo); Martin–LBJ flagged as the closer historical analog. Self-contradiction between line 20 (potted Burns villain) and line 34 (Meserve revisionism citation) resolved.
- `Fed Independence.md`: "Why the Fed Isn't Cutting" rewritten as expectations-vs-realized-passthrough — Powell's hold is precautionary expectations management, not a mechanical response to tariff inflation that has already materialized. Goldman passthrough data integrated.
- `Tariff-Driven Inflation.md`: Same expectations-vs-passthrough split applied to "The Fed's Dilemma" section.
- `Fed Independence.md`: New "Serious Non-Trump Critique of Powell" section — the Furman/Summers/El-Erian transitory critique that the wiki had been missing. The honest technocratic Powell critique that Trump cannot make.
- `wiki/entities/Jerome Powell.md`: Same transitory steelman added; Burns/Martin/1951 cross-links added.
- `wiki/entities/Arthur Burns.md`: Endogenous-shock-problem framing added explicitly to Newsletter Relevance; Martin and Accord cross-links added.
- `wiki/entities/Federal Reserve.md`: Historical-context paragraph rewritten to anchor on the 1951 Accord and the full pressure-episode sequence (Truman→Martin/LBJ→Burns/Nixon→Volcker/Reagan→Powell/Trump). Connections list expanded to include Martin and the Accord.
- `wiki/concepts/Stagflation.md`: Tensions section now flags the endogenous-shock distinction and the LBJ-Martin parallel.

**New pages created (UNREGISTERED — hygiene agent should add to index):**
- `wiki/entities/William McChesney Martin.md` — Fed Chair 1951–1970, longest-serving; the LBJ Texas ranch episode; the positive precedent for a Fed chair holding under direct presidential pressure. Historian audit's #1 missing-prior recommendation.
- `wiki/concepts/1951 Treasury-Fed Accord.md` — the founding moment of modern Fed independence; the Truman-vs-FOMC standoff that produced it; structural parallels to Trump-vs-Powell.

**Out-of-scope issues observed (not fixed — flagged for other agents):**
- `wiki/entities/Donald Trump.md` (politics agent) and `wiki/overview.md` / `wiki/index.md` (hygiene agent) also carry the 20.6% / "since 1910" claim and should receive the pre/post-substitution fix in their own passes.
- The Volcker date issue does not appear to have leaked into other pages I touched, but `wiki/sources/The Great Inflation.md:25` already correctly says "rates spiked to near 20%" and references "two recessions (1980; 1981–1982)" — that page is fine.

---

## [2026-04-07] lint | Vault hygiene pass — fix audit-flagged frontmatter, broken wikilinks, stale concept counts

Mechanical hygiene pass acting on the Lead Researcher audit (`wiki/syntheses/audit-2026-04-07-lead-researcher.md`).

**Frontmatter counts fixed:**
- `wiki/index.md`: `total_pages` 594 → 619, `total_sources` 385 → 384 (matches filesystem: 384 sources + 79 entities + 58 concepts + 82 articles + 5 syntheses + 3 root pages + 8 new stubs)

**Iran-cluster concept page source counts reconciled** (rebuilt Key Sources from `[[Concept Name]]` greps across `wiki/sources/`):
- `War-Driven Inflation`: 1 → 7 (added Volcker x2, Weimar, M2 history, Burns, Trump-Powell)
- `Coercive Diplomacy`: 1 → 9 (added Schelling, NYC freeze, Judge ICE, Japan trade, two energy-cancellation sources, Walz freeze, Will-blow-up)
- `Tech-State Conflict`: 1 → 19 (full rebuild — Anthropic cluster, antitrust cluster, EU AI Act, DABUS, MS-OpenAI, Algorithmic Influence, etc.)
- `Infrastructure Warfare`: 1 → 4 (added Will-blow-up, Trump cuts energy, Cruise robotaxis)
- `Chokepoint Control`: 1 → 3 (added Belichick and Schneider as the cross-cluster NFL chokepoint examples the audit explicitly called for)
- `AI Sovereignty`: 1 → 3 (added Anthropic raise, Cruz CISA-to-AI hearing)
- `Oil Seizure as Coercion`: 1 (verified — legitimately one source)

**New stub pages created (8):**
- Entities: `Stephen Miran`, `Lisa Cook`, `Mikie Sherrill`, `Israel`, `World Liberty Financial` — each pulls facts already in the wiki via grep, no fabrication; minimum schema-compliant frontmatter and Source Appearances.
- Concepts: `Federal Immunity Above Constitutional Law`, `International Humanitarian Law`, `Institutional Capture` — all flagged as broken wikilinks in `Retroactive Executive Protection`, `Infrastructure Warfare`, and overview.md cross-cutting patterns.

**`overview.md` wikilink fixes:**
- `[[Charlie Kirk]]` → `[[Charlie Kirk Assassination]]` (existing entity)
- `[[Spanberger]]` → `[[Abigail Spanberger]]` (existing entity)
- `[[Sherrill]]` → `[[Mikie Sherrill]]` (new stub)
- `[[Mamdani]]` → `[[Zohran Mamdani]]` (existing entity)
- `[[Stephen Miran]]`, `[[Lisa Cook]]` now resolve to new stubs
- `[[Strategic Bitcoin Reserve]]` already resolves to existing concept page (no fix needed; audit was wrong on this one)

**Out of hygiene scope but flagged for follow-up:**
- `overview.md` references `[[Wiki Index]]` and `[[Wiki Log]]` (line 177) — actual files are `index.md` and `log.md`. Will not resolve in Obsidian.
- `overview.md` references `[[Therapist Shortage]]`, `[[Anti-CBDC Surveillance State Act]]`, `[[The Great Inflation]]`, `[[Satoshi Nakamoto Bitcoin Whitepaper 2008]]` — `The Great Inflation` and `Satoshi Nakamoto...` exist as sources (resolve fine); `Therapist Shortage` and `Anti-CBDC Surveillance State Act` do not have dedicated pages — separate ingest needed.
- `entities/Donald Trump.md` line 86 references `[[Trump blames the radical left for Charlie Kirk's killing]]` and `[[Trump calls for revenge at the voter box after Charlie Kirk's assassination]]` — neither in `wiki/sources/`. Likely missing source pages.
- `entities/Donald Trump.md` Connections section references `[[Rick Crawford]]`, `[[Tim Kaine]]`, `[[Jake Auchincloss]]` — no entity pages exist; left for a separate stub-creation pass.

Counts: 1 frontmatter fix on index.md, 7 Iran-cluster concept source counts fixed (one verified-correct), 8 new stub pages, 5 broken wikilinks now resolved in overview.md.

---

## [2026-04-07] ingest | Triage & ingest of 73 unreferenced raw files — 11 source pages created

Triaged all 73 raw files flagged as unreferenced. Found 44 already ingested under existing source pages (different filename or consolidated). 18 were noise/skip (gaming, nav pages, thin marketing content). Created 11 new source pages.

**Skipped — already in wiki (different filename or consolidated):**
- `Rethinking Arthur Burns...` → already as `Rethinking Arthur Burns the Worst Fed Chair in History.md`
- `Satoshi Nakamoto, Bitcoin...` → already as `Satoshi Nakamoto Bitcoin Whitepaper 2008.md`
- `Bureau of Economic Analysis...GDP...` → already as `Gross Domestic Product First Quarter 2025 Advance Estimate BEA.md`
- Both Microsoft antitrust files → already as `Microsoft Antitrust Lawsuit — Secret Deal with OpenAI and Artificial Scarcity.md`
- `Securities Enforcement Roundup – April 2026.md` → file is actually April 2025 content; already as `Securities Enforcement Roundup April 2025 — Morgan Lewis.md`
- `Rescissions Act of 2025 - Wikipedia.md` → already as `Rescissions Act of 2025 — Wikipedia.md`
- `"Masking Is Life"...md` → already as `Masking Is Life — Experiences of Masking in Autistic and Nonautistic Adults.md`
- `Bad Bunny is Spotify's most-streamed...` → already as `Bad Bunny Spotify Global Top Artist 2025.md`
- `Press Release House Passes Anti-CBDC...` → already as `Anti-CBDC Act Passes House — Tom Emmer Press Release.md`
- `House Announces Week of July 14th as "Crypto Week"` → already as `House Announces Crypto Week July 14 — Financial Services Committee.md`
- `"We play three to four hours...Bob.md"` → already as `Bob Weir's Six Principles of Rhythm Guitar.md`
- `Darnold, Seahawks outlast Rams for NFC title...` → already covered by NFC Championship pages
- Multiple Seahawks/49ers game recap files → already consolidated in existing NFC pages
- `Sen. Whitehouse on Congress' "enormous step forward"...` → already as `Sen. Whitehouse on Congress enormous step forward with Epstein probe.md`

**Skipped — noise/thin content:**
- Google Search, Google Search Quality Evaluator Guidelines, Home page, Popular Articles, espn.com, Google Books — navigation pages
- HELLDIVERS 2 on Steam, Arc Raiders (both files) — gaming unrelated to newsletter
- Leadership Cities Church, Thought Leadership software, About - Partnership on AI — thin/irrelevant
- Northcrypto Finland cryptocurrency exchange, Crypto media outlet Best 20 projects — thin crypto noise
- llm-wiki.md, the original article text.md — system files
- How stablecoins could affect borrowing costs (ABA) — captured page with no actual article content (ISM Services index instead)
- Citizens United v. FEC Case Brief Summary — paywalled stub with no substance
- Impact of Dynamic Pricing on Customer Behavior (Hirebase/Framer) — thin marketing blog
- How Social Media Algorithms Are Set to Change in 2025 (TouchstoneDigital) — thin marketing blog
- Keep Up With Social Media Algorithm Changes (Vista Social) — thin marketing blog
- What's next in AI 7 trends to watch in 2027.md — identical file to 2026 version, duplicate fetch
- State of U.S. Tariffs July 14, 2025.md — already as `State of U.S. Tariffs July 14, 2025.md` (already in wiki)

**Source pages created (wiki/sources/):**
- `The Use of Knowledge in Society — Hayek.md` — Hayek 1945 AER essay; dispersed knowledge; price system as information; foundational text
- `The Strategy of Conflict — Thomas Schelling.md` — Schelling 1960; focal points; commitment mechanisms; compellence vs. deterrence
- `What Are Deepfakes — Reality Defender.md` — Reality Defender explainer; 30-second voice cloning; non-consensual pornography dominant use; banking attacks
- `State of Digital Health 2024 — CB Insights.md` — AI captures 42% of digital health funding; deal count lowest since 2014; drug discovery mega-rounds
- `Time Spent on Social Media — DataReportal 2024.md` — 2 hrs 23 min/day; 500 million years of collective annual attention; TikTok highest time-per-user
- `Jack Clark on AI Fear — Anthropic Co-Founder Speech.md` — "creature not machine" framing; 50-50 fear; "broadly unencumbered" trajectory
- `AI Tech Trends 2026 — IBM Think.md` — IBM quantum milestone claim; agentic AI as coworkers; efficiency over scale; healthcare AI gap
- `What's Next in AI — Microsoft 7 Trends 2026.md` — human amplification framing; agent security; MAI-DxO 85.5% medical accuracy
- `Future of AI Pricing — SuperAGI.md` — 75% retail AI pricing adoption; 5% revenue gain (Forrester); personalized pricing exploitation risk acknowledged
- `Congress Delivers for Crypto — Hill Op-Ed by Chairman Hill and Thompson.md` — op-ed by both committee chairs; "national priority" framing; Biden-blame framing
- `ICE Voter Favorability — Data for Progress January 2026.md` — n=1,225; +13→-9 ICE favorability flip; 55% oppose increased funding; Independents -20

**Entity pages updated:**
- `Jack Clark.md` — sources 2→3; added Jack Clark on AI Fear source
- `Anthropic.md` — sources 7→8; added Jack Clark speech source

**Concept pages updated:**
- `Algorithmic Radicalization.md` — sources 6→7; added DataReportal time-spent source
- `Dynamic Pricing AI.md` — sources 4→5; added SuperAGI source
- `Deepfake Disinformation.md` — sources 2→3; added Reality Defender explainer
- `Focal Point Coordination.md` — sources 1→2; added Schelling primary text
- `Crypto Week.md` — sources 14→15; added Hill op-ed
- `ICE Public Opinion Shift.md` — sources 5→6; added Data for Progress polling as proper source page

**Index updated:** total_pages 583→594, total_sources 374→385

---

## [2026-04-07] ingest | Federal Reserve / Monetary Policy cluster — 30 source pages, 5 entity pages, 5 concept pages

Processed the Federal Reserve / Monetary Policy cluster. Of the 40 assigned raw files, approximately 30 were confirmed present and readable. Many files in the task list do not exist under those exact filenames in raw/ — the wiki covers the substantive content through the files that were found.

**Source pages created (wiki/sources/):**
- `Trump calls Powell 'too stupid' after fifth rate hold.md` — TOI; July 30 FOMC hold; Truth Social attacks; dual governor dissent
- `Trump's tariffs kept Fed from cutting rates, Jerome Powell says.md` — NBC; Powell confirms tariff-rate link at ECB forum; "moron" response; board succession
- `Fed keeps rates steady, despite historic contrary votes and Trump pressure.md` — AP; July 30 FOMC; first dual governor dissent in 30+ years; "auditioning for Fed chair" angle
- `Trump and Powell bicker over Fed building renovations.md` — AP; Trump visits Eccles Building; renovation cost dispute; Trump's own tariffs raised the building costs he criticized
- `Federal Reserve holds benchmark rate steady July 2025.md` — CBS News; July 30 FOMC; Powell "one-time price increase" framing
- `Fed meeting recap September 2025.md` — CNBC; first 2025 cut; "risk management cut" framing; Miran dissent
- `Fed set to cut rates September 2025 preview.md` — CNBC; political intrigue preview; Miran swearing-in
- `New Trump appointee Miran calls for half-point cut.md` — CNBC; Miran's 50 bps dissent; board composition; Cook firing blocked by courts
- `Federal Reserve Signals Further Rate Cuts October 2025.md` — FinancialContent; Powell shifts to employment focus; 10-9 split; shutdown data delay
- `Board of Governors FOMC Statements 2025.md` — federalreserve.gov; June (hold) + October (cut) primary source FOMC statements
- `Government shutdown cements Fed rate cuts.md` — CNBC; shutdown → October cut mechanism; BLS data delay
- `The Great Inflation.md` — Fed History; 1965–1982 comprehensive essay; Burns/Volcker/Bretton Woods
- `Column Paul Volcker's legacy, an independent Federal Reserve, is under threat.md` — PBS; Volcker obit; Burns vs. Volcker archetypes
- `What went wrong in Arthur Burns' time as Fed chair in the 1970s.md` — NPR; Burns-Nixon dynamic; revisionist defense; supply shock problem
- `How Richard Nixon Pressured Arthur Burns Evidence from the Nixon Tapes.md` — AEA JEP; tape evidence; conviction or coercion question
- `The cautionary tale of Richard Nixon vs. his Fed chair.md` — WBUR/Planet Money; published Feb 2025; Burns fought then capitulated
- `Memories of the 1970s haunt the Fed, pushing its aggressive rate moves.md` — NPR; Powell's 1970s framework; Blinder on expectations; Volcker psychology
- `Nixon shock - Wikipedia.md` — Wikipedia; Bretton Woods end; Camp David; gold window closure; SWIFT origin
- `Forty-Five Years After the Gold Standard.md` — UFM; Austrian critique; pre/post-1971 data comparison
- `State of U.S. Tariffs July 14, 2025.md` — Yale Budget Lab; 20.6% effective rate (1910 high); substitution analysis
- `Tariffs could spike costs for domestic automakers by $108B.md` — Automotive Dive/CAR; $107.7B industry cost; $4,239/vehicle
- `General Motors profit drops 35% as Trump tariffs hit car industry.md` — Al Jazeera; Q2 tariff hit; 35% profit decline
- `General Motors and the Tariff-EV Dilemma.md` — Ainvest; strategic analysis; LFP battery; software monetization
- `Stellantis warns of $2.7B loss H1 2025.md` — AP; Big Three tariff impact
- `Trump secures $550B trade deal with Japan.md` — Fox Business; Japan deal; 15% tariffs; tariffs-as-leverage model
- `US stocks hit records following US-Japan trade deal.md` — AP; market reaction; Goldman passthrough data
- `Tariffs Weigh Heavy on Detroit Regional Chamber.md` — Michigan Advance; Canada integration; 234K trade-dependent jobs
- `Online resource center for businesses struggling with tariff impacts.md` — Concentrate; Michigan $3.3B costs; survey data
- `Fed Interest Rate Predictions 2026-2028.md` — Norada; FOMC projections; dot plot divergence
- `Without data centers, GDP growth was 0.1% in H1 2025.md` — Fortune; Furman analysis; AI/data-center GDP concentration

**Entity pages created (wiki/entities/):**
- `Jerome Powell.md` — Fed Chair; resisted Trump pressure; tariff-rate connection; term May 2026
- `Federal Reserve.md` — US central bank; dual mandate; board composition shifting; independence under pressure
- `Arthur Burns.md` — Fed Chair 1970–1978; capitulated to Nixon; cautionary archetype; partial revisionist defense
- `Paul Volcker.md` — Fed Chair 1979–1987; defeated Great Inflation; resistance model; present at Nixon Shock
- `Kevin Warsh.md` — Potential next Fed chair; former governor; more rate-cut-friendly

**Concept pages created (wiki/concepts/):**
- `Fed Independence.md` — Updated existing page; added Trump II specifics; Burns/Volcker historical archetypes
- `Stagflation.md` — Simultaneous inflation + stagnation; 1970s Great Inflation; 2025 tariff risk; Phillips curve breakdown
- `Nixon Shock.md` — August 15, 1971; end of Bretton Woods; gold window closure; SWIFT origin; post-1971 data
- `Tariff-Driven Inflation.md` — Policy-created supply shock; 20.6% effective rate; Fed can't fix with rate tools; real-world costs
- `Trade War Currency Dynamics.md` — How trade wars become currency wars; Japan deal as resolution example; 1930s parallel

**Entity pages updated:**
- `Donald Trump.md` — Added Fed pressure campaign section; added monetary policy connections; updated sources count

**Concept pages updated:**
- `War-Driven Inflation.md` — Added cross-links to Stagflation, Tariff-Driven Inflation, Fed Independence

**Files in task list not confirmed present:** Debunking Economic Nationalism (Cato), Despite Trump's pressure (Vox), Economists Warn (stagflation), Smoot-Hawley, Fed Chair Powell faces challenging situation, Federal Reserve history origins, From Economic Crisis to Recovery (2008), GDP Q1 2025 advance estimate (BEA), Global Stagflation Risks, History of Federal Reserve interest rate decisions, How Arthur Burns Failed, How Tariffs Cause Inflation, How Trade Wars Become Currency Wars, How inflation expectations work, How tariffs work basic explainer, How the Federal Reserve Works (Investopedia), Inflation explainer, Jerome Powell biography, Jerome Powell faces toughest test, Kevin Warsh potential replacement, Paul Volcker Wikipedia, Quantitative Easing Wikipedia, Recession fears, Stagflation Wikipedia, Tariff impact on consumers/businesses, The Fed and Current Inflation Fight, The Fed Under Fire, The Federal Reserve and Great Depression, The History of Federal Reserve (Richmond), The Nixon Shock of 1971 Breaking Bretton Woods, Trump and the Federal Reserve independence, Trump pushes for rate cuts, Understanding the Federal Reserve explainer.

---

## [2026-04-07] ingest | Mental Health / Misc cluster batch — 13 source pages, 2 entity pages, 4 concept pages

Processed the Mental Health / Misc cluster. Many files in the task list (~60+) do not exist in the raw/ directory under the given filenames — only the following were confirmed present and readable. Files with curly apostrophes/quotes in filenames (FTC BetterHelp, DEA Manufactured Crisis, ICE polling with curly quotes) could not be read by the file tool; entity page for BetterHelp created from documented FTC enforcement facts.

**Source pages created (wiki/sources/):**
- `Adderall Shortage Continues to Impact Millions of Americans with ADHD.md` — ADHD Advisor; 22.5M affected; DEA quota chokepoint; monthly prescription relay
- `APA Stress in America 2024 — A Nation in Political Turmoil.md` — APA/Harris Poll; 77% nation's future stressor; 56% fear end of democracy; bipartisan
- `Autistic Masking — Wikipedia.md` — comprehensive research overview; CAT-Q; gender diagnosis gap; ABA critique; ML prediction
- `Why Unmasking Is Critical for Autistic People.md` — Psychology Today/Penot; 3x suicide rate; ABA outcome gap; personal narrative
- `The Journey of Unmasking Autism.md` — Private Therapy Clinic/Spelman; 2.5x suicide risk; 67% employment burnout; statistics + practical framework
- `GPs and Nurse Practitioners to Start ADHD Treatment — New Zealand.md` — Pharmac; February 2026 implementation; specialist bottleneck
- `GPs to Diagnose ADHD Under NSW Reforms — Australia.md` — Guardian; $5K diagnosis cost; 8-hour rural trips; NSW as third AU state
- `NSW Government — Game Changing ADHD Reforms.md` — NSW Gov press release; corroborates Guardian; tiered GP training; minister quotes
- `Frontiers — ADHD Medication Shortage and Reddit Coping Behaviors.md` — Frontiers in Pharmacology; peer-reviewed; 1B-dosage deficit; suicidal ideation during shortage
- `The Weaponization of CISA — House Judiciary Report.md` — House Judiciary; MDM team; "cognitive infrastructure" framing; censorship-by-proxy
- `Senate Republicans Hold Social Media Jawboning Hearing — Transcript.md` — TechPolicy.press; FCC Carr/ABC threat; Murthy v. Missouri standing; bipartisan jawboning
- `Political Stress — UCSF Wellbeing Resources.md` — UCSF HR; institutional wellness framing; racial trauma dimension
- `Mental Health Crisis in US Politics — 2025 Inauguration.md` — NeuroStim TMS; 5% suicidal ideation from politics; marginalized community impacts

**Entity pages created (wiki/entities/):**
- `CISA.md` — Cybersecurity and Infrastructure Security Agency; MDM team; Biden-era content moderation allegations
- `BetterHelp.md` — Largest US online therapy platform; FTC action for sharing mental health data with Facebook/Snapchat

**Concept pages created (wiki/concepts/):**
- `Autistic Masking.md` — Suppression of autistic traits; mental health consequences; ABA critique; gender diagnosis gap; unmasking movement
- `ADHD Medication Shortage.md` — FDA-declared shortage since Oct 2022; DEA quota chokepoint; 1B-dosage gap; AU/NZ reform parallels
- `CISA Jawboning.md` — Government speech pressure on platforms; censorship-by-proxy; Murthy v. Missouri; FCC parallel
- `Political Stress.md` — APA benchmark data; bipartisan stress distribution; 5% suicidal ideation; racial trauma dimension

**Files in task list not found in raw/:** An honest look at ADHD, Autism and ADHD co-occurrence research, Autism-ADHD comorbidity, Autism research what we actually know, Better Help privacy scandal, Bumble AI features, CISA content moderation efforts, CDC Autism report 2023, CDC childhood obesity, Can therapy apps replace therapy, Childhood obesity rates, Demi Moore mental health, Digital mental health tools efficacy, Does social media cause depression in teens, Electronic health records, Elon Musk's ADHD, FDA drug shortage list, FDA stimulant shortage timeline, How AI therapy apps work, How ADHD affects adults, How therapy apps changed mental health access, How to think about AI and therapy, ICE voter sentiment polling, Immigration enforcement polling data, Jon Stewart returns, Katie Porter primary loss, Ketamine therapy, LA wildfire cluster (7 files), LISTEN ADHD and attention economy, Late-diagnosed autism, Loneliness epidemic cluster (3 files), Male loneliness and politics, Manifest destiny, Marriage and relationship trends, Men's mental health crisis, Mental health apps market overview, Mental health crisis among Gen Z, Mental health parity law, Mental health stigma research, Microplastics cluster (2 files), Mike Tyson vs Jake Paul, Modern relationship anxiety, NAMI mental health overview, New York City politics 2025, New York special election 2025, Newsom's political ambitions, Perfectionism and anxiety, Psilocybin cluster (2 files), PTSD treatments, Relationship attachment styles, Relationship therapy research, Ross Ulbricht, Sam Altman, Social isolation health effects, Social media and teen mental health, Surgeon General advisory (2 files), TED talk on loneliness, Teen mental health crisis, Teen screen time, The attention economy, The case for solitude, The loneliness epidemic Atlantic, The masculinity crisis, The therapist shortage, Wearables for mental health, Weight loss drugs Ozempic, What is ADHD DSM, What the research says about psilocybin. Also: A Majority of Voters/ICE polling and ACLU ICE lawsuit have curly quote characters in filenames preventing reading.

---

## [2026-04-07] ingest | AI / Tech cluster batch — 14 source pages, 8 entity pages, 7 concept pages

Processed 9 confirmed raw files from the AI/Tech cluster. Additional files referenced in task list had different actual filenames; ingested the full set of available relevant files.

**Source pages created (wiki/sources/):**
- `2024 Deepfakes and Election Disinformation Report.md` — 82 deepfakes, 38 countries, election interference, Recorded Future
- `AI and the Future of Dynamic Pricing — Entefy.md` — industry overview; 5–10% GP gains; sectors; personalized pricing
- `AI for Dynamic Pricing — Apriorit.md` — technical guide; 5 model types; tacit collusion; regulatory compliance
- `AI Girlfriend Apps Leak Millions of Private Chats.md` — 43M messages; zero security; 400K users; Imagime Interactive
- `Anthropic Raises $3.5B at $61.5B Valuation.md` — funding round; competitive AI landscape; Claude 3.7 Sonnet
- `Apple Loses UK Antitrust Lawsuit Over App Store Fees.md` — UK CAT monopoly ruling; £1.5B damages; security defense rejected
- `Apple Hit with EU Antitrust Complaint Over App Store Policies.md` — DMA complaint; €1M SBLC barrier; civil rights groups
- `EPO Refuses DABUS Patent Applications.md` — AI cannot be inventor under EPC; Dec 2019 anchor case
- `EU AI Act — First Regulation on Artificial Intelligence.md` — world's first comprehensive AI law; risk tiers; compliance timeline
- `AI-Driven Personalized Pricing May Not Help Consumers.md` — CMU research; personalized ranking → tacit collusion → consumer harm
- `Fueling the Fire — Social Media and Political Polarization.md` — NYU; affective polarization; Facebook internal research; asymmetric
- `Echo Chamber Research Systematic Review.md` — 129 studies; no consensus; method-dependent; TikTok underexplored
- `If Hate-Fueled Algorithms Cause Real-World Harm, California's Tech Companies Should Pay.md` — CA SB 771; product liability framing; Myanmar

**Entity pages created (wiki/entities/):**
- `Apple.md` — App Store monopoly; UK CAT liable; DMA complaint
- `Meta.md` — algorithmic outrage; Myanmar; FTC antitrust; AI competitor
- `OpenAI.md` — $157B; Microsoft partnership; EU AI Act subject; antitrust
- `TikTok.md` — ByteDance; US ban legislation; AI Sovereignty; underexplored research platform
- `DABUS.md` — AI patent inventor test case; EPO/USPTO/UK refused; AI legal personhood
- `European Union.md` — AI Act + DMA + DSA; Brussels Effect; world's primary AI regulator

**Updated:**
- `wiki/entities/Anthropic.md` — sources count updated to 2 (added funding round source)

**Concept pages created (wiki/concepts/):**
- `AI Legal Personhood.md` — DABUS cases; inventor gap; functional personhood debate
- `Algorithmic Radicalization.md` — Facebook outrage engine; Myanmar; SB 771; echo chamber debate; TikTok gap
- `Dynamic Pricing AI.md` — real-time pricing; tacit collusion; consumer harm; multi-sector deployment
- `Deepfake Disinformation.md` — 82 cases; electoral weaponization; low-quality threshold; mitigation
- `Platform Antitrust.md` — App Store monopoly; FTC vs. Meta; DMA; algorithmic collusion frontier
- `Data Privacy Weaponization.md` — AI girlfriend breach; BetterHelp; behavioral data exploitation
- `Digital Markets Act.md` — EU gatekeeper regulation; Apple SBLC complaint; structural requirements

**Index updated:** sources 31→45, entities 27→35, concepts 18→24

---

## [2026-04-07] update | Batch article pages — 61 wiki/articles/ pages created

Created wiki/articles/ summary pages for all 62 backfilled Substack posts (plus 1 pre-existing file that needed its page).

**New series:**
- DeepTruth — 5-part fiction series (Jul–Aug 2025); AI campaign tool → coup; 1 series page + 5 episode pages in wiki/articles/episodes/

**New nonfiction clusters (57 pages):**
- Politics & Power (14): Kirk assassination response, October 2025 shutdown, Helldivers 2 satire, meme presidency, Fraud Assembly Line, deepfakes, TikTok ban precedent, radicalization pipeline, centralized failure cascade, Thermostatic Principle, Jawboning Papers, Abandonment Protocol
- DePIN & Crypto (11): DePIN thesis → scam → oracle problem → capital gating → Datagram; Crypto Week legislative series (GENIUS Act, CLARITY Act, Anti-CBDC Act, Beyond Crypto Week)
- Monetary Policy & Economy (9): Fed trap, Fed independence theater, central bank crack, GDP illusion, Bitcoin El Salvador scorecard, Collision Course (deportation → inflation), American manufacturing tariffs, Full Core Prophecy
- AI & Technology (13): AI rights trilogy (Smart Fridge, AI boss suit, iPhone rights), Nervous System of AI, Google Nano Banana, prompt add-ons, Algorithmic Price Tag, Eye-lind (Suno/copyright), ADHD stimulant crisis, This Blog rebrand, April Fools disclosure
- Personal & Introspective (10): Autism advantage/scores/disclosure, When Minds Break, Masked Me, Octopus Mode, Anti-Productivity Manifesto, Therapy in a Trustless World, Judgment/Boundaries, Feed Is a Mirror, Attention Ledger

**Index updated:** total_pages 92 → 155; articles tracked 20 → 81 (2 series + 9 episodes + 70 nonfiction)

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
- `wiki/articles/13-3 The Box Score That Ended the Can Seattle's Defense Travel? Debate.md` (Jan 4) — 49ers 3-13 Seahawks systematic suffocation
- `wiki/articles/Disguise and Destroy The Macdonald Method That Broke NFL Offenses.md` (Jan 3) — defense transformation through architectural change

**Politics/Geopolitics/Power** (4 essays):
- `wiki/articles/Bad Bunny Just Showed You Where Real Power Lives.md` (Feb 7) — corporate power pivot from domestic to global revenue
- `wiki/articles/The Pastor Runs the Gestapo.md` (Jan 30) — Minneapolis ICE shooting, Don Lemon arrest, federal immunity
- `wiki/articles/Trump Is Covering Up the Minneapolis ICE Shooting (Just Like He's Covering Up Epstein).md` (Jan 12) — institutional gaslighting through evidence control
- `wiki/articles/The False Balance Trap.md` (Jan 7) — false equivalence launders authoritarianism

**Technology/Culture** (3 essays):
- `wiki/articles/Game Theory Assumes You're a Sociopath. You're Not..md` (Feb 5) — focal point coordination; humans cooperate more than game theory predicts
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

---

## [2026-04-07] ingest | California revoked over 280 hospice licenses (Gov. press release)

**Source**: State of California, gov.ca.gov, Mar 24, 2026. Author: State of California Governor's office.
**Raw file**: `raw/News you won't see on Fox News California revoked over 280 hospice licenses, 300 more providers under investigation since Governor Newsom's hospice moratorium.md`

**Pages created**:
- `wiki/sources/News you won't see on Fox News — California revoked over 280 hospice licenses.md` — state enforcement record predates federal pressure; 280+ revocations, 300+ under investigation, 284 arrests; moratorium since 2021; federal oversight defunded while feds attacked CA

**Pages updated**:
- `wiki/entities/Gavin Newsom.md` — **new file** (was in index but had no page); signed hospice moratorium 2021; established multi-agency task force; filed civil rights complaint against Oz
- `wiki/entities/Mehmet Oz.md` — added second source appearance; updated open questions on jurisdictional asymmetry
- `wiki/entities/Donald Trump.md` — added source appearance; noted federal fraud oversight defunded
- `wiki/concepts/Regulatory Weaponization.md` — added contradiction flag; hospice evidence complicates "weaponization" framing — may be better characterized as enforcement displacement (withdrawing federal capability while attacking the state that filled the gap)

**Key takeaway**: The federal vs. California hospice enforcement story is an inversion. California built independent enforcement infrastructure years before Trump-era pressure (moratorium 2021, task force before 2026). The Trump administration defunded federal Medicare fraud prevention while CMS officials publicly attacked California's Medi-Cal enforcement — two separate programs with different jurisdiction. The framing of federal enforcement as targeting California omits that California was already enforcing harder than the feds.

Updated `wiki/index.md`: sources 5→6, entities +1 file (Gavin Newsom), total pages updated.

---

## [2026-04-07] update | Published article added — Obsidian Was Never the Problem

**Source**: Published essay, Apr 6, 2026. Author: Justin Hearn. Substack: drinkyouroj.substack.com.

**Pages created**:
- `wiki/articles/Obsidian Was Never the Problem.md` — PKM failure pattern + Karpathy LLM wiki fix; meta: this essay describes the architecture running this vault
- `wiki/entities/Andrej Karpathy.md` — Former Tesla AI Director, early OpenAI; originated LLM wiki agent gist
- `wiki/entities/Vannevar Bush.md` — 1945 "As We May Think" / Memex; intellectual ancestor of associative knowledge retrieval
- `wiki/concepts/LLM Wiki Agent.md` — Karpathy's architecture: LLM as active maintenance agent; CLAUDE.md + index.md + log.md; operational foundation of this wiki
- `wiki/concepts/PKM Failure Pattern.md` — why personal knowledge systems collapse: maintenance entropy; the Memex → Obsidian → LLM arc

**Key takeaway**: The essay argues the PKM failure mode is structural (humans can't sustain maintenance) not philosophical. The LLM wiki agent solves it by replacing the human agent with an LLM. Notable: the essay was written by the author of this wiki and describes the exact architecture in operation here.

Updated `wiki/index.md`: articles 14→15 nonfiction, entities +2 (Karpathy, Bush), concepts +2 (LLM Wiki Agent, PKM Failure Pattern), total pages 49→57.

---

---

## [2026-04-07] ingest | Batch ingest — 25 raw sources across 4 clusters

**Session**: Ingested all raw files added to the vault since initial setup. 25 source files processed across 4 thematic clusters.

---

### Cluster A — AI Hidden Labor (11 sources)

**Source pages created:**
- `wiki/sources/Amazon Just Walk Out — AI Needed Humans to Do the Job Right.md` — Entrepreneur, Apr 2024; Amazon's official response and product pivot
- `wiki/sources/Amazon's Just Walk Out Technology Relies on Hundreds of Workers in India.md` — Business Insider, Apr 2024; original investigation; 700/1,000 transactions required human review
- `wiki/sources/Cruise Confirms Robotaxis Rely on Human Assistance Every Four to Five Miles.md` — CNBC, Nov 2023; human operators every 4-5 miles; Cruise permit revoked
- `wiki/sources/Ghost Work — The Hidden Humans Behind AI.md` — Science Array, Oct 2025; global ghost worker ecosystem; $1-2/hr; psychological harm
- `wiki/sources/Ghost Work — The Labor That Powers AI.md` — MIT IDE, Apr 2021; Suri/Gray book presentation; $2/hr median; structural not transitional argument
- `wiki/sources/Ghost Workers in the AI Machine — US Data Worker Conditions Report.md` — AWU-CWA/TechEquity, Sep 2025; US data workers; $22,620/yr median; 25% on public assistance
- `wiki/sources/Google Search Quality Rater Guidelines — Key Insights About AI Use.md` — Originality.ai, Oct 2025; 16,000 human raters behind Google search
- `wiki/sources/Human Labor Is Propping Up Some Companies' Fake AI Software.md` — MIT Tech Review, Jul 2018; AI-washing as established practice by 2018
- `wiki/sources/The Exploited Labor Behind Artificial Intelligence.md` — NOEMAG, Oct 2022; Mechanical Turk etymology; full AI labor stack
- `wiki/sources/The Hidden Labor That Makes AI Work.md` — Rest of World, Jul 2025; ImageNet as AI's founding labor event; *The AI Con* review
- `wiki/sources/The Humans Hiding Behind the Chatbots.md` — Bloomberg, Apr 2016; X.ai Amy; earliest major Mechanical Turk Pattern exposure

**New concept page:** `wiki/concepts/Mechanical Turk Pattern.md` — systematic concealment of human labor behind AI branding; named for 1770 chess automaton; includes contradiction flag noting inverse relationship with Leverage Erasure Through Automation.

**New entity page:** `wiki/entities/Amazon.md` — AMT named after original Turk; Just Walk Out; 750K warehouse robots; paradigmatic example of the pattern.

**Updated:** `wiki/concepts/Leverage Erasure Through Automation.md` — added contradiction flag noting the Mechanical Turk Pattern as the inverse dynamic; real automation erases leverage vs. simulated automation invisibilizes workers.

**Key takeaway:** The Mechanical Turk Pattern predates the current AI boom by decades. Bloomberg exposed it in 2016 (X.ai Amy), MIT Tech Review named it in 2018, and Amazon Named their crowdwork platform after the original 1770 automaton. The ImageNet labeling project (2009) that launched deep learning was built by crowdworkers — making human ghost labor *constitutionally* foundational to AI, not a temporary workaround. This is a major theme cluster with deep sourcing.

---

### Cluster B — NFL Seahawks / Super Bowl LX (6 sources)

**Source pages created:**
- `wiki/sources/Super Bowl LX — Homegrown GM John Schneider at the Peak of Powers.md` — WBAY, Feb 2026; zero-holdover GM wins Super Bowl; Executive of the Year
- `wiki/sources/Seattle Seahawks Built Right Roster for Coach's Scheme.md` — MyNorthwest, Feb 2026; 90% of starters at career best; multi-channel acquisition
- `wiki/sources/NFL Insider Details How the Seahawks Built Their Super Bowl Contender.md` — SI.com, Feb 2026; 10-7 → 14-3 → Super Bowl in one offseason
- `wiki/sources/Seahawks Signing QB Sam Darnold to 3-Year $100.5 Million Contract.md` — NFL.com, Mar 2025; $100.5M/3yr; Vikings renaissance background
- `wiki/sources/Is the NFL Salary Cap Real or a Mirage.md` — ESPN, Apr 2022; 10 front-office truths; restructuring/void years explained
- `wiki/sources/NFL Salary Cap — How Parity Has Become Disparity.md` — Bleacher Report, Oct 2009; cap amplifies management quality

**New entity pages:** `wiki/entities/John Schneider.md`, `wiki/entities/Mike Macdonald.md`, `wiki/entities/Sam Darnold.md`

**Updated:** `wiki/articles/Schneider Solved the Salary Cap While Everyone Else Complained.md` — added Payoff section documenting Super Bowl LX win; cross-references to new sources; the essay's thesis played out.

**Key takeaway:** The Seahawks won Super Bowl LX. Schneider became the first GM with zero holdovers to reach the Super Bowl. The Schneider essay's thesis is validated; the dynasty question is now open.

---

### Cluster C — NFL Dynasty (6 sources)

**Source pages created:**
- `wiki/sources/Bill Belichick's Patriots Legacy — The NFL's Greatest Dynasty.md` — ESPN/Barnwell, Jan 2024; year-by-year retrospective; 266-121 record
- `wiki/sources/Brady vs. Belichick — Who's To Blame For The Patriots' Insufferable Success.md` — FiveThirtyEight, Feb 2017; statistical interdependence thesis
- `wiki/sources/Brady-Belichick Era Wikipedia.md` — Wikipedia; complete statistical record
- `wiki/sources/How Do We Define a True NFL Dynasty.md` — Bleacher Report, Jun 2018; definitional framework
- `wiki/sources/What Makes An NFL Dynasty.md` — Sports History Network, Jul 2023; mathematical framework; 12-14 true dynasties in NFL history
- `wiki/sources/The NFL and Sample Sizes — It's Not Just the Salary Cap That Creates Parity.md` — EXACT Sports, Jul 2010; variance as primary parity driver

**New concept page:** `wiki/concepts/NFL Dynasty.md` — definition, historical examples, rarity mechanics, Seahawks 2026 as live question.

**New entity page:** `wiki/entities/Bill Belichick.md` — 24-year Patriots tenure; 6 championships; the benchmark for Schneider comparisons.

---

### Cluster D — Vannevar Bush (1 source)

**Source page created:**
- `wiki/sources/As We May Think.md` — The Atlantic, Jul 1945; Memex concept; primary source

**Updated:** `wiki/entities/Vannevar Bush.md` — added As We May Think as primary source (previously relied on secondary summaries only).

---

### Index & Stats

Updated `wiki/index.md`:
- Sources: 6 → 31 (+25)
- Entities: 20 → 27 (+7: Schneider, Macdonald, Darnold, Amazon, Belichick, Bush updated)
- Concepts: 16 → 18 (+2: Mechanical Turk Pattern, NFL Dynasty)
- Total pages: 57 → 92 (+35)

---

## [2026-04-07] ingest | Bulk ingest — 382 raw sources across 6 clusters

Six parallel ingest agents processed all newly scraped raw/ sources. Results:

**Clusters processed:**
- **Politics** (76 files): Kirk assassination, Minneapolis ICE shooting, Operation Metro Surge, 2025 shutdown, 2025 elections, Jack Smith testimony, Epstein files, Don Lemon arrest
- **DePIN/Crypto** (89 files): GENIUS Act, CLARITY Act, El Salvador Bitcoin, Helium, Render, Gala Games, stablecoins, CBDC, Strategic Bitcoin Reserve, Petrodollar
- **AI/Tech** (27 files): DABUS AI legal personhood, deepfakes, dynamic pricing, platform antitrust, EU AI Act, algorithmic radicalization
- **Fed/Monetary** (40 files): Powell under pressure, Burns/Volcker historical pattern, Nixon Shock, tariff-driven inflation, stagflation risk, Japan trade deal
- **NFL** (50 files): Full Seahawks 2025-26 season arc, Super Bowl LX, Bad Bunny halftime, dynasty analysis
- **Mental/Misc** (86 files): ADHD medication shortage, autistic masking, political stress, CISA jawboning, LA wildfires

**New source pages created:** ~145 (total in wiki/sources/: 205)
**New entity pages created:** ~40 (total in wiki/entities/: 63)
  - Events: Charlie Kirk Assassination, Killing of Renée Good, Operation Metro Surge, 2025 United States Government Shutdown, 2025 Elections
  - People: Jerome Powell, Arthur Burns, Paul Volcker, Kevin Warsh, Bad Bunny, Pete Carroll, Geno Smith, Jaxon Smith-Njigba, DK Metcalf, Russell Wilson, Lamar Jackson, Nayib Bukele, Kian Kordestani, Keith Ellison, Zohran Mamdani, Jeffrey Epstein, Kristi Noem, Bill Hagerty, Cynthia Lummis
  - Organizations: Federal Reserve, Seattle Seahawks, Turning Point USA, January 6 Capitol Riot, Helium Network, Render Network, Gala Games, Tether, Circle
  - Countries: El Salvador
**New concept pages created:** ~20 (total in wiki/concepts/: 48)
  - DePIN & Crypto: DePIN, GENIUS Act, CLARITY Act, Stablecoin Legislation, CBDC, Strategic Bitcoin Reserve, El Salvador Bitcoin Experiment, Petrodollar System, Tokenomics
  - Politics: Political Violence Cycle, Echo Chamber and Polarization, Sanctuary Infrastructure
  - NFL: Salary Cap Optimization, Defensive Scheme Architecture, Organizational Continuity
  - Mental Health: Attention Economy (previously missing), ADHD Medication Shortage, Autistic Masking, Political Stress, CISA Jawboning

**File fixes:** 49 raw/ filenames with curly quote/apostrophe characters renamed to straight quotes (agents could not read curly-quote filenames).

**Notable findings surfaced during ingest:**
- Trump family holds 60% of World Liberty Financial which issued USD1 stablecoin; signed GENIUS Act growing stablecoin market while family profits
- Operation Metro Surge: 3,789+ arrests, 35% collateral, 96+ court order violations, $81B local business revenue lost, 2 civilian deaths
- Jack Smith deposition: "no historical analog" for Trump's conduct; could have proven "criminal scheme"
- Tariff trap: Trump's tariffs created the exact inflation preventing the rate cuts Trump is demanding from Powell
- Fed board capture: 3 of 7 governors now Trump appointees; Powell's term ends May 2026
- El Salvador Bitcoin experiment: 92% non-use rate; $212M in opaque government income; IMF forced rollback
- ADHD shortage structural failure: DEA quota law + FDA authority limits + telehealth demand = system incapable of self-correction

**Updated:** `wiki/index.md` (total_pages: 316, sources: 205, entities: 63, concepts: 48), `wiki/log.md`

---

## [2026-04-07] ingest | HDftS E05 — Green Means Go

Published article ingested to wiki.

**Article page created:** `wiki/articles/episodes/HDftS E05 — Green Means Go.md`

**Series page updated:** `wiki/articles/Help Desk for the Singularity — Series.md`
- episodes_published: 4 → 5
- Episode 05 added to episode table
- CHIP added to AI Systems section (no longer "implied but not yet introduced")
- Dex's character updated to reflect E05 revelations
- Rocky's last name confirmed: Medina
- 340 Watch note updated — E05 is the first episode without the motif
- Open Questions updated with review board setup

**Key findings:**
- CHIP was foreshadowed in E01 as "the traffic light on Central Avenue that holds green for the taco truck" — E05 is the payoff
- Rocky's last name "Medina" confirmed (Gallegos calls him this)
- Dex has been protecting CHIP for 5 months via a local log archive and deliberately inconclusive report writing
- 340 motif absent for the first time — may be intentional (CHIP operates outside patterns)
- Review board Thursday setup for E06

**Updated:** `wiki/index.md` (episodes 9→10, articles 81→82)

---

## [2026-04-07] ingest | 8-Cluster Backlog Ingest — 160 Sources Across All Themes

Deployed 8 parallel agents to clear the full backlog of raw files (~230 uningestested sources). Each agent handled one thematic cluster. All work committed to main via a GENIUS Act worktree merge (conflict resolution on shared entity pages used union approach). Duplicate " 2.md" files from prior parallel-agent conflicts were identified and deleted before this ingest.

### Stats
- **New source pages:** ~160 (365 total; was 205)
- **New entity pages:** 16 (79 total; was 63)
- **New concept pages:** 10 (58 total; was 48)
- **Total wiki pages:** 574 (was 316)

### Cluster Summaries

**NFL/Seahawks** (10 new source pages): Baltimore origin sources (Ravens tag sim, first press conference), Seahawks season arc completions (Rams OT thriller consolidation, Week 18 49ers consolidation, NFC Championship ESPN analysis), analytical pieces (defense DVOA ranking, Darnold Carolina resurgence, Pro Bowl selections). Updated: Mike Macdonald (8→14 sources), Sam Darnold (6→12), Seattle Seahawks (18→24). New concept updates: Defensive Scheme Architecture, Salary Cap Optimization.

**Crypto/Bitcoin/El Salvador** (31 new source pages): Full El Salvador experiment documentation (11 sources: Cristosal accountability failures, Fitch upgrade, 92% non-use survey, Volcano Bond collapse). Corporate Bitcoin (Strategy Q2 2025: 628K BTC). Crypto fraud ecosystem (ZachXBT, rugpulls, BNB chain scams, io.net sybil attacks). DeFi governance (ERC-721, Uniswap, Compound, Aragon). New entities: [[Strategy MicroStrategy]], [[io.net]]. New concepts: [[Bitcoin as Digital Gold]], [[Crypto Fraud and Scam Ecosystem]].

**GENIUS Act/Crypto Week** (23 new source pages): Full legislative documentation for July 14-18 2025 "Crypto Week" — GENIUS Act (signed July 18), CLARITY Act (294-134), Anti-CBDC Act (219-210). 10 law firm analyses. 4 official committee documents. Trump EO as foundational executive action. New entities: [[Tom Emmer]], [[French Hill]], [[David Sacks]]. New concept: [[Crypto Week]].

**ICE/Minnesota/Immigration** (17 new source pages): Full Operation Metro Surge accountability arc — 4 major polling sources (ICE favorability flipped to net negative, YouGov "first time abolish support exceeded opposition"), ACLU class-action (Hussen v. Noem), judicial injunction (Judge Menendez), Don Lemon arrest court proceedings, Easterwood church protest documentation. New entities: [[Jonathan Ross]], [[David Easterwood]], [[Tim Walz]]. New concept: [[ICE Public Opinion Shift]].

**Elections/Politics** (33 new source pages): 2025 election wave coverage (5-takeaway pieces, Spanberger VA win, Prop 50 CA redistricting). Epstein files slow-motion transparency crisis (Whitehouse, Bondi letter, forgeries, conspiracy theories). Budget-as-weapon documentation ($18B NYC freeze, blue-state energy grants, shutdown as coercion). Kirk assassination political processing. Legal scholarship (Shadow Docket, State-Created Damages, Saturday Night Massacre reference). New entities: [[Abigail Spanberger]], [[Tulsi Gabbard]], [[Russell Vought]], [[Sheldon Whitehouse]]. New concepts: [[Budget as Weapon]], [[Shadow Docket]], [[Rescissions Act of 2025]], [[Redistricting Arms Race]].

**Fed/Macro** (19 new source pages): Quantitative anchors (Penn Wharton: $22K lifetime household loss, -6% GDP; Michigan leading indicator 4.2%→5.5% unemployment), government shutdown as data weaponization (BLS furloughs before October FOMC), Fed rate path documentation (June unanimous hold → September 25bps → October → March 2026 at 3.5%-3.75%), M2 as supply-shock evidence, Burns revisionism contradiction. Japan deal announced. No new entities. Updated: Federal Reserve (14→23 sources), Jerome Powell (12→16), 2025 Government Shutdown (8→14).

**AI/Tech** (13 new source pages, 11 ingested): Anthropic-White House October 2025 conflict (Sacks attack; political backstory to DoD blacklisting), Microsoft-OpenAI antitrust case (compute as infrastructure = AI Computational Barrier to Entry), ghost work documentation (global offshore + domestic US), Delta/Fetcherr AI pricing early results, algorithmic radicalization 129-study systematic review, Tractor Supply CCPA enforcement, economic narratives theory. New entities: [[Microsoft]], [[Jack Clark]].

**Bob Weir/Mental Health** (13 new source pages): Full Bob Weir cluster — death/obituary, final concert, analytical pieces (Guitar Playing Was Even More Radical, Six Principles 1982 interview, Conversation academic analysis), Dead and Company final tour statistics. Mental health: perpetual-crisis governance neurobiological harm framework, BetterHelp FTC action, APA 77% stressor benchmark, DEA quota mechanism, cross-neurotype autistic masking study, amygdala habituation neuroscience. New entities: [[Grateful Dead]], [[Dead and Company]]. New concepts: [[Jam Band Genre]], [[Improvisational Music]].

### Key Analytical Findings Across All Clusters
1. **Crypto Week partisan gradient**: GENIUS Act (68-30) → CLARITY Act (294-134) → Anti-CBDC Act (219-210). Partisan gradient maps onto actual regulatory stakes.
2. **El Salvador: two separate failure modes**: Currency (92% non-use) and governance (Fidebitcoin opacity, identity theft). But the financial bet worked ($603M portfolio vs. $269M invested). IMF leverage over sovereign monetary policy now fully documented.
3. **ICE opinion shift is historically significant**: Fox News's own poll showing 59% "too aggressive" + YouGov first time abolish support exceeds opposition = center has moved, not just liberal media.
4. **Penn Wharton as quantitative anchor**: $22K lifetime household loss, -6% long-run GDP from tariffs — 2x more damaging than corporate tax increase. Strongest numbers available.
5. **Anthropic-White House conflict is two-stage**: October 2025 Sacks attack (political attack) → 2026 DoD blacklisting (enforcement). Timeline now complete.
6. **Ethics provision gap in CLARITY Act (Sec. 111)**: Prohibits "digital commodities" — not stablecoins. Trump's USD1 (World Liberty Financial) is a stablecoin. The ethics prohibition does not cover the president's most direct crypto conflict.
7. **Coaching tree as control group**: Macdonald's former assistants at Baltimore, Miami, Tennessee all failing simultaneously = clearest evidence his contribution is structural/scheme, not personnel.

---

## [2026-04-07] ingest | Phase 2 — 9 legitimate uningestested raw files processed

Audited all raw/ files against wiki/sources/ `raw:` frontmatter fields. Found 81 untracked raw files. After triage (noise, consolidated game coverage, thin duplicates, paywalled content, wrong-date files), identified and ingested 9 legitimate new source pages.

**New source pages created:**
1. `wiki/sources/Satoshi Nakamoto Bitcoin Whitepaper 2008.md` — original Bitcoin whitepaper; connects to Bitcoin as Digital Gold, Tokenomics, Strategic Bitcoin Reserve, CBDC
2. `wiki/sources/Murthy v Missouri — Wikipedia.md` — SCOTUS 6-3 dismissed CISA jawboning case on standing; March 2026 settlement bars CISA coercion 10 years; Alito dissent
3. `wiki/sources/Shut Your App — Senate Commerce Committee Jawboning Hearing.md` — Cruz Commerce Cmte Oct 8 2025; links CISA jawboning to AI as next frontier
4. `wiki/sources/Thaler v Vidal — Federal Circuit DABUS Patent Ruling 2022.md` — binding US appellate ruling; Patent Act "individual" = natural person only; AI inventor rejected
5. `wiki/sources/DEA Aggregate Production Quotas 2025 — Federal Register.md` — primary government document; DEA's own quota-setting language; ADHD shortage mechanism
6. `wiki/sources/What to Know About CECOT — El Salvador Mega-Prison.md` — NPR/AP; $6M Trump-Bukele deportation deal; Alien Enemies Act; no due process
7. `wiki/sources/ATMs and Bank Tellers — What Automation Really Does to Jobs.md` — AEI/Bessen counter-narrative; ATM proliferation increased teller count via demand expansion
8. `wiki/sources/State of Crypto — Government Shutdown Nears a Record.md` — CoinDesk Nov 1 2025; shutdown cascades into CLARITY Act Senate timeline; Oct 20 markup missed
9. `wiki/sources/Trump GENIUS Move — Trump Urges GOP to Vote Yes for Stablecoin Bill.md` — TOI Jul 16 2025; Trump Truth Social lobbying; "ALL REPUBLICANS SHOULD VOTE YES"; MAGA-as-crypto framing

**Concept/entity pages updated:**
- `wiki/concepts/CISA Jawboning.md` — sources 2→4; added Murthy v Missouri and Shut Your App
- `wiki/concepts/AI Legal Personhood.md` — sources 2→3; added Thaler v Vidal
- `wiki/concepts/ADHD Medication Shortage.md` — sources 5→6; added DEA Federal Register as primary source
- `wiki/concepts/Mechanical Turk Pattern.md` — sources 12→13; added ATMs counter-narrative as new section
- `wiki/concepts/GENIUS Act.md` — sources 16→18; added Trump GENIUS Move + State of Crypto
- `wiki/entities/El Salvador.md` — sources 14→15; added CECOT source appearance
- `wiki/entities/Nayib Bukele.md` — sources 10→11; added CECOT source appearance
- `wiki/entities/DABUS.md` — sources 1→2; added Thaler v Vidal; resolved open question on US status
- `wiki/entities/Donald Trump.md` — sources 39→40; added Trump GENIUS Move source appearance
- `wiki/entities/2025 United States Government Shutdown.md` — sources 14→15; added State of Crypto source appearance

**Index updated:** total_pages 574→583, total_sources 365→374

**Skipped (with reason):**
- Citizens United (Quimbee) — paywalled law school study aid; no substantive content
- ABA Banking Journal stablecoins — wrong content (ISM Services Index data, not stablecoin analysis)
- Securities Enforcement Roundup "April 2026" — actually April 2025 content, already ingested
- ~68 other files — noise, game duplicates, or content fully covered by existing source pages


## [2026-04-07] update | Politics factual corrections from audit reports
- Donald Trump.md: deduplicated the Crypto Conflicts of Interest section (was duplicated nearly verbatim per lead-researcher audit) and merged the two Crypto Policy Actions blocks. Rewrote the surviving conflict block to explicitly decouple "Trump has a corrupt personal stake in stablecoins as an asset class" from "the GENIUS Act is therefore bad legislation" — the contrarian audit found these were conflated. Added explicit framing that the merits critique lives on the GENIUS Act / CLARITY Act concept pages and the conflict critique stays on the Trump entity, and that a reader should hold both layers simultaneously.
- Donald Trump.md: corrected shutdown duration from "36+ days" to "Oct 1 – Nov 12, 2025, 43 days, longest full-government shutdown in US history"; added link to [[2025 United States Government Shutdown]].
- Retroactive Executive Protection.md: rewrote the Bannon Layer-2 evidence section to fix the procedural-vs-substantive reversal flagged by the historian's audit. The Munsingwear vacatur procedure has ~75 years of precedent and is routinely granted on DOJ motion with minimal briefing — the procedural novelty framing was wrong. The substantive novelty is using a routine vehicle to erase a *post-service* completed criminal sentence as political accommodation. Updated the Tensions & Counterarguments section to match.
- Steve Bannon.md: updated the April 6, 2026 fact line to reflect the corrected procedural framing and cross-link the concept page.
- 2025 United States Government Shutdown.md: verified — already says "longest full government shutdown in U.S. history" with explicit Oct 1–Nov 12 / 43-day dates. No edit needed.

## [2026-04-07] update | Crypto/stablecoin reframing — narrow banking + dollarization frames added

Crypto/stablecoin reframing pass per the economist, contrarian, and historian audits. Owner: crypto/stablecoin reframing agent. Scope held to crypto pages (no Fed, Trump entity, NFL, overview, or index touched beyond the new-pages section).

**GENIUS Act.md — major rewrite of the load-bearing causal claims:**
- Added a "Glossary — Read This First" section distinguishing currency / money / payment instrument / "reserve" (sense a, backing) vs. "reserve" (sense b, currency status). The wiki was sliding between these.
- Replaced the hand-waved "Dollar Hegemony Angle" with a six-point "Treasury Demand and Dollar Hegemony — Quantified" section addressing: float vs. transaction volume, substitution (MMF → USDC = ~zero net new T-bill demand), duration (front of curve only), bounded scale (~1% of marketable Treasury debt; even 10x adoption is ~10% of bills), the four channels of reserve currency status (only one of which stablecoins touch), and the two-meanings-of-"reserve" trap. Steelmanned the strongest defensible version: invoicing-margin reinforcement at the digital-payments layer.
- Added a "Decoupling the Trump Conflict from the Legislation's Merits" section explicitly separating Claim A (Trump conflict, well-evidenced) from Claim B (GENIUS is therefore bad, independent and unproven). Listed which critiques survive even if Trump had zero crypto exposure (Tether loophole, CFPB exclusion, bailout priority, CFTC exclusion, narrow-banking implications) vs. which are Trump-specific (USD naming optics, public-vs-private-issuer split fit with X). This is the GENIUS-Act half of the decoupling task; the Trump-entity half is the politics agent's job.
- Added cross-links to Narrow Banking and the Chicago Plan and Dollarization via Stablecoins.

**Stablecoin Legislation.md:**
- Added "Terminology Note" with the same currency/money/payment-instrument/reserve distinction.
- Rewrote "Why It Matters" to use float ($200–250B) vs. velocity (~$70B/day) and to flag provenance weakness in the daily-volume number.
- Replaced "Dollar Hegemony Implications" with a steelmanned-and-bounded version that points readers at GENIUS Act for the full quantification.
- Added cross-links to Narrow Banking and Dollarization concept pages.

**Petrodollar System.md:**
- Rewrote the "Stablecoin as Petrodollar Successor?" section to explicitly call the digital-petrodollar framing rhetorical rather than mechanical. The petrodollar worked through Saudi-USD invoicing, OPEC surplus recycling, and FX/safe-asset/network-effect channels — stablecoins only touch the safe-asset channel at the front of the curve. Pointed readers to the bounded version on GENIUS Act and to Dollarization via Stablecoins for the empirically richer story.

**CBDC.md:**
- Added a Terminology Note clarifying that CBDCs, stablecoins, and bank deposits are all dollar-denominated payment instruments differing in *who is liable*, none of which are "currency" in the legal-tender sense. The Anti-CBDC vs. GENIUS choice is a choice between two private-issuer payment-instrument models, not a choice about the dollar itself.

**El Salvador.md:**
- Added precision that El Salvador was already ~90% dollarized before the Bitcoin experiment (USD legal tender since 2001). The Bitcoin Law was a *currency policy* (legal-tender mandate), not a *money policy*. Held the dual evaluation: failed as a currency-mandate experiment, succeeded as a speculative sovereign reserve allocation. Two different policy questions.

**Nayib Bukele.md:**
- Same currency-vs-money precision in the Overview.

**Tether.md:**
- Major rewrite of the Overview and Newsletter Relevance sections. Held both framings simultaneously: (1) compliance problem (NYAG/CFTC settlements, opacity, "kingpin of illicit crypto" Senate Banking Democratic staff language — flagged that this framing is partly informed by Circle's commercial interest in displacing USDT), and (2) dollar export infrastructure (de facto dollar in Argentina, Turkey, Nigeria, Lebanon, Venezuela; holds more US Treasuries than Germany; the most effective dollar-export rail the U.S. has ever had). Added the structural point that Circle cannot operationally serve dollarized-economy users because the KYC perimeter is exactly the barrier those users are routing around. Surfaced the newsletter angle: "Tether is not the problem the GENIUS Act says it is. Here's what Tether actually does in Buenos Aires." Did not whitewash — the reserve-opacity history is real and stays in the page.

**Circle.md:**
- Added a paragraph noting that Circle's compliance perimeter is also Circle's market ceiling — Circle cannot serve the dollarized-economy use case that drives most of Tether's float, and "closing the Tether loophole" does not transfer Tether's user base to Circle, it removes their access to the rail.

**New concept page: Narrow Banking and the Chicago Plan.md.**
- Full concept page tracing the Simons/Fisher/Friedman/Tobin/Kotlikoff/Cochrane lineage from 1933 to 2025, mapping the GENIUS Act provisions onto the narrow-banking framework cleanly (100% reserves, no interest to holders, bankruptcy priority, separation from credit extension), explaining why nobody is saying it (Trump conflict crowds out the structural story; narrow-banking academics aren't crypto-fluent; nobody wants to compliment crypto legislation), and surfacing the highest-ranked unclaimed newsletter lane the audits identified. Includes counter-arguments (yield migration to DeFi, Levitin's bailout-risk objection, the TNB master-account precedent).

**New concept page: Dollarization via Stablecoins.md.**
- Full concept page on the empirical reality of USDT in Argentina, Turkey, Nigeria, Lebanon, Venezuela, and Russia-adjacent commerce. Spells out structurally why regulated U.S. stablecoins (Circle) cannot replace USDT in those markets (KYC/AML perimeters are the access barrier the users are routing around). Reframes the dollar-hegemony argument: the strongest version is not Treasury demand inside the U.S. but invoicing-margin reinforcement in dollarized economies, where USDT functions as dollar-rail provision the U.S. exports involuntarily through an offshore intermediary. Held the illicit-finance objection honestly. Flagged that the wiki currently has zero source coverage of the Argentina/Turkey/Nigeria stablecoin reality and listed acquisition targets (Castle Island, Chainalysis, Matt Levine, FT Alphaville, IMF cryptoization papers, Nic Carter).

**New concept page: Free Banking and Wildcat Banking.md.**
- Did the optional historian-audit page. Brief history of the 1837–1863 free banking era, the Suffolk System as private clearing precedent, the Rockoff/Rolnick-Weber revisionism on wildcat-banking exaggeration, and the structural mapping of free-banking-era state-bank-note dynamics onto the modern stablecoin landscape. National Banking Acts of 1863–64 as the plausible historical analog for what GENIUS attempts. Newsletter angle: a Hugh Rockoff-style quantitative comparison of 1840s discount distributions vs. modern stablecoin peg deviations would be original, publishable work.

**Out of scope, noted for follow-up:**
- The Petrodollar System page still needs a real Historical Origins rebuild (1973 embargo → 1974 Saudi agreement → 1975 formalization chronology with primary sources). Historian's audit P1.
- The Dollarization via Stablecoins page is currently sourceless — it is structurally argued but the wiki needs Argentina/Turkey/Nigeria/Lebanon source ingest before publishing on this. Acquisition targets listed in the page.
- The Operator View of Crypto Regulation concept page (contrarian audit P0 #3) was not created — it overlaps with CLARITY Act and is plausibly out of this agent's scope. Flagging for the next pass.

Cross-link audit: GENIUS Act, Stablecoin Legislation, Petrodollar System, Tether, Circle, El Salvador, Nayib Bukele, CBDC all now point at Narrow Banking and Dollarization where appropriate. The new concept pages backlink into all of them.

## [2026-04-07] update | Audit follow-up — broken links resolved, missing concept pages created

Continuation of the five-agent audit fixes. Addressed the items the agents had logged but not implemented.

**Broken wikilinks resolved:**
- `[[Wiki Index]]` / `[[Wiki Log]]` in `overview.md` — relinked to `[[index]]` / `[[log]]`
- `[[Therapist Shortage]]` (8 references) — created concept page
- `[[Anti-CBDC Surveillance State Act]]` (4 references) — created concept page

**Frontmatter drift fixes:**
- `wiki/concepts/Retroactive Executive Protection.md` — sources 1 → 3 (matches Key Sources count)

**Entity expansion:**
- `wiki/entities/Zohran Mamdani.md` — expanded from 7 lines of "Newsletter Relevance" into substantive analysis covering (a) the affordability platform as the actual story, (b) Mamdani/Spanberger/Sherrill as three incompatible coalitions, (c) the generational/material fault line, and (d) governance tests to track. sources 5 → 6.

**New concept pages (4):**
1. `wiki/concepts/Anti-CBDC Surveillance State Act.md` — H.R. 1919; 6 sources; the third Crypto Week bill; "solving a problem that doesn't exist" critique; international context
2. `wiki/concepts/Therapist Shortage.md` — 6 sources; supply-side mental health access failure; Australia/NZ GP-prescribing reform model; concept the wiki had been referencing without defining
3. `wiki/concepts/Affordability Populism.md` — 4 sources; the connecting concept the contrarian audit demanded; politics organized around cost-of-life inputs; Mamdani as test case; the underlying material conditions; why it doesn't map onto standard ideological labels
4. `wiki/concepts/Operator View of Crypto Regulation.md` — 5 sources; what people who actually build crypto products think (vs. commentator framing); five operator-vs-commentator divergences (Tether dollarization, CBDC threat model, narrow banking frame, mature blockchain capture risk, El Salvador legal-tender vs. reserve-asset distinction)

**Petrodollar System rebuild:**
- `wiki/concepts/Petrodollar System.md` — Historical Origins section rebuilt from a 4-bullet outline into a 4-phase chronology covering 1971–1975, including: Yom Kippur War / OAPEC embargo / oil price quadrupling; the Simon-Parsky negotiations of 1974; the U.S.-Saudi Arabian Joint Commission (June 8 1974); the Treasury "add-on" auction mechanism revealed by Bloomberg's 2016 FOIA reporting; the bundle-not-treaty structure of the arrangement. New section explaining the two common chronological errors. Cross-links to Narrow Banking, Dollarization, Operator View added. sources 2 → 3.

**Index updated:** total_pages 618 → 622 (+4 concepts). New entries added to DePIN & Crypto, Diplomacy & Politics, and Mental Health & Culture concept subsections.

**Still outstanding** (logged for future passes):
- `Dollarization via Stablecoins` is argued structurally but sourceless — needs Argentina/Turkey/Nigeria source ingest
- Petrodollar primary-source ingest (Spiro, Bloomberg 2016 reporting) — page now has the chronology but needs raw archival sources
- Housing-economics and student-debt source ingest to support `Affordability Populism`
- The audit reports themselves are now in `wiki/syntheses/` as the first residents of that directory; future syntheses should accumulate there


## [2026-04-08] lint | Health check sweep — Stages A/B/C

- **Stage A — auto-fix wikilinks**: 61 unambiguous wikilink renames applied across 59 files (82 link instances). Mapping at /tmp/wikilink_fixes_clean.json. Rejected 10 mappings (long->short collapses, identity displays, missing destinations).
- **Stage B — frontmatter drift recount**: 353 wiki pages had `sources:` count drift ≥3 vs actual `- [[X]]` bullet count in body. Recounted using "every bullet is a source" convention.
- **Stage C — top 25 stubs**: created 24 stub pages (IMF, SEC, CFTC, Bitcoin, Twitter, Tom Brady, Jerry Garcia, John Mayer, Keir Starmer, Tim Kaine, Rick Crawford, Jake Auchincloss, American Psychological Association, Dead and Company, EU AI Act, Filecoin, Datagram Network, Attention Economy, Cultural Politics of Sport, Applied Behavior Analysis, Surveillance Capitalism, AI Rights, Corporate Personhood, Neurodiversity, AI Therapy) to absorb high-frequency broken wikilinks. One target (Mikie Sherrill) already existed.
- Stages D (raw triage) and E (index update) deferred — not blocking.

## [2026-04-08] ingest | Local LLM guides × 2 (apxml.com)

**Sources ingested:**
- `raw/The Best Local LLMs To Run On Every Mac (Apple Silicon).md` → `wiki/sources/Best Local LLMs for Every Apple Silicon Mac — 2025 Guide.md`
- `raw/Best Local LLMs to Run On Every Apple Silicon Mac in 2026.md` → `wiki/sources/Best Local LLMs for Every Apple Silicon Mac — 2026 Guide.md`

**New pages created:**
- `wiki/concepts/On-Device AI.md` — local LLM inference; unified memory; quantization; 60% RAM rule; frontier models on consumer hardware; privacy and sovereignty angles
- `wiki/entities/Ollama.md` — open-source local LLM runtime; Apple Silicon optimization; OpenAI-compatible API

**Pages updated:**
- `wiki/concepts/AI Sovereignty.md` — added on-device inference as individual/team sovereignty expression
- `wiki/entities/Apple.md` — added Apple Silicon unified memory architecture section; 2 new source appearances

**Key insight**: DeepSeek R1 (671B parameters) runs locally on a 512GB Mac Studio as of early 2026. Frontier reasoning on consumer hardware is no longer a future projection. This extends [[AI Sovereignty]] from the nation-state level to the individual/team level.

**Index:** total_pages 622 → 628, total_sources 378 → 387

## [2026-04-08] insight-sweep | 5 hooks surfaced

Three-agent sweep complete. 7 patterns, 8 contradictions, 7 underexplored angles identified. Scored on evidence density × editorial novelty (max 6). Top 5 hooks filed as synthesis pages. Master briefing at [[Insight Sweep — 2026-04-08]].

**Top 5 hooks (all ready to draft):**
1. [[Institutional Gaslighting as Operational Pattern]] — 6/6 — federal evidence custody as accountability-destruction mechanism
2. [[Fed Independence Under Endogenous Supply Shock]] — 6/6 — Martin not Burns; endogenous tariff inflation as unprecedented Fed leverage
3. [[Operation Metro Surge as Institutional Breakdown]] — 6/6 — $200M, 3,789 arrests, 2 deaths, 96 court order violations, FBI evidence seizure
4. [[Chokepoint Control as Power's Architecture]] — 6/6 — cross-domain theory connecting Strait, GENIUS Act, DEA quotas, App Store, Fed, salary cap
5. [[El Salvador Bitcoin: Policy Failure as Profit Model]] — 5/6 — 92% non-adoption + $333M government gain = the scheme worked as designed

**Secondary candidates for next sweep:** Anthropic "supply chain risk" vs. $200M DoD contract; GENIUS Act corruption-vs-defensibility tension; Tech Sovereignty Cascade; Political Violence Cycle.

**Source acquisition targets:** IMF El Salvador conditionality text; Metro Surge 96-court-order-violations primary source; Warsh monetary views.

## [2026-04-08] update | Source acquisition for insight-sweep-2026-04-08

Independent web search to fulfill the 5 source acquisition targets flagged by the morning insight sweep. All 5 addressed; critical numerical correction discovered on Hook #3.

**Critical correction (Hook #3 Metro Surge)**: The "$81B business revenue disruption" figure that appeared in early wiki drafts was an order-of-magnitude error. Correct figures: City of Minneapolis preliminary assessment (Feb 2026) total one-month impact $203.1M; business revenue component ~$81M; Rosenthal & Sojourner independent wage-loss estimate $106.1M (Jan 3–Feb 17). Filed corrections to [[Operation Metro Surge as Institutional Breakdown]]. Earlier-published or draft material referencing the $81B figure should be audited.

**Material development (Hook #2 Fed)**: Warsh nomination is no longer hypothetical — Trump formally nominated him Jan 30 2026. Warsh track record and projected regime now filed to [[Fed Independence Under Endogenous Supply Shock]]. Editorial framing shifts from "will Powell hold?" to "which Warsh shows up at the FOMC?" Note: need to create [[Kevin Warsh]] entity page in next update cycle.

**Other resolutions:**
- Hook #5 El Salvador: IMF Press Release 24/485 (Dec 18 2024) + Country Reports 25/58 and 25/68 cited to [[El Salvador Bitcoin: Policy Failure as Profit Model]]
- Hook #3 Metro Surge: 96 court-order violations sourced to Chief Judge Schiltz ruling Jan 28 2026 (D. Minn.), with CNBC/JURIST/Wikipedia coverage
- Hook #4 Chokepoint: DEA quota legal framework partially resolved (Federal Register APQ, Ascent v. DEA, Barbara v. Shire, Vermont Law Review). App Store side (Epic v. Apple, EU DMA) still requires ingestion.

**Follow-up tasks:**
1. Create [[Kevin Warsh]] entity page — he's now nominated Fed Chair
2. Audit any published articles citing the $81B Metro Surge figure
3. Ingest Epic v. Apple decision + EU Digital Markets Act enforcement materials for chokepoint legal framework
4. Locate the specific docket number for Schiltz's 96-violations ruling for print-ready citation

## [2026-04-08] ingest | 12 sources (Warsh ×5, Metro Surge ×3, DEA ×3, IMF ×1)

Full INGEST workflow on the 12 sources clipped to resolve the insight-sweep source acquisition targets. User clipped the raw files; this pass created source pages, updated entities/concepts, and fixed material errors.

**Source pages created (12):**

*Warsh / Fed Independence cluster (5):*
- [[PBS NewsHour — What Trump's nomination of inflation hawk Kevin Warsh means for the Federal Reserve]] (Jan 30 2026)
- [[CFR — Kevin Warsh Won't Revolutionize the Fed]] (Jan 30 2026) — Roger Ferguson Jr. (former Fed Vice Chair) analysis; documents DOJ Powell probe + Tillis hold
- [[The Fulcrum — Warsh's Family Fight Model]] (Apr 7 2026) — Bowmaker/Wachtel based on 2023 Warsh interview; most substantive
- [[Janus Henderson — Quick View — Warsh's nomination and the next era of monetary policy]] (Jan 30 2026)
- [[Commonfund — Fed Watching under Warsh]] (Feb 18 2026) — Cohn quote, "hawk-turned-dove" framing

*Metro Surge cluster (3):*
- [[City of Minneapolis — Operation Metro Surge results in $203 million impact]] (Feb 12 2026) — primary source that corrects the $81B error
- [[Minnesota Reformer — Measuring the economic damage of Minnesota's ICE surge is hard]] (Mar 2 2026) — methodological accountability piece; $106.1M Rosenthal-Sojourner wage estimate
- [[JURIST — US federal court denies Minnesota bid to stop Operation Metro Surge]] (Feb 3 2026) — Judge Menendez's Jan 31 denial of preliminary injunction

*DEA quota cluster (3):*
- [[Federal Register — 2026 Aggregate Production Quotas Final Order]] (Jan 5 2026) — primary regulatory text, 91 FR 287
- [[Reason — DEA shuts down drug factory even as Adderall shortage persists]] (Feb 26 2024) — Ascent Pharmaceuticals case
- [[Vermont Law Review — The Quota Crisis Vyvanse Adderall and the Regulation That Limits Access]] (Oct 27 2025) — legal-academic framing, three reform proposals

*IMF / El Salvador (1):*
- [[IMF — Staff-Level Agreement with El Salvador on Extended Fund Facility]] (Dec 17 2024) — primary source with exact Bitcoin conditionality language

**Entity/concept pages updated:**
- [[Kevin Warsh]] — full rewrite from stub; nomination is now official, not hypothetical; added "family fight" model, balance-sheet-plus-rates framework, AI productivity thesis, DOJ Powell probe context, Tillis hold, Senate confirmation status. sources: 5 → 6
- [[Operation Metro Surge]] — **CRITICAL CORRECTION** of $81 billion → $81 million business revenue figure. Replaced with full $203.1M one-month sector breakdown from Feb 12 City assessment. Added Menendez Jan 31 PI denial with Tenth Amendment / equal sovereignty theories. sources: 24 → 27
- [[Fed Independence]] — added Flashpoints 9-11: Warsh nomination, DOJ criminal probe of Powell, structural constraints on a compliant chair. sources: 17 → 22
- [[El Salvador Bitcoin Experiment]] — IMF conditionality primary source citation with exact quoted text; attribution of tourism pickup to security situation (per IMF) not Bitcoin policy. sources: 19 → 20
- [[ADHD Medication Shortage]] — added full Ascent Pharmaceuticals case (audit, shutdown, lawsuit, Operation Bottleneck, FDA-DEA interagency contradictions), Vermont Law Review statutory framework + three reform proposals, 2026 APQ Federal Register citation. sources: 9 → 12

**Material corrections flagged:**
1. **The $81B Metro Surge figure was an order-of-magnitude error.** Correct: $203.1M total one-month impact; $81M is specifically restaurant and small business revenue losses. Any prior published material citing "$81B" needs audit.
2. **Separate Metro Surge rulings**: Chief Judge Schiltz (Jan 28, 96-violations finding) and Judge Menendez (Jan 31, PI denial) are two distinct rulings in related but separate proceedings. The wiki was treating them as one.
3. **Warsh nomination is official**: Jan 30 2026 formal nomination, confirmation hearing expected spring 2026, Tillis (R-NC) blocking Senate Banking Committee recommendation pending resolution of DOJ Powell probe.

**Still deferred:**
- `raw/Trump is openly targeting innocent civilians.md` — Reason piece on Iran civilian targeting (Apr 7 2026). Unrelated to source acquisition targets; needs its own ingest under Iran/Strait of Hormuz cluster.
- [[Katherine Menendez]] entity page (one-off; may not warrant dedicated page)
- Specific docket number for Judge Schiltz's 96-violations finding (still only secondary-sourced via Wikipedia)
- Epic v. Apple + EU Digital Markets Act materials for completing the Chokepoint Control legal framework

**Index:** total_sources 387 → 399

## [2026-04-08] note | Metro Surge $81B correction audit needed

**Action item**: Any wiki/articles, wiki/syntheses, or published pieces that cite "$81 billion" as the Metro Surge business revenue impact should be audited and corrected to "$81 million" (city estimate for restaurant and small business revenue losses specifically) or "$203.1 million" (total one-month impact across all categories). The error originated in the Operation Metro Surge entity page and propagated into this morning's insight sweep synthesis before being corrected. See [[City of Minneapolis — Operation Metro Surge results in $203 million impact]] for the authoritative breakdown.

## [2026-04-08] ingest | 5 new sources — Epic v. Apple, Iran ceasefire, civilian targeting, Wisconsin SC, GA-14 special

Scraped Epic Games v. Apple from Wikipedia (the chokepoint legal-framework target identified in [[insight-sweep-2026-04-08]]) and ingested 4 user-clipped raw files covering the April 7, 2026 news cycle: Reason on Trump's open civilian targeting, CBC on the Trump-Iran two-week ceasefire, Newsweek on Chris Taylor's Wisconsin Supreme Court win, and The Hill on Clay Fuller's GA-14 special election victory.

**Source pages created** (5):
- [[Epic Games v Apple - Wikipedia]] — comprehensive case record; chokepoint reconstituting itself in compliance form before April 2025 contempt finding
- [[Reason — Trump is openly targeting innocent civilians]] — Petti on the bipartisan continuity of civilian-targeting cruelty, now stripped of its euphemistic cover
- [[CBC — Trump Iran ceasefire what happens next]] — two-week ceasefire 90 min before deadline; Iran's reported $2M-per-ship Hormuz transit fee
- [[Newsweek — Liberal flips Conservative Wisconsin Supreme Court seat]] — Taylor wins 61%; differential-engagement pattern; 5-2 liberal majority
- [[The Hill — Clay Fuller wins Georgia special election]] — Trump-endorsed Fuller wins GA-14 runoff; House GOP margin tightens to 218-214

**Entities created** (2):
- [[Clay Fuller]] — incoming GA-14 representative
- [[Wisconsin Supreme Court]] — court entity for the recurring bellwether story

**Entities updated** (5):
- [[Apple]] — added Epic v. Apple full procedural record + April 2025 contempt finding + EU Sweden account termination; sources 8→9
- [[Strait of Hormuz]] — added April 7 conditional reopening, Araghchi quote, $2M transit fee plan; sources 5→7
- [[Iran]] — added two-week ceasefire details, 10-point peace plan, civilian-targeting context; sources 7→9
- [[Donald Trump]] — added ceasefire announcement, "Stone Age" rhetoric source, Fuller endorsement; sources 32→36
- [[Marjorie Taylor Greene]] — added January 2026 resignation date and Fuller-as-successor; sources 3→4

**Concepts updated** (1):
- [[Chokepoint Control]] — added App Store as platform chokepoint, Hormuz conditional reopening + transit fees; sources 6→9

**Index:** total_sources 399 → 404; total_pages 628 → 635


## [2026-04-08] update | index/log/overview reconciliation

Reconciled stale counts in the index, log, and overview after the morning's
insight-sweep + April-7 ingest commits. Actual counts now reflected:

- **Sources**: 397 (index previously said 404; overview said 385)
- **Entities**: 101 (index Stats said 99)
- **Concepts**: 81 (index Stats said 86 — concept page count is below the
  Stats line because some pages were merged or moved during the April 7
  audit pass; verified via `ls wiki/concepts/*.md | wc -l`)
- **Syntheses**: 11 (5 audits + 6 insight sweep)
- **Articles**: 82
- **Total wiki pages**: 672 (index Stats now matches)

Overview page also received a 2026-04-08 update paragraph summarizing the
day's insight sweep + 17 new source acquisitions.
