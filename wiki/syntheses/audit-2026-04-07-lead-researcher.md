---
title: "Audit 2026-04-07 — Lead Researcher Report"
type: synthesis
tags: [audit, methodology, schema, wiki-hygiene]
created: 2026-04-07
updated: 2026-04-07
sources: 0
query: "Structural audit of the wiki — schema compliance, cross-linking integrity, concept coverage, index hygiene, and whether overview.md's emerging argument holds up."
---

## Answer

The wiki is doing its job at the content level — clusters are coherent, entity/concept pages are substantive, and the overview synthesis is sharp. But it is failing at the structural plumbing in ways that will compound. The two biggest problems are (1) **the `wiki/syntheses/` directory does not exist**, so every query output since project start has either evaporated into chat or been misfiled, and (2) **`wiki/overview.md` is the single largest source of broken wikilinks in the vault** — it liberally references named actors (Miran, Lisa Cook, Spanberger, Sherrill, Mamdani-as-surname, World Liberty Financial, Israel, Strategic Bitcoin Reserve) that have no backing page. The wiki's best-written document is also its biggest schema violator.

The emerging argument in overview.md largely holds up — the infrastructure-chokepoint spine is real and evidenced — but it papers over the Iran cluster's thinness (6 of the 8 Iran-related concept pages have `sources: 1`) and the mental health cluster's unfinished connective tissue.

Priority below. Numbers in `[brackets]` are the counts I verified against the filesystem today, not what frontmatter claims.

---

## Supporting Evidence

### P0 — Fix These Before The Next Ingest

**P0-1. `wiki/syntheses/` directory does not exist.**
- Verified by `Glob wiki/syntheses/**/*` → no files.
- CLAUDE.md (core rule #7) says "If a query produces a useful synthesis, save it to `wiki/syntheses/`." There is nowhere to save them. This report is the first file in the directory.
- **Action**: This file creates the directory. But it also means every prior query output since the wiki's inception has either been lost to chat scrollback or misfiled into `wiki/concepts/` (which is why some "concept" pages read more like one-off analyses — see the LLM Wiki Agent page). Recommend a one-time sweep of `wiki/concepts/` to identify query-output pages that should move to `syntheses/`.

**P0-2. `wiki/index.md` frontmatter counts are wrong by large margins.**
- `wiki/index.md:5` claims `total_pages: 594` and `total_sources: 385`.
- Actual filesystem counts (from Glob + Grep):
  - `wiki/sources/`: **~384** files (Glob returned 384; one source listed in index probably doesn't have a corresponding file, or vice versa — small drift)
  - `wiki/entities/`: **79** files
  - `wiki/concepts/`: **58** files
  - `wiki/articles/` (including `episodes/`): **82** files
  - `wiki/syntheses/`: **0** files (directory absent)
  - Plus `overview.md`, `index.md`, `log.md` = 3
  - **Total: ~606 pages**, not 594. And `total_sources` should be ~384, not 385.
- The drift is small, but the principle is important: the index is load-bearing metadata and its counts should match the filesystem. This is also a lint item that can be automated.
- **Action**: Recompute both numbers at the end of each ingest; consider adding a section-level count check (Sources: 384, Entities: 79, …) inside `wiki/index.md:9` so drift is visible.

**P0-3. `wiki/overview.md` has at least 10 named-entity broken wikilinks.**
I searched the entire vault for each of these bracketed links and confirmed the target page does not exist:

| Broken link | Where it's referenced | Severity |
|---|---|---|
| `[[Stephen Miran]]` | overview.md L40 + Fed section | P0 — central actor in Fed pressure campaign |
| `[[Lisa Cook]]` | overview.md L40 | P0 — Trump attempted firing is a landmark event |
| `[[Sherrill]]` | overview.md L46 | P0 — NJ governor, 2025 elections centerpiece |
| `[[Spanberger]]` | overview.md L46 (but [[Abigail Spanberger]] exists) | P1 — link format mismatch |
| `[[Mamdani]]` | overview.md L46 (but [[Zohran Mamdani]] exists) | P1 — link format mismatch |
| `[[Strategic Bitcoin Reserve]]` | overview.md L30 | P1 — referenced in Trump entity, but no standalone page |
| `[[World Liberty Financial]]` | implied throughout crypto section, not bracketed but should be an entity | P1 — $57M conflict of interest, no page |
| `[[Israel]]` | entities/Donald Trump.md L93 | P1 — co-belligerent in the active war, no page |
| `[[Jake Auchincloss]]`, `[[Rick Crawford]]`, `[[Tim Kaine]]` | Donald Trump.md Connections | P2 — supporting actors, stubs acceptable |

Additional broken links found elsewhere:
- `[[Federal Immunity Above Constitutional Law]]` — referenced in concepts/Retroactive Executive Protection.md L74 and overview.md L130's cross-cutting patterns. No file.
- `[[Institutional Capture]]` — referenced in concepts/Retroactive Executive Protection.md L76. No file.
- `[[International Humanitarian Law]]` — referenced in concepts/Infrastructure Warfare.md L41. No file.
- `[[Trump blames the radical left for Charlie Kirk's killing]]` — referenced in entities/Donald Trump.md L86. Not in `wiki/sources/` (confirmed via Glob).

**Action**: Create stubs for Stephen Miran, Lisa Cook, Mikie Sherrill, World Liberty Financial, Israel (minimum). Fix the Spanberger/Mamdani link format (use `[[Abigail Spanberger|Spanberger]]` or rename the target). This is a 45-minute pass.

---

### P1 — Schema Compliance Drift

**P1-1. Concept-page `sources:` counts are stale across the entire Iran cluster and most "recent-ingest" concepts.**

The overview says Iran/geopolitics has "~10 sources." Actual counts from concept frontmatter:
- `concepts/War-Driven Inflation.md:7` → `sources: 1`
- `concepts/Chokepoint Control.md:7` → `sources: 1`
- `concepts/Infrastructure Warfare.md:7` → `sources: 1`
- `concepts/Coercive Diplomacy.md` → `sources: 1`
- `concepts/Oil Seizure as Coercion.md` → `sources: 1`
- `concepts/Tech-State Conflict.md` → `sources: 1`
- `concepts/AI Sovereignty.md` → `sources: 1`
- `concepts/Retroactive Executive Protection.md:7` → `sources: 1`
- `concepts/PKM Failure Pattern.md` → `sources: 1`
- `concepts/LLM Wiki Agent.md` → `sources: 1`
- `concepts/Shadow Docket.md` → `sources: 1`

Every one of these has a "Key Sources" section with exactly one entry — so the frontmatter is technically accurate, but that means the concept pages have not been updated as newer sources landed. For example, the Iran war has at least: [[Trump threatens hell on Iran infrastructure if Strait remains blocked]], [[Will blow up everything, take over Iran's oil — Trump says can reach deal by Monday]], [[Britain woos Anthropic expansion after US defence clash]] (DoD angle), and the Marjorie Taylor Greene / coalition sources — but none of that has flowed down into the concept pages.

**This is the single biggest process failure in the ingest workflow**: Step 4 of the INGEST workflow in CLAUDE.md says "If a wiki page already exists: update it, add source to its list, increment `sources:` count." That's not happening for concepts — only for entities (entity counts on Donald Trump = 40, Federal Reserve = 23 look reasonable).

**Action**: One-time reconciliation pass — for each concept, search for `[[Concept Name]]` across `wiki/sources/` and rebuild the Key Sources list. This is the highest-leverage hygiene task in the audit.

**P1-2. Source count in the `wiki/index.md` Federal Reserve section already exceeds the overview's "~30 sources" claim.**

Counting just the Federal Reserve subsection of `wiki/index.md` (lines 23–78): ~35 source entries visible in the first screen, and the section continues further. Not a correctness problem, but the overview numbers are aging.

**P1-3. Concept stubs that are actually fine vs. concept stubs that need work.**

Thin concepts (`sources: 1–2`) that need expansion *now* because the material exists:
- **Chokepoint Control** — should cite Iran sources + NFL Macdonald piece (pre-snap ambiguity is an information chokepoint) + GENIUS Act T-bill backing (captive Treasury chokepoint). The overview explicitly calls out that these are all the same concept (L126), but the concept page doesn't reflect it.
- **Infrastructure Warfare** — should cite Russia/Ukraine if that's in the wiki, and definitely the Gulf energy infrastructure strikes across the Iran cluster.
- **Coercive Diplomacy** — should absorb the Trump dual-track messaging thread that's all over the Iran cluster.
- **Tech-State Conflict** — Anthropic blacklisting + UK recruitment is evidenced across 2+ sources but the concept shows `sources: 1`.

Thin concepts that are correctly thin (genuine 1-source observations):
- **PKM Failure Pattern**, **LLM Wiki Agent** — these are the user's own reflection pages; leave alone.

**P1-4. Entity frontmatter is clean.**

Spot-checked Donald Trump (sources: 40), Jerome Powell (sources: 16), Mechanical Turk concept (sources: 13, matches ~13 evidence citations). Entity and active-cluster concept frontmatter is disciplined. The drift is specifically in the concept pages that haven't been revisited.

---

### P2 — Cross-Linking Integrity Spot Checks

I pulled 10 entity/concept pages and verified a few key ones against their actual citation footprint (files that contain `[[Page Name]]`):

| Page | Claimed `sources:` | Observed citations in `wiki/sources/` | Assessment |
|---|---|---|---|
| Donald Trump | 40 | Not recounted (too many), but Source Appearances list is substantive | Looks accurate |
| Jerome Powell | 16 | Heavy and consistent | Accurate |
| Federal Reserve | 23 | Heavy | Accurate |
| Mechanical Turk Pattern | 13 | Key Sources list has 7+; full text has 10+ inline citations | Roughly accurate |
| Chokepoint Control | 1 | Only cites Iran source | **Stale — should be ~4-6** |
| War-Driven Inflation | 1 | Only cites Iran source + The Great Inflation | **Stale — should be 2-3** |
| Retroactive Executive Protection | 1 | Lists 3 Key Sources | **Frontmatter wrong (should be 3)** |
| Infrastructure Warfare | 1 | Cites only Iran | **Stale** |
| GENIUS Act | 18 | Index shows ~15 GENIUS-titled sources + many that cite it | Roughly accurate |
| Fed Independence | 20 | Strong alignment | Accurate |

**Finding**: Entity pages are maintained; concept pages from the Iran cluster and the older "first draft" concepts are not. The ingest workflow treats entities as the active index but concepts as write-once.

**Orphan check**: Did not do a full orphan sweep (would require reading every page), but based on the ~15 files that reference any of Miran/Cook/Sherrill/Spanberger/Mamdani/etc., the overview.md is carrying the wiki's best cross-link density by a wide margin. Most concept pages have 3-6 outgoing links, most entity pages 5-10. The bottleneck is missing target pages, not missing links.

---

### The Emerging Argument — Does It Hold?

**Yes, mostly, with two caveats.**

The overview.md (182 lines, thoughtful, tight) argues that the wiki's theoretical spine is infrastructure-chokepoint + concealment + state-power-without-accountability + conflict-of-interest, with a Schelling layer underneath. Against the material I spot-checked, that holds:

1. **Chokepoint control** genuinely recurs across Strait of Hormuz, DEA quotas (ADHD shortage), FOMC independence, App Store, stablecoin reserves, and NFL salary cap. The cross-cutting pattern at `wiki/overview.md:126` is well-earned.
2. **Mechanical Turk Pattern** is the cleanest, best-sourced concept in the vault (13 sources, tight concept page, clean entity links to Amazon/Cruise/Google). This is the model for what every concept page should look like.
3. **Crypto cluster** is dense and internally consistent — GENIUS Act, CLARITY Act, Anti-CBDC, Crypto Week all have substantial dedicated pages.
4. **Fed Independence cluster** is similarly dense and the Burns/Volcker historical framing is well-integrated.

**Caveats:**

1. **The Iran cluster is doing heavy lifting for the "infrastructure warfare" thesis but it is only 2 sources of primary coverage** (per the index). The overview says "~10 sources" but half of those are coalition-fracture reactions and tangential material. The war is the most-invoked example of the chokepoint thesis and the least-sourced cluster. If this wiki is feeding a newsletter, the Iran coverage is a risk point — one Reuters story is doing most of the analytical work. **Action**: flag this explicitly in overview.md's Open Questions rather than obscuring it.

2. **The mental health / ADHD / autism cluster doesn't actually hook into the rest of the argument.** It sits on its own with ~30 sources and no cross-link into the chokepoint/infrastructure spine. The overview claims (L87) "DEA Schedule II quota mechanism is the chokepoint" — great argument, but neither [[Chokepoint Control]] nor [[ADHD Medication Shortage]] explicitly links the two. The wiki has the argument; the wiki doesn't have the link.

3. **The NFL cluster doesn't hook in either.** The overview (L126) says the NFL salary cap is "the same kind of object" as the Strait of Hormuz and the Fed chair. That's a genuinely interesting claim. It doesn't appear in [[Chokepoint Control]], [[Salary Cap Optimization]], or [[Defensive Scheme Architecture]]. This is the move the synthesis hasn't made yet — if the cross-cluster spine is real, the concept pages need to cite each other across clusters. Right now each cluster is an island linked only by overview.md.

4. **"Concealment as operating mode" (overview L128)** is an elegant pattern claim but it has no concept page. The three examples (Mechanical Turk Pattern, CISA Jawboning, Iran dual-track messaging) sit in separate pages with no connective concept. This is the strongest synthesis-that-should-become-a-concept in the vault.

---

## Caveats & Gaps

- I did not do a full cross-link orphan sweep. That would require reading every page and is a 2-hour job; I targeted the overview.md's highest-leverage references instead.
- I did not verify the `raw:` field in source pages against actual files in `raw/`. The log.md entry shows the user already did a triage pass on April 7, so this is probably in reasonable shape.
- Spot-checked 5-6 frontmatter samples rather than all 84+ concept/entity pages. A full schema lint would be a separate pass.
- I could not run counts from the shell; all counts are from Glob and Grep output, which has a 250-file cap in some cases. File counts marked as "~384" etc. are within ±2 of the truth.

---

## Newsletter Application

None of this changes the newsletter output directly. But three things here will affect newsletter quality if not fixed:

1. **The missing syntheses directory** means every past query-driven analysis has either been lost or misfiled. Recovering those from chat history and filing them in `wiki/syntheses/` would be a significant one-time content recovery.
2. **The stale concept source counts** mean that when the agent writes an article about "chokepoint control" or "infrastructure warfare," it's pulling from 1 source instead of 5-10. The raw material is there; the indexing isn't. Articles are almost certainly thinner than the vault's actual knowledge would support.
3. **The missing cross-cluster concept page ("Concealment as operating mode," or similar)** is a potential Substack piece in waiting. The synthesis already exists in overview.md L128 — it just needs a home page.

---

## Follow-up Questions

1. Where did the query outputs go before `wiki/syntheses/` existed? Are they recoverable?
2. Should `wiki/index.md` section counts be automated at the bottom of each ingest as a lint step?
3. Is there appetite for a one-time "concept-page reconciliation" pass — rebuild Key Sources for every concept from a `[[Concept Name]]` grep? Estimated 90 minutes.
4. Should the overview.md's cross-cutting patterns (L124-136) be promoted to proper concept pages ("Concealment as Operating Mode," "State Power Without Accountability," "Distributed Alternatives as Implicit Argument")? These are the wiki's highest-leverage ideas and currently live only in overview.md.
5. Are Obsidian sync duplicate files (the ` 2.md` entries in git status) a recurring issue? They're not on disk now but showed up in the status snapshot.

---

## Prioritized Action List (What To Do In One Sitting)

If the user has 60 minutes, in order:

1. **[10 min]** Create stub entity pages for Stephen Miran, Lisa Cook, Mikie Sherrill, World Liberty Financial, Israel. Even minimal (3-sentence overview + 1-2 source links) unbreaks overview.md.
2. **[5 min]** Fix `wiki/index.md` frontmatter counts (`total_pages`, `total_sources`) to match reality.
3. **[10 min]** Reconcile the Iran-cluster concept page source counts: open each of War-Driven Inflation, Chokepoint Control, Infrastructure Warfare, Coercive Diplomacy, add the 2-3 Iran sources that exist, bump counts.
4. **[15 min]** Cross-link the NFL and ADHD clusters into [[Chokepoint Control]]: add a line each citing [[ADHD Medication Shortage]] (DEA quota) and [[Salary Cap Optimization]] (NFL cap) as parallel chokepoint cases. This actually makes the overview's thesis visible at the concept level.
5. **[15 min]** Create the "Concealment as Operating Mode" concept page that consolidates Mechanical Turk Pattern + CISA Jawboning + Iran dual-track messaging. This is the highest-leverage missing page in the vault.
6. **[5 min]** Add one line to `wiki/overview.md`'s Iran cluster noting that the cluster is thinly sourced and should be expanded.
