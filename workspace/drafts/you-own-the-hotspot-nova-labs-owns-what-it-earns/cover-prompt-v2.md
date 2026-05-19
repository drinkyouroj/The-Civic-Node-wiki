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
Role and Subject: A massive, encyclopedic 3D infographic poster with a 16:9 ratio (1456 × 816). Title at top in bold condensed editorial serif: "THE ARCHITECTURE OF HELIUM GOVERNANCE — 2022–2026". Subtitle below in smaller weight: "Six votes. Three eras. Top-proxy share rose from 15% to 57% in eleven months." The visual style is a high-end fusion of museum-quality archival document photography and technical schematic blueprints. Editorial journalism, not crypto marketing.

Core Lineup (Chronology): Arrange SIX stylized governance documents in a linear chronology across a horizontal measuring-scale base. Each document is rendered as a photorealistic 3D object — a folded protocol-improvement-proposal paper with header, signature lines, and a wax-seal-style protocol stamp. From left to right:

1. "HIP-53 / July 25, 2022 / Mobile subDAO"
   Slim foundational document on unweathered cream paper. Header reads "HIP-53: MOBILE subDAO — PROTOCOL IMPROVEMENT PROPOSAL". Author line: "Joey Padden et al." (do NOT write "Nova Labs"). Status: Accepted. Category: Economic / Technical.
   Annotation below: "Establishes MOBILE token and subDAO. Sets data transfer rate at $0.50/GB. 97.22% pass on 2,438,837 veHNT (2.4M total network)."

2. "HIP-138 / November 22, 2024 / Return to HNT"
   Thicker bound document. Header reads "HIP-138: RETURN TO HNT — PROTOCOL IMPROVEMENT PROPOSAL". Author line: "Nova Labs". Status: Accepted. Category: Tokenomics.
   Annotation below: "IoT + Mobile tokens consolidated into single HNT at 1:1 ratio. 92.54% pass on 476,224,373 veHNT. Top voter: anonymous wallet at 15.00% — no proxy yet exceeds that share."

3. "HIP-143 / April 3, 2025 / Decoupling Service Provider Pricing from Governance"
   Document with a prominent red two-line stamp angled across it reading "1-YEAR TERM" on the top line and "+ AUTO-EXTENDS" on the second line (this stamp is one of the few uses of the accent red — preserve it). The "+ AUTO-EXTENDS" portion is drawn slightly fainter than "1-YEAR TERM" on document 3, signaling that it's the contingent clause not yet triggered. Header reads "HIP-143: DECOUPLING SERVICE PROVIDER PRICING FROM GOVERNANCE". Author line MUST read: "Inversion Capital, zer0tweets, Nova Labs & ferebee" (four co-authors — this is the corrected attribution). Status: Accepted. Category: Governance.
   Annotation below: "Pricing authority delegated to Nova Labs for one year. The HIP's text adds: 'extended for one additional year if no HIP is passed by Helium governance that determines otherwise.' 90.53% pass on 763,503,755 veHNT. Nova Labs proxy 26.00% (199.8M). ferebee proxy 24.00% (183.85M). Top two proxies combined: 50%. Initial term ends April 3, 2026; auto-extends through April 3, 2027 absent override."

4. "Halving / August 2025"
   Small ledger with a downward arrow. Header: "HNT EMISSIONS HALVING". No HIP number — this is a protocol-scheduled event, not a vote.
   Annotation below: "HNT emissions cut from 15,000,000 to 7,500,000 per year. Post-halving operator earnings: $4–$8 / month on a well-placed urban hotspot."

5. "HIP-148 / October 10, 2025 / Reallocate Mobile Mapping Rewards"
   Heavier, more authoritatively-sealed document — the seal visibly larger and more concentrated than HIP-143. Header reads "HIP-148: REALLOCATE MOBILE MAPPING REWARDS". Author line: "Nova Labs". Status: Accepted. Category: Network Economics.
   Annotation below: "Mobile Mapping rewards eliminated. Service Provider Pool 10% → 24%, 100% allocated to Nova Labs. 96.72% pass on 902,275,496 veHNT. ferebee 31.00% (285.92M). Nova Labs 26.00% (241.87M). Jay M. 5.00% (52.63M). Top three proxies combined: 62%. Keith Rettig was the only named dissent (1.00%, 13.98M veHNT, voted Against)."

6. "April 2026 / Auto-Extension Triggered"
   The HIP-143 document reappears. The same red two-line stamp from document 3 ("1-YEAR TERM / + AUTO-EXTENDS") is visible — but on document 6, the "+ AUTO-EXTENDS" portion has been newly inked in solid, bright red (matching the saturation of "1-YEAR TERM"), indicating the contingent clause is now active. A fine handwritten note in black ink reads "no overriding HIP filed" next to the stamp. Below the document: a single small ledger card reading "385,000 deployed hotspots. Authority continues to April 3, 2027."
   Annotation below: "Initial year ended April 3, 2026. No superseding HIP was filed. The auto-extension clause triggered as written. The pricing authority now runs through April 3, 2027."

Rendering: Ultra-realistic 3D, 8K resolution. Each document slightly aged and creased; the chronological progression shows the documents becoming more formally sealed and authoritative even as the operator's position weakens. The horizontal measuring-scale ruler at the document baseline runs from July 2022 to April 2027, with tick marks for every month, and TWO vertical red gridlines: a solid one at April 3, 2026 (initial term end / auto-extension trigger) and a dashed one at April 3, 2027 (the next critical date — when the authority is supposed to expire absent further extension). The dashed gridline is labeled "AUTHORITY EXPIRES (absent override)" in small red text. The ruler must accommodate the actual time spacing (HIP-53 is far to the left; HIPs 138/143/Halving/148 cluster in 2024–2025; the auto-extension window 2026–2027 is the rightmost portion).

Brand Atmosphere (Canvas): Background — a deep matte cream textured paper with subtle linen weave, lightly aged at the edges. Overlaid with low-opacity watermarks: fragments of the actual HIP-143 markdown, a HIP-148 voter-breakdown table from heliumvote.com, and a Messari Q4 2025 State of Helium report margin (no fabricated quote — leave the Messari panel as a typographic document fragment without inventing language). All watermarks in faded grayscale, never competing with the foreground.

Palette: Strict monochrome industrial — warm cream paper background, deep black ink linework and typography, charcoal grays for secondary annotations, soft sepia accents where documents have aged. ONE accent color only: a desaturated brick red (#9B2C2C), reserved exclusively for: (a) the 1-YEAR SUNSET stamp on document 3; (b) the worn/crossed-out version of the same stamp on document 6; (c) the proxy-concentration percentages (Nova Labs %, ferebee %, Jay M. %) wherever they appear; (d) the April 2026 gridline on the time ruler. The red is the visual argument: it appears only where concentration of governance power is being documented.

"Ultra-Dense" Information Layer (Editorial Style):

High-Density Annotation Network: Hundreds of ultra-fine black hairlines connect specific elements of each HIP document to compact text blocks floating in negative space, set in a clean editorial serif (think New York Times graphics desk).

Era Modules: Three grouped "Era" banners floating above the chronology — "Era I: Foundation (2022)", "Era II: Consolidation (Nov 2024 – Aug 2025)", "Era III: Concentration (Oct 2025 – Apr 2026)". Each era's documents grouped under its banner with a thin black bracket.

Top-Left Panel — TOP PROXY SHARE BY VOTE (rising). Four rows:
   HIP-53 (Jul 2022): top voter share unknown — total network only 2.4M veHNT
   HIP-138 (Nov 2024): top voter 15.00% (anonymous wallet, 72.9M veHNT)
   HIP-143 (Apr 2025): top voter 26.00% (Nova Labs, 199.8M veHNT)
   HIP-148 (Oct 2025): top voter 31.00% (ferebee, 285.92M veHNT)
The 26.00% and 31.00% in red. Below the table: a tiny line-chart spark showing the rise from 15% to 31% across three votes. This is the article's thesis in one panel.

Top-Right Panel — heliumvote.com final tally for HIP-148, dated correctly: "Final Tally (Oct 10, 2025)":
   Yes  872,704,450.74 veHNT  96.72%
   No   29,571,045.78 veHNT    3.27%
   Total 902,275,496.53 veHNT 100.00%
   Quorum requirement: 100M veHNT. Approval threshold: 67%. Both exceeded.

Magnified Inserts (three circular "zoom-in" lenses scattered in negative space):
A. Macro close-up of the HIP-143 two-line stamp showing "1-YEAR TERM / + AUTO-EXTENDS" with the auto-extends line crisply visible, caption: "The auto-extension clause was written into the proposal text the operators approved. Initial term ends April 3, 2026; the authority extends through April 3, 2027 unless an overriding HIP passes."
B. Signature panel for HIP-143 showing the four co-author names ('Inversion Capital · zer0tweets · Nova Labs · ferebee') in handwritten ink, caption: "ferebee co-authored the HIP that authorized pricing authority. ferebee then accumulated voting power to pass HIP-148 eighteen months later."
C. Macro close-up of a single dissent line item from the heliumvote.com HIP-148 breakdown: row reading "EYd23…PUani / Against HIP 148 / 13,983,104.10 / 1.00% / Keith Rettig". Caption: "The only named dissent."

Technical Specification Strip: A structured data bar across the bottom in a fixed-width editorial font, SIX columns matching the six documents above. For each column, top to bottom:
   HIP ID / Event
   Date (vote close)
   Title
   Vote % For
   veHNT Cast
   Nova Labs Share
   ferebee Share
   Operator Impact

Concrete data:
Col 1: HIP-53 / Jul 25 2022 / Mobile subDAO / 97.22% / 2,438,837 / N/A / N/A / Baseline pricing established
Col 2: HIP-138 / Nov 22 2024 / Return to HNT / 92.54% / 476,224,373 / N/A (top voter 15%) / N/A / Token unification
Col 3: HIP-143 / Apr 3 2025 / Decoupling SP Pricing / 90.53% / 763,503,755 / 26.00% / 24.00% / One-year pricing authority delegated
Col 4: Halving / Aug 2025 / HNT Emissions Halving / N/A (protocol) / N/A / N/A / N/A / Emissions cut 50% — earnings reduced
Col 5: HIP-148 / Oct 10 2025 / Reallocate Mobile Mapping / 96.72% / 902,275,496 / 26.00% / 31.00% / Rewards centralized to Nova Labs
Col 6: HIP-143 (auto-extension) / Apr 3 2026 / Auto-Extension Triggered / N/A / N/A / N/A / N/A / Auto-extension clause activated; authority runs to Apr 3 2027

Right-edge column: "AGGREGATE (Apr 2026): 385,000 deployed hotspots. $124.77 / day IoT revenue. $56,635 / day Mobile revenue. Outdoor unit payback: 10–20 years."

Bottom-right corner: a small, formally-set credit block — "The Civic Node · drinkyouroj.substack.com" in a single restrained line.

Notes panel (bottom-right above credit): "All vote data: heliumvote.com. veHNT = vote-escrowed HNT. Proxy labels from on-chain proxy registry. Financial data: Messari Q4 2025 State of Helium."

Technical Specifications: Octane render with cinematic editorial lighting, soft diffuse top-light as if photographed on an archivist's table, sharp focus throughout, professional color grading favoring warm cream and ink black, deep shadows under each document for depth, masterpiece of analytical information design. Reference style: a New York Times Sunday Review graphic, a Bloomberg Businessweek investigative chart, a Bureau of Investigative Journalism dossier cover. NOT crypto marketing. NOT promotional. Editorial journalism. --ar 16:9 --v 6.0 --stylize 250
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
