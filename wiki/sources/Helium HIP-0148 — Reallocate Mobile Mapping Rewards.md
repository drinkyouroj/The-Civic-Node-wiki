---
title: "Helium HIP-0148 — Reallocate Mobile Mapping Rewards"
type: source
tags: [technology, infrastructure, crypto, depin, governance]
created: 2026-05-19
updated: 2026-05-19
sources: 4
raw: "raw/HIP0148-reallocate-mobile-mapping-rewards.md at main · heliumHIP.md"
source_url: "https://github.com/helium/HIP/blob/main/0148-reallocate-mobile-mapping-rewards.md"
author: "madninja"
published: 2025-09-23
---

[Original source](https://github.com/helium/HIP/blob/main/0148-reallocate-mobile-mapping-rewards.md)

## Summary

Helium Improvement Proposal #148, authored by GitHub user `madninja` and merged to the HIP repository on September 23, 2025. The proposal eliminates the Mobile Mapping rewards category entirely — the 20% of HNT emissions that had previously been earmarked for Helium Mobile subscribers who shared location data — and redirects those emissions to the Service Provider Pool (10%) and the Data Transfer Pool (10%). In a separate but bundled change, the proposal also repeals HIP-87's proportional Service Provider reward formula and directs the entire Service Provider Pool to a single recipient: Nova Labs. The proposal additionally rolls the 4% Oracle Operator allocation into the Service Provider Pool, bringing Nova Labs's combined allocation to 24% of Mobile network HNT emissions. Subscribers who had been earning HNT for mapping retain access to the cellphone plans but no longer earn HNT for sharing location data — those subscribers now receive "Cloud Points" (gift-card credits redeemable for eGift cards or charity donations) instead. The proposal passed in the October 3–10, 2025 vote.

## Key Points

**The mapping rewards elimination (the headline change):**
- Pre-HIP-148: 20% of Mobile network HNT emissions allocated to Mobile Mapping (subscribers earning HNT for sharing location data from their phones).
- Post-HIP-148: 0% to mapping. 10% redirected to the Service Provider Pool, 10% to the Data Transfer Pool.
- Subscribers who had been mapping for HNT are migrated to Cloud Points (gift-card credits), not HNT.

**The Service Provider Pool consolidation (the second change):**
- Pre-HIP-148: Service Provider Pool was 10% of emissions, distributed proportionally based on each provider's Data Credit burn (per HIP-87).
- Post-HIP-148: Service Provider Pool grows to 24% of emissions (10% original + 10% from mapping + 4% from Oracle Operators). The full pool is emitted directly to "the current single active Service Provider (Nova)" — i.e., Nova Labs.
- HIP-87 (proportional formula), HIP-114 (subscriber referral program), HIP-79 (mapping rewards increase), and HIP-118 (verification mapping granularity) are all repealed.

**The motivation as stated in the proposal:**
1. Mapping software complexity caused battery/memory/CPU problems on user phones.
2. Gamers gamed the location data, "polluting the mapping data set substantially."
3. Verification Mapping (the supposed bridge between mapping data and PoC) was observed in <5% of mapping data.
4. Helium Mobile subscribers turning off mapping was "quite high" once the user base shifted to non-crypto subscribers who saw no clear benefit.
5. The mapping data set "has not been very useful in guiding deployers" — "carrier offload locations are a much higher quality signal of where to deploy than mapping data."

**The allocation table (from the proposal itself):**

|                   | HIP 53 | HIP 79 | HIP 146 | HIP 148 |
|-------------------|:------:|:------:|:-------:|:-------:|
| Data Transfer     | 40%    | 40%    | 60%     | **70%** |
| PoC               | 20%    | 20%    | 0%      | 0%      |
| Service Providers | 20%    | 10%    | 10%     | **24%** |
| Mappers           | 10%    | 20%    | 20%     | **0%**  |
| Oracle Operators  | 4%     | 4%     | 4%      | **0%**  |
| Stakers           | 6%     | 6%     | 6%      | 6%      |

**Stakeholders explicitly named in the proposal:**
- "Legacy Crypto Mappers, who would lose their mapping rewards. The upside is that they retain a competitive cellphone plan."
- "Helium Mobile would see the rewards shift from per-subscriber mapping rewards to a simpler Service Provider rewards model."
- "Token-based Subscriber Referral Programs, which will be terminated as part of this HIP."
- "Nova as Oracle Operator will no longer have access to a future Oracle Operator Rewards Pool, as the rewards will be moved to the Service Provider Rewards Pool, which may be re-allocated for other uses in the future."

**Vote outcome (per companion source [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]):**
- Vote window: October 3–10, 2025.
- Approval rate: 96.72% in favor.
- Deployment: rolled out in the 2025-11 HRP release.

## Newsletter Angles

- **The substitution is unambiguous.** HIP-143 substituted "Nova Labs negotiates pricing" for "governance negotiates pricing" — operators could argue this was efficiency rather than extraction. HIP-148 substitutes "Cloud Points" (gift-card credits) for "HNT" (a token with a market price) as the reward for the same labor (sharing data). The substitution is named in the proposal text itself: subscribers go from earning HNT to earning Cloud Points. There is no efficiency framing available — it is a category change.
- **Nova Labs ends HIP-148 with 24% of Mobile emissions allocated to it directly.** The proposal text says this explicitly: *"To simplify technical implementation, we propose to emit the full allocation available from Service Provider Rewards and Oracle Operator Rewards to the single Service Provider Nova Labs."* This is the primary-source quote the May 22 flagship needed — Messari paraphrased it; the proposal itself is unambiguous.
- **The motivation section concedes that mapping data was never useful.** The proposal acknowledges that gaming polluted the data, that verification mapping was <5%, and that "carrier offload locations are a much higher quality signal of where to deploy than mapping data." This is Helium's own admission that an entire 20% emissions category was an experiment that failed. The operators who deployed expecting that category to compensate them got the upside reallocated to Nova Labs.
- **This is the second governance-changes-economics-after-deployment event in 18 months.** HIP-143 (April 2025) authorized Nova Labs to set carrier pricing without governance involvement. HIP-148 (October 2025) directs ~24% of Mobile emissions to Nova Labs and eliminates a 20% category that subscribers had been earning from. The franchise architecture documented in [[Helium HIP-143 and the DePIN Franchise Architecture]] is now a documented pattern, not a single-incident inference.

## Entities Mentioned

- [[Helium Network]] — the protocol this governs
- [[Nova Labs]] — explicitly named in the proposal as the "single active Service Provider" receiving the consolidated 24% allocation; also the entity losing future Oracle Operator pool access (which is moot, since the proposal moves those funds to Nova Labs anyway via the Service Provider Pool)
- madninja — proposal author (GitHub handle; not currently a documented wiki entity)

## Concepts Mentioned

- [[DePIN]] — governance theater: the operators voted to redirect rewards away from themselves and toward the corporate operator
- [[Tokenomics]] — emissions reallocation; HNT → Cloud Points substitution

## Quotes

> "To simplify technical implementation, we propose to emit the full allocation available from Service Provider Rewards and Oracle Operator Rewards to the single Service Provider Nova Labs, allowing Nova to use the pool as needed for protocol development, operations including Oracles, and subscriber incentives."

> "Legacy Crypto Mappers, who would lose their mapping rewards. The upside is that they retain a competitive cellphone plan."

> "Carrier offload locations are a much higher quality signal of where to deploy than mapping data."

> "Service Provider Rewards will be emitted directly to the current single active Service Provider (Nova)."

## Notes

Primary governance document, fetched directly from the helium/HIP GitHub repository on 2026-05-19. The PR (#1186) was merged 2025-09-23, which is also the "Start Date" listed in the proposal header. The vote ran 2025-10-03 to 2025-10-10. Companion source page [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]] captures the tally (96.72% for) — the full proxy breakdown requires manual screenshot capture from the JS-rendered Helium Vote portal, mirroring the HIP-143 capture pattern.

This proposal is the second-instance proof of the franchise-architecture pattern documented in [[Helium HIP-143 and the DePIN Franchise Architecture]]. Where HIP-143 could be argued as commercial efficiency (delegating pricing negotiation to Nova Labs), HIP-148 cannot — it directly substitutes tokens for gift-card credits as the reward for the same subscriber labor, and consolidates 24% of Mobile emissions directly to Nova Labs by removing every other Service Provider that could have competed for that pool.
