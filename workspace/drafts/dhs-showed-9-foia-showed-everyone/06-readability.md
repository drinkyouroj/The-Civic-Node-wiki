# Readability Report

**Draft:** "DHS Showed 11%. FOIA Showed Everyone."
**Apparent reader load:** Medium-high — political accountability + legal mechanics (Touhy, Supremacy Clause, contempt tools). TCN audience can carry the domain load; the analytical spine is clear. Density is mostly earned. Audit severity calibrated for Marcus: tolerates density that earns its keep, quits on passages that ask him to hold more than he needs to.
**Overall density:** Moderate
**Bottom-line take:** Publishable with three targeted fixes — one critical voice violation ("Draw your own conclusions"), one abstract closer that under-delivers on setup ("The numbers generated the label"), and one clunky sentence that needs a split. Everything else is surface or borderline.

---

## Top Comprehension-Breaking Violations

### 1. §3J / §3H.2 — "Draw your own conclusions." (end of Source Code section)

> "Schiltz threatened criminal contempt. His language: 'ICE is not a law unto itself.' The enforcement continued anyway. Draw your own conclusions."

Why: This is the hardest-working moment in the source code section — 210 documented violations, a federal judge on the record, and the operation kept running. "Draw your own conclusions" evacuates exactly the claim that should land here. It instructs the reader to infer instead of making the claim. For Marcus, this reads as either evasion or AI hedging. Both are wrong.

**Revision (Option A — cut):**
> "Schiltz threatened criminal contempt. His language: 'ICE is not a law unto itself.' The enforcement continued anyway."

**Revision (Option B — make the claim):**
> "Schiltz threatened criminal contempt. His language: 'ICE is not a law unto itself.' The enforcement continued anyway. Schiltz had documented 210 violations. None of them had stopped an arrest."

Option A is cleaner. Option B is appropriate if you want to close the section with the count rather than leaving it hanging from the contempt-threat paragraph. Your call on which punch lands harder.

---

### 2. Audit 2 + §3H.2 + §3J — "Each element of that definition came from an operational metric already in evidence. The numbers generated the label." (Source Code, P5 — Enforcement Theater paragraph)

> "Enforcement theater is what this category of output is called: maximum visibility, minimum precision, structural insulation from external review. Each element of that definition came from an operational metric already in evidence. The numbers generated the label."

Why: The paragraph worked hard to establish "enforcement theater" from the data. Then it closes with two abstract pointing sentences that don't name the mapping. "The numbers generated the label" is §3H.2 applied to data — it asserts the move happened without showing it. The reader already has all three numbers in the preceding paragraph; they just need the writer to close the loop explicitly.

**Revision:**
> "Enforcement theater is what this category of output is called: maximum visibility, minimum precision, structural insulation from external review. The 97% street arrests are the visibility. The 63% no-record is the precision. The 11%/89% gap between what DHS published and what FOIA showed is the insulation."

This trades two vague closing sentences for three short, mapped ones. The reader now has a named correspondence, not an instruction to derive one themselves.

---

### 3. Audit 5 — Double preposition construction (§4, My Debug, P5)

> "The move to Michigan was the second kind: a logistics decision made under fear of a government that had started to look like something to stay out of the sightline of."

Why: "Something to stay out of the sightline of" — two trailing prepositions create comprehension drag at the sentence's end. The reader has to parse "sightline of" before they realize they've reached the sentence's end. Structural, not stylistic.

**Revision:**
> "The move to Michigan was the second kind. I left because I wanted to be somewhere harder to find."

Splits the compound sentence, names the actor (I), uses active verbs (left, wanted), cuts the preposition pile. The honesty of the preceding sentences carries the emotional weight; this just needs to close cleanly.

---

## Cumulative Drag

- **Three consecutive "mechanism → limit" paragraphs in §3 (The Upgrade)**: Touhy (no law compels disclosure → DHS self-certified out) → contempt (two tools → both have ceilings) → Supremacy Clause (lever the president can't reach → immunity doctrine complicates it). Each follows the same argumentative shape: introduce mechanism, explain how it works, name its limit. By paragraph 3, Marcus has detected the formula and may start skimming. **Recommendation:** vary the opening construction of one of the three. Currently all open with either "There's no..." or "[named actor] has..." The contempt paragraph (P4) opens most abstractly — "Schiltz has two enforcement tools" — and is the best candidate for restructuring to break the shape, perhaps by opening with the Arpaio example rather than the category.

- **Stat cluster 25%/13%/63%/97% in Source Code P2**: The first three percentages decompose the arrested population and complete a 100% accounting. The pivot to 97% (method of arrest, not criminal history) is abrupt — the reader has been tracking "what kind of record" and suddenly gets "how they were arrested" without a bridge. **Recommendation:** Add one bridging sentence between the population breakdown and the method-of-arrest figure. Something like: "The arrest method is a separate tell." then the 97% stat. Not required; worth 15 words.

---

## Surface Drag

- **"Drury" without context marker** (§3, Upgrade, Supremacy Clause paragraph): "*Horiuchi* (Ruby Ridge)" gets a parenthetical; "*Drury*" gets nothing. TCN readers know Ruby Ridge but not every federal qualified immunity case. Add a 3-word context: "*Drury* (Ninth Circuit, 2000)" or "*Drury* (off-duty officer)" — whichever detail is actually load-bearing for the argument.

- **"habeas filings" without gloss** (Source Code, P4): "Habeas filings confirmed 273 valid work-permit holders detained" — the reader gets the implication from "confirmed detained" but a brief gloss earns the term for later use: "habeas filings (emergency legal challenges to detention)" or simply "habeas petitions filed by detainees." One parenthetical.

---

## Borderline — Your Call

- **"That's a sentence I wouldn't have believed I'd write a decade ago."** (§4, end of P5) — Close to §3H.2 pointing-and-labeling. But in a personal reflection section, self-commentary on your own situation reads as human register, not AI hedging. The §3H.2 carve-out applies: "a brief deictic landing IS sometimes the right move." Apply the litmus: if deleted, does the prose lose information? The prior sentence already carries the weight; this one adds emphasis. Borderline. Keep if it feels true; cut if you'd rather the prior sentence land directly.

- **Source Code P5 (Enforcement Theater) at ~95 words**: Under the 120-word flag threshold. Dense but every sentence is doing work. Not a hard flag.

- **Upgrade P5 (Supremacy Clause) at ~115 words**: Near the threshold, and the paragraph is doing multiple legal moves simultaneously (lever/state conviction → Supremacy Clause immunity doctrine → Horiuchi/Drury cases that defeat it). Technically borderline but the sentence-level mechanics work. If you want to trim, the Horiuchi/Drury case citation could be promoted to its own short paragraph ("Two cases can defeat it: *Horiuchi* and *Drury*. Both hold that when the facts of the officer's use of force are genuinely disputed, immunity doesn't automatically attach at the pretrial stage.") — that gives the case law its own breathing room and breaks the density.

---

## What's Working

The 71%/11% pivot paragraph ("DHS showed you the top 11%. The FOIA data shows you everyone.") is the cleanest analytical moment in the draft — short, declarative, earned. The contempt paragraph (Schiltz, civil vs. criminal contempt, Arpaio) is exceptionally well-grounded legal explanation without any jargon drag. The §3 two-sentence compression ("Minnesota's evidence request went to the same agency whose agent fired the gun. The agency decided what the state would receive.") is doing exactly what it should. The closer (Minneapolis/Good family/ICE receipt) completes the invoice metaphor with named actors and active verbs throughout. The §4 personal reflection is honest and properly calibrated — the "close enough / far enough" distinction is doing real work.
