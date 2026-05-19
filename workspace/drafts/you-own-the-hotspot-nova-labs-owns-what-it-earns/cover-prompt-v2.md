# Cover Prompt v2 — You Own the Hotspot. Nova Labs Owns What It Earns.

**Date**: 2026-05-19
**Article**: `10-final.md`
**Source template**: [Encyclopedic 3D Infographic Evolution Chart (#4847)](https://youmind.com/nano-banana-pro-prompts?id=4847)
**Aspect ratio**: 16:9 (1456 × 816) — native Substack cover dimension
**Subject (from prompt selection)**: HIP governance documents as the "evolving product"
**Palette (from prompt selection)**: Monochrome industrial — cream / black / charcoal + restrained desaturated red (#9B2C2C) reserved for proxy-concentration data

---

## Corrections applied from v1 → v2

After cover v1 was drafted, primary-source heliumvote.com screenshots for HIP-53, HIP-138, HIP-143, and HIP-148 were obtained. The v1 cover contained the following factual errors, now corrected in v2:

1. HIP-53 date `May 12, 2022` → **`July 25, 2022`**
2. HIP-53 framing "data transfer rate set" → **"Mobile subDAO established; $0.50/GB rate set within"**
3. HIP-53 author "Nova Labs" → **"Joey Padden et al."** (multi-author, not Nova Labs)
4. HIP-138 date `January 15, 2025` → **`November 22, 2024`** (migration completed Jan 2025)
5. HIP-138 title added: **"Return to HNT"**
6. HIP-143 author "Nova Labs" → **"Inversion Capital, zer0tweets, Nova Labs & ferebee"** (four co-authors)
7. HIP-148 date `October 27, 2025` → **`October 10, 2025`** (corrected in both the doc seal and the top-right results panel)
8. HIP-148 total veHNT `902,814,846` → **`902,275,496`**
9. ferebee Apr 2025 holdings `279.6M` (calculated 31% × 902M) → **`285.92M`** (actual on-chain holding)
10. Nova Labs Oct 2025 holdings `234.7M` → **`241.87M`**
11. Top-left "ferebee Proxy Holdings" panel (entirely fabricated breakdown with `bclq…7k0` and `ferebee2.sol` sub-wallets) → **replaced with "Top Proxy Share by Vote (rising)"** panel showing 15% → 26% → 31% across HIP-138/143/148
12. Messari excerpt (unverified quote) → **typographic-fragment-only**, no invented language
13. Era II banner `Jan–Aug 2025` → **`Nov 2024 – Aug 2025`** (HIP-138 vote closed Nov 22, 2024)

## Post-fact-check update (auto-extension reframing)

Reading the HIP-143 markdown directly during fact-check revealed: the proposal text says *"will remain in effect for one year from implementation, and will be extended for one additional year if no HIP is passed by Helium governance that determines otherwise."* The "1-year sunset" framing in v1 and the initial v2 was a paraphrase of the headline framing, not the actual contract language. HIP-143 is a 1-year initial term + 1-year automatic extension by design, with full authority running through April 3, 2027 absent an overriding HIP. The cover prompt has been updated to surface the auto-extension clause as the visual story rather than a missed sunset:

- Document 3 stamp: `1-YEAR SUNSET` → `1-YEAR + AUTO-EXTENDS`
- Document 6 cross-out: `no replacement filed` (suggesting failure) → the `AUTO-EXTENDS` portion of the stamp activated in fresh red ink (showing the designed-in extension triggering) plus the handwritten note `no overriding HIP filed`
- Insert A caption rewritten to surface April 3, 2027 as the next critical date
- A second vertical red gridline added to the time ruler at April 3, 2027

## New facts added in v2

- Insert B: HIP-143 four-co-author panel; explicit "ferebee co-authored, then accumulated, then passed HIP-148" line.
- Insert C: Keith Rettig named as the only labeled dissent on HIP-148 (1.00%, 13.98M veHNT, Against).
- Top-Right panel: corrected heliumvote.com final tally with Yes/No/Total veHNT figures, quorum requirement (100M), and 67% approval threshold (both exceeded).
- Top-Left panel: Top Proxy Share by Vote curve — the rising concentration is now the strongest single visual on the cover.
- Bottom strip: Jay M. as a third concentration vector; top-three-combined 62% on HIP-148.
- Notes panel: heliumvote.com / on-chain proxy registry / Messari Q4 2025 as provenance.

---

## v2 Prompt (use this for generation)

```
Role and Subject: A massive, encyclopedic 3D infographic poster, 16:9 ratio (1456 × 816). Title in bold condensed editorial serif at top: "THE ARCHITECTURE OF HELIUM GOVERNANCE — 2022–2026". Subtitle in smaller weight: "Six votes. Three eras. Top-proxy share rose from 15% to 57% in eleven months." Visual style: high-end fusion of museum-quality archival document photography and technical schematic blueprints. Editorial journalism, not crypto marketing.

Core Lineup (Chronology): Six stylized governance documents in linear chronology across a horizontal measuring-scale base. Each is a photorealistic 3D folded protocol-improvement-proposal paper with header, signature lines, and a wax-seal-style protocol stamp. From left to right:

1. "HIP-53 / July 25, 2022 / Mobile subDAO"
   Slim foundational document on unweathered cream paper. Header: "HIP-53: MOBILE subDAO — PROTOCOL IMPROVEMENT PROPOSAL". Author line: "Joey Padden et al." (do NOT write "Nova Labs"). Status: Accepted. Category: Economic / Technical.
   Annotation: "Establishes MOBILE token and subDAO. Sets data transfer rate at $0.50/GB. 97.22% pass on 2,438,837 veHNT (2.4M total network)."

2. "HIP-138 / November 22, 2024 / Return to HNT"
   Thicker bound document. Header: "HIP-138: RETURN TO HNT — PROTOCOL IMPROVEMENT PROPOSAL". Author line: "Nova Labs". Status: Accepted. Category: Tokenomics.
   Annotation: "IoT + Mobile tokens consolidated into single HNT at 1:1 ratio. 92.54% pass on 476,224,373 veHNT. Top voter: anonymous wallet at 15.00% — no proxy yet exceeds that share."

3. "HIP-143 / April 3, 2025 / Decoupling Service Provider Pricing from Governance"
   Document with a prominent red two-line stamp angled across it: "1-YEAR TERM" on top, "+ AUTO-EXTENDS" below (one of the few accent-red uses — preserve it). The "+ AUTO-EXTENDS" line is slightly fainter, signaling a contingent clause not yet triggered. Header: "HIP-143: DECOUPLING SERVICE PROVIDER PRICING FROM GOVERNANCE". Author line MUST read: "Inversion Capital, zer0tweets, Nova Labs & ferebee" (four co-authors). Status: Accepted. Category: Governance.
   Annotation: "Pricing authority delegated to Nova Labs for one year, with text extending it 'one additional year if no HIP is passed by Helium governance that determines otherwise.' 90.53% pass on 763,503,755 veHNT. Nova Labs 26.00% (199.8M) / ferebee 24.00% (183.85M). Top two combined: 50%. Auto-extends April 2026 → April 2027 absent override."

4. "Halving / August 2025"
   Small ledger with a downward arrow. Header: "HNT EMISSIONS HALVING". No HIP number — a protocol-scheduled event, not a vote.
   Annotation: "HNT emissions cut from 15,000,000 to 7,500,000 per year. Post-halving operator earnings: $4–$8 / month on a well-placed urban hotspot."

5. "HIP-148 / October 10, 2025 / Reallocate Mobile Mapping Rewards"
   Heavier, more authoritatively-sealed document — the seal visibly larger and more concentrated than HIP-143. Header: "HIP-148: REALLOCATE MOBILE MAPPING REWARDS". Author line: "Nova Labs". Status: Accepted. Category: Network Economics.
   Annotation: "Mobile Mapping rewards eliminated. Service Provider Pool 10% → 24%, 100% to Nova Labs. 96.72% pass on 902,275,496 veHNT. ferebee 31.00% (285.92M). Nova Labs 26.00% (241.87M). Jay M. 5.00% (52.63M). Top three: 62%. Keith Rettig was the only named dissent (1.00%, 13.98M veHNT, voted Against)."

6. "April 2026 / Auto-Extension Triggered"
   The HIP-143 document reappears with the same two-line stamp, but now the "+ AUTO-EXTENDS" portion is freshly inked in solid bright red (matching "1-YEAR TERM" saturation) — the contingent clause activated. Handwritten black-ink note next to the stamp: "no overriding HIP filed." Below the document: a small ledger card reading "385,000 deployed hotspots. Authority continues to April 3, 2027."
   Annotation: "Initial year ended April 3, 2026. No superseding HIP filed. The auto-extension clause triggered as written. Pricing authority now runs through April 3, 2027."

Rendering: Ultra-realistic 3D, 8K resolution. Documents slightly aged and creased; chronological progression shows them becoming more formally sealed and authoritative as the operator's position weakens. Horizontal measuring-scale ruler runs July 2022 to April 2027, monthly tick marks, two vertical red gridlines: solid at April 3, 2026 (initial term end / auto-extension trigger), dashed at April 3, 2027 (authority expires absent further extension; label "AUTHORITY EXPIRES" in small red text). Time spacing: HIP-53 far left; HIPs 138/143/Halving/148 cluster 2024–2025; auto-extension window 2026–2027 at right.

Canvas: Deep matte cream textured paper with subtle linen weave, lightly aged at edges. Low-opacity grayscale watermarks: HIP-143 markdown fragments, a HIP-148 voter-breakdown table from heliumvote.com, and a Messari Q4 2025 State of Helium report margin (typographic fragment only — no fabricated quote text). Watermarks never compete with foreground.

Palette: Strict monochrome industrial — warm cream paper, deep black ink linework and typography, charcoal grays for secondary annotations, soft sepia accents where documents have aged. ONE accent color only: desaturated brick red (#9B2C2C), reserved for the document 3 + 6 stamps, all proxy-concentration percentages (Nova Labs %, ferebee %, Jay M. %), and the April 2026 gridline. The red is the visual argument: it appears only where governance concentration is documented.

"Ultra-Dense" Information Layer (Editorial Style):

High-Density Annotation Network: Hundreds of ultra-fine black hairlines connect specific elements of each HIP document to compact text blocks floating in negative space, set in a clean editorial serif (NYT graphics desk).

Era Modules: Three grouped "Era" banners floating above the chronology — "Era I: Foundation (2022)", "Era II: Consolidation (Nov 2024 – Aug 2025)", "Era III: Concentration (Oct 2025 – Apr 2026)". Each era's documents grouped under its banner with a thin black bracket.

Top-Left Panel — TOP PROXY SHARE BY VOTE (rising). Four rows:
   HIP-53 (Jul 2022): top voter share unknown — total network only 2.4M veHNT
   HIP-138 (Nov 2024): top voter 15.00% (anonymous wallet, 72.9M veHNT)
   HIP-143 (Apr 2025): top voter 26.00% (Nova Labs, 199.8M veHNT)
   HIP-148 (Oct 2025): top voter 31.00% (ferebee, 285.92M veHNT)
The 26.00% and 31.00% in red. Below the table: a tiny line-chart spark showing the rise from 15% to 31% across three votes. This is the article's thesis in one panel.

Top-Right Panel — heliumvote.com final tally for HIP-148, "Final Tally (Oct 10, 2025)":
   Yes  872,704,450.74 veHNT  96.72%
   No   29,571,045.78 veHNT    3.27%
   Total 902,275,496.53 veHNT 100.00%
   Quorum requirement: 100M veHNT. Approval threshold: 67%. Both exceeded.

Magnified Inserts (three circular "zoom-in" lenses in negative space):
A. Macro close-up of the HIP-143 two-line stamp ("1-YEAR TERM / + AUTO-EXTENDS"), auto-extends line crisply visible. Caption: "The auto-extension clause was written into the proposal text. Authority extends through April 3, 2027 unless overridden."
B. Signature panel for HIP-143 with the four co-author names ('Inversion Capital · zer0tweets · Nova Labs · ferebee') in handwritten ink. Caption: "ferebee co-authored the HIP that authorized pricing authority. ferebee then accumulated voting power to pass HIP-148 six months later."
C. Macro close-up of a single dissent line from the heliumvote.com HIP-148 breakdown: "EYd23…PUani / Against HIP 148 / 13,983,104.10 / 1.00% / Keith Rettig". Caption: "The only named dissent."

Technical Specification Strip: Structured data bar across the bottom, fixed-width editorial font, SIX columns matching the six documents. Each column lists top-to-bottom: HIP ID/Event, Date, Title, Vote% For, veHNT Cast, Nova Labs Share, ferebee Share, Operator Impact.

Col 1: HIP-53 / Jul 25 2022 / Mobile subDAO / 97.22% / 2,438,837 / N/A / N/A / Baseline pricing established
Col 2: HIP-138 / Nov 22 2024 / Return to HNT / 92.54% / 476,224,373 / N/A (top voter 15%) / N/A / Token unification
Col 3: HIP-143 / Apr 3 2025 / Decoupling SP Pricing / 90.53% / 763,503,755 / 26.00% / 24.00% / One-year pricing authority delegated
Col 4: Halving / Aug 2025 / HNT Emissions Halving / N/A / N/A / N/A / N/A / Emissions cut 50% — earnings reduced
Col 5: HIP-148 / Oct 10 2025 / Reallocate Mobile Mapping / 96.72% / 902,275,496 / 26.00% / 31.00% / Rewards centralized to Nova Labs
Col 6: HIP-143 (auto-extension) / Apr 3 2026 / Auto-Extension Triggered / N/A / N/A / N/A / N/A / Auto-extension activated; authority to Apr 3 2027

Right-edge column: "AGGREGATE (Apr 2026): 385,000 deployed hotspots. $124.77 / day IoT revenue. $56,635 / day Mobile revenue. Outdoor unit payback: 10–20 years."

Bottom-right corner: a small credit block — "The Civic Node · drinkyouroj.substack.com" in a single restrained line.

Notes panel (above credit): "All vote data: heliumvote.com. veHNT = vote-escrowed HNT. Proxy labels from on-chain proxy registry. Financial data: Messari Q4 2025 State of Helium."

Technical Specs: Octane render, cinematic editorial lighting, soft diffuse top-light (as if photographed on an archivist's table), sharp focus, professional color grading favoring warm cream and ink black, deep shadows under each document. Reference style: NYT Sunday Review graphic, Bloomberg Businessweek investigative chart, Bureau of Investigative Journalism dossier cover. Editorial journalism, not crypto marketing. --ar 16:9 --v 6.0 --stylize 250
```

---

## Aspect-ratio adapter notes

- **Midjourney / Nano Banana Pro**: use `--ar 16:9` as written.
- **DALL-E 3**: request "wide landscape, 1792 × 1024".
- **Stable Diffusion / Flux**: set width 1456, height 816 explicitly.
- **GPT Image 1.5 / Seedream 5.0**: request "16:9 aspect ratio, 1456 × 816 px".

## Provenance

All vote data and proxy concentration figures sourced from:
- `raw/assets/HIP-53 vote results.png` (heliumvote.com, captured 2026-05-19)
- `raw/assets/HIP-138 vote results.png` (heliumvote.com, captured 2026-05-19)
- `raw/assets/HIP-143 summary-details.png` + `raw/assets/HIP-143 voter breakdown.png` (heliumvote.com, captured 2026-05-16)
- `raw/assets/HIP-148 vote breakdown.png` + `raw/assets/HIP-148 X announcement.png` (heliumvote.com + X, captured 2026-05-19)
- Wiki sources: [[Helium HIP-53 Vote Results — Helium Vote - 2022-07-25]], [[Helium HIP-138 Vote Results — Helium Vote - 2024-11-22]], [[Helium HIP-143 Vote Results — Helium Vote - 2025-04-03]], [[Helium HIP-148 Vote Results — Helium Vote - 2025-10-10]]
