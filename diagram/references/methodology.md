# Methodology — How to think before you draw

This is the *why* and *how-to-think* of the skill. Read it before designing any diagram. The concrete recipes live in [`../playbooks/`](../playbooks/); the visual building blocks in [`visual-patterns.md`](visual-patterns.md).

---

## Core philosophy

**A diagram must ARGUE, not DISPLAY.**

A diagram is not formatted text. It is a visual argument that expresses relationships, causality, and flow that words alone cannot. The shape MUST BE the meaning.

- **Isomorphism Test**: If you erase all the text, does the structure alone convey the concept? If not, redesign.
- **Education Test**: Does someone learn something concrete from this diagram, or does it just label boxes? A good diagram teaches — it shows real formats, real event names, concrete examples.

---

## Assess depth FIRST

Before designing, decide how detailed this diagram needs to be.

### Simple / Conceptual
Use abstract shapes when:
- Explaining a mental model or a philosophy
- The viewer doesn't need technical detail
- The concept ITSELF is the abstraction (e.g. "separation of concerns")

### Comprehensive / Technical
Use concrete examples when:
- Drawing a real system, protocol, or architecture
- The diagram will teach or explain (e.g. a tutorial, a YouTube video)
- The viewer needs to understand what things actually look like
- You're showing how several technologies integrate

**For technical diagrams you MUST include evidence artifacts** (see below).

| Simple diagram | Comprehensive diagram |
|----------------|-----------------------|
| Generic labels: "Input" → "Process" → "Output" | Concrete: shows what input/output actually look like |
| Named boxes: "API", "Database", "Client" | Named boxes + real request/response examples |
| Label "Events" or "Messages" | Timeline with real event/message names from the spec |
| A "UI" or "Dashboard" rectangle | A mockup showing real UI elements and content |
| ~30 seconds to explain | ~2-3 minutes of teaching content |
| Viewer learns the structure | Viewer learns structure AND detail |

---

## Research requirement (for technical diagrams)

**Before drawing anything technical, research the real specs.**

If you're diagramming a protocol, API, or framework:
1. Look up the real JSON/data formats
2. Find real event names, method names, or API endpoints
3. Understand how the pieces actually connect
4. Use real terminology, not generic placeholders

Bad: "Protocol" → "Frontend"
Good: "AG-UI emits events (RUN_STARTED, STATE_DELTA, A2UI_UPDATE)" → "CopilotKit renders via createA2UIMessageRenderer()"

Research makes the diagram both accurate AND educational.

---

## Evidence artifacts

Evidence artifacts are concrete examples that prove your diagram is correct and help the viewer learn. Include them in technical diagrams.

| Artifact type | When to use | How to render |
|---------------|-------------|---------------|
| **Code snippet** | API, integration, implementation detail | Dark rectangle + syntax-colored text (see palette for evidence colors) |
| **Data/JSON example** | Data format, schema, payload | Dark rectangle + colored text (see palette) |
| **Event/step sequence** | Protocol, process, lifecycle | Timeline pattern (line + dots + labels) |
| **UI mockup** | Showing the real result/output | Nested rectangles mimicking the real interface |
| **Real input content** | Showing what goes INTO the system | Rectangle with clearly shown sample content |
| **API/method names** | Real function calls, endpoints | Use real names from docs, not placeholders |

Key principle: **show what things actually look like**, not just what they're called.

---

## Multi-zoom architecture

Comprehensive diagrams work at multiple zoom levels at once — like a map that shows both national borders AND street names.

- **Level 1: Summary flow** — a simplified overview of the whole pipeline at a glance. Usually top or bottom of the diagram. *e.g.* `Input → Process → Output` or `Client → Server → Database`.
- **Level 2: Section boundaries** — labeled regions that group related components into visual "rooms" so the viewer understands what belongs to what. *e.g.* group by responsibility (Backend / Frontend), by phase (Setup / Execution / Cleanup), or by actor (User / System / External).
- **Level 3: Detail inside sections** — the evidence artifacts, code snippets, and concrete examples inside each region. This is where the educational value lives.

For comprehensive diagrams, aim to include all three levels: overview gives context, sections organize layout, detail teaches.

---

## Container vs free-floating text

**Not every piece of text needs a box around it.** The default is free-floating text. Add a container only when it serves a purpose.

| Use a container when… | Use free-floating text when… |
|-----------------------|------------------------------|
| It's the focal point of a region | It's a label or description |
| It needs to be visually grouped with other elements | It's supporting detail or metadata |
| An arrow connects into it | It describes something nearby |
| The shape itself carries meaning (decision diamond, etc.) | Typography alone creates enough hierarchy |
| It represents a distinct "thing" in the system | It's a section title, subtitle, or caption |

**Typography creates hierarchy**: use font size, weight, and color to build visual hierarchy without boxes. A 28px title doesn't need a rectangle around it.

**Container test**: for each boxed element ask "would it work as free-floating text?" If yes, drop the container. Aim for **<30% of text elements inside containers**.

---

## Shape meaning

Pick shapes based on what they represent — or use no shape at all:

| Concept type | Shape | Why |
|--------------|-------|-----|
| Label, description, detail | **none** (free-floating text) | Typography makes hierarchy |
| Section title, caption | **none** (free-floating text) | Size/weight is enough |
| Timeline marker | small `ellipse` (10-20px) | Visual anchor, not a container |
| Start, trigger, input | `ellipse` | Soft, evokes an origin |
| End, output, result | `ellipse` | Completion, destination |
| Decision, condition | `diamond` | The classic decision symbol |
| Process, action, step | `rectangle` | A contained action |
| Abstract state, context | overlapping `ellipse`s | Hazy, cloud-like |
| Hierarchy node | line + text (no box) | Structure through lines |

**Rule**: default to no container. Only add shapes when they carry meaning.

---

## Layout principles

### Hierarchy through size
- **Hero (focal point)**: 300×150 — most important visual anchor
- **Primary**: 180×90
- **Secondary**: 120×60
- **Small**: 60×40

### Whitespace = importance
The most important element has the most empty space around it (200px+).

### Flow direction
Lead the viewer's eye: usually left→right or top→bottom for sequences; radial for hub-and-spoke.

### Connection is mandatory
Position alone doesn't express a relationship. If A relates to B, there must be an arrow.

---

## Text rules

The JSON `text` property contains ONLY readable words:

```json
{ "id": "myElement1", "text": "Start", "originalText": "Start" }
```

Settings: `fontSize: 16` (in-shape) / 20-28 (free-floating titles), `fontFamily: 1` (Excalifont/Virgil handwriting), `textAlign: "center"`, `verticalAlign: "middle"`.

- Keep label text short — long strings overflow containers (you'll catch this in the render-verify loop).
- Use color for free-floating text hierarchy (title / subtitle / detail) — see [`color-palette.md`](color-palette.md).

---

## Bad vs Good (quick reference)

| Bad (Display) | Good (Argue) |
|---------------|--------------|
| 5 equal boxes with labels | Each concept has a shape reflecting its behavior |
| Card-grid layout | Visual structure matches conceptual structure |
| Decorative icons for text | The shape IS the meaning |
| Same container type for everything | Distinct visual vocabulary per concept |
| Everything inside a box | Free-floating text with selective containers |
