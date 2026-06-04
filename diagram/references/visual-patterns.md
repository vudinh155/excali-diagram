# Visual pattern library

These are the **primitive building blocks**. Playbooks combine them into full diagram recipes. In step S3, map each major concept to the pattern that reflects its *behavior* — and give different concepts different patterns (no uniform card grid).

| If a concept… | Use this pattern |
|---------------|------------------|
| Produces many outputs | **Fan-out** (arrows radiate from a center) |
| Merges many inputs into one | **Convergence** (funnel, arrows joining) |
| Has hierarchy/nesting | **Tree** (lines + free-floating text) |
| Is a sequence of steps | **Timeline** (line + dots + free-floating labels) |
| Repeats or continuously improves | **Cycle** (arrows return to the start) |
| Is an abstract state or context | **Cloud** (overlapping ellipses) |
| Turns input into output | **Chain** (before → process → after) |
| Compares two things | **Side-by-side** (parallel with contrast) |
| Splits into phases | **Gap/Break** (visual separation between regions) |

---

## Fan-out (one-to-many)
A central element with arrows radiating to multiple destinations. For: sources, root causes, central hubs, broadcast.
```
        ○
       ↗
  □ → ○
       ↘
        ○
```

## Convergence (many-to-one)
Multiple inputs joining via arrows into a single output. For: aggregation, funnels, summaries.
```
  ○ ↘
  ○ → □
  ○ ↗
```

## Tree (hierarchy)
Parent-child branching with connecting lines and free-floating text (no boxes needed). For: file systems, org charts, taxonomies.
```
  label
  ├── label
  │   ├── label
  │   └── label
  └── label
```
Use `line` elements for the trunk and branches, free-floating text for labels.

## Cycle (continuous loop)
Sequential elements with an arrow returning to the start. For: feedback loops, iterative processes, evolution.
```
  □ → □
  ↑     ↓
  □ ← □
```

## Cloud (abstract state)
Overlapping ellipses of varying sizes. For: context, memory, conversation, mental state.

## Chain (transformation)
Input → process box → output, with clear before/after. For: transforms, processing, conversions.
```
  ○○○ → [PROCESS] → □□□
  chaos              order
```

## Side-by-side (comparison)
Two parallel structures with visual contrast. For: before/after, options, trade-offs.

## Gap/Break (separation)
Whitespace or a visual barrier between regions. For: phase changes, context resets, boundaries.

---

## Lines as structure

Use `line` elements (not arrows) as the primary structural element instead of boxes:

- **Timeline**: a vertical or horizontal line with small dots (10-20px ellipses) at intervals, free-floating labels beside each dot.
- **Tree structure**: a vertical trunk line + horizontal branch lines, with free-floating text labels (no boxes).
- **Dividers**: thin dashed lines to separate regions.
- **Flow axis**: a central line that elements relate to, instead of connecting boxes.

```
Timeline:           Tree:
  ●─── Label 1        │
  │                   ├── item
  ●─── Label 2        │   ├── sub-item
  │                   │   └── sub-item
  ●─── Label 3        └── item
```

Line + free-floating text is usually cleaner than box + contained text.

---

## Modern aesthetics

- **Roughness**: `0` = clean/sharp (only when explicitly requested), `1` = lightly hand-drawn, `2` = fully hand-drawn — **this is the default**. The hand-drawn look is Excalidraw's signature.
- **Fill style**: `"hachure"` (sketchy, default for shapes); `"solid"` (only for layer bands and evidence artifacts).
- **Stroke width**: `1` = thin (lines, dividers, subtle connectors), `2` = standard (shapes, main arrows), `3` = bold (used sparingly for emphasis).
- **Opacity**: always `100`. Use color, size, and stroke width for hierarchy — never transparency.
- **Small markers over shapes**: use small dots (10-20px ellipses) as timeline markers, bullet points, connection nodes, and visual anchors for free-floating text.
