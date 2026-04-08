---
title: "GENIUS Act"
type: concept
tags: [politics, monetary-policy, technology, stablecoin, crypto, legislation]
created: 2026-04-07
updated: 2026-04-07
sources: 18
---

## Glossary — Read This First

The crypto policy debate routinely conflates four distinct concepts. The GENIUS Act sits at the intersection of all four, so precision matters:

- **Currency** — a legal tender concept (who is required to accept it in payment of debts).
- **Money** — an economic function (medium of exchange, unit of account, store of value).
- **Payment instrument** — a settlement rail (checks, ACH, Fedwire, stablecoins).
- **Reserves** — has TWO unrelated meanings: (a) the *backing assets* an issuer holds against its liabilities, and (b) *reserve currency status*, the dollar's role in international invoicing, FX holdings, and safe-asset markets. These are different concepts that share a word.

A payment stablecoin like USDC is **a payment instrument that represents a redemption claim on dollar money issued by Circle.** It is not currency (no legal tender status), it is not money (it is a claim on money), and the "100% reserves" it holds (sense a) have no mechanical relationship to the dollar's "reserve currency" status (sense b). The wiki used to elide these. This page tries not to.

## Definition

The Guiding and Establishing National Innovation for U.S. Stablecoins (GENIUS) Act is the first comprehensive federal regulatory framework for payment stablecoins in the United States. Signed into law by President Trump on July 18, 2025, it establishes a federal-state supervision regime for stablecoin issuers, requires 1:1 reserve backing with liquid assets (U.S. dollars or short-term Treasuries), and excludes the SEC, CFTC, and CFPB from oversight — placing authority with banking regulators (OCC, FDIC, Federal Reserve, NCUA).

## Why It Matters

Stablecoins — dollar-pegged payment instruments — have grown to a market cap of roughly $200–250 billion as of mid-2025 (with daily on-chain transaction volume often quoted at ~$70B, though the provenance of that number is weak — see "Numbers" below). The GENIUS Act's 100% reserve requirement makes regulated stablecoin issuers structural buyers of short-dated U.S. Treasuries, which has triggered claims that the Act will "extend dollar hegemony" into digital finance. That claim is partly true and partly hand-waved; the rewritten "Treasury Demand and Dollar Hegemony" section below tries to bound it honestly.

Critics also charge that the bill is corruption-tainted because the Trump family holds a majority stake in USD1, one of the larger U.S. stablecoins. **That criticism is well-evidenced as a conflict-of-interest claim, but it does not by itself determine whether the underlying legislation is good or bad policy.** See "Decoupling the Trump Conflict from the Legislation's Merits" below.

## Key Provisions

- **1:1 reserve requirement**: Issuers must hold liquid assets (USD, short-term T-bills) equal to outstanding stablecoins.
- **Permitted Payment Stablecoin Issuer (PPSI)**: Three paths — bank subsidiary, OCC-approved nonbank, or state-regulated issuer (under $10B).
- **No interest to holders**: PPSIs may not pay yield on stablecoins.
- **Bankruptcy priority**: Stablecoin holders get first-priority claims over other creditors in insolvency.
- **Big Tech restriction**: Public non-financial companies blocked unless Stablecoin Certification Review Committee unanimously approves — but *private* companies (e.g., Elon Musk's X) face no such restriction.
- **Tether loophole**: Foreign issuers can issue offshore and trade on U.S. decentralized exchanges, even if non-compliant.
- **SEC/CFTC excluded**: Payment stablecoins are explicitly not securities or commodities.
- **Effective date**: November 2026 (18 months post-enactment, or 120 days after final rules).
- **Three-year compliance window** for exchanges/custodians to transition to approved issuers only.

## Democratic Opposition

Senate Banking Committee Democratic staff identified four major flaws in the bill before passage:
1. No prohibition on elected officials (including Trump) profiting from stablecoin ventures.
2. Private Big Tech companies (X, private entities) still allowed to issue stablecoins.
3. The Tether loophole — offshore non-compliant stablecoins can still circulate on U.S. decentralized exchanges.
4. Inadequate consumer protections; CFPB explicitly excluded.

The carve-out of the "USD" acronym from naming restrictions directly benefits Trump's USD1 stablecoin.

## Treasury Demand and Dollar Hegemony — Quantified

The wiki used to assert a clean causal chain: "100% reserves in T-bills → captive Treasury demand → dollar hegemony reinforced." Each arrow has problems that earlier framing skipped.

**1. Float vs. transaction volume.** "$70 billion daily transaction volume" is a *velocity* number, not a *float* number. Reserves only have to back the float. Combined USDT + USDC float is roughly $200–250B in mid-2025; daily turnover doesn't add anything to the reserve pool. The wiki used to quote both numbers as if they were equivalent macro signals. They aren't.

**2. Substitution, not net new demand.** The relevant counterfactual is not "stablecoin Treasury demand vs. zero." It is "stablecoin Treasury demand vs. wherever that dollar would have sat instead." If a user moves $1 from a money-market fund (which already holds ~85% in T-bills) into USDC (which holds T-bills), **net new Treasury demand from that switch is approximately zero**. If they move it from a non-interest-bearing checking deposit, the bank previously held a mix of T-bills, MBS, loans, and reserves at the Fed — so net new T-bill demand is positive but smaller than the headline implies. The honest claim is that stablecoins *reallocate* dollar holdings into bills, not that they create them.

**3. Duration matters.** The Act requires *liquid, short-term* reserves (cash, T-bills ≤93 days, overnight repo). That demand is concentrated at the very front of the Treasury curve. It does not finance 10-year or 30-year issuance — which is where fiscal sustainability lives. "Captive Treasury demand" compresses the entire curve in a way that doesn't match the statute. Stablecoin growth lowers bill yields at the margin and may modestly steepen the curve; it does not lower long-end financing costs.

**4. Scale, bounded.** Against ~$28T in marketable U.S. Treasury debt, current combined stablecoin reserves represent roughly 1%. Even a 10x adoption scenario gets the stablecoin sector to roughly 10% of the *bill* market — meaningful for short-end yields, not transformative for the overall debt stock. "Multi-trillion dollar range" projections are aspirational; they should be presented as scenarios, not facts.

**5. Reserve currency status is not just T-bill demand.** Reserve currency status is driven by: (a) *invoicing share* (what fraction of global trade is denominated in dollars), (b) *FX reserves* held by foreign central banks, (c) *safe-asset depth* (the size and liquidity of the Treasury market), and (d) *settlement network effects* (SWIFT, correspondent banking, CLS). Stablecoin T-bill demand only touches channel (c), and only at the front end. It barely touches (a) and (b), and only marginally affects (d). Conflating "more T-bill buyers" with "more reserve currency status" is the [[Petrodollar System]] page's old sin (see below).

**6. The two-meanings-of-"reserve" trap.** The word "reserve" appears in the legislation in sense (a) — *backing assets*. The hegemony argument requires sense (b) — *international monetary status*. The wiki used to slide between them without acknowledging the jump. Holding T-bills as backing for a private payment instrument has no mechanical connection to the dollar's role in central bank reserves or oil invoicing. There is an *invoicing/settlement* channel by which globally-circulating dollar-pegged stablecoins might reinforce dollar incumbency at the digital-payments margin — that's the strongest version of the hegemony claim — but it operates through habit and rail dominance, not through Treasury demand.

**The strongest defensible claim** the wiki can make: stablecoins push marginal demand into the front of the Treasury curve, and lock a growing share of dollar-denominated digital payments into dollar-denominated collateral, which helps incumbency at the *invoicing/settlement* margin without meaningfully changing U.S. borrowing costs or central bank reserve composition. That is a real but bounded claim. The "digital petrodollar" framing in [[Petrodollar System]] is rhetoric, not mechanism.

See also: [[Narrow Banking and the Chicago Plan]], [[Dollarization via Stablecoins]], [[Stablecoin Legislation]], [[Petrodollar System]].

## Decoupling the Trump Conflict from the Legislation's Merits

The wiki has two separate claims that earlier framings collapsed into one moral story:

- **Claim A (well-evidenced):** The Trump family's stake in USD1 / [[World Liberty Financial]] / the $TRUMP meme coin while signing the GENIUS Act is a textbook presidential conflict of interest, plausibly worth ~$57M+ in unrealized gains. See [[Donald Trump]] for the conflict-specific ledger.
- **Claim B (independent and unproven):** The GENIUS Act is bad legislation *because of* Trump's stake, or the bill's provisions exist *because* of his stake.

These are different claims, and conflating them produces lazy analysis. The intellectually honest version: *the GENIUS Act is a serious-looking first attempt at a stablecoin framework that is tainted, but not invalidated, by the president's personal financial stake in its primary asset class.*

**Critiques that survive even if Trump had zero crypto exposure:**
- The Tether loophole (offshore issuers reachable via DEXs) is a real regulatory gap.
- CFPB exclusion removes consumer-protection authority over a $200B+ payment instrument.
- The bankruptcy priority carveout creates the moral-hazard / implicit-bailout dynamic Adam Levitin warns about.
- CFTC exclusion removes anti-manipulation jurisdiction without creating a replacement.
- The 100% reserve requirement is unprecedented for U.S. financial intermediaries (see [[Narrow Banking and the Chicago Plan]]) and the consequences haven't been thought through.

**Critiques specifically tied to Trump:**
- The "USD" naming carve-out's optics relative to USD1 (the underlying drafting decision is defensible regardless of who happens to own USD1; the optics are not).
- The public-vs-private issuer split's fit with Elon Musk's privately-held X.
- The political economy of which stablecoin operators benefit from which provisions.

The wiki should hold both layers simultaneously. Earlier versions of this page (and [[Donald Trump]]) treated the carveouts as evidence of corruption rather than as defensible policy choices that nonetheless raise conflict-of-interest concerns.

## Tensions & Counterarguments

- **Innovation vs. oversight**: The bill speeds market growth but weakens CFPB/SEC consumer protection levers.
- **Regulatory arbitrage**: Offshore issuers like Tether remain largely unaddressed.
- **Corruption risk**: Trump family's financial stake in USD1 is a direct conflict of interest with the president's regulatory authority over the stablecoin market.
- **STABLE Act differences**: The STABLE Act alternative had stricter state certification and a two-year moratorium on algorithmically-backed stablecoins; the GENIUS Act has neither.

## Related Concepts

- [[CLARITY Act]] — companion crypto market structure legislation passed same week
- [[CBDC]] — what the GENIUS Act does NOT create; Anti-CBDC Act blocks this
- [[Stablecoin Legislation]] — broader regulatory landscape
- [[Narrow Banking and the Chicago Plan]] — the missing analytical frame: 100% reserve issuance is narrow banking by another name
- [[Dollarization via Stablecoins]] — what stablecoins actually do in failing-currency economies; the part the DC framing misses
- [[Petrodollar System]] — analog for how dollar incumbency works at the invoicing layer; the "digital petrodollar" framing is rhetorical, not mechanical
- [[Fed Independence]] — both bills reshape monetary power without involving the Fed

## Vote Counts and Legislative Path

- Senate: 68-30 (June 17, 2025)
- House: 308-122 (July 17, 2025) — strong bipartisan majority
- Signed by President Trump: July 18, 2025
- Effective date: January 18, 2027, or 120 days after final rules (whichever first)
- Digital asset service providers must comply with full issuer restrictions by July 18, 2028

## Stablecoin Certification Review Committee (SCRC)

The GENIUS Act establishes a new governance body: the Stablecoin Certification Review Committee, comprised of the Treasury Secretary (chair), Fed Chair/Vice Chair for Supervision, and FDIC Chair. The SCRC:
- Approves or rejects state regulatory regime certifications (30-day deadline; unanimous vote required)
- Rules on whether public companies (non-financial) can issue stablecoins (unanimous approval required)
- Determines whether foreign issuer regimes are "comparable" to U.S. standards (Treasury leads)

## Bailout Risk

Georgetown law professor Adam Levitin argues the GENIUS Act's bankruptcy priority reform sets up a future government bailout: stablecoin holders get priority over administrative creditors (lawyers, professionals) in bankruptcy, but lawyers won't work without guaranteed payment. A broken stablecoin peg leaves holders at risk, and the implied government backing creates moral hazard. TerraUSD's 2022 collapse ($40B+ wiped out) is the precedent. [[GENIUS Act Impact on Stablecoins and Taxpayers — Bankrate]]

## Fed Account Access Gap

The GENIUS Act does not address whether Permitted Payment Stablecoin Issuers will have access to Federal Reserve accounts — a significant operational gap for efficient dollar settlement. [[GENIUS Act Framework — Sidley Austin]]

## Executive Foundation

The GENIUS Act codifies the policy direction established by Trump's January 23, 2025 Executive Order "Strengthening American Leadership in Digital Financial Technology," which: (1) revoked Biden's EO 14067; (2) prohibited CBDC development; (3) directed a 180-day regulatory framework report. The GENIUS Act is the legislative follow-through to that EO. [[Trump EO on Digital Financial Technology — White House]]

## Key Sources

- [[GENIUS Act Passes in US Congress — Morgan Lewis Breakdown]]
- [[GENIUS Act Establishes 100% Reserve Backing for Stablecoins]]
- [[Banking Committee Democratic Staff Analysis on Latest GENIUS Act Draft]]
- [[Bitcoin soars past $120,000 ahead of Crypto Week]]
- [[GENIUS Act Comprehensive Framework — Goodwin Law]]
- [[GENIUS Act Framework — Sidley Austin]]
- [[GENIUS Act New Era of Stablecoin Regulation — Gibson Dunn]]
- [[GENIUS Act Federal Framework for Stablecoin Issuers — Pillsbury]]
- [[GENIUS Act Impact on Stablecoins and Taxpayers — Bankrate]]
- [[Trump EO on Digital Financial Technology — White House]]
- [[House Announces Crypto Week July 14 — Financial Services Committee]]
- [[Securities Enforcement Roundup April 2025 — Morgan Lewis]]
- [[Trump GENIUS Move — Trump Urges GOP to Vote Yes for Stablecoin Bill]] — Trump's Truth Social posts during Crypto Week; personally met with 11 of 12 needed House holdouts; "ALL REPUBLICANS SHOULD VOTE YES"; July 16, two days before signing
- [[State of Crypto — Government Shutdown Nears a Record]] — shutdown's downstream effect on CLARITY Act Senate timeline; Oct 20 markup missed; context for what came after GENIUS Act signing
