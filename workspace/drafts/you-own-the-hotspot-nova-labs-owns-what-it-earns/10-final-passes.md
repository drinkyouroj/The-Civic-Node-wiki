# Step 10: Final Readability + Humanizer Pass

**Draft:** `07-humanized.md` (post-reconcile, post-HIP-53 URL fix)
**Date:** 2026-05-19

---

## tcn-readability — Final Pass

**Apparent reader load:** Medium-high. Same as Step 6 assessment — DePIN governance niche, anchored in hardware costs, vote percentages, dollar figures. Density is earned.
**Overall density:** Moderate. Unchanged from Step 6.
**Bottom-line take:** Clean. No issues introduced by the fact-reconcile changes.

### Changed Passages Audited

**Source Code ¶1 (after HIP-82→HIP-53 + text change):**

> Three rule changes shaped the network before either of those votes landed. [HIP-53] set the data transfer rate at $0.50 per gigabyte. [HIP-138] consolidated the IoT and Mobile subnetwork tokens into a single HNT in January 2025. The [August 2025 halving] cut new emissions in half. Each change had its own stated rationale. All three had a defensible rationale at the time.

- Paragraph length: ~55 words. ✓
- Rhythm: Six sentences ranging 7–16 words. Varied. ✓
- Statistics grounded: $0.50/GB embedded in HIP-53 sentence (evidence of what HIP-53 did). ✓
- Abstraction: "Each change had its own stated rationale" followed immediately by "All three had a defensible rationale at the time." — two short sentences in close succession with similar structure. This was flagged as borderline in Step 6 and retained as the "charitable reading" close. No change in assessment. ✓

**Source Code ¶2 (after $56,635 source swap — text unchanged):**

> The revenue split is where the rationales run dry. The IoT side of the network, all 385,000 hotspots, generates [$124.77 per day in actual data transfer revenue]. The Mobile side, routing carrier offload traffic for T-Mobile and AT&T, generates [$56,635 per day]. One half of the network is the revenue. The other half is the hardware that gives the project something to point at.

- No text changed. Source link only. ✓

**Source Code ¶5 (after HIP-148 quote ellipsis):**

> "To simplify technical implementation, we propose to emit the full allocation available from Service Provider Rewards and Oracle Operator Rewards to the single Service Provider Nova Labs..."

- Ellipsis notation is correct. The sentence now reads naturally — the `...` signals truncation without stopping the paragraph's momentum. ✓

**Source Code ¶9 (after dual-link on sunset):**

> In April 2026, [the HIP-143 sunset expired] with [no replacement vote filed]. The [Helium Foundation's own guidance] recommends that operators "set a proxy as a backup to ensure you don't miss out on rewards." Ferebee and Nova Labs were the proxies most operators were pointed toward. Both had been accumulating.

- Two linked clauses in the first sentence. Reads cleanly — the linked phrases are natural chunks of the sentence, not awkward anchor text. ✓
- No new density issues. ✓

### Full Re-Check (Unchanged Sections)

All five audits against the full draft:

| Audit | Finding |
|---|---|
| 1. Paragraph length | All paragraphs within 40–100 word range. Source Code ¶5 (~98 words) justified by block quote. My Debug ¶4 (~93 words) is the one borderline — unchanged from Step 6, acceptable given density is earned. |
| 2. Touch ground within three | Every abstract claim grounds within three sentences throughout. Opener grounds in ¶1 (hardware cost, earnings figures). Each body section grounds immediately on entry. ✓ |
| 3. Statistics in causal chains | All 12+ statistics embedded in mechanisms or consequences. None naked. ✓ |
| 4. Reader address | "You" appears once in The Upgrade ("You're buying a revenue-share position..."). Single approved instance. ✓ |
| 5. Anaphora vs. AI rule-of-three | The Upgrade's four disclosure paragraphs open with compound noun phrases (written floor / aggregate disclosure / geographic acknowledgment / sunset provisions). Parallel four times — deliberate list structure, not AI default-three. Length variation (68/28/65/36 words) prevents flat rhythm. ✓ |

**Voice canonical §3A–§3J re-check (changed passages only):**
- "set the data transfer rate" — not on §3A banned list; not a dead phrase; not a vocabulary cliff for this audience. ✓
- "no replacement vote filed" (as linked anchor text) — plain, specific, accurate. ✓
- No em dashes introduced. ✓
- No negative parallelisms introduced. ✓
- No closing-line abstraction. Final line ("does the math before the hardware ships") is a concrete action by a named actor class. ✓

**Readability verdict:** No issues. Ready.

---

## tcn-text-humanizer — Final Pass

**Scope:** Audit the text changes introduced since Step 7. All text unchanged from 07-humanized.md is already cleared; this pass covers only the fact-reconcile text modifications.

### Changed Text Audited

**"HIP-53 set the data transfer rate at $0.50 per gigabyte."**

- §3A banned vocabulary: none. ✓
- §3B dead phrases: "set" is a direct verb; "data transfer rate" is technical vocabulary appropriate for this audience. Not a dead phrase. ✓
- §3F negative parallelism: not present. ✓
- §3G tribal cringe: "data transfer rate" is operational vocabulary for DePIN audience, not shibboleth. ✓
- §3I vocabulary cliff: "data transfer rate" is self-evident; no gloss needed for this audience. ✓
- Rhythm: 11 words, single clean clause. Fits the surrounding short-sentence pattern. ✓
- Voice: dry, specific, factual. Sounds like a governance cite, which is what it is. ✓

**"...to the single Service Provider Nova Labs..." (ellipsis notation)**

- Not a prose voice issue; quote notation. ✓

**"with [no replacement vote filed]" (added link)**

- Prose quality unchanged. The linked text reads naturally in context. ✓

### Full Draft Voice Re-Confirmation

No §3A–§3J patterns found in changed passages. The phrase "set the data transfer rate" is the one new phrase; it passes all checks. The rest of the draft was cleared in Step 7 and is unchanged.

**One phrase to note (not a flag — confirming the Step 7 judgment holds):** "set the data transfer rate at $0.50 per gigabyte" is slightly more clinical than the original "capped data transfer rewards" — but the correction was factually necessary (HIP-53 set a rate, not a cap on rewards), and the technical phrasing fits Source Code ¶1's analytical register. The voice canonical's §3I meaning-preservation sub-principle applies: accuracy to the source wins over colorful but wrong phrasing.

**Humanizer verdict:** No changes needed. Draft is in Justin's voice throughout.

---

## Summary

Both passes clean. The draft is publication-ready. Final article in `10-final.md`.

**Inline source link count (final):** 20
- Two links were added vs. the original 18: (1) second Messari link for $56,635 (swapped from Sarson Funds, same count slot); (2) GitHub HIP repo link on "no replacement vote filed" (net new). The HIP-53 URL update (indirect → direct) is a link change, not a count change.

**Word count:** ~1,535 (within the 1,500–1,600 word target).
