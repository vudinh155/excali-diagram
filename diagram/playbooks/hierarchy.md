# Playbook: Mindmap / org chart / hierarchy / ER

> Recipe for mindmaps, org charts, classification trees, and entity-relationship (data) diagrams. Read [`../references/methodology.md`](../references/methodology.md) and [`../references/color-palette.md`](../references/color-palette.md) first.

## When to use
- **Parent-child hierarchy**: org charts, file trees, taxonomies, breakdowns
- **Mindmaps**: one central idea radiating into branches and sub-branches
- **Entity-relationship (ER)**: data entities and how they relate (1-to-many, etc.)
- Anything where the structure is "X contains / owns / branches into Y"

## Shape vocabulary + patterns

| Element | Shape | Color |
|---------|-------|-------|
| Tree/mindmap nodes | **free-floating `text`** + connecting `line`s (mostly NO boxes) | Title / Subtitle / Body by depth |
| Org chart roles | `rectangle` (rounded) — boxes are OK here (they're "things") | Primary; root = highlighted |
| Branch/connector | `line` (structure) or thin `arrow` | Slate `#64748b` |
| Small node anchor | tiny `ellipse` dot (12px) | marker dot |
| ER entity | `rectangle` with title + attribute list | Primary / Secondary |
| ER relationship | `arrow` or `line` with cardinality label ("1", "N") | Slate |

Patterns used: **Tree** (lines + free-floating text) for mindmaps/taxonomies, **Fan-out** for mindmap from a center, **Convergence** for many-to-one ER relations.

> **Container discipline matters most here**: mindmaps and taxonomies should be mostly *line + free-floating text*, aiming for <30% boxed. Org charts are the exception — roles are discrete "things", so boxes are appropriate.

## Layout recipe

### Mindmap (radial fan-out)
- Central idea at canvas center (~`700, 400`), as a larger title text or a single hero ellipse.
- Branches radiate outward; spread main branches around the center (e.g. 4 branches at NE/SE/SW/NW). Each branch = a `line` from center outward + a title label at the end.
- Sub-branches: shorter lines off each branch line, with smaller free-floating labels. Color-code by branch.
- Keep depth ≤ 3 levels; beyond that it gets unreadable.

### Org chart / tree (top→down)
- Root box centered at top (x≈`700, y=40`), `220×80`.
- Each level down: children spread horizontally, centered under the parent. Vertical gap between levels `~120px`; horizontal gap between siblings `~60px`.
- Connectors: a vertical line down from parent, a horizontal "bus" line, then short verticals down to each child (classic org-chart elbow) — use `line` elements.
```
            [ CEO ]
               │
      ┌────────┼────────┐
   [ CTO ]  [ CFO ]  [ COO ]
      │
   ┌──┴──┐
[Eng] [Data]
```

### ER diagram
- Entities as rectangles with a title row + attributes listed below (free text inside, left-aligned). Width `~240`.
- Place related entities near each other; draw a `line`/arrow between them with a cardinality label at each end ("1" near the one side, "N" near the many side). Simulate crow's-foot with the label rather than custom arrowheads.

## Color mapping
- **Depth = color hierarchy**: root/center = Title `#1e40af` (or Primary box); level-2 = Subtitle `#3b82f6`; level-3 = Body `#64748b`. This makes depth readable without boxes.
- Org chart: root box highlighted (Primary), departments Secondary, sub-teams Tertiary.
- Mindmap: give each main branch a distinct semantic color and inherit it for that branch's sub-nodes.
- ER: entities Primary/Secondary; relationship lines Slate with dark cardinality labels.

## Pitfalls (specific to hierarchies)
- **Over-boxing mindmaps**: a box around every node turns a mindmap into a cluttered grid. Use line + text.
- **Overlapping branches**: sub-branches from adjacent nodes colliding. Fix: widen sibling spacing, or angle branches apart.
- **Depth > 3**: deep trees overflow. Fix: collapse a subtree into a single labeled node, or split into a second diagram.
- **Crossing connectors**: in org charts, reorder siblings so the elbow lines don't cross.
- **Unanchored labels**: a floating label not clearly tied to its branch line. Keep labels touching the end of their line; add a tiny dot anchor if ambiguous.
- **Unbound relation arrows** (ER / concept maps): where you use `arrow`s (not plain `line`s) between entities, bind them both ways — arrow `startBinding`/`endBinding` plus a back-reference in each entity's `boundElements`. See [`../references/binding.md`](../references/binding.md). Plain structural `line`s (org-chart elbows, mindmap branches) are not bound and don't need this.

## Worked example
[`../examples/mindmap-hierarchy.excalidraw`](../examples/mindmap-hierarchy.excalidraw) — a central topic with 4 color-coded branches and sub-branches, built from lines + free-floating text (minimal boxes). Render it to see radial fan-out and depth-by-color.

## Variations
- **Org chart**: top-down boxes with elbow connectors (roles are "things" → boxes OK).
- **Taxonomy / breakdown**: left→right tree (root on the left), good for deep nesting that reads like a bracket.
- **ER / data model**: entity rectangles + cardinality-labeled relations.
- **Concept map**: like a mindmap but relations are labeled (arrows say *how* nodes relate), borrowing from architecture.
