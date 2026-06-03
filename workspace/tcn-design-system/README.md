# The Civic Node — Design System

> Dispatches from inside the machine.

A weekly systems-analysis newsletter covering the collision between centralized institutions and the technologies competing with them — written for readers fluent in at least two of monetary policy, decentralized infrastructure, and political-systems analysis.

**Editorial standard:** if you could have gotten this from a Twitter thread, it should not have been published here.

---

## 1 — Brand fundamentals

| | |
|---|---|
| **Name** | The Civic Node |
| **Publisher URL** | drinkyouroj.substack.com |
| **Established** | 2025 |
| **Tagline** | Dispatches from inside the machine. |
| **Core promise** | Composure through frameworks. |
| **Audience** | Systems analysts, 30–45, who read both Lyn Alden and Matt Taibbi. |
| **Logo philosophy** | "Terminal Authority" — typewriter-monospace, no decoration, slate-on-black. |

### Permanent anti-patterns

> Never. Not for any reason. These compromise the brand directly.

- Partisan drift
- Sponsored content
- Community-before-trust
- Contrarianism for its own sake
- Doomerism

### Standard disclosure (verbatim, append to any analysis piece)

> No token positions, advisory roles, allocation letters, or sponsored content. If I have an operational relationship with a project or infrastructure mentioned in this piece, it is disclosed in the body before the relevant analysis. If I'm wrong, the primary sources are linked — you can check.

---

## 2 — Source materials

This system is built from materials the user supplied:

- **Figma file** — `The Civic Node — Logo System.fig`, mounted as a virtual filesystem.
  Focus pages: `/Thicker/*` (Cover, Mark Dark/Light, Lockups, Color Palette, Wordmark, Substack logo, Bluesky/Facebook covers).
- **Reference image** — `uploads/Facebook Cover · 820×462.png` (also: `assets/facebook-cover-reference.png`).

The Figma file declares 1 font (Courier Prime), 7 brand colors and a single logomark variant. There are no production codebases, no prior CSS, no component library — this design system is the **first** programmatic articulation of the brand.

---

## 3 — Content fundamentals

### Voice
**Dry, sardonic, deadpan, precise.** "Accessible smart." Never a jersey, never a cheerleader. The voice of someone who has read the primary source and is going to tell you what it actually says, in the order that matters, without flinching from the implication.

### Casing
- **Headlines:** sentence case (`The crowding-out paradox`), not Title Case.
- **Section labels / kickers / metadata:** ALL CAPS, mono, wide-tracked (`POLITICS · INFRASTRUCTURE · AI · POWER · NO HYPE`).
- **Body:** standard prose. No vibe-marketing capitalisation (`Why It Matters` → `why it matters`).

### Person
- Default to **first-person singular** when making a call (`I think this is wrong because…`). The publication is one person's analysis, not a faceless institution.
- Address the reader as **"you"** when handing over a framework or a question. Avoid "we" — "we" implies tribe.

### Punctuation
- **Em dashes** with spaces — like this — are heavily used as a beat / aside.
- **Middle dot** `·` is the brand's preferred series separator (`POLITICS · INFRASTRUCTURE · AI`). Never `|`, never `/`.
- **No exclamation marks.** None. Strip them.
- **No emoji.** None. Not in headlines, not in social, not in dispatch numbering. Use mono-tagged labels (`[01]`, `EST. 2025`) instead.
- **Smart quotes** in body. Straight quotes inside `code` blocks.

### What we say (examples)
- ✅ `The crowding-out paradox: when sovereign debt absorbs the productivity premium.`
- ✅ `If I'm wrong, the primary sources are linked — you can check.`
- ✅ `This is the third time the Treasury has signalled it. Worth taking seriously.`
- ✅ `Three frames for thinking about it. The third is the one most people miss.`

### What we don't say
- ❌ `🔥 Hot take: the Fed is COOKED.`
- ❌ `Why this matters for YOU` (capitalised vibe-marketing)
- ❌ `As we've covered extensively…` (we / community drift)
- ❌ `The system is rigged!!!` (doomerism + exclaim)
- ❌ `Smart money is doing X` (jersey)

### Standing furniture (always present)
- Issue number in mono: `Dispatch №042`
- Reading time and word count: `12 min · 2,840 words`
- Disclosure block at the foot of any analysis piece (verbatim, see §1).

---

## 4 — Visual foundations

### The "Terminal Authority" thesis
Everything looks like it was set on a typewriter, then transmitted through a **single uplink node** at 4am. One typeface. One mark. Two flavours of slate. A lot of black.

### Color
- **Slate 400** `#557FA3` — the brand colour on dark surfaces. Headlines, marks, links.
- **Slate 600** `#3A6A8F` — the brand colour on light surfaces. Same role, different chassis.
- **Twilight** `#485070` — meta / metadata text on dark.
- **Black** `#0D0D0F` — the canvas. Not pure black; warmer, denser.
- **Gray 900** `#1A1A24` — raised surfaces.
- **Gray 50** `#F6F6F8` — light canvas.
- **Gray 200** `#E4E4EA` — light borders.

Tints `rgba(85,127,163,0.14)` and `rgba(58,106,143,0.10)` are used as **radial glows** behind the mark on social covers — never as flat fills.

There is **no green, no red, no orange, no purple**. There is no "success/danger/warning" semantic palette. If something is wrong, the words say so.

### Type
- **Single typeface:** **Courier Prime** (Regular and Bold, plus italics).
- Display sizes (54 / 90 / 166 px) are tracked **tight** at `-0.025em`. Fixing the gappiness of monospace at large sizes is the whole reason the wordmark works.
- Meta labels (11 / 13 px) are tracked **wide** at `0.10em–0.27em`, all caps. They read as terminal output, not as ad copy.
- Body is set at **16 px / 1.55**. We do not use a serif body face; the entire publication holds the line on mono.

### Backgrounds
- **Default canvas: black** (`#0D0D0F`). Not a true `#000` — it's slightly warm/dense.
- **Hairline rules** are linear gradients that fade in and out at the edges (15%/85% opacity stops). Never a hard solid line.
- **Radial glows** of slate (≤14% alpha) sit behind the mark on banners. They imply "transmission", not gloss.
- **No imagery.** No stock photos. No generative-AI textures. No grain unless explicitly added at very low opacity. The brand's restraint is the texture.

### Animation
- **Sparing.** Fades and 1-px hairline draws only.
- Easing: `cubic-bezier(0.2, 0, 0, 1)` — quick out, settle. No bounce. No spring.
- Durations: 120 / 200 / 360 ms.
- The cursor on a kicker label may **blink** (1Hz, square wave) — this is the one permitted "alive" cue. Use it once per page, never twice.

### Hover
- Links: **underline-thickens** from `1px transparent → 1px slate-400`.
- Buttons: outline brightens by ~10% lightness. **Never** a colour change to a different hue. **Never** a glow / shadow.

### Press
- Buttons: 1px **shadow inset** of the same slate at 30% — feels like the key bottoms out. No translate, no scale.

### Borders
- `1px` is the only stroke weight in UI chrome.
- The **mark** uses `3.5px` stroke at its 114-px reference width — i.e. the mark is heavier than UI by design.
- Rounded corners are used **only** on the node itself (a perfect circle) and on input fields (`r-1` = 2px). Cards do not round. Buttons do not round. The terminal does not round.

### Shadow
- **None on dark surfaces.** Black-on-black shadow is invisible and we don't fake depth.
- **One soft shadow** on light surfaces, used only on floating popovers / dropdowns:
  `0 2px 12px rgba(13,13,15,0.08)`.

### Layout
- Single-column reading width: **640 px** content, **720 px** with gutters.
- Terminal frames (cover, banner) use full bleed and centre the mark+wordmark with generous negative space.
- "Standing furniture" — issue number, reading time, disclosure — is **fixed** to the top-left and bottom-right corners of dispatch pages, set in 11px mono, 0.10em tracking.

### Transparency / blur
- Used **only** for the radial-glow tints behind the mark.
- No frosted-glass UI. No backdrop blur. The terminal is opaque.

### Imagery
- Not part of the system. If imagery is needed for a specific piece, treat it as a **specimen** in a black-bordered frame with a `FIG. 01 — caption.` mono label below. Convert all photographs to high-contrast monochrome before use.

### Cards
- **Black surface, slate hairline border, no shadow, no radius** on dark.
- On light: paper surface, paper-2 hairline, no radius, no shadow.
- A card has a `meta` kicker at the top (11px caps), a single h3, a body, and an optional `→` chevron at the bottom-right. Nothing else.

### Buttons
- Primary: solid **slate-400** background, **black** text on dark; on light it's slate-600 background, paper text.
- Secondary: **1px slate hairline border**, slate text, transparent background.
- Both: 12 px vertical / 20 px horizontal padding, 11 px mono caps text with 0.10em tracking.

### Iconography
See `ICONOGRAPHY` section below.

---

## 5 — Iconography

The brand has **one mark and one mark only**: the Civic Node — a vertical "antenna" with a horizontal cap, two diagonal "guy-wire" legs, and a circular **node** at the centre where they meet. It is the antenna of a single transmission station.

`assets/mark.svg` (SVG, single-colour `currentColor`, `3.5px` stroke).
`assets/mark-lines.svg` (high-fidelity export from Figma).
`assets/lockup-dark.svg` and `assets/lockup-light.svg` (mark + wordmark).

### General icon usage
- **Avoid icons.** Almost every place a designer would normally reach for an icon, this brand reaches for a **mono-tagged label** (`[01] CONTEXT`, `[02] FRAME`, `[03] CALL`). Words do the work icons usually do.
- When a navigational cue is genuinely required, use a **single ASCII glyph** in mono: `→`, `←`, `↗`, `·`, `—`, `[+]`, `[×]`. Never an SVG icon set.
- **No emoji.** Anywhere.
- **No icon font.** Lucide / Heroicons / FontAwesome are explicitly not part of this system.
- **No two-tone, no filled+outlined pairs.** There is no second style.

### Permitted exceptions
- **Substack's own icons** (heart / restack / share) when rendering inside a real Substack mock — those belong to the host platform, not us.
- **Social platform marks** (Bluesky butterfly, Substack `S`) when the mark is the link.

### Substitution flag
The `mark-lines.svg` and `mark-lines-fb.svg` files copied from the Figma binary are **path-accurate**; the simplified `mark.svg` is a clean line+stroke version that scales arbitrarily. Use the simplified one in HTML; reach for the binary export only when pixel-matching the Figma frames.

---

## 6 — Fonts

**Courier Prime** — Regular, Bold, Italic, Bold Italic.

> ⚠ **Substitution flag.** The user did not ship `.ttf` / `.woff2` files. We're loading Courier Prime via Google Fonts (`https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400;1,700`). If the brand needs offline / production-grade hosting, please drop the OFL-licensed font files into `fonts/` and the `@import` in `colors_and_type.css` will be removed in favour of `@font-face` declarations.

---

## 7 — Index

```
README.md                  ← you are here
SKILL.md                   ← Claude Code / Skill manifest
colors_and_type.css        ← all CSS vars (colors, type, spacing, motion)
fonts/                     ← (empty — see §6 substitution flag)
assets/                    ← logos, marks, lockups, social-cover references
preview/                   ← Design System tab cards (~16 cards)
ui_kits/
  newsletter/              ← Substack-style newsletter recreation
    README.md
    index.html             ← above-the-fold home (issue list + masthead)
    issue.html             ← reading view of a single dispatch
    cover.html             ← branded cover/social card
    components/*.jsx       ← Masthead, IssueCard, Disclosure, etc.
```

### Where to start
- **Designing a one-off mock?** → open `colors_and_type.css`, add `class="tcn"` to your root, build.
- **Mocking the newsletter?** → open `ui_kits/newsletter/index.html`.
- **Need the mark?** → `assets/mark.svg` (single-colour, currentColor).
- **Posting on social?** → `assets/lockup-dark.svg` + the cover-template HTML in `ui_kits/newsletter/cover.html`.

---

## 8 — Caveats & open questions

1. **Fonts.** Loaded from Google Fonts CDN; no offline fallback shipped. See §6.
2. **Imagery direction is undefined.** The Figma file contains zero images. We've codified the brand's "no-imagery" stance as restraint, but this should be confirmed when the editor wants to run a chart, photo, or screen-grab in a dispatch.
3. **The component library is small by design.** Newsletter, dispatch, social cover, masthead. The brand does not have an app, dashboard, settings panel, or marketing site — and we have not invented one.
