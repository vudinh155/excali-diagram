# Playbook: Flowchart / process / decision flow

> Recipe for process flowcharts, decision trees, approval flows, and swimlane diagrams. Read [`../references/methodology.md`](../references/methodology.md) and [`../references/color-palette.md`](../references/color-palette.md) first.

## When to use
- Sequential steps with **branching/conditions** ("if X then Y else Z")
- Approval / review workflows, onboarding flows, request handling
- Anything with decision points, loops back, or parallel paths
- **Swimlanes**: the same flow split across actors/roles (User / System / Admin)

If there's no branching and it's purely time-ordered → consider [`sequence-timeline.md`](sequence-timeline.md) instead.

## Shape vocabulary + patterns

| Element | Shape | Color (semantic) |
|---------|-------|------------------|
| Start / End | `ellipse` | Start = Start/Trigger; End = End/Success |
| Process step / action | `rectangle` (rounded) | Primary or Secondary |
| Decision | `diamond` | Decision |
| Error / reject path | `rectangle` | Error or Warning/Reset |
| Connector | `arrow` | source element's stroke; **dashed** for "no"/fallback |
| Branch label ("Yes"/"No") | free-floating `text` | Body/Detail |

Patterns used: **Chain** (the happy path), **Fan-out** (decision → multiple branches), **Cycle** (loop-back arrow on retry/rejection).

## Layout recipe

**Default direction: top → down** (vertical). Use a single center column for the main path; branch decisions sideways.

- Column center x ≈ `400`. Step width `200`, height `80`. Vertical gap between steps: **`70px`** (step bottom to next step top).
- Start/End ellipses: `160×70`, centered on the column.
- Decision diamonds: `180×110`, centered on the column.
- **Yes branch** continues straight down; **No branch** exits the diamond's right vertex → goes right ~`260px`, then down. Put the branch label ~`20px` from the diamond on each exiting arrow.
- Loop-back (retry): arrow from a later step's left side, out left ~`120px`, up, and back into an earlier step's left side — use 3-4 `points` waypoints so it routes *around* the column, never through it.

**Vertical rhythm (y positions for a typical flow):**
```
Start      y=40
 ↓
Step 1     y=170
 ↓
Decision   y=320   ──No──►  Reject  (x≈700, y=335)
 ↓ Yes
Step 2     y=500
 ↓
End        y=660
```

**Swimlanes** (when roles matter): draw horizontal swimlane bands (see `element-templates.md` → "Swimlane band"), one per actor, stacked vertically. Place each step inside its actor's lane; arrows cross lanes vertically. Lane height ~`200px`, label top-left in caps.

## Color mapping
- Start ellipse → Start/Trigger fill `#fed7aa` / stroke `#c2410c`.
- End ellipse → End/Success fill `#a7f3d0` / stroke `#047857`.
- Process steps → Primary `#3b82f6`/`#1e3a5f` (or alternate Secondary `#60a5fa` for visual rhythm).
- Decision → Decision fill `#fef3c7` / stroke `#b45309`.
- Reject/error → Error fill `#fecaca` / stroke `#b91c1c`, reached by a **dashed** arrow.

## Pitfalls (specific to flowcharts)
- **Unbalanced decisions**: a diamond with text but no clear Yes/No exits reads as a process box. Always label both exits and route them to distinct elements.
- **Overlapping branch arrows**: the No-branch arrow crossing the main column. Fix: exit from the diamond's *side* vertex and add a waypoint so it bends around.
- **Loop-backs through boxes**: retry arrows cutting straight through steps. Fix: route them out to the left margin with waypoints.
- **Too many shapes**: >10 steps in one column → split into phases with a labeled divider, or switch to swimlanes.
- **Decision overload**: more than ~4 decisions stacked vertically gets unreadable; group into sub-flows.

## Worked example
[`../examples/flowchart-approval.excalidraw`](../examples/flowchart-approval.excalidraw) — a content approval flow: Submit → Auto-checks → Decision (pass?) → reviewer decision → Publish / Send back (loop). Render it to see the branch routing and loop-back waypoints.

## Variations
- **Horizontal flow** (left→right): same recipe rotated; good for short pipelines that read like a sentence.
- **Decision tree** (no loops): pure fan-out, each decision splitting into 2-3 leaves; let it grow downward and widen.
- **Swimlane**: bands by actor as above — best when "who does what" is the point.
