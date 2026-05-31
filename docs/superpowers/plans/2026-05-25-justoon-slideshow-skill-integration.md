# Justoon Slideshow Skill Integration — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the `tcn-youtube-slideshow` skill so it consumes the populated Justoon library at `~/Pictures/tcn-justin-slideshow/` and emits a Claude Design prompt that includes per-slide Justoon directives plus the 1:1-primary layout primitives proven in the 2026-05-25 hand-test.

**Architecture:** Surgical edits to `~/.claude/skills/tcn-youtube-slideshow/SKILL.md` (~460 lines, 7 sections touched) and `~/.claude/skills/tcn-youtube-slideshow/references/template-mapping.md` (~150 lines, 1 new section added). No new files. No code, just docs/markdown edits to skill instructions. The skill's output prompt format is what changes; the skill's process is what learns how to pick Justoon variants.

**Tech Stack:** Filesystem only (`Read`, `Edit`, `Bash` for grep verifications). The skill files live in `~/.claude/skills/` which is NOT a git repo, so skill edits do not commit anywhere. Only this plan file commits to the project repo.

**Scope boundary:** This plan modifies the skill's prompt template + picker logic. It does NOT run the prompt through Claude Design (that's Justin's manual step after the plan executes). It does NOT add role B (corner companion — still deferred per the spec). It does NOT modify `tcn-youtube-thumbnail` or any other sibling skill.

**Reference docs:**
- Spec: [`docs/superpowers/specs/2026-05-25-justoon-slideshow-library-design.md`](../specs/2026-05-25-justoon-slideshow-library-design.md) (commits `77675df` + `a0c4a07` beard fix)
- Layout reference (proven CSS): [`docs/superpowers/reference-renders/2026-05-25-justoon-slideshow-layout.html`](../reference-renders/2026-05-25-justoon-slideshow-layout.html) (commit `237bc28`)
- Library being consumed: `~/Pictures/tcn-justin-slideshow/` (CLAUDE.md inventory + 10 PNGs already exist as of this plan)

**The three architectural deltas this plan applies to the spec:**

1. **1:1 is the primary recording canvas, not 16:9.** The original spec implied 16:9 was the design target with 9:16/1:1 as derivatives. Hand-test reversed this — the safe-zone is always a square (`min(85cqw, 85cqh)`), so designing for 1:1 means the other aspects work as margin around the square.
2. **Absolute positioning + `cqh` max-heights for `.justoon`, not grid.** Grid's row auto-sizing made `height: 100%` resolve to the image's natural 2048px. Proven pattern: `position: absolute` with `height: 75cqh` (role C bust, max-width 55%) or `height: 88cqh` (role A full-body, max-width 32%).
3. **Token clamps tuned for 1:1 primary** + `text-wrap: balance` on headlines/captions: hero `clamp(80px, 24cqmin, 360px)`, h1 `clamp(28px, 9cqmin, 144px)`, h2-mid `clamp(22px, 6.5cqmin, 96px)`, body `clamp(14px, 5cqmin, 72px)`, kicker `clamp(10px, 2.5cqmin, 36px)`. Note the unit change `vmin → cqmin` so type scales relative to the slide container, not the viewport.

---

## Task 1: Re-read both files to confirm current state

**Files:**
- Read: `/Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md` (~460 lines)
- Read: `/Users/justin/.claude/skills/tcn-youtube-slideshow/references/template-mapping.md` (~150 lines)

The plan was written against a specific snapshot of these files. If they've been edited since, the `old_string` values in subsequent Edit steps will fail. This task verifies the snapshot is still current and surfaces drift before damage.

- [ ] **Step 1: Read SKILL.md in full**

Run:
```
Read tool: /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Verify:
- Line count is approximately 461 (`wc -l` will confirm)
- Section headers match: What This Skill Does, Why a Prompt-Builder, Position in the YouTube Workflow, Inputs and Outputs, Slide-Type Mapping, Kicker Convention, Animation Intensification, Small-Screen Readability and Multi-Aspect Layout, Output Format, The Process, Failure Modes, What This Skill Is NOT, Companion Skills, Reference Files

If the structure has drifted, halt and surface to the user; the subsequent Edit steps assume the snapshot.

- [ ] **Step 2: Read template-mapping.md in full**

Run:
```
Read tool: /Users/justin/.claude/skills/tcn-youtube-slideshow/references/template-mapping.md
```

Verify:
- Line count is approximately 153 (`wc -l`)
- Has 6 numbered sections: Slide-type mapping, Kicker convention, Animation intensification, Visible-text budgets, Slide-splitting rules, Future-option seam

- [ ] **Step 3: Verify the Justoon library exists at the expected path**

Run:
```bash
ls ~/Pictures/tcn-justin-slideshow/*.png | wc -l
test -f ~/Pictures/tcn-justin-slideshow/CLAUDE.md && echo "CLAUDE.md present"
test -f ~/Pictures/tcn-justin-slideshow/justoon-neutral.png && echo "anchor present"
```

Expected: `10` PNGs, both files present. The skill's new `--justoon-refs` default points here; if the library moved, the default needs updating.

- [ ] **Step 4: No commit** — discovery only.

---

## Task 2: SKILL.md §"Inputs and Outputs" — add `--justoon-refs` optional input

**Files:**
- Modify: `/Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md` (Optional inputs subsection, around lines 51-55)

- [ ] **Step 1: Edit — insert `--justoon-refs` option into the Optional inputs list**

Use the Edit tool with:

**old_string:**
```
### Optional inputs

- **Path to the TCN design system bundle.** Defaults to the user's maintained path (Justin's current path: `~/Documents/The Civic Node — Design System.zip`). If not provided, the skill leaves a placeholder in the prompt with an instruction to upload before pasting.
- **Steering** — free-text guidance like "use sl-compare instead of sl-frames on Slide 4", "make Slide 3's chart larger", or "skip animation intensification on the Tease slide".
- **Override slide type** — for any individual slide, the user can force a specific template (e.g., "Slide 3 must be sl-data with the SVG chart variant").
```

**new_string:**
```
### Optional inputs

- **Path to the TCN design system bundle.** Defaults to the user's maintained path (Justin's current path: `~/Documents/The Civic Node — Design System.zip`). If not provided, the skill leaves a placeholder in the prompt with an instruction to upload before pasting.
- **`--justoon-refs <path>`** — path to the Justoon slideshow library. Defaults to `~/Pictures/tcn-justin-slideshow/`. Absence triggers "no Justoon" mode: the skill produces typography-only slides exactly as today. Presence triggers per-slide Justoon auto-picks per the slide-type table (Receipt/Stakes → role A pointing pose; Twist → role C reaction). The library's `justoon-neutral.png` is the required anchor / fallback if a mapped variant is missing. Library convention: `~/Pictures/tcn-justin-slideshow/CLAUDE.md`.
- **Steering** — free-text guidance like "use sl-compare instead of sl-frames on Slide 4", "make Slide 3's chart larger", "skip animation intensification on the Tease slide", or "no Justoon on this dispatch" (forces no-Justoon mode even when `--justoon-refs` resolves).
- **Override slide type** — for any individual slide, the user can force a specific template (e.g., "Slide 3 must be sl-data with the SVG chart variant").
- **Override Justoon variant** — for any individual slide, the user can force a specific variant or none (e.g., "Slide 8: use justoon-react-raised-eyebrow instead of deadpan", or "Slide 4: no Justoon").
```

- [ ] **Step 2: Verify the edit landed**

Run:
```bash
grep -c "justoon-refs" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Expected: at least `2` (one for the input definition, one for the no-Justoon-mode parenthetical).

- [ ] **Step 3: No commit** — skill not in a git repo.

---

## Task 3: SKILL.md §"Slide-Type Mapping" — add Justoon role column

**Files:**
- Modify: `/Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md` (Slide-Type Mapping table, around lines 75-86)

- [ ] **Step 1: Edit — extend the mapping table with a Justoon role column**

Use the Edit tool with:

**old_string:**
```
Each narration slide maps deterministically to a slide template type from `slides/deck.html`. The mapping is driven by the narration's zone (Cold Open / Body / Outro) and slide sub-label.

| Narration slide | Default template | Fallback / variant |
|---|---|---|
| Cold Open / Hook (Slide 1) | `sl-title` | — |
| Cold Open / Thesis (Slide 2) | `sl-lead` | `sl-section` if thesis is one declarative phrase |
| Body / Receipt (data-heavy) | `sl-data` with `ms-numgrid` | `sl-data` with `sl-chart` SVG if the article has a chart |
| Body / Frame | `sl-frames` | `sl-compare` for two-way comparison |
| Body / Stakes | `sl-lead` | — |
| Body / Twist | `sl-frames` (numbered escalation) | `sl-compare` (before/after) |
| Body / Historical Echo | `sl-compare` (then/now) | `sl-lead` |
| Body / Verbatim | `sl-quote` | — |
| Outro / Tease (Slide N-1) | `sl-lead` with bullet listing | `sl-section` with `[TEASE]` kicker if shorter |
| Outro / End (Slide N) | `sl-end` | — |

**Combined slide types** (e.g., `THE FRAME + STAKES, Author's Debug` from dispatch-004): pick the first sub-label's template type, adjust the layout (fewer numbered columns, more prose), and note the combination in the prompt. Do not invent new template types.

The full mapping table with fallback rules, combined-type handling, and worked examples lives in `references/template-mapping.md`.
```

**new_string:**
```
Each narration slide maps deterministically to a slide template type from `slides/deck.html`. The mapping is driven by the narration's zone (Cold Open / Body / Outro) and slide sub-label.

| Narration slide | Default template | Fallback / variant | Justoon role |
|---|---|---|---|
| Cold Open / Hook (Slide 1) | `sl-title` | — | none |
| Cold Open / Thesis (Slide 2) | `sl-lead` | `sl-section` if thesis is one declarative phrase | none |
| Body / Receipt (data-heavy) | `sl-data` with `ms-numgrid` | `sl-data` with `sl-chart` SVG if the article has a chart | **A** (pointing teacher) |
| Body / Frame | `sl-frames` | `sl-compare` for two-way comparison | none |
| Body / Stakes | `sl-lead` | — | **A** (pointing teacher) |
| Body / Twist | `sl-frames` (numbered escalation) | `sl-compare` (before/after) | **C** (reaction-as-anchor) |
| Body / Historical Echo | `sl-compare` (then/now) | `sl-lead` | none |
| Body / Verbatim | `sl-quote` | — | none |
| Outro / Tease (Slide N-1) | `sl-lead` with bullet listing | `sl-section` with `[TEASE]` kicker if shorter | none |
| Outro / End (Slide N) | `sl-end` | — | none |

**Justoon role column:** activates only when `--justoon-refs` is provided. Role A = full-body pointing teacher, picked from `justoon-point-{right,up,down,open-palm}.png`. Role C = bust reaction-as-anchor, picked from `justoon-react-{deadpan,raised-eyebrow,concerned,smirk,shocked}.png`. Variant selection within a role is interpretive per the slide's specific content — full picker logic lives in `references/template-mapping.md` §7. Slides marked `none` stay typography-only even with `--justoon-refs` active. Anchor / fallback for any missing variant: `justoon-neutral.png`.

**Combined slide types** (e.g., `THE FRAME + STAKES, Author's Debug` from dispatch-004): pick the first sub-label's template type, adjust the layout (fewer numbered columns, more prose), and note the combination in the prompt. Do not invent new template types. For Justoon role, also use the first sub-label's role.

The full mapping table with fallback rules, combined-type handling, and worked examples lives in `references/template-mapping.md`.
```

- [ ] **Step 2: Verify the edit landed**

Run:
```bash
grep -c "Justoon role" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Expected: at least `2` (column header + explanatory paragraph).

Also verify:
```bash
grep -E "Body / Receipt.*pointing teacher" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -E "Body / Twist.*reaction-as-anchor" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Expected: both grep lines match.

- [ ] **Step 3: No commit** — skill not in a git repo.

---

## Task 4: SKILL.md §"Small-Screen Readability and Multi-Aspect Layout" — reframe 1:1-primary + update type-scale clamps

**Files:**
- Modify: `/Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md` (multi-aspect section, around lines 143-213)

This task does TWO edits in sequence: (1) reframe the section's framing language to 1:1-primary, (2) replace the type-scale table with the hand-test-proven clamp values. Both edits target the same section but are independent enough to apply separately.

- [ ] **Step 1: Edit — reframe the opening from "16:9 default" to "1:1 primary"**

Use the Edit tool with:

**old_string:**
```
The deck must be **readable at thumbnail size** (a phone watching a YouTube card, ~240px wide playback) and must play correctly at **16:9, 9:16, and 1:1 from a single HTML source**. This is non-negotiable. The prompt encodes the rules explicitly so Claude Design enforces them at render time.

### Single-source multi-aspect: letterbox into a safe zone

One HTML file. The same deck plays at any aspect ratio. The user resizes the recording window to the target aspect (1920×1080 for 16:9, 1080×1920 for 9:16, 1080×1080 for 1:1) and screen-captures.

- **Safe zone:** all critical content (kicker, headline, body, hero numbers, source attributions, CTA, disclosure) lives inside a centered square of `min(85vw, 85vh)`. This square is the *intersection* of all three target aspect ratios with a small margin.
- **Decorative extension:** the brand mark, `sl-hairline` rules, `sl-glow` radial, and slide background may extend to the full viewport. They make 16:9 not feel hollow and let 9:16 feel anchored.
- **No reflow per aspect.** No container queries, no `@media (aspect-ratio: ...)` rules. The layout is identical at every aspect — only the viewport's *empty margin* changes.
```

**new_string:**
```
The deck must be **readable at thumbnail size** (a phone watching a YouTube card, ~240px wide playback) and must play correctly at **16:9, 9:16, and 1:1 from a single HTML source**. This is non-negotiable. The prompt encodes the rules explicitly so Claude Design enforces them at render time.

### 1:1 is the primary canvas; other aspects are derivative

**Recording happens at 1:1 (1080×1080).** The 16:9 and 9:16 outputs are derived from the same HTML by changing the recording window's aspect — the slide content does not reflow. This was confirmed by the 2026-05-25 hand-test (see `docs/superpowers/reference-renders/2026-05-25-justoon-slideshow-layout.html` in the Substack Research project for the proven layout).

The mechanism that makes one HTML work at three aspects: the **safe zone is always a square** (`min(85cqw, 85cqh)`), so designing slide content inside the safe zone means it renders identically at any aspect — only the empty viewport margin differs. Critical insight: think of the slide-design problem as "what fits inside a square," not "what fits inside a 16:9 rectangle."

- **Safe zone:** all critical content (kicker, headline, body, hero numbers, source attributions, CTA, disclosure, any Justoon image) lives inside a centered square of `min(85cqw, 85cqh)`. (Note: `cqmin` / `cqw` / `cqh` are container-query units relative to the slide element, not viewport units. This decouples slide layout from page layout — necessary if multiple slides ever share a page.)
- **Decorative extension:** the brand mark, `sl-hairline` rules, `sl-glow` radial, and slide background may extend to the full slide bounds. They make 16:9 not feel hollow and let 9:16 feel anchored.
- **No reflow per aspect.** No container queries beyond the safe-zone definition. No `@media (aspect-ratio: ...)` rules. The layout is identical at every aspect — only the viewport's *empty margin* changes.
```

- [ ] **Step 2: Verify edit 1 landed**

Run:
```bash
grep -c "1:1 is the primary" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "min(85cqw, 85cqh)" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Expected: at least `1` each. The first proves the reframe header is present; the second proves the cqmin units replaced vmin.

- [ ] **Step 3: Edit — replace the type-scale table with the hand-test-proven clamps**

Use the Edit tool with:

**old_string:**
```
### Type scale (vmin-based; same physical size at any aspect)

Using `vmin` (1% of the smaller viewport dimension) means a 1080-tall viewport and a 1080-wide viewport produce identical type — exactly what multi-aspect requires.

| Role | Size | Why this floor |
|---|---|---|
| **Hero number / hero word** (the slide's thumbnail anchor) | `clamp(180px, 24vmin, 360px)` | Readable at 240px playback. Occupies ~25% of safe-zone height. |
| **Headline (h1/h2)** | `clamp(60px, 9vmin, 144px)` | Comfortably readable at 480px playback. |
| **Body / supporting text (h3, p, bullet)** | `clamp(30px, 5vmin, 72px)` | Above the thumbnail floor; readable at half-screen on mobile. |
| **Kicker, foot row, disclosure copy** | `clamp(18px, 2.5vmin, 36px)` | Decorative / contextual. Not load-bearing for thumbnail readability. |

No exceptions. No `font-size: 14px` anywhere in the deck.
```

**new_string:**
```
### Type scale (cqmin-based; tuned for 1:1 primary canvas)

Using `cqmin` (1% of the slide container's smaller dimension) means a 1080-tall slide and a 1080-wide slide produce identical type — exactly what multi-aspect requires. The clamps below are tuned for 1:1 as the primary recording aspect, with floors gentle enough that derivative aspects (16:9 / 9:16) stay legible without overweighting them.

| Role | Size | Why this floor |
|---|---|---|
| **Hero number / hero word** (the slide's thumbnail anchor) | `clamp(80px, 24cqmin, 360px)` | Readable at 240px playback. Occupies ~25% of safe-zone height. Floor lowered from 180px (vmin era) because cqmin scales per slide, not viewport. |
| **Headline (h1, used for primary heading slides)** | `clamp(28px, 9cqmin, 144px)` | Comfortably readable at full size; legible at thumbnail. |
| **Headline mid (h2-mid, used for body slides where the headline isn't the anchor)** | `clamp(22px, 6.5cqmin, 96px)` | New role added during the 2026-05-25 hand-test for slides where Justoon is the anchor and the headline is supporting (role C twist slides especially). |
| **Body / supporting text (h3, p, bullet)** | `clamp(14px, 5cqmin, 72px)` | Floor lowered from 30px (vmin era) so body text stays clean at thumbnail without forcing the headline floor up. |
| **Kicker, foot row, disclosure copy** | `clamp(10px, 2.5cqmin, 36px)` | Decorative / contextual. Floor lowered from 18px so thumbnail kicker reads as texture, not legible content. |

No exceptions. No `font-size: 14px` (or other ad-hoc values) anywhere in the deck.

**Text-wrap directive:** every headline and caption uses `text-wrap: balance` to distribute lines visually rather than greedy-fill ragged-right. This was added during the hand-test after the 9:16 portrait view produced 2-character-wide ragged lines without it.
```

- [ ] **Step 4: Verify edit 3 landed**

Run:
```bash
grep -c "cqmin-based" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "text-wrap: balance" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "clamp(80px, 24cqmin, 360px)" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "h2-mid" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Expected: `1` each for the header + text-wrap, `1` for the hero clamp, `1+` for h2-mid (new role).

- [ ] **Step 5: No commit** — skill not in a git repo.

---

## Task 5: SKILL.md §"Output Format" — extend the prompt template with safe-zone-as-square + Justoon directives + .justoon CSS + v5 reference

**Files:**
- Modify: `/Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md` (Output Format section, around lines 251-294)

This task updates the Claude Design prompt template the skill emits. Two edits: (1) replace the "Small-screen / multi-aspect requirements" block inside the prompt template to match the new 1:1-primary framing and add `.justoon` CSS rules; (2) add a new "Justoon directives" subsection to the slide-by-slide spec.

- [ ] **Step 1: Edit — replace the Small-screen/multi-aspect block inside the prompt template**

Use the Edit tool with:

**old_string:**
```
## Small-screen / multi-aspect requirements (non-negotiable)

This deck must render correctly at 16:9, 9:16, and 1:1 from this single
HTML file, and must be readable at thumbnail playback (~240px wide on a
phone). The author records by resizing the browser to the target aspect
and screen-capturing; the HTML does not branch per aspect.

- Define `--safe-zone: min(85vw, 85vh)` at `:root`. Every slide's
  critical-content container is exactly this size, centered.
- Critical content (kicker, headline, body, hero numbers, source
  attributions, CTA, disclosure) lives ONLY inside the safe zone.
- Decorative elements (brand mark, `sl-hairline` rules, `sl-glow`
  radial, slide background fill) may extend to viewport edges.
- No fixed-pixel widths on layout containers. No media queries based on
  aspect ratio. No container queries. Layout is identical at every
  aspect; only the empty viewport margin differs.

**Type scale (apply globally, not per slide):**

```css
:root {
  --type-hero:    clamp(180px, 24vmin, 360px);
  --type-h1:      clamp(60px,  9vmin,  144px);
  --type-h2:      clamp(60px,  9vmin,  144px);
  --type-body:    clamp(30px,  5vmin,  72px);
  --type-kicker:  clamp(18px,  2.5vmin, 36px);
  --safe-zone:    min(85vw, 85vh);
}
```

No element renders below `--type-kicker`. The hero/h1/h2/body/kicker
roles are the only sizes used on the deck.

**Thumbnail-anchor rule:** every slide has exactly one element at
`--type-hero` (or `--type-h1` for slides without a numeric anchor).
That element must occupy ≥20% of the safe-zone height.

**Visible-text budget:** ≤25 visible words per slide across all on-
screen elements, OR one hero number + ≤15 supporting words. Speaker
notes are not counted. Where a slide is marked as panel-a / panel-b
below, render both panels and use the `data-advance-at` attribute on
panel-a to auto-advance to panel-b at the specified mid-narration
timestamp.
```

**new_string:**
```
## Small-screen / multi-aspect requirements (non-negotiable)

This deck must render correctly at 16:9, 9:16, and 1:1 from this single
HTML file, and must be readable at thumbnail playback (~240px wide on a
phone). **The primary recording aspect is 1:1 (1080×1080).** The 16:9
and 9:16 outputs are derived from the same HTML by changing the
recording window's aspect — slide content does not reflow.

The mechanism: the safe zone is always a square (`min(85cqw, 85cqh)`).
Design slide content inside the safe zone and it renders identically at
any aspect — only the empty viewport margin differs.

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
- No fixed-pixel widths on layout containers. No media queries based on
  aspect ratio. Layout is identical at every aspect; only the empty
  margin differs.

**Type scale (apply per slide via container-query units):**

```css
.slide {
  container-type: size;
  --type-hero:    clamp(80px, 24cqmin, 360px);
  --type-h1:      clamp(28px,  9cqmin, 144px);
  --type-h2-mid:  clamp(22px,  6.5cqmin, 96px);
  --type-body:    clamp(14px,  5cqmin,  72px);
  --type-kicker:  clamp(10px,  2.5cqmin, 36px);
  --safe-zone:    min(85cqw, 85cqh);
}
```

No element renders below `--type-kicker`. The hero/h1/h2-mid/body/kicker
roles are the only sizes used on the deck. Use `--type-h2-mid` (not
`--type-h1`) on body slides where Justoon is the anchor and the headline
is supporting (role C twist slides specifically).

**Text-wrap directive:** every `.headline` and `.caption` element uses
`text-wrap: balance` to distribute lines visually.

**Slide zone modifier class.** Each `.slide` element gets a zone modifier class derived from the narration's zone label: `slide-hook`, `slide-thesis`, `slide-receipt`, `slide-frame`, `slide-stakes`, `slide-twist`, `slide-historical-echo`, `slide-verbatim`, `slide-tease`, `slide-end`. The class enables the Justoon CSS rules below and supports any future zone-specific styling without changing the markup pattern. Example: `<div class="slide slide-twist">…</div>`.

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
grid's row auto-sizing with image children makes `height: 100%` resolve
to the image's natural pixel height (a 2048×2048 PNG renders at 2048px,
breaking the layout). Always use absolute positioning with explicit
`cqh` max-heights. (See the reference layout at
`docs/superpowers/reference-renders/2026-05-25-justoon-slideshow-layout.html`
for the proven implementation.)

**Thumbnail-anchor rule:** every slide has exactly one element at
`--type-hero` (or `--type-h1` for slides without a numeric anchor; or
the Justoon image itself for role C reaction-as-anchor slides). That
element must occupy ≥20% of the safe-zone height.

**Visible-text budget:** ≤25 visible words per slide across all on-
screen elements, OR one hero number + ≤15 supporting words. Speaker
notes and Justoon images are not counted against this budget. Where a
slide is marked as panel-a / panel-b below, render both panels and use
the `data-advance-at` attribute on panel-a to auto-advance to panel-b
at the specified mid-narration timestamp.
```

- [ ] **Step 2: Verify edit 1 landed**

Run:
```bash
grep -c "primary recording aspect is 1:1" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "container-type: size" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "Slide zone modifier class" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "Justoon CSS rules" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "DO NOT use CSS grid" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Expected: `1` each. The fifth grep guards against the regression mode the hand-test surfaced (grid `align-items: center` + `height: 100%` on the .justoon img).

- [ ] **Step 3: Edit — add a Justoon directives subsection to the Slide-by-slide spec**

Use the Edit tool with:

**old_string:**
```
## Slide-by-slide specification

### Slide 1 — sl-title
Kicker: `DISPATCH №[NNN] · HOOK`
Headline (anchor, `--type-h1`): [from narration Slide 1]
Tag (sub-line, `--type-body`): [from narration cold-open candidate or steering]
Foot row (`--type-kicker`): `The Civic Node` / `[YYYY·MM·DD] · [N] MIN`
Visible-text budget: ~12 words. Headline ≤8 words.
Animation: sl-mark-pulse on the mark; sl-reveal cascade 1→2→3 on
  headline → tag → foot row. Hold for ~2s after the pulse settles.
```

**new_string:**
```
## Slide-by-slide specification

**Per-slide directive shape.** Each slide directive lists: kicker, anchor element, supporting content, visible-text budget, animation directive, AND — when Justoon is in play on this slide — a Justoon block of the form:

```
Justoon role: A | C
Justoon variant: <filename from ~/Pictures/tcn-justin-slideshow/>
Justoon placement: per the role's CSS rule (above)
```

Slides without Justoon omit the Justoon block entirely. When `--justoon-refs` is not provided, NO slide gets a Justoon block.

### Slide 1 — sl-title
Kicker: `DISPATCH №[NNN] · HOOK`
Headline (anchor, `--type-h1`): [from narration Slide 1]
Tag (sub-line, `--type-body`): [from narration cold-open candidate or steering]
Foot row (`--type-kicker`): `The Civic Node` / `[YYYY·MM·DD] · [N] MIN`
Visible-text budget: ~12 words. Headline ≤8 words.
Animation: sl-mark-pulse on the mark; sl-reveal cascade 1→2→3 on
  headline → tag → foot row. Hold for ~2s after the pulse settles.
Justoon: none.
```

- [ ] **Step 4: Verify edit 3 landed**

Run:
```bash
grep -c "Per-slide directive shape" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -E "^Justoon: none\." /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md | head -3
```

Expected: `1` for the header; the inline `Justoon: none.` appears on the Slide 1 example.

- [ ] **Step 5: No commit** — skill not in a git repo.

---

## Task 6: SKILL.md §"The Process" — insert Justoon-pick step

**Files:**
- Modify: `/Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md` (Process section, around lines 388-394)

The current process has 10 numbered steps. Insert a new step between current step 5 (Map each slide to a template type) and current step 6 (Generate per-slide directives). The new step picks Justoon variants. All subsequent steps shift +1.

- [ ] **Step 1: Edit — insert the Justoon-pick step**

Use the Edit tool with:

**old_string:**
```
### 5. Map each slide to a template type

Apply the §5 mapping table. Apply user steering or overrides if provided. For combined slide types (e.g., `FRAME + STAKES`), pick the first sub-label's template type and note the combination in the prompt.

### 6. Generate per-slide directives

For each slide, compose: kicker text (per §6), headline, body, animation specifications (per §7).
```

**new_string:**
```
### 5. Map each slide to a template type

Apply the §5 mapping table. Apply user steering or overrides if provided. For combined slide types (e.g., `FRAME + STAKES`), pick the first sub-label's template type and note the combination in the prompt.

### 5b. Pick Justoon variants (only when `--justoon-refs` is provided)

Resolve `--justoon-refs` (invocation argument, or default `~/Pictures/tcn-justin-slideshow/`). If the path doesn't exist, log "no Justoon" mode and skip this step entirely.

For each slide whose template-type row in the mapping table specifies a Justoon role (A or C):

1. Apply the role's variant-pick rule from `references/template-mapping.md` §7 (interpretive — based on the slide's specific content, not a rigid table).
2. Verify the picked file exists in `--justoon-refs`. If missing, fall back to `justoon-neutral.png` and note the substitution in the artifact header.
3. Honor any per-slide override from user steering ("Slide 8: use raised-eyebrow instead of deadpan" / "Slide 4: no Justoon").

Slides whose role is `none` get no Justoon. Slides that would have been Justoon-active but where the user steered "no Justoon on this dispatch" get no Justoon.

If `justoon-neutral.png` itself is missing from the refs dir, halt and surface to the user: the anchor / fallback is required.

### 6. Generate per-slide directives

For each slide, compose: kicker text (per §6), headline, body, animation specifications (per §7), AND — when Justoon is in play on this slide — the Justoon block (role + variant filename) per the Output Format spec.
```

- [ ] **Step 2: Verify the edit landed**

Run:
```bash
grep -c "### 5b. Pick Justoon variants" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Expected: `1`.

- [ ] **Step 3: No commit** — skill not in a git repo.

---

## Task 7: SKILL.md §"Failure Modes" + §"Reference Files" — bundled cleanups

**Files:**
- Modify: `/Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md` (Failure Modes around lines 416-422; Reference Files around line 461)

- [ ] **Step 1: Edit — add Justoon-related failure modes**

Use the Edit tool with:

**old_string:**
```
- **Combined slide type encountered** (e.g., `FRAME + STAKES`) — pick the first sub-label's template type, adjust the layout (fewer numbered columns, more prose), note the combination in the prompt's slide-by-slide block.
- **User redirects** — re-invoke the affected step. Common redirects:
```

**new_string:**
```
- **Combined slide type encountered** (e.g., `FRAME + STAKES`) — pick the first sub-label's template type, adjust the layout (fewer numbered columns, more prose), note the combination in the prompt's slide-by-slide block. Justoon role also uses the first sub-label's role.
- **`--justoon-refs` path provided but directory missing** — halt with a setup note (where to place files, link to `~/Pictures/tcn-justin-slideshow/CLAUDE.md` convention).
- **`justoon-neutral.png` missing from the refs dir** — halt with the same setup note. The anchor / fallback is required; without it, missing-variant substitution can't fall back safely.
- **Mapped Justoon variant missing from the refs dir** — fall back silently to `justoon-neutral.png` and note the substitution in the artifact's header (e.g., `**Justoon substitution:** intended justoon-react-deadpan.png on Slide 8, used justoon-neutral.png (file not found).`).
- **No `--justoon-refs` flag and no config file** — produce today's typography-only output unchanged. Not a failure; the absence is the explicit opt-out.
- **User redirects** — re-invoke the affected step. Common redirects:
```

- [ ] **Step 2: Edit — add a Justoon redirect to the common-redirects list**

Use the Edit tool with:

**old_string:**
```
  - "rebuild from scratch with steering X" → re-run the full process with steering applied
```

**new_string:**
```
  - "rebuild from scratch with steering X" → re-run the full process with steering applied
  - "swap Slide N Justoon to <variant>" → re-pick that slide's Justoon variant and regenerate the Justoon block in the prompt only
  - "drop Justoon from Slide N" → set Slide N's Justoon to none; regenerate that slide's directive without the Justoon block
  - "no Justoon on this dispatch" → re-run with Justoon mode forced off; produce typography-only output even though refs are present
```

- [ ] **Step 3: Edit — extend §"Reference Files" with the layout reference + Justoon library convention**

Use the Edit tool with:

**old_string:**
```
## Reference Files

- `references/template-mapping.md` — full narration-zone → slide-template mapping table with fallback rules, combined-type handling, kicker convention details, and animation directive tables.
```

**new_string:**
```
## Reference Files

- `references/template-mapping.md` — full narration-zone → slide-template mapping table with fallback rules, combined-type handling, kicker convention details, animation directive tables, AND (as of 2026-05-25) the §7 Justoon variant-pick guidance for role A and role C slides.
- **Justoon layout reference (in the Substack Research project repo, not in this skill dir):** `docs/superpowers/reference-renders/2026-05-25-justoon-slideshow-layout.html` — the proven CSS layout from the 2026-05-25 hand-test. Open this in a browser to see the target output the Claude Design prompt should produce. Both role A (pointing teacher) and role C (reaction-as-anchor) are demonstrated at 1:1, 16:9, 9:16, and 1:1 thumbnail (240×240) aspects.
- **Justoon library convention:** `~/Pictures/tcn-justin-slideshow/CLAUDE.md` — naming, format spec, inventory, regeneration workflow. The skill reads its `--justoon-refs` from here by default.
```

- [ ] **Step 4: Verify all three edits landed**

Run:
```bash
grep -c "justoon-refs.*path provided but directory missing" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "swap Slide N Justoon" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "Justoon layout reference" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "Justoon library convention" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Expected: `1` each.

- [ ] **Step 5: No commit** — skill not in a git repo.

---

## Task 8: references/template-mapping.md — append §7 Justoon variant-pick guidance

**Files:**
- Modify: `/Users/justin/.claude/skills/tcn-youtube-slideshow/references/template-mapping.md` (append after §6 Future-option seam, end of file around line 153)

- [ ] **Step 1: Edit — append §7 Justoon variant-pick to the end of the file**

Use the Edit tool with:

**old_string:**
```
## 6. Future-option seam

Per the spec's Q8=B path, a future iteration may extend `deck-stage.js` with NEW animation primitives — scroll-triggered number counters (numbers ticking up), text-typewriter effects on quote slides, programmatic chart morphing between data slides, dynamic radial-glow pulses that breathe with the slide. Not built today — the existing primitives, used aggressively, should be enough for the first few decks. When/if needed, the prompt structure can accept new animation directives without restructuring the skill itself — only the §3 animation table and the SKILL.md's Animation Intensification section need updating.
```

**new_string:**
```
## 6. Future-option seam

Per the spec's Q8=B path, a future iteration may extend `deck-stage.js` with NEW animation primitives — scroll-triggered number counters (numbers ticking up), text-typewriter effects on quote slides, programmatic chart morphing between data slides, dynamic radial-glow pulses that breathe with the slide. Not built today — the existing primitives, used aggressively, should be enough for the first few decks. When/if needed, the prompt structure can accept new animation directives without restructuring the skill itself — only the §3 animation table and the SKILL.md's Animation Intensification section need updating.

---

## 7. Justoon variant-pick guidance

Activated when `--justoon-refs` is provided to the skill. Read this section at process step 5b ("Pick Justoon variants").

The Justoon role per slide type is locked in the SKILL.md mapping table (Receipt/Stakes → A; Twist → C; others → none). This section is the **interpretive layer** that picks the specific filename inside each role based on the slide's content.

### Role A — Pointing teacher (full-body)

Picked for Receipt and Stakes slides. Available variants:

| File | When to pick |
|---|---|
| `justoon-point-right.png` | **Default.** Slide layout has the hero stat / headline on the right; Justoon left points across to it. Receipt slides almost always land here. |
| `justoon-point-up.png` | Slide layout has the hero stat / headline above Justoon. Less common — use when the narration phrasing implies "look up at this" or when a vertical 9:16 derivative wants Justoon at the bottom pointing up to text above. |
| `justoon-point-down.png` | Slide layout has the hero stat below Justoon (rare — only when the visual composition really wants Justoon at the top half pointing down). |
| `justoon-point-open-palm.png` | **Bidirectional fallback.** Soft "here's the thing" presenting gesture. Use when the slide content is more presentational than data-pointed (e.g., a Stakes slide that summarizes rather than naming a specific number). Also use when neither the right-pointing nor up-pointing variants feel right. |

Picking rule:
- If the slide has a single dominant hero number / hero word in the right half of the safe-zone → `justoon-point-right.png`
- If the dominant element is above Justoon → `justoon-point-up.png`
- If the slide is presentational (multiple supporting points, no single hero stat) → `justoon-point-open-palm.png`
- Default fallback within role A → `justoon-point-right.png`

### Role C — Reaction-as-anchor (bust)

Picked for Twist slides. Available variants:

| File | When to pick |
|---|---|
| `justoon-react-deadpan.png` | The dry, flat-stare register. For Twist slides whose narration close is deadpan / "by whom, the company says, can't be known" / "the cause was impossible to determine" / any slide where the rhetorical move is *the absence of expression*. The canonical role C variant. |
| `justoon-react-raised-eyebrow.png` | The "really?" register. For Twist slides where the absurdity is the move but the figure shouldn't editorialize fully. |
| `justoon-react-concerned.png` | Furrowed brow, alarm. For Twist slides where the stakes are real and the figure should signal that. |
| `justoon-react-smirk.png` | The sardonic-amused register. For Twist slides whose narration carries dry wit or "you can't make this up" energy. The TCN signature dial. |
| `justoon-react-shocked.png` | Open mouth, "they did WHAT". For Twist slides at the highest-arousal register. **Use sparingly** — shock loses force when overused; reserve for genuinely visceral reveals (~1 in 5 Twist slides). |

Picking rule (interpretive — read the slide's narration body, not just the kicker):
- Default fallback within role C → `justoon-react-deadpan.png` (the canonical TCN-Marcus close)
- Narration ends with a "you can't make this up" smirk → `justoon-react-smirk.png`
- Narration carries an "I want to react but I'm restraining myself" beat → `justoon-react-raised-eyebrow.png`
- Narration signals real-stakes alarm → `justoon-react-concerned.png`
- Narration is high-arousal incredulity → `justoon-react-shocked.png`

### Anchor / fallback

`justoon-neutral.png` is the required anchor. Used when:
- A mapped variant is missing from the refs dir (silent substitution; note in artifact header)
- A future skill consumer needs a stable Justoon image without role context (e.g., a `tcn-youtube-thumbnail` cross-reference)

### Coherence across slides

Don't aggressively vary Justoon variants across a single deck — the figure should feel consistent. A deck with three Twist slides shouldn't pick three different reactions just for variety; pick the variant that fits the dominant register and reuse it unless a specific slide demands a different read.

### Worked example (dispatch-005, bill-of-rights-contractors-door)

The 11-slide deck has 4 slides with Justoon roles active:

- Slide 3 (Receipt · Bend): role A → `justoon-point-right.png` (hero stat "279" is in the right half)
- Slide 4 (Receipt · Scale): role A → `justoon-point-right.png` (consistency with Slide 3; hero stats "364,000" / "1.6 million" / "4,500" all live in the right half)
- Slide 8 (Twist): role C → `justoon-react-deadpan.png` (the narration close "By whom, the company says, can't be known." is the canonical deadpan beat)
- Slide 9 (Stakes): role A → `justoon-point-open-palm.png` (presentational summary of Atlanta's resolution stack, no single hero stat)

The other 7 slides (Hook, Thesis, Frame, Anaphora ×2, Tease, End) stay typography-only.
```

- [ ] **Step 2: Verify the edit landed**

Run:
```bash
grep -c "^## 7. Justoon variant-pick guidance" /Users/justin/.claude/skills/tcn-youtube-slideshow/references/template-mapping.md
grep -c "justoon-react-deadpan" /Users/justin/.claude/skills/tcn-youtube-slideshow/references/template-mapping.md
grep -c "Worked example (dispatch-005" /Users/justin/.claude/skills/tcn-youtube-slideshow/references/template-mapping.md
```

Expected: `1` each.

- [ ] **Step 3: No commit** — file not in a git repo.

---

## Task 9: End-to-end verification — trace updated skill against dispatch-005's narration

**Files:**
- Read: `/Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md` (post-edit state)
- Read: `/Users/justin/.claude/skills/tcn-youtube-slideshow/references/template-mapping.md` (post-edit state)
- Read: `/Users/justin/Documents/substack-research/Substack Research/workspace/drafts/bill-of-rights-contractors-door/youtube-narration.md`

The actual skill is invoked via the `Skill` tool by the user. This task is the executor manually tracing through the skill's process against the dispatch-005 narration to confirm the expected output shape. It does NOT invoke the skill; it verifies the skill instructions would produce the right output if invoked.

- [ ] **Step 1: Confirm the narration is the 11-slide v2 we updated earlier**

Run:
```bash
grep -E "^\*\*\[SLIDE [0-9]+ " "/Users/justin/Documents/substack-research/Substack Research/workspace/drafts/bill-of-rights-contractors-door/youtube-narration.md" | wc -l
```

Expected: `11` (one per slide marker).

- [ ] **Step 2: Identify the 4 Justoon-active slides per the mapping**

Run:
```bash
grep -E "^\*\*\[SLIDE " "/Users/justin/Documents/substack-research/Substack Research/workspace/drafts/bill-of-rights-contractors-door/youtube-narration.md"
```

Expected output:
```
**[SLIDE 01 — HOOK]**
**[SLIDE 02 — THESIS]**
**[SLIDE 03 — RECEIPT · BEND]**
**[SLIDE 04 — RECEIPT · SCALE]**
**[SLIDE 05 — FRAME]**
**[SLIDE 06 — ANAPHORA · SPEECH + SEARCH]**
**[SLIDE 07 — ANAPHORA · BIOMETRIC + HEALTH]**
**[SLIDE 08 — TWIST]**
**[SLIDE 09 — STAKES]**
**[SLIDE 10 — TEASE]**
**[SLIDE 11 — END]**
```

Per the updated mapping table:
- Slide 3 (RECEIPT) → role A
- Slide 4 (RECEIPT) → role A
- Slide 8 (TWIST) → role C
- Slide 9 (STAKES) → role A

The other 7 (Hook, Thesis, Frame, Anaphora ×2, Tease, End) get no Justoon. This matches the §7 Worked Example we just wrote into template-mapping.md.

- [ ] **Step 3: Apply the §7 variant-pick rules to each active slide**

Tracing through with the updated picker logic:

- **Slide 3 (Receipt · Bend)** — hero stat "279" is the dominant right-side element → `justoon-point-right.png`. ✓ matches the §7 Worked Example.
- **Slide 4 (Receipt · Scale)** — hero stats "364,000" / "1.6 million" / "4,500" all right-side → `justoon-point-right.png` (consistency rule). ✓ matches.
- **Slide 8 (Twist)** — narration ends "By whom, the company says, can't be known." (canonical deadpan beat) → `justoon-react-deadpan.png`. ✓ matches.
- **Slide 9 (Stakes)** — presentational summary of Atlanta's resolution stack, no single hero number, narration ends "The next agency querying them doesn't have to read a single Atlanta document." → `justoon-point-open-palm.png` (presentational, bidirectional fallback). ✓ matches.

The skill's updated process step 5b would produce these picks deterministically.

- [ ] **Step 4: Confirm the updated Claude Design prompt template would emit the right CSS for these slides**

For the post-edit Output Format section to be correct, the emitted prompt should contain:
- `--type-h2-mid` clamp definition (new role we added)
- `.slide-receipt .justoon` CSS rule (role A — Slides 3, 4, 9)
- `.slide-twist .justoon` CSS rule (role C — Slide 8)
- A `.slide-stakes .justoon` rule reusing the role A pattern (since Slide 9 is Stakes, not Receipt) — verify this is documented

Run:
```bash
grep -E "\.slide-stakes \.justoon|\.slide-receipt \.justoon, \.slide-stakes" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Expected: at least 1 match. The Task 5 edit grouped Receipt and Stakes under the same CSS rule (`.slide-receipt .justoon, .slide-stakes .justoon`). Confirm this is correct for Slide 9's role A treatment.

- [ ] **Step 5: Confirm there's no regression at the brand-rules level**

Run:
```bash
grep -c "No emoji, no icon fonts" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "Courier Prime" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
grep -c "slate-400 / slate-600 / black / twilight" /Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md
```

Expected: all positive counts. None of the brand-rule strings should have been accidentally edited.

- [ ] **Step 6: No commit** — verification only.

---

## Task 10: Commit the plan file to the project repo

**Files:**
- Already created: `docs/superpowers/plans/2026-05-25-justoon-slideshow-skill-integration.md` (this file)

- [ ] **Step 1: Stage the plan file**

Run from the project repo root:
```bash
cd "/Users/justin/Documents/substack-research/Substack Research"
git add docs/superpowers/plans/2026-05-25-justoon-slideshow-skill-integration.md
git status --short
```

Expected: shows the plan staged, nothing else newly staged.

- [ ] **Step 2: Commit**

Run:
```bash
git commit -m "$(cat <<'EOF'
plan: Justoon slideshow skill integration (2026-05-25)

Implementation plan to update tcn-youtube-slideshow skill so it
consumes the Justoon library (~/Pictures/tcn-justin-slideshow/) and
emits Claude Design prompts with per-slide Justoon directives plus
the 1:1-primary layout primitives proven in the hand-test reference
(docs/superpowers/reference-renders/2026-05-25-justoon-slideshow-
layout.html, commit 237bc28).

Derived from the design spec at docs/superpowers/specs/2026-05-25-
justoon-slideshow-library-design.md (commit 77675df) plus three
architectural deltas surfaced during the 2026-05-25 hand-test:
1:1 is primary recording aspect (not 16:9); absolute positioning
with cqh max-heights beats grid for Justoon placement; token
clamps tuned for 1:1 primary + text-wrap: balance for clean line
breaks.

9 execution tasks: discovery, 6 surgical SKILL.md edits, 1
references/template-mapping.md append (§7 variant-pick guidance),
end-to-end trace against dispatch-005's 11-slide narration.

The skill files live in ~/.claude/skills/ which is NOT a git repo,
so skill edits do not commit anywhere — only this plan file
commits. Out of scope: rendering dispatch-005's deck through
Claude Design (Justin's manual step after plan execution).

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

- [ ] **Step 3: Verify**

Run:
```bash
git log --oneline -5
```

Expected: latest commit is the plan commit; previous commits in order are the reference render (237bc28), library plan (a45aefa), beard fix (a0c4a07), narration rewrite (39259d4).

---

## What ships after this plan executes

On disk (NOT in any git repo — `~/.claude/skills/` is not version-controlled):
- Updated `/Users/justin/.claude/skills/tcn-youtube-slideshow/SKILL.md` with 6 sections edited
- Updated `/Users/justin/.claude/skills/tcn-youtube-slideshow/references/template-mapping.md` with new §7 Justoon picker

In the project repo:
- `docs/superpowers/plans/2026-05-25-justoon-slideshow-skill-integration.md` (this plan, committed)

What does NOT ship (deferred to Justin's manual step):
- A rendered HTML deck for dispatch-005 with Justoon on Slides 3, 4, 8, 9. To produce that, Justin invokes the updated `tcn-youtube-slideshow` skill on the dispatch-005 narration, then pastes the emitted Claude Design prompt into claude.ai/design with the design system bundle attached and the `~/Pictures/tcn-justin-slideshow/` PNGs uploadable as scene references. Claude Design then renders the HTML.

## Next step after this plan executes

Justin runs the updated skill on dispatch-005's narration:
```
Skill tool: tcn-youtube-slideshow
args: workspace/drafts/bill-of-rights-contractors-door/youtube-narration.md
```

The output `workspace/drafts/bill-of-rights-contractors-door/youtube-slideshow.md` should contain:
1. A header noting `--justoon-refs` mode is active
2. The 1:1-primary safe-zone CSS + new clamp values + `text-wrap: balance` directives
3. The `.justoon` CSS rules (both role A and role C variants)
4. Per-slide Justoon blocks on Slides 3, 4, 8, 9 (variants per Task 9 Step 3 trace)
5. A reference to `docs/superpowers/reference-renders/2026-05-25-justoon-slideshow-layout.html` as the layout ground truth
6. The other 7 slides typography-only (no Justoon block)

Justin pastes that prompt into claude.ai/design, uploads the design system + the 4 needed Justoon PNGs (justoon-point-right, justoon-react-deadpan, justoon-point-open-palm, justoon-neutral as fallback), and Claude Design renders `dispatch-005.html`. Justin records by resizing to 1080×1080 (primary) and screen-capturing.
