---
title: "Series Template — The Thinking Behind the Thinking (Cover Image Prompt)"
type: image-prompt-template
series: The thinking behind the thinking
based_on_library_template: "#13068 — Editorial Magazine Spread Concept Prompt"
library_template_url: "https://youmind.com/nano-banana-pro-prompts?id=13068"
established: 2026-05-19
first_use: "2026-05-20 — I Had the Wrong Bottom of the Stack"
aspect_ratio: "16:9 (1456 × 816)"
model: Nano Banana Pro / Flux / Midjourney
---

# Series Cover Template — The Thinking Behind the Thinking

This is the locked visual identity for paid notes in the *Thinking Behind the Thinking* series. Use this template for every new installment. The composition, paper, lighting, palette, and brand mark are fixed. Only **four variables** swap per piece.

## The four swap variables

| Variable | What it is | Example (May 20 — "I Had the Wrong Bottom of the Stack") |
|---|---|---|
| `{{TITLE}}` | The headline in 3 staircased lines, ALL CAPS. One word set in italic for emphasis. | `I HAD THE / WRONG BOTTOM / OF THE STACK` (italic on "WRONG") |
| `{{DATE_LINE}}` | The series identifier line — only the date changes. Format: month name, day, year. | `May 20, 2026` |
| `{{ANCHOR_NUMBER}}` + `{{ANCHOR_UNIT}}` + `{{ANCHOR_GLOSS}}` | The lower-right typographic anchor: one specific number from the piece, its unit, and a one-line italic gloss. | `128` + `WEEKS` + `the order book the chip layer doesn't fit on` |
| `{{MARGIN_NOTE}}` + `{{UNDERLINED_WORDS}}` | A handwritten brick-red cursive note + which word(s) in the headline get the brick-red underline | margin: `underneath all five.` · underline: `BOTTOM OF THE STACK` |

**Locked elements** (do not change across installments):
- Brand mark: `The Civic Node · drinkyouroj.substack.com` in lower-left
- Aspect ratio: 16:9 horizontal, 1456 × 816
- Paper: warm cream uncoated stock with subtle linen weave, photographed on a warm cream desk surface under directional side light
- Typography: condensed display serif (Bodoni / Didone family) in deep charcoal, headline at ~200pt
- Accent: desaturated brick red `#9B2C2C` at exactly three points — the underline, the margin note, and the thin horizontal rule line below the date

---

## How to use this template

1. Pick the four variables for the new installment by reading the finished note draft:
   - **TITLE**: the headline from the note's `title:` frontmatter, broken into 3 lines with one word italicized for emphasis (usually the verb of self-correction or the surprising noun)
   - **DATE_LINE**: the publication date
   - **ANCHOR_NUMBER / UNIT / GLOSS**: the one number from the note that most reliably haunts a reader (see "Anchor number selection" below)
   - **MARGIN_NOTE / UNDERLINED_WORDS**: a 2–6 word phrase that compresses the analytical correction, plus the word(s) in the headline that get the brick-red underline (usually the words being analytically replaced)

2. Substitute the four variables into the master prompt below.

3. Generate at 16:9. Verify the four variables rendered correctly. AI typography is the most common failure mode — if any text is garbled, regenerate with simpler line breaks before changing anything else.

4. Once approved, save the customized prompt to the piece's own cover-prompt file (`workspace/paid/YYYY-MM-DD-[slug]-cover-prompt.md`) for the project's audit trail, with a one-line note pointing back to this template.

---

## Anchor number selection — the editorial signature

Every installment includes one specific number from the piece, pulled forward as a typographic anchor. This is the cover's secondary editorial move and a TCN signature — same as the May 15 flagship's headline ("12 Gigawatts Were Announced. 4 Are Being Built.") and the May 22 Helium cover's "15% to 57% in eleven months" pull-quote.

**Selection rule**: pick the single number that most reliably haunts a reader after they finish the piece. The test: if someone asks "what was that one about?" a week later, which number would they remember?

Worked examples for ranking candidates against this rule:
- **May 20 — I Had the Wrong Bottom of the Stack** → `128 WEEKS` ✓ (the procurement calendar; haunts because it's longer than the chip layer's entire reversion timeline)
- **May 13 — I Had the Wrong Protagonist** → `191` ✓ (tracked Strait of Hormuz crossings against pre-war 3,000/month; the figure that converts a "supply shock" into a tanker count) — could also be `19.7%` (tariff rate) or `20%` (Strait's share of global oil)
- **May 6 — Minnesota Isn't Here for the Injunction** → harder. Candidates: `335` (named defendants from the original court order) or `3,000` (arrests) — but neither is mentioned in the May 6 *paid note* specifically; the paid note's content is about evidence-gathering and a paper trail. May need a fresh number from the paid note itself, or accept that some notes will lean more verbal than numeric.

If a piece genuinely has no anchor number, replace the ANCHOR block with a short pulled-forward phrase set in the same typographic register (e.g., a 2–4 word fragment from the piece) — but this should be the exception. Numbers travel.

---

## Margin note selection — the analytical correction in 2–6 words

The handwritten brick-red margin note compresses the analytical correction into a phrase the reader can hold. It should pair semantically with the underlined word(s) in the headline.

Worked examples:
- **May 20** → underline: `BOTTOM OF THE STACK` · margin: `underneath all five.` (the correction names where the bottom actually is)
- **May 13** → underline: `PROTAGONIST` · margin: `the mandate is what matters.` (the correction names what the actual protagonist should have been)
- **May 6** → underline: `PRESS RELEASE` · margin: `it's a paper trail.` (the correction names what the document actually is)

The margin note is the only cursive element on the cover. Keep it short — the legibility of cursive in AI-rendered images degrades fast past ~6 words.

---

## Master prompt (substitute the four variables, then generate)

```
A photographic editorial magazine cover, 16:9 horizontal landscape (1456 × 816), based on the editorial magazine spread aesthetic: muted earth tones with raw linen texture, large-scale serif headline at 200pt in deep charcoal, off-white margins with subtle grain overlay, geometric rule lines in desaturated brick red, cinematic side lighting casting long shadows across the layout, high-end editorial print finish.

Composition:
A single magazine cover page photographed flat-on (not at an angle) on a warm cream desk surface, the page itself filling roughly 90% of the frame with narrow margins of desk surface visible on the left and right edges. The page is printed on warm cream uncoated stock with subtle linen weave texture and very faint grain overlay. Directional side lighting from the upper-left casts long soft shadows across the page surface, giving the cover the depth of an actual printed artifact photographed for an editorial feature.

Typography (all set in classic editorial serif — Bodoni, Didone, or similar condensed display serif — in deep charcoal black):

UPPER HALF — The massive headline, set in three lines, left-aligned, occupying roughly the upper 55% of the page:

"{{TITLE_LINE_1}}
{{TITLE_LINE_2}}
{{TITLE_LINE_3}}"

The word "{{ITALIC_WORD}}" is set in italic to draw the eye. Generous letter-spacing. The headline is approximately 200pt — it dominates the composition.

Below the headline, separated by a thin horizontal geometric rule line in desaturated brick red (#9B2C2C), a single small line of editorial serif in medium charcoal gray:
"Process note · The thinking behind the thinking · {{DATE_LINE}}"

LOWER-RIGHT THIRD — A secondary typographic anchor. The numeral "{{ANCHOR_NUMBER}}" set in a contrasting heavy serif weight, with "{{ANCHOR_UNIT}}" stacked underneath in editorial serif caps, and below in small italic regular weight:
"{{ANCHOR_NUMBER}}
{{ANCHOR_UNIT}}
{{ANCHOR_GLOSS}}"

LOWER-LEFT CORNER — A small unobtrusive credit line in editorial sans-serif:
"The Civic Node · drinkyouroj.substack.com"

Single accent mark (the only saturated color in the entire composition):
A thin desaturated brick red (#9B2C2C) underline drawn beneath the words "{{UNDERLINED_WORDS}}" in the headline — looks like a real ink underline added by hand after printing. Beside it, in the right margin of the headline, a small handwritten margin note in matching brick-red ink cursive: "{{MARGIN_NOTE}}" The geometric rule line below the date is also brick red. Nothing else in the composition uses saturated color.

Style references:
The page should look like a real magazine cover — Harper's, n+1, The Baffler, the New Yorker fiction issue, NYT Magazine — photographed for an editorial process feature. Restrained, confident, intentional. The kind of cover you'd see in an editorial design retrospective. Not a digital mockup, not a flat vector design — a printed artifact with paper texture, subtle ink weight variation, and natural light.

Color palette (strict):
- Warm cream paper background (subtle linen weave, faint grain)
- Warm cream desk surface visible at the margins (slightly different tone from the page paper)
- Deep charcoal black ink for all headline and body typography
- Medium charcoal gray for secondary type (date line, gloss line)
- Single accent: desaturated brick red (#9B2C2C) — used ONLY at three points: the underline beneath "{{UNDERLINED_WORDS}}," the handwritten "{{MARGIN_NOTE}}" margin note, and the geometric rule line below the date. Nothing else is colored.

Lighting:
Cinematic side lighting from the upper-left, soft and directional, casting long subtle shadows across the page from the right edge of any typography that protrudes. The shadow quality should be soft (diffused window light, not hard studio strobe). Slightly warmer light tone in the upper-left, cooler in the lower-right, giving the page subtle directional warmth.

Negative prompts:
no people, no faces, no hands, no illustrations on the page (this is type-only), no diagrams, no charts, no infographics, no decorative borders or ornaments, no barcodes, no commercial magazine furniture (no UPC, no cover lines listing additional articles, no flash sale banners), no glossy magazine finish (must be matte uncoated stock), no white background (must be warm cream), no AI-generated nonsense text in the typography (every word must be the exact text specified), no logos of real magazines, no commercial brand logos, no photographic imagery of any subject (this is a type cover, not a photo cover), no archival document elements (we are deliberately moving away from the flagship covers' archival aesthetic).

Output:
16:9 horizontal landscape, 1456 × 816, 8K resolution. Sharp focus on typography. Paper texture and side lighting visible but not distracting. The image should read instantly at thumbnail size — the headline should be legible even at 150px wide. --ar 16:9 --v 6.0 --stylize 150
```

---

## Variable substitution worksheet (paste below for each new installment)

When prepping a new cover, copy this block to the piece's own cover-prompt file and fill it in:

```
Installment: [PIECE TITLE]
Publication date: [YYYY-MM-DD]

{{TITLE_LINE_1}}       = [first line of headline, ALL CAPS]
{{TITLE_LINE_2}}       = [second line]
{{TITLE_LINE_3}}       = [third line]
{{ITALIC_WORD}}        = [which word in the headline is italicized]
{{DATE_LINE}}          = [Month DD, YYYY]
{{ANCHOR_NUMBER}}      = [the haunting number]
{{ANCHOR_UNIT}}        = [WEEKS / DAYS / GW / % / etc. — ALL CAPS]
{{ANCHOR_GLOSS}}       = [one-line italic gloss explaining what the number is, lowercase]
{{UNDERLINED_WORDS}}   = [the words in the headline that get the brick-red underline]
{{MARGIN_NOTE}}        = [2–6 word handwritten brick-red cursive correction, with period]
```

---

## Aspect-ratio adapter notes

- **Midjourney / Nano Banana Pro**: use `--ar 16:9` as written.
- **DALL-E 3 / GPT Image 1.5**: request "wide landscape, 1792 × 1024".
- **Stable Diffusion / Flux**: set width 1456, height 816 explicitly.
- **Seedream 5.0**: request "16:9 aspect ratio, 1456 × 816 px".

## Provenance

- Library template source: [#13068 — Editorial Magazine Spread Concept Prompt](https://youmind.com/nano-banana-pro-prompts?id=13068)
- Series established: 2026-05-19 (during build of the May 20 paid note "I Had the Wrong Bottom of the Stack")
- First piece using this template: [`workspace/paid/2026-05-20-thinking-behind-the-thinking-grid-cover-prompt.md`](2026-05-20-thinking-behind-the-thinking-grid-cover-prompt.md) — see that file for the worked example with all four variables filled in
- Visual relationship to flagship covers: deliberate visual differentiation from the archival-illustration aesthetic used for flagship covers (May 15 "12 Gigawatts" #4847, May 22 Helium #4847). Paid notes are typographic; flagships are encyclopedic. Subscribers see them as different formats at a glance.

## Future updates

If a future installment surfaces a need to evolve the template (a new piece doesn't fit the four-variable swap, the AI generator stops rendering reliably, the series shifts visual direction), document the change here as a numbered revision rather than overwriting silently. The template's value is its consistency across installments — modifications should be deliberate and dated.
