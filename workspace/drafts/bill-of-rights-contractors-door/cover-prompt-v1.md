---
title: "Cover Prompt — The Bill of Rights Ends at the Contractor's Door"
type: image-prompt
article: "drafts/bill-of-rights-contractors-door/draft-v5.md"
model: Nano Banana Pro | Flux | Midjourney
aspect_ratio: "16:9 (1456 × 816)"
based_on: "Editorial Photograph Composition Prompt for Nano Banana Pro (YouMind id: 13292)"
prompt_source: ai-image-prompts-skill
compression: "The seal stops at the door"
register: "photographic, cinematic editorial"
palette: "Warm institutional (brass + marble cream + mahogany) on camera-side vs. cold clinical (fluorescent white + concrete gray + server-rack blue) past the threshold; color-temperature contrast carrying federal/contractor argument"
dna_checks:
  compression: yes
  two_elements_or_fewer: yes
  no_embedded_text: yes
  cinematic_or_technical_register: yes
  contrast_carries_argument: yes
face_decision: no
face_subject: null
face_reasoning: "Piece names individuals (Easterly, Langley, Beekman, Chavies, Barrett) but none is the editorial protagonist. Argument is structural — vendor contracts as constitutional workaround across four domains. Face-forward would narrow the piece to a personality story when the thesis is architectural."
created: 2026-05-27
---

# Cover Image Prompt: The Bill of Rights Ends at the Contractor's Door

## Prompt

A cinematic editorial photograph in 16:9 landscape orientation, shot from a low three-quarter angle, depicting a heavy institutional doorway as the central composition. The camera-side of the threshold shows a polished cream-veined marble floor with a brass federal seal — eagle and laurel wreath only, no surrounding text or motto — embedded directly into the stone. The seal's circular boundary terminates precisely at the line of the doorframe. The door itself is solid mahogany with brushed-brass hardware, opened to roughly seventy degrees so the interior space beyond is partially but clearly visible. The doorframe and architrave are cream-painted plaster with subtle institutional moulding. Long warm shadows fall across the marble in the foreground.

Past the threshold, on the other side of the doorframe, the floor changes abruptly to industrial polished concrete in a cool desaturated gray. The space beyond is a generic vendor workspace — modern, clinical, lit from above by cold overhead fluorescent panels. Visible activity inside the workspace, in soft mid-ground focus: a single bare hand resting on a black keyboard at a low desk; a small pole-mounted security camera angled toward something out of frame; the open corner of a manila contract folder with the edge of a freshly-signed page lifting slightly. The activity is unstaged and candid-feeling. No faces. No identifying features on any person — only a hand, a camera silhouette, and a folder corner.

Lighting: a single hard warm key light from the camera-side at a forty-five-degree angle, illuminating the marble, the brass seal, and the doorframe with rich amber tonality, casting long shadows toward the doorway interior. The vendor space past the threshold is lit entirely by ambient cool fluorescent overhead — distinctly cooler color temperature (~5500K) versus the camera-side amber (~3000K). The two light temperatures meet exactly at the line of the doorframe, producing a visible color break at the threshold. Shallow depth of field with the brass seal in sharpest focus, the vendor activity slightly softened. Editorial-magazine cover quality, subtle film grain, no post-processed glow, no HDR halos.

The compositional argument: the brass federal seal stops at the threshold; the work continues on a floor where the seal never reached. The warm/cold light split at the doorframe is the visual carrier of that argument.

Aspect ratio: 16:9 landscape, 1456 × 816 pixels. For Midjourney / Nano Banana Pro: append `--ar 16:9`. For Flux / Stable Diffusion: set width 1456, height 816 explicitly. For GPT Image 1.5 / Seedream 5.0: include "16:9 aspect ratio, 1456 × 816 px".

## Negative prompts

- no embedded text in the image
- no annotation labels
- no chart titles
- no sticky-note callouts
- no document captions
- no stamped editorial words
- no documentary-scrapbook elements
- no labeled blueprints
- no cork-board / pinboard layouts
- no UPC codes, barcodes, or magazine furniture
- no multi-panel layouts (single image only)
- no encyclopedic infographic styling
- no visible faces or identifying features of any person
- no readable text on the contract folder, keyboard keys, camera body, or anywhere in the image
- no text, motto, or words on or around the federal seal — eagle and wreath shape only
- no recognizable corporate logos or vendor brand marks
- no patriotic visual cliches (no waving flags, no stars-and-stripes color flooding, no eagle clutching anything in talons beyond the wreath)

## Alt text

A brass federal seal embedded in polished marble floor ends exactly at the line of an open institutional doorway. Past the threshold, a cool fluorescent-lit workspace shows a hand at a keyboard, a pole-mounted security camera, and a freshly-signed contract — the work continuing on a floor where the seal never reached.

## Caption

The seal stops at the door. The work continues on the other side.

## Remix notes

- **Library scaffold used:** YouMind #13292 ("Editorial Photograph Composition Prompt for Nano Banana Pro") — selected for its structural pattern (single subject + deep background context, asymmetric composition, controlled color palette, single directional light source, single-source hard lighting with cool ambient secondary). The template's JSON-structured composition/color_profile/lighting blocks gave a clean mapping framework. Element substitution: subject → marble threshold with embedded brass seal; background context → vendor workspace past the doorframe; color palette → warm institutional vs. cold clinical split at the threshold line; lighting → hard warm key from camera-side + ambient cool fluorescent from past-door interior.
- **Core DNA preserved:** photographic-cinematic register (Principle 4); warm/cold color-temperature contrast carrying the federal-vs-contractor argument (Principle 5); single unified threshold-scene that reads at thumbnail size (Principle 2); the brass seal is a photographed real-world physical object, not a label, and all other potential text surfaces are explicitly negative-prompted (Principle 3); the seal-stops-at-doorframe relationship IS the constitutional-limit-vs-vendor-bypass relationship (Principle 1).
- **Deviation from $71B Bluff exemplar (#8791 Neo-Noir):** no human face, no portrait composition. This piece's argument is structural, not personality-driven (Helium-inversion logic applied).
- **Deviation from Atlanta exemplar:** photographic-architectural composition rather than photographic-with-reflection. The boundary device here is the floor-material-change at the doorframe, not a reflective surface. The two share the warm/cold color-temperature contrast as carrying device.
- **Render-time risks to watch for:**
  - **Text on the seal.** AI generators want to write "DEPARTMENT OF JUSTICE" or "UNITED STATES OF AMERICA" around the eagle. The negative prompt addresses this but reroll if any text appears on or near the seal. If persistent, explicit "an unlettered eagle and laurel wreath in brass relief, no inscription, no perimeter text."
  - **Activity-zone competition.** If the keyboard + camera + contract trio reads too busy at thumbnail size and competes with the seal/threshold focal point, drop the contract and let just the keyboard hand + camera carry the vendor activity. Two cues are enough; three is a render-time call.
  - **Patriotic styling drift.** A federal-seal-on-marble prompt risks pulling in flag colors, eagle close-ups, or stars-and-stripes flooding. Negative-prompted but watch for it — the seal should be brass-on-marble, monochromatic relief, not a flag composition.
  - **Doorframe centering.** The threshold line should sit roughly at the vertical-thirds line (left or right of center) so the warm/cold color break creates compositional weight on one side. A doorframe centered exactly in the middle dilutes the argument.

