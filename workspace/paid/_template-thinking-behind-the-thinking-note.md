# The Civic Node — "Thinking Behind the Thinking" Paid Note (Locked Prose DNA)

> **What this file is.** The source-of-truth DNA for the paid "Thinking Behind the Thinking" backstage note. The `tcn-paid-note` skill loads this file on every run and enforces the format described here. This is the prose analogue of `workspace/core/_template-flagship-cover.md` (which the `tcn-flagship-cover` skill loads for image prompts): the DNA stays stable so the series reads as a series; the per-note execution flexes so each week's note is its own essay.
>
> **This file is a spec, not a published note.** The rules below describe what a finished note must do. The "no em dash in the body" rule, the word band, the furniture skeleton — those govern *the notes*, not this document. Em dashes, long headings, and tables are fine *here* because this is documentation.
>
> **How to edit.** Change the format here, never in the skill. When the series grows, append the new note to the Exemplar Gallery (§10). The skill globs the gallery; it never hardcodes the count.

---

## 1. Series purpose

The paid note is a weekly first-person essay that exposes **one analytical move from behind the published flagship** — a number that changed once the writer sat with the primary source, a framing that looked sharp until the dollars were traced, a sentence that almost shipped and didn't. It is sold to founding-tier subscribers as the backstage pass to the writer's reasoning, and the implicit promise is reproduced verbatim in the closing furniture line of every note:

> *the analytical moves behind the piece, including the ones that didn't survive contact with the primary sources.*

That refrain is the contract. A note honors it by showing the subscriber a move they could **not** have reconstructed from the free flagship — the reasoning that left no trace in the published text. A note that merely re-summarizes the flagship breaks the contract; the subscriber paid for the part that isn't in the article.

---

## 2. The single-move rule

**A note features exactly ONE analytical move. Never a summary.**

One wrong read, one thing that broke it, one corrected read, one lesson. Not "here are three things I reconsidered." Not "here is what the flagship argued." If you can't name the single move in one sentence ("I joined the bonus and the bill with the same money, and following the dollars killed the line"), you don't have a note yet — you have a recap, and a recap is not what the subscriber bought.

The discipline is subtractive. The flagship already made the argument. The note's job is to isolate the *one* place where the writer's private analysis diverged from where it started, and to walk only that path. Everything that isn't the move is cut.

---

## 3. The "invisible move" principle

**Prefer the move that left no trace in the published flagship. Explicitly subtract anything the flagship already confesses openly.**

This is the property that makes the note worth paying for. The free flagship is visible to everyone. If the note features a move the flagship already names on the page — a caveat the article already prints, a limitation the article already admits — then the paying subscriber gets nothing they didn't get for free. The note must feature reasoning that is *invisible* in the published piece: the dead-end the writer walked down and backed out of, the number that was in an earlier draft and got cut, the connection that was the original thesis until it fell apart.

**How to detect candidate moves is the mining-playbook's job (`references/mining-playbook.md`); this doc defines only what a conformant move is.** The honesty principle that governs the output stays here: if the *only* candidate is something the flagship already confesses, that is a signal the week may not have a strong note. Do not fabricate a backstage move to fill the slot. An honest "no strong note this week" or a quiet method-note (§5) is an acceptable output; dressing up a public confession as backstage access is not.

---

## 4. Title formula

### Strong default: `I Had the Wrong ___`

The default formula dominates the back-catalog: *I Had the Wrong Protagonist*, *I Had the Wrong Bottom of the Stack*, *I Had the Wrong Number*, *I Had the Wrong Thread* (see the §10 gallery for the audited titles). The blank is filled by the **thing that was wrong** — the unit of the mistake. It is a correction frame: it announces that the writer's published-or-near-published read was off in one specific, nameable way, and the body shows the fix.

The `___` should be concrete and small. "Protagonist," "number," "thread," "bottom of the stack" — each names a single analytical object, not a vibe. Avoid abstractions ("I Had the Wrong Idea") and avoid topic-words ("I Had the Wrong Take on the Fed"); the blank is the *unit* of the error, not the subject area.

### The exception test (verbatim — quote this when deciding)

> Break the formula only when the move is a near-miss the writer caught BEFORE publishing (nothing was "wrong" in print). Then use the shape `I Almost Wrote "___"` or `The Sentence I Cut`. The 2026-06-10 windfall-thread note is the canonical exception (it kept `I Had the Wrong Thread` but its true nature was a near-miss — either framing is acceptable when the writer caught it pre-publish).

**Reading of the exception.** The default frame ("I Had the Wrong ___") implies something *was* wrong in the printed article. When the writer caught the error in drafting — so the published flagship is clean and nothing shipped wrong — forcing a "correction" frame slightly misrepresents the process. For that case the sanctioned alternatives are:

- `I Almost Wrote "___"` — quote the sentence or claim that almost shipped.
- `The Sentence I Cut` — for a specific cut line.

The 2026-06-10 windfall-thread note is the canonical near-miss: its "same money" closing line never shipped (it died in drafting), yet the title kept the default `I Had the Wrong Thread`. That is allowed. **Either framing is acceptable when the writer caught it pre-publish** — the decision is the writer's, and the skill confirms which one fits rather than imposing it. Pick the frame that most honestly describes whether the error reached print.

---

## 5. The four beats

Every note moves through four beats in order. They are a spine, not a paragraph count; a beat can be one line or several.

1. **The wrong read** — the first, easiest, most shareable version of the claim or connection. State it plainly and own it as yours. ("I started this piece thinking Minnesota's lawsuit was a press release." / "My first draft joined them with money.")
2. **The breaking moment** — a **CONCRETE pivot**: a specific source, a specific number, a specific sentence that exposed the wrong read. This is the load-bearing beat and it must be tangible, not a mood. ("Then I sat down with the vote screenshot. Two proxy labels stacked toward the top: Nova Labs at 26.00%, ferebee at 24.00%." / "191 tracked crossings in April against a pre-war pace of roughly 3,000 per month.")
3. **The corrected read** — what replaced the wrong read, and why the replacement is *truer*, not merely safer. The reorganization the breaking moment forced. ("What the two halves actually share is the cause... the outcomes run opposite because the leverage runs opposite.")
4. **The lesson** — the closer aphorism that generalizes the move into a transferable discipline (see §8). The final line.

### The quiet method-note variant (do not force false drama)

Not every week has a cinematic break. Some moves are not "I was wrong, then a number hit me" but rather "here is a quiet methodological thing I did by hand that the published piece doesn't show." The **Helium note** is the model: its breaking moment is *"I had to add them in my head; the platform shows each proxy as a separate line item."* That is a **method reveal**, not a dramatic pivot — the move is the manual aggregation step the reader would never know happened. The beats still run (wrong read = trusting the headline pass rate; method = adding the proxies yourself; corrected read = who the proposal was for; lesson = the closer), but beat ② is a disclosed technique rather than a thunderclap.

**Rule:** when the week's production was frictionless and there is no genuine breaking moment, use the quiet method-note shape or flag that the week may lack a strong note. **Do not manufacture a false pivot.** A fabricated "and then it hit me" is worse than an honest "here is the unglamorous step I took that you couldn't see."

---

## 6. Furniture lines (LOCKED — reproduce this skeleton verbatim)

Every note is built on this exact scaffold. Fill the angle brackets; keep everything else byte-for-byte.

```
<Title, plain text, repeated under the frontmatter>

*<Subtitle: two parallel sentences, italic>*

*Process note — analytical backstage for [<Flagship Title>](<flagship url>).*

... body ...

---

*Founding-tier subscribers get this in every issue: the analytical moves behind the piece, including the ones that didn't survive contact with the primary sources.*
```

Notes on the furniture:

- **Title repeat.** The title appears twice: once in the YAML `title:` field, once as plain text (no `#` heading) directly under the frontmatter. Identical strings.
- **Subtitle.** Italic, placed under the title repeat, and identical to the YAML `subtitle:` field. It is **two parallel sentences**: the first names the wrong read, the second names the correction or the truer thread. **Locked rule: join the two sentences with a period, not an em dash.** The mature exemplars (strait, grid, helium, windfall) all use a period. The first installment, federal-state, used an em dash in its subtitle; that is a **deprecated, grandfathered case**, not a violation. A lint of the back-catalog against this doc must NOT flag federal-state's subtitle. Going forward, subtitles use a period.
- **`Process note —` line.** This line **KEEPS its em dash**, and it is the **only em dash permitted in the body** (see §7; the subtitle is furniture, not body, and its grandfathered em-dash case is covered above). Format: `*Process note — analytical backstage for [Flagship Title](url).*` The flagship title is a live link to the Substack URL. (Trailing period inside or outside the link is cosmetic; windfall-thread puts it after the link, earlier notes omit it. Either is fine.)
- **Horizontal rule + refrain.** A `---` separates the body from the closing refrain. The refrain is reproduced **verbatim, italic**, every issue:

  > *Founding-tier subscribers get this in every issue: the analytical moves behind the piece, including the ones that didn't survive contact with the primary sources.*

---

## 7. Body rules

- **Word band: 240–490 words** (body only — from the first line after the `Process note —` furniture down to the `---` before the refrain).
  - **Target band for a mature installment: 365–490.** This is where the mature installments cluster and where new notes should aim; the early installments (federal-state especially) run shorter. Read per-exemplar counts from the verification note at the end of this file (the single source of truth for the numbers) rather than restating them here — body counts and frontmatter `word_count` differ by a few words, so cite one basis consistently.
  - **Hard floor: 240.** The first installment (federal-state, 2026-05-06) runs ~240 words and sits below the 365 target. It is the shortest note and anchors the absolute floor. A new note *can* run that short if the move is genuinely tight, but the default ambition is the 365–490 target. (See the verification note at the end of this file.)
- **ZERO em dashes in the body.** Use semicolons, periods, parentheses, and commas instead. The locked `Process note —` furniture line (§6) is the only em dash permitted in the body. (The subtitle is furniture, not body; its rule is a period, with federal-state's em dash grandfathered — see §6. So "no em dash in the body" governs everything from the first body line to the closing `---`, and does not reach back to the subtitle.) When you reach for an em dash, choose: a period for a hard stop, a semicolon for a linked clause, parentheses for an aside, a comma for a light pause.
- **2–4 primary-source links, pulled from the flagship.** Inline `[anchor text](url)` links to the actual primary sources the flagship cites — the HIP markdown, the capacity-auction report, the analyst note, the court filing. These are the receipts that prove the backstage move is real. Helium carries the most worked example (links to two HIPs, two vote pages, plus a third HIP); windfall carries two (the analyst note on the bonus, the PJM market-monitor PDF). Do not invent links; reuse what the flagship already sourced.
- **First person, plain, declarative.** "I started this piece thinking..." / "I had been quoting one number..." / "I went looking for the dollar... There isn't one." The writer is visibly present and owns the wrong read.
- **Short paragraphs; several one-line.** The rhythm is built on isolation — a one-line paragraph lands the pivot or the verdict. ("I was half-right." / "That's a paper trail." / "So the thread isn't dollars.") Do not run dense blocks; the form breathes.
- **Mechanism over shorthand.** Consistent with the house voice (`workspace/core/anti-ai-writing-style.md`): name the specific mechanism rather than the insider term. "A circuit breaker manufactured in South Korea on a 128-week order book" beats "a supply-chain bottleneck." Do not use dismissal labels ("it's theater," "it's noise") as substitutes for explaining the mechanism.

---

## 8. Closer-aphorism pattern

The final line **generalizes the single move into a transferable discipline** — a rule the reader could carry to the next piece, stated so it outlives the specific story. It is not a summary of the note; it is the note's lesson abstracted one level.

Two families have emerged:

**(a) The series signature** — used when the move was a genuine correction. The strait and grid notes both close on the same line, and it functions as the series' recurring refrain:

> *When the private analysis produces a correction, the published work should say so.*

The federal-state note closes on a near-variant of the same idea: *"That's what changed in my read. When the private analysis produces a correction, the published work should say so."*

**(b) The move-specific aphorism** — used when the move has its own teachable shape that the signature line wouldn't capture. The writer derives a fresh closer that names *this* move's discipline:

- Helium (a two-number method note): *"When the private analysis produces a different number than the published one, the paid note carries both."* (Note how it bends the signature line to fit a method reveal rather than a flat correction.)
- Windfall-thread (a near-miss about false symmetry): *"When the parallel is real, compress it. When it isn't, name the asymmetry. The plain sentence is the test that tells you which."*

**Choosing between them:** use the signature line (family a) when the move is cleanly "I corrected something." Write a fresh aphorism (family b) when the move is a method, a near-miss, or a two-number split where the signature line would undersell it. The closer should feel inevitable given the body — the reader arrives at the discipline, then the line names it.

---

## 9. Output frontmatter spec

Reproduce this YAML block at the top of every note. Each field is annotated with how it is set: **auto** (derived mechanically), **confirm** (derived but confirmed with the writer before saving), **set-at-save** (computed at the final save step).

```yaml
title: "I Had the Wrong ___"          # confirm  — the title formula instance (§4), from the interview
subtitle: "..."                        # confirm  — two parallel sentences (§6), from the interview
type: paid-note                        # auto     — constant for this series
status: draft                          # auto     — "draft" on creation; the writer flips to "ready" later
pillar: <inherit from flagship manifest>   # confirm — read from the flagship manifest (`workspace/drafts/{slug}/manifest.md`), confirmed with the writer
published: <flagship date + 5 days>    # confirm  — flagship publish date + 5 days (Fri → Wed), confirmed
created: <today>                       # set-at-save — today's date, stamped at the final save step
updated: <today>                       # set-at-save — re-stamped on every save/edit
word_count: <accurate body count>      # set-at-save — accurate count, computed at the final save step
plan_ref: ""                           # auto     — empty unless a content-plan item maps to this note
series: The thinking behind the thinking   # auto — constant for this series
series_ref: <flagship title> (published <flagship date>)   # auto — composed from the flagship title + date
source_url: "https://drinkyouroj.substack.com/p/{slug}"    # confirm — derived from the flagship slug, confirmed
```

**No field is silently assumed.** `pillar`, `published`, and `source_url` are each confirmed with the writer before the file is saved. `word_count` is set at the final save step from an actual count, not estimated.

**`source_url` grandfather clause.** Early notes (federal-state) predate the `source_url` field and carry an empty `Process note` link (`[Title]()`); `source_url` is required going forward. New notes always populate it, and the `Process note —` furniture link (§6) resolves to that URL.

---

## 10. Exemplar gallery

One row per existing note: filename, the published frontmatter `title:`, the single analytical MOVE it featured, and its beat-shape. The **Published title** column is populated verbatim from each note's real frontmatter `title:` field (verified 2026-06-02) so the §4 title-formula claim is auditable against source. Note that not every note uses the default formula: federal-state's published title is *Minnesota Isn't Here for the Injunction*, the one back-catalog title that does not take the "I Had the Wrong ___" shape. **Beat-shape legend:** *correction* = an error in (or headed for) print that the note fixes; *near-miss* = a move the writer caught pre-publish so nothing shipped wrong; *quiet-method* = a methodological step the writer did by hand that the flagship never shows (no dramatic pivot).

| Filename | Published title (frontmatter `title:`) | Analytical move featured | Beat-shape |
|---|---|---|---|
| `2026-05-06-thinking-behind-the-thinking-federal-state.md` | "Minnesota Isn't Here for the Injunction" | Read Minnesota's ICE lawsuit as a headline-generating press release; the breaking read was that Minnesota is building an evidentiary record (named-agent assault charge + bystander video + the judge writing the open constitutional question into the record) for a longer fight, not chasing the injunction. | correction |
| `2026-05-13-thinking-behind-the-thinking-strait-mandate.md` | "I Had the Wrong Protagonist" | Built a two-act Fed piece around the *chair* as protagonist (Powell pressure, Warsh confirmation); corrected to the *mandate* as protagonist once mapping what rate policy can actually reach — two binding supply-side constraints (Hormuz at 191 crossings vs. ~3,000; tariffs at 19.7%) that no rate tool addresses. | correction |
| `2026-05-20-thinking-behind-the-thinking-grid.md` | "I Had the Wrong Bottom of the Stack" | Ranked the data-center delay (transformers, switchgear) as Force 4 of five holding DRAM prices high; the Stargate Abilene handoffs (Oracle out → OpenAI out → Microsoft in, three upgrades in 90 days) revealed grid capacity as the *floor under all five*, not the fourth force. The site moved because the 1.2 GW grid position was inherited. | correction |
| `2026-05-27-thinking-behind-the-thinking-helium-number.md` | "I Had the Wrong Number" | Led with the 90.53% HIP-143 pass rate as "consensus"; the method reveal was manually summing the proxy labels (Nova Labs 26% + ferebee 24% = ~50% of yes votes from the proposer side) — a step the vote platform doesn't do for you. The pass rate says the vote was clean; the concentration says who it was for. | quiet-method |
| `2026-06-10-thinking-behind-the-thinking-windfall-thread.md` | "I Had the Wrong Thread" | First draft joined the Samsung bonus and the Ohio power bill with "the same money"; writing it in plain words showed the dollars don't meet (the bonus is division profit to shareholders; the bill is PJM's $13.77B capacity-auction cost to ratepayers). The truer shared thread is *leverage* — who at each bottleneck can say no. Caught pre-publish; the "same money" line never shipped. | near-miss |

> **Rows are appended as the series grows.** The `tcn-paid-note` skill discovers the gallery by globbing `workspace/paid/*-thinking-behind-the-thinking-*.md` and never hardcodes the count. **Glob caveat for the skill:** that pattern also matches the cover template (`_template-thinking-behind-the-thinking-cover.md`), this DNA doc (`_template-thinking-behind-the-thinking-note.md`), and any `*-cover-prompt.md` siblings. When enumerating *notes*, the skill should match the dated form `YYYY-MM-DD-thinking-behind-the-thinking-{slug}.md` and exclude `_template-*` and `*-cover*` files.

---

## Verification note (band widened from spec)

The design spec (`docs/superpowers/specs/2026-06-02-tcn-paid-note-design.md` §5, §1) documents the band as **365–490** words. A word-count check of all five exemplars (run 2026-06-02) returned:

| Note | `word_count` frontmatter | clean body count |
|---|---|---|
| federal-state (2026-05-06) | 240 | ~234 |
| strait-mandate (2026-05-13) | 490 | ~431 |
| grid (2026-05-20) | 365 | ~305 |
| helium-number (2026-05-27) | 368 | ~366 |
| windfall-thread (2026-06-10) | 402 | ~404 |

The federal-state note (240 / ~234) falls **below** the spec's 365 floor — it is the first installment and the shortest in the series. Per the task instruction to widen the documented band if any exemplar falls outside it, **this doc documents the band as 240–490** (§7), with **365–490 retained as the target band for mature installments** and **240 as the hard floor**. The 365 figure from the spec is preserved as the ambition, not the minimum. (The clean-body counts run lower than the frontmatter `word_count` values because the frontmatter count appears to include the title/subtitle furniture lines; the §7 band and the `word_count` field both refer to the frontmatter-style count, which is the one a writer sets at save.)
