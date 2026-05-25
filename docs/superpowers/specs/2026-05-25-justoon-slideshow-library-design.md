---
title: "Justoon Slideshow Library — Design"
type: design-spec
status: approved
created: 2026-05-25
authors: ["Justin Hearn", "Claude"]
implementation_path: writing-plans
related_artifacts:
  - ~/Pictures/justoon-neutral.svg
  - ~/Pictures/justoon-standing.svg
  - ~/Pictures/tcn-justin-references/ (existing editorial-illustration PNG library, consumed by tcn-youtube-thumbnail)
  - ~/.claude/skills/tcn-youtube-slideshow/SKILL.md
  - ~/.claude/skills/tcn-youtube-thumbnail/references/reference-image-prompt-template.md
---

# Justoon Slideshow Library — Design

## Problem statement

The TCN YouTube production pipeline currently has no way to put illustrated-Justin ("Justoon") on slideshow slides. The `tcn-youtube-slideshow` skill produces a Claude Design prompt that renders pure-typography slides under strict brand rules (Courier Prime only; slate-400 / slate-600 / black / twilight palette; no shadows on dark). The downstream video has Justin's narration but no on-screen face — viewers see static text decks for the full 5-7 minute runtime. The narration-without-face format limits viewer connection on the format that's supposed to be a trailer for the Substack article.

Recording Justin's actual face per dispatch is the obvious alternative, but it adds video production overhead (lighting, framing, B-roll cuts) Justin has explicitly opted out of. The brief is: keep the narration-driven trailer format, but give the slides a Justoon presence that substitutes for the recorded face.

A parallel asset library already exists for thumbnails — `~/Pictures/tcn-justin-references/` holds ~30 editorial-illustration PNGs in the Brian Stauffer / Yann Legendre register, with locked wardrobe (plaid bucket cap, red DICKIES patch, olive-grey t-shirt, dark jeans, blue square-frame glasses, salt-and-pepper brown beard). That library is consumed by `tcn-youtube-thumbnail` and works there because YouTube thumbnails are CTR-first and the editorial register competes for attention. The same register on a slideshow slide competes with — and loses to — the brand-restricted typographic minimalism the slideshow is built around.

So the slideshow needs its own Justoon library. The two SVG files Justin shared (`justoon-neutral.svg`, `justoon-standing.svg`) are the seed — they define the visual register for this library, distinct from but identifiable as the same character as the thumbnail library.

## Goals

- Establish a slideshow-specific Justoon library at a stable named location, parallel in shape to the existing thumbnail library.
- Produce a prompt batch file Justin can work through manually in Freepik/Magnific to populate the library.
- Define the slideshow skill's integration touchpoints so the populated library can be wired in as a follow-up task without re-deciding architecture.
- Keep the editorial-illustration thumbnail library and the slideshow library cleanly separated — different registers, different consumers, no accidental cross-use.

## Non-goals (this spec)

- LoRA training. Justin explicitly opted out for this iteration. Generation is manual reference-image-mode via Freepik/Magnific.
- Building the slideshow skill update (consumption logic, per-slide auto-pick, Claude Design prompt directive). That's a follow-up implementation task after the library is populated.
- Vectorization of generated PNGs to SVG. Cosmetic; revisit only if needed.
- Role-B "corner reaction companion" integration. Justin selected role A + C only.
- Backfilling Justoon onto previously-shipped dispatches. Forward-only.
- Updating the `tcn-youtube-thumbnail` skill or its library. Out of scope.

## Scope

In scope:
- Library naming convention, location, file format
- Generation method (prompt batch file consumed manually in Freepik/Magnific)
- Slide-type integration roles (A = pointing teacher, C = reaction-as-anchor)
- The initial 10-variant batch composition
- Slideshow skill integration architecture (touchpoints only — implementation deferred)
- `CLAUDE.md` for the new library directory

Out of scope (will be its own work):
- The actual slideshow skill code changes
- End-to-end dispatch-005 test render

## The two roles (locked)

Justin chose a hybrid integration after seeing three mockups (role A pointing-teacher, role B reaction-companion-corner, role C reaction-as-anchor). The library serves two of the three:

**Role A — Pointing teacher.** Justoon left, points across at the stat. Hero anchor is the number; Justoon contextualizes — "look at this." Best on Receipt and Stakes slides where the rhetorical move is a stat reveal. Needs directional pointing poses: right, up, down, open-palm-presenting.

**Role C — Reaction-as-anchor.** Justoon is the slide's hero anchor. Stat becomes secondary caption. Best on Twist and emotional-climax slides where the reaction *is* the rhetorical move (the canonical example: dispatch-005 Slide 8's "By whom, the company says, can't be known" deadpan close). Needs the strongest expression range: deadpan, raised-eyebrow, concerned, smirk, shocked.

**Role B — Corner reaction companion.** Not in this scope. Defer to a later iteration if the role A + C pattern surfaces a gap.

## Architecture

Three artifacts, three purposes:

| File / directory | Role | Updated by |
|---|---|---|
| `~/Pictures/tcn-justin-slideshow/` | The slideshow-specific Justoon library. Holds the 10 initial variants + any later additions. | Manual additions via Freepik/Magnific renders of the prompt batch file. |
| `~/Pictures/tcn-justin-slideshow/_generation-prompts.md` | The prompt batch file. One prompt block per intended variant. Re-runnable: any variant can be regenerated by re-pasting its block. Versioned in case of style retunes. | Manual edits only when the prompt language needs adjustment after seeing rendered results. |
| `~/Pictures/tcn-justin-slideshow/CLAUDE.md` | Library convention doc. Parallel to the one Justin maintains in the thumbnail refs directory. Documents naming, format, role mapping, regeneration workflow. | Manual edits as the library evolves. |

Why this split mirrors the thumbnail library: the thumbnail library lives at `~/Pictures/tcn-justin-references/` and is consumed by `tcn-youtube-thumbnail` via the named-by-purpose lookup pattern. The slideshow library should look identical in structure so future skill work has only one mental model. The two libraries differ in register (editorial-illustration vs. SVG-vector), not in interface.

## The 10-variant initial batch

| # | Filename | Role | What it does |
|---|----------|------|--------------|
| 1 | `justoon-neutral.png` | Anchor / fallback | Re-render of `justoon-neutral.svg` at 1024×1024 PNG with transparent background. Required file. The fallback target for any missing variant. |
| 2 | `justoon-point-right.png` | A | Full-body, points across to upper-right. Stat lives in right negative space. |
| 3 | `justoon-point-up.png` | A | Full-body, points up. Headline lives above the pointing finger. |
| 4 | `justoon-point-down.png` | A | Full-body, points down-right. Stat below. |
| 5 | `justoon-point-open-palm.png` | A | Softer "presenting" gesture instead of directional point. |
| 6 | `justoon-react-deadpan.png` | C | Bust, flat stare. The dispatch-005 Slide 8 "by whom, the company says, can't be known" close. |
| 7 | `justoon-react-raised-eyebrow.png` | C | Bust, one eyebrow up. "Really?" register. |
| 8 | `justoon-react-concerned.png` | C | Bust, furrowed brow. Alarm-bell slides. |
| 9 | `justoon-react-smirk.png` | C | Bust, dry TCN signature smirk. |
| 10 | `justoon-react-shocked.png` | C | Bust, open mouth + raised brows. "They did WHAT" moments. |

Composition: 4 pointing poses, 5 reactions, 1 neutral anchor. Justin can drop any block before generation, add new blocks later by appending to the same prompt file.

## Prompt block structure

Each block in `_generation-prompts.md` follows this structure (so blocks are uniform and re-runnable):

```markdown
## [N] — justoon-{slug}.png

**Reference image to attach:** `~/Pictures/justoon-{neutral|standing}.svg`
**Output spec:** 1024×1024, transparent background
**Post-processing:** [e.g., "if Magnific renders a background, run through remove.bg before saving"]

**Prompt:**

> [Full prompt text — character consistency directive + style anchor + composition directive + expression / pose directive + wardrobe preservation]

**Save as:** `~/Pictures/tcn-justin-slideshow/justoon-{slug}.png`
```

The prompt text in every block includes:
- **Character consistency directive** — "use attached reference; match facial features, wardrobe, illustrated style exactly"
- **Style anchor** — names the vector-illustration register, anchors against drift (mirrors the `NOT flat vector / NOT photoreal / NOT explainer-cartoon` discipline from `tcn-youtube-thumbnail`'s reference-image-prompt-template, adapted to the SVG-vector register)
- **Composition directive** — framing (full-body for role A, bust for role C), pose specifics (pointing direction, eyes following finger, eyebrows / mouth state)
- **Expression-preservation language** — for role C, the explicit "do not soften toward neutral friendly" forbid pattern proven in the thumbnail skill's dispatch-004 test
- **Wardrobe preservation** — plaid bucket cap with DICKIES patch (preserve exactly — NO Supreme substitutions), olive-grey t-shirt, dark jeans, glasses, beard

This language is the same proven-against-drift discipline `tcn-youtube-thumbnail`'s `reference-image-prompt-template.md` documents — the slideshow library inherits it rather than re-deriving it.

## Slideshow skill integration (architecture only)

Implementation deferred. Architecture locked here so the follow-up task has no decisions left.

**New optional input on `tcn-youtube-slideshow`:**
- `--justoon-refs <path>` — defaults to `~/Pictures/tcn-justin-slideshow/`. Absence triggers "no Justoon" mode; the skill produces today's pure-typography output unchanged.

**New per-slide auto-pick logic** in the slide-type mapping table:

| Slide type | Justoon role | Variant pick logic |
|---|---|---|
| Hook (Slide 1) | none | Typography only. |
| Thesis (Slide 2) | none | Typography only. |
| Receipt | A | Default `justoon-point-right.png`; `-up` if hero number sits above the pointing zone; `-down` if below. |
| Stakes | A | Same as Receipt. |
| Frame | none | Frame slides carry framing-line typography; Justoon would compete. |
| Anaphora | none | Anaphora pairs are the rhetorical move; Justoon would dilute. |
| Twist | C | Variant matched to emotional charge: `deadpan` for dry close, `raised-eyebrow` for "really?", `concerned` for alarm, `shocked` for "they did WHAT". |
| Historical Echo | none | Defer; not yet load-bearing in observed dispatches. |
| Verbatim | none | Quote carries the slide. |
| Tease (Slide N-1) | none | Curiosity-gap typography; Justoon would compete. |
| End (Slide N) | none | Standard close, brand-pure. |

**Per-slide directive added to the Claude Design prompt** (when Justoon is in play):

```
Justoon role: A | C
Justoon variant: justoon-{slug}.png
Justoon placement: [LEFT 25-30% / RIGHT 35-45% / centered] of safe-zone
Justoon sizing: [proportion of safe-zone height]
Mobile safe-zone: Justoon fits inside; brand mark + hairline rules extend to viewport edges as before.
```

For the bill-of-rights dispatch-005 (11 slides), this means Justoon shows on **Slides 3, 4, 8** and possibly 9 — the other 7-8 slides stay typography-only. That ratio (Justoon on ~30% of slides) is a sanity check that the role A + C pattern doesn't overload the deck.

**Failure modes** (the follow-up implementation needs to handle):
- `--justoon-refs` path provided but directory missing → halt with setup note
- `justoon-neutral.png` (the anchor / fallback) missing inside the directory → halt with setup note
- Slide-type's auto-picked variant missing → fall back to `justoon-neutral.png`, note substitution in the prompt artifact header
- No `--justoon-refs` flag and no config file → no-Justoon mode silently (today's behavior unchanged)

## Failure modes (this spec's deliverables)

- **Freepik/Magnific renders drift in style** across batches → the proven mitigation is always attaching the same anchor SVG as the character reference, and re-running any drifted variant against a freshly-uploaded reference. The prompt batch file is re-runnable per-block specifically for this case.
- **Generated variants have unwanted backgrounds** despite the "transparent background" directive → each prompt block names `remove.bg` (or equivalent) as the post-processing fallback. Magnific's transparent-output support varies by mode.
- **Character drift on facial features** (the model softens an expression back to neutral) → forbid-the-default language in each role-C block, inherited from the thumbnail skill's dispatch-004 lessons.
- **Wardrobe drift** (model substitutes a different cap brand patch) → wardrobe preservation language in every block, with the explicit "preserve DICKIES patch exactly — NO Supreme or other brand substitutions" directive proven necessary in dispatch-004.

## Sequencing

1. **Today (this spec's deliverables):**
   - Write this design doc (this file)
   - Create the library directory `~/Pictures/tcn-justin-slideshow/`
   - Write `CLAUDE.md` inside the directory
   - Write `_generation-prompts.md` inside the directory with all 10 prompt blocks
2. **Justin's manual step** (after spec approval):
   - Work through the 10 prompts in Freepik/Magnific, saving each output as the named file
   - Inspect outputs; regenerate any blocks that drift; append additional blocks if the initial 10 surface gaps
3. **Follow-up implementation task** (writing-plans skill picks this up):
   - Update `tcn-youtube-slideshow` to consume the library per the integration architecture above
   - Render dispatch-005's slideshow with Justoon on Slides 3, 4, 8 (and possibly 9) as the end-to-end test
   - Iterate on per-slide placement / sizing based on the test render

## Open questions (defer, do not block)

- Whether to add role B (corner companion) after Justin has lived with role A + C for 2-3 dispatches.
- Whether to wire a `--render-mode` flag on `tcn-youtube-slideshow` for "include Justoon" vs. "typography-only" so individual dispatches can opt out without removing the refs path.
- Whether the slideshow skill should write a `Justoon picks` block into its output artifact (parallel to the cold-open / refrain blocks already in the narration's Script Notes) so downstream skills can read which Justoon variants the deck used.

None of these block the current deliverable.
