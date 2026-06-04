# Playbook: Sequence / timeline / lifecycle

> Recipe for event sequences, protocols, lifecycles, and time-ordered roadmaps. Read [`../references/methodology.md`](../references/methodology.md) and [`../references/color-palette.md`](../references/color-palette.md) first.

## When to use
- **Time/step ordering**: events in succession, protocol handshakes, message exchanges
- Lifecycle / state progression (created → active → archived)
- Roadmaps and phased plans (Q1 → Q2 → Q3)
- Anything where *order and timing* are the point, with little branching

If there's significant branching/conditions → [`flowchart.md`](flowchart.md). If actors exchange messages back and forth → consider a sequence variation below.

## Shape vocabulary + patterns

| Element | Shape | Color |
|---------|-------|-------|
| Time axis | `line` (no arrowheads, or a single arrowhead at the end) | Slate `#64748b` or Primary stroke |
| Milestone / event marker | small `ellipse` 12-16px, `fillStyle: solid` | marker dot color, or semantic by phase |
| Event/milestone label | free-floating `text` | Title (name) + Body (detail) |
| Phase grouping | optional layer band behind a span of markers | Layer band colors |
| Real payload/event data | evidence panel | Evidence dark + green |

Patterns used: **Timeline** (line + dots + free-floating labels) as the backbone, **Gap/Break** for phase separation, **Chain** for cause→effect between events.

## Layout recipe

**Two orientations:**

### Horizontal (roadmaps, protocol over time) — default
- Axis: a horizontal `line` from x=`120` to x=`1400` at y≈`400`. Optional end arrowhead to show direction of time.
- Markers evenly spaced along it: e.g. 5 events at x = `220, 500, 780, 1060, 1340`. **Keep spacing identical** — uneven gaps imply uneven time.
- **Alternate labels above/below** the axis to avoid crowding: event 1 above, event 2 below, etc. Title ~`40px` from the marker, detail line under the title.
- Phase bands (optional): a solid layer band behind a group of markers, label in the band's top-left.

### Vertical (lifecycles, top→down sequences)
- Axis: vertical `line` from y=`80` to y=`800` at x≈`300`.
- Markers down the axis; labels to the **right** of each marker (title + detail), evidence panels further right.

**Horizontal skeleton:**
```
   [above]  Connect            Authenticated         Closed
   label    title              title                 title
            ●─────────●─────────●─────────●─────────●──────►  (time)
                      title              title
                   [below]  Handshake           Streaming
```

## Color mapping
- Markers: use the **marker dot color** (`#3b82f6`) for a neutral timeline, OR color markers by phase using semantic colors (Start→Decision→Success) to show progression.
- Phase bands: layer band colors in sequence.
- Event titles: Title color `#1e40af`; detail lines: Body `#64748b`.
- Use real event/message names from the spec (e.g. `RUN_STARTED`, `STATE_DELTA`) — not "Event 1".

## Pitfalls (specific to timelines)
- **Uneven marker spacing** when time is uniform — reads as variable duration. Keep gaps equal unless duration is intentional (then scale gaps to time and say so).
- **Label crowding**: all labels on one side overlap. Fix: alternate above/below (horizontal) or stagger detail length.
- **Generic labels**: "Step 1, Step 2" teaches nothing. Use real event/phase names.
- **No direction cue**: add an arrowhead at the axis end or a "time →" label so the reader knows which way it flows.
- **Mixing in branches**: if you find yourself adding diamonds, you actually need a flowchart.

## Worked example
[`../examples/timeline-protocol.excalidraw`](../examples/timeline-protocol.excalidraw) — a streaming-protocol session timeline (Connect → Handshake → Authenticated → Streaming → Closed) with alternating labels and a JSON evidence panel for one event. Render it to see marker spacing and label alternation.

## Variations
- **Sequence diagram (actors)**: vertical lifelines per actor (lines down from actor boxes), horizontal arrows between lifelines for messages, ordered top→down. Use when two+ parties exchange messages.
- **Gantt-ish roadmap**: horizontal bars (rectangles) per workstream across a shared time axis, instead of point markers.
- **State machine**: if states loop back (active ⇄ paused), it's a cycle — use ellipse states + arrows with condition labels (borrow from flowchart).
