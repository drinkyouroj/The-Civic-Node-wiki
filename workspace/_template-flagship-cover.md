---
title: "Template — Flagship Substack Cover (DNA Specification)"
type: image-prompt-template
applies_to: flagship nonfiction Substack covers
established: 2026-05-22
aspect_ratio: "16:9 (1456 × 816)"
model: Nano Banana Pro / Flux / Midjourney
status: locked-dna-variable-execution
---

# Flagship Cover Template — DNA Specification

This is the locked visual identity for flagship nonfiction Substack covers (e.g., "Cheaper AI Won't Use Less of Anything," "The System Is Functioning Correctly," "Atlanta Passed a Sanctuary Resolution," "The $71 Billion Bluff"). Unlike the paid-note template ([`workspace/paid/_template-thinking-behind-the-thinking-cover.md`](paid/_template-thinking-behind-the-thinking-cover.md)) — which locks a single composition with four variable substitutions — flagship covers lock a **DNA** (five principles) and leave **execution** (four axes) open per piece.

The reason: paid notes are a consistent format with a consistent register, so a single composition works. Flagship pieces vary widely — a Fed-policy explainer, a surveillance-infrastructure investigation, a market-collapse analysis, and a constitutional-law breakdown all need different visual idioms but a shared editorial voice. The DNA produces that shared voice without dictating the idiom.

Companion skill: `tcn-flagship-cover` — invokes this template, applies the DNA to a finished article, proposes 2–3 concept briefs, and writes the prompt file. Use this template doc directly only for reference or for revising the DNA itself.

---

## The five locked principles

These are non-negotiable. A concept that fails any of them is not a flagship-quality cover.

### 1. Metaphor compression, not evidence illustration

The image carries the thesis through ONE relationship — face-IS-bureaucracy, camera-vs-neighborhood, signature-vs-collapse, steam-engine-↔-DDR5. The reader's eye finds the metaphor in under a second.

The failure mode: documentary-evidence collages, labeled blueprints, document stacks, cork boards with sticky notes, encyclopedic infographic posters. These illustrate the *evidence* the piece is built from instead of *compressing* what the piece argues. The reader has to read the cover before they can understand it. That's a verbal job the title already does.

### 2. ≤2 primary visual elements

Either one central subject (a face, an object, a unified scene) OR two icons in a clean comparison. Never three competing zones. Never a multi-panel layout. Never a labeled diagram with multiple callouts.

A scene with multiple objects can pass this if the objects form ONE compositional unity — e.g., the ukiyo-e scholars on the cliff are technically two figures, but they read as a single tableau. The test is whether a viewer at thumbnail size resolves it as one image or as several elements competing for attention.

### 3. No embedded text in the image

No labels, no sticky-note callouts, no document captions, no "stamped" words, no chart titles. The image stays visual; the post title and subtitle do all verbal work.

This is the principle most often violated by AI image generators, because text-in-image is a common request and the models default toward including it. The skill should explicitly negative-prompt embedded text.

Exception: when the metaphor *requires* a piece of text (e.g., a hand-painted "Welcoming City ATL GA" sign reflected in the Atlanta camera housing, where the sign IS the metaphor), the text must be a real-world physical element, not an editorial annotation. The Atlanta cover has text but it's photographed signage — the camera is the editorial element, the sign is the world.

### 4. Cinematic OR technical illustration register

Permitted registers:
- Editorial poster (B&W subject + saturated color backdrop, single hard key light, film grain — see *$71B Bluff*)
- Surreal symbolic (one symbolic object composed of unexpected materials — see *System Is Functioning Correctly*)
- Photographic with reflection device (one photographed object whose surface or reflection embeds the secondary subject — see *Atlanta*)
- Clean technical illustration (isometric, white background, industrial palette — see *Cheaper AI*)
- Narrative scene (single illustrated tableau in a stylistically distinct register — see *I Had the Wrong Protagonist*, ukiyo-e)

Excluded registers: documentary scrapbook, encyclopedic infographic, labeled blueprint, split-frame "before/after" with cluttered scenes, screenshot composite.

### 5. High contrast as the carrying device

Something is the contrast that carries the argument: B&W subject vs. saturated backdrop, cold color vs. warm color, present vs. absent, sparse vs. ornate, photographed-real vs. illustrated-symbolic. The contrast IS the visual argument; without contrast, the cover lacks editorial weight.

---

## The four variable axes

Where execution choices happen. The skill should pick deliberately on each axis for every piece — never "default."

### Axis 1: Photographic vs. illustrated

| Pole | When to use | Examples |
|---|---|---|
| Photographic | Real public figure as subject; piece reports on a specific public moment | *$71B Bluff* (Altman), *Atlanta* (Flock camera in situ) |
| Surreal symbolic illustration | Thesis is about an institution, a system, or an abstract pattern | *System Functioning Correctly* (face-of-documents) |
| Clean technical illustration | Thesis is a structural argument across two domains | *Cheaper AI* (steam engine ↔ DDR5) |
| Narrative illustration in distinct register | Thesis benefits from a specific cultural visual idiom | *I Had the Wrong Protagonist* (ukiyo-e) |

### Axis 2: Palette

No fixed palette. The palette serves the contrast (Principle 5) and the register (Principle 4). Some patterns we've validated:
- B&W subject + single saturated backdrop color (the $71B Bluff move)
- Cold object + warm reflected scene (Atlanta — steel-blue camera, amber neighborhood)
- White background + industrial charcoal/steel-blue (Cheaper AI)
- Warm cream/sepia + brick-red accent (paid note covers — preserved here as a sibling system)
- Muted natural multi-color (ukiyo-e register)

Never: rainbow palettes, default-AI saturated photography, "infographic" colored data bars.

### Axis 3: Light vs. dark mood

Varies with piece register. Investigative pieces lean dark/cinematic ($71B Bluff). Structural-systems pieces can be either ("System" is dark and chaotic; Cheaper AI is light and ordered). Whatever serves the argument.

### Axis 4: Person / object / scene

The subject type is determined by the piece. The skill should propose at least one non-face concept for every piece, and at least one face-forward concept ONLY when a face would genuinely strengthen the cover (see Face Consideration below).

---

## Exemplar gallery

Four worked examples covering different points on the variable axes. Each demonstrates the DNA in a different register.

### Exemplar 1 — *The $71 Billion Bluff* (Apr 2026)

- **Article**: [The $71 Billion Bluff](https://drinkyouroj.substack.com/p/the-71-billion-bluff)
- **Compression**: Person + symbolic backdrop. The signature decision a single executive holds over a collapsing market.
- **Subject**: Sam Altman in B&W three-piece suit, seated at conference table, fountain pen + unsigned document.
- **Secondary element**: Saturated green DRAM cascade behind him (the market falling).
- **Register**: Editorial poster / financial thriller (neo-noir).
- **Palette**: B&W subject + saturated green; dark moody.
- **Why it passes**: ✓ Compression (one face, one prop, one backdrop carries the thesis). ✓ ≤2 elements. ✓ No embedded text. ✓ Cinematic. ✓ B&W/green contrast carries the argument.
- **Face decision**: Yes — Altman is the named decisionmaker, his face anchors the piece to the specific moment.
- **Full prompt file**: [`workspace/drafts/the-71-billion-bluff-cover-prompt.md`](drafts/the-71-billion-bluff-cover-prompt.md)
- **Library reference**: YouMind #8791 (Neo-Noir Fashion Portrait)

### Exemplar 2 — *Cheaper AI Won't Use Less of Anything* (Apr 2026)

- **Article**: [Cheaper AI Won't Use Less of Anything](https://drinkyouroj.substack.com/p/cheaper-ai-wont-use-less-of-anything)
- **Compression**: Two-icon comparison. Jevons paradox — same machine, different era. The connecting line IS the thesis.
- **Subject**: Victorian brass steam engine with coal at its base.
- **Secondary element**: Stack of green DDR5 memory modules with gold contacts, connected to the steam engine by a thin line.
- **Register**: Clean technical illustration, isometric.
- **Palette**: White background, industrial charcoal + steel blue + brass + green-gold.
- **Why it passes**: ✓ Compression (the line is the argument). ✓ 2 elements connected. ✓ No embedded text. ✓ Technical-illustration register. ✓ Contrast (Victorian brass vs. modern memory).
- **Face decision**: No — piece is a structural argument about energy economics, not a named protagonist.
- **Full prompt file**: not preserved — reconstruct from alt text if needed.

### Exemplar 3 — *The System Is Functioning Correctly* (Apr 2026)

- **Article**: [The System Is Functioning Correctly](https://drinkyouroj.substack.com/p/the-system-is-functioning-correctly)
- **Compression**: Symbolic object — the bureaucracy IS the face. One unified subject built from the materials of the system the piece indicts.
- **Subject**: A face materializing from a typewriter, composed of denial stamps, redaction bars, and government text.
- **Secondary element**: A chaotic desk with multiple clocks behind, gray-suited hands still typing.
- **Register**: Surreal symbolic illustration.
- **Palette**: Muted bureaucratic — paper, ink, manila, gray suits, faded blues.
- **Why it passes**: ✓ Compression (the materials ARE the subject). ✓ 1 primary visual element (the face), with secondary scene supporting. ✓ Embedded text is the *material*, not editorial annotation (the words are what the face is made of, not labels on top). ✓ Surreal symbolic register. ✓ Contrast (organic face form, bureaucratic materials).
- **Face decision**: No, in the strict sense — no real individual. But the symbolic face is the editorial move.
- **Full prompt file**: not preserved — reconstruct from alt text if needed.

### Exemplar 4 — *Atlanta Passed a Sanctuary Resolution* (Apr 2026)

- **Article**: [Atlanta Passed a Sanctuary Resolution. The Vendor Contract Didn't.](https://drinkyouroj.substack.com/p/atlanta-passed-a-sanctuary-resolution)
- **Compression**: Photograph with reflection device — one photographed object embeds the secondary subject inside its surface.
- **Subject**: A Flock Safety ALPR camera on a pole, close-up, cold steel-blue.
- **Secondary element**: A warm amber street scene reflected in the camera housing — a "Welcoming City ATL GA" sign, parked cars, a corner deli.
- **Register**: Photographic with reflection device.
- **Palette**: Cold steel-blue exterior vs. warm amber reflection. Color-temperature contrast IS the argument.
- **Why it passes**: ✓ Compression (the reflection IS the thesis — the city the camera doesn't see). ✓ ≤2 elements (camera + reflected scene). ✓ Embedded text is real-world signage (the "Welcoming City" sign is the metaphor's hinge). ✓ Photographic register. ✓ Cool/warm contrast.
- **Face decision**: No — piece is about institutional capture, not named individuals.
- **Full prompt file**: not preserved — reconstruct from alt text if needed.

---

## Concept brief format

The skill produces concept briefs in this structure (each option):

```
Compression name:      [the metaphor strategy in 3-5 words]
Subject:               [primary visual element]
Secondary element:     [the thing the subject relates to — backdrop, reflection, second icon, absence]
The relationship:      [one sentence — what carries the thesis]
Visual register:       [photographic / illustrated / isometric / surreal symbolic / etc.]
Palette direction:     [palette choice and why]
DNA checks:            [5/5 — confirmed inline]
One-line evocation:    [the cover described in the voice you'd describe it to a reader]
```

Three concepts means three different *compressions*, not three variants of one composition. If the piece only has two strong compressions, propose two. Editorial honesty over feature completeness.

---

## Face consideration

When the article has an identifiable individual at its center, the skill prompts for a yes/no decision with reasoning. The skill should also volunteer when a face would be wrong — having a named protagonist does not mean the cover should be face-forward (e.g., the Helium piece has named co-authors but the argument is structural).

The decision and reasoning get captured in the output file frontmatter:

```yaml
face_decision: yes | no
face_subject: "[name]" | null
face_reasoning: "[one sentence explaining the choice]"
```

Over time this builds an audit trail — which pieces used faces, which didn't, and which framings worked.

---

## Legal note on real public figures

AI-generated likenesses of real public figures are widely used in editorial cover art, but the legal contour varies by subject.

*Editorial use of public officials* (presidents, members of Congress, Fed chairs, federal judges, agency heads) is well-protected First Amendment territory. *Senior executives at large public companies* (CEOs like Altman, Cook, Musk; named officers in SEC filings) are generally treated similarly in editorial context, especially when the piece is reporting on their public-record decisions. *Less-public figures* (mid-level executives, named-but-not-famous individuals, plaintiffs/defendants in civil litigation, identified-but-not-public engineers or staff) carry more right-of-publicity risk and benefit from a non-face concept by default.

None of this is legal advice — when uncertain, default to a non-face compression or consult counsel. Track decisions in `face_decision` so the catalog is auditable.

---

## Output file convention

Every cover decision produces a saved prompt file at:

```
workspace/drafts/{slug}/cover-prompt.md
```

(Or `cover-prompt-v1.md` if iteration is anticipated — the v1→v2 audit-trail pattern from the Helium piece.)

Frontmatter captures:

```yaml
---
title: "Cover Prompt — [Article Title]"
type: image-prompt
article: "[path to final draft]"
model: Nano Banana Pro | Flux | Midjourney | other
aspect_ratio: "16:9 (1456 × 816)"
based_on: "[template id or 'flagship-dna']"
compression: "[compression name]"
register: "[visual register]"
palette: "[palette description]"
dna_checks:
  compression: yes
  two_elements_or_fewer: yes
  no_embedded_text: yes
  cinematic_or_technical_register: yes
  contrast_carries_argument: yes
face_decision: yes | no
face_subject: "[name]" | null
face_reasoning: "[one sentence]"
created: YYYY-MM-DD
---
```

Body sections: the full model-ready prompt, alt text, caption, remix notes (what was varied vs. an exemplar, if relevant).

No `cover-prompt.md` saved = the cover is considered unfinished, regardless of whether an image has been rendered.

---

## Aspect-ratio adapter notes

- **Midjourney / Nano Banana Pro**: use `--ar 16:9` in the prompt.
- **DALL-E 3**: request "wide landscape, 1792 × 1024".
- **Stable Diffusion / Flux**: set width 1456, height 816 explicitly.
- **GPT Image 1.5 / Seedream 5.0**: request "16:9 aspect ratio, 1456 × 816 px".

---

## Provenance

- Established 2026-05-22 during brainstorming session that codified the DNA from a rated corpus of 9 covers (5 favorites, 4 least-favorites).
- DNA principles derived from cross-checking what favorites share and least-favorites share, not from external visual-system theory.
- Companion skill `tcn-flagship-cover` built separately via skill-creator; this doc is its source of truth.
- Parallel system: paid notes ([`workspace/paid/_template-thinking-behind-the-thinking-cover.md`](paid/_template-thinking-behind-the-thinking-cover.md), established 2026-05-19) — different format, different locked composition, sibling not parent.
- Fiction-episode cover system: deferred (separate spec, future).

## Future updates

If a future piece surfaces a need to evolve the DNA (a new register that produces a great cover the current principles don't capture; a principle that turns out to over-constrain; an exemplar that should replace one of the current four), document the change here as a numbered revision rather than overwriting silently. The DNA's value is its stability across pieces — modifications should be deliberate and dated.
