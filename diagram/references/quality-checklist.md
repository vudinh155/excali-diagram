# Quality checklist

Run through this before declaring a diagram done. Group A is a pre-check for technical diagrams; the rest applies to all diagrams.

## A. Depth & evidence (pre-check for technical diagrams)
1. **Researched**: Did you look up the real spec, format, event names?
2. **Evidence**: Are there code snippets, JSON examples, or real data?
3. **Multi-zoom**: Is there a summary flow + section boundaries + detail?
4. **Concrete over abstract**: Real content shown, not just labeled boxes?
5. **Educational value**: Would someone learn something concrete from it?

## B. Conceptual
6. **Isomorphism**: Does each visual structure reflect the concept's behavior?
7. **Argument**: Does the diagram SHOW what words alone cannot?
8. **Variety**: Does each major concept use a different visual pattern?
9. **No uniform containers**: Avoided card grids and rows of equal boxes?

## C. Container discipline
10. **Minimal containers**: Could any boxed element become free-floating text?
11. **Lines as structure**: Do tree/timeline patterns use line + text instead of boxes?
12. **Typographic hierarchy**: Do size and color create hierarchy (reducing the need for boxes)?
13. **<30% boxed**: Fewer than ~30% of text elements are inside containers.

## D. Structure
14. **Connection**: Every relationship has an arrow or line.
15. **Flow**: There's a clear visual path for the viewer's eye.
16. **Hierarchy**: Important elements are larger / more separated.

## E. Technical correctness
17. **Clean text**: `text` contains only readable words (matches `originalText`).
18. **Font**: `fontFamily: 1` (Excalifont/Virgil handwriting).
19. **Roughness**: `roughness: 2` for the hand-drawn style (default).
20. **Fill style**: `"hachure"` for shapes, `"solid"` for layer bands and evidence.
21. **Opacity**: `100` for every element (no transparency).
22. **Colors from palette**: Every color comes from `color-palette.md`.
23. **Valid bindings**: All IDs and `boundElements`/binding references point to elements that exist.

## F. Visual verification (render required)
24. **Rendered to PNG**: The diagram was rendered and inspected with the Read tool.
25. **No text overflow**: All text fits inside its container.
26. **No accidental overlap**: Shapes and text don't overlap unintentionally.
27. **Even spacing**: Similar elements are evenly spaced.
28. **Arrows land right**: Arrows connect the intended elements without cutting through others.
29. **Readable at export size**: Text is clear in the rendered PNG.
30. **Balanced layout**: No gaping empty areas or overcrowded zones.
