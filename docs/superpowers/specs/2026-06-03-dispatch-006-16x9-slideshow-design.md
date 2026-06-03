# Design Spec — Dispatch №006 16:9-Native Slideshow Prompt

- **Date:** 2026-06-03
- **Status:** Approved design, pre-implementation
- **Author:** Justin + Claude (brainstorming session)
- **Implements:** A second Claude Design prompt for Dispatch №006 ("Samsung's $400,000 Bonus, and the $4,000 One") that renders the deck **16:9-native** — filling a 1920×1080 widescreen frame for the primary YouTube upload — as a layout re-skin of the existing single-source prompt.

---

## 1. Problem & Context

The existing slideshow prompt (`workspace/drafts/samsungs-400000-bonus-and-the-4000-one/youtube-slideshow.md`, committed `f876cda`) is **single-source multi-aspect**: all content lives inside a *square* safe zone, `--safe-zone: min(85cqw, 85cqh)`. Recording at 16:9 centers that square in the 1920-wide frame, leaving **~420px of empty gutter on each side**. On a phone watching a square social card that's fine; as the primary widescreen YouTube upload it reads as sparse/pillarboxed, and the hero numbers ($400,000, 10.5%, $13.77 BILLION, +755%) are shrunk to fit the 1080-wide square rather than the full frame.

The `tcn-youtube-slideshow` skill has no 16:9-native mode — it is hard-wired to the square-safe, 1:1-primary design. So this variant is authored **outside** the skill, by adapting the committed prompt.

**The defining property:** the narration is locked (10 scenes, 102 beats, verbatim speaker notes), the brand guardrails are fixed, and the build-on-reveal motion model is fixed. The *only* thing that changes for 16:9-native is **layout** — the safe-zone geometry, the reserved-face placement, the type scale, and the output target. This is a re-skin, not a new deck.

---

## 2. Goals & Non-Goals

### Goals
- Produce a second prompt, `youtube-slideshow-16x9.md`, that yields a deck filling 1920×1080 with no centered-square pillarboxing.
- Let hero numbers grow to fill the wide content column (width is no longer the binding constraint).
- Keep the composited-face workflow (Justoon-OFF), placed in a reserved column that uses the widescreen frame.
- Reuse the locked beats, speaker notes, brand rules, and motion model verbatim — only the layout sections change.
- Make the reserved-face column a **reusable modifier class** so any slide can opt into a face in post without a re-layout (supports the "adjust if too static" iteration path).

### Non-Goals
- **Multi-aspect.** This deck is 16:9-only. The existing square-based prompt remains the source for the 1:1 / 9:16 social cuts. No multi-aspect language carries over.
- **Re-narration / re-beating.** Scenes, beats, and speaker notes are untouched.
- **Editing the `tcn-youtube-slideshow` skill.** The skill stays single-source; this is a hand-authored sibling artifact for this dispatch.
- **Recording / compositing the face.** The prompt reserves the space; post-production adds the face.

---

## 3. Decisions (resolved forks)

| # | Fork | Decision | Rationale |
|---|------|----------|-----------|
| D1 | Layout philosophy | **B — per-slide reservation, widened** (not A persistent rail, not C corner PiP) | Preserves the locked deck's instinct: the face earns its place on the evidence slides; the big rhetorical beats (Hook 100:1, refrains, NOT THE SAME MONEY, NOT YET.) go full-bleed and get the most screen. A shrinks every dramatic beat and needs a face animated for all 10 scenes. |
| D2 | Face presence | **Built to extend** | User wants a face on *almost* every slide, but "motion may carry it." Reserved-face is a reusable class applicable to any slide; build pure-B, add faces per-slide in post if a slide reads static. One-line change, not a re-layout. |
| D3 | Core mechanism | **Replace the square safe zone with a 16:9 content rectangle + named columns** | The square safe zone *is* the pillarboxing. A 16:9 rectangle with a face-rail column + content column is the whole fix; type then grows because horizontal space stops binding. |
| D4 | Face geometry | **Data slides: rail LEFT 30%, content right ~64%. Twist: face flips RIGHT 32%, text left ~60%.** | 30% of 1920 ≈ 576px — a present, full-height portrait region for a head-and-shoulders face. The Twist's right-flip is a deliberate rhetorical beat in the locked deck (deadpan correction); preserved. |
| D5 | Hero scaling | **Height-driven (`cqh`) with raised maxima; full-bleed beats scale until height-bound** | At 16:9, `cqmin == cqh`, so vertical rhythm is unchanged; raising the clamp maxima + freeing width lets long hero strings fill the column / frame. |
| D6 | Scope & coexistence | **Standalone 16:9-only deck; locked square deck stays for 1:1 / 9:16** | User accepted "two layouts" at the variant decision. Naming both decks explicitly prevents the recorder from confusing sources. |
| D7 | Authoring method | **Layout re-skin of the committed prompt** | ~80% of the prompt text (scenes, beats, speaker notes, brand, motion) is reused verbatim; only ~5 sections are swapped. Minimizes drift risk against the locked narration. |

---

## 4. Layout Architecture (the deltas from the locked prompt)

The new prompt keeps the locked prompt's structure and swaps these sections:

1. **Header block** — `Format` line unchanged; `Primary recording aspect` becomes **16:9 (1920×1080), no other aspects**; the reserved-face note re-states the 16:9 column fractions (D4).
2. **"Small-screen / multi-aspect requirements"** → **"16:9-native frame & safe zone."** Replace `--safe-zone: min(85cqw,85cqh)` with a 16:9 content rectangle:
   - `--safe-w: 92cqw; --safe-h: 88cqh;` (content fills the frame, small uniform margin).
   - `--rail: 30cqw;` (face column) and `--content: calc(92cqw - var(--rail) - gutter);`.
   - Type scale: keep `cqh`-driven clamps; raise hero maxima (`--type-hero: clamp(96px, 34cqh, 520px)` for full-bleed; column heroes a step smaller). Thumbnail floor + `text-wrap: balance` retained.
3. **Reserved face-space layout (CSS)** — re-expressed for the 16:9 frame:
   - `.has-face-left .content { left: var(--rail); width: var(--content); }` rail empty on the left.
   - `.slide-twist` mirrored: text left ~60%, rail right 32%.
   - Reusable: `.has-face-left` / `.has-face-right` are modifier classes any slide can take (D2). Default full-type slides use neither (full-bleed).
4. **Thumbnail-anchor & visible-text budget** — retained; "240px wide" thumbnail test stays (YouTube cards still shrink), evaluated against the 16:9 frame.
5. **Output requirements** — filename `dispatch-006-16x9.html`; "renders at 16:9, 9:16, 1:1" replaced by "renders at 16:9 (1920×1080); designed for that frame only." Slide IDs, speaker-notes JSON (10 entries), relative asset paths, no-CDN rules unchanged.

**Unchanged verbatim:** Context, Inputs, Brand requirements, Motion model, the entire Slide-by-slide specification (Scenes 01–10, all 102 beats), Speaker notes JSON, Pacing holds. Per-scene "reserve left ~32%" notes are updated to the 16:9 fractions but the beat content is identical.

---

## 5. Deliverable & Location

- **File:** `workspace/drafts/samsungs-400000-bonus-and-the-4000-one/youtube-slideshow-16x9.md`
- Sits beside the committed `youtube-slideshow.md` (the square/multi-aspect source).
- Produces `dispatch-006-16x9.html` when pasted into Claude Design.

---

## 6. Verification

Acceptance is a read-through against this spec (the artifact is a prompt, not runnable code here):
- Square safe-zone language is fully gone; 16:9 rectangle + named columns present.
- All 10 scenes / 102 beats and the 10 speaker-notes entries match the locked prompt verbatim.
- Face geometry matches D4; `.has-face-*` is a reusable class.
- Brand guardrails and motion model carried over unchanged.
- Output names `dispatch-006-16x9.html`; no multi-aspect claims remain.
