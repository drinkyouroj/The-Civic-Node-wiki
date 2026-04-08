---
title: "Free Banking and Wildcat Banking"
type: concept
tags: [monetary-policy, history, finance, stablecoin, crypto]
created: 2026-04-07
updated: 2026-04-07
sources: 5
---

## Definition

The **Free Banking Era** is the period in U.S. monetary history from roughly 1837 to 1863 during which states (rather than the federal government) chartered banks and authorized those banks to issue their own paper notes redeemable in specie (gold or silver). There was no federal currency. A traveler in 1850 might carry a wallet of notes from a dozen different state-chartered banks, each circulating at a *discount to par* that varied with the issuer's reputation, the geographic distance from the issuing bank, and the perceived credibility of its specie reserves. Specialized publications — *Bicknell's Counterfeit Detector*, *Thompson's Bank Note Reporter* — published quoted discount rates the way newspapers later quoted exchange rates.

**"Wildcat banking"** is the pejorative subset: banks chartered in remote locations (where it was hard to bring notes for redemption), capitalized with shaky securities, and known for note issuance disproportionate to actual specie holdings. The legend held that such banks deliberately located their physical offices in places "where only wildcats lived" to deter redemption. The legend is partly accurate and partly anti-banking propaganda. Hugh Rockoff's quantitative work in the 1970s and Arthur Rolnick and Warren Weber's research at the Minneapolis Fed showed that wildcat banking was significantly less common than the caricature suggested — the era's failures were more often caused by exogenous shocks (collateral price collapses) than by deliberate fraud — and that several state systems actually performed reasonably well.

The era ended with the **National Banking Acts of 1863–64**, which created federally chartered banks, taxed state bank notes out of existence (the 10% tax of 1865 effectively eliminated them), and centralized U.S. currency issuance under federal authority for the first time outside of wartime emergencies. The Federal Reserve, created in 1913, completed the centralization.

## Why It Matters for the Newsletter

The contemporary stablecoin landscape — [[Tether]] (USDT), [[Circle]] (USDC), USD1, FDUSD, USDe, DAI, the long tail — is a recognizable modern recapitulation of free banking. The structural features map almost cleanly:

| Free Banking (1837–63) | Stablecoin Era (2018–present) |
|---|---|
| State-chartered private note issuers | Private stablecoin issuers, sometimes state-chartered |
| Notes redeemable for specie at issuer | Stablecoins redeemable for USD at issuer |
| Notes circulate at discount based on perceived issuer credibility | Stablecoins occasionally trade at discount during reserve panics (USDC March 2023, UST collapse 2022) |
| Counterfeit detector publications publishing quoted discounts | Stablecoin reserve attestations, peg dashboards, on-chain monitoring |
| Geographic / informational distance increases discount | Cross-chain bridges, jurisdictional uncertainty increase risk premium |
| The Suffolk System: a private New England clearing arrangement that maintained par redemption regionally | Modern private clearing/redemption arrangements among large stablecoin holders |
| 1863 National Banking Acts: federal centralization, state notes taxed out of existence | 2025 GENIUS Act: federal framework, ?eventual displacement of non-compliant issuers |

The wiki's [[GENIUS Act]] page calls the Tether residual a "loophole" — but in 1855 a contemporary critic would have called Suffolk-System-clearing a "loophole" too. The "loophole" is the discount-note dynamic that the post-1863 federal system tried to eliminate. Whether stablecoins recapitulate that elimination, or whether they preserve a permanently distributed issuance landscape, is one of the most interesting open questions in monetary history.

## Newsletter Angle

The historian audit flagged this as a missing analytical lens: **the wiki discusses Tether/USDC/USD1 as if private dollar issuance were historically novel, when the U.S. had nearly thirty years of it.** A newsletter piece comparing 1840s state-bank-note discount tables to 2022–25 stablecoin peg deviations — a Hugh Rockoff–style quantitative exercise — would be genuinely original work. Nobody in the current stablecoin commentariat is drawing this parallel cleanly.

The deeper newsletter angle: the 1863 National Banking Acts were the federal response to the free banking era. The 2025 [[GENIUS Act]] is plausibly the analogous federal response to the stablecoin era. What that analogy implies depends on whether you read 1863 as a *necessary* centralization (the conventional Banking School / progressive view) or as a *destructive* one (the Free Banking School view that argues the era's reputation was worse than its performance). The wiki should hold both readings.

## What the Historical Record Actually Shows

- **Failure rates were uneven.** Some state systems (New York, Massachusetts, Indiana, Louisiana) had relatively low failure rates and well-functioning private note redemption. Others (Michigan, Wisconsin in particular periods) had genuinely high failure rates and bank notes circulating at deep discounts.
- **The Suffolk System (1818–1858)** was a private arrangement among Boston banks that effectively maintained par redemption for New England state-bank notes. It functioned as a distributed clearing house decades before the federal Clearing House Interbank Payments System. It is the closest historical precedent for something like the Lightning Network or modern stablecoin clearing.
- **Rockoff (1974, 1975)** showed that the median wildcat-bank loss to noteholders was much smaller than the popular legend implied. Most failures returned 60-80% to noteholders rather than zero. The "free banking was a disaster" narrative is overstated.
- **The era ended for political reasons as much as economic ones.** The Civil War created federal financing pressure. The National Banking Acts were partly designed to create captive demand for federal Treasury debt (national banks were required to hold Treasuries as backing for their notes — a 19th-century version of GENIUS Act 100%-reserve framing). The 10% tax on state notes (1865) was the explicit kill switch.

## Tensions & Counterarguments

- **The parallel can be overdrawn.** Stablecoins differ from state bank notes in several important ways: redemption is technically instantaneous via blockchain (vs. weeks of physical travel), reserve attestation is more transparent (in some cases), and the unit of account (USD) is already established and stable. Contemporary stablecoin discounts during stress events have been smaller and shorter-lived than 1840s state-note discounts.
- **The 1863 centralization was about war finance, not consumer protection.** The GENIUS Act framing as "federal response to a private issuer landscape" is structurally similar but the political driver is different. Beware of historical-analogy reasoning that imports the 1863 motivation onto 2025.
- **Free banking apologists overstate.** The Rockoff and Rolnick-Weber revisionism is real, but the era did have genuine failures and genuine consumer harm. The current revisionist consensus is "free banking was not as bad as the caricature," not "free banking was good."

## Related Concepts

- [[GENIUS Act]] — the plausible 2025 analog to the 1863 National Banking Acts
- [[Stablecoin Legislation]] — broader landscape
- [[Tether]], [[Circle]] — the contemporary issuers most closely matching the state-bank-note pattern
- [[Dollarization via Stablecoins]] — the dollarized-economy use case has its own free-banking-era parallels (the U.S. silver discount trades of the 1840s, the eurodollar parallels)
- [[Narrow Banking and the Chicago Plan]] — the policy framework that GENIUS imposes; structurally a different solution to the same problem the 1863 Acts addressed

## Key Sources

*(Pending ingest. Foundational secondary sources: Hugh Rockoff (1974, "The Free Banking Era: A Reexamination"), Arthur Rolnick and Warren Weber (1983, "New Evidence on the Free Banking Era"), Bray Hammond (1957, *Banks and Politics in America*), Richard Sylla on the National Banking Acts, the *Bicknell's* and *Thompson's* counterfeit-detector publications themselves as primary sources, Charles Calomiris and Larry Schweikart on regional comparisons.)*

## Open Questions

- Has anyone done a quantitative comparison of 1840s state-bank-note discount distributions vs. modern stablecoin peg deviations? This is a publishable empirical project.
- The Suffolk System maintained private clearing without federal backing for 40 years. What does its eventual collapse (1858) suggest about the durability of private stablecoin clearing arrangements?
- Were the wildcat bank failures of the era driven primarily by deliberate fraud, exogenous collateral shocks, or regulatory failure? The Rockoff/Rolnick-Weber consensus leans toward shocks and regulatory failure; how does that update the "Tether is a fraud" priors that dominate one side of the current debate?
- The 1863 National Banking Acts created federal demand for Treasury backing of national bank notes — the structural ancestor of the GENIUS Act 100%-reserve provision. Has any historian drawn this lineage explicitly?
