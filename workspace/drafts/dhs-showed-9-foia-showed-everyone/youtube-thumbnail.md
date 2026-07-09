# Thumbnail prompts — TCN Dispatch №007

**Mode:** reference-image
**Generated:** 2026-06-11
**Vibe reference:** "Political Split Screen — figure pointing across at a contrasting scene" (YouMind library id 4729) · https://youmind.com/nano-banana-pro-prompts?id=4729
**Chosen headline:** "DHS showed you 9%"
**Ref picks:** Variant A → `fullbody-pointing-right.png` · Variant B → `headshot-stern.png` (no substitutions; both present in refs dir)
**Cold-open source:** transcript (`dispatch-007_en.srt`)

> Note: vibe is borrowed for composition + register only. The library sample carries in-image yellow text and named politicians; both are discarded. TCN renders no in-image text (overlay-only) and substitutes illustrated-Justin. Register dialed down from saturated political-thumbnail to sober investigative (two dead citizens — saturation would read as disrespectful).

---

## Variant A — wide editorial composition

```
Use the attached reference image as the character reference. Match the character's facial features, hair, hat, glasses, beard, wardrobe, and illustrated-portrait style exactly. Place the same character into a new scene as described below.

REFERENCE IMAGE TO ATTACH: fullbody-pointing-right.png

STYLE REGISTER: Editorial magazine illustration in the visual register of Brian Stauffer, Yann Legendre, or Tom Bachtell. Soft semi-realistic shading with visible illustrative brushwork, paper texture grain across the canvas, deliberate cool/warm color temperature variation. NOT flat vector. NOT photoreal. NOT explainer-cartoon.

COMPOSITION:
- LEFT 25-30% of frame: the illustrated character, three-quarter angle, arm extended pointing across the frame to the right at the scene. Eyes follow his own pointing hand toward the right side. Eyebrows level and slightly lowered, sober and unimpressed — NOT amused, NOT alarmed. Mouth set in a flat, serious line, NOT a friendly grin. He is presenting damning evidence, not accusing the camera. NOT looking at camera.
- RIGHT 60-65% of frame: a vast crowd of faded, desaturated human figures receding into cold grey-blue haze — hundreds of indistinct people, the scale reading as a multitude (the 3,789 arrested). At the FRONT of the crowd, a single small tightly-lit cluster of about a dozen figures glows brighter and sharper, isolated from the dark mass behind them (the small published "9%"). The size contrast is the rhetorical engine: the lit cluster is tiny; the dark crowd dwarfs it and fills the depth of the frame. Cold institutional fluorescent lighting over the crowd. NO recognizable faces, NO text or signage anywhere.
- Vertical 5-10% transition zone in the middle — NOT a hard color block seam. Let the cold light and haze flow across the divide.

LIGHTING:
- Key light from upper-left in cool fluorescent blue-grey, falling on the character.
- The crowd side colder and more desaturated; the small front cluster lit a half-step warmer so it separates from the dark mass.
- Subtle rim light along the top edge of the cap brim separating the figure from the background.
- Faint cast shadows under the front cluster to ground its scale.

MOOD: investigative, documentary, quiet-dread. Grave-not-sensational — the register of a sober accountability report, not a rage-bait reaction. NOT alarm-bell. NOT cartoonish. NOT saturated political-thumbnail color.

Match the reference image's character: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red DICKIES brand patch (preserve this patch exactly — NO Supreme or other brand substitutions), olive-grey t-shirt, dark jeans, grey sneakers. Match the illustrated-portrait style — soft semi-realistic shading, illustrated editorial register, not photoreal, not flat-vector. Keep facial features and proportions consistent with the reference.

ASPECT RATIO: 16:9 (1280×720).

COMPOSITION RULES: Center 80% of frame un-busy enough that headline text overlays cleanly center-left at ~55% canvas height, identity-block elements in top-right corner. Keep the dark crowd's densest detail to the outer-right and lower-right so the center-left stays open for text.

EXCLUDE: text, words, typography anywhere in the image (including on objects, signs, screens, or labels), watermarks, logos, captions, lettering — text will be added in post. No second prominent human figure beside the main character. No flat color blocks. No literal 50/50 vertical split.
```

## Variant B — tight close-up composition

```
Use the attached reference image as the character reference. Match the character's facial features, hair, hat, glasses, beard, wardrobe, and illustrated-portrait style exactly. Place the same character into a new scene as described below.

REFERENCE IMAGE TO ATTACH: headshot-stern.png

CRITICAL EXPRESSION DIRECTIVE — match the chosen ref's expression precisely. For headshot-stern.png: brow lowered, mouth tight, no smile. Do NOT add any warmth or hint of amusement — this is the unimpressed, "the data is damning" register. The figure is grave and composed, not shocked.

STYLE REGISTER: Editorial magazine illustration portrait in the visual register of Brian Stauffer, Yann Legendre, or Tom Bachtell. Soft semi-realistic shading with visible illustrative brushwork, paper texture grain across the canvas. NOT flat vector. NOT photoreal. NOT explainer-cartoon.

COMPOSITION:
- Close-up of the character from the upper-chest up.
- Head right-aligned, occupying the right 35-45% of the frame width. Face turned slightly toward camera-left, gaze level and direct, fixed off-camera-left as if meeting the viewer's question.
- The collar of the olive-grey t-shirt is visible at the bottom of the frame; the cap fills the upper portion of the head.
- Generous negative space on the LEFT 50% of the frame reserved for headline overlay.

BACKGROUND: a heavily gaussian-blurred field of cold institutional blue-grey, deepening to near-black at the lower-left. The transition is GRADUAL and DIFFUSE — NO hard vertical seam, NO recognizable architectural shapes, NO blurred buildings, NO blurred crowd, NO scene context of any kind. Mood color field ONLY — a pure heavily-blurred wash of cold grey-blue, not a blurred scene with shapes.

LIGHTING:
- Key light from camera-right in cool blue-grey, warming the right side of the face only slightly.
- Cooler fill from the left bringing the left side of the face into subtle shadow.
- Subtle rim light along the top edge of the cap brim separating the figure from the background.
- Editorial portrait register — soft but DIRECTIONAL, not flat.

MOOD: investigative, sober, grave. Restrained, unimpressed, "look at what their own data says." NOT alarm-bell. NOT warm-friendly. NOT saturated.

Match the reference image's character: salt-and-pepper brown beard, blue square-frame glasses, plaid bucket cap with red DICKIES brand patch (preserve this patch exactly — NO Supreme or other brand substitutions), olive-grey t-shirt, dark jeans, grey sneakers. Match the illustrated-portrait style — soft semi-realistic shading, illustrated editorial register, not photoreal, not flat-vector. Keep facial features and proportions consistent with the reference.

ASPECT RATIO: 16:9 (1280×720).

COMPOSITION RULES: Face right-aligned, occupying right 35-45% of frame width. Left 50% as soft-blurred negative-space color field for overlay. Center 80% un-busy.

EXCLUDE: text, words, typography, signs, watermarks, logos, captions, lettering. No full-body shots. No multiple figures. No hard color block backgrounds. No teeth-visible smile. No specific architectural or scene context in the background blur.
```

---

## Text overlay spec

**Canvas:** 1280 × 720 (16:9). Center-80% safe zone (text within 128–1152 px horizontal, 72–648 px vertical).

**Headline:**
- Text: "DHS showed you 9%"
- Font: Courier Prime Bold, sentence case (TCN never screams in all-caps)
- Size: 120 px at 1280×720
- Tracking: -0.025em
- Color: slate-400 `#557FA3` fill with a 4 px black `#0D0D0F` stroke at 60% opacity (recommended — Variant A's split-screen / mixed cool-lighting scene needs the stroke for legibility, treatment Option B). If compositing Variant B (uniform blurred color field), drop the stroke and use flat slate-400 (Option A).
- Position: center-left, baseline at ~55% canvas height (~396 px from top), left edge at 128 px. For Variant A (figure occupies left 25–30%), drop the baseline to ~62% height and/or nudge right so the headline clears the figure and sits over the lower crowd haze; keep it inside the center-80% safe zone.
- Max width 768 px; 4 words should hold on one line, wrap to 2 if needed, never 3.

**Corner identity block (top-right):**
- Mark.svg: 40×40 px, slate-400 `#557FA3`
- Dispatch serial: "DISPATCH №007", Courier Prime Regular, 24 px, all-caps, tracking 0.18em, slate-400 `#557FA3`
- Both right-aligned at right edge 1184 px (96 px inset), mark top at 72 px, serial 8 px below the mark

**Palette:** slate-400 `#557FA3`, slate-600 `#3A6A8F`, black `#0D0D0F`, twilight `#485070`. No other colors on overlay text.

**Mobile safe-zone note:** All text must stay inside the center 80% of the canvas. YouTube crops mobile feed thumbnails aggressively at the edges.

---

## Per-tool rendering notes

Reference-image mode is model-agnostic — paste a variant prompt into your tool and attach the named ref file. Use whichever block matches your tool:

- **Freepik / Pikaso / Mystic:** paste the prompt; attach the ref via the "character reference" / Pikaso character feature; set aspect 16:9.
- **Nano Banana 2 / Gemini:** upload the ref first, then paste the prompt. (No fixed seed configured at `~/.config/tcn/illustrated-justin-seed` — no seed line appended.)
- **Midjourney:** append `--cref <ref-image-URL> --ar 16:9 --cw 100`; the character-reference sentence at the top becomes redundant with `--cref` (keep or trim).
- **Flux Kontext (image-to-image):** set the ref as the input image, denoise ~0.7; keep the wardrobe/style directive as the prompt body.

Overlay assets (mark.svg, Courier Prime) live in `~/Documents/The Civic Node — Design System.zip`.
