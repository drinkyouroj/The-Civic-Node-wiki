# Fact Check Report: "DHS Showed 11%. FOIA Showed Everyone." — Iteration 2

**Iteration:** 2 (draft `05-draft-v4.md`)
**Focus:** the 3 source SWAPS the reconcile introduced (CBS, ProPublica, State Court Report) — new source↔claim pairings iteration 1 never checked — plus re-confirmation that iteration-1 corrections held.
**Claims extracted:** ~30 (unchanged draft body; only the 5 corrected lines + 3 swapped links differ from v3)
**Verified:** 28 | **Flagged:** 2 (1 MED, 1 LOW) | **Unsourced:** 0 | **Wiki/source divergence:** 0
**Link health:** Wikipedia live-fetched 200 OK (used to verify the Good-shooting details); 10 other URLs are ingested wiki sources matching their `source_url`.

---

## Bottom line

Much cleaner than iteration 1 — the denominator/attribution fixes all held, and 2 of the 3 source swaps verify clean. The loop caught exactly one real thing: **the CBS swap (§1) is too thin.** CBS's wiki record confirms the core (Good, U.S. citizen, shot by ICE agent Jonathan Ross) but not the two vivid details the sentence carries ("through her windshield," "after dropping her child at school"). I live-verified those details against the Wikipedia "Killing of Renée Good" article — which is an ingested wiki source — so the fix is a one-line link swap, no new sourcing needed. One LOW item on the §3 enumeration. After those, the piece is factually clean.

---

## Flagged Claims

### Claim #1 [MED]: §1 Good-shooting link (CBS) doesn't carry the vivid details

**Article says (§1):** "Two dead U.S. citizens: [Renée Good](cbsnews.com…), shot through her windshield by ICE agent Jonathan Ross after dropping her child at school, and Alex Pretti."

**Source (CBS wiki record) says:** "ICE agent Jonathan Ross fatally shooting Renée Good, a 37-year-old U.S. citizen, in south Minneapolis on January 7, 2026." Note on the page: *"Lightweight ingest. Initial breaking news; for full detail see the Wikipedia article."* The CBS record confirms Ross + citizen + shooting, but **does not contain** "through her windshield" or "after dropping her child at school."

**Discrepancy:** The reconcile swapped this link off the Substack and onto CBS — but CBS (as ingested) is a thin breaking-news stub that doesn't carry the two details that make the opener land. Linking vivid specifics to a source that doesn't state them is the exact failure the fact-check guards against.

**Resolution — live-verified:** I fetched the Wikipedia "Killing of Renée Good" article (live, 200 OK) and confirmed both details verbatim:
- *"Ross fired the first shot at the SUV's windshield and the second and third shots through the driver's side window."* → "shot through her windshield" ✓
- *"she had just dropped her son off at school … and was on her way home."* → "after dropping her child at school" ✓
- Also confirmed live: U.S. citizen ✓, Jonathan Ross ✓, and the FBI reversal (see Claim context below).

**Recommendation:** Swap the §1 link from CBS to the **Wikipedia "Killing of Renée Good"** page (`https://en.wikipedia.org/wiki/Killing_of_Ren%C3%A9e_Good`) — already an ingested wiki source, and the comprehensive, heavily-cited record the CBS note itself points to. Tier trade-off noted: CBS is Tier-2, Wikipedia is Tier-3 tertiary, but the litmus is "does the source contain the claim," and only Wikipedia (live-verified) does for this detail bundle. (CBS stays in the wiki, just unlinked.)

---

### Claim #2 [LOW]: §3 enumerated evidence seizure is broader than the linked source states

**Article says (§3):** "The FBI reversed course. It took exclusive control of the car, the forensic evidence, and the witness interviews, and locked Minnesota out without explanation."

**Source (ProPublica wiki record) says:** "After initial agreement to cooperate following Good's shooting, federal government reversed course… The federal government has refused to cooperate with state law enforcement." Wikipedia (live) confirms: "the FBI had revoked their access to evidence of the shooting, reversing an earlier agreement that a joint investigation would be undertaken."

**Discrepancy:** The FBI **reversal and evidence lockout** are solidly verified (ProPublica + Wikipedia, live). The specific **three-item enumeration** — "the car, the forensic evidence, and the witness interviews" — traces to the synthesis / the (now-unlinked) Frozen Accountability report, not to ProPublica's general "refused to cooperate / revoked access to evidence." The enumeration is true and well-documented; it's just more granular than the linked source states.

**Recommendation (keep or soften — your call, LOW):**
- Keep as-is: the enumeration is accurate and corroborated across the synthesis + Frozen Accountability; ProPublica/Wikipedia confirm the lockout it specifies. Defensible.
- Or generalize to match the linked source exactly: "It revoked Minnesota's access to the evidence and locked the state out without explanation." Loses the vivid three-item list; gains exact link-source fidelity.

I lean **keep** — the detail is true, and the §3 link's job (the FBI reversal) is fully verified. Flagging only for completeness.

---

## Verified — the swaps that held + iteration-1 corrections re-confirmed

| Claim | Source (swapped/corrected) | Status |
|---|---|---|
| FBI initially agreed to partner, then reversed course | ProPublica (record) + Wikipedia (live): "reversing an earlier agreement that a joint investigation would be undertaken" | ✓ |
| Supremacy Clause immunity shields federal officers from state prosecution for on-duty acts; *Horiuchi* (Ruby Ridge) + *Drury*/1906 PA soldiers defeat it on disputed facts | State Court Report (record): Neagle origin, "necessary and proper," four exceptions incl. 1906 PA soldiers case + Ruby Ridge 9th Cir. | ✓ |
| 71% = 124 of 174 metro-slice names (not all 335, not all arrested) | Davidson: "124 flagged for Violent & Sexual Offenses (71%)" of 174 | ✓ (corrected in v4) |
| 335 names ≈ 11% of the 3,000 DHS claimed; under 9% of 3,789 | Davidson "≈11%"; 335/3,789 = 8.8% | ✓ (corrected in v4) |
| "The claim: 3,000 … arrested in six weeks" | DHS release: "in the last 6 weeks … arrested 3,000" | ✓ (corrected in v4) |
| Touhy "built on the Housekeeping Statute at 5 U.S.C. §301" | Touhy concept: "read together with… §301" | ✓ (corrected in v4) |
| "an ICE and CBP operation" (National Guard removed) | entity: 2,000 ICE + 1,000 CBP | ✓ (cut in v4) |

All other claims (the $203.1M breakdown, $240M/$610M, 3,789/<25%/13%/63%/97%, the 96→210 court-order count, Arpaio/contempt mechanics, Touhy "doesn't apply"/AG "no lawful basis," Moriarty/Morgan) were verified in iteration 1 and are byte-identical in v4 — no re-drift possible.

---

## Link Health

| URL | Status | Note |
|---|---|---|
| en.wikipedia.org/wiki/Killing_of_Renée_Good | 200 OK (live-fetched) | Verified the Good-shooting detail bundle; recommended as the §1 link |
| cbsnews.com (Good shooting) | ingested wiki source | Too thin for the §1 detail bundle → recommend unlinking (Claim #1) |
| propublica.org (Minnesota legal battle) | ingested wiki source | Confirms §3 FBI reversal ✓ |
| statecourtreport.org (When Can States Prosecute) | ingested wiki source | Confirms §3 Supremacy Clause doctrine ✓ |
| law.cornell.edu/supremecourt/text/340/462 | raw stub (created v4) | Touhy doctrine primary; still needs ingestion before publish |
| ag.state.mn.us, mprnews.org, dhs.gov, northernnewsnow.com, minnesotareformer.com (×2), courtlistener.com, notus.org | ingested wiki sources | Verified in iteration 1 |

---

## Summary

Iteration 2 converges the loop. The five iteration-1 corrections all held with no re-drift, and 2 of the 3 source swaps verify clean (ProPublica for the FBI reversal, State Court Report for the Supremacy Clause doctrine). The one real catch is the CBS swap (§1): a thin breaking-news stub that doesn't carry the opener's vivid details — fixed by re-pointing to the Wikipedia "Killing of Renée Good" article, which I live-verified contains every detail and is already in the wiki. One LOW item (§3 enumeration) is the writer's call. **After the §1 link swap, the piece is factually clean.** No wiki re-ingestion needed (no divergences); the only outstanding housekeeping is ingesting the Cornell LII Touhy stub before publish.

**Recommended next:** run tcn-fact-reconcile to (a) swap §1 CBS → Wikipedia "Killing of Renée Good," (b) apply your call on the §3 enumeration → produces `05-draft-v5.md`. Then the loop exits clean (the only iteration-2 flag is resolved by the swap; nothing would carry to an iteration 3).
