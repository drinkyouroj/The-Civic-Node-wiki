# Claude Design prompt — TCN Dispatch №005 slideshow

> **How to use this file.** Open a new project at [claude.ai/design](https://claude.ai/design), upload the design system files listed below plus the four Justoon PNGs listed in §5 (Slides 3, 4, 8, 9), then paste everything from "## Context" to the end into the chat. Claude Design will produce one bundled HTML file. Verify by resizing the browser to 1:1 (1080×1080), 16:9 (1920×1080), and 9:16 (1080×1920), then scale to ~240px wide to confirm thumbnail legibility.

---

## Context

You are building an HTML slideshow for The Civic Node, Dispatch №005:
**"The Bill of Rights Ends at the Contractor's Door."** The slideshow
is the visual companion to a 5-minute, 15-second YouTube narration
video; viewers will watch the slides while listening to the narration
as audio. The deck has 11 slides. Primary recording aspect is 1:1
(1080×1080); 16:9 and 9:16 outputs derive from the same HTML by
changing the recording window's aspect.

The piece argues a single structural pattern: where the Constitution
writes a rule binding the government, the government contracts the
function to a private vendor not bound by the rule. Four domains
(surveillance, speech, biometrics, health data) all show the same
architecture. The deck's job is to make that pattern visually legible.

## Inputs (attached / uploaded to this Claude Design project)

- `colors_and_type.css` — brand CSS variable system. Load at runtime.
- `slides.css` — slide-specific styles (sl-title, sl-section, sl-lead,
  sl-data, sl-frames, sl-compare, sl-quote, sl-end).
- `deck-stage.js` — kinetic engine. Load via `<script src="deck-stage.js">`.
- `assets/mark.svg`, `assets/lockup-dark.svg` — brand marks.
- `slides/deck.html` — reference template; mimic its slide structure.
- **Justoon PNGs** (illustrated host character — 4 files for this deck):
  - `justoon-point-right.png` — Slides 3 and 4 (Receipt slides)
  - `justoon-react-deadpan.png` — Slide 8 (Twist slide)
  - `justoon-point-open-palm.png` — Slide 9 (Stakes slide)
  - `justoon-neutral.png` — anchor / fallback, upload as safety net

> If any design system file is missing from this project's uploads,
> stop and ask the user to upload it before proceeding.

## Brand requirements (non-negotiable)

- One typeface: Courier Prime.
- Palette: slate-400 / slate-600 / black / twilight only. No other colors.
- No emoji, no icon fonts, no exclamation points, no shadows on dark.
- Middle dot `·` as the kicker separator. Never `|`, never `/`.
- Easing on every animation: `cubic-bezier(0.2, 0, 0, 1)`.
- Durations: 120ms, 200ms, or 360ms. Nothing longer than 500ms.
- No bounce, no spring, no rainbow gradients.
- Kickers: mono, wide-tracked (`0.18em`), all-caps, slate-400.

## Small-screen / multi-aspect requirements (non-negotiable)

This deck must render correctly at 16:9, 9:16, and 1:1 from this
single HTML file, and must be readable at thumbnail playback (~240px
wide on a phone). **The primary recording aspect is 1:1 (1080×1080).**
The 16:9 and 9:16 outputs are derived from the same HTML by changing
the recording window's aspect — slide content does not reflow.

The mechanism: the safe zone is always a square (`min(85cqw, 85cqh)`).
Design slide content inside the safe zone and it renders identically
at any aspect — only the empty viewport margin differs.

- Each `.slide` element uses `container-type: size` so cq-units scale
  to the slide, not the viewport. This decouples slide layout from
  page layout.
- Define `--safe-zone: min(85cqw, 85cqh)` per slide. Every slide's
  critical-content container is exactly this size, centered.
- Critical content (kicker, headline, body, hero numbers, source
  attributions, CTA, disclosure, Justoon image when present) lives
  ONLY inside the safe zone.
- Decorative elements (brand mark, `sl-hairline` rules, `sl-glow`
  radial, slide background fill) may extend to slide edges.
- No fixed-pixel widths on layout containers. No media queries based
  on aspect ratio. Layout is identical at every aspect; only the
  empty margin differs.

**Type scale (apply per slide via container-query units):**

```css
.slide {
  container-type: size;
  --type-hero:    clamp(80px, 24cqmin, 360px);
  --type-h1:      clamp(28px,  9cqmin,  144px);
  --type-h2-mid:  clamp(22px,  6.5cqmin, 96px);
  --type-body:    clamp(14px,  5cqmin,  72px);
  --type-kicker:  clamp(10px,  2.5cqmin, 36px);
  --safe-zone:    min(85cqw, 85cqh);
}
```

No element renders below `--type-kicker`. The hero/h1/h2-mid/body/
kicker roles are the only sizes used on the deck. Use `--type-h2-mid`
(not `--type-h1`) on body slides where Justoon is the anchor and the
headline is supporting — Slide 8 specifically.

**Text-wrap directive:** every `.headline` and `.caption` element uses
`text-wrap: balance` to distribute lines visually.

**Slide zone modifier class.** Each `.slide` element gets a zone
modifier class derived from the narration's zone label:
`slide-hook`, `slide-thesis`, `slide-receipt`, `slide-frame`,
`slide-anaphora`, `slide-twist`, `slide-stakes`, `slide-tease`,
`slide-end`. The class enables the Justoon CSS rules below.
Example: `<div class="slide slide-twist">…</div>`.

**Justoon CSS rules** (apply when any slide includes a `.justoon` image):

```css
/* Role A — full-body pointing teacher (Receipt + Stakes slides) */
.slide-receipt .justoon, .slide-stakes .justoon {
  position: absolute;
  left: 0;
  bottom: calc(var(--type-kicker) + 1.5cqh);
  height: 88cqh;
  width: auto;
  max-width: 32%;
  object-fit: contain;
  object-position: left bottom;
}

/* Role C — bust reaction-as-anchor (Twist slides) */
.slide-twist .justoon {
  position: absolute;
  right: 0;
  bottom: calc(var(--type-kicker) + 1.5cqh);
  height: 75cqh;
  width: auto;
  max-width: 55%;
  object-fit: contain;
  object-position: right bottom;
}
```

DO NOT use CSS grid with `align-items: center` for Justoon placement;
grid's row auto-sizing with image children makes `height: 100%`
resolve to the image's natural pixel height (a 2048×2048 PNG renders
at 2048px, breaking the layout). Always use absolute positioning with
explicit `cqh` max-heights. (See the reference layout at
`docs/superpowers/reference-renders/2026-05-25-justoon-slideshow-layout.html`
in the Substack Research project for the proven implementation.)

**Thumbnail-anchor rule:** every slide has exactly one element at
`--type-hero` (or `--type-h1` for slides without a numeric anchor;
or the Justoon image itself for Slide 8's role C reaction-as-anchor).
That element must occupy ≥20% of the safe-zone height.

**Visible-text budget:** ≤25 visible words per slide across all on-
screen elements, OR one hero number + ≤15 supporting words. Speaker
notes and Justoon images are not counted against this budget. No
panel-splits are required on this deck — the upstream narration was
re-paced from 9 to 11 slides specifically to land each slide under
budget.

## Slide-by-slide specification

---

### Slide 1 — sl-title  (Cold Open · Hook)

Kicker: `DISPATCH №005 · HOOK`
Headline (anchor, `--type-h1`): `THE BILL OF RIGHTS ENDS AT THE CONTRACTOR'S DOOR`
Tag (sub-line, `--type-body`): `Atlanta has a sanctuary policy. The cameras don't.`
Foot row (`--type-kicker`, three-part, separated by `·`):
  `The Civic Node · 2026·05·25 · 5 MIN`

Visible-text budget: ~18 words. Headline runs ~2-3 wrapped lines with
`text-wrap: balance` — keep the structural break between "RIGHTS" and
"ENDS" if the engine respects it; otherwise let `text-wrap: balance`
choose. Tag sits below headline, slate-400, smaller than body.

Animation:
- `sl-glow` radial slate behind the mark, full intensity
- `sl-mark-pulse` on the mark, single pulse on entry
- `sl-reveal-3` cascade: headline → tag → foot row
- Hairline draw left-to-right on the foot-row baseline, 360ms
- Hold for ~2s after foot row settles before allowing advance

Justoon: none.

---

### Slide 2 — sl-lead  (Cold Open · Thesis)

Kicker: `DISPATCH №005 · THESIS`
Heading (anchor, `--type-h1`): `Surveillance. Speech. Biometrics. Health data.`
Body (`--type-body`, slate-400 italic to mark it as the refrain):
  `The rule applies to the government.`
  `The company holds the database.`

The body is a two-line refrain. Each line on its own line, with the
line-break visible (use `<br>` or two `<p>` elements). Do NOT collapse
into one sentence.

Visible-text budget: ~16 words total.

Animation:
- `sl-hairline` draws left-to-right on entry, 360ms
- `sl-reveal-2` cascade: heading → body
- Body's two lines reveal with a 180ms gap between them (the refrain
  needs the second line to land separately — match the narration's
  pacing cue at Slide 2)

Justoon: none.

---

### Slide 3 — sl-data (numgrid)  (Body · Receipt · Bend)

Kicker: `DISPATCH №005 · THE RECEIPT · BEND`
Layout: three-column `ms-numgrid` occupying the right ~68% of the
safe-zone. Justoon occupies the left ~32%.

Numgrid (left to right):

| Number (role) | Caption (`--type-kicker`) |
|---|---|
| `99,000` (`--type-h1`) | `Population` |
| `279` (`--type-hero` — THE ANCHOR) | `ICE searches · 3 weeks` |
| `118` (`--type-h1`) | `CBP searches · 3 weeks` |

Foot attribution (`--type-kicker`, slate-600, below the numgrid):
  `Bend, Oregon · 2025 · open-records audit`

Visible-text budget: 3 numbers + 11 supporting words. Hero anchor:
`279`. (Within budget: one hero number + ≤15 supporting words.)

Animation:
- `sl-reveal-3` cascade left-to-right on the three number columns,
  120ms stagger
- `sl-glow` radial slate behind the hero `279` after its column settles
- Subtle Justoon entry (fade + 8px slide-in from left), 360ms,
  triggered after first number column reveals

Justoon: role A.
  Justoon variant: `justoon-point-right.png`
  Justoon placement: per the `slide-receipt .justoon` rule (above) —
  absolute, left:0, bottom, 88cqh tall, pointing into the numbers.

---

### Slide 4 — sl-data (numgrid)  (Body · Receipt · Scale)

Kicker: `DISPATCH №005 · THE RECEIPT · SCALE`
Layout: three-column `ms-numgrid` occupying the right ~68% of the
safe-zone. Justoon occupies the left ~32% (same composition as
Slide 3 — visual consistency is intentional).

Numgrid (left to right):

| Number (role) | Caption (`--type-kicker`) |
|---|---|
| `364,000` (`--type-h1`) | `Ventura · 2 years` |
| `1,600,000` (`--type-hero` — THE ANCHOR) | `San Francisco · 7 months` |
| `4,500` (`--type-h1`) | `Police departments on the network` |

Foot attribution (`--type-kicker`, slate-600, below the numgrid):
  `California · Flock Safety class action filed Feb 2026`

Visible-text budget: 3 numbers + 14 supporting words. Hero anchor:
`1,600,000`. (Within budget.)

Animation:
- `sl-reveal-3` cascade left-to-right on the three number columns,
  120ms stagger — begins AFTER Slide 3's cascade completes (per the
  intensification rule: second data slide draws after first completes)
- `sl-glow` radial slate behind `1,600,000` after its column settles —
  stronger glow than Slide 3 to mark the scale escalation
- Justoon fades in mirroring Slide 3's entry timing

Justoon: role A.
  Justoon variant: `justoon-point-right.png` (consistency with Slide 3)
  Justoon placement: per the `slide-receipt .justoon` rule.

---

### Slide 5 — sl-frames  (Body · Frame)

Kicker: `DISPATCH №005 · THE FRAME`
Three numbered frames `[01]` / `[02]` / `[03]` in a horizontal grid
(at 16:9 / 1:1) or a vertical stack (at 9:16 — handled by the existing
`sl-frames` grid logic).

Frames:

| # | Label (`--type-h2-mid`) | Body line (`--type-body`) |
|---|---|---|
| `[01]` | `THE RULE` | `Constitution binds the government.` |
| `[02]` | `THE BYPASS` | `Government contracts to a vendor.` |
| `[03]` | `THE OUTCOME` | `Rule on paper. Function performed.` |

Visible-text budget: 6 label words + 13 body words = 19. Headline is
the slide's title implied by the frame labels; this slide has no
single anchor element. Use `[02]` BYPASS as the visual anchor — make
its label slightly heavier (apply `--type-h1` to `[02]` only, leaving
`[01]` and `[03]` at `--type-h2-mid`).

Animation:
- `sl-reveal-3` cascade left-to-right (or top-down at 9:16) on the
  three frames, 180ms stagger
- `sl-hairline` draws between adjacent frame columns on entry, 360ms,
  AFTER all three frames have settled — the hairlines visually
  connect the architecture
- `sl-caret` blinking on the `[02]` BYPASS kicker (one of the two
  caret budgets for the deck)

Justoon: none.

---

### Slide 6 — sl-compare  (Body · Anaphora · Speech + Search)

Kicker: `DISPATCH №005 · THE ANAPHORA · SPEECH + SEARCH`
Two-column side-by-side. Each column has a small section label
(`--type-kicker`) above and a paired-statement body (`--type-h2-mid`).

Left column:
  Label: `FIRST AMENDMENT`
  Statement:
    `The Amendment prohibits the order.`
    `CISA placed the call.`

Right column:
  Label: `FOURTH AMENDMENT`
  Statement:
    `The Amendment requires the warrant.`
    `Flock accepted the query.`

Vertical hairline divides the two columns, full safe-zone height.

Visible-text budget: 4 label words + 20 statement words = 24. The
parallel structure between the two columns is the entire visual move —
the second line of each pair (`CISA placed the call` / `Flock accepted
the query`) must visually rhyme. Apply `--type-h2-mid` to both pairs
and right-align the second line of each so the parallel lands.

Animation:
- Vertical hairline draws top-to-bottom on entry, 360ms
- `sl-reveal-2` cascade: left column → right column (180ms stagger)
- Within each column, the two paired lines reveal with a 120ms gap —
  matches the narration's anaphora pacing

Justoon: none.

---

### Slide 7 — sl-compare  (Body · Anaphora · Biometric + Health)

Kicker: `DISPATCH №005 · THE ANAPHORA · BIOMETRIC + HEALTH`
Two-column side-by-side, identical structure to Slide 6.

Left column:
  Label: `BIOMETRIC`
  Statement:
    `Congress can't compel the biometric.`
    `The verification vendor holds it.`

Right column:
  Label: `HEALTH RECORD`
  Statement:
    `HIPAA protects the record.`
    `BetterHelp sold the category.`

Vertical hairline divides the two columns, full safe-zone height.

Visible-text budget: 4 label words + 21 statement words = 25.

**Important:** the narration's climactic refrain at Slide 7
("In each case, the protection was written to govern one party. The
work was contracted to another.") is delivered AURALLY ONLY and does
NOT appear on this slide. The slide visually mirrors Slide 6's
structure and lets the audio carry the climax. Do not add a third
text element.

Animation:
- Vertical hairline draws top-to-bottom on entry, 360ms (mirrors
  Slide 6 for visual continuity)
- `sl-reveal-2` cascade: left column → right column (180ms stagger)
- Within each column, the two paired lines reveal with a 120ms gap
- After both columns settle, hold for ~3s with no further motion —
  this is the climax-pause space; the narration's spoken refrain
  lands during this stillness

Justoon: none.

---

### Slide 8 — sl-frames  (Body · Twist)

Kicker: `DISPATCH №005 · THE TWIST`
Layout: three numbered frames in the LEFT ~45% of the safe-zone,
stacked vertically (not horizontal — the right half is Justoon).
Justoon is the slide's anchor here (role C reaction-as-anchor).

Frames (vertical stack, left half):

| # | Label (`--type-h2-mid`) | Body line (`--type-kicker`) |
|---|---|---|
| `[01]` | `OFF` | `Sheriff disabled federal search · 2023 · in writing` |
| `[02]` | `ON` | `Setting got flipped back on` |
| `[03]` | `UNKNOWN` | `Flock: cause impossible to determine` |

Visible-text budget: 3 labels + 17 body words = 20. **Headline does
NOT use `--type-h1` on this slide — use `--type-h2-mid` for the frame
labels because the Justoon image IS the thumbnail anchor here.**

Animation:
- `sl-reveal-3` cascade top-to-bottom on the three frames, 200ms
  stagger (slower than other slides — the deadpan needs space)
- Justoon enters AFTER all three frames have settled — fade + 8px
  slide-in from the right, 360ms
- After Justoon settles, hold for ~2s before allowing advance
- No glow, no pulse, no caret on this slide. The stillness IS the
  punchline — the deadpan expression carries the joke.

Justoon: role C (reaction-as-anchor).
  Justoon variant: `justoon-react-deadpan.png`
  Justoon placement: per the `slide-twist .justoon` rule (above) —
  absolute, right:0, bottom, 75cqh tall, max-width 55%, object-fit
  contain.

> **Why deadpan, not raised-eyebrow or smirk:** the narration's close
> ("By whom, the company says, can't be known.") is the canonical TCN
> deadpan beat — the absence of expression IS the editorial move. Per
> the §7 picker guidance, deadpan is the default role C variant and
> the specific pick for this beat.

---

### Slide 9 — sl-lead  (Body · Stakes)

Kicker: `DISPATCH №005 · STAKES`
Layout: heading + body occupies the right ~68% of the safe-zone.
Justoon occupies the left ~32%.

Heading (anchor, `--type-h1`):
  `FIVE ACTIONS. CAMERAS STILL ON.`

Body (`--type-body`):
  `Sanctuary policy. Canceled ICE contract.`
  `Open-records audit. Two new resolutions.`
  `Neither of the new ones touches the vendor.`

Visible-text budget: 6 heading words + 18 body words = 24.

Animation:
- `sl-reveal-2` cascade: heading → body
- Body's three lines reveal with 150ms gap between them
- Justoon fades in on slide entry, 360ms, with the same 8px slide-in
  from the left as Slides 3 and 4
- `sl-hairline` draws underneath "FIVE ACTIONS." on the heading after
  the heading settles, 360ms — visually punches the count

Justoon: role A.
  Justoon variant: `justoon-point-open-palm.png`
  Justoon placement: per the `slide-stakes .justoon` rule (which
  reuses the role A CSS) — absolute, left:0, bottom, 88cqh tall.

> **Why open-palm, not point-right:** this is a presentational
> summary, not a single-hero-stat slide. Per the §7 picker guidance,
> open-palm is the "here's the thing" gesture for slides that
> summarize rather than direct attention at one figure.

---

### Slide 10 — sl-lead (bullets)  (Outro · Tease)

Kicker: `DISPATCH №005 · TEASE`
Heading (anchor, `--type-h1`): `READ THE PIECE`
Body (`--type-body`, bulleted list):
  `· $4B in statutory damages`
  `· $7.8M FTC clawback`
  `· The SCOTUS case that ducked`
  `· + the three-word tool that surfaces all four`

Visible-text budget: 3 heading words + 21 bullet words = 24.

Animation:
- `sl-reveal-5` cascade: heading → 4 bullets (5 steps, 150ms stagger)
- The last bullet (the loop-opener) reveals with an extra 200ms gap
  before it — gives the "+ the three-word tool" line emphasis
- `sl-hairline` draws under the heading on entry, 360ms
- No glow, no pulse — the Tease is conversational, not dramatic

Justoon: none.

---

### Slide 11 — sl-end  (Outro · End)

Kicker: `DISPATCH №005 · END`
Heading (anchor, `--type-h1`): `The Civic Node`
URL CTA (`--type-h2-mid`): `drinkyouroj.substack.com`
Tagline (`--type-body`): `Weekly. No hype.`
Disclosure block (`--type-kicker`, slate-600, bottom of safe-zone):
  Standard TCN disclosure copy from the design system end-card.

Visible-text budget: ~15 words (excluding disclosure boilerplate).

Animation:
- `sl-glow` radial slate behind the mark, full intensity
- `sl-mark-pulse` on the mark at 44px, single pulse on entry then
  ambient slow pulse every 4s
- `sl-caret` blinking on the heading kicker (the second of the two
  caret budgets for the deck)
- `sl-reveal-3` cascade: heading → URL CTA → tagline
- Disclosure block fades in last, no cascade, 360ms

Justoon: none.

## Speaker notes (embed as JSON at end of HTML)

Embed as a `<script type="application/json" id="speaker-notes">`
block. One entry per slide. Each entry is the narration text verbatim
from `youtube-narration.md` — no paraphrasing.

```json
[
  {
    "slide": 1,
    "text": "Atlanta passed a sanctuary policy in 2025. Police officers don't help federal immigration enforcement. The city said so on the record.\n\nThat same year, the open-records audit showed three thousand two hundred and fifty-four Border Patrol searches of Atlanta's police cameras.\n\nThe same audit reported both.\n\nThe pattern shows up in four places."
  },
  {
    "slide": 2,
    "text": "Surveillance. Speech. Biometrics. Health data.\n\nIn each one, the Constitution writes a rule about what the government can't do. And in each one, the government hires a private company to do the same thing.\n\nThe rule applies to the government. The company holds the database."
  },
  {
    "slide": 3,
    "text": "Bend, Oregon. Population ninety-nine thousand.\n\nThe police department signed onto Flock, a private camera network used by police agencies. Three weeks later, the captain figured out the federal-search feature was reciprocal. Turn it on to query other cities. Other cities can query yours.\n\nIn those three weeks, federal agencies ran two hundred and seventy-nine immigration searches into Bend's cameras. Customs and Border Protection ran one hundred eighteen.\n\nThat's the floor. The smallest example."
  },
  {
    "slide": 4,
    "text": "Now the scale.\n\nVentura County, California. The sheriff turned the federal-search feature off in 2023, in writing, to comply with state law. Two years later, federal and out-of-state agencies had queried Ventura's cameras three hundred and sixty-four thousand times.\n\nSan Francisco. The class action filed in February says outside agencies accessed police cameras one point six million times. In seven months.\n\nThere are roughly forty-five hundred police departments on this network."
  },
  {
    "slide": 5,
    "text": "Same architecture every time.\n\nThe Constitution writes a rule about the government. So the government finds a private company that isn't bound by the rule. And contracts the work to them.\n\nThe rule still exists on paper.\n\nThe function still gets performed."
  },
  {
    "slide": 6,
    "text": "Watch it work in two directions.\n\nThe First Amendment prohibits the government from ordering speech taken down. So CISA, the federal cybersecurity agency, called the platform. The platform took the post down. Under its own content policy.\n\nThe Fourth Amendment requires a warrant for government searches. So the search ran through Flock's private camera network. No warrant needed to query a private company.\n\nThe First Amendment prohibits the order. CISA placed the call.\n\nThe Fourth Amendment requires the warrant. Flock accepted the query."
  },
  {
    "slide": 7,
    "text": "Two more.\n\nCongress can't compel children to hand over biometric data. So nineteen states passed laws requiring a third-party vendor to collect the face scan. The vendor holds the database. A national security letter reaches it without a judge.\n\nHIPAA protects health records. So a therapy app relabeled its session data as a marketing category. The category isn't HIPAA. The category sold to advertisers.\n\nCongress can't compel the biometric. The verification vendor holds it.\n\nHIPAA protects the record. BetterHelp sold the category.\n\nIn each case, the protection was written to govern one party. The work was contracted to another."
  },
  {
    "slide": 8,
    "text": "Back to Ventura.\n\nThe sheriff turned the federal-search feature off in 2023. In writing. To comply with state law.\n\nSomething turned it back on.\n\nFlock said the cause was impossible to determine. Their own logging system couldn't track which account flipped the setting. The sheriff's own investigation found no one on staff did it.\n\nConstitutional protection. State law. Department policy. All three in alignment.\n\nThe setting still got flipped.\n\nBy whom, the company says, can't be known."
  },
  {
    "slide": 9,
    "text": "In April 2026, the Atlanta City Council passed two more resolutions.\n\nOne opposed ICE detention. The other set new guidelines for Atlanta police.\n\nThat makes five. A sanctuary designation. A canceled ICE contract. An open-records audit. Two more resolutions stacked on top.\n\nNeither of the new ones mentions Flock. Neither touches the vendor contract.\n\nThe cameras are still on.\n\nThe next agency querying them doesn't have to read a single Atlanta document."
  },
  {
    "slide": 10,
    "text": "The piece covers more than what's in this video.\n\nIt names the lawsuit putting four billion dollars of statutory damages on one city's surveillance vendor. It names the federal case that pulled seven point eight million dollars back from a therapy app for selling session data. It names the Supreme Court case that didn't reach the constitutional question.\n\nAnd it names the one tool that already works. The one method of accountability that surfaced every story in this video.\n\nThree words. The piece tells you what they are."
  },
  {
    "slide": 11,
    "text": "The Civic Node. Subscribe free at drinkyouroj.substack.com.\n\nWeekly. No hype."
  }
]
```

## Output requirements

- Single bundled HTML file named `dispatch-005.html`.
- All external resources loaded relatively (`../colors_and_type.css`,
  etc.). Justoon PNGs loaded as `assets/justoon-*.png` or whatever
  path the project uses for image assets.
- Speaker notes embedded as JSON in the document.
- Self-contained: opens in any browser, plays the full deck via
  `deck-stage.js`.
- No external CDN calls. No remote fonts. No analytics.
- Renders correctly at 16:9 (1920×1080), 9:16 (1080×1920), and 1:1
  (1080×1080) from this same file. Test by resizing the browser
  window to each target aspect before recording — type sizes and
  safe-zone content stay identical; only the empty viewport margin
  changes.
- Every slide passes the thumbnail test: scale the browser window to
  240px wide and confirm the slide's anchor element is legible.
- Every slide passes the visible-text budget (≤25 visible words OR
  one hero number + ≤15 supporting words). Speaker notes excluded.
- No panel-splits in this deck — the upstream narration was re-paced
  to land under budget on every slide.
