---
title: "Fact Check — The $71 Billion Bluff v11"
type: factcheck
draft: "the-71-billion-bluff-v11.md"
prior_factcheck: "the-71-billion-bluff-v9-factcheck.md"
created: 2026-04-12
claims_checked: 30
confirmed: 26
should_fix: 2
minor_notes: 2
must_fix: 0
---

# Fact Check: The $71 Billion Bluff (v11)

Delta fact-check against v9 report. All five v9 fixes confirmed applied. Verified all new/changed claims and spot-checked previously confirmed claims for staleness. Conducted April 12, 2026.

---

## v9 FIX VERIFICATION — All 5 Applied Correctly

| v9 Issue | Fix Applied in v11 | Status |
|---|---|---|
| MUST FIX #1: "95%" DRAM share | → "over 90%" (both instances, lines 31 + 53) | ✅ Correct |
| MUST FIX #2: CXMT/YMTC "2028" | → "both targeting volume production in 2027 — ramp to market-moving scale" (line 57) | ✅ Correct |
| SHOULD FIX #3: $400 categorical | → "That's what you'll actually pay" (line 21) | ✅ Correct |
| SHOULD FIX #4: "Oracle's financing collapsed" | → "financing terms fell apart and OpenAI's demand projections shrank" (line 41) | ✅ Correct |
| MINOR #5: HP "up from 15%" | → "up from 15-18%" (line 23) | ✅ Correct |

---

## NEW/CHANGED CLAIMS IN v11

### Link swap: $180→$710 now cites PCPartPicker instead of Tom's Hardware

**Draft claim (line 35):** "A 64GB DDR5 kit went from $180 in May to $710 by December — a 294% increase in seven months."
**New link:** https://pcpartpicker.com/trends/price/memory/

**Verdict: ✅ CONFIRMED.** PCPartPicker trend data directly supports the $180→$710 figure for DDR5-5600 64GB kits, May-December 2025. Upgrade from Tom's Hardware (JS-rendered, hard to verify specific historical data points) to PCPartPicker (raw trend data) is a source quality improvement.

---

### Reframed: "Neither supplier knew" → "combined scale only became apparent"

**v9 text:** "Neither supplier knew about the other's deal." (linked to TechCrunch)
**v11 text (line 33):** "The combined scale of the commitment — 40% of the world's DRAM output, locked up by a single buyer — only became apparent once both deals were announced." (linked to TrendForce)

**Verdict: ✅ CONFIRMED — and an improvement.** The original "neither supplier knew" was supported by Moore's Law Is Dead analysis and tech commentary but never by official confirmation from Samsung or SK Hynix. The reframed version states a documented fact (the public 40% figure emerged on announcement day) rather than asserting knowledge asymmetry that no primary source conclusively documents. The TrendForce link supports the 40% figure and the October 2, 2025 timing. More defensible.

---

### Reframed: TBPN from "podcast with 58,000 subscribers" to "tech talk show" + "nine-figure sum"

**v11 text (line 41):** "acquired a tech talk show for a reported nine-figure sum"

**Verdict: ⚠️ SHOULD FIX — "nine-figure sum" is less precise than available reporting.**

- "Tech talk show": ✅ Accurate. TechCrunch, Fortune, PYMNTS, and OpenAI itself describe TBPN as a live daily video show (11 AM-2 PM PT on YouTube/X), not primarily a podcast. "Tech talk show" is more accurate than v9's "podcast."
- "Nine-figure sum": Technically correct ($100M-$999M) but vague. TechCrunch, Fortune, CNBC, and Tech Startups all consistently report "low hundreds of millions." The v9 phrasing ("a reported sum in the low hundreds of millions") was more precise. "Nine-figure sum" could mean anything from $100M to $999M — "low hundreds of millions" narrows it to ~$100-300M.
- Dropping the 58K subscriber detail: Fine editorially. The detail was accurate (confirmed by TechCrunch) but not essential to the argument.

**Suggested fix:** "acquired a tech talk show for a reported low-hundreds-of-millions" or restore "for a reported sum in the low hundreds of millions."

---

## NEW ISSUE SURFACED BY SPOT-CHECK

### $1.4T → $600B framing: comparing different metrics

**Draft claim (appears twice — lines 21 + 41):** "OpenAI cut its spending target from $1.4 trillion to $600 billion — a 57% reduction" / "OpenAI had cut its compute spending target from $1.4 trillion to $600 billion"

**Cited source:** Futurism

**What deeper reporting shows:**
- **$1.4 trillion** = CAPEX commitment (2025-2032/33), includes OpenAI + partner investments (Azure, AWS, Oracle, CoreWeave)
- **$600 billion** = Compute spend (OPEX, 2026-2030), OpenAI's own compute costs
- These are different categories (CAPEX vs compute/OPEX) and different time horizons

**Mitigating factor:** CNBC, Futurism, DCD, ZeroHedge, and virtually every major outlet framed this identically — as a cut from $1.4T to $600B. The article follows the prevailing media framing. A Substack deep-dive (FundaAI) flagged the definitional mismatch, but mainstream reporting does not distinguish.

**Verdict: ⚠️ SHOULD FIX — low urgency, but worth noting.**

The article is following standard media framing, which is defensible for a general audience. However, since this piece's central thesis is about how surface-level signals mislead markets, getting caught making the same apples-to-oranges comparison the media makes would undercut the piece's authority with informed readers.

**Suggested fix options (pick one):**
- Simplest: "OpenAI slashed its spending ambitions from $1.4 trillion to $600 billion" (avoids claiming they're the same category)
- More precise: "OpenAI told investors its compute target was $600 billion — a dramatic retreat from the $1.4 trillion infrastructure commitment it had been touting"
- Leave as-is with acknowledgment that this follows mainstream framing (acceptable if you don't want to relitigate definitions)

---

## MINOR NOTES (2)

### Samsung Q1 2026 figures are preliminary guidance, not final earnings

**Draft claim (line 45):** "Samsung posted Q1 2026 operating profit of 57.2 trillion won..."

Samsung's Q1 2026 final earnings call is April 30. The 57.2T won figure is preliminary guidance released April 6-8. The numbers are unlikely to change materially (Samsung guidance is typically accurate within 1-2%), but technically the article should say "Samsung guided" or "Samsung estimated" rather than "Samsung posted." In practice, media universally reports preliminary Samsung guidance as fact, so this is standard. Not a fix, just a note.

### LOIs confirmed abandoned — strengthens the article's thesis

Spot-check found reporting (PixelRTX, April 2026) that OpenAI terminated its SK Hynix LOI commitment by late March 2026. The article already describes the LOIs as "by all functional measures, abandoned" (line 41), which is accurate and conservative. The newer reporting confirms this characterization. No fix needed — if anything, the article could be more assertive.

---

## PREVIOUSLY CONFIRMED CLAIMS — SPOT-CHECK RESULTS

| Claim | Spot-Check | Status |
|---|---|---|
| Samsung Q1 2026: 57.2T won, 8.5x YoY, chip div 95% | No contradicting data; final earnings April 30 | ✅ Holds |
| OpenAI $1.4T → $600B cut | No newer updates post-Feb 2026 | ✅ Holds (see framing note above) |
| Micron exited Crucial | No reversal | ✅ Holds |
| Half of US data centers delayed/cancelled | Sightline says 30-50%; "half" is high end of range | ✅ Holds |
| Samsung/SK Hynix LOIs abandoned | Confirmed by April 2026 reporting | ✅ Holds (strengthened) |

---

## ALL CLAIMS STATUS

### Confirmed Clean (26)

All 24 claims confirmed in v9 fact-check remain valid. Plus:
- PCPartPicker $180→$710 link: ✅ Confirmed
- Reframed supplier awareness claim: ✅ Confirmed (improved)

### Should Fix (2)

1. **TBPN "nine-figure sum"** — technically correct but less precise than available reporting ("low hundreds of millions"). Low impact on article argument.
2. **$1.4T → $600B framing** — follows mainstream media framing but compares CAPEX (with partners, 2025-2032) to compute OPEX (2026-2030). Defensible but could undercut credibility with informed readers given the article's thesis about misleading signals.

### Must Fix (0)

No must-fix issues. All v9 must-fixes were resolved.

---

## MATH CHECK — All Pass (unchanged from v9)

| Calculation | Check | Result |
|---|---|---|
| $180 → $710 increase | (710-180)/180 | 294.4% ✅ |
| $1.4T → $600B reduction | (1400-600)/1400 | 57.1% ✅ |
| 900K / 2.2M capacity share | 900/2200 | 40.9% ✅ |
| 57.2T KRW → USD | 57.2T / ~1508 | $37.93B ≈ $37.92B ✅ |

---

## SOURCE TIER AUDIT

| Tier | Count | Notes |
|---|---|---|
| Tier 1-2 | 24 | +1 (PCPartPicker swap from TH) |
| Tier 3 | 4 | WCCFTech ×4 (citing KED; best English source) |
| Tier 4 | 0 | — |

No tier regressions from v9.

---

## SUMMARY

| Category | Count |
|---|---|
| Must fix | 0 |
| Should fix | 2 (TBPN price precision; $1.4T/$600B apples-to-oranges) |
| Minor notes | 2 (Samsung preliminary earnings; LOI abandonment confirmed) |
| Confirmed clean | 26 |
| Math errors | 0 |
| Unsourced claims | 0 |
| Source tier violations | 0 |

**Overall assessment:** v11 is significantly cleaner than v9. All mandatory fixes applied. The two remaining should-fixes are low-impact — one is a precision issue on a parenthetical detail (TBPN price), the other is a framing choice shared by every major outlet that covered the story. Neither would be a credibility risk for most readers, though the $1.4T/$600B issue could matter to the finance-literate audience this piece targets.
