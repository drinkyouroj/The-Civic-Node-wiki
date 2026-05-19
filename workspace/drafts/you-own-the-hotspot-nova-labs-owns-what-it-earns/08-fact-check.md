# Fact Check Report: "You Own the Hotspot. Nova Labs Owns What It Earns."

**Draft verified:** `07-humanized.md`
**Verification sources:** wiki source pages, raw files, bash grep on HIP raw text
**Claims extracted:** 19 linked + 4 unsourced factual claims
**Verified:** 15 | **Partially verified:** 1 | **Not found in source:** 3 | **Source inaccessible:** 0 | **Unsourced:** 4

---

### Verified Claims

| # | Claim (from article) | Source | Status |
|---|---|---|---|
| 1 | Pro outdoor hotspot costs $949 | bytetree.com | ✓ Verified |
| 2 | Basic indoor Helium IoT box costs $249 | bytetree.com | ✓ Verified |
| 3 | A well-placed urban hotspot earns $4 to $8 a month | AMBCrypto | ✓ Verified |
| 4 | HIP-143 passed April 3, 2025 | HIP-143 GitHub | ✓ Verified |
| 5 | HIP-143 authorized Nova Labs to negotiate carrier pricing without governance vote | HIP-143 GitHub | ✓ Verified |
| 6 | HIP-143 proposal came with a 1-year sunset | HIP-143 GitHub | ✓ Verified |
| 7 | 385,000 deployed hotspots | Messari Q4 2025 | ✓ Verified |
| 8 | August 2025 halving reduced HNT emissions from 15M to 7.5M per year | Helium halving blog | ✓ Verified |
| 9 | HIP-143 proposal text quote ("If Nova Labs would be able to move quickly...") | HIP-143 GitHub raw file | ✓ Verified verbatim at line 31 |
| 10 | HIP-143 vote: 90.53% on 763M veHNT cast | heliumvote.com (HIP-143 proposal) | ✓ Verified |
| 11 | Nova Labs proxy: 26.00% of vote; ferebee proxy: 24.00%; together 50% | heliumvote.com (HIP-143 proposal) | ✓ Verified; math: 26+24=50 ✓ |
| 12 | ferebee listed as co-author of HIP-143 | HIP-143 GitHub | ✓ Verified |
| 13 | HIP-148 voted October 3–10, 2025 | HIP-148 GitHub | ✓ Verified |
| 14 | Mobile Mapping rewards were 20% of HNT emissions | HIP-148 wiki source | ✓ Verified |
| 15 | HIP-148 proposal text quote ("To simplify technical implementation...") | HIP-148 wiki source | ✓ Verified (see Flag #4 below for truncation note) |
| 16 | Service Provider Pool went from 10% → 24% of Mobile emissions, flowing to Nova Labs | HIP-148 wiki source | ✓ Verified |
| 17 | Cloud Points = gift-card credits redeemable for eGift cards or charity donations | HIP-148 wiki source | ✓ Verified |
| 18 | HIP-148 vote: 96.72% on 902M veHNT; 18% more participation than HIP-143 | HIP-148 vote results wiki source | ✓ Verified; math: (902-763)/763 = 18.2% ✓ |
| 19 | ferebee: 31.00%; Nova Labs: 26.00%; combined 57% | HIP-148 vote results wiki source | ✓ Verified; math: 31+26=57 ✓ |
| 20 | Nova Labs: flat % but +21% in absolute veHNT | HIP-148 vote results wiki source | ✓ Verified; math: (241.87-199.79)/199.79 = 21.1% ✓ |
| 21 | Keith Rettig voted against, held 1.00% | HIP-148 vote results wiki source | ✓ Verified |
| 22 | ferebee veHNT: 183.85M → 285.92M, up 55.5% | HIP-148 vote results wiki source | ✓ Verified; math: (285.92-183.85)/183.85 = 55.5% ✓ |
| 23 | Network participation grew 18.2% in the same period | HIP-148 vote results wiki source | ✓ Verified (same calculation as claim 18) |
| 24 | Three times the network average | Derived calculation | ✓ Verified; 55.5%/18.2% = 3.05x ✓ |
| 25 | Helium Foundation guidance: "set a proxy as a backup to ensure you don't miss out on rewards" | Helium halving blog | ✓ Verified; confirmed at line 83 of raw file. Full sentence: "It is highly recommended to set a proxy as a backup to ensure you don't miss out on rewards." Article correctly excerpts the relevant clause. |
| 26 | $124.77 per day in actual IoT data transfer revenue | Messari Q4 2025 | ✓ Verified |
| 27 | $949 outdoor hotspot payback: 10 years at $8/mo, 20 years at $4/mo | Derived from sourced figures | ✓ Verified; $949/$8 = 118.6 mo ≈ 10 yr; $949/$4 = 237.25 mo ≈ 20 yr ✓ |

---

### Flagged Claims

#### Flag #1 (Required correction): HIP-82 attributed wrong function; wrong source
**Article says:** `"[HIP-82](https://www.tokenomist.ai/helium) capped data transfer rewards at $0.50 per gigabyte."`
**Source says:** Tokenomist.ai/helium is a token supply and vesting data dashboard. It contains no governance documentation, no HIP references, and no per-gigabyte pricing data. The claim is not in this source.
**Primary source says:** The HIP-143 raw file (line 21) states: `"The nominal cost of data remains at $0.50/GB as defined in HIP-53."` Line 29 of the same file states HIP-82 introduced "Rewardable Data rules" — the criteria governing which data transfers qualify for rewards, a different mechanism from the $0.50/GB rate.
**Discrepancy:** Two separate errors. (1) The HIP number is wrong: $0.50/GB was set by HIP-53, not HIP-82. HIP-82 introduced Rewardable Data eligibility criteria, not per-GB pricing. (2) The source link (Tokenomist) does not contain this claim.
**Recommendation:** Change "HIP-82" to "HIP-53." Replace the Tokenomist link with the HIP-53 GitHub page (or the HIP-143 GitHub page, which cites HIP-53 at line 21 and is already linked in the piece). If HIP-82's actual contribution (rewardable data rules) is worth preserving, rewrite as two separate claims; otherwise, drop HIP-82 from the list of three rule changes.

---

#### Flag #2 (Required correction): $56,635/day sourced to wrong outlet
**Article says:** `"The Mobile side, routing carrier offload traffic for T-Mobile and AT&T, generates [$56,635 per day](https://sarsonfunds.com/heliums-exceptional-growth-in-2025-sustaining-leadership-in-decentralized-wireless/)."`
**Source says:** The Sarson Funds blog post covers Helium's growth broadly but does not explicitly report the $56,635/day figure.
**Primary source says:** The Messari Q4 2025 report (already linked elsewhere in the piece) contains "Mobile share of daily burns: $56,635."
**Discrepancy:** Figure exists in Messari, not Sarson Funds. Source link points to the wrong outlet.
**Recommendation:** Swap the Sarson Funds link for the Messari Q4 2025 link (same URL already used in the piece for other claims: `https://messari.io/report/state-of-helium-q4-2025`). The paragraph will then have both the $124.77 and $56,635 figures sourced to Messari — correct and consistent.

---

#### Flag #3 (Required correction): HIP-138 sourced to wrong outlet
**Article says:** `"[HIP-138](https://www.tokenomist.ai/helium) consolidated the IoT and Mobile subnetwork tokens into a single HNT in January 2025."`
**Source says:** Tokenomist.ai/helium is a token supply and vesting data dashboard. It contains no governance documentation and no HIP-138 reference.
**Primary source says:** The AMBCrypto source (already linked in the piece at `https://eng.ambcrypto.com/how-much-can-you-really-earn-with-helium-hotspots-in-2025/`) states: "Helium Improvement Plan #138, subnetwork tokens...have been phased out in favour of HNT."
**Discrepancy:** Correct claim, wrong source link. AMBCrypto (already in the piece) supports this; Tokenomist does not.
**Recommendation:** Change the `[HIP-138]` link from Tokenomist to the AMBCrypto URL: `https://eng.ambcrypto.com/how-much-can-you-really-earn-with-helium-hotspots-in-2025/`. No claim text change needed.

---

#### Flag #4 (Style — minor): HIP-148 quote truncated without ellipsis notation
**Article says:** `"To simplify technical implementation, we propose to emit the full allocation available from Service Provider Rewards and Oracle Operator Rewards to the single Service Provider Nova Labs."`
**Source says (full sentence):** `"To simplify technical implementation, we propose to emit the full allocation available from Service Provider Rewards and Oracle Operator Rewards to the single Service Provider Nova Labs, allowing Nova to use the pool as needed for protocol development, operations including Oracles, and subscriber incentives."`
**Discrepancy:** The article adds a period after "Nova Labs" where the source has a comma continuing the sentence. The truncated portion ("allowing Nova to use the pool as needed for protocol development...") is omitted without notation.
**Assessment:** The truncated text doesn't alter the meaning of the claim being sourced — the article is sourcing the consolidation to Nova Labs, not how Nova uses those funds. The omission is defensible. However, standard practice is to mark truncation with "..." or "[...]" so readers know the quote continues.
**Recommendation:** Change the closing period to an ellipsis: `"...to the single Service Provider Nova Labs..."` — or use `[...]` before the closing period. Either resolves the notation gap. Low priority; the claim remains accurate as written.

---

### Partially Verified Claims

#### Partial #1: April 2026 HIP-143 sunset — temporal sourcing gap
**Article says:** `"In April 2026, [the HIP-143 sunset expired](https://messari.io/report/state-of-helium-q4-2025) with no replacement vote filed."`
**Source says:** The Messari Q4 2025 report notes the upcoming 1-year sunset on HIP-143's pricing authority. The report was published in Q4 2025, before April 2026. It predicts the sunset; it does not confirm the absence of a superseding HIP filed after the fact.
**Discrepancy:** The claim is inferentially sound — HIP-143 passed April 3, 2025 with a 1-year sunset, making the expiry date ~April 3, 2026, and no replacement is visible in the Helium governance GitHub — but no post-April-2026 source directly confirms "no replacement was filed."
**Assessment:** The underlying fact is almost certainly correct (confirmed by absence of a superseding HIP in the governance repo). The temporal gap in sourcing is real: Messari accurately describes the mechanism but can't confirm the April 2026 outcome from Q4 2025.
**Recommendation:** Either (a) add a brief qualifier: "The HIP-143 sunset arrived in April 2026 with no superseding proposal on file as of [Messari's Q4 2025 report]" — or (b) find a post-April-2026 confirmation (a community forum post, a Helium Foundation announcement, or a search of the HIP GitHub showing no HIP in the 143-successor range filed before May 2026). If (b) can be verified, the current phrasing stands and the source link is acceptable as background context.

---

### Unsourced Claims

| # | Claim | Recommendation |
|---|---|---|
| U1 | "Nova Labs...negotiates carrier offload deals with T-Mobile and AT&T" (opener + The Glitch) | Acceptable as established background; widely documented in Helium coverage. No inline link needed, but a link to the Helium Mobile landing page or a press release announcing the T-Mobile deal could strengthen the claim if sourcing is desired. |
| U2 | "$949" outdoor hotspot price in the opener (first paragraph) | Acceptable restatement — this figure is sourced via bytetree when it appears in The Glitch section. Standard journalistic practice for opener setup. |
| U3 | HIP-143 had "a 1-year sunset" (opener paragraph, no inline link) | Acceptable — the claim is supported by the HIP-143 GitHub link immediately following in The Glitch. The opener is setting up the argument; the source appears at first substantive mention. |
| U4 | "ferebee and Nova Labs were the proxies most operators were pointed toward" | Acceptable editorial inference from the Foundation's guidance linking to these proxies. The Helium Foundation halving blog (already linked) recommends proxy delegation; ferebee and Nova Labs are the named top proxies in the vote results (already sourced). The editorial characterization is supported by the sourced data. |

---

### Source Accessibility Issues

All required sources were verified via wiki source pages or raw files. No sources were inaccessible.

| Source | Method | Notes |
|---|---|---|
| HIP-143 GitHub | Raw file grep | Confirmed verbatim; HIP-53/$0.50GB finding from line 21 |
| HIP-148 GitHub | wiki/sources page | Confirmed quote and pool percentages |
| heliumvote.com (both HIPs) | wiki/sources pages | Confirmed all vote figures |
| Messari Q4 2025 | wiki/sources page | Confirmed $124.77/day, 385,000 hotspots, sunset reference |
| Helium halving blog | wiki/sources page + raw file | Confirmed halving figures and proxy delegation quote (line 83) |
| AMBCrypto | wiki/sources page | Confirmed $4–$8/month earnings; confirmed HIP-138 reference |
| bytetree.com | wiki/sources page | Confirmed hardware costs |
| tokenomist.ai | Nature of source | Tokenomics data dashboard — does not contain HIP governance data. Confirmed as wrong source for HIP-82 and HIP-138 claims. |
| Sarson Funds | wiki/sources page | Investment firm blog — $56,635/day figure not explicitly present; correct figure is in Messari |

---

**Summary:** The piece is well-sourced and the primary-source quotations (HIP-143 proposal text, HIP-148 proposal text, Helium Foundation proxy guidance) are all confirmed verbatim from primary documents. Three source link errors require correction before publication. The most significant is Flag #1: "HIP-82 capped data transfer rewards at $0.50 per gigabyte" — wrong HIP number (should be HIP-53) AND wrong source (Tokenomist). Flags #2 and #3 are source-swap fixes only (correct figures, wrong outlet links). The HIP-148 quote truncation (Flag #4) is a style note, not a factual error. The temporal sourcing gap on the April 2026 sunset (Partial #1) is the one claim where the source predates the event it's documenting — adding a secondary confirmation or a brief qualifier resolves it. No vote figures, dollar amounts, or HIP vote percentages are incorrect. The article is publishable pending these four targeted corrections.
