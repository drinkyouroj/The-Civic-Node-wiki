---
title: "Economist Audit — Causal Chains, Numbers, and Framing (2026-04-07)"
type: synthesis
tags: [audit, economics, monetary-policy, methodology]
created: 2026-04-07
updated: 2026-04-07
sources: 0
query: "Audit the wiki's economic claims for causal integrity, numbers, conflated concepts, counterargument coverage, and the Hayek/Schelling framing."
---

## Answer

The wiki is in strong shape as a journalistic-synthesis brief; it is not yet in shape as an economics brief. Most headline numbers trace back to real primary sources, but several flagship causal claims are assertions of mechanism without a quantified mechanism — and a handful of central economic concepts are conflated in ways that will embarrass the newsletter if picked up by a sharp reader. The Hayek/Schelling "theoretical spine" the overview claims exists is mostly editorial hindsight; the underlying source base is dominated by legal/journalistic coverage, not game theory.

Top-line: six P0 findings, ten P1 findings, plus corrections. Fix the P0s before publishing anything that leans on Fed independence, GENIUS/T-bill demand, or tariff arithmetic as a load-bearing claim.

---

## Supporting Evidence

### 1. Causal chain integrity

#### P0-1. "GENIUS Act creates captive Treasury demand → reinforces dollar hegemony"

Found in [[GENIUS Act]] (lines 14–16, 40–42), [[Stablecoin Legislation]] (line 16, 38–40), [[Petrodollar System]] (lines 35–37).

This is the wiki's single most macroeconomic claim and it is **entirely hand-waved**. The mechanism described is:

1. Stablecoins must hold 100% reserves in cash/T-bills.
2. Therefore stablecoin issuers will buy Treasuries.
3. Therefore Treasury demand rises.
4. Therefore dollar hegemony is reinforced.

Each arrow has problems the wiki doesn't engage with:

- **Substitution is not addressed.** If a user moves $1 from a bank money-market fund (which already holds T-bills) into USDC (which holds T-bills), net Treasury demand is zero. The relevant counterfactual is not "stablecoin demand vs. nothing" but "stablecoin demand vs. the MMF, checking deposit, or short-duration bond fund the dollar would otherwise sit in." The wiki never states this.
- **Duration matters.** The GENIUS Act requires *liquid, short-term* reserves. That moves demand into the very front of the Treasury curve (bills, ≤93 days). It does not finance 10Y or 30Y issuance, which is where fiscal sustainability pressure lives. "Captive Treasury demand" compresses the entire curve as if bills and bonds were interchangeable. They are not.
- **Scale is asserted, not bounded.** The wiki repeats "$70B daily transaction volume" and "multi-trillion dollar range," but transaction volume is not reserves. USDC float is ~$60B; USDT is ~$120B; combined stablecoin market cap is ~$200–250B in mid-2025. Against $28T in Treasury marketable debt, current stablecoin reserves are ~1%. Even a 10x adoption scenario gets you to the rough order of ~10% of the bill market, not "dollar hegemony extension."
- **Hegemony and Treasury demand are not the same variable.** Reserve currency status is driven by (a) invoicing share, (b) FX reserves held by central banks, (c) depth of safe-asset markets, and (d) network effects in settlement. Stablecoin T-bill demand affects only (c), and only at the front end. The "petrodollar successor" framing in [[Petrodollar System]] elides all of this.

**Fix:** Add a "Quantification" subsection to [[GENIUS Act]] distinguishing (a) float vs. transaction volume, (b) bills vs. bonds, (c) substitution vs. net new demand, and (d) the invoicing/reserves channel vs. the financing-demand channel. The strongest form of the claim the wiki should make is something like: "Stablecoins push marginal demand into the T-bill curve and lock a growing share of dollar-denominated digital payments into dollar-denominated collateral — which helps incumbency at the invoicing/settlement margin without meaningfully changing U.S. borrowing costs."

Counterargument the wiki should name but doesn't: Matt Levine's point that the GENIUS Act is, in a real sense, **narrow banking by another name** — it is forcing issuers to do exactly what Admati/Kotlikoff/Cochrane proposed for narrow banking reform (100% reserves, no lending against deposits). That is a bigger and more interesting angle than "digital petrodollar."

#### P0-2. "Trump tariffs raised effective rate to 20.6%, highest since 1910, prevented Fed cuts"

Found in [[Tariff-Driven Inflation]] (lines 16, 29), [[Donald Trump]] (line 59), overview line 40.

The number traces correctly to Yale Budget Lab ([[State of U.S. Tariffs July 14, 2025]]). But the wiki repeats the pre-substitution number everywhere and omits the distinction. The Yale source explicitly says:

- **Pre-substitution: 20.6%, highest since 1910.**
- **Post-substitution: 19.7%, highest since 1933.**

The post-substitution number is what actually shows up in the economy once firms and consumers reroute. Both are headline-worthy, but they are not the same number. The wiki quietly picks the bigger one and the older comparison year (1910 sounds scarier than 1933). That's a selection bias that a Brookings or Cato reader will flag immediately. Also: "highest since 1910" is not *quite* right — the true comparison is "highest since the decade *before* Smoot-Hawley" — the peak of the 1930 tariff regime was actually higher than 20.6%, and Yale's own framing is "highest since 1933" because that is where the post-substitution number lands.

**Causal chain issue:** The claim "prevented Fed cuts" is asserted from Powell's own language, which is fine, but the wiki does not engage with the identification problem: the Fed held rates because of tariff-*expected* inflation, not yet-realized tariff inflation. Core PCE has not actually moved up commensurate with a 20.6% effective rate increase because passthrough is running "somewhat lower than in 2019" ([[Tariff-Driven Inflation]] line 52, citing Goldman). If passthrough is low, the Fed's hold is partly an *expectations* story, not a mechanical tariff-inflation story. The wiki's language conflates these.

**Fix:** Clarify pre/post-substitution everywhere the 20.6% figure appears. Say "highest since 1933" for the realized number and "highest since 1910" only when using the pre-substitution version. Add a sentence distinguishing tariff-passthrough (small, so far) from tariff-expectations (the actual transmission channel to Powell's decision).

#### P1-1. "Dynamic pricing AI enables tacit collusion"

[[Dynamic Pricing AI]] lines 14, 21–22. Sourced to [[AI-Driven Personalized Pricing May Not Help Consumers]], which is a CMU press release summarizing Qiu, Huang, Singh, Srinivasan (Marketing Science, 2025). That paper is a **simulation study with reinforcement-learning agents in a constructed environment**, not an observation of real-world collusion. This is a well-known finding in the Calvano/Calzolari/Denicolò/Pastorello 2020 AER literature — the wiki doesn't cite that earlier and more authoritative work.

The claim is real, but the wiki presents a simulation as if it were empirical evidence. That is the difference between "algorithms can tacitly collude in toy models" (which is established) and "algorithms *are* tacitly colluding in Delta's pricing" (which is not).

The Delta/Fetcherr bullet (line 24) is interesting but also hand-waved — "industry acknowledges regulatory scrutiny risk" is not the same as evidence of supracompetitive pricing. There is no price-level comparison to pre-AI benchmarks.

**Fix:** Cite Calvano et al. (2020, AER). Distinguish simulation evidence from empirical evidence. Note that the RealPage algorithmic rent-setting DOJ case is the best live example of algorithmic collusion — and is strangely not in this concept page at all, though "rent optimization" is mentioned in passing (line 30).

#### P1-2. "El Salvador Bitcoin experiment failed by its own metrics"

[[El Salvador Bitcoin Experiment]] is actually the strongest-argued page in this cluster. The 92% non-use figure traces cleanly to the DPL News survey and the Digital Watch Observatory coverage. The Chicago paper is cited. The IMF loan condition is documented.

The tension the wiki identifies itself (line 70+) is the right one: **as a currency experiment it failed; as a speculative sovereign allocation it succeeded.** Those are two different policy questions. My only note is that the page would benefit from saying this more pointedly: the Bitcoin-as-currency thesis and the Bitcoin-as-reserve-asset thesis require completely different empirical tests, and the wiki implicitly holds El Salvador to the first while [[Strategic Bitcoin Reserve]] evaluates the U.S. on the second. This is a subtle but important framing distinction.

No fix needed for the data, but clarify the evaluative criterion up front.

#### P1-3. "Tether loophole means offshore non-compliant stablecoins still circulate"

[[GENIUS Act]] line 25, [[Stablecoin Legislation]] line 35, overview line 27. The claim is correct as a matter of statutory reading: the GENIUS Act restricts what can be *issued* in the U.S. but does not force decentralized exchanges to delist non-compliant tokens. However:

- The wiki never addresses that the three-year compliance window ([[GENIUS Act]] line 28) actually does force custodians and centralized exchanges to delist non-PPSI stablecoins. That's a significant constraint on Tether's U.S. on-ramps.
- The "DEX circulation" claim is not quantified. How much Tether volume actually runs through U.S.-person-accessible DEXs? Without that number, the "loophole" claim is qualitative rather than mechanical.
- The page does not engage with the Treasury's actual enforcement tools against Tether (OFAC, FinCEN actions, 2023 DOJ settlement discussions).

**Fix:** Quantify U.S. DEX-routed Tether volume or acknowledge the gap. Distinguish the CEX/custodian compliance window (binding) from the DEX residual (unquantified).

### 2. Numbers integrity

- **$70B stablecoin daily volume** — traces to a Morgan Lewis lawyer memo characterization ("some estimates ranging as high as"), which itself does not cite a primary source. This is a secondary characterization of a tertiary estimate. It is roughly in the ballpark of Visa onchain stablecoin dashboard data, but the wiki should acknowledge the provenance weakness and (ideally) cite the Visa/ARIS analytics dashboard directly. **P1.**

- **$250B stablecoin market** — appears once in [[Trump GENIUS Move]] source page (line 23). Consistent with mid-2025 DeFi Llama / CoinGecko aggregate market cap. No concern. But the wiki conflates "market cap" (~$250B) and "daily volume" ($70B) as if they were different windows on the same thing. They're not — volume/market cap is a velocity statistic, and the wiki doesn't distinguish them. **P2.**

- **20.6% tariff rate** — see P0-2 above. Correct at the pre-substitution number, misleadingly paired with "highest since 1910" throughout. **P0.**

- **~$57M Trump WLF gain** — traces to [[Congress Advances Crypto Bills — StratNews Global]] and [[What is Crypto Week — Al Jazeera]]. Both are wire/journalistic sources citing unspecified estimates. No primary documentation (filings, trust disclosures) is offered. The number is plausible given the WLF $550M raise and 75% net revenue share claim, but the wiki treats it as hard while it's actually derived. Also: [[Donald Trump]] contains **two duplicated "Crypto Conflicts of Interest" sections** (lines 32–42 and 62–70) with slightly different numbers and framing — needs deduplication. **P1.**

- **92% El Salvador non-use** — traces cleanly to DPL News survey and Digital Watch Observatory secondary coverage. Survey n, methodology, and date are not reported in the wiki source summary. Verify the underlying survey methodology before publishing — this is the kind of number where a reader will ask "92% according to whom?" **P1.**

- **$22,620 US data worker median** — traces correctly to the AWU-CWA/TechEquity report ($15/hr × 29 hr/wk × 52 weeks = $22,620). Arithmetic checks out, methodology is the survey's own (self-reported). Note: the [[Mechanical Turk Pattern]] page at line 42 says "$15/hr median" and the page at line 75 says "$22,620/year" — these are consistent, but different summaries pick different framings. Minor but worth unifying. **P2.**

- **1-billion-dosage ADHD deficit** — traces to DEA-commissioned report per [[Frontiers — ADHD Medication Shortage]]. The underlying methodology is not reproduced in the wiki. This is a Frontiers paper's characterization of a DEA report; not ideal provenance, but not wrong. The number is not independently verifiable from the wiki's current source base. **P2.**

- **$3.1B vs $2.5B Fed construction cost** ([[Fed Independence]] line 28) — a $600M spread between Trump's claim and the Fed's number is real per AP reporting, but the wiki does not flag that this is a *dispute* rather than a fact. **P2.**

### 3. Conflated concepts

#### P0-3. Currency vs. money vs. payment instrument

[[GENIUS Act]], [[Stablecoin Legislation]], [[El Salvador Bitcoin Experiment]], and [[Petrodollar System]] all use "currency," "money," and "payment instrument" as if they were the same thing. They are not.

- **Currency** is a legal tender concept (who has to accept it).
- **Money** is an economic function (medium of exchange, unit of account, store of value).
- **Payment instrument** is a settlement rail (checks, ACH, stablecoins, Fedwire).

Stablecoins are a payment instrument that represents a claim on U.S. dollar money. They are not currency (legal tender), and they are not themselves money — they are redemption claims on money. This matters because the wiki's "digital petrodollar" claim requires stablecoins to generate structural *dollar* demand, but stablecoin users never stop holding dollars — they just change the form of the claim. The sophistication of the mechanism is exactly at the conflation point.

Similarly, El Salvador's "legal tender" status for Bitcoin was a **currency** policy (mandatory acceptance), not a **money** policy (Bitcoin still couldn't perform the money functions because of volatility). The wiki sometimes treats the legal tender removal as a failure of Bitcoin-as-money, which confuses the two.

**Fix:** Add a one-paragraph glossary at the top of [[GENIUS Act]] and [[El Salvador Bitcoin Experiment]] distinguishing these three. Then audit the text for which concept each sentence actually uses.

#### P0-4. "Reserve" (backing) vs. "reserve" (currency status)

In [[GENIUS Act]] and [[Petrodollar System]] the word "reserve" does double duty:

- "100% reserve requirement" — meaning the issuer's *backing assets*.
- "Reserve currency status" — meaning the dollar's role in *international monetary arrangements*.

These are wildly different concepts, and the wiki's "digital petrodollar" thesis literally depends on eliding them: "100% reserves → reserve currency status → dollar hegemony." But having reserves *for a stablecoin* has no mechanical connection to having *reserve currency status in the international system*. The argument slides from one meaning to the other without acknowledging the jump. **P0.**

#### P1-4. Security vs. commodity

[[GENIUS Act]] line 27 says "payment stablecoins are explicitly not securities or commodities." This is correct as statutory text but the page never explains *why it matters* — namely, that this removes CFTC anti-manipulation jurisdiction from a $250B market entirely, with no replacement fraud/manipulation authority. That's a significant gap worth flagging. **P1.**

#### P1-5. Monopoly vs. monopsony vs. tacit oligopoly

[[Platform Antitrust]] and [[Dynamic Pricing AI]] use "monopoly" loosely. Amazon's Just Walk Out relationship with India labor is a **monopsony** (one buyer of many sellers of labor). Algorithmic price coordination is **tacit oligopoly**. The Microsoft-OpenAI exclusivity is **vertical foreclosure**. These are different antitrust theories with different legal standards. The wiki uses "antitrust" as a catch-all. **P1.**

#### P1-6. Inflation vs. relative price change

[[Tariff-Driven Inflation]] does the best job in the wiki of distinguishing supply-shock (one-time level shift) from sustained inflation (ongoing growth rate change) — see lines 54 and 56, and the M2 reference. This is one place the wiki gets it right. The concern is that [[War-Driven Inflation]] and [[Stagflation]] are inheriting "Tariff-Driven Inflation" as a template without re-running the same careful distinction. I did not fully read those, but recommend an audit pass. **P2.**

### 4. Counterargument absence

For the load-bearing claims, here are the strongest steelmen an honest critic would make, and whether the wiki engages them:

- **GENIUS Act / Treasury demand:** Strongest counter is the narrow-banking / substitution argument (see P0-1). **Not represented.**
- **Tariff inflation trapping Fed:** Strongest counter is that the Fed's hold is actually driven by uncertainty about passthrough, not realized inflation, and Powell's public language is a communication device rather than a causal statement. **Partially represented** via the Goldman passthrough bullet, not named as the core counter.
- **Trump Fed pressure / independence capture:** Strongest counter is Rogoff's observation that "Fed independence" is partly a myth — the Fed has always been politically responsive, and a Trump-era correction to a post-2008 overshoot of discretionary authority is defensible on democratic-accountability grounds. The Kevin Warsh view. **Not represented.** The "Arthur Burns revisionism" bullet gestures at this but doesn't bring it home.
- **El Salvador failure:** Best counter is that El Salvador is sui generis (90% dollarized already, tiny remittance-heavy economy, political economy under Bukele is not replicable) and does not generalize to any other Bitcoin adoption question. **Represented implicitly** but not named.
- **Mechanical Turk Pattern:** The ATM/Bessen counter-narrative *is* represented (line 46+). Good work.
- **Dynamic pricing tacit collusion:** Best counter is that observed dispersion in airline ticket prices pre-dates AI by decades (Stigler-Varian framework; airline yield management since the 1980s); AI is a continuation of a trend, not a regime change, and the consumer welfare effects are theoretically ambiguous. **Partially represented** (line 28) but weak.
- **Dynasty via Schneider/Macdonald:** Best counter is the Super Bowl winner's curse — reversion to mean across NFL champions is powerful, and scheme advantages are exactly the kind of thing that attenuate as opponents have an offseason of film. **Represented** (Defensive Scheme Architecture line 39). Good.

Broadly: the wiki is better at steelmanning on the non-economics clusters than on the economics clusters. The reason is probably that economic counterarguments are the kind of critique a professor would make, and the source base is mostly journalistic, lawyerly, or advocacy-adjacent.

### 5. The Hayek / Schelling framing

The overview claims (line 136): "The wiki's emerging theoretical spine is more game-theoretic than economic."

This is half-true and half-imposed. Let's take it seriously.

**The case that it's true:** [[Focal Point Coordination]] is a real page with real content, and it does make a Schelling argument that connects across domains (NFL pre-snap ambiguity as reverse focal point, DeFi cooperative equilibria, crypto adoption as coordination problem). [[Chokepoint Control]] (not read in this audit but referenced heavily) is a Schelling-adjacent concept. The "concealment as operating mode" pattern in the overview is about information asymmetry, which is game-theoretic.

**The case that it's imposed hindsight:**
- The actual source base is overwhelmingly journalistic (The Atlantic, AP, wire copy) and legal (Morgan Lewis, Gibson Dunn memos). Neither genre is game-theoretic.
- [[The Strategy of Conflict — Thomas Schelling]] is listed as a foundational text, but it only powers two concept pages ([[Focal Point Coordination]] and, implicitly, [[Coercive Diplomacy]]).
- [[The Use of Knowledge in Society — Hayek]] is listed but I find no concept page that *applies* Hayek's dispersed-knowledge argument. The closest is [[DePIN]] which would be the obvious place, but I didn't see Hayek cited there. The foundational text is in the shelf, not in the synthesis.
- Most of the wiki's explanatory heavy lifting is done by *structural/institutionalist* concepts (regulatory weaponization, chokepoint control, organizational continuity), not game-theoretic ones.
- Hayek and Schelling are, in fact, load-bearing in *very different* directions. Hayek is an epistemic argument against central planning. Schelling is an analytical framework for strategic interaction under asymmetric information. The overview flattens them together into "game theory-ish."

**Verdict:** The wiki has *gestures toward* game theory but its actual theoretical spine is institutionalist — "who controls the chokepoint, and how is that control enforced or evaded." That's closer to North/Ostrom/Acemoglu than to Schelling. The overview should either (a) claim institutionalism as the spine, which is what the evidence supports, or (b) commit to actually developing the Schelling and Hayek arguments across more concept pages.

The sentence "more game-theoretic than economic" is also philosophically confused — game theory *is* economics. The distinction the overview is reaching for is probably "more strategic-interaction than macro-accounting," which is a fine thing to say but should be said precisely.

---

## Prioritized Findings

**P0 (fix before publishing load-bearing pieces):**
1. Quantify the GENIUS → Treasury demand mechanism (substitution, duration, scale). Current framing is a mechanism without a mechanism.
2. Clarify pre- vs. post-substitution tariff rates; drop "highest since 1910" when using the post number.
3. Add a currency/money/payment-instrument glossary and audit the stablecoin and El Salvador pages for which concept each sentence uses.
4. Stop eliding "reserve" (backing) with "reserve" (currency status). The "digital petrodollar" thesis depends on this conflation.
5. Name the narrow-banking steelman for GENIUS and the data-dependence steelman for the Fed-tariff causal chain.
6. Deduplicate [[Donald Trump]]'s two "Crypto Conflicts of Interest" sections (lines 32–42 and 62–70).

**P1:**
1. Provenance the $70B/day number or weaken the claim.
2. Distinguish stablecoin float from stablecoin transaction volume everywhere.
3. Cite Calvano et al. (2020, AER) on algorithmic collusion; distinguish simulation from empirical evidence in [[Dynamic Pricing AI]].
4. Add the RealPage DOJ case to [[Dynamic Pricing AI]] — it's the best live example and is missing.
5. Verify the El Salvador 92% survey methodology; note n and date in the source page.
6. Quantify the Tether DEX "loophole" or acknowledge it's qualitative.
7. Explain why CFTC exclusion from stablecoin oversight matters (anti-manipulation gap).
8. Disambiguate monopoly/monopsony/tacit-oligopoly in [[Platform Antitrust]] and [[Dynamic Pricing AI]].
9. Name the Rogoff / Kevin-Warsh steelman against Fed-independence-as-default-good.
10. Reconcile the government shutdown length (overview says 43 days; [[Donald Trump]] line 88 says "36+ days").

**P2:**
1. Note the $3.1B/$2.5B Fed building dispute explicitly as disputed.
2. Unify "$15/hr" and "$22,620/year" framings for US data workers.
3. Audit [[War-Driven Inflation]] and [[Stagflation]] for supply-shock vs. inflation discipline (inherits from Tariff-Driven Inflation).
4. Resolve the Hayek/Schelling framing in the overview — either commit to developing it or rewrite as institutionalism.

---

## Caveats & Gaps

- I did not read every concept page — notable omissions are [[Chokepoint Control]], [[Stagflation]], [[War-Driven Inflation]], [[Nixon Shock]], and most of the AI/tech cluster. Findings may extend to those.
- I did not verify the underlying surveys/papers against their originals; I verified claim-to-source linkage within the wiki.
- The "narrow banking" steelman is the most important thing this audit adds. If nothing else lands from this report, land that.

## Newsletter Application

The most publishable angle that emerged from this audit: **"The GENIUS Act is narrow banking in drag."** The left and the right both miss this because they're fighting the Trump-conflict-of-interest story. The actual structural story is that the U.S. just mandated a new banking framework — 100% reserves, no lending against deposits, first-priority in bankruptcy — that the post-2008 reform movement spent fifteen years failing to get through Congress for actual banks. It arrived as crypto legislation because crypto is where the political coalition exists. That piece writes itself.

Second-best angle: **"Tariffs are a commitment device, not a tax."** The Powell "hold because of tariffs" framing only makes sense if you read tariffs as Trump's signaling to expectations, and the Fed as responding to the expectations channel rather than the price channel. That's a Schelling-flavored story (commitment, compellence), which is the kind of synthesis the wiki *could* support if the Schelling framing were actually developed.

## Follow-up Questions

- What is the empirical passthrough rate of 2025 tariffs to CPI/PCE by category, as of the most recent data?
- What is the Visa/ARIS onchain stablecoin transaction volume, real rather than washed?
- Is there a primary source (SEC filing, trust disclosure) for the $57M WLF number?
- What fraction of Tether volume is reachable by U.S. persons via permissionless DEXs?
- Does the wiki have a concept page on regulatory arbitrage? If not, GENIUS Act / Tether loophole / Big Tech private-vs-public split all point at one.
