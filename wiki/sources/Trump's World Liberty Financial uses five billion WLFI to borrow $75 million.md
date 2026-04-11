---
title: "Trump's World Liberty Financial uses five billion WLFI to borrow $75 million"
type: source
tags: [crypto, politics, power]
created: 2026-04-11
updated: 2026-04-11
sources: 8
raw: "raw/Trump's World Liberty Financial uses five billion WLFI to borrow $75 million from a platform its adviser co-founded.md"
source_url: "https://www.coindesk.com/markets/2026/04/09/trump-s-world-liberty-financial-borrows-usd75-million-against-its-own-token-trapping-depositors-on-dolomite"
author: "Shaurya Malwa"
published: 2026-04-09
---

[Original source](https://www.coindesk.com/markets/2026/04/09/trump-s-world-liberty-financial-borrows-usd75-million-against-its-own-token-trapping-depositors-on-dolomite)

## Summary

Onchain data shows [[World Liberty Financial]] (WLFI), the Trump family crypto venture, deposited 5 billion of its own governance tokens plus 14 million USD1 (its own stablecoin) as collateral on [[Dolomite]], a DeFi lending protocol co-founded by WLFI adviser [[Corey Caplan]]. WLFI borrowed approximately $75 million in stablecoins, which were sent to [[Coinbase]] Prime -- a fiat off-ramp. The operation pushed Dolomite's USD1 pool to ~93% utilization, effectively trapping retail depositors who cannot withdraw their funds until the large borrower repays.

## Key Points

- WLFI treasury deposited 14M USD1 as collateral on [[Dolomite]] on Feb. 8, borrowing 11.4M USDC. The USDC moved to Coinbase Prime minutes later.
- Two days later, 12.5M USD1 was sent directly from WLFI treasury to a separate Coinbase Prime address -- not borrowed, just sent straight to a fiat off-ramp.
- On Feb. 20, WLFI deposited 890M WLFI tokens as collateral and borrowed 20M USD1 against them. On March 24, another 1.1B WLFI followed. Total: 1.99B WLFI tokens as collateral, ~$31.4M in stablecoins borrowed.
- [[Dolomite]] co-founder [[Corey Caplan]] is an adviser to World Liberty Financial. This is a direct insider relationship.
- WLFI constitutes ~55% of Dolomite's entire $835.7M total value locked (TVL) -- massive concentration risk for the protocol.
- The USD1 pool hit ~93% utilization ($180M supplied, $167.5M borrowed). At that utilization, ordinary depositors who lent USD1 cannot all withdraw simultaneously.
- USD1 supply rate: 16.24%, borrow rate: 9.18% -- reflecting concentrated borrowing rather than organic demand.
- WLFI has limited market depth relative to the collateral position size. If the token drops and liquidation triggers, the forced sale would crash the price before collateral could be unwound, leaving Dolomite with bad debt falling on retail depositors.
- In April, WLFI treasury sent an additional 3B WLFI tokens to a Gnosis Safe proxy wallet. Destination unclear -- worth ~$266M at current price of $0.0888.
- After CoinDesk's reporting, WLFI token dropped 12% to record lows. WLFI responded that it would "simply supply more collateral" -- which did not reassure holders.

## Newsletter Angles

- **[[Conflict-of-Interest Gap]]**: The WLFI-Dolomite-Caplan triangle is a textbook case of insider self-dealing using DeFi's permissionless infrastructure. The adviser to the borrower co-founded the lending platform. This is the kind of arrangement that would trigger regulatory action in traditional finance.
- **[[Crypto Fraud and Scam Ecosystem]]**: The structure -- borrow against your own illiquid token on a protocol you dominate, send proceeds to a fiat off-ramp -- mirrors classic extractive patterns in crypto. The innovation is doing it under the political protection of a sitting president's family brand.
- **[[GENIUS Act]]** implications: USD1 is WLFI's own stablecoin. If the GENIUS Act passes with favorable stablecoin provisions, it could retroactively legitimize this kind of self-dealing. The overlap between Trump-family crypto ventures and Trump-administration crypto regulation is the story.
- **DeFi's governance vacuum**: Dolomite's permissionless architecture means a single entity can dominate 55% of TVL and trap other depositors with no governance mechanism to prevent it. The "decentralized" label provides cover for what is functionally an insider extraction operation.

## Entities Mentioned

- [[World Liberty Financial]] — Trump family crypto venture; executed the borrowing operation
- [[Donald Trump]] — family co-founders of WLFI; political dimension of the conflict of interest
- [[Dolomite]] — DeFi lending protocol where the borrowing occurred; co-founded by WLFI adviser
- [[Corey Caplan]] — co-founder of Dolomite and adviser to WLFI; the insider link
- [[Coinbase]] — Coinbase Prime used as the fiat off-ramp for borrowed stablecoins

## Concepts Mentioned

- [[Conflict-of-Interest Gap]] — adviser to borrower co-founded the lending platform
- [[Crypto Fraud and Scam Ecosystem]] — the structure mirrors classic extractive DeFi patterns
- [[GENIUS Act]] — pending stablecoin legislation that could interact with USD1's regulatory status

## Quotes

> WLFI responded that it would "simply supply more collateral" if markets moved against it -- a statement that did not reassure holders.

## Notes

- CoinDesk's analysis is based on onchain records (Etherscan, Arkham, public wallet data) -- this is verifiable primary sourcing, not speculation. The structural facts are strong.
- WLFI did not respond to CoinDesk's initial request for comment. Their subsequent defense ("supply more collateral") actually highlights the circular risk: the collateral is their own token, which would also decline in a liquidation cascade.
- The 3B WLFI tokens sent to a Gnosis Safe in April are unaccounted for. This is an open question worth tracking.
- The article does not discuss whether Dolomite's smart contracts have any mechanisms to prevent this kind of concentration, or whether its governance structure could theoretically intervene.
