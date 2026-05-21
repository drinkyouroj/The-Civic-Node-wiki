# Fact-Reconcile Notes — Iteration 1

**Source draft:** `07-humanized.md`
**Applied:** 2026-05-19
**Based on:** `08-fact-check.md` (Iteration 1)

## Changes Applied

| Flag | Location | Change |
|---|---|---|
| #1 Required | Source Code ¶1 | "HIP-82" → "HIP-53"; claim text "capped data transfer rewards" → "set the data transfer rate"; source link Tokenomist → HIP-143 GitHub |
| #2 Required | Source Code ¶2 | $56,635/day source link: Sarson Funds → Messari Q4 2025 |
| #3 Required | Source Code ¶1 | HIP-138 source link: Tokenomist → AMBCrypto |
| #4 Style | Source Code ¶5 | HIP-148 quote closing period → ellipsis: `"...Nova Labs."` → `"...Nova Labs..."` |
| Partial #1 Option A | Source Code ¶9 | Added second link: "no replacement vote filed" → `https://github.com/helium/HIP` |

## Notes on Flag #1

The HIP-53 link currently points to the HIP-143 GitHub page (`https://github.com/helium/HIP/blob/main/0143-decoupling-service-provider-pricing-from-governance.md`), which explicitly cites HIP-53 as defining the $0.50/GB rate at line 21: "The nominal cost of data remains at $0.50/GB as defined in HIP-53."

This is the best available source in the wiki. The direct HIP-53 URL (e.g., `https://github.com/helium/HIP/blob/main/0053-[filename].md`) was not verified in this session. **Before final publish: look up the HIP-53 filename in the helium/HIP GitHub repo and update the link.** The HIP-143 link is defensible as an interim source.

## Claim Text Change (Flag #1)

The original claim said "capped data transfer rewards at $0.50 per gigabyte." The HIP-143 raw file describes HIP-53 as setting "the nominal cost of data" — which is the per-GB pricing mechanism, not specifically a cap on operator rewards. "Set the data transfer rate" more accurately reflects the source language.

## Outcome

All three required source corrections applied. Style fix applied. Option A dual-sourcing applied for the sunset claim. Draft ready for second fact-check pass.
