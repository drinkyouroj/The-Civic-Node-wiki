---
title: "Helium HIP-148 Vote Results — Helium Vote"
type: source
tags: [technology, infrastructure, crypto, depin, governance]
created: 2026-05-19
updated: 2026-05-19
sources: 4
raw: "raw/assets/HIP-148 vote breakdown.png, raw/assets/HIP-148 X announcement.png"
source_url: "https://heliumvote.com/hnt/proposals/2PEJVC3nc2EncXMeyAzwYexRQmBSv6JyvBCJqNWHg76v"
author: "Helium Foundation / on-chain veHNT holders"
published: 2025-10-10
---

[Original source](https://heliumvote.com/hnt/proposals/2PEJVC3nc2EncXMeyAzwYexRQmBSv6JyvBCJqNWHg76v)

## Summary

Primary-source vote-tally screenshots from the Helium Vote governance portal for HIP-148 (Reallocate Mobile Mapping Rewards), captured 2026-05-19. The vote closed October 10, 2025, 10:51 AM. The proposal passed overwhelmingly (96.72% for) — but the voter breakdown shows the ferebee proxy alone controlled 31.00% of the total vote, the Nova Labs proxy controlled 26.00%, and together those two proxies cast **57% of all votes** (and 57% of yes votes, since both voted For). The single named "Against" vote (Keith Rettig) totaled 1.00% of voting power. The companion @helium X account announced passage on October 14, 2025.

## Key Points

**Vote tally:**
- **For HIP 148: 872,704,450.74 veHNT (96.72%)**
- **Against HIP 148: 29,571,045.78 veHNT (3.27%)**
- Total veHNT cast: **902,275,496.10**
- Date occurred (vote close): **October 10, 2025, 10:51 AM**
- Voting window: Oct 3 – Oct 10, 2025 (7 days)
- Quorum threshold: not displayed on this view; 902.28M veHNT cast is 9.0× the 100M quorum that applied to HIP-143
- (Note: 96.72% + 3.27% = 99.99% — the 0.01% gap is a rounding artifact in the portal display; For + Against raw figures sum to within 0.42 veHNT of the displayed total, confirming there is no third option being hidden)

**Comparison to HIP-143:**

|                  | HIP-143 (Apr 3, 2025) | HIP-148 (Oct 10, 2025) | Change       |
|------------------|:---------------------:|:----------------------:|:------------:|
| Total veHNT cast | 763.5M                | 902.3M                 | +18.2%       |
| For %            | 90.53%                | **96.72%**             | +6.19 pp     |
| Against %        | 9.46%                 | 3.27%                  | -6.19 pp     |
| Nova Labs proxy  | 26.00% (199.79M)      | 26.00% (241.87M)       | flat % / +21% absolute |
| ferebee proxy    | 24.00% (183.85M)      | **31.00% (285.92M)**   | +7 pp / +55.5% absolute |
| Nova + ferebee   | **50%** of yes votes  | **57%** of total votes | +7 pp        |

**Voter breakdown (top 12 voters, all proxies):**

| Owner (truncated) | Choice           | Vote Power     | %      | Proxy Name    |
|-------------------|------------------|---------------:|-------:|---------------|
| FEREB...wKfLn     | For              | 285,917,702.34 | 31.00% | **ferebee**   |
| 80fBw...lwv69     | For              | 241,867,765.19 | 26.00% | **Nova Labs** |
| 8AQ8Q...L2apU     | For              |  52,630,899.59 |  5.00% | Jay M.        |
| H8uAP...NxqoJ     | For              |  49,131,289.38 |  5.00% | —             |
| 85ynw...EDfJu     | For              |  45,368,128.90 |  5.00% | —             |
| 5MXQL...UXEnp     | For              |  37,484,283.58 |  4.00% | AndrewsMD     |
| 8XEzB...vSdc8     | For              |  31,871,446.20 |  3.00% | —             |
| 3X9Rf...b6c9D     | For              |  21,000,000.00 |  2.00% | —             |
| 7pkz0...3FjVL     | For              |  19,904,172.92 |  2.00% | —             |
| EYn23...PUar1     | **Against**      |  13,983,104.10 |  1.00% | **Keith Rettig** |
| 4yUoG...n3xC7     | For              |  10,446,172.61 |  1.00% | —             |
| 9xaQT...GVAQa     | For              |   6,084,774.29 |  0.00% | —             |

(Owner ID prefixes/suffixes truncated as displayed in the portal. Some proxies show no proxy-name label, meaning the wallet did not set one publicly.)

**The proxy concentration finding (the smoking gun):**
- **ferebee proxy alone: 285.92M veHNT (31.00% of total vote)** — voted For
- **Nova Labs proxy: 241.87M veHNT (26.00% of total vote)** — voted For
- **Combined: 527.78M veHNT = 57.00% of total vote, 60.5% of yes votes**
- The proposal authored by `madninja` (whose relationship to ferebee and Nova Labs is not disclosed in the proposal text) was approved by votes that the ferebee proxy and the Nova Labs corporate proxy controlled.
- The single largest opposition vote: Keith Rettig at 1.00% (13.98M veHNT). Total named "Against" representation was 1.00%; the remaining 2.27% of "Against" was distributed across unlabeled proxies.

**Concentration grew between HIP-143 and HIP-148.** Nova Labs's absolute veHNT held grew 21% (199.79M → 241.87M) — but its percentage share stayed flat at 26%. The ferebee proxy's absolute veHNT grew 55.5% (183.85M → 285.92M), increasing its percentage share from 24% to 31%. The proposing entity and the largest co-author proxy are accumulating veHNT faster than the rest of the network.

**Companion X announcement (October 14, 2025, 9:05 PM):**
- "✅ HRP 2025-10 and HIP 148 have passed!"
- "🗳️ HRP 2025-10: 99.80% in favor"
- "🗳️ HIP 148: 96.72% in favor"
- "Deployment Update: HRP 2025-10: Protocol Changes are now active."
- "HIP 148 will roll out during the 2025-11 HRP release. This timing allows legacy and crypto subscribers to be notified and offered plan switch incentives."
- Engagement: 11.3K views, 61 likes, 4 reposts, 7 replies, 2 bookmarks (as of capture date).
- Bundled HRP 2025-10 (procedural protocol release) with HIP 148 (substantive emissions reallocation) in the same tweet — framing the substantive change as routine release housekeeping.

**Provisions of the proposal (from companion proposal text):**
- Mobile Mapping rewards (20% of Mobile emissions) eliminated entirely.
- 10% redirected to Service Provider Pool, 10% to Data Transfer Pool.
- Oracle Operator pool (4%) folded into Service Provider Pool.
- Service Provider Pool (now **24% of Mobile emissions**) emitted directly to Nova Labs as the sole active Service Provider.
- Subscribers who had been earning HNT for mapping now receive Cloud Points (gift-card credits).
- Repealed: HIP-79, HIP-87, HIP-114, HIP-118.
- See [[Helium HIP-0148 — Reallocate Mobile Mapping Rewards]] for full mechanism.

## Newsletter Angles

- **The franchise architecture is documented twice with primary-source vote receipts.** HIP-143's proxy concentration finding (Nova Labs + ferebee = 50% of yes votes) is no longer a single-incident anomaly. HIP-148's concentration is HIGHER — ferebee 31% + Nova Labs 26% = 57% of total votes — for a proposal that consolidates 24% of Mobile emissions directly to Nova Labs and substitutes Cloud Points for HNT as subscriber compensation. The pattern Messari paraphrased as "passed without organized opposition" is, when the screenshot is in hand, structurally guaranteed: the entity benefiting from the proposal's passage holds majority voting control.
- **The opposition vote has a name and a face.** Keith Rettig — 1.00%, 13.98M veHNT, voted Against — is the named human-scale dissent. Every other named proxy in the top 12 voted For. This is a clean lede for the May 22 flagship: name Rettig, then show what 99% of voting power did with the proposal.
- **ferebee's veHNT grew 55% between April and October 2025** while everyone else's participation grew at the network average. This is the third-order finding: it's not just that the proposing entity controls the proposal vote — the proposing entity is *accumulating veHNT faster than the network*, which means future HIPs will be even more concentrated. The franchise architecture is self-reinforcing through the veHNT lock-up mechanism.
- **The Helium account bundled the announcement.** "✅ HRP 2025-10 and HIP 148 have passed!" treated a procedural release proposal (99.80% approval, no economic content) and a substantive emissions reallocation (96.72%, consolidates 24% to Nova Labs) as a single news beat. Operators reading the announcement would have to click through to find that one of the two was eliminating their reward category.

## Entities Mentioned

- [[Nova Labs]] — 26% of HIP-148 votes via own proxy; recipient of consolidated 24% Service Provider Pool emissions per the proposal
- [[Helium Network]] — the protocol being governed
- ferebee — proxy holding 31% of HIP-148 votes; up from 24% on HIP-143; HIP-143 co-author; relationship to HIP-148 author `madninja` not disclosed in proposal text
- madninja — HIP-148 proposal author (GitHub handle)
- Keith Rettig — named Against voter (1.00%); largest single opposition proxy
- Jay M., AndrewsMD — named For voters (5.00% and 4.00% respectively); HIP-143 also showed a "Jay M." voter at 5.00%

## Concepts Mentioned

- [[DePIN]] — governance theater documentation; second-instance proof
- [[Tokenomics]] — veHNT lock-duration voting power concentration; veHNT accumulation by the proposing-entity proxy outpacing network average
- "Proxy Concentration Audit" (from [[Helium HIP-143 and the DePIN Franchise Architecture]]) — this is the second clean application of the audit, and the result is more concentrated than the first

## Notes

Primary source: two PNG screenshots of the Helium Vote portal and the @helium X announcement, preserved at `raw/assets/HIP-148 vote breakdown.png` and `raw/assets/HIP-148 X announcement.png`. The vote portal is JS-rendered and could not be scraped automatically — the user manually captured the screenshots on 2026-05-19. This is the same constraint and capture pattern that applied to HIP-143.

The proxy names are public on-chain identifiers. "Nova Labs" and "ferebee" appearing as proxy labels means the wallet addresses voluntarily set their public proxy names to those values — these are the corporate entity behind the proposal acknowledging its own vote, and the largest individual co-author proxy doing the same, not inferences.

The proposal text names `madninja` as the author, not ferebee. The HIP-143 proposal text named "Inversion Capital, zer0tweets, Nova Labs, ferebee" as co-authors. madninja's relationship to ferebee and Nova Labs is not disclosed in the HIP-148 text. This is worth flagging as a follow-up question: whether `madninja` is a Nova Labs developer, an independent contributor, or a pseudonym associated with one of the named HIP-143 co-authors. The vote outcome does not depend on this — ferebee + Nova Labs proxies carried the proposal regardless — but the authorship chain matters for accurately naming who designed the substitution.

The 0.01% rounding gap between For (96.72%) and Against (3.27%) — totaling 99.99% — is a portal display artifact. The raw veHNT counts (872,704,450.74 + 29,571,045.78 = 902,275,496.52, vs. displayed total of 902,275,496.10) differ by 0.42 veHNT, well within rounding tolerance. There is no hidden third option.
