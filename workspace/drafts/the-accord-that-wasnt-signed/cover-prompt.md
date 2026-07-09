---
title: "Cover Prompt — The Accord That Wasn't Signed"
type: image-prompt
article: "drafts/the-accord-that-wasnt-signed/05-draft-v5.md"
model: Nano Banana Pro | Flux | Midjourney
aspect_ratio: "16:9 (1456 × 816)"
based_on: "flagship-dna"
prompt_source: scratch
compression: "The accord that wasn't signed"
register: "surreal symbolic illustration / cinematic still"
palette: "warm sepia-cream + ink-black (dense top) → cold desaturated grey void (blank, unsigned bottom)"
dna_checks:
  compression: yes
  two_elements_or_fewer: yes
  no_embedded_text: yes
  cinematic_or_technical_register: yes
  contrast_carries_argument: yes
face_decision: no
face_subject: null
face_reasoning: "Named officials (Warsh, Bessent, Miran) are vectors for a structural argument about an off-the-record reversal of Fed independence; a face would frame the piece as a personality story and contradict its thesis that the mechanism is deliberately authorless — the absence is the subject."
created: 2026-06-17
---

# Cover Image Prompt: The Accord That Wasn't Signed

## Prompt

A surreal, cinematic still life of a single official government document on a sheet of heavy archival paper, photographed head-on and filling the frame, standing upright against a plain dark studio void. The upper third of the sheet is dense, formal, and authoritative — packed with tightly-set rows of fine print, an embossed circular seal, and the weight of a signed historical record — but every word is rendered as illegible texture, abstract ink strokes that read as type without ever forming readable letters. As the eye travels downward, the printed lines thin, loosen, and break apart into fine particles of ink and paper fiber that lift off the page and dissolve into the air, until the lower half of the sheet is almost entirely blank — an empty, unwritten expanse.

At the very bottom of the document sits a single horizontal signature line, ruled and waiting, completely empty — no signature, no name, no pen anywhere in frame. The vast quiet of blank paper above the empty line is the place where the record should be. The document is the only object in the image; nothing else competes for attention.

Lighting is soft, low, and reverent — a single raking key light from the upper left grazes the embossed top of the page, catching the relief of the seal and the grain of the fibers. The dense top half glows in warm sepia-cream and deep ink-black: aged, archival, important. The dissolving lower half cools into a desaturated steel-grey void, the color temperature dropping as the record disappears. Fine film grain, shallow depth of field, museum-grade macro detail. The register is surreal-symbolic editorial illustration crossed with a cinematic conservation photograph — restrained, serious, no whimsy. The high contrast between the warm, dense, signed top and the cold, empty, unsigned bottom carries the entire image.

Ultra-detailed, photorealistic textures, cinematic color grading, single object, no people. 16:9 aspect ratio, 1456 × 816 px, --ar 16:9.

## Negative prompts

- no legible or readable words, letters, numbers, or dates — all type appears as abstract illegible texture only
- no annotation labels, captions, or callout text
- no chart titles or headings
- no sticky-note callouts
- no stamped editorial words
- no documentary-scrapbook elements
- no labeled blueprints
- no cork-board / pinboard layouts
- no UPC codes, barcodes, or magazine furniture
- no multi-panel layouts (single image only)
- no encyclopedic infographic styling
- no people, hands, or faces

## Alt text

A single official-looking document stands in a dark void; its dense, formal text at the top dissolves into drifting ink particles and fades to a blank lower half that ends at an empty, unsigned signature line.

## Caption

The agreement is already in force. The signature was always the optional part.

## Remix notes

- **Path taken: scratch (Path B).** The `ai-image-prompts-skill` library ran but returned no usable template for an object-only surreal still life. Closest hits were a face-disintegration portrait (YouMind id 9950 — person-centric, requires a face reference) and a torn-paper *image-edit* prompt (YouMind id 761 — requires an existing reference image). Neither maps to a document-as-subject composition, so the prompt was composed directly from the flagship DNA.
- **Structure** modeled on `the-71-billion-bluff-cover-prompt.md` (subject paragraph → secondary-element paragraph → lighting/palette/register paragraph → render directives).
- **Principle 3 handling:** the subject is a document, so it necessarily contains type. Resolved the same way as the *System Is Functioning Correctly* exemplar — text is *material/texture*, never legible words. The negative block forbids any readable letters, numbers, or dates so the model cannot drift into editorial annotation.
- **Differentiation from $71B Bluff:** no person, no fountain pen. There the unsigned document meant a deal that *didn't happen*; here the empty signature line means a binding agreement that *did* happen and left no record — the inverse thesis.
- **Core DNA preserved:** single object (≤2 elements); warm-dense-signed top vs. cold-empty-unsigned bottom is the carrying contrast; surreal-symbolic register; no legible text; metaphor compression (the record erasing itself = the accord that operates with "nothing to FOIA").

## Render guidance

- **Flux:** set width 1456, height 816 explicitly; the `--ar 16:9` token can be dropped.
- **Midjourney / Nano Banana Pro:** keep `--ar 16:9`.
- The dissolve reads best when the particle drift is *upward and sparse* — over-dense smoke turns it into a "burning paper" cliché, which is the wrong connotation (destruction, not quiet erasure). If the first render looks like fire/ash, add "no fire, no flames, no embers, no smoke plume" to the negative block.
