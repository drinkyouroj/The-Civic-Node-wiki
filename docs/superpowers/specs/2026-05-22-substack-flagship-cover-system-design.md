---
title: "Substack Flagship Cover System — Design"
type: design-spec
status: approved
created: 2026-05-22
authors: ["Justin Hearn", "Claude"]
implementation_path: skill-creator
related_artifacts:
  - workspace/core/_template-flagship-cover.md
  - workspace/paid/_template-thinking-behind-the-thinking-cover.md
---

# Substack Flagship Cover System — Design

## Problem statement

Across ~80 published flagship pieces, Substack covers have ranged from very strong ($71B Bluff with Altman + green DRAM cascade, Cheaper AI's steam-engine ↔ DDR5 isometric, System Functioning Correctly's face-of-documents, Atlanta's reflective ALPR camera) to genuinely weak (3,000 Arrests' cork-board collage, Process Is the Punishment's labeled castle blueprint, Cypherpunk S-1's split-frame, Defendant in Miami's forum-screenshot composite). The recent flagships (May 2026 — 12 Gigawatts, Helium) converged on a single archival-infographic aesthetic (YouMind template #4847) but that template sits closer to the user's least-favorites than favorites despite the craft involved. The paid-note series ("Thinking Behind the Thinking," 3 installments) has a fully locked typographic template that works. Flagship covers do not.

The inconsistency the user feels has two distinct sources:

1. **No documented system for flagships.** Each cover is prompted freehand against a different YouMind library template per piece, with no DNA enforcement.
2. **No saved-prompt discipline.** Six of nine rated covers have no preserved prompt file. Successful patterns can't be reverse-engineered or iterated on.

The cost: the system that produces $71B Bluff is the same system that produces Defendant in Miami. There is no audit, no DNA check, and no compounding intelligence between covers.

## Goals

- Lock the **DNA** that the user's favorite covers share, leaving execution variable per piece.
- Make the cover-prep step part of the article workflow (parallel to `tcn-youtube-thumbnail` in the YouTube chain).
- Require saved prompt files for every cover (closes the audit-trail gap).
- Preserve the editorial creative call ("which framing sharpens this piece?") as the user's decision, not the system's.

## Non-goals (this spec)

- Fiction-episode covers (DeepTruth, HDftS). Different DNA, thinner corpus, separate spec later.
- Substack Notes / social imagery. Out of scope.
- YouTube thumbnails. Already systematized via the `tcn-youtube-thumbnail` skill.
- Retroactive re-rendering of past covers. Forward-only.
- A skill that auto-generates the image (the skill produces the *prompt*; image generation stays in the user's existing Nano Banana Pro / Flux workflow).

## Scope

In scope: flagship nonfiction Substack covers — the cover image attached to the post in Substack's metadata, primary social card.

## The DNA — five locked principles

These derive from cross-checking what the user's favorite covers share and what their least-favorites share. They are documented in full with explanations in [`workspace/core/_template-flagship-cover.md`](../../../workspace/core/_template-flagship-cover.md). Summary:

1. **Metaphor compression, not evidence illustration.** The image carries the thesis through ONE relationship.
2. **≤2 primary visual elements.** Never three competing zones, never a labeled diagram.
3. **No embedded text in the image.** No labels, no annotations, no callouts. The post title does the verbal work.
4. **Cinematic OR technical illustration register.** Editorial poster, surreal symbolic, photo-with-reflection-device, clean isometric, or single-tableau narrative illustration. Never documentary scrapbook or encyclopedic infographic.
5. **High contrast as the carrying device.** B&W vs. saturated, cold vs. warm, present vs. absent. Contrast IS the argument.

## The variable axes — four execution choices

Documented in full in the template doc. Summary:

1. **Photographic vs. illustrated** — both work; chosen per piece.
2. **Palette** — no fixed palette; serves the contrast and the register.
3. **Light vs. dark mood** — varies with piece register.
4. **Person / object / scene** — subject type determined by the piece, with face-consideration gate (see below).

## Architecture

Two artifacts, two purposes:

| File | Role | Updated by |
|---|---|---|
| [`workspace/core/_template-flagship-cover.md`](../../../workspace/core/_template-flagship-cover.md) | Authoritative DNA reference + exemplar gallery. Single source of truth. Human-readable. | Manual edits only; revisions dated and numbered. |
| `/Users/justin/CascadeProjects/claude-skills/tcn-flagship-cover/` | Workflow logic. Loads template on invocation, applies DNA to a finished article, runs concept-generation loop, writes output file. | Skill-creator agent (built once, refined as patterns surface). |

Why this split: the skill should never duplicate the DNA principles inline in its description, because that creates two copies that can drift. The skill loads the template doc on every invocation, so updates to the DNA propagate automatically.

## Workflow

The skill executes nine steps when invoked:

| Step | Action |
|---|---|
| 1 | Locate the finished article draft (e.g., `workspace/drafts/{slug}/{N}-final.md`). Disambiguate if multiple candidates exist. |
| 2 | Read the article in full; load [`workspace/core/_template-flagship-cover.md`](../../../workspace/core/_template-flagship-cover.md) for DNA principles + exemplars. |
| 3 | **Identify the core compression** — reason out loud about what visual relationship would carry this piece's thesis. This is the analytical step that turns prose argument into visual metaphor. |
| 4 | **Face-consideration gate** — if the piece has an identifiable individual, ask the user yes/no with reasoning. The skill should also volunteer when a face would weaken the cover even on pieces with named protagonists. |
| 5 | **Propose 2–3 concept briefs.** Each follows the concept brief format (compression name, subject, secondary element, relationship, visual register, palette direction, DNA checks, one-line evocation). Each must propose a *meaningfully different compression* — not three variants of one composition. If only 2 strong compressions exist, propose 2; do not pad. |
| 6 | User picks one concept (or asks for revisions). Standard pause-for-approval. |
| 7 | **Generate the full model-ready prompt via `ai-image-prompts-skill` (preferred path).** Invoke the library-lookup skill via the Skill tool, passing the locked concept brief (compression name, subject, secondary element, visual register, palette direction). The library returns a matching prompt template — e.g., neo-noir editorial portrait for a face-forward photographic concept, clean isometric for a two-icon comparison, surreal symbolic for an institutional metaphor. Map the concept-specific elements into the returned template's variables, enforce DNA negative prompts (no embedded text, no labels, no documentary-scrapbook elements) *regardless of what the library template contains*, and add the standard 16:9 1456 × 816 aspect ratio + model directives. Produce alt text and a one-line caption. **Fallback path** if `ai-image-prompts-skill` is unavailable: build from scratch following the structure of `workspace/drafts/the-71-billion-bluff-cover-prompt.md`. Record which path was taken in the output frontmatter (`prompt_source: ai-image-prompts-skill | scratch`). |
| 8 | **Save the prompt file** to `workspace/drafts/{slug}/cover-prompt.md` (or `cover-prompt-v1.md` if iteration is anticipated). Frontmatter captures: article reference, model, aspect ratio, compression name, register, palette, the 5 DNA checks as booleans, face decision + subject + reasoning, created date. Body has the prompt, alt text, caption, remix notes. |
| 9 | **(Optional, v1.5) Render-audit + v2 flow** — after image generation, user pastes the rendered image (or its alt text); skill audits against DNA and article facts, flags failures, proposes corrections, writes v2 file with explicit changelog (mirrors the Helium v1→v2 audit-trail pattern). |

Outputs are non-optional. No `cover-prompt.md` saved = the skill considers the cover unfinished.

## Concept brief format

Locked by the template doc. Each concept option is structured:

```
Compression name:      [the metaphor strategy in 3-5 words]
Subject:               [primary visual element]
Secondary element:     [the thing the subject relates to]
The relationship:      [one sentence — what carries the thesis]
Visual register:       [photographic / illustrated / isometric / surreal symbolic / etc.]
Palette direction:     [palette choice and why]
DNA checks:            [5/5 — confirmed inline]
One-line evocation:    [the cover described in the voice you'd describe it to a reader]
```

Three concepts ≠ three variants of one image. Three concepts = three *different compressions* (the piece could be argued as "cost," as "absence," as "process," etc.). Picking among them is an editorial framing decision, not a palette decision.

## Face consideration

When the article has an identifiable individual at its center, the skill prompts:

> *"This piece is centered on [name]. Should the cover build around their face? If yes — what makes [name]'s face strengthen this piece's argument? If no — what's the reason (not visually distinctive enough? structural piece where the face would be misleading? legal hesitation?)."*

The skill should also volunteer when a face would be wrong (e.g., the Helium piece has named co-authors but the argument is structural concentration — face-forward would mislead).

Decision and reasoning captured in `face_decision` / `face_subject` / `face_reasoning` frontmatter fields. Over time this builds an audit trail of when faces help vs. hurt.

Legal contour documented in the template doc: editorial use of public officials and senior public-company executives is well-protected; less-public figures benefit from non-face concepts by default; not legal advice.

## Output file convention

```
workspace/drafts/{slug}/cover-prompt.md
```

(Or `cover-prompt-v1.md` / `cover-prompt-v2.md` if iteration discipline is in use, mirroring the Helium pattern.)

Frontmatter spec is documented in the template doc; this spec doesn't duplicate.

## Integration with existing infrastructure

| Existing | Relationship |
|---|---|
| `tcn-article-builder` orchestrator | The cover skill is invoked manually after the article-builder chain finishes. It is NOT automatically chained — covers benefit from a separate decision moment, often after the writer has slept on the finished draft. |
| `tcn-youtube-thumbnail` skill | Sibling skill. Same architectural pattern (loads a template, applies DNA, proposes options, writes a prompt file). Different DNA — YouTube uses illustrated-Justin + text overlay; flagship covers use the compression DNA. |
| `tcn-substack-notes` skill | Independent. Substack Notes use different images (or no image); not a cover decision. |
| `ai-image-prompts-skill` (anthropic-skills) | **Used dependency for Step 7 (preferred path).** After the concept brief is locked, the cover skill invokes `ai-image-prompts-skill` via the Skill tool to recommend a prompt template matching the concept's register and compression. The cover skill then maps concept-specific elements into the returned template, enforces DNA negative prompts (which the library template may not include), and adds aspect-ratio/model directives. The cover skill remains the orchestrator and DNA enforcer; `ai-image-prompts-skill` provides the prompt-structure scaffolding. Rationale: the user's existing successful prompts (`$71B Bluff` #8791, paid notes #13068, Helium #4847) were already library lookups done by hand — this formalizes the existing workflow. Fallback to building from scratch if the library skill is unavailable. |
| `nano-banana-pro-prompts-recommend-skill` | Same role as `ai-image-prompts-skill`, model-specific. The cover skill should treat them as interchangeable library backends — whichever is available, use it. If both are available, prefer `ai-image-prompts-skill` (broader library, model-agnostic). |

## What's deliberately not built

- **Image generation.** The skill produces the prompt. The user runs the prompt through their existing Nano Banana Pro / Flux / Midjourney workflow.
- **Cross-piece consistency enforcement.** No system tries to make covers match each other. The DNA is the consistency mechanism; mechanical matching would defeat the variable-axes design.
- **Format-aware variants** (Twitter card vs. Substack card vs. RSS thumb). All Substack flagship covers are 16:9 1456 × 816. One aspect ratio, one render.

## Build order

The skill loads the template doc on first invocation. The template doc must exist first.

1. ✅ [`workspace/core/_template-flagship-cover.md`](../../../workspace/core/_template-flagship-cover.md) — committed in this brainstorming session.
2. ⏳ Build the skill via skill-creator using the prompt in the next section. The skill description must be accurate enough to trigger on phrases like "make the cover," "design the cover," "build the cover," "Substack cover for [piece]," "cover prompt for [piece]" — not on YouTube-thumbnail or paid-note-cover requests.
3. ⏳ First-use validation: invoke on a fresh piece and audit the output against the DNA. Iterate the skill body if outputs systematically miss a principle.

## Skill-creator-ready prompt (paste this into a skill-creator session)

The prompt below is intended for the `anthropic-skills:skill-creator` (or `skill-creator:skill-creator`) agent. It encodes the design above as a build brief.

```
Create a skill called tcn-flagship-cover.

Purpose: Generate a Substack flagship-cover image prompt for a finished Civic Node nonfiction article, following the locked DNA documented in workspace/core/_template-flagship-cover.md. The skill produces a saved prompt file ready for the user to run through Nano Banana Pro / Flux / Midjourney. It does NOT generate the image itself.

Skill location: /Users/justin/CascadeProjects/claude-skills/tcn-flagship-cover/

Skill description (for the SKILL.md frontmatter — must trigger reliably without false positives):

"Generate the Substack flagship cover image prompt for a Civic Node nonfiction article. Loads the locked DNA from workspace/core/_template-flagship-cover.md and produces 2-3 concept briefs, then a complete model-ready prompt saved to workspace/drafts/{slug}/cover-prompt.md. Use this skill when Justin says 'make the cover', 'design the cover', 'build the cover', 'cover prompt for [piece]', 'Substack cover for [piece]', 'cover image for this article', or any variant that asks for a flagship Substack cover image prompt. Does NOT apply to: YouTube thumbnails (use tcn-youtube-thumbnail), paid-note covers (use the locked template at workspace/paid/_template-thinking-behind-the-thinking-cover.md — different system), Substack Notes images (use tcn-substack-notes), fiction episode covers (separate system, not yet built), or image generation itself (this skill writes the prompt; the user runs it through Nano Banana Pro / Flux / Midjourney)."

Behavior:

The skill executes 8 steps (with optional v1.5 step 9 documented but not required for first version):

1. LOCATE THE ARTICLE. Identify the finished draft. Look for the highest-numbered or "*-final.md" file in workspace/drafts/{slug}/. If ambiguous, ask the user which file.

2. LOAD CONTEXT. Read the article in full. Load workspace/core/_template-flagship-cover.md for DNA principles, variable axes, exemplar gallery, concept brief format, output file frontmatter spec, and legal note.

3. IDENTIFY THE CORE COMPRESSION. Reason out loud (visible to the user) about what visual relationship would carry this piece's thesis in one image. This is the analytical step. Reference the article's actual argument, not the topic.

4. FACE-CONSIDERATION GATE. If the piece has an identifiable individual at its center, ask the user yes/no with this prompt:
   "This piece is centered on [name]. Should the cover build around their face? If yes — what makes [name]'s face strengthen this piece's argument? If no — what's the reason (not visually distinctive enough? structural piece where the face would be misleading? legal hesitation?)."
   IMPORTANT: When a piece has named individuals but the argument is structural/systemic (not personality-driven), the skill should proactively flag that face-forward would weaken the cover and recommend non-face concepts. Use the Helium piece as a worked example of this inversion (named co-authors, but argument is about governance concentration, so face-forward would mislead).

5. PROPOSE 2-3 CONCEPT BRIEFS. Each follows the concept brief format documented in the template doc. Each must propose a meaningfully different COMPRESSION — not three variants of one composition. If only 2 strong compressions exist, propose 2. Hard constraint: NEVER pad with a weak third option. Each concept must pass all 5 DNA checks inline.

6. USER PICKS ONE. Standard pause-for-approval. If the user asks for revisions, regenerate the picked concept or replace one of the unpicked concepts.

7. GENERATE THE FULL MODEL-READY PROMPT.

   PREFERRED PATH — use ai-image-prompts-skill: invoke the `ai-image-prompts-skill` (or `anthropic-skills:ai-image-prompts-skill`, or `nano-banana-pro-prompts-recommend-skill` — whichever is available) via the Skill tool. Pass the locked concept brief (compression name, subject, secondary element, visual register, palette direction). The library will recommend a matching prompt template (e.g., neo-noir editorial portrait for a face-forward photographic concept; clean isometric for a two-icon comparison; surreal symbolic for an institutional metaphor). Map the concept-specific elements into the returned template's variables.

   Whether using the library template or building from scratch, ALWAYS enforce the DNA negative-prompt requirements (which the library template likely will NOT include): "no embedded text in the image" / "no annotation labels" / "no chart titles" / "no documentary scrapbook elements" / "no labeled blueprints" / "no UPC or magazine furniture." Add the standard 16:9 1456 × 816 aspect ratio and any model-specific directives. Produce alt text and a one-line caption.

   FALLBACK PATH — if no library-recommender skill is available: build the prompt from scratch following the structure of `workspace/drafts/the-71-billion-bluff-cover-prompt.md` as the cleanest reference. Include the same elements: composition description, typography (if any), palette specification, lighting, style references, negative prompts, aspect ratio, model directives, alt text, caption.

   Rationale for preferring the library path: the user's existing successful prompts ($71B Bluff #8791, paid notes #13068, Helium #4847) were already library lookups done by hand. This formalizes that workflow rather than freehanding prompts.

   Record which path was taken in the output file frontmatter:
   prompt_source: ai-image-prompts-skill | nano-banana-pro-prompts-recommend-skill | scratch

8. SAVE THE PROMPT FILE to workspace/drafts/{slug}/cover-prompt.md. If the user signals iteration is anticipated, use cover-prompt-v1.md. Frontmatter MUST include all fields documented in the template doc's "Output file convention" section, including: article path, model, aspect_ratio, based_on, compression, register, palette, dna_checks (5 booleans), face_decision + face_subject + face_reasoning, created date.

NEVER:
- Skip step 8. No saved file = cover is not finished.
- Generate the image itself (this is a prompt-writing skill, not an image-generation skill).
- Propose 3 concepts when only 2 strong compressions exist.
- Embed text/labels/annotations in the cover image (except real-world physical signage that IS the metaphor, per the Atlanta exemplar).
- Override the user's face decision — the skill flags considerations, the user decides.
- Use the YouMind #4847 archival-infographic template or any documentary-scrapbook register — these are explicitly excluded by Principle 4.

The DNA principles and exemplar gallery live in workspace/core/_template-flagship-cover.md. The skill body should reference that file rather than duplicating its content, so DNA updates propagate without skill edits.

Worked example to include in the skill's reference materials (showing the system correcting a known failure):

The Process Is the Punishment (published April 2026) currently has a cover that fails DNA — a labeled castle blueprint cross-section with three competing zones (castle + courthouse + calendar) and embedded labels ("moats / curtain / supply lines / provisions"). Article thesis: "the lawsuit is the punishment; the trial is the least important thing." The skill should have proposed three compressions instead:

  Concept 1 — Wallet bleeding time: Photographed worn leather wallet on a dark table, a clock face reflected in its metal clasp with months crossed off as hour marks. B&W with one warm-amber color spill from the clock. Compression: time IS the cost.

  Concept 2 — Two chairs, one absent: B&W photograph of an empty courtroom, two chairs at the plaintiff/defendant tables, one occupied (silhouette), one empty with visible dust. Compression: the defense is being run from the empty chair.

  Concept 3 — Hourglass paper-flow: Clean isometric of an hourglass on white, papers streaming through the narrow center but never reaching the bottom verdict mark, industrial charcoal/steel blue palette. Compression: the trial is below the flow, out of frame.

All three pass the DNA. All three argue the piece differently. The skill's job is to surface that editorial range, not to deliver one "correct" answer.

Test cases for skill triggering (should fire):
- "Make the cover for the AI's Power Bill piece"
- "Design the Substack cover for tomorrow's article"
- "Cover prompt for the Helium piece"
- "Build the cover for [slug]"
- "I need a cover image for this article"

Test cases for skill NOT triggering:
- "Make the YouTube thumbnail" (use tcn-youtube-thumbnail)
- "Cover for the paid note" (use the locked paid-note template manually — not via skill)
- "Generate the cover image" (this skill writes the prompt; user generates)
- "Cover prompt for the DeepTruth episode" (fiction system not yet built; skill should explain and decline)
```

End of skill-creator-ready prompt.

## Open questions for the next phase

- Whether step 9 (render audit + v2 flow) ships in v1 of the skill or v1.5. Recommended: ship as v1.5 once the v1 flow is validated on 3–4 real pieces. The audit logic is non-trivial and benefits from real-world calibration.
- Whether the skill should ever auto-fire from `tcn-article-builder` at the publish-readiness step, or remain strictly user-invoked. Recommended: keep user-invoked. Cover prep benefits from being a separate decision moment, often after the writer has slept on the finished draft.
- Whether the exemplar gallery in the template doc should be expanded (currently 4 entries — $71B Bluff, Cheaper AI, System Functioning Correctly, Atlanta). Recommended: leave at 4 for now; add new exemplars only when a piece introduces a register the current gallery doesn't capture.

## Provenance

Designed 2026-05-22 in a brainstorming session that:
- Audited the existing cover landscape (paid notes locked; flagships converged but undocumented; earlier flagships drifted)
- Rated a corpus of 9 covers (5 favorites, 4 least-favorites)
- Cross-checked what favorites share vs. what least-favorites share, deriving the 5-principle DNA inductively rather than from external visual-system theory
- Validated the DNA against the user (4 design sections approved sequentially)
- Codified the operational system as a skill following the existing tcn-* skill convention

Implementation deferred to a skill-creator session per the user's preferred workflow.
