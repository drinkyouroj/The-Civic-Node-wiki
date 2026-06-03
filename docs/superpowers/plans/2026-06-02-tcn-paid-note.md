# tcn-paid-note Skill — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `tcn-paid-note` skill that writes the weekly "Thinking Behind the Thinking" paid backstage note by mining the flagship's workflow artifacts and interviewing the writer to steer the angle.

**Architecture:** A single self-contained interactive skill (no sub-skill orchestration). It loads a locked prose-DNA doc, mines the flagship's manifest + draft-version diffs + fact-check history for candidate backstage moves, presents them at a pick-gate, interviews to sharpen the chosen move, drafts to the locked format, and saves to `workspace/paid/`. Detail is pushed to a `references/` folder so `SKILL.md` stays lean.

**Tech Stack:** Markdown + YAML frontmatter (Claude Code skill format). No build, no runtime. "Tests" are validation checks (frontmatter parse, link resolution, exemplar-format match, end-to-end reproduction).

**Source spec:** `docs/superpowers/specs/2026-06-02-tcn-paid-note-design.md` — read it first; this plan implements it section-by-section.

**Commit policy:** Per Justin's global rule, do NOT auto-commit. Each task ends with a `git add` (staging) step and a checkpoint. Commit only when Justin says so — ideally one commit at the end, or grouped as he directs. If committing, branch off `main` first (we are currently on `article/issue6-ai-windfall-sharing`, an unrelated branch — do not commit skill work there).

---

## File Structure

| File | Responsibility |
|---|---|
| `workspace/paid/_template-thinking-behind-the-thinking-note.md` | **Source of truth.** The locked prose DNA: format rules, title formula + exception, four beats, furniture lines, body rules, frontmatter spec, exemplar gallery. Loaded by the skill every run. |
| `.claude/skills/tcn-paid-note/SKILL.md` | The machine: 7-step process, 3 gates, failure modes, scope boundaries, triggers. Links to references. |
| `.claude/skills/tcn-paid-note/references/note-format-spec.md` | Output frontmatter schema + furniture-line checklist + pre-save validation. |
| `.claude/skills/tcn-paid-note/references/mining-playbook.md` | The 4 mining sources, detection heuristics, the "subtract the flagship's confession" rule. |
| `.claude/skills/tcn-paid-note/references/interview-question-bank.md` | The four beats × move-type variants + empty-handed path. |
| `.claude/skills/tcn-paid-note/CLAUDE.md` | Small claude-mem context block (project convention). |

**Build order:** DNA doc → references → SKILL.md (so its links resolve) → CLAUDE.md → end-to-end validation.

---

## Task 1: Locked prose-DNA doc

**Files:**
- Create: `workspace/paid/_template-thinking-behind-the-thinking-note.md`
- Reference inputs (read, do not modify): the existing notes globbed via `workspace/paid/*-thinking-behind-the-thinking-*.md` (four as of writing: `2026-05-06-...-federal-state.md`, `2026-05-13-...-strait-mandate.md`, `2026-05-20-...-grid.md`, `2026-05-27-...-helium-number.md`), plus the manually-written `2026-06-10-...-windfall-thread.md`.

- [ ] **Step 1: Acceptance criteria (write these into the top of the file as an HTML comment for the implementer, then delete before finishing)**
  The doc must let the skill, loading ONLY this file, reproduce the format of all five existing notes: the title formula, the three furniture lines, the body em-dash ban, the 365–490 word band, and the closer-aphorism pattern.

- [ ] **Step 2: Read all five existing notes in full** to extract the invariants. Run:
```bash
cd "/Users/justin/Documents/substack-research/Substack Research"
for f in workspace/paid/*-thinking-behind-the-thinking-*.md; do echo "=== $f ==="; cat "$f"; done
```
Note the recurring structure: title (plain repeat) → italic subtitle → `*Process note — analytical backstage for [flagship](url).*` → body → `---` → founding-tier refrain.

- [ ] **Step 3: Write the DNA doc** with these sections (content per spec §5):

  1. **Series purpose** — the implicit subscriber promise (quote the refrain: *"the analytical moves behind the piece, including the ones that didn't survive contact with the primary sources"*).
  2. **The single-move rule** — one analytical move per note, never a summary.
  3. **The "invisible move" principle** — prefer a move that left no trace in the published piece; subtract anything the flagship already confesses openly.
  4. **Title formula** — `I Had the Wrong ___` as strong default (3 of 4 exemplars). Exception test, verbatim:
     > Break the formula only when the move is a near-miss the writer caught **before** publishing (nothing was "wrong" in print). Then use the shape `I Almost Wrote "___"` or `The Sentence I Cut`. The 2026-06-10 windfall-thread note is the canonical exception (it kept `I Had the Wrong Thread` but its true nature was a near-miss — either framing is acceptable when the writer caught it pre-publish).
  5. **The four beats** — ① wrong read → ② breaking moment (concrete pivot) → ③ corrected read → ④ lesson (closer aphorism). Document the **quiet method-note variant** (cite the Helium note's "I had to add them in my head" — a method reveal, not a dramatic pivot) for weeks with no cinematic break.
  6. **Furniture lines (LOCKED, verbatim):**
     ```
     <Title, plain text, repeated>

     *<Subtitle — two parallel sentences>*

     *Process note — analytical backstage for [<Flagship Title>](<flagship url>).*

     ... body ...

     ---

     *Founding-tier subscribers get this in every issue: the analytical moves behind the piece, including the ones that didn't survive contact with the primary sources.*
     ```
     Note: the `Process note —` line KEEPS its em dash. This is the ONLY em dash permitted in the note.
  7. **Body rules** — 365–490 words; **zero em dashes in the body** (use semicolons, periods, parentheses, commas); 2–4 primary-source links pulled from the flagship; first person, plain, declarative; short paragraphs, several one-line.
  8. **Closer-aphorism pattern** — generalizes the move into a transferable discipline. Give the three exemplar closers verbatim as models (federal-state, strait, grid, helium variants).
  9. **Output frontmatter spec** — the YAML block from spec §8, verbatim.
  10. **Exemplar gallery** — a table: each existing note, the move it featured, and its beat-shape (correction vs. near-miss vs. quiet-method). Note: "appended as the series grows."

- [ ] **Step 4: Verify the DNA doc is self-sufficient.** Re-read it and confirm you could write the windfall-thread note from it alone. Run a word-band sanity check on the exemplars to confirm the 365–490 claim:
```bash
cd "/Users/justin/Documents/substack-research/Substack Research"
for f in workspace/paid/*-thinking-behind-the-thinking-*.md; do
  body=$(sed -n '/^\*Process note/,/^Founding-tier/p' "$f" | sed '/^\*Process note/d;/^---$/d;/Founding-tier/d')
  echo "$f: ~$(echo "$body" | wc -w) body words"
done
```
Expected: each in the ~360–490 range (helium ~368, grid ~365, strait ~490, federal-state shorter — confirm the band covers them; widen the documented band in the DNA doc if an exemplar falls outside).

- [ ] **Step 5: Stage (commit gated on Justin).**
```bash
git add "workspace/paid/_template-thinking-behind-the-thinking-note.md"
```

---

## Task 2: references/note-format-spec.md

**Files:**
- Create: `.claude/skills/tcn-paid-note/references/note-format-spec.md`

- [ ] **Step 1: Acceptance criteria** — a pre-save checklist the skill runs at Step 5/7 that catches a malformed note (missing furniture line, body em dash, out-of-band word count, unconfirmed derived field).

- [ ] **Step 2: Write the file** with:
  1. **Frontmatter schema** — every field from spec §8, each annotated `auto` / `confirm` / `set-at-save`:
     ```yaml
     title: confirm            # from interview
     subtitle: confirm
     type: paid-note           # constant
     status: draft             # constant
     pillar: confirm           # inherit from flagship manifest
     published: confirm        # flagship date + 5 days (Fri→Wed) default
     created: set-at-save      # today
     updated: set-at-save      # today
     word_count: set-at-save   # accurate count after final draft
     plan_ref: ""              # usually empty
     series: The thinking behind the thinking   # constant
     series_ref: auto          # "<Flagship Title> (published <date>)"
     source_url: confirm        # https://drinkyouroj.substack.com/p/{slug}
     ```
  2. **Furniture-line checklist** — the four locked lines from DNA §6, as a verifiable list.
  3. **Body validation** — em-dash scan (`grep` for `—` in the body region must return zero), word-count band, link count 2–4.
  4. **Pre-save gate** — "if any check fails, fix before writing; never save a note that fails the em-dash or furniture checks."
  Provide the body em-dash check verbatim:
  ```bash
  # Run after drafting, before save. Body = between the Process-note line and the refrain.
  # NOTE: strip the boundary lines with `sed '1d;$d'` — the Process-note line itself carries the one allowed em dash, so an inclusive range false-fails.
  sed -n '/^\*Process note/,/^Founding-tier/p' DRAFT.md | sed '1d;$d' | grep -n '—' && echo "FAIL: em dash in body" || echo "PASS: no body em dash"
  ```

- [ ] **Step 3: Verify** the checklist catches a bad note: mentally run it against a note with an em dash in the body and confirm it flags. 

- [ ] **Step 4: Stage.**
```bash
git add ".claude/skills/tcn-paid-note/references/note-format-spec.md"
```

---

## Task 3: references/mining-playbook.md

**Files:**
- Create: `.claude/skills/tcn-paid-note/references/mining-playbook.md`

- [ ] **Step 1: Acceptance criteria** — given the Samsung flagship's manifest + drafts, following this playbook surfaces the "same money" cut and the 755%-attribution fix as candidates, and correctly subtracts the flagship's own "I read the wrong variable" confession.

- [ ] **Step 2: Write the file** documenting the four sources (spec §6 Step 2), each with: what to read, what a candidate looks like, and a worked example from the Samsung piece:
  1. **Manifest fact-check loop history** → *the number that changed.* Read the manifest's "Fact-check loop history" table. Worked example: the iteration-3 `755%` attribution precision flag (division vs. company).
  2. **Draft v1→vN diffs** → *the sentence that almost shipped.* Diff consecutive draft versions; reworked/cut closers and frames are candidates. Provide the command:
     ```bash
     cd "/Users/justin/Documents/substack-research/Substack Research/workspace/drafts/<slug>"
     for n in 1 2 3 4 5; do echo "=== v$n → v$((n+1)) ==="; diff <(cat 05-draft-v$n.md) <(cat 05-draft-v$((n+1)).md); done
     ```
     Worked example: the "same money" refusal (visible in the manifest Notes as an analytical commitment; the easy version was cut).
  3. **Manifest "analytical commitments" / Notes** → *the discipline pre-committed to.* Read the manifest "Notes" section. Worked example: "Weld = asymmetry … No 'same money' compression."
  4. **The flagship's own confession section** → **subtract it.** Scan the final draft for a first-person admission section (e.g., a "Personal Code" / "I called this wrong" passage). Any move it already confesses is OFF the candidate list — the note must feature an invisible move. Worked example: the Samsung flagship's "I read the wrong variable" is public, so steer away from it.
  5. **Candidate output shape:** `{ one-line move, evidence (file + location), visible|invisible in published }`. Prefer invisible. Cap at 2–3; never pad a weak third.

- [ ] **Step 3: Verify** by dry-running the playbook against the Samsung artifacts:
```bash
cd "/Users/justin/Documents/substack-research/Substack Research/workspace/drafts/samsungs-400000-bonus-and-the-4000-one"
grep -n "same money\|755%\|asymmetry\|Personal Code\|wrong variable" 05-draft-v6.md manifest.md
```
Expected: hits confirming "same money" (commitment), 755% (fact-check), and the flagship's public "wrong variable" confession (to subtract).

- [ ] **Step 4: Stage.**
```bash
git add ".claude/skills/tcn-paid-note/references/mining-playbook.md"
```

---

## Task 4: references/interview-question-bank.md

**Files:**
- Create: `.claude/skills/tcn-paid-note/references/interview-question-bank.md`

- [ ] **Step 1: Acceptance criteria** — the bank gives, for the chosen move, 3–5 one-at-a-time questions that extract the four beats and the title/closer, and a documented fallback when there's no crisp breaking moment.

- [ ] **Step 2: Write the file** with:
  1. **The four beats, with a default question each** (verbatim, spec §7):
     - Wrong read: "What was the first/easiest version of the connection or claim — the one that would've been most shareable?"
     - Breaking moment: "What specific source, number, or sentence exposed it? When did you *see* it was wrong?"
     - Corrected read: "What replaced it, and why is the replacement truer rather than just safer?"
     - Lesson: "State the discipline in one transferable line — the rule a reader could carry to the next piece."
  2. **Move-type variant openers** — tuned first questions for: (a) fact-check change, (b) cut sentence, (c) pre-committed discipline, (d) quiet method note.
  3. **Title/closer confirmation** — "Does `I Had the Wrong ___` fit, or is this a near-miss you caught pre-publish (use `I Almost Wrote ___`)?" and "Give me the closing aphorism, or approve mine: ___."
  4. **Empty-handed path** — if the writer can't produce a crisp breaking moment: offer the quiet method-note shape, or flag that the week may lack a strong note (do NOT fabricate).
  5. **Interview discipline** — one question at a time; never ask what mining already answered; lead with what you found ("you cut X between v1 and v6 — was that the move?").

- [ ] **Step 3: Verify** the bank against the windfall-thread note: confirm its four beats map to the four default questions (wrong read = "same money"; breaking moment = writing it in plain words / following the dollars; corrected read = leverage; lesson = "when the parallel is real, compress it; when it isn't, name the asymmetry").

- [ ] **Step 4: Stage.**
```bash
git add ".claude/skills/tcn-paid-note/references/interview-question-bank.md"
```

---

## Task 5: SKILL.md (the machine)

**Files:**
- Create: `.claude/skills/tcn-paid-note/SKILL.md`
- Pattern reference (read, do not modify): `.claude/skills/tcn-flagship-cover/SKILL.md`

- [ ] **Step 1: Acceptance criteria** — `SKILL.md` has valid frontmatter (`name`, `description` with triggers + anti-triggers), documents the 7 steps with the 3 gates, lists failure modes and scope boundaries, and every `references/` link resolves to a file created in Tasks 2–4.

- [ ] **Step 2: Write the frontmatter** (model the description on `tcn-flagship-cover`'s rich trigger paragraph):
  ```yaml
  ---
  name: tcn-paid-note
  description: "Writes the weekly 'Thinking Behind the Thinking' paid backstage note for The Civic Node — a ~365–490 word first-person process essay that exposes ONE analytical move from behind that week's flagship article. Mines the flagship's manifest, draft-version diffs, and fact-check history for candidate moves, then interviews Justin to steer the angle before drafting to the locked format. Invoke when Justin says 'write the paid note', 'this week's paid article', 'paid piece', 'backstage note', 'thinking behind the thinking', 'the process note for [flagship]', or points at a finished flagship and asks for its paid companion. Does NOT write the flagship (tcn-draft / tcn-article-builder), the paid cover (manual template / future tcn-paid-cover), social posts (tcn-post), or Substack Notes (tcn-substack-notes)."
  ---
  ```

- [ ] **Step 3: Write the body** with these sections (mirror `tcn-flagship-cover`'s structure; content per spec §6, §9, §10):
  - **What This Skill Does** — extract the backstage (not summarize the draft); the saved file is the deliverable.
  - **Why Interview, Not Summarize** — the raw material is invisible in the published piece; it lives in the workflow exhaust + the writer's head.
  - **Where This Sits** — table routing flagship/cover/Notes to their skills; this skill = paid note prose only.
  - **The Process** — the 7 steps with GATE 1/2/3 marked (Step 0 preconditions, 1 locate+load, 2 mine, 3 pick-gate, 4 interview-gate, 5 draft, 6 revise-gate, 7 save+handoff). At Steps 2/4/5 link the three references.
  - **What This Skill NEVER Does** — the §10 bullets (no cover, no fabricated move, no duplicating the flagship's confession, no weak third, no body em dash, never skip save).
  - **Failure Modes** — the §9 table.
  - **Reference Files** — link all three with one-line descriptions.
  - **Companion Systems** — upstream (tcn-article-builder produces the flagship + manifest); shared source-of-truth (`workspace/paid/_template-thinking-behind-the-thinking-note.md`); sibling (future tcn-paid-cover).

- [ ] **Step 4: Verify frontmatter parses and required keys exist.**
```bash
cd "/Users/justin/Documents/substack-research/Substack Research"
f=.claude/skills/tcn-paid-note/SKILL.md
awk 'NR==1&&$0=="---"{p=1;next} p&&$0=="---"{exit} p{print}' "$f" | grep -E '^(name|description):' && echo "PASS: frontmatter keys present" || echo "FAIL"
```
Expected: both `name:` and `description:` print; PASS.

- [ ] **Step 5: Verify every reference link resolves.**
```bash
cd "/Users/justin/Documents/substack-research/Substack Research/.claude/skills/tcn-paid-note"
ok=1; for r in $(grep -oE 'references/[a-z-]+\.md' SKILL.md | sort -u); do [ -f "$r" ] && echo "OK $r" || { echo "MISSING $r"; ok=0; }; done; [ $ok = 1 ] && echo "PASS" || echo "FAIL"
```
Expected: all three references exist; PASS.

- [ ] **Step 6: Stage.**
```bash
git add ".claude/skills/tcn-paid-note/SKILL.md"
```

---

## Task 6: CLAUDE.md context block

**Files:**
- Create: `.claude/skills/tcn-paid-note/CLAUDE.md`
- Pattern reference: `.claude/skills/tcn-flagship-cover/CLAUDE.md`

- [ ] **Step 1: Write a minimal `CLAUDE.md`** matching the sibling convention — a one-line description of the skill's directory plus an empty `<claude-mem-context>` block for auto-population (open the sibling first to copy the exact shape).

- [ ] **Step 2: Stage.**
```bash
git add ".claude/skills/tcn-paid-note/CLAUDE.md"
```

---

## Task 7: End-to-end validation

**Files:** none created — this validates the whole skill against real artifacts.

- [ ] **Step 1: Confirm the skill is discoverable.** In a fresh turn, confirm `tcn-paid-note` appears in the available-skills list (it will once `SKILL.md` exists with valid frontmatter).

- [ ] **Step 2: Dry-run the mining step** against the Samsung flagship and confirm candidate surfacing:
```bash
cd "/Users/justin/Documents/substack-research/Substack Research/workspace/drafts/samsungs-400000-bonus-and-the-4000-one"
echo "fact-check candidates:"; grep -n "755%\|attribution" manifest.md
echo "commitment candidates:"; grep -n "same money\|asymmetry\|GAP 4" manifest.md
echo "flagship confession to SUBTRACT:"; grep -n "wrong variable\|Personal Code" 05-draft-v6.md
```
Expected: "same money" + 755% surface as candidates; "wrong variable" is identified as the public confession to exclude.

- [ ] **Step 3: Acceptance test — reproduction.** Invoke `tcn-paid-note` against the Samsung flagship. Confirm it:
  - locates `samsungs-400000-bonus-and-the-4000-one` as the (only) `ready-to-publish` flagship,
  - surfaces "same money" among 2–3 candidates at GATE 1,
  - on selecting it, interviews toward the four beats,
  - drafts a note that passes `note-format-spec.md` (furniture lines present, zero body em dashes, 365–490 words, 2–4 links) and lands close to the hand-written `2026-06-10-...-windfall-thread.md` in angle and shape.
  Acceptance: the skill reproduces the angle + format without hand-holding. Differences in wording are fine; a different *move* or a broken format is a FAIL → fix the relevant reference/DNA file.

- [ ] **Step 4: Run the body em-dash check on the skill's output** to confirm the rule holds:
```bash
sed -n '/^\*Process note/,/^Founding-tier/p' <NEW_NOTE>.md | sed '1d;$d' | grep -n '—' && echo "FAIL: em dash in body" || echo "PASS"
```

- [ ] **Step 5: Final staging + commit checkpoint.** Stage any remaining files and PAUSE for Justin's commit decision (do not commit unprompted). Suggested message when approved:
```bash
git add .claude/skills/tcn-paid-note workspace/paid/_template-thinking-behind-the-thinking-note.md docs/superpowers
git commit -m "feat: add tcn-paid-note skill + locked DNA for the weekly backstage note"
```

---

## Self-Review (run by author of this plan)

**1. Spec coverage:**
- §3 decisions D1–D5 → reflected in architecture + Tasks 1/5. ✓
- §5 DNA doc (10 parts) → Task 1 Step 3. ✓
- §6 process (7 steps, 3 gates) → Task 5 Step 3. ✓
- §7 interview bank → Task 4. ✓
- §8 frontmatter → Task 2 + Task 5. ✓
- §9 failure modes → Task 5 Step 3 (Failure Modes section). ✓
- §10 scope boundaries → Task 5 Step 3 (NEVER section). ✓
- §11 triggers → Task 5 Step 2 frontmatter. ✓
- §13 checklist (6 files + validation) → Tasks 1–7. ✓

**2. Placeholder scan:** No "TBD/TODO/handle edge cases." Content steps specify sections + verbatim locked elements + worked examples. Long-form explanatory prose is specified by required points (acceptable for prose authoring) with the locked/structured parts shown verbatim. ✓

**3. Type/name consistency:** File paths consistent across tasks; `tcn-paid-note`, `_template-thinking-behind-the-thinking-note.md`, the three reference filenames, and the three gate labels match between the plan, the spec, and the validation commands. ✓ (Fixed: Task 3 had a duplicated list-number "3" for the candidate-output bullet — cosmetic, not a name collision.)

**Note on TDD adaptation:** there is no executable unit-test framework for Markdown skills. Each task's "verify" step is a real, runnable check (grep/awk/diff/word-count) or the end-to-end reproduction test, which is the meaningful acceptance gate here.
