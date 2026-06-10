# Arrow binding — the single most important technical rule

> Arrows that don't *bind* to their boxes are the #1 defect in AI-generated Excalidraw
> files. The file opens looking fine, but the moment a box is dragged the arrow detaches,
> and the arrow length/position looks wrong on reopen. **Read this whole file before
> drawing any diagram that has arrows.** Then verify with `check_bindings.py` (below).

## Why arrows detach: binding is TWO-WAY

Excalidraw stores a connection in **two places**, and both must agree:

1. On the **arrow** — `startBinding` / `endBinding`, each pointing at a box via `elementId`.
2. On **each box** — a back-reference to the arrow inside the box's `boundElements` array.

The classic AI mistake is writing only direction 1: the arrow names its boxes, but the
boxes never name the arrow back. With only one direction, Excalidraw draws the arrow at
the literal `points` coordinates (so a freshly opened file *looks* connected), but it has
no live link — drag the box and the arrow stays behind. **Both directions are mandatory.**

```
   ┌─ arrow.startBinding.elementId ─►┐        ┌─◄ arrow.endBinding.elementId ─┐
 [ BOX A ]                          [ ARROW ]                          [ BOX B ]
   └◄─ A.boundElements: [arrow] ────┘        └──── B.boundElements: [arrow] ─►┘
        (the half everyone forgets)               (the half everyone forgets)
```

## The 4 fields every connection needs

For an arrow `arrow_a_b` connecting box `A` → box `B`:

| Where | Field | Value |
|-------|-------|-------|
| arrow | `startBinding` | `{ "elementId": "A", "focus": 0, "gap": 4 }` |
| arrow | `endBinding` | `{ "elementId": "B", "focus": 0, "gap": 4 }` |
| **box A** | `boundElements` | must **contain** `{ "id": "arrow_a_b", "type": "arrow" }` |
| **box B** | `boundElements` | must **contain** `{ "id": "arrow_a_b", "type": "arrow" }` |

If a box already has bound text, **append** the arrow — don't overwrite:
`"boundElements": [{ "id": "A_text", "type": "text" }, { "id": "arrow_a_b", "type": "arrow" }]`

### Field meanings

- **`focus`** — normalized `−1..1`, where the arrow aims on the box's edge. `0` = center.
  Positive/negative shifts the attachment point toward one side. Use non-zero values to
  fan several arrows out of different points on the same box (see Fan-out below).
- **`gap`** — pixels of breathing room kept between the arrowhead and the box edge.
  `4–8` looks clean; the examples use `2`. Keep it small and consistent.

## Geometry: where to put the arrow's `x`, `y`, and `points`

Excalidraw recomputes arrow geometry live **only when a bound box is dragged**. On file
open it draws the arrow exactly at its stored `points`. So the stored geometry must
already match the binding, or the first view looks broken. The rule:

> **Place the arrow's start point on the source box's edge and its end point on the
> target box's edge.** `points` are relative to the arrow's own `x,y`.

Concrete recipe for a **vertical** arrow A (above) → B (below), both centered on x≈`cx`:

```
arrow.x = cx
arrow.y = A.y + A.height + gap          # just below A's bottom edge
endY    = B.y - gap                      # just above B's top edge
arrow.points = [[0, 0], [0, endY - arrow.y]]
arrow.width  = 0
arrow.height = endY - arrow.y
```

For a **horizontal** arrow A (left) → B (right), both centered on y≈`cy`:

```
arrow.x = A.x + A.width + gap            # just right of A's right edge
arrow.y = cy
endX    = B.x - gap                      # just left of B's left edge
arrow.points = [[0, 0], [endX - arrow.x, 0]]
arrow.width  = endX - arrow.x
arrow.height = 0
```

`points` always starts at `[0,0]` (the arrow's own origin) and the last point is the
displacement to the far end. For curved/routed arrows, insert waypoints between them
(see "Routing" below).

## Worked example — 1→1 (vertical)

`start_ellipse` (x=360, y=60, w=200, h=70) → `step1` (x=310, y=180, w=300, h=80),
both centered on x=460. Bottom of ellipse = 130; top of step1 = 180; gap = 2.

```json
{
  "id": "start_ellipse", "type": "ellipse",
  "x": 360, "y": 60, "width": 200, "height": 70,
  "boundElements": [
    { "id": "start_text", "type": "text" },
    { "id": "a1", "type": "arrow" }
  ]
},
{
  "id": "step1", "type": "rectangle",
  "x": 310, "y": 180, "width": 300, "height": 80,
  "boundElements": [
    { "id": "step1_text", "type": "text" },
    { "id": "a1", "type": "arrow" }
  ]
},
{
  "id": "a1", "type": "arrow",
  "x": 460, "y": 132, "width": 0, "height": 46,
  "points": [[0, 0], [0, 46]],
  "startBinding": { "elementId": "start_ellipse", "focus": 0, "gap": 2 },
  "endBinding":   { "elementId": "step1", "focus": 0, "gap": 2 },
  "startArrowhead": null, "endArrowhead": "arrow"
}
```

## Worked example — fan-out (1 → many)

**There is no "branching arrow."** One box pointing at three boxes is **three separate
arrow elements**. Excalidraw has no multi-headed arrow.

Consequence for binding: the **source box is shared**, so its `boundElements` must list
**all three** arrows. Each target box lists only its own arrow.

```json
{
  "id": "box1", "type": "rectangle",
  "x": 100, "y": 200, "width": 160, "height": 60,
  "boundElements": [
    { "id": "arrow_1_2", "type": "arrow" },
    { "id": "arrow_1_3", "type": "arrow" },
    { "id": "arrow_1_4", "type": "arrow" }
  ]
},
{ "id": "box2", "type": "rectangle", "x": 400, "y": 80,  "width": 160, "height": 60,
  "boundElements": [{ "id": "arrow_1_2", "type": "arrow" }] },
{ "id": "box3", "type": "rectangle", "x": 400, "y": 200, "width": 160, "height": 60,
  "boundElements": [{ "id": "arrow_1_3", "type": "arrow" }] },
{ "id": "box4", "type": "rectangle", "x": 400, "y": 320, "width": 160, "height": 60,
  "boundElements": [{ "id": "arrow_1_4", "type": "arrow" }] },

{ "id": "arrow_1_2", "type": "arrow",
  "x": 264, "y": 230, "width": 136, "height": -120, "points": [[0,0],[136,-120]],
  "startBinding": { "elementId": "box1", "focus": 0.4,  "gap": 4 },
  "endBinding":   { "elementId": "box2", "focus": 0,    "gap": 4 },
  "startArrowhead": null, "endArrowhead": "arrow" },
{ "id": "arrow_1_3", "type": "arrow",
  "x": 264, "y": 230, "width": 136, "height": 0, "points": [[0,0],[136,0]],
  "startBinding": { "elementId": "box1", "focus": 0,    "gap": 4 },
  "endBinding":   { "elementId": "box3", "focus": 0,    "gap": 4 },
  "startArrowhead": null, "endArrowhead": "arrow" },
{ "id": "arrow_1_4", "type": "arrow",
  "x": 264, "y": 230, "width": 136, "height": 120, "points": [[0,0],[136,120]],
  "startBinding": { "elementId": "box1", "focus": -0.4, "gap": 4 },
  "endBinding":   { "elementId": "box4", "focus": 0,    "gap": 4 },
  "startArrowhead": null, "endArrowhead": "arrow" }
```

Fan-out tips:
- **Stagger `focus` at the source** (e.g. `0.4 / 0 / −0.4`) so the arrows leave from
  different points along box1's edge — it reads like a branching tree instead of three
  lines crammed into one spot. Target ends stay at `focus: 0` (into center).
- **`points` of each arrow must aim at its real target** (up / level / down), relative to
  that arrow's own `x,y`.
- **Unique arrow ids** — name them `arrow_{from}_{to}`. Reusing an id silently corrupts
  binding. This is the most common fatal slip when fanning out.

## Convergence (many → 1)

The mirror image: the **target box is shared**, so its `boundElements` lists every
incoming arrow; each source box lists only its outgoing one. Same rules, reversed.

## Labels on boxes (text binding)

A box's text label is bound the same two-way way, with `type: "text"`:
- The text element has `containerId` pointing at the box.
- The box's `boundElements` contains `{ "id": "<text id>", "type": "text" }`.

So a box that has both a label and an arrow lists **both** in `boundElements`. Excalidraw
re-centers bound text automatically, so the text's `x,y` is just a starting estimate.

## Routing around obstacles

To bend an arrow around an element, add waypoints to `points` (3+ points). The first is
always `[0,0]` and the last is the far endpoint; middle points are intermediate bends,
all relative to the arrow's `x,y`. Binding still works — keep both bindings and both
back-refs. Use this for No-branches that must not cross the main column and for loop-back
arrows routed out to the margin.

## Optional self-check

The rule above is what matters — bind both ways **as you write each arrow** and you won't
have a problem. If you want a quick sanity check on a finished file (especially a large
fan-out or a multi-region diagram where it's easy to miss a back-reference), you *can* run
the linter **once**:

```bash
cd .claude/skills/diagram/references && uv run python check_bindings.py <path-to-file.excalidraw>
```

It reports every arrow whose binding is missing its box back-reference, every dangling
`elementId`, and every arrow with no binding at all. This is a single, cheap, deterministic
pass — not something to loop on, and not part of the mandatory render cycle. Treat it as an
optional verification, not a gate.

## Common mistakes → fixes

| Symptom | Cause | Fix |
|---------|-------|-----|
| Drag a box, arrow stays behind | Box `boundElements` missing the arrow back-ref | Add `{id: arrowId, type:"arrow"}` to **both** boxes |
| Arrow looks right on open but "snaps" weirdly later | Only one binding direction present | Add the missing back-ref(s) |
| Fan-out: dragging source drops one branch | Source `boundElements` lists only some arrows | List **all** outgoing arrows on the source box |
| Arrow points into empty space | `points` don't match the bound boxes' positions | Recompute `x,y,points` from the box edges (geometry recipe) |
| Two arrows behave as one | Duplicate arrow `id` | Give every arrow a unique `arrow_{from}_{to}` id |
| Lint flags a dangling `elementId` | Arrow binds to an id that doesn't exist | Fix the typo or create the missing box |
