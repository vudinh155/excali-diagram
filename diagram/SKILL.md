---
name: diagram
description: Create visual diagrams as Excalidraw files (.excalidraw) that ARGUE visually — process flowcharts, system architecture & data pipeline diagrams, sequence/timeline/lifecycle diagrams, mindmaps/org charts/hierarchy trees/entity-relationship (ER) diagrams. Use this skill when the user wants to "draw a diagram", "make a flowchart", "architecture diagram", "process diagram", "mindmap", "org chart", "timeline", "lifecycle", or to visualize a system/process/concept. Also triggers on Vietnamese phrasing ("vẽ sơ đồ", "vẽ diagram", "sơ đồ kiến trúc", "lưu đồ quy trình"). The skill renders to PNG and self-verifies visually through a mandatory loop.
metadata:
  author: MangoAds Co., Ltd.
  copyright: Copyright (c) 2024-2026 MangoAds Co., Ltd.
license: Apache-2.0 — see the LICENSE file for details.
---

# Diagram Builder (Excalidraw)

Create `.excalidraw` JSON files that **argue visually**, not merely display information.

> **Core philosophy**: A diagram must **ARGUE**, not **DISPLAY**. The shape itself MUST BE the meaning.
> - **Isomorphism Test**: Erase all the text — does the structure alone convey the concept? If not, redesign.
> - **Education Test**: Does the viewer learn something concrete, or do they just see labels glued onto boxes?
>
> Read the full methodology in [`references/methodology.md`](references/methodology.md) **before** designing.

**Brand customization**: All colors and styling live in [`references/color-palette.md`](references/color-palette.md) — the single source of truth for every color choice. Read it before creating any diagram. If the user supplies a **customer brand guide** (e.g. `input/brand-style-guide/<brand>-DESIGN.md`), apply its colors via the **Brand override** section of that file — map the brand's colors onto the existing semantic slots (never rewrite the structure), derive any slots the brand doesn't define, and ignore brand fonts/shadows (no Excalidraw equivalent).

---

## The 7-step workflow (REQUIRED, in order)

| Step | Task | Reference |
|------|------|-----------|
| **S0 — Assess depth** | Is this a **Simple/Conceptual** diagram (abstract shapes, mental models) or a **Comprehensive/Technical** one (concrete examples, code, real data)? If technical → **research the real spec/format/names first**. | [`methodology.md`](references/methodology.md) |
| **S1 — Understand deeply** | What does each concept **DO** (not what it IS)? What are the relationships, the flow, the core transformation? What must the viewer SEE? | [`methodology.md`](references/methodology.md) |
| **S1.5 — Brand styling (optional)** | If a customer brand guide is supplied → apply its colors via the **Brand override** section; pick `roughness`/`fillStyle` to match the brand's personality. Otherwise use the default palette. | [`color-palette.md`](references/color-palette.md) |
| **S2 — Pick a playbook** | Based on the diagram type, pick one playbook below as the primary recipe. Combine two if the diagram is hybrid. | "Pick a playbook" table |
| **S3 — Map to patterns** | Each major concept uses a **different visual pattern** (fan-out, convergence, tree, cycle…). Never a uniform card grid. | [`visual-patterns.md`](references/visual-patterns.md) |
| **S4 — Sketch the flow** | Picture how the viewer's eye moves through the diagram. There must be a clear visual story. | [`methodology.md`](references/methodology.md) |
| **S5 — Build JSON region by region** | Build **one region at a time** (never the whole file at once). Use the schema + templates. Every arrow MUST be bound **both ways** (arrow→box AND box→arrow) — get this right as you write each arrow. | [`json-schema.md`](references/json-schema.md) · [`element-templates.md`](references/element-templates.md) · [`binding.md`](references/binding.md) · [`rendering.md`](references/rendering.md) |
| **S6 — Render & verify** | **MANDATORY**: render to PNG → Read the PNG → fix → loop until it's right. Never ship a diagram from JSON alone. | [`rendering.md`](references/rendering.md) · [`quality-checklist.md`](references/quality-checklist.md) |

---

## Pick a playbook (S2) — user request → recipe

| The user wants… | Playbook | Tell-tale signs |
|-----------------|----------|-----------------|
| Process flowchart, if/else decisions, approval flow, swimlanes by role | [`playbooks/flowchart.md`](playbooks/flowchart.md) | **branching/conditions**, sequential steps, "if… then…" |
| Software architecture, microservices, data pipeline, layered diagram | [`playbooks/architecture.md`](playbooks/architecture.md) | **system components** that communicate, tiers/layers, request/response |
| Event sequence, protocol, lifecycle, time-ordered roadmap | [`playbooks/sequence-timeline.md`](playbooks/sequence-timeline.md) | **time/step ordering**, milestones, events in succession |
| Mindmap, org chart, classification tree, data relationships (ER) | [`playbooks/hierarchy.md`](playbooks/hierarchy.md) | **parent-child hierarchy**, branching from one root, entity relationships |

> **Hybrid diagrams**: e.g. "a pipeline with a decision branch" → architecture (layer frame) + flowchart (the branch). Take the layout from the primary playbook, borrow patterns from the secondary one.

Each playbook points to a **real, render-verified example** in [`examples/`](examples/) — read the example to follow its JSON structure.

---

## Hard rules (do not violate)

1. **Bind every arrow BOTH ways.** An arrow needs `startBinding`/`endBinding` pointing at its boxes **and** each box must back-reference the arrow in its `boundElements`. Writing only the first half is the #1 defect: the file looks fine but arrows detach the moment a box moves. A fan-out (1→many) is N separate arrows, and the shared source box must list **all** of them. Read [`binding.md`](references/binding.md) before drawing anything with arrows. (Optional: `check_bindings.py` can confirm bindings in one cheap pass — see below — but the rule is what matters; get it right while writing.)
2. **Build JSON one region at a time** — do NOT try to emit the whole file in one response. The ~32k-token output limit will truncate large JSON → broken file. Even when it fits, region-by-region produces better quality. (Strategy: [`rendering.md`](references/rendering.md).)
3. **Do NOT use a coding agent** to generate the JSON — agents lack the skill's rules context.
4. **Do NOT write a Python script to generate JSON** — the indirection makes debugging harder. Hand-written JSON with descriptive IDs (e.g. `trigger_rect`, `arrow_fan_left`) is easier to maintain.
5. **MANDATORY render-verify loop** (S6) — you cannot judge a diagram from JSON alone. Usually 2-4 iterations.
6. **Colors come only from [`color-palette.md`](references/color-palette.md)** — color encodes meaning; never invent new colors.
7. **Render defaults**: `roughness: 2`, `fontFamily: 1`, `fillStyle: "hachure"` (shapes) / `"solid"` (layer bands & evidence), `opacity: 100`.

---

## Documentation map

**Methodology & principles**
- [`references/methodology.md`](references/methodology.md) — philosophy, depth assessment, research, evidence artifacts, multi-zoom, container vs free-floating text, shape meaning, layout, text rules
- [`references/visual-patterns.md`](references/visual-patterns.md) — primitive pattern library (fan-out, convergence, tree, cycle, cloud, chain, side-by-side, gap, line-as-structure)

**Technical reference**
- [`references/json-schema.md`](references/json-schema.md) — Excalidraw JSON schema
- [`references/binding.md`](references/binding.md) — **arrow binding (two-way) — read before any diagram with arrows**; geometry, fan-out, convergence, labels, the linter
- [`references/element-templates.md`](references/element-templates.md) — copy-paste JSON template per element type
- [`references/color-palette.md`](references/color-palette.md) — brand colors + render defaults (color source of truth)
- [`references/rendering.md`](references/rendering.md) — render & verify loop, large-diagram strategy, setup, troubleshooting
- [`references/quality-checklist.md`](references/quality-checklist.md) — final quality checklist
- `references/check_bindings.py` — **optional** binding linter; run it once if you want to self-check a finished file (not required, not auto-run)

**Playbooks per diagram type** → [`playbooks/`](playbooks/) · **Real examples** → [`examples/`](examples/)

---

**START**: Read `methodology.md` + `color-palette.md` (+ `binding.md` if the diagram has arrows), assess depth (S0), pick a playbook (S2), build JSON region by region (binding every arrow both ways as you go), then **render-verify until it's right**. Match the user's language for the diagram text.
