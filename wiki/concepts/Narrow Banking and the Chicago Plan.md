---
title: "Narrow Banking and the Chicago Plan"
type: concept
tags: [monetary-policy, finance, history, stablecoin, legislation]
created: 2026-04-07
updated: 2026-04-07
sources: 5
---

## Definition

**Narrow banking** is a class of monetary-system proposals in which deposit-taking institutions are required to hold 100% reserves against their demand liabilities — typically in the form of central bank reserves or short-dated government securities — and are prohibited from lending against those deposits. Lending and maturity transformation are confined to other, non-deposit institutions that fund themselves with longer-term liabilities. The structural goal is to insulate the payment system from credit risk: the unit of account never depends on the solvency of the credit-extending entity, because they are different entities.

The **Chicago Plan** is the canonical 1933 articulation of narrow banking, drafted by economists at the University of Chicago — Henry Simons, Frank Knight, Jacob Viner, Henry Schultz, and others — in response to the cascading bank failures of 1930–33. Irving Fisher (Yale) developed and popularized it in *100% Money* (1935). The plan would have required commercial banks to back 100% of demand deposits with central bank reserves, eliminating fractional reserve banking for the payment-instrument layer of the financial system.

## Why It Matters for the Newsletter

**The single most underwritten frame in the 2025 stablecoin debate is that the [[GENIUS Act]] is narrow banking by another name.** The 100% reserve requirement, the prohibition on paying interest to holders, the bankruptcy priority for stablecoin holders over other creditors, and the institutional separation from credit extension all map almost exactly onto the Chicago Plan / Fisher / Kotlikoff / Cochrane proposals that the post-2008 reform movement spent fifteen years failing to get through Congress for actual banks. It arrived as crypto legislation because crypto is where the political coalition exists.

This framing reframes the entire stablecoin debate:

- **It's not "innovation vs. consumer protection."** It's a 90-year-old policy question (do you want a payment system insulated from bank credit risk?) being answered for digital dollar instruments while still being open for analog dollar instruments.
- **It's not "captive Treasury demand → dollar hegemony."** That framing imports macro consequences the narrow-banking literature doesn't actually claim. The Chicago Plan was a *banking-stability* proposal, not a hegemony proposal.
- **It's not "regulatory weakness."** A 100% reserve requirement is the most stringent backing rule in U.S. financial regulation. It's stricter than what banks face. Critics calling GENIUS "weak" are using "weak" to mean "lacks CFPB jurisdiction" — which is a different complaint.
- **It does have real downsides** the literature has been arguing about for 90 years (see Tensions below).

The newsletter angle the contrarian audit ranked highest: **"The 100% Reserve Stablecoin Is Chicago Plan Narrow Banking and Nobody Is Saying So."** The DC consensus is fighting the Trump conflict-of-interest story; the crypto-Twitter consensus is fighting the regulatory-capture story; neither is engaging with the structural fact that Congress has just enacted, for one slice of the dollar payment system, the policy framework that Friedman, Tobin, Kotlikoff, Cochrane, and Levitin have been arguing for since 1933.

## Brief History

- **1933 — Original Chicago Plan.** Drafted in March 1933 by Henry Simons et al. as a memo to the Roosevelt administration during the banking crisis. Proposed full reserve requirements for demand deposits, separation of deposit-taking from lending, and 100% government backing of the payment-instrument layer.
- **1935 — Irving Fisher's *100% Money*.** Yale's Fisher developed the proposal in book form, framing it as both a stability measure (eliminating bank runs) and a debt-management tool (the reserve increase would let the government retire a chunk of public debt).
- **1948 — Friedman's "A Monetary and Fiscal Framework for Economic Stability."** Milton Friedman (then at Chicago) endorsed 100% reserves as part of a broader rules-based monetary framework. He continued to support the idea throughout his career, including in *A Program for Monetary Stability* (1960).
- **1987 — James Tobin's "The Case for Preserving Regulatory Distinctions."** Tobin (Yale) proposed "deposited currency" — essentially a narrow-bank account at the Fed for retail users — as a way to insulate the payment system from financial-sector instability. This is the most direct intellectual ancestor of both retail CBDCs and stablecoins.
- **2010 — Laurence Kotlikoff's *Jimmy Stewart Is Dead*.** Boston University economist's full reform proposal: "Limited Purpose Banking" — every financial intermediary structured as a mutual fund, full transparency, no leverage. The most ambitious modern narrow-banking program.
- **2014 — John Cochrane's "Toward a Run-Free Financial System."** Hoover Institution / University of Chicago. Proposed that demand-deposit-equivalents (including money-market funds) be 100% backed by Treasuries, with all credit extended through equity-funded vehicles. Closer to what GENIUS actually does.
- **2016 — Adair Turner, Mervyn King.** Both former central bankers wrote serious narrow-banking-adjacent books. King's *The End of Alchemy* explicitly argued for "pawnbroker for all seasons" central banking — a structural redesign where the central bank lends only against pre-positioned high-quality collateral.
- **2018 — TNB USA narrow-bank application.** A startup attempted to open an actual narrow bank with a Fed master account. The Fed denied master account access. The case is often cited as evidence that the Fed views narrow banking as a destabilizing force in conventional banking.
- **2025 — GENIUS Act.** The first U.S. statute that mandates 100% reserve backing for a class of demand-payment instruments, prohibits interest payments to holders (which would be the form of credit extension), and assigns priority to holders in insolvency. It does not call itself narrow banking. Almost nobody in the public debate has called it narrow banking.

## The GENIUS Act as Narrow Banking, Mapped

| Narrow banking principle | GENIUS Act provision |
|---|---|
| 100% reserves against demand liabilities | Issuer must hold liquid assets (cash, T-bills ≤93 days, overnight repo) equal to outstanding stablecoins |
| No credit extension against the payment-instrument | "No interest to holders" — issuers cannot pay yield, foreclosing the most obvious form of credit-funded return |
| Insolvency protection for the payment-instrument layer | Stablecoin holders get first-priority claims over other creditors |
| Separation from credit-extending institutions | Public-company restrictions, OCC supervision, separate legal structure for issuers |
| Government-quality backing | Reserves restricted to U.S. dollars and short-dated Treasuries — the highest-quality assets in the system |

The fit is unusually clean. The GENIUS Act is closer to the Chicago Plan than to any actual existing U.S. financial regulation. It is closer to the Chicago Plan than CBDC alternatives are. It is closer to the Chicago Plan than money-market fund reform.

## Implications — Good and Bad

**Arguments in favor (the narrow-banking tradition):**
- Insulates the payment-instrument layer from credit risk. A stablecoin holder cannot lose their dollars because the issuer made bad loans, because the issuer is forbidden from making loans against the dollars.
- Eliminates a significant source of bank-run dynamics in the digital-payments layer.
- Makes monetary policy transmission cleaner — the Fed knows exactly what backs each unit of stablecoin.
- Consistent with the long-standing intuition that "money" (in the unit-of-account sense) and "credit" (the bank-loan business) should be institutionally separated.

**Arguments against (the orthodox-banking tradition):**
- **Credit creation cost.** Conventional fractional-reserve banking creates credit by lending against deposits. Narrow banking moves that credit creation elsewhere (typically into longer-term equity-funded vehicles), which the orthodox view holds is more expensive and less efficient. If stablecoin float reaches a multi-trillion scale, the dollars locked in T-bill backing are dollars no longer being lent into the productive economy. *Counter:* the dollars were not previously being lent in any direct sense either — they were either in MMFs (already in T-bills) or in deposits (which banks recycled into a mix of loans, securities, and Fed reserves). Substitution effects matter, but the total credit-supply shock is bounded.
- **Yield migration to DeFi.** Because the Act prohibits interest payments to holders, the yield competition is forced onto DeFi rails — staking, lending protocols, restaking, structured products — which (a) is where crypto-native users actually live and (b) creates exactly the kind of regulatory arbitrage the bill is ostensibly designed to prevent. The narrow-banking purity of the issuance layer is bought at the cost of pushing risk into the layer immediately above it.
- **Implicit bailout dynamic.** Adam Levitin's argument: when a 100% reserve stablecoin issuer fails (operational risk, fraud, custody loss), the bankruptcy priority for holders means lawyers and other administrative creditors won't get paid, which means lawyers won't work the case, which means the government has to step in. The "no credit risk" framing creates moral hazard precisely because it makes the implicit guarantee feel costless. This is the standard objection to narrow banking and it has not been answered.
- **The TNB precedent.** The Fed denied master account access to TNB in 2018 specifically to prevent narrow banking from disintermediating conventional banks. The GENIUS Act creates the same disintermediation pressure but routes around the master-account question — see the Fed Account Access gap in [[GENIUS Act]].

## Why Nobody Is Saying It

Three reasons:

1. **The Trump conflict story crowded out the structural story.** The dominant frame for GENIUS in mainstream coverage is "Trump signed a bill that benefits his own crypto venture." That frame is true and important, but it leaves no oxygen for the policy-history frame.
2. **The narrow-banking academics aren't crypto-fluent.** Cochrane, Kotlikoff, Levitin, and the post-Chicago tradition mostly haven't engaged the stablecoin literature. The crypto-fluent commentators (Castle Island, Matt Levine, Nic Carter, Austin Campbell) mostly haven't engaged the narrow-banking literature. The two communities have not collided.
3. **Nobody wants to compliment crypto legislation.** Acknowledging that GENIUS is structurally what reformers have been asking for since 1933 would require both progressive and conservative critics to soften their attacks. Neither has incentive.

The wiki's "politically homeless" voice can claim this lane.

## Tensions & Counterarguments

- The mapping is not perfect. Cochrane and Kotlikoff envisioned narrow banking inside the existing banking perimeter, integrated with the Fed and supervised as banks. GENIUS routes around the Fed (no master account access yet), routes around the SEC, routes around the CFPB, and creates a new sui generis category. A purist narrow-banking advocate would find the institutional architecture awkward.
- The "narrow banking" defense of GENIUS does not address the Trump conflict. Both can be true simultaneously: the legislation can be defensible-on-its-merits *and* the president's stake in its primary asset class can be a textbook conflict of interest. The wiki should hold both layers.
- Whether narrow banking is *good* policy is itself contested. The orthodox banking literature (Diamond/Dybvig and descendants) holds that fractional-reserve banking with deposit insurance is the optimal arrangement; narrow banking is a deviation that has costs. The narrow-banking literature (Fisher/Friedman/Cochrane/Kotlikoff) holds the opposite. The wiki does not need to settle this. It needs to flag that the debate exists and that GENIUS just took one side of it.

## Related Concepts

- [[GENIUS Act]] — the legislation that is structurally narrow banking
- [[Stablecoin Legislation]] — broader regulatory landscape
- [[CBDC]] — the alternative narrow-banking-adjacent route (Tobin's "deposited currency"); explicitly blocked by the Anti-CBDC Act
- [[Fed Independence]] — the Fed's master-account denial to TNB suggests institutional resistance to narrow banking from inside the Fed itself
- [[Dollarization via Stablecoins]] — narrow banking framing matters for how T-bill demand is interpreted

## Key Sources

- *(To be added as raw sources are ingested.)* Foundational texts: Henry Simons et al. (1933, "Banking and Currency Reform"), Irving Fisher (1935, *100% Money*), Milton Friedman (1948, 1960), James Tobin (1987), Laurence Kotlikoff (2010, *Jimmy Stewart Is Dead*), John Cochrane (2014, "Toward a Run-Free Financial System"), Mervyn King (2016, *The End of Alchemy*), Adam Levitin (2025, GENIUS Act bailout-risk commentary cited in [[GENIUS Act Impact on Stablecoins and Taxpayers — Bankrate]]).

## Open Questions

- Has any commentator outside the wiki drawn the GENIUS-as-narrow-banking parallel cleanly? (Levitin nearly does it but anchors his critique on the bailout-risk angle, not the narrow-banking lineage.)
- What does the post-2008 narrow-banking literature say about the *yield-migration* problem — do Cochrane or Kotlikoff address whether forcing yield competition into shadow-banking-adjacent rails recreates the problem narrow banking was supposed to solve?
- The TNB master-account case is the cleanest precedent for institutional resistance to narrow banking. Is there a primary source for the Fed's denial reasoning?
- Does Hugh Rockoff's quantitative work on free banking (see [[Free Banking and Wildcat Banking]] if the page exists) bear on the stablecoin/narrow-banking question, or is it about a different historical problem?
