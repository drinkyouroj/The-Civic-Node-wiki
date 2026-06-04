---
name: civic-node-design
description: Use this skill to generate well-branded interfaces and assets for The Civic Node, either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.

If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.

If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.

## Quick reminders for The Civic Node

- **One typeface only:** Courier Prime. Display sizes tracked tight (-0.025em); meta sizes tracked wide (0.10–0.27em, all caps).
- **Colors:** slate-400 (#557FA3) on dark, slate-600 (#3A6A8F) on light. Black is `#0D0D0F`. There is no green, no red, no warning palette.
- **No emoji. No icon fonts. No shadows on dark.** ASCII glyphs (→ ← · — [+]) are the only icon set.
- **Voice:** dry, sardonic, deadpan, precise. Sentence case in headlines. First-person singular. No exclamation marks.
- **The mark** is in `assets/mark.svg` — a vertical antenna, two diagonal arms, and a circular node where they meet.
- **The disclosure block** in `README.md` §1 is verbatim and goes at the foot of any analysis piece.
- **Anti-patterns to never do:** partisan drift, sponsored content, community-before-trust, contrarianism for its own sake, doomerism.

## Files

```
README.md             ← brand, voice, visual foundations, iconography
colors_and_type.css   ← all CSS vars (drop class="tcn" on root)
assets/               ← mark.svg, lockup-dark.svg, lockup-light.svg, social refs
preview/              ← design-system specimen cards
ui_kits/newsletter/   ← Substack-style newsletter recreation
```
