# Design: `tcn-substack-engagement` skill

**Date:** 2026-06-08
**Status:** Approved — ready for implementation
**Author:** Justin Hearn (via brainstorming session)

---

## What This Skill Does

Prepares the day's Substack engagement — comments, restacks, and new follows — as a **paste-ready worksheet** the user executes by hand. It reads today's content-plan note for the engagement assignment, uses the Claude-for-Chrome extension as a **read-only sensor** to dedup against the user's own recent activity and discover who is *actually* posting the day's beat, drafts every comment and restack addendum in Justin Hearn's voice, and writes the result to a dated worksheet file.

The skill is **100% read-only on the Substack account.** Claude never types into a composer, never clicks Reply / Restack / Post / Submit, and never clicks Follow. Every action is taken by the user, by hand, from the worksheet. "Act independently" means Claude does all the *cognitive* labor (dedup, live discovery, ranking, drafting); the human does only the final clicks.

It does **NOT**:
- Submit, post, comment, restack, follow, like, or vote — ever (read-only doctrine).
- Write the daily content plan or its Engagement section (that is `tcn-content-plan`).
- Write X/Bluesky/LinkedIn/Facebook social copy (that is `tcn-post` / `tcn-facebook-post`).
- Write Substack Notes (that is `tcn-substack-notes`).
- Promote articles on Reddit (that is `tcn-reddit-campaign`).
- Run headless/autonomously — it requires the user's live logged-in browser session (see Out of Scope).

---

## Position in the Workflow

```
tcn-content-plan  (Mode 1: "check today's plan")
        │  produces workspace/notes/YYYY-MM-DD-*-options.md
        │  whose Engagement section names comment + restack targets
        ▼
tcn-substack-engagement   ← THIS SKILL
        │  reads that Engagement section + duplication_audit + hold list
        │  + live Substack state (via the Chrome extension, read-only)
        ▼
workspace/engagement/YYYY-MM-DD-worksheet.md
        │  paste-ready comments + restack addenda + follow list
        ▼
USER executes by hand (the only writes that ever happen)
```

The skill is a **downstream consumer of the daily content plan** and a **daily recurring** operation. Its sibling in doctrine is `tcn-reddit-campaign` (read-only sensor, human executes, durable ledger), but applied to a recurring daily surface rather than a per-article campaign. That recurrence is why the dedup gate carries the design's weight: the same authors and angles resurface day after day, so *"did I already say this, to this person, this week?"* is the question the whole skill is organized around.

---

## Hard Constraints (Doctrine — never violate)

1. **Read-only on the account.** The Chrome extension is a sensor, never a submit button. Claude never types into a composer and never clicks Reply / Restack / Post / Submit / Follow / Like. The worksheet is the only output.
2. **Account check is a precondition.** Verify the logged-in account is `@drinkyouroj` before any read that informs drafting. If it is not, stop and report — do nothing.
3. **Dedup is a hard gate.** Read `substack.com/@drinkyouroj/likes` (the Likes & Replies tab) *first*, before drafting. Dedup at three levels: **same note**, **same author**, **same analytical angle**. When one lane of the flagship's thesis is already spent, pivot engagement to the unspent lane.
4. **Honest, voice-true authorship.** First-person, truthful attribution; never astroturf, never pose as a third party. All drafted copy must pass `workspace/core/anti-ai-writing-style.md`. No template-stamping — each comment answers what the target actually said.
5. **Stay in the day's authorized lane.** Inherit the plan's spend/hold boundaries. Comments must not spend material the plan is holding for the flagship (e.g., on a cost-layer day: the deaths, sealed evidence, and contempt findings are *held* and must not appear in comments).

---

## Inputs

### Required

- **Today's content-plan note** — `workspace/notes/YYYY-MM-DD-*-options.md`. The skill reads:
  - The **Engagement** section — named comment targets (each with a pre-written angle) and restack targets (each with addendum text).
  - The `duplication_audit` frontmatter — `spent_this_week` and `fresh_today`.
  - The **hold list** — material reserved for the flagship that comments must not spend.
- **Voice DNA** — `workspace/core/anti-ai-writing-style.md`. Loaded in full before any drafting; **never duplicated** into this skill (same contract as `tcn-content-plan`).
- **Live Substack state** — via the Claude-for-Chrome extension (`mcp__Claude_in_Chrome__*`), read-only:
  - The user's Likes & Replies (for dedup).
  - A topic search of the day's beat (to find live posters).
  - Each candidate note's actual text (so the drafted reply is responsive, not generic).
  - The user's existing follows (so follow recommendations exclude accounts already followed).

### Optional

- **Topic override** — a free-text beat to engage, used when no plan note exists for today.
- **Volume override** — e.g., "just 4 comments today," "no restacks," "skip follows."
- **Steering** — free-text like "lean toward the budget-incidence angle," "avoid the partisan accounts."

---

## Run Flow (single primary mode: "run today's engagement")

### 0. Preconditions
- Confirm the Chrome extension is connected and pointed at the correct browser. If not connected, ask the user to connect it — **never** fall back to computer-use clicking a browser (tiered-apps rule: browsers are read-only under computer-use).
- Navigate to `substack.com`; verify the logged-in account is `@drinkyouroj`. If not, stop and report.
- Locate today's plan note. If none exists, offer to invoke `tcn-content-plan` (Mode 1) or proceed from a user-supplied topic. If the user declines both, abort.

### 1. Load context
- Parse the plan's Engagement section (comment targets + angles, restack targets + addenda).
- Parse `duplication_audit` (`spent_this_week`, `fresh_today`) and the hold list.
- Load `workspace/core/anti-ai-writing-style.md` in full.
- Read yesterday's worksheet (`workspace/engagement/`) if present, as a local dedup supplement.

### 2. Dedup read (hard gate)
- Open `substack.com/@drinkyouroj/likes`; read recent replies and restacks.
- Build the **spent set** keyed at three levels: note permalink, author handle, analytical angle.
- Merge in the prior worksheet's targets as a supplement. **Likes & Replies is the source of truth on any conflict.**

### 3. Live discovery
- Search the day's topic at `substack.com/search` (Top + Recent tabs) and scan the home/Notes feed for who is *actually* posting the beat right now.
- Treat the plan's named Tier-1 list as **aspirational seeds, not a checklist** — verify handles (e.g., `@noahsmith` is a CS academic, not Noahpinion) and weight toward whoever is genuinely in the live conversation.

### 4. Target-confirm gate (human checkpoint #1)
- Present the ranked target list as: **live poster → which plan angle it maps to → the specific note permalink**, plus the proposed ~3–5 follow list.
- The user prunes. Claude drafts **only the survivors.** (Rationale: the named list is aspirational, so live targets need a human eye before a full drafting pass is spent.)

### 5. Draft
- For each confirmed comment target: write the paste-ready reply from the plan's angle **against the note's actual content**, so it responds to what the author said rather than stamping a template.
- For each restack target: write the one-sentence added-analysis addendum.
- Run the entire worksheet's prose through the voice DNA check (`anti-ai-writing-style.md`): em dashes, negative parallelisms, dismissal labels, vocabulary cliffs, abstract closers.
- Enforce lane discipline: drop or rewrite anything that would spend held material.

### 6. Output the worksheet
- Write `workspace/engagement/YYYY-MM-DD-worksheet.md` (format below) and surface it in chat.

### 7. (User executes — outside the skill)
- The user opens each permalink, pastes, and clicks. Optionally reports back what was posted so the worksheet can be marked done (keeping the local ledger accurate).

---

## The Worksheet Artifact

**Path:** `workspace/engagement/YYYY-MM-DD-worksheet.md` (new folder; create on first run).

**Dual role:** it is both the day's execution checklist **and** the next day's local dedup ledger. Because it is durable and dated, tomorrow's dedup reads *both* the canonical Likes & Replies (source of truth — catches anything posted off-worksheet) *and* yesterday's worksheet (cheap supplement — catches intended targets).

**Per comment item:**
- `[ ]` checkbox
- Target author + handle
- Note permalink (direct link to open)
- The note's gist (1 line — what the author actually said)
- **Paste-ready comment text** (the deliverable)
- "Why this target" (1 line — which plan angle, why it's unspent)

**Per restack item:**
- `[ ]` checkbox
- Target note permalink + author
- The note's gist (1 line)
- **Paste-ready addendum** (the one sentence of added analysis)

**Per follow item:**
- `[ ]` checkbox
- Account name + profile link
- Rationale (1 line — why following this account trains the algorithm toward the audience)

A short header records: date, the plan note it was built from, the account verified (`@drinkyouroj`), and a one-line dedup summary (what was found already-spent and skipped).

---

## Target Discovery & Ranking

Rank candidate notes by, in priority order:
1. **In the live conversation** — actively posting the day's beat now (Recent tab, recent feed).
2. **Maps to a plan angle** — the plan's angles are the analytic payload; a live poster is only a target if Justin has something specific to add.
3. **Not deduped** — clears all three dedup levels.
4. **Account fit** — audience overlap and engagement likelihood; mid-tier writers in the live topic usually outperform chasing exact Tier-1 handles.

If no live on-topic posters are found: widen to adjacent beats, then report a **"thin day"** with whatever surfaced — never force weak targets to hit a number.

---

## Follow Selection

Default candidate pool (~3–5/day), deduped against existing follows:
1. Authors engaged with today (comment or restack targets) whom Justin does not already follow.
2. Live-topic discoveries on the day's beat that fit the audience but weren't selected as comment targets.

Follows always land on the worksheet for the user to click — never auto-clicked (read-only doctrine).

---

## Browser Interaction Recipe (read-only sensor)

Full detail lives in `references/browser-recipe.md`. Core proven patterns (from the engagement memory):
- The Notes feed lazy-loads and reorders, so coordinate-clicks drift. To act on a specific note reliably: use `find` to get the note-text element ref, then open the permalink by clicking the note body.
- To read reply context: click the comment icon to open the reply modal (read-only — observe, never type/submit). The reply composer sometimes needs an in-modal scroll to reveal fields.
- To read restack context: the restack icon → "Restack with a note" surfaces the compose path (observed read-only).
- Dedup read: `substack.com/@drinkyouroj/likes`.
- Topic discovery: `substack.com/search`, Top + Recent tabs.
- Login check: confirm the visible account is `@drinkyouroj` before any drafting-relevant read.

---

## Skill File Structure

```
claude-skills/tcn-substack-engagement/
├── SKILL.md                          # controller: doctrine, run flow, preconditions, gates
└── references/
    ├── browser-recipe.md             # the read-only interaction recipe (above, expanded)
    └── dedup-and-targeting.md        # three-level dedup, spent-lane pivot, aspirational-Tier-1
                                       #   caveat, ranking heuristic, follow-selection heuristic
```

- Voice DNA is **referenced, never duplicated** — the skill loads `workspace/core/anti-ai-writing-style.md` at runtime (same contract as `tcn-content-plan`).
- After creation, symlink the skill directory into **both** roots (global `~/.claude/skills/` and project `.claude/skills/`), per the repo topology. The canonical source is `/Users/justin/CascadeProjects/claude-skills/tcn-substack-engagement/`.
- Cross-skill reference paths follow the `../../` rule: a file inside `references/` reaches a sibling skill with `../../sibling/...`.

---

## Edge Cases & Failure Modes

| Situation | Behavior |
|---|---|
| No plan note for today | Offer to run `tcn-content-plan` (Mode 1), or take a topic from the user. Abort if both declined. |
| Wrong account logged in (not `@drinkyouroj`) | Stop immediately; report; take no action. |
| Chrome extension not connected | Ask the user to connect it. Never fall back to computer-use clicking a browser. |
| No live on-topic posters | Widen to adjacent beats; report a "thin day" with what surfaced. Do not force weak targets. |
| A plan target is already spent (dedup hit) | Skip it; note it in the worksheet's dedup summary; pivot to an unspent lane/author per the plan. |
| A drafted comment would spend held material | Drop or rewrite to stay on the authorized lane. |
| Voice check fails on a draft | Rewrite before it reaches the worksheet (the worksheet only ever contains voice-passed copy). |

---

## Out of Scope (v1)

- **Headless / autonomous runs.** The dedup read and live discovery require the user's logged-in browser session, which is unavailable headless. v1 is strictly human-present. (A possible v2 could pre-bake a plan-only worksheet flagged "not live-verified, dedup not run," but this is explicitly deferred — YAGNI for now.)
- **Any write action on Substack** — comments, restacks, follows, likes, votes. Permanently out of scope by doctrine, not just v1.
- **Auto-marking the worksheet done.** The user optionally reports back; the skill does not poll the account to detect what was posted.

---

## Open Questions / Future

- **v2 autonomous worksheet pre-bake** — if scheduled-task pre-baking proves valuable, define the degraded "plan-only, not-live-verified" mode and how it reconciles against the next human-present run's dedup.
- **Worksheet completion feedback loop** — whether to add a lightweight "mark done" step that improves the local ledger's accuracy over the canonical Likes & Replies read.
- **Cross-surface dedup** — whether engagement should also dedup against what was said in that day's own Notes (`tcn-substack-notes`) to avoid Justin echoing his own published framing in a comment.
