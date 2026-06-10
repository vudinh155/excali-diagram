# Element templates

Copy-paste JSON templates for each Excalidraw element type. The `strokeColor` and `backgroundColor` values are placeholders — always pull real colors from [`color-palette.md`](color-palette.md) based on the element's semantic purpose.

**Global defaults** (from `color-palette.md`): `roughness: 2`, `fontFamily: 1`, `fillStyle: "hachure"`. Every template below uses these defaults.

## Free-floating text (no container)
```json
{
  "type": "text",
  "id": "label1",
  "x": 100, "y": 100,
  "width": 200, "height": 25,
  "text": "Section Title",
  "originalText": "Section Title",
  "fontSize": 20,
  "fontFamily": 1,
  "textAlign": "left",
  "verticalAlign": "top",
  "strokeColor": "<title color from palette>",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 2,
  "opacity": 100,
  "angle": 0,
  "seed": 11111,
  "version": 1,
  "versionNonce": 22222,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false,
  "containerId": null,
  "lineHeight": 1.25
}
```

## Line (structural, not an arrow)
```json
{
  "type": "line",
  "id": "line1",
  "x": 100, "y": 100,
  "width": 0, "height": 200,
  "strokeColor": "<structural line color from palette>",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 2,
  "opacity": 100,
  "angle": 0,
  "seed": 44444,
  "version": 1,
  "versionNonce": 55555,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false,
  "points": [[0, 0], [0, 200]]
}
```

## Small marker dot
```json
{
  "type": "ellipse",
  "id": "dot1",
  "x": 94, "y": 94,
  "width": 12, "height": 12,
  "strokeColor": "<marker dot color from palette>",
  "backgroundColor": "<marker dot color from palette>",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 2,
  "opacity": 100,
  "angle": 0,
  "seed": 66666,
  "version": 1,
  "versionNonce": 77777,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false
}
```

## Rectangle
```json
{
  "type": "rectangle",
  "id": "elem1",
  "x": 100, "y": 100, "width": 180, "height": 90,
  "strokeColor": "<stroke from palette based on semantic purpose>",
  "backgroundColor": "<fill from palette based on semantic purpose>",
  "fillStyle": "hachure",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 2,
  "opacity": 100,
  "angle": 0,
  "seed": 12345,
  "version": 1,
  "versionNonce": 67890,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": [{"id": "text1", "type": "text"}],
  "link": null,
  "locked": false,
  "roundness": {"type": 3}
}
```
**`boundElements` holds every element bound to this box** — its label text AND every arrow
touching it. A box that is the start/end of arrows `a1` and `a2` and holds text `text1`:
`"boundElements": [{"id":"text1","type":"text"},{"id":"a1","type":"arrow"},{"id":"a2","type":"arrow"}]`.
Missing an arrow here = that arrow detaches on drag. (See [`binding.md`](binding.md).)

## Layer band (full-width background for grouping)
```json
{
  "type": "rectangle",
  "id": "layer1",
  "x": 50, "y": 100, "width": 900, "height": 150,
  "strokeColor": "<layer band stroke from palette>",
  "backgroundColor": "<layer band fill from palette>",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 2,
  "opacity": 100,
  "angle": 0,
  "seed": 88888,
  "version": 1,
  "versionNonce": 99999,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false,
  "roundness": {"type": 3}
}
```
**Note**: layer bands use `fillStyle: "solid"` (not hachure) for a clean pastel background. Place them BEFORE the content elements in the `elements` array so content renders on top.

## Swimlane band (labeled horizontal lane)
A layer band plus a left-aligned free-floating label. Use for flowchart swimlanes (by role/actor) or architecture tiers. Place the band first, then the label, then the lane's content.
```json
{
  "type": "rectangle",
  "id": "lane_backend",
  "x": 40, "y": 300, "width": 1400, "height": 220,
  "strokeColor": "<layer band stroke from palette>",
  "backgroundColor": "<layer band fill from palette>",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 2,
  "opacity": 100,
  "angle": 0,
  "seed": 31000,
  "version": 1, "versionNonce": 31001, "isDeleted": false,
  "groupIds": [], "boundElements": null, "link": null, "locked": false,
  "roundness": {"type": 3}
}
```
Lane label (free-floating, top-left of the band):
```json
{
  "type": "text",
  "id": "lane_backend_label",
  "x": 60, "y": 312,
  "width": 160, "height": 22,
  "text": "BACKEND",
  "originalText": "BACKEND",
  "fontSize": 16, "fontFamily": 1,
  "textAlign": "left", "verticalAlign": "top",
  "strokeColor": "<title color from palette>",
  "backgroundColor": "transparent", "fillStyle": "solid",
  "strokeWidth": 1, "strokeStyle": "solid", "roughness": 2, "opacity": 100,
  "angle": 0, "seed": 31002, "version": 1, "versionNonce": 31003,
  "isDeleted": false, "groupIds": [], "boundElements": null,
  "link": null, "locked": false, "containerId": null, "lineHeight": 1.25
}
```

## Diamond (decision)
```json
{
  "type": "diamond",
  "id": "decision1",
  "x": 100, "y": 100, "width": 140, "height": 100,
  "strokeColor": "<Decision stroke from palette>",
  "backgroundColor": "<Decision fill from palette>",
  "fillStyle": "hachure",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 2,
  "opacity": 100,
  "angle": 0,
  "seed": 55555,
  "version": 1,
  "versionNonce": 66666,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": [{"id": "decision_text1", "type": "text"}],
  "link": null,
  "locked": false
}
```

## Text (centered inside a shape)
```json
{
  "type": "text",
  "id": "text1",
  "x": 130, "y": 132,
  "width": 120, "height": 25,
  "text": "Process",
  "originalText": "Process",
  "fontSize": 16,
  "fontFamily": 1,
  "textAlign": "center",
  "verticalAlign": "middle",
  "strokeColor": "<text color — match parent shape's stroke or use 'on light/dark fills' from palette>",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "strokeStyle": "solid",
  "roughness": 2,
  "opacity": 100,
  "angle": 0,
  "seed": 11111,
  "version": 1,
  "versionNonce": 22222,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false,
  "containerId": "elem1",
  "lineHeight": 1.25
}
```
**Note**: when text is bound to a shape via `containerId`, the parent shape must list it in `boundElements`. Excalidraw re-centers bound text automatically, so the `x`/`y` here are a starting estimate.

## Arrow
```json
{
  "type": "arrow",
  "id": "arrow1",
  "x": 282, "y": 145, "width": 118, "height": 0,
  "strokeColor": "<arrow color — typically matches source element's stroke from palette>",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "solid",
  "roughness": 2,
  "opacity": 100,
  "angle": 0,
  "seed": 33333,
  "version": 1,
  "versionNonce": 44444,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null,
  "locked": false,
  "points": [[0, 0], [118, 0]],
  "startBinding": {"elementId": "elem1", "focus": 0, "gap": 2},
  "endBinding": {"elementId": "elem2", "focus": 0, "gap": 2},
  "startArrowhead": null,
  "endArrowhead": "arrow"
}
```
**CRITICAL — binding is two-way.** This arrow names `elem1`/`elem2`, but that is only
half. You MUST also add `{"id": "arrow1", "type": "arrow"}` to **both** `elem1.boundElements`
and `elem2.boundElements` (append it next to any existing `text` entry — see the Rectangle
template). Skip this and the arrow detaches when a box is dragged. The arrow's own
`boundElements` stays `null`. For a fan-out, the source box lists **every** arrow leaving it.
Place the arrow's start point on the source box's edge and its end point on the target's
edge (geometry recipe in [`binding.md`](binding.md)). For a curved arrow or to route around
an element, use 3+ points in `points` (waypoints).

## Dashed arrow (async / optional / "no" branch)
Same as the arrow above but with a dashed stroke — use for optional flows, async messages, or fallback/"no" branches. Set:
```json
"strokeStyle": "dashed",
"strokeColor": "<a muted or warning stroke from palette>"
```

## Evidence artifact (code / JSON on a dark panel)
A solid dark rectangle with free-floating monospace-style text on top (place the rect first, then the text). Use the evidence colors from `color-palette.md`.
```json
{
  "type": "rectangle",
  "id": "evidence_payload",
  "x": 900, "y": 400, "width": 360, "height": 140,
  "strokeColor": "#0f172a",
  "backgroundColor": "#1e293b",
  "fillStyle": "solid",
  "strokeWidth": 1, "strokeStyle": "solid", "roughness": 2, "opacity": 100,
  "angle": 0, "seed": 41000, "version": 1, "versionNonce": 41001,
  "isDeleted": false, "groupIds": [], "boundElements": null,
  "link": null, "locked": false, "roundness": {"type": 3}
}
```
Evidence text (green for JSON/data; place on top of the panel):
```json
{
  "type": "text",
  "id": "evidence_payload_text",
  "x": 920, "y": 416,
  "width": 320, "height": 108,
  "text": "{\n  \"event\": \"RUN_STARTED\",\n  \"runId\": \"r_01H...\"\n}",
  "originalText": "{\n  \"event\": \"RUN_STARTED\",\n  \"runId\": \"r_01H...\"\n}",
  "fontSize": 14, "fontFamily": 3,
  "textAlign": "left", "verticalAlign": "top",
  "strokeColor": "#22c55e",
  "backgroundColor": "transparent", "fillStyle": "solid",
  "strokeWidth": 1, "strokeStyle": "solid", "roughness": 2, "opacity": 100,
  "angle": 0, "seed": 41002, "version": 1, "versionNonce": 41003,
  "isDeleted": false, "groupIds": [], "boundElements": null,
  "link": null, "locked": false, "containerId": null, "lineHeight": 1.25
}
```
**Note**: evidence text is the one place to use `fontFamily: 3` (monospace) — it signals "this is literal code/data", and keeps alignment for multi-line snippets.
