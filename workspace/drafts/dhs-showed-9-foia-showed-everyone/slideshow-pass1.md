# Slideshow Pass 1 — Dispatch №007

**Source narration:** `youtube-narration.md` · "DHS Showed 9%. FOIA Showed Everyone."
**Deck target:** `dispatch-007.html` (built in Pass 2)
**Canvas:** 1:1 (1080×1080). Final video reaches 16:9 by compositing this square deck beside the host talking-head cam.

---

## Beat inventory (111 beats across 10 scenes)

```
  scene-header:        10  (generated, one per scene)
  stamp:               43
  hero-number:         13
  refrain:              3  (S02/B11, S05/B12, S09/B9 — inverted, identical treatment)
  HTML/CSS/SVG visual: 46  (invoice build, crowd grids, US map, icons, diagrams)
  image (standalone):   6  (S03/B13, S03/B14, S04/B5, S07/B1, S07/B4, S09/B10)
  ─────────────────────────
  Total beat slides:   111
  + scene-headers:      10
  = Deck total:        121 slides
```

**Image-backdrop beats** (typography rendered over an image; keep `stamp` type): S01/B1–B5 (over 007-01), S04/B4 ("Renée Good" over 007-04).

**Motif → render decision:**
- **Invoice → sealed receipt (A):** HTML/CSS — an invoice table that builds line-by-line (S02/B6–B10, S03/B1–B8), recurs as locked cabinet (S07/B12), returns S08/B10.
- **List vs. crowd (B):** HTML/CSS — proportional grids carry data (9%/91%, 63%, conviction slices). An AI image can't render "63% of 3,789" honestly.
- **Windshield → car (C):** narrative IMAGE (007-04, 007-05) — pictorial + recurring subject + emotional floor.

---

## Image placement map (5 generated + 1 existing-asset)

| ID | Scene(s) | Use | Ratio | Necessity | Covers |
|----|----------|-----|-------|-----------|--------|
| 007-01 | S01 | Backdrop | 1:1 | OPTIONAL | S01/B1–B5 (hook stamps overlay) |
| 007-02 | S03 | Standalone | 1:1 | Strong | S03/B13 ("People stopped going to work") |
| 007-03 | S03 | Standalone | 1:1 | Strong | S03/B14 ("Customers stopped crossing the street") |
| 007-04 | S04 + S07 | Backdrop + Standalone | 1:1 | **Non-negotiable** | S04/B4 (overlay), S04/B5 (held), S07/B1 (returns) |
| 007-05 | S07 | Standalone | 1:1 | **Non-negotiable** | S07/B4 ("It took the car") |
| cover | S09 | Standalone | 1:1 | existing asset | S09/B10 — drop in real flagship cover; HTML/CSS card fallback |

Cut priority if fewer images wanted: drop 007-01 first, then 007-02. Never cut 007-04/05 (motif C payoff). 007-02 can also fall back to an HTML/CSS empty-desk icon.

---

## Image prompts (custom — built on the TCN style brief)

All: **1:1 (1080×1080)** · flat editorial vector · near-black `#0f172a` bg · mid-slate `#334155`/`#475569` · light-slate `#64748b` · near-white `#e2e8f0` focal only · NO photography · NO faces/people · NO readable text · NO logos · NO gradients/lens-flare/bright colors. Set the model's aspect-ratio/image_size to **square 1:1** (1080×1080) — the deck records square and crops full-bleed images with `object-fit: cover`, so a 16:9 source would lose its left/right edges.

### 007-01 — Minneapolis, January (OPTIONAL backdrop)
```
Flat editorial vector illustration, 1:1 square. A cold, desolate Minneapolis avenue at dawn in
deep January — empty street receding to a low, simplified downtown skyline of flat rectangular
towers placed across the upper-middle. Bare leafless tree silhouettes, one dark traffic signal,
snowbanks as flat muted-slate shapes. No people, no moving vehicles, no readable signage. Let
the empty dark street and snow fill the foreground/bottom as calm near-black negative space for
a bottom-center typography overlay. Near-black background #0f172a; forms in mid-slate #334155
and #475569; sparse near-white #e2e8f0 only on the farthest skyline edge. Flat geometric shapes,
no gradients beyond subtle flat tonal bands, no photographic texture, no lens flare, no bright
colors. Quiet, austere, documentary-cold mood.
```

### 007-02 — Empty workplace (standalone)
```
Flat editorial vector illustration, 1:1 square. A deserted industrial shift floor, the empty
floor filling the square frame — rows of empty workstations and idle simplified machinery, an
overturned stool, a single time-clock on the far wall, a hard hat left hanging. Completely
abandoned: no workers, no figures, no faces. Cold raking light from high windows as flat
pale-slate beams. Near-black background #0f172a; machinery and benches in mid-slate #334155 /
#475569; light-slate #64748b edges; sparse near-white #e2e8f0 highlights only on the window
light. Flat geometric design, no photographic texture, no gradients, no text, no logos, no
bright colors. Stillness and absence as the subject.
```

### 007-03 — Shuttered storefront (standalone)
```
Flat editorial vector illustration, 1:1 square. A shuttered small storefront centered in the
square frame, on an empty commercial street at dusk — metal roll-down security gate fully
closed over the shopfront, dark unlit interior behind a blank window, a bare sign frame with no
readable text, empty sidewalk, a single dark lamppost. No people, no faces, no traffic.
Near-black background #0f172a; facade and gate in mid-slate #334155 / #475569; sidewalk and
lamppost in light-slate #64748b; one faint near-white #e2e8f0 reflection on the darkened glass.
Flat geometric editorial style, no photographic texture, no gradients, no readable signage, no
brand logos, no bright colors. Mood: economic desolation, a fear-emptied street.
```

### 007-04 — Renée Good's car (backdrop + standalone) — EMOTIONAL FLOOR
```
Flat editorial vector illustration, 1:1 square. A parked sedan from a low front three-quarter
angle, the car and its cracked windshield as the upper-center focal point; the windshield bears
a single radiating bullet-impact star-crack at driver height; the driver's seat visible through
the glass is empty — no person, no face, no figure anywhere. Behind the car, a simplified low
school building with a flagpole and small blank windows across the middle; an empty crosswalk in
the foreground, kept calm for an occasional bottom-center text overlay. Cold early-morning
light. Near-black background #0f172a; car and school in mid-slate #334155 / #475569; light-slate
#64748b structural edges; a single near-white #e2e8f0 glint radiating from the impact crack as
the one focal point. Flat geometric editorial style, no photographic texture, no gradients, no
readable text, no logos, no bright colors, absolutely no people or faces. Restrained, grave,
documentary stillness.
```

### 007-05 — The car in custody (standalone) — MOTIF C PAYOFF
```
Flat editorial vector illustration, 1:1 square. The same sedan, centered in the square frame,
now immobilized inside a federal impound bay — pulled behind a lowered barrier arm and a run of
chain-link fencing, partly draped with a flat evidence tarp, a numbered evidence cone by the
front tire (no readable digits). Cold overhead bay lighting as flat pale-slate pools on the
concrete. No people, no faces, no figures. Near-black background #0f172a; car / tarp / fencing
in mid-slate #334155 / #475569; concrete and barrier in light-slate #64748b; one near-white
#e2e8f0 highlight on the barrier arm. Flat geometric editorial style, no photographic texture,
no gradients, no readable text, no logos, no bright colors. Mood: evidence sealed away, access
denied.
```

### S09/B10 cover — existing asset (do NOT generate)
Use the real flagship cover for this dispatch once produced (publishes Fri 6/12). Until then,
Pass 2 renders an HTML/CSS "cover card" placeholder.

---

## Gate
Generate 007-01…007-05 at **1:1 (1080×1080)** → save PNGs in this draft folder named
`007-01.png` … `007-05.png` → say **"continue"** to build `dispatch-007.html` (Pass 2). Any
missing file renders as a dark placeholder box; the deck still builds.
