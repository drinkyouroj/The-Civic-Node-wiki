# Readability Report

**Draft:** "You Own the Hotspot. Nova Labs Owns What It Earns." (`05-draft-v1.md`)
**Apparent reader load:** Medium-high. DePIN governance is a niche domain, but the piece is anchored throughout in hardware costs, dollar figures, and vote percentages that any financially literate reader can process. The piece earns its density.
**Overall density:** Moderate — well within range for TCN's audience, but one hard rule violation runs through the entire piece.
**Bottom-line take:** Publishable with one systematic fix (em dashes, hard rule §2) and two targeted sentence-level rewrites. No structural passes needed.

---

## Top Comprehension-Breaking Violations

### 1. Em dashes — systematic throughout (~10 instances) — **HARD RULE violation §2**

The voice canonical explicitly bans em dashes: "NO em dashes. AI overuses them. Use commas, periods, colons, semicolons, or parentheses." The draft uses them approximately 10 times, mostly as inline-gloss markers and parenthetical asides.

**Why:** §2 hard rule. No exceptions.

**Systematic rewrites — all instances:**

*The Glitch ¶3:*
Before: `After the [August 2025 halving] — the algorithmic cut that reduced new HNT (Helium's native token) emissions from 15 million per year to 7.5 million — a well-placed urban hotspot [earns $4 to $8 a month].`
After: `After the [August 2025 halving] (the algorithmic cut that took new HNT (Helium's native token) emissions from 15 million per year to 7.5 million), a well-placed urban hotspot [earns $4 to $8 a month].`

*The Glitch ¶4:*
Before: `Helium is a DePIN project — decentralized physical infrastructure networks, where independent operators deploy hardware that earns token rewards for coverage the network provides.`
After: `Helium is a DePIN project (decentralized physical infrastructure networks, where independent operators deploy hardware that earns token rewards for coverage the network provides).`

*The Source Code ¶2:*
Before: `The IoT side of the network — all 385,000 hotspots — generates [$124.77 per day in actual data transfer revenue].`
After: `The IoT side of the network, all 385,000 hotspots, generates [$124.77 per day in actual data transfer revenue].`

*The Source Code ¶4:*
Before: `HIP-143 passed 90.53% on 763 million veHNT cast — vote-escrowed HNT, the staked governance token that determines voting weight.`
After: `HIP-143 passed 90.53% on 763 million veHNT cast (vote-escrowed HNT, the staked governance token that determines voting weight).`

*The Source Code ¶5:*
Before: `It eliminated Mobile Mapping rewards — the 20% of HNT emissions that subscribers had been earning by sharing location data from their phones.`
After: `It eliminated Mobile Mapping rewards, the 20% of HNT emissions that subscribers had been earning by sharing location data from their phones.`

*The Source Code ¶8:*
Before: `ferebee's veHNT holdings grew from 183.85 million to 285.92 million] — up 55.5% in six months.`
After: `ferebee's veHNT holdings grew from 183.85 million to 285.92 million], up 55.5% in six months.`

*The Upgrade ¶3 (disclosure 1):*
Before: `A written floor on what triggers a material change to the reward structure, plus an operator right to exit at that floor — a hardware buyback, migration provision, or refund of residual.`
After: `A written floor on what triggers a material change to the reward structure, plus an operator right to exit at that floor: a hardware buyback, migration provision, or refund of residual.`

*The Upgrade ¶6 (disclosure 4):*
Before: `The execution gap — nothing requiring a new vote before the authority extended — is fixable.`
After: `The execution gap, where nothing required a new vote before the authority extended, is fixable.`

*My Debug ¶2:*
Before: `Earlier pieces I published on DePIN positioned Datagram as the legitimate counter-example — the project doing decentralized infrastructure differently.`
After: `Earlier pieces I published on DePIN positioned Datagram as the legitimate counter-example, the project doing decentralized infrastructure differently.`

*My Debug ¶4:*
Before: `The structural problem — governance that lets the proposing entity accumulate authority over time — and the fraud problem share an architecture.`
After: `The structural problem and the fraud problem share an architecture.`
(The parenthetical content about "governance that lets the proposing entity accumulate authority over time" is already established from Section 2; restating it here is redundant and the em-dash form was the only thing making it load-bearing. Cutting it tightens the sentence.)

---

### 2. §3F violation — "The unit economics can stay private. The total revenue split can't." (The Upgrade ¶4)

**Why:** §3F bans any two-sentence pair where the second sentence negates the first's permission. "Can stay private" then "can't" is the two-sentence version of "Not X. Y." The positive claim is "disclose the revenue split." The negation of "can't" adds no information — it just restates the first sentence's implied contrast.

**Revision:**
Before: `The unit economics can stay private. The total revenue split can't.`
After: `The total revenue split gets disclosed, audited annually. The carrier-by-carrier rate sheets stay private.`

The fix reverses the order to lead with the positive claim (what happens), then confirms what doesn't change (carrier rates stay confidential). Both sentences are now positive assertions rather than one permission and one negation.

---

### 3. Section 2 close abstraction — "Most of the proxies available to delegate to were already accumulating." (The Source Code ¶9, final sentence)

**Why:** Borderline §3J (closing-line abstraction). "Proxies" is anonymous at this point; "accumulating" requires the reader to retrieve the ferebee/Nova Labs context from two paragraphs earlier. As the close of Section 2, this is the last thing Marcus reads before the section break — it should land with a name, not a reference.

**Revision:**
Before: `Most of the proxies available to delegate to were already accumulating.`
After: `The two most prominent proxies available for delegation were ferebee and Nova Labs. Both had been accumulating the whole time.`

(Alternatively, if length is tight: `The most-used proxies for delegation were ferebee and Nova Labs — but see above re: em dashes — both of which had been accumulating throughout.` — better written as: `Ferebee and Nova Labs were the proxies most operators were pointed toward. Both had been accumulating.`)

---

## Cumulative Drag

- **Section 2 (Source Code) ¶1–¶4 length run:** Four consecutive paragraphs at 57 / 73 / 57 / 63 words. Range is 16 words; threshold for flagging is 15. Borderline flat. The Keith Rettig two-sentence break at ¶7 provides a strong downstream rhythm reset, and the variation within the four paragraphs is real (the 73-word ¶2 is the noticeable outlier). Recommendation: if any single sentence can come out of ¶2 or ¶4 without losing the argument, remove it. Otherwise this is acceptable given the Keith Rettig break.

- **The Upgrade disclosure paragraphs (¶3–¶6) — same opening construction:** All four disclosure paragraphs open with a compound noun phrase naming the disclosure type ("A written floor," "Aggregate disclosure," "Geographic acknowledgment," "Sunset provisions"). Syntactically parallel four times running. The length variation (72 / 28 / 64 / 38 words) prevents this from reading flat, and the parallelism is intentional (these are items in a list). Recommendation: no change required, but if it reads mechanical in a final read-through, vary the opening of disclosure 3 or 4 (e.g., "Rural coverage and urban carrier traffic are different goods — operators buying in for one shouldn't be surprised to receive the other").

---

## Surface Drag

- **¶S5 (HIP-148 paragraph) word count:** ~108 words, approaching the 120-word ceiling. The length is justified by the block quote from the proposal text, which counts as an allowed exception. No action required, but watch this paragraph in final read-through.

- **¶D3 three "that" clauses stacked:** "Before any hotspot shipped, it would have revealed that pricing authority didn't belong to the operator class, that the reward structure had no exit provisions, and that no audit of the rural/urban split was built into the governance documents." (~38 words, three parallel "that" clauses.) The parallelism is deliberate and does work (it's anaphoric, cataloguing three things the audit would catch). Fine as is. Borderline flag only.

---

## Borderline — Your Call

- **"Present them fairly." (Source Code ¶1, final sentence)** — Self-directed deadpan imperative. Intended as a signal that the charitable reading is done and the audit begins. This is a voice move (Justin talking to himself in a way the reader can see), which fits the TCN register. A cold reader who doesn't know the convention might briefly read it as instructional. If you keep it, no change needed. If you want to remove the ambiguity: "All three had a defensible rationale at the time." That's a flat statement instead of a voice move, which changes the feel. Your call.

- **Stat cluster ¶S6 (eight figures in 67 words):** Every number is embedded in the concentration-grew mechanism (this is the analytical payoff paragraph of Section 2), so technically none are naked. The density is high but earned. No flag required; noted for your awareness in the final read.

- **¶D4 third sentence abstraction:** "The structural problem and the fraud problem share an architecture." (After the em dash fix above, this reads clean as a standalone sentence.) The surrounding sentences ground it: "Datagram" at the start of the paragraph and "twelve nodes without reading the documents" immediately after. The sentence is pure abstraction but is bracketed correctly. Fine as is.

- **"The audit is the floor. It doesn't catch fraud." (The Upgrade, final two lines)** — The second sentence is a negation statement, §3F adjacent. But these two sentences are independent analytical claims, not a corrected-framing pair ("The audit is the floor" is not a misframing of "fraud"; it's a separate claim). The intent-vs-pattern test comes out fine. Keeping these as-is is defensible.

---

## What's Working

The opener is clean and the thesis landing in ¶O3 ("The hardware they paid for is theirs. The pricing authority that determines what their hardware earns is not.") is one of the strongest three sentences in the piece. The Keith Rettig two-sentence paragraph is correctly placed and correctly weighted — "Keith Rettig voted against. He held 1.00% of the total vote." does exactly what it should without commentary. The Section 2 primary-source quotations (both HIP-143 and HIP-148 proposal texts) are introduced cleanly and allowed to land without editorializing after them. The Section 4 correction of the prior Datagram framing is personal, specific, and earns its position. The closing line callback to the opener's payback math is tight.

---

## Summary of Required Fixes

| Priority | Location | Fix |
|---|---|---|
| **Required** | Throughout (~10 instances) | Convert all em dashes per rewrites above (§2 hard rule) |
| **Required** | The Upgrade ¶4 | "Total revenue split gets disclosed... carrier rates stay private." |
| **Required** | The Source Code ¶9 final sentence | Name ferebee and Nova Labs in the closing accumulation sentence |
| **Borderline** | The Source Code ¶1 final sentence | "Present them fairly." — keep or swap for flat statement, your call |
| **Borderline** | The Upgrade ¶3–¶6 | Disclosure paragraph openings — parallel structure, length variation saves it |
