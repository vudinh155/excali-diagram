# Rendering & verification

You cannot judge a diagram from JSON alone. After creating or editing Excalidraw JSON, you MUST render it to PNG, look at the image, and fix what you see — in a loop until it's right. This is a core part of the process, not a final check.

---

## Large-diagram strategy — build region by region

**For comprehensive or technical diagrams, you MUST build the JSON one region at a time.** Do NOT try to emit the whole file in one response. This is a hard constraint — output is capped at ~32k tokens per response, and a comprehensive diagram easily exceeds that, producing truncated, broken JSON. Even when it fits, region-by-region is better in every way.

### Phase 1 — Build region by region
1. **Create the root file** with the JSON wrapper (`type`, `version`, `appState`, `files`) and the first region's elements.
2. **Add one region per edit.** Give each region its own turn — think carefully about layout, spacing, and how it connects to what already exists.
3. **Use descriptive string IDs** (e.g. `"trigger_rect"`, `"arrow_fan_left"`) so cross-region references are readable.
4. **Namespace seeds per region** (e.g. region 1 = 100xxx, region 2 = 200xxx) to avoid collisions.
5. **Update cross-region bindings as you go (BOTH directions).** When a new region's arrow binds to an earlier box, in the **same edit** add the arrow's `startBinding`/`endBinding` AND append `{"id": "<arrowId>", "type": "arrow"}` to the earlier box's `boundElements`. Forgetting the back-reference on the older box is the most common cross-region binding bug. See [`binding.md`](binding.md).

### Phase 2 — Review the whole
After all regions exist, read through the full JSON and check:
- Are cross-region arrows bound correctly at both ends?
- Is overall spacing balanced, or are some regions cramped while others have too much whitespace?
- Do all IDs and bindings reference elements that actually exist?

Fix any alignment or binding issues before rendering. (For a big fan-out or many regions
where a back-reference is easy to miss, you may optionally run `check_bindings.py` once to
confirm — see [`binding.md`](binding.md).)

### Don'ts
- **Don't generate the whole diagram in one response** — you'll hit the output limit and produce truncated JSON.
- **Don't use a coding agent** to generate JSON — it won't have the skill's rules context.
- **Don't write a Python script to generate JSON** — the indirection makes debugging harder than hand-written JSON with descriptive IDs.

### Region boundaries
Plan regions around natural visual groups. A typical large diagram splits into:
- **Region 1**: Entry / trigger
- **Region 2**: First decision or routing
- **Region 3**: Main content (the focal, often largest single region)
- **Region 4-N**: Remaining phases, outputs, etc.

Each region should be self-contained: its elements, internal arrows, and any cross-references to adjacent regions.

---

> **Bindings**: detached arrows are the #1 defect and you cannot see them in a still PNG —
> a freshly rendered file looks connected even when the back-references are missing. So get
> binding right **while writing the JSON** (the strict rule in [`binding.md`](binding.md)),
> not by re-rendering. If you want to verify a finished file you may optionally run
> `check_bindings.py` once — it is not part of this render loop.

## How to render

```bash
cd .claude/skills/diagram/references && uv run python render_excalidraw.py <path-to-file.excalidraw>
```

This outputs a PNG next to the `.excalidraw` file. Then use the **Read tool** on the PNG to actually look at it.

Options: `--output path.png`, `--scale 2` (device scale factor), `--width 1920` (max viewport width).

---

## The verify loop

After creating the initial JSON, run this cycle:

**1. Render & look** — run the render script, then Read the PNG.

**2. Compare against your original vision** — before hunting for defects, compare the render to what you designed in S0-S4:
- Does the visual structure match the conceptual structure you planned?
- Does each region use the pattern you intended (fan-out, convergence, timeline…)?
- Does the eye flow through the diagram in the order you designed?
- Is the visual hierarchy correct — hero element prominent, supporting elements smaller?
- For technical diagrams: are evidence artifacts (code, data examples) readable and well-placed?

**3. Check for visual defects:**
- Text clipped by or overflowing its container
- Text or shapes overlapping other elements
- Arrows cutting through elements instead of routing around them
- Arrows landing on the wrong element or pointing into empty space
- Floating labels that are ambiguous (not clearly attached to what they describe)
- Uneven spacing between elements that should be evenly spaced
- A region with too much whitespace next to a cramped region
- Text too small to read at render size
- Overall layout feels lopsided or unbalanced

**4. Fix** — edit the JSON. Common fixes:
- Widen a container when text is clipped
- Adjust `x`/`y` to fix spacing and alignment
- Add a waypoint to an arrow's `points` array to route around an element
- Move a label closer to what it describes
- Resize elements to rebalance visual weight between regions

**5. Re-render & re-look** — run the script again and Read the new PNG.

**6. Repeat** — keep iterating until the diagram passes both the vision check (step 2) and the defect check (step 3). Usually 2-4 iterations. Don't stop after one pass just because there are no critical errors — if the layout could be better, improve it.

### When to stop
- The render matches the conceptual design from your planning steps
- No clipped, overlapping, or unreadable text
- Arrows route cleanly and connect the right elements
- Spacing is consistent and the layout is balanced
- You'd be comfortable showing it to someone without apologizing

---

## First-time setup

If the render tooling isn't set up yet:
```bash
cd .claude/skills/diagram/references
uv sync
uv run playwright install chromium
```

## Troubleshooting

| Symptom | Cause / fix |
|---------|-------------|
| `playwright not installed` | Run the first-time setup above. |
| `Chromium not installed` | `uv run playwright install chromium` |
| Render hangs / times out on module load | The template imports `@excalidraw/excalidraw@0.18.0` from esm.sh — needs network on first run; it caches after. Timeout is 120s. |
| `'elements' array is empty` | The JSON has no (non-deleted) elements. |
| `Invalid JSON` | A trailing comma or unclosed bracket — likely a truncated region. Re-emit that region. |
| Text overflows boxes | The handwriting font is wider than expected; shorten labels or widen containers, then re-render. |
| Arrow detaches when a box is dragged | The box's `boundElements` is missing the arrow back-reference. Add `{id, type:"arrow"}` to the box (both ends). See [`binding.md`](binding.md); optionally confirm with `check_bindings.py`. |
