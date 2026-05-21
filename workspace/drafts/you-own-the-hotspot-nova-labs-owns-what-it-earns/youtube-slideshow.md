# Claude Design prompt — TCN Dispatch №004 slideshow

## Context

You are building an HTML slideshow for The Civic Node, Dispatch №004:
"You Own the Hotspot. Nova Labs Owns What It Earns." The slideshow is the
visual companion to a 5:11 YouTube narration video (trailer-format, 8
slides). Viewers will watch the slides while listening to the narration
as audio.

This is a trailer-format dispatch — short, dense, no live recap. The
narration runs at ~140 wpm with deliberate breath cues. The deck must
match that pace: dense enough to reward attention, restrained enough not
to compete with the audio.

## Inputs (attached / uploaded to this Claude Design project)

Upload the TCN design system bundle to this project before running this
prompt. Specifically:

- `colors_and_type.css` — the brand CSS variable system. Load at runtime.
- `slides.css` — slide-specific styles (sl-title, sl-section, sl-lead,
  sl-data, sl-frames, sl-compare, sl-quote, sl-end).
- `deck-stage.js` — kinetic engine. Load via `<script src="deck-stage.js">`.
- `assets/mark.svg`, `assets/lockup-dark.svg` — brand marks.
- `slides/deck.html` — reference template; mimic its slide structure.

If any of these are missing, halt and ask before generating the HTML.

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
- Zero-padded dispatch number (`№004`, not `№4`).

## Slide-by-slide specification

---

### Slide 1 — `sl-title`

**Kicker:** `DISPATCH №004 · HOOK`

**Headline:** You Own the Hotspot. Nova Labs Owns What It Earns.

**Tag (sub-line):** What McDonald's discloses that Helium didn't.

**Foot row:** `The Civic Node` · `2026·05·22 · 5 MIN`

**Animation:**
- `sl-mark-pulse` on the brand mark (44px, slate-400).
- `sl-glow` radial slate behind the mark.
- `sl-reveal` cascade 1 → 2 → 3 on headline → tag → foot row (200ms
  stagger, 360ms reveal each).
- Hold for ~2 seconds after the pulse settles before any transition cue.

---

### Slide 2 — `sl-lead`

**Kicker:** `DISPATCH №004 · THESIS`

**Heading (h3):** Helium operators bought a franchise. They were sold a business.

**Body:**

> The hardware they paid for is theirs. The pricing that determines what
> the hardware earns is set by Nova Labs.
>
> Nova Labs is the company that runs Helium Mobile and negotiates the
> carrier deals with T-Mobile and AT&T.
>
> That's the whole piece. The rest is verification.

**Animation:**
- `sl-hairline` draws left-to-right above the heading, 360ms on entry.
- `sl-reveal` cascade 1 → 2 on heading → body (200ms stagger).
- Heading kicker gets a single `sl-caret` blink (one of two carets in
  the deck — paired with the End slide).

---

### Slide 3 — `sl-data` with `ms-numgrid`

**Kicker:** `DISPATCH №004 · THE RECEIPT · UNIT ECONOMICS`

**Heading (h3):** The unit math, after the August 2025 halving.

**Number grid (3-column ms-numgrid, then a 2-column row beneath):**

Row 1 (3 columns):

| Numeral | Label |
|---|---|
| `$949` | Pro outdoor hotspot |
| `$4–8 / mo` | Well-placed urban earnings |
| `10–20 yrs` | Hardware payback period |

Row 2 (2 columns, beneath):

| Numeral | Label |
|---|---|
| `$125 / day` | IoT network revenue (all 385K hotspots) |
| `$56,000 / day` | Mobile-side carrier offload revenue |

**Closing line below the grid (slate-600, smaller):**

> The hotspot side is the hardware the project points at. The Mobile side
> is where the revenue actually lives.

**Animation:**
- `sl-chart-draw` triggers the numgrid reveal — numerals fade in at
  200ms each, left-to-right, top row first then bottom row.
- `sl-glow` radial slate behind the `$56,000 / day` cell (the
  dominant number that anchors the slide's argument).
- `sl-reveal` on the closing line, 360ms after the grid completes.

---

### Slide 4 — `sl-frames` (numbered escalation through time)

**Kicker:** `DISPATCH №004 · THE RECEIPT · HIP-143`

**Heading (h3):** A one-year sunset that extended itself.

**Three-frame grid `[01] / [02] / [03]`** (each frame's slate-400
sub-label is the date; prose beneath):

`[01] APR 2025`

> HIP-143 passes. Nova Labs gets authority to negotiate carrier pricing
> without routing each deal through governance. Sold as a one-year
> sunset.

`[02] APR 2026`

> Initial year ends. No overriding HIP passed. The sunset clause's fine
> print: the authority extends another year by default.

`[03] APR 2027`

> Where the authority now runs through.

**Punchline beneath the grid (single line, slate-400, slightly larger,
set off by a hairline above):**

> Nobody overrode it.

**Animation:**
- `sl-reveal` cascade 1 → 2 → 3 → 4 on heading → frame [01] → frame
  [02] → frame [03] (200ms stagger, 360ms reveal each).
- `sl-hairline` draws above the punchline, 360ms.
- Punchline line: hold a 1-second beat before it appears, then `sl-glow`
  radial slate underneath the words. Treat this as the slide's
  exhalation — let it sit.

---

### Slide 5 — `sl-frames` (numbered escalation)

**Kicker:** `DISPATCH №004 · THE TWIST · VOTE CONCENTRATION`

**Heading (h3):** Half the yes votes came from Nova Labs and a co-author.

**Three-frame grid `[01] / [02] / [03]`:**

`[01] HIP-143 — APR 2025`

> Passed at 90%. Nova Labs voted yes with 26% of the total. ferebee, one
> of the four co-authors, voted yes with another 24%. Together: half the
> yes votes authorizing Nova Labs's pricing authority came from Nova
> Labs and one of its co-authors.

`[02] HIP-148 — OCT 2025`

> Consolidated more rewards to Nova Labs. Subscribers who had been
> earning Helium tokens for sharing location data got gift cards
> instead. The vote passed at 97%. The top three voters controlled 62%
> of it.

`[03] BETWEEN THE TWO`

> ferebee's voting stake grew 55%. The rest of the network grew 18%.

**Closing line beneath the grid (slate-400, single line, set off by a
hairline above):**

> Every HIP starts from a more concentrated baseline than the last.

**Animation:**
- `sl-reveal` cascade 1 → 2 → 3 → 4 → 5 on the three frames + heading
  + closing line (sl-reveal-5 max, 200ms stagger).
- `sl-hairline` draws above the closing line, 360ms.
- `sl-mark-pulse` ambient on the brand mark (24px, slow — this is a
  Twist slide and earns the extra weight).

---

### Slide 6 — `sl-frames` (combined-type: FRAME + STAKES — fewer columns, more prose)

**Kicker:** `DISPATCH №004 · THE FRAME + STAKES · AUTHOR'S DEBUG`

**Heading (h3):** The audit is the floor. It doesn't catch fraud.

**Two-frame layout** (replacing the standard 3-column, since this is
reflective prose, not numbered escalation):

`[01] WHAT I WAS WRONG ABOUT`

> I ran twelve Datagram nodes. I moderated their community for seven
> months. Without pay. The project collapsed.
>
> Earlier pieces I published called Datagram the legitimate
> counter-example. The decentralized-infrastructure project doing it
> right. That framing was wrong.

`[02] WHAT THE STANDARD CATCHES — AND WHAT IT DOESN'T`

> The four-disclosure standard this piece argues for would have caught
> Helium in 2021. Before any hotspot shipped. It would have flagged
> that pricing authority sat outside the operator class.
>
> The same standard would not have caught Datagram. The documents
> passed. The software wasn't running what they described.

**Animation:**
- `sl-reveal` cascade on heading → frame [01] → frame [02] (200ms
  stagger, 360ms reveal each).
- No chart-draw. No glow. This slide is the deck's quiet moment —
  intensification stays restrained here.

---

### Slide 7 — `sl-lead` (bullet-style listing)

**Kicker:** `DISPATCH №004 · TEASE`

**Heading (h3):** What the piece on Substack covers.

**Body (bulleted, slate-400 numerals as bullet markers `[01]` / `[02]` etc.):**

`[01]` The four disclosures Helium operators never received, written
out in plain language. A hardware buyback floor. An exit provision when
the reward structure changes underneath you. Revenue disclosure even
when individual carrier rates stay confidential. A sunset clause that
requires an active re-vote instead of extending by default.

`[02]` The full HIP-148 vote. The Mobile Mapping rewards subscribers
earned by sharing location data, traded for redeemable gift cards.

`[03]` The Helium Foundation's own guidance pointing operators toward
the same two proxies that were accumulating the most voting power.

`[04]` The rationalization that made me run twelve Datagram nodes
without pay for a project that had no business underneath it.

**Closing line (slate-400, larger, set off by hairline above):**

> drinkyouroj.substack.com

**Animation:**
- `sl-reveal` cascade 1 → 2 → 3 → 4 on the four bullets (120ms
  stagger — pick up the pace here, per the narration's pacing cue).
- `sl-hairline` draws above the URL, 360ms.
- `sl-reveal` on the URL, 200ms after the hairline lands.
- URL gets a faint `sl-glow` radial slate behind it (subtle — this is
  the CTA, not the dominant number).

---

### Slide 8 — `sl-end`

**Kicker:** `DISPATCH №004 · END`

**Heading (h2):** The Civic Node

**Body (disclosure block):**

> Subscribe free at drinkyouroj.substack.com.
>
> Weekly. No hype.

**Foot row:** `The Civic Node` · `2026·05·22`

**Animation:**
- `sl-mark-pulse` on the brand mark at 44px (slate-400).
- `sl-glow` radial slate behind the mark.
- `sl-reveal` cascade 1 → 2 → 3 on heading → URL line → "Weekly. No
  hype." (200ms stagger).
- Heading kicker gets the deck's second `sl-caret` blink (paired with
  the Thesis kicker on Slide 2 — two carets total in the deck).
- Hold the end state — no transition out. Last slide.

---

## Speaker notes (embed as JSON at end of HTML)

Embed as a `<script type="application/json" id="speaker-notes">` block
at the end of the `<body>`. One entry per slide. Each entry is the
narration text verbatim from `youtube-narration.md` — no paraphrasing,
no compression, no register adjustment.

```json
[
  {
    "slide": 1,
    "text": "Buy a McDonald's franchise and you get a two-hundred-page disclosure document. Federal law requires it. The pricing. The exit terms. What happens if McDonald's changes the menu and your numbers stop working.\n\nThree hundred eighty-five thousand people bought a Helium hotspot.\n\nThe franchise disclosure equivalent?\n\nThey didn't get one.\n\nVibes."
  },
  {
    "slide": 2,
    "text": "Helium operators bought a franchise. They were sold a business.\n\nThe hardware they paid for is theirs. The pricing that determines what the hardware earns is set by Nova Labs.\n\nNova Labs is the company that runs Helium Mobile and negotiates the carrier deals with T-Mobile and AT&T.\n\nThat's the whole piece. The rest is verification."
  },
  {
    "slide": 3,
    "text": "A pro outdoor Helium hotspot is nine hundred forty-nine dollars.\n\nAfter the August 2025 halving, a well-placed urban unit earns four to eight dollars a month.\n\nAt eight dollars, the hardware pays itself off in ten years. At four, twenty.\n\nTen years is what asphalt shingles take to wear out. Twenty is most of a mortgage.\n\nThe whole IoT side of the network, all three hundred eighty-five thousand hotspots, generates a hundred twenty-five dollars a day in data transfer revenue.\n\nThe Mobile side, which is the carrier offload for T-Mobile and AT&T, generates fifty-six thousand a day.\n\nThe hotspot side is the hardware the project points at. The Mobile side is where the revenue actually lives."
  },
  {
    "slide": 4,
    "text": "In April 2025, a governance vote called HIP-143 gave Nova Labs the authority to negotiate carrier pricing without routing each deal through governance.\n\nCarrier deals are confidential. Governance is slow. The commercial case is real.\n\nThe proposal was sold as a one-year sunset.\n\nRead the text closer. It extends for another year if no overriding HIP passes.\n\nApril 2026. The initial year ended. No overriding HIP passed.\n\nThe authority extended itself. It now runs through April 2027.\n\nNobody overrode it."
  },
  {
    "slide": 5,
    "text": "HIP-143 passed at ninety percent.\n\nNova Labs voted yes with twenty-six percent of the total vote. A proxy named ferebee, one of the four co-authors who wrote the proposal, voted yes with another twenty-four percent.\n\nTogether: half the yes votes authorizing Nova Labs's pricing authority came from Nova Labs and one of its co-authors.\n\nSix months later, a vote called HIP-148 consolidated more rewards to Nova Labs. Subscribers who had been earning Helium tokens for sharing location data from their phones got gift cards instead.\n\nThat vote passed at ninety-seven percent. The top three voters controlled sixty-two percent of it.\n\nIn those six months, ferebee's voting stake grew fifty-five percent. The rest of the network grew eighteen.\n\nEvery HIP starts from a more concentrated baseline than the last."
  },
  {
    "slide": 6,
    "text": "I ran twelve Datagram nodes. I moderated their community for seven months. Without pay. The project collapsed.\n\nEarlier pieces I published called Datagram the legitimate counter-example. The decentralized-infrastructure project doing it right.\n\nThat framing was wrong.\n\nThe four-disclosure standard this piece argues for would have caught Helium in 2021. Before any hotspot shipped. It would have flagged that pricing authority sat outside the operator class.\n\nThe same standard would not have caught Datagram. The documents passed. The software wasn't running what they described.\n\nThe audit is the floor. It doesn't catch fraud."
  },
  {
    "slide": 7,
    "text": "The piece on Substack covers what this video skipped.\n\nThe four disclosures Helium operators never received, written out in plain language. A hardware buyback floor. An exit provision when the reward structure changes underneath you. Revenue disclosure even when individual carrier rates stay confidential. A sunset clause that requires an active re-vote instead of extending by default.\n\nThe full HIP-148 vote. The Mobile Mapping rewards that subscribers earned by sharing location data, traded for redeemable gift cards.\n\nThe Helium Foundation's own guidance pointing operators toward the same two proxies that were accumulating the most voting power.\n\nAnd the rationalization that made me run twelve Datagram nodes without pay for a project that had no business underneath it.\n\nIt's at drinkyouroj.substack.com."
  },
  {
    "slide": 8,
    "text": "The Civic Node. Subscribe free at drinkyouroj.substack.com.\n\nWeekly. No hype."
  }
]
```

## Output requirements

- Single bundled HTML file named `dispatch-004.html`.
- All external resources loaded relatively (`../colors_and_type.css`,
  `../slides.css`, `../deck-stage.js`, `../assets/mark.svg`, etc.) so the
  file can drop into `slides/` alongside the existing `deck.html`.
- Speaker notes embedded as JSON in the document per the §Speaker Notes
  section above.
- Self-contained: opens in any browser, plays the full deck via
  `deck-stage.js`.
- No external CDN calls. No remote fonts. No analytics.
- Slide IDs: `slide-01` through `slide-08`. Each slide is a top-level
  `<section class="sl-[type]" id="slide-NN">` element matching
  `slides/deck.html`'s structure.

## Pacing cues (from the narration's Script Notes — apply if the deck
auto-advances; otherwise treat as guidance for the speaker-notes
consumer)

- Slide 01: hold ~1 second of silence after "Vibes." before transitioning.
- Slide 02: slight pause between "bought a franchise" and "They were
  sold a business" — let the contrast set.
- Slide 04: hard pause before "Nobody overrode it." Two beats of silence
  after.
- Slide 05: slow the closing line — "Every HIP starts from a more
  concentrated baseline than the last." Each clause delivered as its
  own beat.
- Slide 06: slow the close — "The audit is the floor. It doesn't catch
  fraud." Two beats between the sentences.
- Slide 07: pick up the pace through the cuts list. Slow on the personal
  closer ("twelve Datagram nodes without pay").

These cues inform animation hold durations on the affected slides.
