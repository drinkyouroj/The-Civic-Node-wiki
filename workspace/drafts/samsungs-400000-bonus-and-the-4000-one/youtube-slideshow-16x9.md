# Claude Design prompt — TCN Dispatch №006 slideshow (16:9-native)

> **Artifact header (skill-side, delete before pasting if you like):**
> - **Format:** beat-segmented *motion* deck (build-on-reveal), NOT the legacy cascade-then-hold deck. 11 narration scenes → 109 beat-steps (synced to narration v7: Scene 09 is now the "No valve to grab" personal landing, Scene 10 the TEASE, Scene 11 the END). See "Motion model" below.
> - **Aspect:** **16:9-native (1920×1080), single frame.** This is the primary YouTube upload, designed to FILL the widescreen frame — no centered-square safe zone, no pillarboxing. The square-safe sibling `youtube-slideshow.md` in this same folder remains the source for 1:1 / 9:16 social cuts. **Do not derive other aspects from THIS file.**
> - **Justoon mode:** OFF (an animated face is composited into the reserved rail in post). Reserved-face columns at 16:9:
>   - Slides 03, 05, 06 (Receipt) + 08 (Stakes) → `.has-face-left`: rail = **left 30%** of the frame; content fills the right ~64%.
>   - Slide 07 (Twist) → `.has-face-right`: rail = **right 32%**; text builds in the left ~60%.
>   - Scenes 01, 02, 04, 09, 10, 11 → **full-bleed typography, no rail** (the big rhetorical beats get the whole frame).
>   - The rail is a reusable `.has-face-*` modifier: **any slide can take a face in post without re-layout.** Build the listed slides as face slides; leave the rest full-bleed unless told otherwise.

## Context

You are building an HTML slideshow for The Civic Node, Dispatch №006:
"Samsung's $400,000 Bonus, and the $4,000 One." The slideshow is the
visual companion to a ~6:30 YouTube narration video (trailer-format).
Viewers watch the slides while listening to the narration as audio. This
build targets the **16:9 (1920×1080) YouTube upload**.

This deck uses a **build-on-reveal motion format**. Each of the 11 scenes
below is one logical slide (one kicker, one speaker-notes entry), but its
content is revealed **one beat at a time** — one advance step per spoken
line — so the screen changes roughly every 2–3 seconds and never sits
static for longer. This is deliberate. Read the "Motion model" section
before building any slide.

## Inputs (attached / uploaded to this Claude Design project)

Upload the TCN design system bundle (`The Civic Node — Design System.zip`,
already on disk at `~/Documents/`) to this project before running this
prompt. Specifically:

- `colors_and_type.css` — the brand CSS variable system. Load at runtime.
- `slides.css` — slide-specific styles (sl-title, sl-section, sl-lead,
  sl-data, sl-frames, sl-compare, sl-quote, sl-end).
- `deck-stage.js` — kinetic engine. Load via `<script src="deck-stage.js">`.
- `assets/mark.svg`, `assets/lockup-dark.svg` — brand marks.
- `slides/deck.html` — reference template; mimic its slide structure.

No Justoon / character PNGs are used in this deck. The presenter composites
an animated face into the reserved rail in post-production — so the deck
must LEAVE that column empty (see "Reserved face-space layout" below and
the per-scene notes). Do not fill the reserved region with text or
decoration.

If any design-system file above is missing, halt and ask before generating
the HTML.

## Brand requirements (non-negotiable)

- One typeface: Courier Prime.
- Palette: slate-400 (`#557FA3`) / slate-600 / black / twilight only. No
  other colors.
- No emoji, no icon fonts, no exclamation points, no shadows on dark.
- Middle dot `·` as the kicker separator. Never `|`, never `/`.
- Easing on every animation: `cubic-bezier(0.2, 0, 0, 1)`.
- Durations: 120ms, 200ms, or 360ms. Nothing longer than 500ms.
- No bounce, no spring, no rainbow gradients.
- Kickers: mono, wide-tracked (0.18em), all-caps, slate-400 on dark.
- Zero-padded dispatch number (`№006`, not `№6`).

## 16:9-native frame & safe zone (non-negotiable)

This deck is built for ONE frame: **16:9 (1920×1080)**, the primary YouTube
upload. It does NOT render at 9:16 or 1:1 — those cuts come from the
square-safe `youtube-slideshow.md` sibling. Design content to **fill the
widescreen frame**; there is no centered-square safe zone here.

It must still be readable at thumbnail playback (~240px wide on a phone
card): the per-scene thumbnail anchor below stays legible when the frame is
scaled to 240px.

The mechanism: each `.slide` uses `container-type: size`, and content lives
in a `.stage` that fills the frame (inset by a small uniform margin). On
face slides, the `.stage` shifts to one side, leaving a full-height rail
column EMPTY for the composited face. Layout is built for 16:9 — no
aspect-ratio media queries, no square safe zone.

- `.slide { container-type: size; }` so cq-units scale to the slide, not
  the viewport.
- Critical content (kicker, headline, body, hero numbers, source
  attributions, CTA, disclosure) lives inside `.stage`. On `.has-face-*`
  slides the reserved rail stays empty (the face is composited in post).
- Decorative elements (brand mark, `sl-hairline`, `sl-glow` radial, slide
  background fill) may extend to the frame edges, including across the rail.
- No fixed-pixel widths on layout containers.

**Frame tokens & type scale (apply per slide via container-query units):**

```css
.slide {
  container-type: size;
  --pad:           5cqh;                          /* uniform frame margin */
  --rail:          30cqw;                          /* reserved face column width */
  --gutter:        4cqw;                           /* rail ↔ content gap */
  --type-hero:     clamp(96px, 34cqh, 520px);      /* full-bleed beats fill the frame */
  --type-hero-col: clamp(80px, 26cqh, 400px);      /* hero inside the content column */
  --type-h1:       clamp(34px, 11cqh, 168px);
  --type-h2-mid:   clamp(26px,  8cqh, 120px);
  --type-body:     clamp(16px,  4.5cqh, 64px);
  --type-kicker:   clamp(11px,  2.4cqh, 34px);
}
```

No element renders below `--type-kicker`. **Full-bleed hero beats** (Scene
01's `100 : 1`, the refrains, `NOT THE SAME MONEY`, `NO VALVE TO GRAB`) use
`--type-hero` and fill the frame. **Column heroes** (the data-slide numbers,
sitting in the right ~64% content column) use `--type-hero-col`. Because the
column is now ~1150px wide (not trapped in an 1080-wide square), long strings
like `$13.77 BILLION` fill the column and may stack to two lines at
`line-height: 0.85`.

**Text-wrap directive:** every `.headline` and `.caption` uses
`text-wrap: balance`.

**Slide zone modifier class.** Each `.slide` gets a zone modifier class:
`slide-hook`, `slide-thesis`, `slide-receipt`, `slide-frame`,
`slide-stakes`, `slide-twist`, `slide-tease`, `slide-end`. Face slides
additionally get `has-face-left` or `has-face-right`. Example:
`<section class="slide slide-receipt has-face-left" id="slide-03">`.

**Reserved face-space layout** (no character image is rendered — the
presenter composites an animated face into the empty rail in post). The rail
is a reusable modifier; the content `.stage` shifts away from it.

```css
/* Content stage — fills the frame by default (full-bleed slides) */
.slide .stage {
  position: absolute;
  inset: var(--pad);
  display: flex; flex-direction: column; justify-content: center; gap: 2cqh;
}

/* Face LEFT (Receipt / Bill / Stakes) — content shifts right; LEFT rail stays EMPTY */
.slide.has-face-left .stage {
  left: calc(var(--pad) + var(--rail) + var(--gutter));
}

/* Face RIGHT (the Twist) — content stays left; RIGHT rail stays EMPTY */
.slide.has-face-right .stage {
  right: calc(var(--pad) + var(--rail) + var(--gutter));
}

/* Column heroes fill the content column */
.has-face-left .hero-num, .has-face-right .hero-num {
  font-size: var(--type-hero-col); line-height: 0.85; color: #fff;
  font-weight: 700; letter-spacing: -0.02em;
}
/* Full-bleed heroes use the larger scale */
.hero-num.full-bleed { font-size: var(--type-hero); line-height: 0.85;
  color: #fff; font-weight: 700; letter-spacing: -0.02em; text-align: center; }
.stat-label {
  font-size: var(--type-body); color: var(--paper);
  margin-top: 0.4em; max-width: 92%; line-height: 1.15; text-wrap: balance;
}

/* Twist text column — wider than the square deck (~60%), so the headline
   of record steps up to --type-h1 (was --type-h2-mid in the square build). */
.slide-twist .headline {
  font-size: var(--type-h1); line-height: 1.04; color: #fff; text-wrap: balance;
}
.slide-twist .caption {
  font-size: var(--type-kicker); color: var(--slate-400);
  border-left: 2px solid var(--slate-400); padding-left: 0.6em;
  letter-spacing: 0.05em; text-wrap: balance;
}
/* The rail column (var(--rail) wide, full height, on the reserved side)
   stays EMPTY — no text, no decoration. The face is composited there in post. */
```

Keep the rail genuinely empty on `.has-face-*` slides — decorative hairlines /
glow may cross it, but no legible content goes there. **Any full-bleed slide
can be converted to a face slide later** by adding `has-face-left` /
`has-face-right` (the presenter may do this in post if a full-bleed slide
reads too static); building them now is not required beyond the listed scenes.

**Thumbnail-anchor rule:** every scene has exactly one element at
`--type-hero` / `--type-hero-col` (or `--type-h1` on Slide 07) occupying
≥25% of frame height. This is the element the deck rests on at each scene's
final beat — what a 240px phone card catches. Per-scene anchor named below.

**Visible-text budget:** at any single resting beat, ≤25 visible words on
screen, OR one hero number + ≤15 supporting words. Build-on-reveal makes
this easy — only a few elements rest at once, and the composition resets
named below keep each resting frame inside budget. Speaker notes and the
reserved rail are not counted.

---

## Motion model (read before building any slide) — build-on-reveal

This is the load-bearing departure from the legacy deck. Do NOT render
each scene as a static slide with a one-time entrance cascade.

**The rule:** within each scene, reveal the listed elements **one beat at
a time, one advance step per beat.** Each beat's element enters with a
single `sl-reveal` (200ms, the standard easing). After a beat reveals, the
screen **holds for ~2–3 seconds** (the presenter is speaking that beat's
line), then the next advance reveals the next beat's element. The screen
must never sit static longer than ~3 seconds.

- **Advance granularity = one step per beat.** Use `deck-stage.js`'s
  existing step/fragment advance if it supports per-element stepping;
  otherwise implement each beat as its own panel-state and advance with
  the engine's normal slide-advance. Either way: **one advance = one beat
  = one new element on screen.** No new engine primitives.
- **Primary advance mode = manual.** The presenter advances (arrow key /
  click) at each beat as they speak its line. This gives exact voice-sync
  for live VO recording. Build the deck so manual stepping works.
- **Auto-play fallback = `data-advance-at`.** Optionally also emit
  approximate `data-advance-at="M:SS"` cumulative timestamps per beat (see
  each scene) so the deck can auto-play unattended. These are estimates
  tuned to ~140 wpm; the presenter re-times at record if auto-playing.
- **Elements accumulate within a composition group, then reset.** Within a
  group, each new beat's element joins the ones already on screen (the
  picture assembles). At the **[RESET]** markers below, clear the prior
  group's elements (keeping only the named carry-forward anchor) before
  the next beat reveals — this keeps every resting frame inside the ≤25-word
  budget and keeps the composition legible at thumbnail size.
- **Animation intensification still applies** (sl-glow behind the dominant
  number, sl-mark-pulse on title/end/twist, hairline draws, two `sl-caret`
  blinks total) — layered on top of the per-beat reveals, per each scene.
- **Guardrails unchanged:** easing `cubic-bezier(0.2,0,0,1)`, durations
  120/200/360ms, no bounce/spring/glow-rainbow, slate palette only.

`element:` cues below name **what** lands each beat, never **how** it
animates beyond the standard `sl-reveal`. You own the exact entrance.

---

## Slide-by-slide specification

Beat lines below are quoted from the narration (the presenter's spoken
line); the `→` names the on-screen element that reveals on that beat.

---

### Scene 01 — `sl-title` · HOOK · 10 beats · full-bleed, no face

**Kicker:** `DISPATCH №006 · HOOK`
**Thumbnail anchor (resting state):** `100 : 1` at `--type-hero` (full-bleed,
centered), with `$400,000` and `$4,000` at `--type-h1` flanking the two figures.
**Visible budget:** the two $ figures + `100 : 1` are the resting anchors;
the small stamps/labels render at `--type-kicker` (decorative).

Composition group (assembles the two-worker frame, one dim-down at B10):

- **B1** "Two workers walk out of the same Samsung plant in Korea." → two figure silhouettes + Samsung plant outline behind them
- **B2** "Same shift." → `SAME SHIFT` stamp (kicker-size)
- **B3** "They worked it a hundred yards apart." → `100 YARDS APART` + a gap marker between the figures
- **B4** "One of them builds memory chips." → left figure lights; label `MEMORY CHIPS`
- **B5** "This year, his bonus runs toward four hundred thousand dollars." → `$400,000` lands over the left figure (`--type-h1`). **Hold a beat longer here than B7.**
- **B6** "The other builds phones and televisions." → right figure lights; label `PHONES & TVs`
- **B7** "His bonus comes to about four thousand." → `$4,000` over the right figure, visibly smaller
- **B8** "Same company." → `SAME COMPANY` stamp
- **B9** "Same shift." → `SAME SHIFT` stamp echoes
- **B10** "A hundred to one." → **[RESET to anchors]** dim the labels + stamps to faint; `100 : 1` lands center at `--type-hero` (full-bleed) with `sl-glow` radial slate behind it; `$400,000` / `$4,000` stay as the flanking comparison. **Hold ~1.5s.**

**Animation:** `sl-mark-pulse` on the brand mark throughout; per-beat
`sl-reveal`; `sl-glow` behind `100 : 1` on B10; hairline draws under the
two-figure row on B1.

---

### Scene 02 — `sl-lead` · THESIS · 9 beats · full-bleed, no face

**Kicker:** `DISPATCH №006 · THESIS`
**Thumbnail anchor:** `WHO GETS TO SAY NO?` at `--type-h1` (final beat).
**Visible budget:** ≤22 words resting; reset after B7.

Group 1 (the split):
- **B1** "That gap is the whole AI boom in one picture." → title card `THE AI BOOM` (the 100:1 from Scene 01 morphs into it)
- **B2** "One boom hit two different bottlenecks." → one arrow splits into two diverging paths
- **B3** "Two places where everything backs up because one thing is in short supply." → a pinch-point icon on each path
- **B4** "At the first one, the workers walked off with a fortune." → path 1 ticks up; label `A FORTUNE`
- **B5** "At the second one, the cost landed on people who never got a vote." → path 2 ticks down; labels `THE COST` · `NO VOTE`

Group 2 **[RESET — keep nothing; this is the turn]**:
- **B6** "Same boom." → `SAME BOOM` stamp
- **B7** "Opposite endings." → two arrows pull apart; `OPPOSITE ENDINGS`
- **B8** "And one question decides which end you land on." → a large `?` begins forming
- **B9** "Who gets to say no?" → `WHO GETS TO SAY NO?` full at `--type-h1`, `sl-glow` behind it. **[REFRAIN — hold ~1s.]**

**Animation:** hairline draws left-to-right on B1; per-beat `sl-reveal`;
`sl-caret` blink on the THESIS kicker (**caret 1 of 2 in the deck**, paired
with Slide 10); `sl-glow` behind the refrain on B9.

---

### Scene 03 — `sl-data` (ms-numgrid) · THE RECEIPT · THE CHOKEPOINT · 13 beats · `.has-face-left` (rail 30%)

**Kicker:** `DISPATCH №006 · THE RECEIPT · THE CHOKEPOINT`
**Reserved face-space:** keep the **left 30%** of the frame empty
(`.has-face-left`) — the presenter composites the animated face there. Stats
build in the right ~64% content column.
**Thumbnail anchor:** `10.5%` at `--type-hero-col` with `sl-glow` (resting state).

Group 1 — the irreplaceable input **[RESET after B4]**:
- **B1** "So why did the chip worker win?" → the content stat-block frame opens (left rail stays clear for the face)
- **B2** "Because he was sitting on the one part the whole boom can't run without." → a single chip lights in the stat-block
- **B3** "The fast memory that stacks inside every AI chip." → stacked-memory diagram + gloss label "the fast memory in every AI chip"
- **B4** "Right now, it's sold out." → `SOLD OUT` stamp across the chip

Group 2 — Samsung's weight **[RESET after B8]**:
- **B5** "And Samsung is not a normal company." → a `SAMSUNG` scale bar starts to grow
- **B6** "It's almost a quarter of South Korea's entire exports." → `~23% OF KOREA'S EXPORTS` (pie wedge fills)
- **B7** "So one walkout in that plant doesn't dent a single company's quarter." → a small "one company's quarter" dent icon, crossed out
- **B8** "It stalls the AI buildout for the whole planet." → globe + ripple, `WORLDWIDE BUILDOUT — STALLED`

Group 3 — the ask and the win (builds to the hero):
- **B9** "Their profit had jumped seven hundred and fifty-five percent in a year." → `+755%` counts up (sl-chart-draw style)
- **B10** "So the workers asked for a cut." → a hand closes on a valve, `ASKED`
- **B11** "And they got it." → `GRANTED` + check
- **B12** "Ten and a half percent of the division's profit." → `10.5%` hero number lands (`--type-hero-col`), `sl-glow` behind it
- **B13** "Every year. For ten years." → `EVERY YEAR ×10` (ten ticks fill a row beneath the hero). **Hold ~1s.** Resting frame: `10.5%` hero + `+755%` supporting + `EVERY YEAR ×10` (all in the right content column; left rail blank for the face).

**Animation:** numerals reveal `sl-chart-draw` style; `sl-glow` behind
`10.5%`; per-beat `sl-reveal`.

---

### Scene 04 — `sl-frames` · THE FRAME · WHO CAN SAY NO · 12 beats · full-bleed, no face

**Kicker:** `DISPATCH №006 · THE FRAME · WHO CAN SAY NO`
**Thumbnail anchor:** `THE POWER TO SAY NO` at `--type-h1` (B8), then the
refrain at B11.
**Visible budget:** two-slot frame build; reset after B6.

Group 1 — the two ingredients **[RESET after B6, keep nothing]**:
- **B1** "And this is the part that shows up in every other story like it." → faint repeating motif, `THE PATTERN`
- **B2** "The chip workers had two things." → `TWO THINGS` + two empty slots `[ ] [ ]`
- **B3** "A union." → slot 1 fills: `A UNION`
- **B4** "And a product nobody could buy anywhere else." → slot 2 fills: `THE ONLY SUPPLY`
- **B5** "Put those together, and they could shut the whole line down." → the two slots merge into `STOP THE LINE`
- **B6** "So when they asked for a cut, the answer had to be yes." → `YES` lands

Group 2 — the lesson:
- **B7** "That's what this comes down to." → frame tightens to center
- **B8** "The power to say no, and make it stick." → `THE POWER TO SAY NO` at `--type-h1`, hairline above it
- **B9** "The bonus is just the receipt." → a small `$` receipt slip
- **B10** "So hold onto the question." → the `?` returns
- **B11** "Who gets to say no?" → `WHO GETS TO SAY NO?` **[REFRAIN]**
- **B12** "Because the rest of this boom is full of people who can't." → a crowd of faded, faceless figures fills behind the refrain. **Hold ~1s.**

**Animation:** per-beat `sl-reveal`; hairline above `THE POWER TO SAY NO`
on B8. No glow — this is a quieter scene (the refrain carries it).

---

### Scene 05 — `sl-data` · THE RECEIPT · THE OTHER CHOKEPOINT · 13 beats · `.has-face-left` (rail 30%)

**Kicker:** `DISPATCH №006 · THE RECEIPT · THE OTHER CHOKEPOINT`
**Reserved face-space:** left 30% of the frame empty (`.has-face-left`, face
composite); content builds in the right ~64% column.
**Thumbnail anchor:** `BUTLER, PA · 1 MILL` (B8) → then `WITH ONE
DIFFERENCE` cliffhanger (B13) as the resting state.
**Note:** B10–B11 are a verbatim quote — treat as an embedded `sl-quote`
moment (hairline above, attribution below), then return to the chokepoint
comparison.

Group 1 — follow the power **[RESET after B5]**:
- **B1** "Now follow the electricity instead of the chips." → a power line traces across the content column, away from the chips (left rail stays clear for the face)
- **B2** "It leads straight to the second bottleneck." → bottleneck-2 icon highlights at the line's end
- **B3** "Every data center needs a giant transformer before it can switch on." → data center + transformer icon
- **B4** "That's the equipment that moves power across the grid." → gloss label on the transformer, "moves power across the grid"
- **B5** "The wait for a big one has stretched to four years." → wait-meter counts up `2.5 YRS → 4 YRS` (sl-chart-draw style), `sl-glow` behind `4 YEARS`

Group 2 — the one mill **[RESET after B8]**:
- **B6** "And it gets stranger." → the frame narrows into a funnel
- **B7** "The special steel inside that transformer's core comes from exactly one factory in the entire United States." → US map, a single dot
- **B8** "One mill, in Butler, Pennsylvania." → pin drops: `BUTLER, PA · 1 MILL`

Group 3 — the CEO quote **[RESET after B11 — sl-quote treatment]**:
- **B9** "The CEO of that company says it plainly." → a quote frame opens (hairline above)
- **B10** "No AI without electricity." → quote line 1 (`--type-h1`)
- **B11** "And no electricity without transformers." → quote line 2 + attribution `— Cleveland-Cliffs CEO`

Group 4 — the comparison + cliffhanger:
- **B12** "The grid is a chokepoint, exactly like the memory plant." → two chokepoint icons side by side (memory plant · grid)
- **B13** "With one difference." → one icon flips state; `WITH ONE DIFFERENCE`. **Cliffhanger — hold ~1s.**

**Animation:** per-beat `sl-reveal`; `sl-chart-draw` on the wait-meter;
`sl-glow` behind `4 YEARS`; hairline above the quote (B9). This is the
deck's **second** data slide — its number draws fire *after* Scene 03's
have completed (they're separate slides, so this is automatic).

---

### Scene 06 — `sl-data` · THE RECEIPT · THE BILL · 10 beats · `.has-face-left` (rail 30%)

**Kicker:** `DISPATCH №006 · THE RECEIPT · THE BILL`
**Reserved face-space:** left 30% of the frame empty (`.has-face-left`, face
composite); content, including the `$13.77 BILLION` hero, builds in the right
~64% column.
**Thumbnail anchor:** `$13.77 BILLION` at `--type-hero-col` with `sl-glow`
(B4), carried forward; final resting frame is the `A UNION` / `A BILLING
ADDRESS` matched pair.

Group 1 — the number **[RESET after B5, carry forward `$13.77 BILLION`]**:
- **B1** "The difference is that nobody here has a hand on the valve." → a valve with no hand on it (content column; left rail stays clear for the face)
- **B2** "The grid operator for thirteen eastern states ran its auctions for future power." → `PJM · 13 EASTERN STATES` + gloss "the grid operator" + map
- **B3** "The math came back ugly." → a ledger, figures start to tick
- **B4** "Data-center demand added almost fourteen billion dollars to customer bills." → `$13.77 BILLION` hero counts up (`--type-hero-col`), `sl-glow` behind it. **Hold a beat.**
- **B5** "Wholesale power, up more than seventy-five percent in a single year." → `+75.5%` bar shoots up

Group 2 — who absorbs it (ends on the matched pair):
- **B6** "That lands on families in Ohio and Virginia." → Ohio + Virginia outlines, small house icons
- **B7** "They never voted on the data centers driving the number." → `NO VOTE` stamp
- **B8** "They just pay more for the same electricity." → a power bill with a rising figure
- **B9** "The chip workers had a union." → `A UNION` card lands left (callback)
- **B10** "The person opening that power bill has a billing address." → `A BILLING ADDRESS` lands beside it, **equal screen-weight, a hairline between the two**. **Hold ~1.5s.** Resting frame: the matched pair (this is the scene's payoff).

**Animation:** per-beat `sl-reveal`; `sl-glow` behind `$13.77 BILLION`;
hairline between `A UNION` and `A BILLING ADDRESS` (the two-up compare beat).

---

### Scene 07 — `sl-compare` (before/after) · THE TWIST · IT DOESN'T ROLL DOWNHILL · 11 beats · `.has-face-right` (rail 32%)

**Kicker:** `DISPATCH №006 · THE TWIST · IT DOESN'T ROLL DOWNHILL`
**Reserved face-space:** keep the **right 32%** of the frame empty
(`.has-face-right`) — the presenter composites the animated face there,
ideally a deadpan / flat register to match the dry correction. Text builds in
the left ~60% content column.
**Thumbnail anchor:** `NOT THE SAME MONEY` at `--type-h1` (B11), in the left
text column (stepped up from the square deck's `--type-h2-mid` — the wider
16:9 column carries it). No character image renders at build time; the face
is added in post, so this text anchor carries the 240px thumbnail test.
**Layout:** `.has-face-right` — text in the left ~60% `.stage`; the right 32%
rail stays empty. The headline of record is `NOT THE SAME MONEY` (B11).

Group 1 — the easy story **[RESET after B5]**:
- **B1** "Here's where the easy version of this story falls apart." → a clean, tidy arrow drawn across the left text column (right rail stays clear for the face)
- **B2** "You'd think the chip workers' bonus just gets passed down to you." → arrow labeled `BONUS → YOU`
- **B3** "Higher chip prices, higher everything, your bill goes up." → a chain of up-arrows
- **B4** "Clean and simple." → `CLEAN & SIMPLE` (the easy story drawn neat)
- **B5** "It doesn't work that way." → the arrow snaps; a slate `✕` over it

Group 2 — the mechanism:
- **B6** "The bonus is a slice of profit." → a pie with one slice lit, `PROFIT`
- **B7** "It comes out of what's left after the chips sell, not out of the price stamped on each one." → `AFTER THE SALE` lit; a price tag dims out
- **B8** "So his raise did not pay for your bill." → line `HIS RAISE → YOUR BILL`, crossed out
- **B9** "And your bill did not fund his raise." → reverse line `YOUR BILL → HIS RAISE`, crossed out
- **B10** "They come out of the same boom." → both trace back to one source, `THE SAME BOOM`
- **B11** "They are not the same money." → `NOT THE SAME MONEY` lands at `--type-h1` as the headline; two separate money stacks with a gap between them; `sl-glow` behind it. **Longest hold in the deck (~1.5s) — this is the funnel's payoff line.**

**Animation:** per-beat `sl-reveal`; `sl-mark-pulse` ambient on the brand
mark (Twist earns the extra weight); `sl-glow` behind `NOT THE SAME MONEY`
on B11.

---

### Scene 08 — `sl-lead` · THE STAKES · THE PLAYBOOK TRAVELS · 9 beats · `.has-face-left` (rail 30%)

**Kicker:** `DISPATCH №006 · THE STAKES · THE PLAYBOOK TRAVELS`
**Reserved face-space:** left 30% of the frame empty (`.has-face-left`, face
composite); content builds in the right ~64% column.
**Thumbnail anchor:** `+30%` at `--type-h1` (B4), then the `ORGANIZE / OR
THE BILL` split as the resting frame.

Group 1 — the spread **[RESET after B6, keep nothing]**:
- **B1** "And this is already spreading." → a ripple spreading across the content column over a faint world map (left rail stays clear for the face)
- **B2** "Within days of the Samsung vote," → a calendar tick, `DAYS LATER`
- **B3** "TSMC, the one other chipmaker with the same kind of pull," → `TSMC` label + gloss "the one with the same kind of pull"
- **B4** "told its own staff their profit-sharing would jump more than thirty percent." → `+30% PROFIT-SHARING` counts up (`--type-h1`)
- **B5** "In the US, two of the biggest unions are studying exactly what Samsung's workers just pulled off." → `UAW + CWA — STUDYING IT` over a US outline
- **B6** "There's talk of an AI dividend showing up at company shareholder meetings next year." → `AI DIVIDEND — next proxy season?`

Group 2 — the same split travels (ends on the asymmetry):
- **B7** "So the same split travels with it." → the diverging-split icon recurs
- **B8** "Where workers can organize, they write themselves a claim on the boom." → `ORGANIZE → a claim on the boom`, hairline beneath
- **B9** "Where they can't, the bill just shows up in the mailbox." → a mailbox; a bill drops in; `OR THE BILL`. **Hold ~1s.**

**Animation:** per-beat `sl-reveal`; hairline beneath the `ORGANIZE` line
(B8). No glow.

---

### Scene 09 — `sl-lead` · THE STAKES · NO VALVE TO GRAB · 10 beats · full-bleed, no face

**Kicker:** `DISPATCH №006 · THE STAKES · NO VALVE TO GRAB`
**Thumbnail anchor:** `NO VALVE TO GRAB` at `--type-hero` (final beat — overlaid in the empty left space beside the lone ratepayer, image 006-05).
**Funnel mechanism:** this is v7's emotional landing — the author's own power
bill, the proximity-irrelevance beat, then the two-workers callback and the
valve bookend that echoes the cold open. The informational open loops are held
for the TEASE (Scene 10); this scene resolves the *feeling*, not the facts.

The personal turn:
- **B1** "The four hundred thousand dollar bonus is the headline." → hero-number `$400,000`, label `the headline`
- **B2** "The thing I actually feel is a line on my own power bill." → a power-bill document with a rising line (`my own power bill`)
- **B3** "And I don't live anywhere near a data center." → a proximity map: a marked house in a dashed ring, a far data center, a dotted distance line (`not anywhere near a data center`)
- **B4** "You don't have to live near one for the boom to reach the bill." → stamp `YOU DON'T HAVE TO LIVE NEAR ONE`
- **B5** "I'm not the four hundred thousand dollar worker here. Odds are you aren't either." → a single dim figure, `$400,000` faint above (`not me · probably not you`)

The two-workers callback **[image 006-01 returns]**:
- **B6** "So picture those two workers walking out of the plant again." → 006-01 standalone (the cold-open image, full-bleed, no overlay)
- **B7** "Even the four thousand dollar guy had a union and a vote. He was still inside the deal." → 006-01 backdrop, overlay `$4,000 · UNION · VOTE` / `still inside the deal`
- **B8** "The person opening that power bill was never inside it." → 006-05 standalone (the lone ratepayer, full-bleed, no overlay)

The valve bookend:
- **B9** "The chip workers had a hand on the valve. And they turned it." → a bright valve wheel, rotated (turned), small turn-arrow (`they turned it`) — the payoff to Scene 06's dim `no hand on the valve`
- **B10** "The rest of us are still standing somewhere with no valve to grab." → 006-05 backdrop, `NO VALVE TO GRAB` at `--type-hero` overlaid in the empty left space, `sl-glow` behind. **Hold ~2s — the emotional payoff before the TEASE turn.** [REFRAIN — valve bookend; recurrence rides the valve motif, so the inverted refrain treatment stays reserved for `WHO GETS TO SAY NO?`]

**Animation:** per-beat `sl-reveal`; the 006-01/006-05 image beats cross-dissolve; `sl-glow` behind `NO VALVE TO GRAB`.

---

### Scene 10 — `sl-lead` (bullet listing) · TEASE · 7 beats · full-bleed, no face

**Kicker:** `DISPATCH №006 · TEASE`
**Thumbnail anchor:** `WHAT'S NOT IN THIS VIDEO` (header card, B1).
**Funnel mechanism:** names what the video deliberately did NOT cover (the cuts),
then routes to the article. One cut per beat. (The April "called it wrong"
confession was cut from the flagship into the 6/10 paid note, so it is no longer
teased.)

- **B1** "I kept the biggest pieces for the article." → header card `WHAT'S NOT IN THIS VIDEO`
- **B2** "A one-paragraph deal from nineteen fifty-one that this contract quietly rhymes with." → bullet `[01] THE 1951 ECHO` (one-paragraph document silhouette)
- **B3** "Korea's plan to mail every citizen a check funded by AI tax money." → bullet `[02] THE CITIZEN DIVIDEND` (a mailed check)
- **B4** "The fracture inside Samsung, where the phone and TV workers backed this at twenty-one percent." → bullet `[03] THE FRACTURE` (a cracked badge, `21%`)
- **B5** "The shareholders now suing to tear the whole deal up." → bullet `[04] THE SHAREHOLDER SUIT` (a gavel)
- **B6** "And the question I can't close. Does Samsung make the cloud giants pay for it?" → a cloud with an arrow to a `?` (`who pays — the cloud giants?`)
- **B7** "It's all in the piece." → `READ THE PIECE` + the Substack article cover thumbnail

**Animation:** per-beat `sl-reveal` (the cut bullets land 120ms quick).

---

### Scene 11 — `sl-end` · END · 5 beats · full-bleed, no face

**Kicker:** `DISPATCH №006 · END`
**Thumbnail anchor:** `The Civic Node` wordmark / the Substack URL.

- **B1** "The full piece is on Substack." → Substack wordmark / article cover
- **B2** "The two workers, the power bill, and the one question that decides who wins this boom." → three quick recap icons: two figures · a power bill · `?`
- **B3** "The Civic Node." → The Civic Node logo lockup at `--type-h1`, `sl-mark-pulse` on the mark (44px), `sl-glow` radial slate behind it
- **B4** "Subscribe free at drinkyouroj.substack.com." → `drinkyouroj.substack.com` + subscribe affordance
- **B5** "Weekly. No hype." → tagline `Weekly. No hype.` **Hold the end state — no transition out.**

**Foot row:** `The Civic Node` · `2026·06·02 · 7 MIN`
**Animation:** per-beat `sl-reveal`; `sl-mark-pulse` + `sl-glow` on the
mark (B3); `sl-caret` blink on the END kicker (**caret 2 of 2**, paired
with Slide 02's THESIS kicker).

---

## Speaker notes (embed as JSON at end of HTML)

Embed as a `<script type="application/json" id="speaker-notes">` block at
the end of `<body>`. **One entry per narration scene (11 total), NOT one
per beat.** Each entry is the scene's narration verbatim from
`youtube-narration.md`.

```json
[
  { "slide": 1, "text": "Two workers walk out of the same Samsung plant in Korea. Same shift. They worked it a hundred yards apart. One of them builds memory chips. This year, his bonus runs toward four hundred thousand dollars. The other builds phones and televisions. His bonus comes to about four thousand. Same company. Same shift. A hundred to one." },
  { "slide": 2, "text": "That gap is the whole AI boom in one picture. One boom hit two different bottlenecks. Two places where everything backs up because one thing is in short supply. At the first one, the workers walked off with a fortune. At the second one, the cost landed on people who never got a vote. Same boom. Opposite endings. And one question decides which end you land on. Who gets to say no?" },
  { "slide": 3, "text": "So why did the chip worker win? Because he was sitting on the one part the whole boom can't run without. The fast memory that stacks inside every AI chip. Right now, it's sold out. And Samsung is not a normal company. It's almost a quarter of South Korea's entire exports. So one walkout in that plant doesn't dent a single company's quarter. It stalls the AI buildout for the whole planet. Their profit had jumped seven hundred and fifty-five percent in a year. So the workers asked for a cut. And they got it. Ten and a half percent of the division's profit. Every year. For ten years." },
  { "slide": 4, "text": "And this is the part that shows up in every other story like it. The chip workers had two things. A union. And a product nobody could buy anywhere else. Put those together, and they could shut the whole line down. So when they asked for a cut, the answer had to be yes. That's what this comes down to. The power to say no, and make it stick. The bonus is just the receipt. So hold onto the question. Who gets to say no? Because the rest of this boom is full of people who can't." },
  { "slide": 5, "text": "Now follow the electricity instead of the chips. It leads straight to the second bottleneck. Every data center needs a giant transformer before it can switch on. That's the equipment that moves power across the grid. The wait for a big one has stretched to four years. And it gets stranger. The special steel inside that transformer's core comes from exactly one factory in the entire United States. One mill, in Butler, Pennsylvania. The CEO of that company says it plainly. No AI without electricity. And no electricity without transformers. The grid is a chokepoint, exactly like the memory plant. With one difference." },
  { "slide": 6, "text": "The difference is that nobody here has a hand on the valve. The grid operator for thirteen eastern states ran its auctions for future power. The math came back ugly. Data-center demand added almost fourteen billion dollars to customer bills. Wholesale power, up more than seventy-five percent in a single year. That lands on families in Ohio and Virginia. They never voted on the data centers driving the number. They just pay more for the same electricity. The chip workers had a union. The person opening that power bill has a billing address." },
  { "slide": 7, "text": "Here's where the easy version of this story falls apart. You'd think the chip workers' bonus just gets passed down to you. Higher chip prices, higher everything, your bill goes up. Clean and simple. It doesn't work that way. The bonus is a slice of profit. It comes out of what's left after the chips sell, not out of the price stamped on each one. So his raise did not pay for your bill. And your bill did not fund his raise. They come out of the same boom. They are not the same money." },
  { "slide": 8, "text": "And this is already spreading. Within days of the Samsung vote, TSMC, the one other chipmaker with the same kind of pull, told its own staff their profit-sharing would jump more than thirty percent. In the US, two of the biggest unions are studying exactly what Samsung's workers just pulled off. There's talk of an AI dividend showing up at company shareholder meetings next year. So the same split travels with it. Where workers can organize, they write themselves a claim on the boom. Where they can't, the bill just shows up in the mailbox." },
  { "slide": 9, "text": "The four hundred thousand dollar bonus is the headline. The thing I actually feel is a line on my own power bill. And I don't live anywhere near a data center. You don't have to live near one for the boom to reach the bill. I'm not the four hundred thousand dollar worker here. Odds are you aren't either. So picture those two workers walking out of the plant again. Even the four thousand dollar guy had a union and a vote. He was still inside the deal. The person opening that power bill was never inside it. The chip workers had a hand on the valve. And they turned it. The rest of us are still standing somewhere with no valve to grab." },
  { "slide": 10, "text": "I kept the biggest pieces for the article. A one-paragraph deal from nineteen fifty-one that this contract quietly rhymes with. Korea's plan to mail every citizen a check funded by AI tax money. The fracture inside Samsung, where the phone and TV workers backed this at twenty-one percent. The shareholders now suing to tear the whole deal up. And the question I can't close. Does Samsung make the cloud giants pay for it? It's all in the piece." },
  { "slide": 11, "text": "The full piece is on Substack. The two workers, the power bill, and the one question that decides who wins this boom. The Civic Node. Subscribe free at drinkyouroj.substack.com. Weekly. No hype." }
]
```

## Output requirements

- Single bundled HTML file named `dispatch-006-16x9.html`.
- All external resources loaded relatively (`../colors_and_type.css`,
  `../slides.css`, `../deck-stage.js`, `../assets/mark.svg`, etc.) so the
  file drops into `slides/` alongside the existing `deck.html`. No
  character / Justoon images are referenced.
- Speaker notes embedded as JSON per the section above — **11 entries
  (one per scene), not 109.**
- **Build-on-reveal:** each scene reveals one element per advance step
  (109 beat-steps total). Manual advance is primary; emit approximate
  `data-advance-at` timestamps as the auto-play fallback. One advance =
  one beat = one new element. Never extend `deck-stage.js`; use its
  existing step/advance mechanism.
- Self-contained: opens in any browser, plays via `deck-stage.js`.
- No external CDN calls. No remote fonts. No analytics.
- Slide IDs: `slide-01` through `slide-11`. Each scene is a top-level
  `<section class="slide slide-[zone]" id="slide-NN">` matching
  `slides/deck.html`'s structure. Face slides add `has-face-left`
  (Slides 03, 05, 06, 08) or `has-face-right` (Slide 07).
- **Designed for 16:9 (1920×1080) only.** Build content to fill that frame
  (full-bleed beats use the whole frame; data slides use the right ~64%
  content column with the rail empty). Do NOT add 9:16 / 1:1 handling — the
  square-safe `youtube-slideshow.md` sibling owns those cuts.
- Every scene passes the thumbnail test at its resting beat: scale the
  window to 240px wide and confirm the named anchor element is legible.
- Every resting beat passes the visible-text budget (≤25 visible words OR
  one hero number + ≤15 supporting words). The reserved rail and speaker
  notes are excluded.
- The reserved rail (left 30% on Slides 03/05/06/08; right 32% on Slide 07)
  renders empty — no text, no decoration — for the post-production face
  composite. Full-bleed slides (01, 02, 04, 09, 10) use the whole frame.

## Pacing holds (from the narration's Script Notes)

- Scene 01 / B5: hold `$400,000` a beat longer than B7's `$4,000` — the
  asymmetry should be felt in screen-time, not just size.
- Scene 01 / B10, 02 / B9, 04 / B11: let the refrain / `100:1` hang ~1–1.5s.
- Scene 06 / B9–B10: `A UNION` and `A BILLING ADDRESS` land as a matched
  pair, equal weight, short gap.
- Scene 07 / B11: the deck's longest hold (~1.5s) — `NOT THE SAME MONEY`
  is the funnel's payoff.
- Scene 09 / B10: hold the valve bookend `NO VALVE TO GRAB` ~2s — the emotional
  payoff before the TEASE turn.
- Scene 10 / B1: `WHAT'S NOT IN THIS VIDEO` is the funnel header; the cut bullets
  (B2–B6) land quick after it.
