# Color palette & brand style

**This is the single source of truth for all colors, brand style, and render defaults.** To customize diagrams to your brand, edit this file — everything else in the skill is universal.

> Applying a **customer brand guide** (e.g. a `*-DESIGN.md`)? Don't rewrite the structure — see [**Brand override**](#brand-override--applying-a-customer-brand-guide) at the bottom. The roles/bands/defaults below are the fixed template; a brand only swaps the hex values in the slots it defines.

---

## Global render defaults

These defaults apply to EVERY element unless explicitly overridden.

| Property | Value | Note |
|----------|-------|------|
| `roughness` | `2` | Hand-drawn, sketchy look — the signature style |
| `fontFamily` | `1` | Excalifont/Virgil — handwriting font (use `3` monospace only for code/data evidence) |
| `fillStyle` | `hachure` | Sketchy fill for shapes. Use `solid` for layer bands and evidence panels |
| `strokeWidth` | `2` | Standard for shapes and arrows |

**Why hand-drawn?** This style makes diagrams feel approachable, informal, and easy to absorb — like whiteboard sketches. It's Excalidraw's native aesthetic.

---

## Shape colors (semantic)

Color encodes meaning, not decoration. Each semantic purpose has a fill/stroke pair.

| Semantic purpose | Fill | Stroke |
|------------------|------|--------|
| Primary/Neutral | `#3b82f6` | `#1e3a5f` |
| Secondary | `#60a5fa` | `#1e3a5f` |
| Tertiary | `#93c5fd` | `#1e3a5f` |
| Start/Trigger | `#fed7aa` | `#c2410c` |
| End/Success | `#a7f3d0` | `#047857` |
| Warning/Reset | `#fee2e2` | `#dc2626` |
| Decision | `#fef3c7` | `#b45309` |
| AI/LLM | `#ddd6fe` | `#6d28d9` |
| Inactive/Disabled | `#dbeafe` | `#1e40af` (use a dashed stroke) |
| Error | `#fecaca` | `#b91c1c` |

**Rule**: always pair a darker stroke with a lighter fill for contrast.

---

## Layer band colors (for layered/pipeline diagrams)

Use these light pastel fills with `fillStyle: "solid"` for full-width background bands that group related elements into visual layers.

| Layer purpose | Fill | Stroke |
|---------------|------|--------|
| Layer 1 (Input/Intake) | `#a8d8ea` | `#5b9bd5` |
| Layer 2 (Buffer/Processing) | `#fef3c7` | `#d4a843` |
| Layer 3 (Decision/Routing) | `#fecaca` | `#e06666` |
| Layer 4 (Queue/Scheduling) | `#a7f3d0` | `#6aa84f` |
| Layer 5 (Execution/Output) | `#ddd6fe` | `#8e7cc3` |
| Layer 6+ (Additional) | `#fce4ec` | `#c27ba0` |

**Usage**: create a wide rectangle spanning the diagram width, with `fillStyle: "solid"` and `roughness: 2`. Place the layer's content on top.

---

## Text colors (hierarchy)

Use color on free-floating text to create visual hierarchy without containers.

| Level | Color | Used for |
|-------|-------|----------|
| Title | `#1e40af` | Section titles, primary labels |
| Subtitle | `#3b82f6` | Sub-headings, secondary labels |
| Body/Detail | `#64748b` | Descriptions, captions, metadata |
| On light fills | `#374151` | Text inside light-colored shapes |
| On dark fills | `#ffffff` | Text inside **solid** dark-colored shapes |

> **Hachure caveat**: a `hachure` fill is visually *light* (mostly white with sketchy diagonal lines), even when the fill color is a saturated blue. So text inside a `hachure` shape must be **dark** (`#374151` or the shape's stroke color) — white text becomes invisible. Reserve white text for `fillStyle: "solid"` dark panels (evidence, dark layer bands).

---

## Evidence artifact colors

Use for code snippets, data examples, and other concrete evidence inside technical diagrams.

| Evidence | Background | Text color |
|----------|------------|------------|
| Code snippet | `#1e293b` | Syntax-colored (match the language) |
| JSON/data example | `#1e293b` | `#22c55e` (green) |

---

## Default border & line colors

| Element | Color |
|---------|-------|
| Arrow | Use the source element's semantic stroke color |
| Structural line (divider, tree, timeline) | Primary stroke (`#1e3a5f`) or Slate (`#64748b`) |
| Marker dot (fill + stroke) | Primary fill (`#3b82f6`) |

---

## Background

| Property | Value |
|----------|-------|
| Canvas background | `#ffffff` |

---

## Brand override — applying a customer brand guide

This file is the **structural template**: the semantic roles, layer bands, and render defaults above are universal and stay fixed. A customer brand guide does NOT replace this structure — it only **fills the brand-relevant slots with the brand's real colors**. Slots the brand doesn't define keep their defaults or are derived. **Never leave a slot empty.**

**Two ways to apply a brand:**
- **Permanent** — edit the hex values in the tables above directly (the skill always reads this file). Best when every diagram is for one brand.
- **Per-job** — a brand guide is supplied as input (e.g. `input/brand-style-guide/<brand>-DESIGN.md`). Map it on the fly for that diagram; do NOT overwrite the defaults here.

### Mapping table (brand guide → semantic slot)

| A brand guide usually provides | Maps to slot | If the brand lacks it |
|---|---|---|
| Primary / brand color | Primary (fill + stroke) | always present |
| Success / positive (green) | End/Success | derive: a green tint |
| Error / alert / destructive (red) | Error, Warning/Reset | derive: a red tint |
| Heading / body / label neutrals | Text hierarchy (title / subtitle / body) | use defaults |
| Secondary / accent colors | Secondary, Tertiary | tint/shade of Primary |
| *(rarely defined)* **Start/Trigger · Decision · AI/LLM** | those slots | **derive from Primary** (analogous hues) or keep defaults |
| *(rarely defined)* **6 layer-band pastels** | layer bands | keep default pastels, or tint Primary at ~15% |

> Reality: a typical brand defines ~30–40% of the slots (primary, success, error, neutrals). The rest you derive or keep — see below.

### Precedence — the "overlap" rule
1. A color the brand **explicitly defines** → overrides the default in its matching slot.
2. A slot the brand **does not define** → keep the default, or derive a tint/shade of the brand Primary so it still reads on-brand.
3. The **structure never changes** — same slots, same role names, same band count. Only hex values move. No structural conflict is possible because the brand never adds or removes roles.

### Deriving missing slots
- Lighter fills: brand color mixed with white at ~20–25%. Darker strokes: brand color darkened ~30%.
- Always pair a darker stroke with a lighter fill (keeps the contrast rule).
- Keep roles **visually distinct**: Start, Decision, Error, AI must stay distinguishable. If the brand is near-monochrome, vary lightness/saturation instead of collapsing them into one hue.

### Ignore these parts of a brand guide (no Excalidraw equivalent)
- **Fonts** — the renderer only supports `fontFamily: 1` (handwriting) and `3` (monospace). Brand fonts (sohne-var, BMW Type, etc.) cannot render. Borrow only the size/weight **hierarchy** and map it to title / subtitle / body sizes.
- **Shadows, border-radius scales, spacing systems, responsive breakpoints, motion** — none apply to a static hand-drawn diagram.

### Aesthetic match (roughness & fill style)
The default hand-drawn look (`roughness: 2`, `fillStyle: hachure`) suits informal / whiteboard diagrams. For **precise / premium brands** (fintech, automotive, enterprise — e.g. Stripe, BMW, IBM) switch to `roughness: 0` + `fillStyle: solid` for crisp, on-brand edges. For **friendly / playful brands**, keep the hand-drawn defaults. This is the one place a brand may "override" the skill's default *aesthetic*, not just its colors.
