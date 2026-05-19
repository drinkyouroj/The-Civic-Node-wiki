---
title: "Helium HIP-53 Vote Results — Helium Vote"
type: source
tags: [technology, infrastructure, crypto, depin, governance, tokenomics]
created: 2026-05-19
updated: 2026-05-19
sources: 4
raw: "raw/assets/HIP-53 vote results.png"
source_url: "https://heliumvote.com/hnt/proposals/"
author: "@nrnrsdwsrk, @kjake-vmcc, @gabreyem2367, @asknsy, Joey Padden"
published: 2022-07-25
---

[Original source](https://heliumvote.com/hnt/proposals/)

## Summary

Primary-source vote-tally screenshot from the Helium Vote governance portal for HIP-53 (Mobile subDAO). The vote closed July 25, 2022, 11:21 PM. The proposal — which established the MOBILE token and subDAO under the HIP-51 Helium DAO framework and set the data transfer rate at $0.50/GB — passed 97.22% on a total of only 2,438,837.53 veHNT. The very small total network voting power in 2022 is the relevant baseline against which the 2024–2025 concentration story unfolds: the entire HIP-53 network was ~0.3% the size of the HIP-148 voting universe three years later.

## Key Points

**Vote tally:**
- **For HIP 53: 2,371,138.03 veHNT (97.22%)**
- **Against HIP 53: 67,699.50 veHNT (2.78%)**
- Total veTOKENS cast: **2,438,837.53**
- Vote close: **July 25, 2022, 11:21 PM**
- Categories tagged on the proposal: Economic / Technical

**Authors (per proposal header):**
- @nrnrsdwsrk
- @kjake-vmcc
- @gabreyem2367
- @asknsy
- Joey Padden

(Note: Nova Labs is **not** listed as a HIP-53 author. This is the key correction for any article that attributes HIP-53 to Nova Labs.)

**What the proposal did (from the on-portal description):**

> "HIP 53 establishes the MOBILE token and subDAO under the framework established by HIP 51: Helium DAO. In summary, the Helium MOBILE subDAO handles all MOBILE emissions, mining rewards, programmatic treasury, and governance operations for mobile device networks. HNT tokens will be emitted to the MOBILE subDAO treasury as required by HIP 51 and will be used to back the MOBILE token. The MOBILE token will thus always be redeemable for HNT within the Helium ecosystem upon demand through a programmatic treasury controlled by the MOBILE subDAO. Oracles in the MOBILE subDAO will confirm Proof of Coverage, data transfer, and add blocks to the MOBILE subnetwork."

- Establishes the MOBILE token (sub-token redeemable 1:1 for HNT prior to HIP-138).
- Establishes the MOBILE subDAO with its own emissions/treasury/governance scope.
- Sets the data transfer rate baseline at **$0.50/GB** (the rate later preserved by HIP-143 as the nominal anchor against which Nova Labs adjusts the Rewarded/Unrewarded ratio).
- Defers to HIP-51 (Helium DAO) for the overarching DAO structure.

**Why the 2022 baseline matters:**

The total voting power on HIP-53 (2.44M veHNT) is roughly **1/370th** of the voting power on HIP-148 (902.28M veHNT). The network's voting universe grew ~370× between July 2022 and October 2025. Over that same period:
- HIP-138 (Nov 2024) had no single proxy above 15% (anonymous wallet `HKcAP…NqsJ` was the top voter at 15.00% / 72.94M veHNT).
- HIP-143 (Apr 2025) had two named proxies controlling 50% combined (Nova Labs 26%, ferebee 24%).
- HIP-148 (Oct 2025) had two named proxies controlling 57% combined (ferebee 31%, Nova Labs 26%), with a third labeled proxy (Jay M.) at 5%.

The 2022 vote does not have a published voter breakdown in the same format as the 2024–2025 votes (the portal does not show a top-voters table for HIP-53 in the captured screenshot). What it provides is the baseline: a network where the *entire* voting universe was 2.4M veHNT, and the concentration story had not yet started.

## Newsletter Angles

- **The Mobile subDAO was the precondition for everything that followed.** HIP-53 created the substrate that HIP-143 would later delegate to Nova Labs and that HIP-148 would later consolidate. Without HIP-53, there is no "Service Provider Pool" for HIP-148 to redirect to Nova Labs.
- **Authorship matters.** HIP-53 was authored by a five-person community team that did NOT include Nova Labs as an author. By HIP-143 (Apr 2025), Nova Labs is one of four co-authors. By HIP-148 (Oct 2025), Nova Labs's proxy controls 26% of the vote on a proposal redirecting emissions to itself. The authorship trajectory mirrors the concentration trajectory.
- **The $0.50/GB rate has been the nominal anchor since 2022.** Article-writing implication: when HIP-143 "preserves $0.50/GB" while granting Nova Labs the right to adjust Rewarded vs. Unrewarded ratios, the rate is not actually fixed in operator-economic terms. The unit price is fixed; the share of data that earns the rate is not.

## Entities Mentioned

- [[Helium Network]] — the protocol being governed
- [[Nova Labs]] — NOT a HIP-53 author; relevant only as the entity that later (via HIP-143/148) gained pricing and emissions authority over what HIP-53 created
- Joey Padden — named HIP-53 co-author; relationship to Nova Labs or other later-period proxies not documented in this source

## Concepts Mentioned

- [[DePIN]] — Helium is the canonical DePIN case study; HIP-53 is the moment the Mobile subDAO substrate is created
- [[Tokenomics]] — the MOBILE token + 1:1 HNT redemption mechanism is the precursor to HIP-138's "Return to HNT" consolidation

## Notes

Primary source: one PNG screenshot of the Helium Vote portal preserved at `raw/assets/HIP-53 vote results.png`. The vote portal is JS-rendered; screenshot captured manually 2026-05-19. The specific heliumvote.com proposal URL is not visible in the screenshot's address bar — the URL fragment for HIP-53 was not captured. This is a minor follow-up: re-capture the URL if a future piece needs the canonical link. The proposal hash from `0053-mobile-dao.md` is the on-chain canonical reference; the portal URL is a UI artifact.

Top-voters breakdown is not visible on the captured screenshot. The portal may not display a top-voters table for HIP-53 (the breakdown view may have been added to the portal between 2022 and 2024). For the present argument — that concentration grew between 2022 and 2025 — the absence of named proxies on HIP-53 is itself the relevant data point: there were no proxies of >15% size yet.
