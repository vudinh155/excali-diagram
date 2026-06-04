# Playbook: System architecture / data pipeline

> Recipe for software architecture, microservices, data pipelines, and layered system diagrams. Read [`../references/methodology.md`](../references/methodology.md) and [`../references/color-palette.md`](../references/color-palette.md) first.

## When to use
- **System components** that communicate (services, databases, queues, clients)
- Data pipelines: data flowing through stages (intake → process → store → serve)
- Layered/tiered architectures (presentation / logic / data)
- Anything where you want to show *how the pieces integrate*

This is almost always a **technical** diagram → research the real component names, protocols, and payload formats first, and include **evidence artifacts** (see methodology).

## Shape vocabulary + patterns

| Element | Shape | Color |
|---------|-------|-------|
| Layer / tier band | wide `rectangle`, `fillStyle: solid` | Layer band colors (1-6) |
| Service / component | `rectangle` (rounded) | Primary / Secondary by role |
| Datastore / queue | `rectangle` | Layer 4 (queue) or Secondary |
| External system / client | `ellipse` | Tertiary or Primary |
| AI/LLM component | `rectangle` | AI/LLM `#ddd6fe`/`#6d28d9` |
| Request/response, data flow | `arrow` (dashed = async/event) | source stroke |
| Code / JSON payload | dark evidence panel | Evidence `#1e293b` + green text |

Patterns used: **Chain** (the pipeline spine), **Fan-out** (a gateway routing to services), **Convergence** (services writing to one store), **Multi-zoom** (summary flow on top, layers in the middle, evidence in detail).

## Layout recipe

**Default: horizontal layer bands stacked top→down**, data flowing left→right within and downward across layers.

- Canvas width ~`1440`. Bands span x `40 → 1440`, height `180-220`, vertical gap `40px`.
- **Summary flow at the very top** (multi-zoom Level 1): small free-floating chain `Client → API → Queue → Workers → DB`, y≈`40`, before the bands start (~y=`120`). This is the "national borders" view.
- Each band = one layer (Level 2): label top-left in CAPS, components placed inside as rounded rectangles `220×90`, horizontal gap `60px`.
- Cross-layer arrows go **vertically** between bands; intra-layer arrows go horizontally. Bind arrows to both components.
- **Evidence panels (Level 3)**: place a dark code/JSON panel next to the component it illustrates (e.g. the API's response shape beside the API box). Connect with a thin dotted line or place adjacent.

**Vertical structure (typical):**
```
Summary flow (free text)         y=40
─ LAYER 1: CLIENTS               y=120  [Web]  [Mobile]
─ LAYER 2: API / GATEWAY         y=380  [REST API]  ──► evidence: response JSON
─ LAYER 3: PROCESSING            y=640  [Worker A] [Worker B]
─ LAYER 4: DATA                  y=900  [Postgres] [Redis]
```

## Color mapping
- Use the **layer band colors** (palette §"Layer band colors") in pipeline order: intake `#a8d8ea`, buffer `#fef3c7`, routing `#fecaca`, queue `#a7f3d0`, exec/output `#ddd6fe`.
- Components inside bands use **semantic shape colors** that contrast with the band (Primary blue components read well on most bands).
- AI/LLM components always get the purple AI pair so they're instantly identifiable.
- Evidence panels: dark `#1e293b` with green `#22c55e` text for JSON.

## Pitfalls (specific to architecture)
- **Generic boxes**: "API", "DB" with no real names → fails the Education Test. Use real service names and show a real payload.
- **Arrow spaghetti**: many crossing arrows. Fix: order components within a band to minimize crossings; use the band structure so most arrows are short verticals.
- **Missing direction**: who calls whom? Every arrow needs a clear source→target; use dashed for async/events.
- **No summary flow**: a wall of boxes with no overview. Always add the Level-1 chain on top.
- **Evidence as decoration**: a code panel that doesn't match a real component. Anchor each evidence panel to the box it explains.

## Worked example
[`../examples/architecture-pipeline.excalidraw`](../examples/architecture-pipeline.excalidraw) — an event-streaming pipeline with layer bands (Clients → API → Stream/Queue → Workers → Store), a top summary flow, and a JSON evidence panel showing a real event payload. Render it to see band + cross-layer arrow layout.

## Variations
- **Microservices mesh**: drop the strict layers; use a central API-gateway fan-out to services, each with its own datastore (convergence into shared infra).
- **Request lifecycle**: combine with [`sequence-timeline.md`](sequence-timeline.md) to show one request's path over time.
- **C4-style zoom**: one diagram per zoom level (context → container → component) instead of multi-zoom in one canvas.
