# Thumbnail prompts — TCN Dispatch №004

**Mode:** reference-image
**Generated:** 2026-05-21
**Vibe reference:** Political Split Screen (id=4729) — https://youmind.com/nano-banana-pro-prompts?id=4729
**Chosen headline:** "Vibes ≠ Disclosure"
**Variant A ref:** `fullbody-pointing-right.png`
**Variant B ref:** `headshot-smirk.png`
**Ref substitutions:** none (all picked refs present in library).

---

## Variant A — wide editorial composition (revised, stronger art direction)

```
Use the attached reference image as the character reference. Match the character's facial features, hair, hat (plaid bucket cap with red DICKIES brand patch — preserve this patch exactly, NO Supreme or other brand substitutions), glasses, beard, wardrobe, and illustrated-portrait style exactly.

REFERENCE IMAGE TO ATTACH: ~/Pictures/tcn-justin-references/fullbody-pointing-right.png

STYLE REGISTER: Editorial magazine illustration in the visual register of Brian Stauffer, Yann Legendre, or Tom Bachtell. Soft semi-realistic shading with visible illustrative brushwork, paper texture grain across the canvas, deliberate warm/cool color temperature variation. NOT flat vector. NOT photoreal. NOT explainer-cartoon.

COMPOSITION:
- LEFT 25-30% of frame: the illustrated character standing in three-quarter angle, pointing across the frame to his right. Eyes follow his own pointing finger — he is NOT looking at the camera. Eyebrows slightly raised in amused-incredulity, mouth in a closed-lipped half-smile (sardonic, not friendly, NO teeth showing). The pointing arm extends across an invisible vertical seam at ~30% frame width.
- RIGHT 60-65% of frame: a thick BOUND LEGAL DOCUMENT — explicitly a Franchise Disclosure Document. ~200 pages thick. Beige hardback cover. Lying OPEN on a desk with visible page-stack thickness perceptible from the side. The binder occupies ~50% of frame height and DOMINATES this side of the composition with weight, scale, and regulatory authority.
- IMMEDIATE FOREGROUND, in front of and DWARFED by the binder: a small consumer-grade hotspot device (white plastic box with short antenna), no larger than a coffee mug. The hotspot is trivially small against the legal tome behind it.
- The SCALE CONTRAST between the binder (massive, regulatory, authoritative) and the hotspot (tiny, trivial, unremarkable) is the rhetorical engine of the composition. The viewer must feel "this versus that" instantly.
- Vertical 5-10% transition zone in the middle — NOT a hard color block seam. Let lighting and scene flow across.

LIGHTING:
- Key light from upper-left in cool fluorescent blue-grey (regulatory office register).
- Warm consumer-amber bounce light from lower-right (the hotspot's misleadingly cozy product-photography light).
- Subtle rim light along the cap brim separating Justin from the background.
- Visible cast shadows from the binder onto the desk, grounding the scale.

MOOD: Investigative, archival, dryly sardonic. The figure carries "let me show you something" energy — restrained, amused-not-alarmed. Reading-the-receipts register. NOT alarm-bell. NOT shocked. NOT cartoonish.

WARDROBE: Red beard, blue square-frame glasses, plaid bucket cap with red DICKIES brand patch (preserve exactly), olive-grey t-shirt, dark jeans, grey sneakers.

ASPECT RATIO: 16:9 (1280×720).

COMPOSITION RULES: Center 80% of frame un-busy enough that headline text overlays cleanly center-left at ~55% canvas height, identity-block elements in top-right corner.

EXCLUDE: text, words, typography anywhere in the image (including on the binder cover), signs, watermarks, logos, captions, lettering — text will be added in post. No second human figure. No flat color blocks. No literal 50/50 vertical split.
```

---

## Variant B — tight close-up composition (revised, stronger art direction)

```
Use the attached reference image as the character reference. Match the character's facial features, hair, hat (plaid bucket cap with red DICKIES brand patch — preserve this patch exactly, NO Supreme or other brand substitutions), glasses, beard, wardrobe, and illustrated-portrait style exactly. CRITICAL: match the smirk expression in the reference image precisely — closed-lipped half-smile, one eyebrow slightly raised, sardonic-amused register. Do NOT render a warm friendly smile with teeth showing. The smirk is restrained, knowing, slightly conspiratorial — not friendly.

REFERENCE IMAGE TO ATTACH: ~/Pictures/tcn-justin-references/headshot-smirk.png

STYLE REGISTER: Editorial magazine illustration portrait in the visual register of Brian Stauffer, Yann Legendre, or Tom Bachtell. Soft semi-realistic shading with visible illustrative brushwork, paper texture grain across the canvas. NOT flat vector. NOT photoreal. NOT explainer-cartoon.

COMPOSITION:
- Close-up of the character from the upper-chest up.
- Head right-aligned, occupying the right 35-45% of the frame width. Face turned slightly toward camera-left, gaze toward camera with eyebrow quirk.
- The collar of his olive-grey t-shirt is visible at the bottom of the frame; the cap fills the upper portion of the head.
- Generous negative space on the LEFT 50% of the frame reserved for headline overlay.

BACKGROUND: A soft, heavily-blurred gradient color field transitioning from cool blue-grey on the left to warm amber on the right. The transition is GRADUAL and DIFFUSE — NO hard vertical seam, NO recognizable architectural shapes, NO blurred buildings, NO blurred scene context of any kind. Think a heavily gaussian-blurred field of pure color, blur intensity high enough that any underlying shapes are completely unrecognizable. Mood color field ONLY.

LIGHTING:
- Key light from camera-right warming the right side of Justin's face.
- Cool fill from camera-left bringing the left side of the face into subtle shadow.
- Subtle rim light along the top edge of the cap brim separating the figure from background.
- Editorial portrait register — soft but DIRECTIONAL, not flat.

MOOD: Sardonic, restrained, "let me show you something." The figure is amused this needs explaining. NOT alarmed. NOT warm-friendly. NOT smiling-broadly. The smirk + raised eyebrow does the rhetorical work — the expression IS the entire content of the composition.

WARDROBE: Red beard, blue square-frame glasses, plaid bucket cap with red DICKIES brand patch (preserve exactly), olive-grey t-shirt.

ASPECT RATIO: 16:9 (1280×720).

COMPOSITION RULES: Face right-aligned, occupying right 35-45% of frame width. Left 50% as soft-blurred negative-space color field for overlay. Center 80% un-busy.

EXCLUDE: text, words, typography, signs, watermarks, logos, captions, lettering. No full-body shots. No multiple figures. No hard color block backgrounds. No teeth-visible smile. No specific architectural or scene context in the background blur.
```

---

## Per-tool quirks (pick the one matching your render tool)

### Nano Banana 2 / Gemini Imagen
Upload the picked reference image first, then paste the prompt. If using your trained `@oj` character, append `Seed: 8472` to the prompt.

### Freepik / Pikaso / Mystic
Paste the prompt into the image-generation field. Attach the picked reference image via the "character reference" or "Pikaso character" feature. Set aspect to 16:9.

### Midjourney
Append `--cref <path-or-url-to-picked-ref> --cw 100 --ar 16:9` to the prompt. The character-reference instruction at the start of the prompt becomes redundant with `--cref` — trim if desired.

### Flux Kontext
Set the picked reference image as the input image. Set denoise strength to ~0.7 so character is preserved but scene is regenerated.

---

## Text overlay spec

**Canvas:** 1280 × 720 (16:9). Center-80% safe zone.

**Headline:**
- Text: `Vibes ≠ Disclosure`
- Font: Courier Prime Bold, sentence case
- Size: 120 px
- **Critical typography note for the `≠` glyph:** The slash through `≠` must use a visibly heavy weight — thicker than Courier Prime's default. At YouTube's mobile-feed thumbnail compression the thin slash can blur into the equals sign, which would invert the headline's meaning catastrophically (`Vibes = Disclosure` is the opposite argument). At composite time: either set the slash to ≥ 2× the cross-bar weight, or compose `≠` as `=` plus a manual diagonal stroke at sufficient weight. Verify legibility at 240 px-wide preview (approximate mobile-feed display size) before publishing.
- Color: slate-400 `#557FA3` (recommended for the split-screen vibe's mid-light range; black `#0D0D0F` also valid if the rendered image leans bright)
- Stroke: 4 px black at 60% opacity recommended — the split-lighting creates variable backgrounds across the two halves of the frame; stroke ensures legibility on both
- Position: center-left, baseline at 55% canvas height (~396 px from top), left edge at 128 px
- Max width: 768 px. Should comfortably fit on one line — 3 glyphs (2 words + symbol) at 120 px ≈ ~450 px width.

**Corner identity block (top-right):**
- Mark.svg: 40 × 40 px, color slate-400 `#557FA3`
- Dispatch serial: `DISPATCH №004`, Courier Prime Regular, 24 px, all-caps, tracking 0.18em, color slate-400 `#557FA3`
- Both right-aligned at right edge 1184 px (96 px inset from canvas right), mark top at 72 px, 8 px gap between mark and serial

**Palette restriction:** slate-400 `#557FA3`, slate-600 `#3A6A8F`, black `#0D0D0F`, twilight `#485070`. No other colors on overlay text. The illustrated scene beneath the overlay is NOT restricted to this palette.

---

## Render gate

Suppressed — running in reference-image mode. The skill does not know which image-generation tool you will use, so it does not auto-render. Pick a tool from the per-tool quirks block, attach the picked reference image, paste the prompt, and render manually. Two PNG outputs expected (Variant A and Variant B at 1280×720). After rendering, composite the text overlay per the spec above in Figma/Canva/Photoshop.

---

## Selection rationale (for future reference)

**Why these refs:**
- **Variant A → `fullbody-pointing-right.png`** because the chosen Political Split Screen vibe has a directional contrast (left side vs right side) and the dispatch concept is "look at what's missing." Justin pointing right anchors the viewer's eye to the empty space where the franchise binder should be. Coherence with Variant B: both refs carry the same "let me show you something" register.
- **Variant B → `headshot-smirk.png`** because the dispatch tone is sardonic understatement, not alarm-bell. The narration's load-bearing line ("Nobody overrode it.") and the cold-open's one-word punchline ("Vibes.") both lean restrained — the figure is amused this needs explaining, not concerned. `headshot-concerned` would over-rotate the tone toward alarm.

**Why this headline:**
- "Vibes ≠ Disclosure" compresses the cold-open's rhetorical contrast into 3 word-equivalents using math notation as a brand-coherent glyph. TCN reads receipts — math notation in the thumbnail says "this is analysis" before the viewer has read a single word. Maximum visual stop-power at scroll speed.

**Why this vibe:**
- Political Split Screen (id=4729) was picked from 3 surfaced candidates. It was the cleanest match to the dispatch's structural argument (two-sided contrast, character-driven, thumbnail-shaped). The other two candidates (Documentary Style 2×2 grid, VFX Before/After) were either too busy for thumbnail use or tonally mismatched with TCN's illustrated-editorial register.
