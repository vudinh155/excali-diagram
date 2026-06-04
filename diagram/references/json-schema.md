# Excalidraw JSON schema

## Element types

| Type | Used for |
|------|----------|
| `rectangle` | Processes, actions, components |
| `ellipse` | Entry/exit points, external systems, markers |
| `diamond` | Decisions, conditions |
| `arrow` | Connections between shapes |
| `text` | Labels (inside a shape or free-floating) |
| `line` | Non-arrow connections, structural lines |
| `frame` | Grouping container |

## Common properties

Every element shares these properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique identifier |
| `type` | string | Element type |
| `x`, `y` | number | Position in pixels |
| `width`, `height` | number | Size in pixels |
| `strokeColor` | string | Border color (hex) |
| `backgroundColor` | string | Fill color (hex or "transparent") |
| `fillStyle` | string | "solid", "hachure", "cross-hatch" |
| `strokeWidth` | number | 1, 2, or 4 |
| `strokeStyle` | string | "solid", "dashed", "dotted" |
| `roughness` | number | 0 (smooth), 1 (default), 2 (rough) |
| `opacity` | number | 0-100 |
| `seed` | number | Random seed for the roughness |

## Text-specific properties

| Property | Description |
|----------|-------------|
| `text` | Displayed text |
| `originalText` | Same as `text` |
| `fontSize` | Font size in px (16 in-shape, 20-28 for free-floating titles) |
| `fontFamily` | `1` for handwriting (Excalifont/Virgil) — use this |
| `textAlign` | "left", "center", "right" |
| `verticalAlign` | "top", "middle", "bottom" |
| `containerId` | ID of the parent shape (when text is bound inside a shape) |

## Arrow-specific properties

| Property | Description |
|----------|-------------|
| `points` | Array of [x, y] coordinates (relative to the arrow's own `x`/`y`) |
| `startBinding` | Connection to the start shape |
| `endBinding` | Connection to the end shape |
| `startArrowhead` | null, "arrow", "bar", "dot", "triangle" |
| `endArrowhead` | null, "arrow", "bar", "dot", "triangle" |

## Binding format

```json
{
  "elementId": "shapeId",
  "focus": 0,
  "gap": 2
}
```

A bound shape should list the arrow in its `boundElements`: `"boundElements": [{"id": "arrow1", "type": "arrow"}]`. A shape with bound text lists `{"id": "text1", "type": "text"}`.

## Rounded rectangle corners

Add this to round the corners:
```json
"roundness": { "type": 3 }
```

## Curved arrows/lines

Use 3 or more points in the `points` array to create curves or to route around elements (waypoints).
