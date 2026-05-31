# Justoon Slideshow Library Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create the `~/Pictures/tcn-justin-slideshow/` library directory and populate it with two documentation artifacts — `CLAUDE.md` (library convention doc) and `_generation-prompts.md` (10 paste-ready prompts for Freepik/Magnific). After this plan executes, the user can work through the prompt file manually to populate the library with the 10 PNG variants.

**Architecture:** Three artifacts on disk in `~/Pictures/tcn-justin-slideshow/`. No code changes. No git commits inside `~/Pictures/` (not a git repo). The two markdown files inherit anti-drift discipline from `~/.claude/skills/tcn-youtube-thumbnail/references/reference-image-prompt-template.md` (wardrobe preservation, forbid-the-default expression language for role C, character-reference instruction pattern).

**Tech Stack:** Filesystem only — `mkdir`, `Write` tool. No external tools. No image generation in this plan (deferred to user's manual Freepik/Magnific work after the plan finishes).

**Scope boundary:** This plan only produces the library scaffold + prompt batch. The plan does NOT modify `tcn-youtube-slideshow`, does NOT generate any PNG variants, does NOT render dispatch-005's slideshow. Those are separate work, deferred per the approved spec.

**Reference docs:**
- Spec: [`docs/superpowers/specs/2026-05-25-justoon-slideshow-library-design.md`](../specs/2026-05-25-justoon-slideshow-library-design.md) (commit `77675df`)
- Anti-drift discipline to inherit: `~/.claude/skills/tcn-youtube-thumbnail/references/reference-image-prompt-template.md`
- Existing library convention (for naming-pattern parallel): `~/Pictures/tcn-justin-references/` (no human-authored CLAUDE.md exists there — claude-mem owns its CLAUDE.md)

---

## Task 1: Create the library directory

**Files:**
- Create: `~/Pictures/tcn-justin-slideshow/` (directory only)

- [ ] **Step 1: Create the directory**

Run:
```bash
mkdir -p ~/Pictures/tcn-justin-slideshow/
```

- [ ] **Step 2: Verify it exists and is empty**

Run:
```bash
ls -la ~/Pictures/tcn-justin-slideshow/
```

Expected output: just `.` and `..` (empty dir) — confirms creation succeeded and we're not silently writing into a populated location.

- [ ] **Step 3: No commit**

`~/Pictures/` is not a git repo. Skip commit. The plan-level commit at the end of this plan covers the plan file itself.

---

## Task 2: Write `~/Pictures/tcn-justin-slideshow/CLAUDE.md`

**Files:**
- Create: `~/Pictures/tcn-justin-slideshow/CLAUDE.md`

**Design notes (read before writing):**
- The thumbnail library's `CLAUDE.md` is auto-managed by claude-mem (the user's memory tool) and contains only auto-generated activity log content. Our `CLAUDE.md` is hand-authored library convention — must coexist with claude-mem, which appends inside `<claude-mem-context>` tags.
- Structure: hand-authored sections FIRST, then nothing else. If claude-mem ever fires against this file, it will append its tags below our content. We don't preemptively add the tags.
- Audience: future skill code (likely `tcn-youtube-slideshow` once the deferred integration plan runs) needs to read this file and understand which variant to pick for which slide type. Also future-Justin reading the dir cold.
- Tone: factual, terse, parallel in spirit to the SKILL.md docs for TCN skills. No marketing voice.

- [ ] **Step 1: Write the CLAUDE.md content**

Write the file with this exact content:

```markdown
# tcn-justin-slideshow — Justoon library for YouTube slideshows

Slideshow-specific Justoon variants. Distinct from the editorial-illustration
PNG library at `~/Pictures/tcn-justin-references/` (which is consumed by
`tcn-youtube-thumbnail`). This library is consumed by `tcn-youtube-slideshow`
(integration deferred to a follow-up plan as of 2026-05-25).

## Purpose

`tcn-youtube-slideshow` produces brand-restricted typography decks (Courier
Prime only, slate-400 / slate-600 / black / twilight palette, no shadows on
dark). The editorial-illustration register of the thumbnail library competes
with — and loses to — that typographic minimalism on a slide. This library
holds a separate Justoon stylization, matched to the slideshow's brand rules,
that can appear on slides as either:

- **Role A — Pointing teacher.** Full-body Justoon, gestures across the safe
  zone toward the slide's hero stat. Best on Receipt and Stakes slides where
  the stat reveal is the rhetorical move.
- **Role C — Reaction-as-anchor.** Bust-framed Justoon as the slide's hero
  anchor. Stat becomes secondary caption. Best on Twist and emotional-climax
  slides where the reaction itself is the rhetorical move.

Role B (corner reaction companion) is intentionally not in this library's
scope. Defer until role A + C surface a real gap across 2-3 dispatches.

## Inventory

Initial batch (10 variants). Each is generated manually via Freepik/Magnific
using the prompts in `_generation-prompts.md`.

| Filename | Role | Use case |
|---|---|---|
| `justoon-neutral.png` | anchor | Required fallback; re-render of `~/Pictures/justoon-neutral.svg` at PNG. |
| `justoon-point-right.png` | A | Points right; stat lives in right negative space. |
| `justoon-point-up.png` | A | Points up; headline lives above. |
| `justoon-point-down.png` | A | Points down-right; stat below the pointing finger. |
| `justoon-point-open-palm.png` | A | Soft presenting gesture; bidirectional fallback. |
| `justoon-react-deadpan.png` | C | Flat stare; dry-close slides. |
| `justoon-react-raised-eyebrow.png` | C | One eyebrow up; "really?" register. |
| `justoon-react-concerned.png` | C | Furrowed brow; alarm-bell slides. |
| `justoon-react-smirk.png` | C | Dry TCN signature smirk. |
| `justoon-react-shocked.png` | C | Open mouth + raised brows; "they did WHAT" moments. |

Add new variants by appending blocks to `_generation-prompts.md` following
the same block structure, then regenerating.

## Naming convention

`justoon-{role-marker}-{descriptor}.png`

- `justoon-neutral.png` — anchor / fallback (no role marker)
- `justoon-point-{direction-or-gesture}.png` — role A, full-body pointing
- `justoon-react-{expression}.png` — role C, bust reaction

The two role markers (`point` and `react`) map directly to the two integration
roles. A future skill picking a variant for a slide first decides role from
slide type, then picks the descriptor from the role's variant menu.

## Format

- PNG with transparent background
- 1024×1024 square
- No padding around the figure; figure should fill the canvas naturally
  (Freepik/Magnific outputs typically need a `remove.bg` pass to strip any
  background and tight-crop the figure)

## Regeneration workflow

All prompts live in `_generation-prompts.md`. To regenerate any variant:

1. Open `_generation-prompts.md`
2. Find the block for the target filename
3. Upload the named reference SVG (`~/Pictures/justoon-neutral.svg` for bust
   variants, `~/Pictures/justoon-standing.svg` for full-body variants) to
   Freepik/Magnific's character-reference field
4. Paste the prompt text
5. Set aspect to 1:1 (1024×1024), enable transparent background if available
6. Generate, post-process if needed, save as the named filename in this
   directory

## Fallback rule

`justoon-neutral.png` is the required anchor. A future skill consuming this
library should fall back to `justoon-neutral.png` if a tone-mapped variant is
missing, and surface the substitution in its output artifact header. This
mirrors the fallback pattern in `~/.claude/skills/tcn-youtube-thumbnail/references/reference-image-prompt-template.md`.

## Consumed by

- `tcn-youtube-slideshow` (integration deferred; see the design spec at
  `docs/superpowers/specs/2026-05-25-justoon-slideshow-library-design.md` in
  the Substack Research project repo)

This library is intentionally NOT consumed by `tcn-youtube-thumbnail` —
thumbnails use the editorial-illustration register at
`~/Pictures/tcn-justin-references/`. The two libraries are parallel, not
shared.
```

- [ ] **Step 2: Verify the file wrote correctly**

Run:
```bash
ls -la ~/Pictures/tcn-justin-slideshow/CLAUDE.md && wc -l ~/Pictures/tcn-justin-slideshow/CLAUDE.md
```

Expected: file exists, ~75-85 lines.

- [ ] **Step 3: Confirm the seven hand-authored sections are present**

Run:
```bash
grep -E "^## " ~/Pictures/tcn-justin-slideshow/CLAUDE.md
```

Expected output (exact match):
```
## Purpose
## Inventory
## Naming convention
## Format
## Regeneration workflow
## Fallback rule
## Consumed by
```

If any section is missing, the file write was wrong — re-run Step 1.

- [ ] **Step 4: No commit**

Same as Task 1 — not a git repo.

---

## Task 3: Write `~/Pictures/tcn-justin-slideshow/_generation-prompts.md`

**Files:**
- Create: `~/Pictures/tcn-justin-slideshow/_generation-prompts.md`

**Design notes (read before writing):**
- 10 prompt blocks, one per variant from the Inventory table in CLAUDE.md.
- Each block follows a uniform structure (defined in spec §"Prompt block structure").
- Every block must include all five inherited components, adapted to the chosen variant:
  1. **Character consistency directive** — "use attached reference; match facial features, wardrobe, illustrated style exactly"
  2. **Style anchor** — "match the reference image's visual register and stylization exactly; do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to explainer-cartoon"
  3. **Composition directive** — framing (bust vs. full-body), pose/expression specifics, eye direction, eyebrow state, mouth state
  4. **Expression-preservation language (role C only)** — explicit forbid-the-default ("do NOT soften toward neutral friendly", per the exact patterns proven in `tcn-youtube-thumbnail`'s reference-image-prompt-template)
  5. **Wardrobe preservation** — "salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red DICKIES brand patch (preserve this patch exactly — NO Supreme or other brand substitutions), olive-grey t-shirt, dark jeans"
- Bust variants (role C reactions) attach `justoon-neutral.svg` as reference.
- Full-body variants (role A pointing + anchor) attach `justoon-standing.svg` as reference. EXCEPTION: `justoon-neutral.png` re-renders `justoon-neutral.svg` itself (it's the bust anchor), so attach `justoon-neutral.svg`.

Wait — re-check: the spec says `justoon-neutral.png` is the anchor / fallback. The thumbnail equivalent is `headshot-neutral-forward.png` (a bust). But the source SVG `justoon-neutral.svg` is — based on naming — probably a bust. And `justoon-standing.svg` is the full-body. Confirm by the user's earlier statement: "neutral" suggests headshot-ish. Use `justoon-neutral.svg` for `justoon-neutral.png` (bust anchor) and for all role C bust reactions. Use `justoon-standing.svg` for all role A full-body pointing variants.

- [ ] **Step 1: Write the file's frame + the anchor block**

Write the file with this initial content (we'll continue appending the remaining 9 blocks in subsequent steps — write the whole file in one Write call):

```markdown
# Justoon slideshow library — generation prompts

10 paste-ready prompt blocks for Freepik/Magnific. Each block produces one
PNG variant for `~/Pictures/tcn-justin-slideshow/`. Work through top to
bottom, generating one at a time. The order is anchor → pointing poses
(role A) → reactions (role C).

**Workflow per block:**

1. Upload the named reference SVG to Freepik/Magnific's character-reference
   field
2. Paste the prompt text
3. Set aspect to 1:1, enable transparent background
4. Generate
5. Post-process if needed (`remove.bg` for stray background; tight-crop if
   figure is small in frame)
6. Save as the named filename in `~/Pictures/tcn-justin-slideshow/`

**Inherited discipline:** Every block uses the proven anti-drift pattern from
`~/.claude/skills/tcn-youtube-thumbnail/references/reference-image-prompt-template.md`
(wardrobe-preservation language with DICKIES patch protection, forbid-the-
default expression language for role C). Do not edit the wardrobe-preservation
or character-consistency language without understanding why it's there — both
were added after specific drift failures during the dispatch-004 thumbnail
test (Nano Banana 2 hallucinated a Supreme-style patch when wardrobe was
unspecified).

---

## 1 — justoon-neutral.png (anchor / fallback)

**Reference image to attach:** `~/Pictures/justoon-neutral.svg`
**Output spec:** 1024×1024, transparent background
**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-neutral.png`
**Post-processing:** if Freepik/Magnific renders any background, run through
`remove.bg` before saving.

**Prompt:**

> Use the attached reference image as the character reference. Match the
> character's facial features, hair, beard, cap, glasses, wardrobe, and
> illustrated visual register EXACTLY. This is a re-render of the same
> character at PNG resolution with a transparent background.
>
> COMPOSITION: Bust framing (upper chest up). Head centered, direct gaze
> toward camera. Neutral composed expression: no smile, no frown, no eyebrow
> raise. Mouth in relaxed neutral. Eyes looking directly at camera.
>
> STYLE: Match the reference image's visual register and stylization exactly.
> Do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to
> explainer-cartoon. The illustrated register of the reference is the target.
>
> WARDROBE: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red
> DICKIES brand patch (preserve this patch exactly — NO Supreme or other
> brand substitutions), olive-grey t-shirt, dark jeans.
>
> BACKGROUND: fully transparent. No background fill, no environment, no
> backdrop. The character should be the only visible content on a transparent
> canvas.
>
> ASPECT: 1:1, 1024×1024.
>
> EXCLUDE: text, words, captions, watermarks, signs, lettering anywhere in
> the image; secondary figures; background scenery.

---
```

Continue the file by appending these 9 more blocks (writing the entire file in one `Write` call — include all blocks). The blocks follow:

### Pointing poses (role A) — blocks 2-5

```markdown
## 2 — justoon-point-right.png (role A)

**Reference image to attach:** `~/Pictures/justoon-standing.svg`
**Output spec:** 1024×1024, transparent background
**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-point-right.png`
**Post-processing:** if Freepik/Magnific renders any background, run through
`remove.bg` before saving. Tight-crop if figure is small in frame.

**Prompt:**

> Use the attached reference image as the character reference. Match the
> character's facial features, hair, beard, cap, glasses, wardrobe, and
> illustrated visual register EXACTLY.
>
> COMPOSITION: Full-body standing figure, positioned at the LEFT 25-30% of
> the frame. Right arm extended, hand pointing across to the upper-right of
> the frame. Eyes follow the pointing finger (gaze directed up-right, NOT
> at camera). Eyebrows slightly raised (engaged, not surprised). Mouth in
> a slight closed-lip "look at this" expression — engaged but not smiling.
>
> STYLE: Match the reference image's visual register and stylization exactly.
> Do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to
> explainer-cartoon. The illustrated register of the reference is the target.
>
> WARDROBE: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red
> DICKIES brand patch (preserve this patch exactly — NO Supreme or other
> brand substitutions), olive-grey t-shirt, dark jeans.
>
> BACKGROUND: fully transparent. No background fill, no environment, no
> backdrop, no podium, no chart. The character should be the only visible
> content on a transparent canvas.
>
> ASPECT: 1:1, 1024×1024.
>
> EXCLUDE: text, words, captions, watermarks, signs, lettering anywhere in
> the image; secondary figures; background scenery; any object the character
> is pointing AT (the pointing gesture should be directional — the implied
> target is off-figure, supplied by the slide's content).

---

## 3 — justoon-point-up.png (role A)

**Reference image to attach:** `~/Pictures/justoon-standing.svg`
**Output spec:** 1024×1024, transparent background
**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-point-up.png`
**Post-processing:** same as previous.

**Prompt:**

> Use the attached reference image as the character reference. Match the
> character's facial features, hair, beard, cap, glasses, wardrobe, and
> illustrated visual register EXACTLY.
>
> COMPOSITION: Full-body standing figure, centered or slightly offset in the
> frame. One arm raised, hand pointing UP toward the top of the frame. Eyes
> follow the pointing finger (gaze directed upward, NOT at camera). Eyebrows
> slightly raised. Mouth in slight closed-lip "look up" expression.
>
> STYLE: Match the reference image's visual register and stylization exactly.
> Do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to
> explainer-cartoon.
>
> WARDROBE: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red
> DICKIES brand patch (preserve this patch exactly — NO Supreme or other
> brand substitutions), olive-grey t-shirt, dark jeans.
>
> BACKGROUND: fully transparent.
>
> ASPECT: 1:1, 1024×1024.
>
> EXCLUDE: text, words, captions, watermarks; secondary figures; background
> scenery; any object the character is pointing AT.

---

## 4 — justoon-point-down.png (role A)

**Reference image to attach:** `~/Pictures/justoon-standing.svg`
**Output spec:** 1024×1024, transparent background
**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-point-down.png`
**Post-processing:** same as previous.

**Prompt:**

> Use the attached reference image as the character reference. Match the
> character's facial features, hair, beard, cap, glasses, wardrobe, and
> illustrated visual register EXACTLY.
>
> COMPOSITION: Full-body standing figure, positioned at the upper LEFT 25-
> 30% of the frame. Arm extended, hand pointing DOWN and to the right of
> the frame. Eyes follow the pointing finger (gaze directed down-right, NOT
> at camera). Eyebrows slightly raised. Mouth in slight closed-lip
> "look at this below" expression.
>
> STYLE: Match the reference image's visual register and stylization exactly.
> Do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to
> explainer-cartoon.
>
> WARDROBE: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red
> DICKIES brand patch (preserve this patch exactly — NO Supreme or other
> brand substitutions), olive-grey t-shirt, dark jeans.
>
> BACKGROUND: fully transparent.
>
> ASPECT: 1:1, 1024×1024.
>
> EXCLUDE: text, words, captions, watermarks; secondary figures; background
> scenery; any object the character is pointing AT.

---

## 5 — justoon-point-open-palm.png (role A)

**Reference image to attach:** `~/Pictures/justoon-standing.svg`
**Output spec:** 1024×1024, transparent background
**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-point-open-palm.png`
**Post-processing:** same as previous.

**Prompt:**

> Use the attached reference image as the character reference. Match the
> character's facial features, hair, beard, cap, glasses, wardrobe, and
> illustrated visual register EXACTLY.
>
> COMPOSITION: Full-body standing figure, positioned at the LEFT 25-30% of
> the frame. Right arm extended, hand open with palm up (presenting gesture,
> NOT pointing with index finger). Eyes looking out toward the right side
> of the frame (gaze follows the open palm, NOT at camera). Eyebrows in
> neutral position. Mouth in slight closed-lip "here's the thing"
> expression — softer than directional pointing.
>
> STYLE: Match the reference image's visual register and stylization exactly.
> Do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to
> explainer-cartoon.
>
> WARDROBE: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red
> DICKIES brand patch (preserve this patch exactly — NO Supreme or other
> brand substitutions), olive-grey t-shirt, dark jeans.
>
> BACKGROUND: fully transparent.
>
> ASPECT: 1:1, 1024×1024.
>
> EXCLUDE: text, words, captions, watermarks; secondary figures; background
> scenery; any object the character is presenting (the open-palm gesture
> implies a target supplied by the slide's content, not in the image).

---
```

### Reactions (role C) — blocks 6-10

```markdown
## 6 — justoon-react-deadpan.png (role C)

**Reference image to attach:** `~/Pictures/justoon-neutral.svg`
**Output spec:** 1024×1024, transparent background
**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-react-deadpan.png`
**Post-processing:** if Freepik/Magnific renders any background, run through
`remove.bg` before saving.

**Prompt:**

> Use the attached reference image as the character reference. Match the
> character's facial features, hair, beard, cap, glasses, wardrobe, and
> illustrated visual register EXACTLY.
>
> COMPOSITION: Bust framing (upper chest up). Head centered, direct gaze
> toward camera.
>
> CRITICAL EXPRESSION DIRECTIVE: Flat deadpan stare. Mouth completely
> neutral (closed, no smile, no frown, perfectly flat). Eyebrows perfectly
> level (no raise, no furrow). Eyes directed at camera with a flat, unimpressed
> stillness. The expression should read as "I am saying nothing on purpose."
> Do NOT render a micro-smile. Do NOT raise an eyebrow. Do NOT add any
> warmth, amusement, or expression — the deadpan IS the rhetorical move,
> and softening it kills it.
>
> STYLE: Match the reference image's visual register and stylization exactly.
> Do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to
> explainer-cartoon.
>
> WARDROBE: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red
> DICKIES brand patch (preserve this patch exactly — NO Supreme or other
> brand substitutions), olive-grey t-shirt, dark jeans.
>
> BACKGROUND: fully transparent.
>
> ASPECT: 1:1, 1024×1024.
>
> EXCLUDE: text, words, captions, watermarks; secondary figures; background
> scenery.

---

## 7 — justoon-react-raised-eyebrow.png (role C)

**Reference image to attach:** `~/Pictures/justoon-neutral.svg`
**Output spec:** 1024×1024, transparent background
**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-react-raised-eyebrow.png`
**Post-processing:** same as previous.

**Prompt:**

> Use the attached reference image as the character reference. Match the
> character's facial features, hair, beard, cap, glasses, wardrobe, and
> illustrated visual register EXACTLY.
>
> COMPOSITION: Bust framing (upper chest up). Head centered, direct gaze
> toward camera.
>
> CRITICAL EXPRESSION DIRECTIVE: Neutral mouth (closed, no smile), but with
> ONE eyebrow visibly raised — the LEFT eyebrow from the viewer's
> perspective — and the other eyebrow held level. This is the classic
> asymmetric "really?" register. Eyes directed at camera with a skeptical-
> but-restrained read. Do NOT smooth the raised eyebrow back to symmetric.
> Do NOT add any smile (a micro-smile would shift this from "really?" to
> "ah, of course"). The asymmetry IS the expression — it must be visibly
> uneven.
>
> STYLE: Match the reference image's visual register and stylization exactly.
> Do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to
> explainer-cartoon.
>
> WARDROBE: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red
> DICKIES brand patch (preserve this patch exactly — NO Supreme or other
> brand substitutions), olive-grey t-shirt, dark jeans.
>
> BACKGROUND: fully transparent.
>
> ASPECT: 1:1, 1024×1024.
>
> EXCLUDE: text, words, captions, watermarks; secondary figures; background
> scenery.

---

## 8 — justoon-react-concerned.png (role C)

**Reference image to attach:** `~/Pictures/justoon-neutral.svg`
**Output spec:** 1024×1024, transparent background
**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-react-concerned.png`
**Post-processing:** same as previous.

**Prompt:**

> Use the attached reference image as the character reference. Match the
> character's facial features, hair, beard, cap, glasses, wardrobe, and
> illustrated visual register EXACTLY.
>
> COMPOSITION: Bust framing (upper chest up). Head centered, direct gaze
> toward camera.
>
> CRITICAL EXPRESSION DIRECTIVE: Furrowed brow (both eyebrows pulled down
> and slightly together, creating visible tension lines between them).
> Slight mouth downturn (closed, no teeth — corners turned down, lips
> still touching). Eyes alert and direct, not pleading. The expression
> should read as "this is not good" — an alert concern, not panic, not
> fear. Do NOT render a stoic or neutral expression — the concern must
> register clearly. Do NOT soften toward worry or sadness — this is alert
> concern.
>
> STYLE: Match the reference image's visual register and stylization exactly.
> Do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to
> explainer-cartoon.
>
> WARDROBE: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red
> DICKIES brand patch (preserve this patch exactly — NO Supreme or other
> brand substitutions), olive-grey t-shirt, dark jeans.
>
> BACKGROUND: fully transparent.
>
> ASPECT: 1:1, 1024×1024.
>
> EXCLUDE: text, words, captions, watermarks; secondary figures; background
> scenery.

---

## 9 — justoon-react-smirk.png (role C)

**Reference image to attach:** `~/Pictures/justoon-neutral.svg`
**Output spec:** 1024×1024, transparent background
**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-react-smirk.png`
**Post-processing:** same as previous.

**Prompt:**

> Use the attached reference image as the character reference. Match the
> character's facial features, hair, beard, cap, glasses, wardrobe, and
> illustrated visual register EXACTLY.
>
> COMPOSITION: Bust framing (upper chest up). Head centered, direct gaze
> toward camera.
>
> CRITICAL EXPRESSION DIRECTIVE: Closed-lipped half-smile (ONE side of the
> mouth slightly raised, the other neutral — asymmetric). One eyebrow
> slightly raised to match. Sardonic-amused register, restrained, knowing,
> slightly conspiratorial. Eyes directed at camera with a "we both see what's
> happening here" read. Do NOT render a warm friendly smile with teeth
> showing — the smirk is restrained and closed-lip, NOT a grin. Do NOT
> render a symmetric smile — the asymmetry IS the smirk.
>
> STYLE: Match the reference image's visual register and stylization exactly.
> Do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to
> explainer-cartoon.
>
> WARDROBE: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red
> DICKIES brand patch (preserve this patch exactly — NO Supreme or other
> brand substitutions), olive-grey t-shirt, dark jeans.
>
> BACKGROUND: fully transparent.
>
> ASPECT: 1:1, 1024×1024.
>
> EXCLUDE: text, words, captions, watermarks; secondary figures; background
> scenery.

---

## 10 — justoon-react-shocked.png (role C)

**Reference image to attach:** `~/Pictures/justoon-neutral.svg`
**Output spec:** 1024×1024, transparent background
**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-react-shocked.png`
**Post-processing:** same as previous.

**Prompt:**

> Use the attached reference image as the character reference. Match the
> character's facial features, hair, beard, cap, glasses, wardrobe, and
> illustrated visual register EXACTLY.
>
> COMPOSITION: Bust framing (upper chest up). Head centered, direct gaze
> toward camera.
>
> CRITICAL EXPRESSION DIRECTIVE: Open mouth (lips parted, mouth shaped in a
> small "o" — not a wide gape, not laughing). Both eyebrows raised high,
> creating visible forehead lines. Eyes wide open. The expression should
> read as genuine incredulity — "they did WHAT". Do NOT soften toward
> 'surprised' or 'pleasantly startled' — this is alarmed incredulity,
> not delight. Do NOT add a smile — shock is the only expression.
>
> STYLE: Match the reference image's visual register and stylization exactly.
> Do NOT shift to flat-vector, do NOT shift to photoreal, do NOT shift to
> explainer-cartoon.
>
> WARDROBE: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red
> DICKIES brand patch (preserve this patch exactly — NO Supreme or other
> brand substitutions), olive-grey t-shirt, dark jeans.
>
> BACKGROUND: fully transparent.
>
> ASPECT: 1:1, 1024×1024.
>
> EXCLUDE: text, words, captions, watermarks; secondary figures; background
> scenery.
```

- [ ] **Step 2: Write the complete file in one `Write` call**

The full file content is the literal concatenation, in this exact order:

1. The file frame (markdown above starting with `# Justoon slideshow library — generation prompts`)
2. Block 1 (anchor — `## 1 — justoon-neutral.png`)
3. Blocks 2-5 (pointing poses, role A) — copy them verbatim from the "Pointing poses (role A) — blocks 2-5" code block above
4. Blocks 6-10 (reactions, role C) — copy them verbatim from the "Reactions (role C) — blocks 6-10" code block above

Each block is separated by the `---` markdown horizontal rule already shown at the end of each block above.

Issue ONE `Write` tool call with `file_path: ~/Pictures/tcn-justin-slideshow/_generation-prompts.md` and the concatenated content as `content`. The `Write` tool overwrites; appending across multiple calls is not the right pattern here because the file does not exist yet and we want it created atomically.

- [ ] **Step 3: Verify file structure**

Run:
```bash
ls -la ~/Pictures/tcn-justin-slideshow/_generation-prompts.md && wc -l ~/Pictures/tcn-justin-slideshow/_generation-prompts.md
```

Expected: file exists, ~400-500 lines.

- [ ] **Step 4: Verify all 10 blocks are present**

Run:
```bash
grep -E "^## [0-9]+ — justoon-" ~/Pictures/tcn-justin-slideshow/_generation-prompts.md
```

Expected output (10 lines, exact):
```
## 1 — justoon-neutral.png (anchor / fallback)
## 2 — justoon-point-right.png (role A)
## 3 — justoon-point-up.png (role A)
## 4 — justoon-point-down.png (role A)
## 5 — justoon-point-open-palm.png (role A)
## 6 — justoon-react-deadpan.png (role C)
## 7 — justoon-react-raised-eyebrow.png (role C)
## 8 — justoon-react-concerned.png (role C)
## 9 — justoon-react-smirk.png (role C)
## 10 — justoon-react-shocked.png (role C)
```

If any line is missing, re-run Step 2 with the missing block(s).

- [ ] **Step 5: Verify every block has the wardrobe-preservation language**

Run:
```bash
grep -c "DICKIES brand patch" ~/Pictures/tcn-justin-slideshow/_generation-prompts.md
```

Expected: `10` (one per block). If any number other than 10, a block is missing the wardrobe-preservation language — re-write that block.

- [ ] **Step 6: Verify every block has the style anchor**

Run:
```bash
grep -c "Do NOT shift to flat-vector" ~/Pictures/tcn-justin-slideshow/_generation-prompts.md
```

Expected: `10` (one per block).

- [ ] **Step 7: Verify role C blocks have CRITICAL EXPRESSION DIRECTIVE language**

Run:
```bash
grep -c "CRITICAL EXPRESSION DIRECTIVE" ~/Pictures/tcn-justin-slideshow/_generation-prompts.md
```

Expected: `5` (one per role C reaction block — blocks 6, 7, 8, 9, 10). Role A blocks and the anchor use composition directives, not the forbid-the-default critical-expression language.

- [ ] **Step 8: Verify reference image attachments**

Run:
```bash
grep -E "Reference image to attach" ~/Pictures/tcn-justin-slideshow/_generation-prompts.md | sort | uniq -c
```

Expected:
- 4 lines pointing to `~/Pictures/justoon-standing.svg` (blocks 2, 3, 4, 5 — pointing poses)
- 6 lines pointing to `~/Pictures/justoon-neutral.svg` (block 1 anchor + blocks 6-10 reactions)

If counts are wrong, a block is attaching the wrong reference.

- [ ] **Step 9: No commit**

Same as previous tasks — `~/Pictures/` is not a git repo.

---

## Task 4: Commit the plan file to the project repo

**Files:**
- Already created earlier: `docs/superpowers/plans/2026-05-25-justoon-slideshow-library.md` (this plan file)

- [ ] **Step 1: Stage the plan file**

Run from the project repo root (`/Users/justin/Documents/substack-research/Substack Research`):
```bash
git add docs/superpowers/plans/2026-05-25-justoon-slideshow-library.md
git status --short
```

Expected: shows `A  docs/superpowers/plans/2026-05-25-justoon-slideshow-library.md` and nothing else newly staged.

- [ ] **Step 2: Commit**

Run:
```bash
git commit -m "$(cat <<'EOF'
plan: Justoon slideshow library implementation (2026-05-25)

Executable plan derived from the design spec at
docs/superpowers/specs/2026-05-25-justoon-slideshow-library-design.md
(commit 77675df). Three tasks: create ~/Pictures/tcn-justin-slideshow/,
write the library CLAUDE.md, write the 10-block prompt batch file
(_generation-prompts.md) with inherited anti-drift discipline.

Out of scope (deferred to a follow-up plan): tcn-youtube-slideshow
skill integration, dispatch-005 end-to-end test render. Justin's
manual Freepik/Magnific generation step is not automated by this plan.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
EOF
)"
```

- [ ] **Step 3: Verify**

Run:
```bash
git log --oneline -3
```

Expected: latest commit is the plan commit.

---

## What ships after this plan executes

On disk:
- `~/Pictures/tcn-justin-slideshow/` (directory)
- `~/Pictures/tcn-justin-slideshow/CLAUDE.md` (library convention)
- `~/Pictures/tcn-justin-slideshow/_generation-prompts.md` (10 paste-ready prompts)

In the project repo:
- `docs/superpowers/plans/2026-05-25-justoon-slideshow-library.md` (this plan, committed)

What does NOT ship:
- Any PNG files. Generation is Justin's manual step in Freepik/Magnific after the plan executes.
- Any `tcn-youtube-slideshow` skill changes. That's a separate follow-up plan once the PNGs exist.

## Next step after this plan executes

Justin works through `~/Pictures/tcn-justin-slideshow/_generation-prompts.md` in Freepik/Magnific. After enough variants exist to test integration (likely all 10, but the anchor + 1 pointing + 1 reaction would be enough for a minimal test), spawn the follow-up brainstorm/spec/plan cycle for the `tcn-youtube-slideshow` skill update.
