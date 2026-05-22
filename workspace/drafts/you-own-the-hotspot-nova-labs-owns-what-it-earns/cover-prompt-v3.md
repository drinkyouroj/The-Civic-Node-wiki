---
title: "Cover Prompt — You Own the Hotspot. Nova Labs Owns What It Earns."
type: image-prompt
article: "workspace/drafts/you-own-the-hotspot-nova-labs-owns-what-it-earns/10-final.md"
model: Nano Banana Pro | Flux | Midjourney
aspect_ratio: "16:9 (1456 × 816)"
based_on: "flagship-dna"
prompt_source: scratch
compression: "Auto-extension by inaction"
register: "surreal symbolic illustration"
palette: "Deep cinematic shadow + single warm amber key light; ink-black on cream paper"
dna_checks:
  compression: yes
  two_elements_or_fewer: yes
  no_embedded_text: yes
  cinematic_or_technical_register: yes
  contrast_carries_argument: yes
face_decision: no
face_subject: null
face_reasoning: "Named co-authors (ferebee, Nova Labs, Inversion Capital, zer0tweets) are vectors for the structural critique, not its subject. The argument is about a contract architecture that auto-renews when nobody votes, not about the people who wrote it. Face-forward would mislead."
created: 2026-05-22
---

# Cover Image Prompt: You Own the Hotspot. Nova Labs Owns What It Earns.

## Prompt

A surreal symbolic still life, photographed as an editorial cover image. The central subject is a black lacquer fountain pen with a polished gold nib, suspended in mid-air at a writing angle above an unsigned cream-colored document lying flat on a dark walnut desk. No hand is present. No fingers, no wrist, no body — the pen hovers by itself, tilted as if held by an invisible signer. The pen is the focal point of the image: razor-sharp focus, the gold nib catching the light, a single bead of ink hanging from the tip.

Directly beneath the suspended nib, a signature is in the process of forming on the document — a half-completed cursive ink stroke, visibly mid-motion, the wet ink still glossy where it has just been drawn, fading to dry where the stroke began moments earlier. The signature reads as an abstract calligraphic mark, not as legible letters or words. No words anywhere on the page; the document is otherwise blank cream paper, slightly aged at the edges, lying open and flat. In the deep background, an antique wooden chair is pulled back from the desk at an angle — empty, unoccupied, partially swallowed by shadow — visible enough to register but never competing with the foreground pen for attention.

Lighting: a single hard key light from above and slightly behind, warm amber color temperature, falling in a tight pool on the document, the suspended pen, and the half-formed signature — as if from an out-of-frame brass desk lamp. The rest of the scene falls into deep cool blue-black cinematic shadow — the chair, the back of the desk, the walls, the floor. Strong chiaroscuro: the warm pool of writing-light against the cool surrounding dark. The contrast carries the argument: warm/present where the work is happening, cool/absent where the signer should be.

Register: surreal symbolic illustration in the lineage of Magritte and Caravaggio crossed with editorial-photography realism — a single impossible event presented with documentary seriousness. Photorealistic textures throughout (the grain of the walnut, the weave of the paper, the lacquer of the pen, the reflectivity of the gold nib, the gloss of wet ink), but the impossibility (a pen writing with no hand) presented dead-straight, never cartoonish, never whimsical. The mood is quiet and unsettling, not theatrical. Editorial gravitas. Film grain on the shadows. Aspect ratio 16:9, 1456 × 816 px for Substack hero. --ar 16:9

Negative prompts:
- no embedded text in the image
- no legible words, letters, or numbers on the document or anywhere in the scene
- no readable header, title, or document heading on the page
- no annotation labels
- no chart titles or data callouts
- no sticky-note callouts
- no document captions or printed body text
- no stamped editorial words
- no signage, no calendars with dates, no clock faces with numerals
- no hands, arms, wrists, fingers, or any body parts anywhere in frame
- no person, no figure, no silhouette
- no documentary-scrapbook elements
- no cork-board / pinboard layouts
- no labeled blueprints
- no UPC codes, barcodes, or magazine furniture
- no multi-panel layouts (single image only)
- no encyclopedic infographic styling
- no rainbow palettes, no over-saturated photography

## Alt text

A black fountain pen with a gold nib hovers in mid-air above an unsigned document on a dark wooden desk, drawing a half-completed signature on the paper with no hand present; an empty chair sits pulled back in the deep shadow behind, lit only by a single warm pool of light from an unseen lamp.

## Caption

The vote that extended itself. No signer required.

## Remix notes

- **Closest exemplar**: *The System Is Functioning Correctly* (April 2026) — surreal symbolic illustration, single unified impossible object, cinematic chiaroscuro. This cover preserves that exemplar's *register* (one impossibility presented with documentary realism) and *contrast strategy* (a high-stakes editorial mood carried by lighting, not by saturated color), but inverts the subject: System Functioning is symbolic *presence* (a face built from bureaucratic materials); this is symbolic *absence* (a writing instrument acting with no body).
- **Why scratch, not library**: `ai-image-prompts-skill` was invoked first per the skill's preferred path. Library returned strong portrait-anchored candidates (Cinematic Broken Clock #12839, Surreal Portrait with Floating Elements #14281, Cinematic Tropical Noir Still #13235, Neo-Noir Editorial Collage #16754) but none were structurally usable for a no-human still-life. The library is portrait-dominant; the concept's compression *requires* the absence of any figure. Falling back to scratch.
- **DNA preserved**: (1) Compression — the pen-writing-without-a-hand IS the argument (the HIP-143 auto-extension clause activated with no overriding vote). (2) ≤2 elements — pen + document = unified compositional subject; the empty chair is atmospheric, kept in shadow, never competes for visual weight. (3) No embedded text — explicit and aggressive negative prompts; the signature is rendered as a calligraphic shape, not legible letters; the document carries no header or body text. (4) Surreal-symbolic register — permitted; not excluded territory. (5) Carrying contrast — warm key light pool (present, working) vs. cool blue-black shadow (absent, missing signer). The contrast IS the editorial argument.
- **Text-in-image risk and mitigation**: this is the highest-risk principle for this concept, because the scene contains a document and an active signature. AI generators default to writing legible text on any documents in frame. The negative-prompt block is unusually aggressive: forbids legible letters/words/numbers, forbids document headers, forbids dates or numerals anywhere. The signature is specified as a calligraphic *mark*, not text. If a render comes back with legible text on the page despite the negative prompts, re-render with the negative-prompt block strengthened further (drop the signature stroke if necessary; let the empty page + suspended pen carry the metaphor alone).
- **No-body negative prompts**: parallel risk — generators default toward including a hand when prompted with "pen writing." The negative-prompt block explicitly forbids hands, arms, wrists, fingers, and any body parts. If a render leaks a hand in despite the negatives, retry with the no-body line repeated at the top of the prompt for emphasis.
- **Variant for later iteration**: if v3 renders well structurally but feels too "literal," a v4 could push the pen into more abstract suspension — multiple ink droplets caught in mid-fall, the document slightly translucent, the chair barely visible as a vertical line in the dark. Lock that decision after seeing v3 output.

## Aspect-ratio adapter notes

- **Midjourney / Nano Banana Pro**: `--ar 16:9` as included above.
- **DALL-E 3**: replace with "wide landscape, 1792 × 1024".
- **Stable Diffusion / Flux**: set width 1456, height 816 explicitly.
- **GPT Image 1.5 / Seedream 5.0**: "16:9 aspect ratio, 1456 × 816 px".

## Provenance

- Article: [10-final.md](10-final.md) (final draft, 2026-05-22)
- Skill: `tcn-flagship-cover` (v1, established 2026-05-22)
- DNA source: [`workspace/core/_template-flagship-cover.md`](../../core/_template-flagship-cover.md)
- Library search attempted via `ai-image-prompts-skill` (2026-05-22, 13,659 prompts) — no structurally usable template for no-human surreal still life; fell back to scratch.
- Supersedes [cover-prompt-v2.md](cover-prompt-v2.md), which used the explicitly-excluded YouMind #4847 encyclopedic-infographic template (failed Principle 4 — documentary-scrapbook register; failed Principle 1 — illustrated evidence instead of compressing argument; failed Principle 3 — embedded labels, stamps, era banners, document captions throughout).
