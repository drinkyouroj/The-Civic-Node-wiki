---
title: "Helium HIP-143 Vote Results — Helium Vote"
type: source
tags: [technology, infrastructure, crypto, depin, governance]
created: 2026-05-16
updated: 2026-05-16
sources: 4
raw: "raw/assets/HIP-143 summary-details.png, raw/assets/HIP-143 voter breakdown.png"
source_url: "https://heliumvote.com/hnt/proposals/4EemLuZhTgtv6SFNogMByCTEx4DFtBKc32qEhDKL9iaZ"
author: "Inversion Capital, zer0tweets, Nova Labs, ferebee"
published: 2025-04-03
---

[Original source](https://heliumvote.com/hnt/proposals/4EemLuZhTgtv6SFNogMByCTEx4DFtBKc32qEhDKL9iaZ)

## Summary

Primary-source vote-tally screenshots from the Helium Vote governance portal for HIP-143 (Decoupling Service Provider Pricing from Governance). The vote occurred April 3, 2025 at 1:13 PM. The proposal passed overwhelmingly (90.53% for) — but the voter breakdown shows the proposer (Nova Labs) and a co-author (ferebee) controlled 50% of the yes votes via their own proxies.

## Key Points

**Vote tally:**
- **For HIP 143: 691,254,123.19 veHNT (90.53%)**
- **Against HIP 143: 72,249,632.58 veHNT (9.46%)**
- Total veTOKENS cast: 763,503,755.78
- Approval threshold: 67% of voting power; quorum: 100,000,000 veHNT — both met decisively.
- Vote date: April 3, 2025 at 1:13 PM

**Voter concentration (top 6 voters, all proxies):**

| Proxy | Vote | Power | % of Total |
|---|---|---|---|
| Nova Labs | For | 199,790,816.87 veHNT | **26.00%** |
| ferebee | For | 183,846,182.84 veHNT | **24.00%** |
| HKcAP...NxqoJ | **Against** | 63,622,983.73 veHNT | 8.00% |
| 93Dz8...dScH8 (no proxy name) | For | 43,969,699.22 veHNT | 5.00% |
| Jay M. | For | 40,119,856.34 veHNT | 5.00% |
| 95VLQ...fpbG7 (no proxy name) | For | 25,246,965.95 veHNT | 3.00% |

**The proxy concentration finding:**
- The Nova Labs proxy and the ferebee proxy together controlled **50% of all yes votes** for HIP-143.
- HIP-143 was authored by "Inversion Capital, zer0tweets, Nova Labs, ferebee" — so the two largest "yes" proxies represent the proposing entity (Nova Labs) and a co-author (ferebee).
- The proposal granting Nova Labs unilateral pricing authority was approved by votes Nova Labs and its co-author controlled.
- The single largest "against" vote was an anonymous proxy at 8.00% — no organized opposition above that threshold.

**Provisions of the proposal (from companion proposal text):**
- Nova Labs authorized to negotiate Data Transfer pricing with mobile network operators without involving Helium governance.
- Nominal rate of $0.50/GB preserved (HIP-53); Nova Labs can adjust Rewarded vs. Unrewarded Data ratio (HIP-129).
- 1-year delegation period from implementation; auto-renews for additional year if no overriding HIP passes.
- As of Q4 2025 (Messari report), no superseding HIP had been passed — auto-renewal would occur around April 2026.

## Newsletter Angles

- **The proxy voting is the smoking gun.** The "DePIN mullet" thesis (centralized control dressed as community governance) is documented one level deeper: in the case of HIP-143, the entity authorized by the proposal controlled 26% of the votes approving it. The co-author controlled another 24%. The proposal couldn't have failed.
- The veHNT design — voting power scales with lock duration up to 4 years — concentrates governance with whales who can lock for the longest periods. The 90.53% approval looks like community consensus until you see that two proxies = half the yes votes.
- Total turnout was 7.6× the 100M veHNT quorum. High formal participation, extreme concentration. This is what "decentralized governance" produces at scale.

## Entities Mentioned

- [[Nova Labs]] — proposer and 26% of yes votes via own proxy
- [[Helium Network]] — the protocol being governed
- ferebee — co-author of HIP-143; 24% of yes votes via own proxy

## Concepts Mentioned

- [[DePIN]] — governance theater documentation
- [[Tokenomics]] — veHNT lock-duration voting power concentration

## Notes

Primary source: two PNG screenshots of the Helium Vote portal preserved at raw/assets/. The vote portal is JS-rendered and could not be scraped automatically — the user manually captured the vote breakdown.

The proxy names are public on-chain identifiers. "Nova Labs" appearing as a proxy label means the wallet address voluntarily set its public proxy name to "Nova Labs" — this is the corporate entity behind the proposal acknowledging its own vote, not an inference.
