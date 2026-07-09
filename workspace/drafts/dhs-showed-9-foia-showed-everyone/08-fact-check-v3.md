# Fact Check Report: "DHS Showed 9%. FOIA Showed Everyone." — Iteration 3 (confirming)

**Iteration:** 3 (draft `05-draft-v6.md`) — confirming pass after the headline correction (11% → 9%) and the Cornell LII Touhy ingest.
**Scope:** v6 differs from the already-clean v5 in exactly two ways: (1) three 9%-derived figures replacing the 11% framing, and (2) the Touhy link now resolves to an ingested wiki source instead of a raw stub. Everything else is byte-identical to v5 (verified clean across iterations 1–2). This pass verifies the delta.
**Claims extracted:** ~30 (unchanged); delta = 3 figures + 1 link-status change.
**Verified:** 30 | **Partially verified:** 0 | **Not found in source:** 0 | **Wiki/source divergence:** 0 | **Unsourced:** 0
**Link health:** all 12 distinct URLs resolve to ingested wiki sources. **0 raw stubs remain.**

---

## Bottom line

**Clean.** The headline correction is arithmetically sound, internally consistent, and better-sourced than the 11% it replaced. The Touhy ingest closed the last housekeeping item — every inline link now points to an ingested wiki source. No flags. The loop is closed.

---

## The delta, verified

### 1. The 9% figure (headline + 2 body instances) — derived calculation ✓

**Inputs (both previously verified):** 335 named (Davidson / Northern News Now) ÷ 3,789 arrests (MPR/APM FOIA analysis).

| Where | Article text | Math | Verdict |
|---|---|---|---|
| Headline | "DHS Showed 9%." | 335 / 3,789 = 0.0884 = **8.84% → 9%** (nearest integer) | ✓ |
| §3 disclosure | "335 names: about 9% of the 3,789 arrests the FOIA data documented. DHS showed you the top 9%." | same 335 / 3,789 = 8.84% ≈ 9% | ✓ |
| §3 enforcement-theater close | "The 9% it published, against the 91% it didn't" | published 335/3,789 = 8.84% ≈ 9%; withheld 3,454/3,789 = 91.16% ≈ 91%; **9 + 91 = 100** ✓ | ✓ |

The derived figure passes on all three counts the verification rules require: inputs verified (335 ✓, 3,789 ✓), the math checks (8.84% rounds to 9%), and the rounding doesn't mislead — 9% is the *more conservative* of the two candidate denominators (335/3,789 = 9% uses the hard FOIA total; the prior 11% used DHS's softer self-claimed 3,000). The headline now reconciles with the subhead's own "335 from 3,789." Rounding note: 8.84% → 9% rounds the disclosure rate *up* by 0.16pp, which works marginally against the article's "DHS hid almost everything" thesis, i.e., it is not self-serving rounding.

### 2. The "3,000 claimed" point — still intact, still correct ✓

Removing the dual-denominator hedge from the §3 disclosure sentence did **not** drop the 3,000 figure from the piece. It remains in the charitable-reading paragraph two above ("The claim: 3,000 of them, arrested in six weeks"), verified against the DHS Jan 19 release ("in the last 6 weeks … arrested 3,000"). The 3,000 (DHS's claim) and 3,789 (FOIA total) now do distinct jobs in distinct paragraphs — no conflation.

### 3. Touhy link — now an ingested source, claim re-verified against live ✓

**Article (§3):** "The [Touhy regulations](law.cornell.edu/supremecourt/text/340/462) (from *Touhy v. Ragen*, built on the Housekeeping Statute at 5 U.S.C. §301) let the federal agency head decide what evidence is released to outside parties, including states."

- **Link status:** was a `raw/` stub in v4–v5; now resolves to the ingested wiki source [[Touhy v. Ragen — 340 US 462 (1951) — Cornell LII]] (`source_url` matches; `ingest_method: webfetch`).
- **Claim vs. live source (fetched this session):** Cornell LII opinion — "the Secretary [agency head] … may take from a subordinate all discretion as to permitting records … and reserve for his own determination all matters." → "let the federal agency head decide what evidence is released" ✓. Housekeeping Statute = 5 U.S.C. §301 ✓ (the opinion rests on the predecessor §22, now codified at §301 — the draft's "built on the Housekeeping Statute at 5 U.S.C. §301" is precise).

---

## Everything else: unchanged, no re-drift

The full verified set from iterations 1–2 carries forward byte-identical: the $203.1M breakdown, $240M/$610M, 3,789 / <25% / 13% / 63% / 97%, the 71% = 124-of-174 metro slice, the 96→210 court-order count, the FBI reversal (ProPublica + Wikipedia), the Good-shooting details (Wikipedia, live-verified iteration 2), Arpaio/contempt mechanics, Supremacy Clause + Horiuchi/Drury (State Court Report), Moriarty/Morgan. No sentence carrying these claims changed in v6, so no re-verification gap exists.

---

## Link Health — all green

| URL | Wiki status |
|---|---|
| law.cornell.edu/supremecourt/text/340/462 | **now ingested** (was raw stub) ✓ |
| en.wikipedia.org/wiki/Killing_of_Renée_Good | ingested ✓ (live-verified iter 2) |
| ag.state.mn.us · mprnews.org · dhs.gov · northernnewsnow.com · minnesotareformer.com (×2) · courtlistener.com · notus.org · propublica.org · statecourtreport.org | ingested ✓ |

---

## Summary

Iteration 3 confirms the piece is factually clean. The 9% headline correction is arithmetically sound (335/3,789 = 8.84% ≈ 9%), internally consistent (the §3 "9% / 91%" complement sums to 100), and better-grounded than the 11% it replaced (hard FOIA denominator vs. DHS's self-claim). The Cornell LII Touhy ingest closed the last housekeeping item: all 12 inline links resolve to ingested wiki sources, zero raw stubs remain, zero wiki/source divergences. **The fact-check loop is closed clean (3 iterations: 5 → 1 → 0 flags). The piece is ready for the Step 10 final read-through and publish from a factual-accuracy standpoint.**
