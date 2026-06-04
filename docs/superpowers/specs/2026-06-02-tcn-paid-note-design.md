# Design Spec — `tcn-paid-note` Skill

- **Date:** 2026-06-02
- **Status:** Approved design, pre-implementation
- **Author:** Justin + Claude (brainstorming session)
- **Implements:** A weekly skill that writes the paid "Thinking Behind the Thinking" backstage note for The Civic Node, by mining the flagship's workflow artifacts and interviewing the writer to steer the angle.

---

## 1. Problem & Context

The Civic Node ships a weekly **paid companion note** to each flagship article — the "Thinking Behind the Thinking" series. Each note is a ~365–490 word first-person essay that exposes **one analytical move from behind the published piece**: a number that changed, a framing that didn't survive contact with the sources, a sentence that almost shipped.

Four installments exist (`workspace/paid/*.md`), all hand-authored. Every other TCN surface has a skill (`tcn-draft`, `tcn-flagship-cover`, `tcn-substack-notes`, the YouTube suite). The paid note is the gap.

**The defining property of this content:** unlike `tcn-flagship-cover` (which compresses what's *already visible* in the finished article), a paid note's raw material is the **opposite** — the move that left no trace in the published text. That material lives in two places: (a) the workflow exhaust (the manifest's fact-check loop history, the v1→vN draft diffs, the manifest's recorded "analytical commitments"), and (b) the writer's head. Therefore the skill must **extract the backstage**, not summarize the draft — and the interview is load-bearing, not decorative.

This was validated by writing one note manually on 2026-06-02 (`workspace/paid/2026-06-10-thinking-behind-the-thinking-windfall-thread.md`): read the flagship + manifest → spotted candidate moves → picked the angle via a question → drafted to the locked format. This skill formalizes that process.

---

## 2. Goals & Non-Goals

### Goals
- Produce the weekly backstage note **prose**, saved to `workspace/paid/`, as a finished deliverable.
- **Mine** the flagship's workflow artifacts to detect candidate backstage moves before asking the writer anything.
- **Interview** the writer to steer the angle and extract what the files don't hold (the writing-process texture).
- Enforce the series' **locked format** from a single source-of-truth doc, so the format can evolve without editing the skill.
- Fail honestly: when a week's production was frictionless and has no strong backstage move, **say so** rather than fabricate one.

### Non-Goals (v1)
- **The cover.** Scope is note prose only. The paid-note cover stays on its existing manual template (`workspace/paid/_template-thinking-behind-the-thinking-cover.md`); a future `tcn-paid-cover` skill may automate it. The note skill *offers* the cover as a handoff but does not generate it.
- **A general paid-article writer.** This skill is specific to the "Thinking Behind the Thinking" backstage series.
- **Multi-day resumable state / manifest.** One interactive session, one short artifact.
- **Image generation.** Out of scope entirely.

---

## 3. Decisions (resolved forks)

| # | Fork | Decision | Rationale |
|---|------|----------|-----------|
| D1 | Scope box | **Backstage note only** | One job per skill, matching the `tcn-draft` / `tcn-flagship-cover` split. |
| D2 | Interaction model | **Mine, then interview to steer** | Mining lets the interview be short and pointed instead of a blank-slate recall exercise. Formalizes "how it was done manually." |
| D3 | Source of truth | **Extract a locked DNA template doc** | Mirrors `tcn-flagship-cover`'s `_template-*.md`; DNA is auditable and evolves without skill edits; doubles as series documentation. |
| D4 | Title formula | **Strong default + sanctioned exception** | "I Had the Wrong ___" is the series signature (3 of 4 exemplars), but some moves are near-misses ("I Almost Wrote X") where forcing a "correction" frame would misrepresent the process. DNA doc encodes the formula AND the exception test. |
| D5 | Architecture | **Single self-contained interactive skill** (not an orchestrator) | The job is one coherent editorial act; the `tcn-article-builder` orchestration machinery would be ceremony for a 400-word note. |

---

## 4. Architecture & Files

```
.claude/skills/tcn-paid-note/
├── SKILL.md                         ← the machine (lean, ~200 lines)
├── CLAUDE.md                        ← small claude-mem context block (convention)
└── references/
    ├── mining-playbook.md           ← the 4 sources where backstage moves hide + detection heuristics
    ├── interview-question-bank.md   ← steering questions, organized by move-type and by the 4 beats
    └── note-format-spec.md          ← output frontmatter schema + furniture-line checklist + validation

workspace/paid/
└── _template-thinking-behind-the-thinking-note.md   ← NEW: the locked prose DNA, loaded each run
```

- **Output artifact:** `workspace/paid/YYYY-MM-DD-thinking-behind-the-thinking-{slug}.md`. The file IS the deliverable; a note that exists only in chat is not finished.
- **Skill name:** `tcn-paid-note` (matches the `type: paid-note` frontmatter).
- **The DNA doc is the source of truth.** Edit the format there, never in the skill. It catalogs the 4 published notes as the exemplar gallery.

---

## 5. The DNA Template Doc — `_template-thinking-behind-the-thinking-note.md`

The locked prose DNA the skill loads each run. Contents:

1. **Series purpose** — one paragraph: what the paid note is and the implicit subscriber promise ("the analytical moves behind the piece, including the ones that didn't survive contact with the primary sources").
2. **The single-move rule** — a note features exactly ONE analytical move, not a summary.
3. **The "invisible move" principle** — prefer a move that left no trace in the published piece; explicitly subtract anything the flagship already confesses openly.
4. **Title formula** — "I Had the Wrong ___" as strong default; the exception test for near-misses ("I Almost Wrote ___" / "The Sentence I Cut"); both documented with examples.
5. **The four structural beats** — ① the wrong read → ② the breaking moment (concrete pivot) → ③ the corrected read → ④ the lesson (closer aphorism). Plus the **quiet method-note variant** (Helium "I had to add them in my head") for weeks without a dramatic pivot.
6. **Furniture lines (locked typography)** — title (plain text repeat), italic subtitle, `*Process note — analytical backstage for [flagship](url).*` (this line KEEPS its em dash), the founding-tier refrain at the close.
7. **Body rules** — 365–490 word band; **zero em dashes in the body** (semicolons/periods/parentheses instead); 2–4 primary-source links pulled from the flagship; first person, plain, declarative; short paragraphs.
8. **Closer-aphorism pattern** — generalizes the move into a transferable discipline (e.g., "When the private analysis produces a correction, the published work should say so").
9. **Output frontmatter spec** — see §8.
10. **Exemplar gallery** — the published notes (four at time of writing; appended as the series grows), each annotated with the move it featured and which beat-shape it used.

---

## 6. The Process (7 steps, 3 gates)

### Step 0 — Preconditions
Verify the flagship is **final** (manifest `status: ready-to-publish`, or the user confirms) and the DNA template doc exists. Halt if either is missing. Do not guess.

### Step 1 — Locate flagship + load context
Resolve the flagship in order (first match wins): explicit path → newest `workspace/drafts/{slug}/` whose manifest is `ready-to-publish` → ask if ambiguous. Read in full: the final draft (highest `05-draft-vN.md` or `*-final.md`), the **manifest**, the DNA doc, and the existing exemplar notes — **globbed** via `workspace/paid/*-thinking-behind-the-thinking-*.md` (four as of this writing; never hardcode the count, since the series grows weekly). If `workspace/core/anti-ai-writing-style.md` exists, load it too.

### Step 2 — Mine for candidate moves
Scan the workflow exhaust (detail in `mining-playbook.md`). Four sources:
- **Manifest fact-check loop history** → *the number that changed*.
- **Draft v1→vN diffs** → *the sentence that almost shipped*.
- **Manifest "analytical commitments" / Notes** → *the discipline pre-committed to*.
- **The flagship's own confession section** → read it to **subtract** it from the candidate pool (the note must feature a move invisible in the published piece).

Output: 2–3 candidates, each as `{ one-line move, evidence (artifact + location), visible-or-invisible-in-published }`. Prefer invisible.

### Step 3 — Present candidates → writer picks  → **GATE 1**
Surface 2–3 candidates via `AskUserQuestion`. Responses: pick / "different move" (re-mine with steering) / "combine." **Never pad a weak third candidate** (editorial-honesty rule borrowed from `tcn-flagship-cover`).

### Step 4 — Interview to steer  → **GATE 2 (the heart)**
Ask 3–5 targeted questions (from `interview-question-bank.md`), tailored to the chosen move-type, **one at a time**. The interview only asks what mining couldn't already answer. Cover the four beats; confirm the title-formula instance (the "wrong ___" or the exception). Propose a draft title + closer; let the writer steer.

### Step 5 — Draft to the locked format
Compose against the DNA: furniture lines, 365–490 body, zero body em dashes, 2–4 flagship-sourced primary links, the founding-tier refrain. Derive + confirm frontmatter (§8).

### Step 6 — Present draft → revise  → **GATE 3**
Approve / revise specific lines / "wrong move, restart at Step 3." (The series iterates at the line level — confirmed by edit history.)

### Step 7 — Save + hand off
Write to `workspace/paid/YYYY-MM-DD-thinking-behind-the-thinking-{slug}.md`. Set accurate `word_count`. Report the path and a one-line summary of the featured move. Offer the cover as the next step (manual template now; future `tcn-paid-cover`).

---

## 7. Interview Question Bank (summary; full in references)

Organized by the **four beats**, with move-type tailoring:

- **Wrong read:** "What was the first/easiest version of the connection or claim? The one that would've been most shareable?"
- **Breaking moment:** "What specific source, number, or sentence exposed it? When did you *see* it was wrong?" (Push for a concrete pivot.)
- **Corrected read:** "What replaced it, and why is the replacement truer rather than just safer?"
- **Lesson:** "State the discipline in one transferable line — the rule a reader could carry to the next piece."

Move-type variants (fact-check change vs. cut sentence vs. pre-committed discipline vs. quiet method note) each get a tuned opener. Empty-handed path: if the writer can't produce a crisp breaking moment, offer the quiet method-note shape or flag that the week lacks a strong note.

---

## 8. Output Frontmatter (derived, each confirmed)

```yaml
title: "I Had the Wrong ___"          # from Step 4
subtitle: "..."                        # two-sentence parallel, from Step 4
type: paid-note
status: draft
pillar: <inherit from flagship manifest → confirm>
published: <flagship publish date + 5 days, Fri→Wed → confirm>
created: <today>
updated: <today>
word_count: <accurate count, set at Step 7>
plan_ref: ""
series: The thinking behind the thinking
series_ref: <flagship title> (published <flagship date>)
source_url: "https://drinkyouroj.substack.com/p/{slug}"   # → confirm
```

No field is silently assumed; `pillar`, `published`, and `source_url` are each confirmed with the user.

---

## 9. Failure Modes & Graceful Degradation

| Situation | Behavior |
|---|---|
| Flagship not found / not final | Halt, ask for path. Don't guess. |
| Multiple `ready-to-publish` candidates | List, ask which. |
| DNA template doc missing | Halt with the path. |
| **Mining finds no strong move** (frictionless production) | Don't fabricate. Say so, fall back to interview-first, flag that the week may lack a strong note. |
| **Only candidate is the flagship's public confession** | Flag it; ask for an off-the-page move (featuring a public confession shortchanges subscribers). |
| Flagship has no manifest (older/flat-layout) | Degrade: mine draft diffs if present, else interview-first. Don't halt. |
| No cinematic breaking moment | Allowed — offer the quiet method-note shape. Don't force false drama. |
| Writer rejects all candidates | Re-mine with steering, or go interview-first. |

---

## 10. Scope Boundaries (what the skill never does)

- Never generates the cover image or the cover prompt (offers handoff only).
- Never writes a flagship article (that's `tcn-draft` / `tcn-article-builder`).
- Never writes Substack Notes (that's `tcn-substack-notes`).
- Never fabricates a backstage move to fill an empty week.
- Never features a move the flagship already confesses openly.
- Never pads to a third weak candidate.
- Never puts em dashes in the body (the locked "Process note —" furniture line is the only exception).
- Never skips Step 7 — the saved file is the deliverable.

---

## 11. Triggers (for SKILL.md description)

Invoke when the user says: "write the paid note," "paid article," "this week's paid piece," "backstage note," "thinking behind the thinking," "the process note for [flagship]," or points at a finished flagship and asks for its paid companion. Does NOT apply to the flagship draft, the cover, social posts, or Notes.

---

## 12. Future (not in v1)

- **`tcn-paid-cover`** — automate the locked cover template (four variable substitutions). Sibling to `tcn-flagship-cover`.
- **Auto-publish-date intelligence** — read the content calendar instead of confirming the +5-day default.
- **Cross-note dedup** — check prior notes so the same move-type isn't featured two weeks running.

---

## 13. Implementation Checklist (for the plan)

1. Write `workspace/paid/_template-thinking-behind-the-thinking-note.md` (the DNA doc), cataloging the 4 exemplars.
2. Write `.claude/skills/tcn-paid-note/SKILL.md` (the 7-step process, 3 gates, failure modes, scope boundaries, triggers).
3. Write `references/mining-playbook.md` (4 sources + detection heuristics + the "subtract the flagship's confession" rule).
4. Write `references/interview-question-bank.md` (4 beats × move-type variants + empty-handed path).
5. Write `references/note-format-spec.md` (frontmatter schema + furniture checklist + validation).
6. Write `.claude/skills/tcn-paid-note/CLAUDE.md` (small context block, per convention).
7. Validate end-to-end against the 2026-06-10 note written manually on 2026-06-02 (the skill should reproduce that angle-selection + format).
```
