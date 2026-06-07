# Design: `tcn-youtube-shorts` skill

**Date:** 2026-06-06
**Status:** Approved — ready for implementation
**Author:** Justin Hearn (via brainstorming session)

---

## What This Skill Does

Packages a batch of finished 9:16 vertical clips (YouTube Shorts) cut from a TCN dispatch into per-clip title + description artifacts, one file per clip with a per-clip review gate. Reuses shared voice/pattern reference files from the existing `tcn-youtube-*` family without duplicating them.

Does NOT produce thumbnails (deferred to v2), narrations, slideshows, or long-form packaging. Not a retrofit of `tcn-youtube-description` — the format divergence (no chapters, different title math, `#Shorts` classifier, batch-of-N cardinality) justifies a sibling skill.

---

## Position in the Workflow

```
Article (tcn-article-builder)
    ↓
tcn-youtube-narration   [Step 1 — long-form]
tcn-youtube-slideshow   [Step 2 — long-form]
    ↓
┌─── RECORDING ───┐
    ↓
tcn-youtube-title       [Step 3 — long-form 16:9]
tcn-youtube-description [Step 4 — long-form 16:9]
tcn-youtube-thumbnail   [Step 5 — long-form 16:9]

tcn-youtube-shorts      [Parallel track — vertical clips cut from the same recording]
```

The Shorts skill is a parallel track, not a downstream step. It consumes the same master `.srt` transcript the long-form skills use, but produces per-clip artifacts independently.

---

## Inputs

### Required

- **Dispatch directory path** — e.g., `workspace/drafts/samsungs-400000-bonus-and-the-4000-one/`
  - The skill auto-detects the master `.srt` transcript here (any `.srt` file in the dir; if multiple, prefer the one without `1x1` in the name)
  - Halts with an explicit message and example path if no `.srt` found
- **Clip source** — either:
  - A directory path (e.g., `/Volumes/D10/`) where the skill finds `Dispatch NNN-clip-*.mp4` and `Dispatch NNN-<beat>-short-clip.mp4` files via glob
  - Or an explicit list of filenames

### Optional

- **Substack URL override** — bypasses auto-derivation from the dispatch dir slug
- **Steering** — free-text like `"punchier hooks"`, `"clip 03 needs a number in the title"`, `"skip clip 07"`

---

## Per-Clip Processing Pipeline

For each clip, in this order:

### 1. Canonical clip ordering

Sort clips by the numeric index in the filename slug:
- `Dispatch 006-100to1-ai-boom-short-clip.mp4` → clip 01 (no `clip-NN` prefix; any clip without a `clip-NN` prefix sorts before the numbered clips — treat as position 01 unless the user specifies otherwise)
- `Dispatch 006-clip-02-who-gets-to-say-no.mp4` → clip 02
- …
- `Dispatch 006-clip-09-not-the-same-money.mp4` → clip 09

If multiple clips lack a `clip-NN` prefix, surface a one-line warning and ask the user to confirm the intended order before proceeding.

### 2. Beat name extraction

Pull the beat identifier from the filename:
- `clip-03-755-percent` → beat key terms: `755`, `percent`
- `100to1-ai-boom-short-clip` → beat key terms: `100`, `1`, `ai`, `boom`
- Strip `Dispatch NNN-`, `clip-NN-`, `-short-clip`, `.mp4`

### 3. Transcript slicing

Fuzzy-match beat key terms against the `.srt` content to find the passage. Extract the spoken text for that segment.

**Match confidence check:**
- **High confidence:** key terms appear in a tight cluster of subtitle cues → use the sliced transcript
- **Low confidence:** terms scattered or absent → surface a one-line warning (`"weak transcript match for clip NN — falling back to article section"`) and fall back to the relevant article section
- Never silently produce copy from a weak match

### 4. Title drafting

- **Format:** declarative sentence, ≤60 chars total
- **Source:** sliced transcript (or article fallback)
- **Count:** 3 candidates per clip
- **Voice constraints:**
  - No chapters, no two-part-stop math (Shorts feed doesn't surface it)
  - Anti-AI-tells enforced via `workspace/core/anti-ai-writing-style.md`
  - Banned-word/banned-template check via `thumbnail-headline-patterns.md`
  - No em-dashes, no exclamation points, sentence case
- **Concrete anchor rule:** if the transcript slice contains a number, dollar amount, place name, or proper noun, at least one of the three candidates must use it

### 5. Description drafting

Assembled in this fixed order:

```
[HOOK]
1–2 punchy lines from the clip's core claim.
Different mechanism from the chosen title — not a restatement.

[BLANK LINE]

[ARTICLE CTA]
→ Full piece on Substack:
https://drinkyouroj.substack.com/p/<slug>

[BLANK LINE]

[HASHTAGS]
#Shorts #<dispatch-tag-1> #<dispatch-tag-2> [#<dispatch-tag-3>] #TheCivicNode #drinkYourOJ
```

**Hashtag rules:**
- `#Shorts` always first (YouTube classifier signal — non-negotiable)
- 2–4 dispatch-specific tags mined from the beat (proper-noun anchors preferred: companies, people, places, votes)
- `#TheCivicNode #drinkYourOJ` always last (channel-evergreen)
- Sentence case / PascalCase; no all-caps
- Total 4–7 tags; skill re-rolls silently if outside range

### 6. Artifact write

Write `workspace/drafts/<slug>/youtube-shorts-clip-NN.md`:

```markdown
# YouTube Shorts — TCN Dispatch №NNN · Clip NN

**Clip:** <filename>.mp4
**Generated:** YYYY-MM-DD
**Transcript source:** <srt filename> (fuzzy match | fallback: article)
**Article URL:** https://drinkyouroj.substack.com/p/<slug>

---

## Title

<chosen title — paste into YouTube Studio>

---

## Paste this into YouTube

<hook line 1>
<hook line 2>

→ Full piece on Substack:
https://drinkyouroj.substack.com/p/<slug>

#Shorts #<tag1> #<tag2> #TheCivicNode #drinkYourOJ

---

## Title candidates (for reference)

1. <candidate 1>
2. <candidate 2>
3. <candidate 3>
```

### 7. Per-clip review gate

Present the draft and wait for one of:
- `approve [N]` — selects title candidate N, writes file, advances to next clip
- `redirect [steering]` — re-drafts affected surface(s) only (title, hook, hashtags, or all)
- `skip` — writes a placeholder file (`**STATUS: skipped**`), advances to next clip

Gate display format:
```
Clip NN — <beat slug> (<duration>s)
Transcript match: high | low (fallback: article)

Title candidates:
1. <candidate>   — <one-line rationale>
2. <candidate>   — <one-line rationale>
3. <candidate>   — <one-line rationale>

Description preview:
---
<full description block>
---

approve [1/2/3] | redirect [steering] | skip
```

---

## Shared References (read at runtime, never duplicated)

| Reference | Path | Used for |
|---|---|---|
| Voice file | `workspace/core/anti-ai-writing-style.md` | AI-tells, banned words, substitution rules |
| Headline patterns | `~/.claude/skills/tcn-youtube-thumbnail/references/thumbnail-headline-patterns.md` | Banned hype words, banned clickbait templates, structural patterns |
| Channel boilerplate | Hardcoded in skill (same values as sibling skills) | Substack + Bluesky URLs |

**Fallback when voice file is missing:** flag explicitly, skip AI-tells pass, continue with non-voice work. Same pattern as `tcn-youtube-description`.

**Fallback when headline patterns file is missing:** flag explicitly, apply conservative inline heuristics (no all-caps, no exclamation points, no "SHOCKING/AMAZING/INSANE"), continue.

---

## Substack URL Derivation

1. Extract slug from dispatch dir name
2. Construct: `https://drinkyouroj.substack.com/p/<slug>`
3. Surface: `"Detected article URL: <URL>. Confirm or paste override:"`
4. On confirm (empty / "yes" / "confirm"): use candidate
5. On override: use the pasted URL
6. Slug sanity check: >80 chars, underscores, uppercase, or chars outside `[a-z0-9-]` → flag and require explicit override

---

## Failure Modes

| Situation | Behavior |
|---|---|
| No `.srt` found in dispatch dir | Halt with explicit message and example path |
| No clip files found at clip source | Halt with explicit message |
| Weak transcript match for a clip | One-line warning + fallback to article section; never silent |
| Voice file missing | Flag + skip AI-tells pass; continue |
| Headline patterns file missing | Flag + inline heuristics; continue |
| Slug fails sanity check | Flag + require explicit URL override |
| Title candidate fails acceptance after 3 attempts | Surface best-effort with note on which criterion failed |
| User skips a clip | Write placeholder file; continue batch |
| User redirects at gate | Re-draft only the affected surface(s) |

---

## What This Skill Is NOT

- Not a thumbnail generator (deferred to v2)
- Not a long-form description generator (`tcn-youtube-description` covers that)
- Not a transcript transcriber (assumes `.srt` already exists)
- Not a YouTube uploader (user pastes artifacts manually into YouTube Studio)
- Not a TikTok or Facebook packager (out of scope for v1; description anatomy may differ per platform)
- Not a `--shorts` mode flag on an existing skill

---

## Install Location

`~/.claude/skills/tcn-youtube-shorts/SKILL.md`

Sibling to the existing `tcn-youtube-*` family. References the sibling skills' shared reference files by relative path from the skills root.

---

## v2 Considerations (explicitly out of scope now)

- Per-clip custom thumbnail: 9:16 text-overlay spec (Courier Prime, dispatch serial, TCN mark) composited over a chosen video frame
- TikTok/Facebook packaging (different description anatomy, different hashtag conventions)
- Platform-specific metadata manifest for batch upload tools

---

## Implementation notes (deltas from this spec, post-grounding + post-review)

The skill as built deviates from this spec in the following ways, all deliberate and validated. Recorded here so the spec and the shipped `~/.claude/skills/tcn-youtube-shorts/` agree.

**From grounding (sibling-skill conventions + on-disk reality):**
- **No hand-authored `CLAUDE.md`.** The family's per-skill `CLAUDE.md` is an auto-generated claude-mem activity ledger; 100% of the spec lives in `SKILL.md`. (This spec's "Inputs/format" assumed a companion file; there isn't one.)
- **Failure modes are a bulleted list, not a table** — matches `tcn-youtube-description`/`-thumbnail` house style.
- **Pattern library reference = `../tcn-youtube-thumbnail/references/thumbnail-headline-patterns.md`, not `tcn-youtube-title`.** The title skill is not symlinked into the deployed skills root, so `../tcn-youtube-title/references/title-patterns.md` is a broken link there (a latent bug the description skill already has). The thumbnail patterns file resolves and already carries the structural-pattern library + banned lists. (Separately flagged: symlink `tcn-youtube-title` to repair the description skill's link.)
- **Hashtag total is 5–7, not "4–7."** The spec's 4–7 was an arithmetic slip (1 `#Shorts` + 2–4 dispatch + 2 channel = 5–7).

**From adversarial review (dry-run against the real D10 volume + dispatch dir):**
- **Input hygiene rule added** — ignore macOS ` N.ext` sync-collision files everywhere (21 of them in this dispatch dir). Not in the original spec.
- **Clip detection hardened** — video-extension-only (excludes `.cmproj`/`.llc`/`.audiate`/`.wav`/`.png`), de-dup of render variants (`-polished`/`-final`/`-captioned`), and a count-confirmation gate. The naive glob over-counted to 10 (a `-polished` cold-open twin).
- **Clip ordering** decouples "first beat" from "lacks `clip-NN` prefix"; confirms order whenever any unnumbered clip sits beside numbered ones.
- **Final-draft selection** for the low-match fallback is now explicit: highest `05-draft-vNN.md`, ignoring collision/`-lean` variants (→ `v8`).
- **SRT selection** is name-deterministic (prefer the unqualified master; halt if ambiguous) rather than a cue-count heuristic.
- **Slice-vs-article anchor precedence** made explicit for titles and hashtags (the friction 6 of 9 validation drafters independently hit): titles draw only from spoken-slice words; hashtags prefer spoken proper nouns over article-only ones.
- **`youtube-description.md` is the preferred URL + channel-hashtag source** when present (avoids slug drift) — an added cross-skill read the original spec didn't specify.
- Minor: internal-period titles clarified as allowed; hook closer subject to §3J/§3K; `→` mandated; ffprobe portrait-check kept minimal (YAGNI).
