"""Lint Excalidraw arrow/text bindings — catch the #1 AI defect: detached arrows.

Excalidraw bindings are TWO-WAY. An arrow names its boxes via startBinding/endBinding,
and each box must name the arrow back inside its `boundElements`. AI commonly writes only
the first half, so the file looks connected but arrows detach when a box is dragged.

This linter reports, for a .excalidraw file:
  - arrows whose binding target is missing the back-reference in the box's boundElements
  - bindings / boundElements that point at an element id that doesn't exist
  - arrows that have no binding at all (often intentional for a pure structural axis —
    reported as INFO, not an error)
  - duplicate element ids

Usage:
    cd .claude/skills/diagram/references
    uv run python check_bindings.py <path-to-file.excalidraw> [more.excalidraw ...]

Exit code 0 = clean, 1 = problems found (or file/JSON error). Importable: call
`lint_bindings(data) -> list[str]` to get warning strings (empty = clean).
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

# Structural line/arrow ids that are intentionally unbound (e.g. a timeline axis) can be
# named with this substring to silence the "no binding" INFO. Purely a convenience.
_UNBOUND_OK_HINT = "axis"


def lint_bindings(data: dict) -> list[str]:
    """Return a list of human-readable binding problems. Empty list = clean.

    Lines starting with 'INFO:' are advisory (don't fail the build); all others are errors.
    """
    problems: list[str] = []
    elements = [e for e in data.get("elements", []) if not e.get("isDeleted")]
    by_id: dict[str, dict] = {}

    # Duplicate id detection (fatal for binding — two elements sharing an id corrupts links)
    id_counts = Counter(e.get("id") for e in elements if e.get("id") is not None)
    for eid, n in id_counts.items():
        if n > 1:
            problems.append(f"ERROR: duplicate id '{eid}' used by {n} elements")
    for e in elements:
        by_id.setdefault(e.get("id"), e)

    def back_ref_ids(box: dict) -> set[str]:
        return {b.get("id") for b in (box.get("boundElements") or [])}

    for el in elements:
        etype = el.get("type")
        eid = el.get("id")

        # 1) Arrow bindings -> box must back-reference the arrow
        if etype == "arrow":
            has_any = False
            for side in ("startBinding", "endBinding"):
                b = el.get(side)
                if not b:
                    continue
                has_any = True
                tgt = b.get("elementId")
                if tgt not in by_id:
                    problems.append(
                        f"ERROR: arrow '{eid}' {side} -> '{tgt}', but no such element"
                    )
                    continue
                if eid not in back_ref_ids(by_id[tgt]):
                    problems.append(
                        f"ERROR: arrow '{eid}' {side} -> '{tgt}', but '{tgt}'.boundElements "
                        f"is missing the back-reference {{id:'{eid}', type:'arrow'}}"
                    )
            if not has_any:
                lvl = "INFO" if (eid and _UNBOUND_OK_HINT in str(eid)) else "ERROR"
                problems.append(
                    f"{lvl}: arrow '{eid}' has no startBinding or endBinding "
                    f"(it will not follow any box when dragged)"
                )

        # 2) Bound text -> container must exist and back-reference the text
        if etype == "text" and el.get("containerId"):
            cid = el.get("containerId")
            if cid not in by_id:
                problems.append(
                    f"ERROR: text '{eid}' containerId -> '{cid}', but no such element"
                )
            elif eid not in back_ref_ids(by_id[cid]):
                problems.append(
                    f"ERROR: text '{eid}' is in container '{cid}', but '{cid}'.boundElements "
                    f"is missing {{id:'{eid}', type:'text'}}"
                )

        # 3) boundElements entries must point at elements that exist
        for ref in (el.get("boundElements") or []):
            rid = ref.get("id")
            if rid not in by_id:
                problems.append(
                    f"ERROR: '{eid}'.boundElements references '{rid}', but no such element"
                )

    return problems


def _check_file(path: Path) -> int:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON in {path}: {e}", file=sys.stderr)
        return 1

    problems = lint_bindings(data)
    errors = [p for p in problems if not p.startswith("INFO:")]
    infos = [p for p in problems if p.startswith("INFO:")]

    n_arrows = sum(
        1 for e in data.get("elements", [])
        if e.get("type") == "arrow" and not e.get("isDeleted")
    )
    print(f"\n=== {path.name}: {n_arrows} arrows ===")
    if not problems:
        print("  ✓ bindings clean — every arrow back-referenced by its boxes")
        return 0
    for p in errors:
        print(f"  ✗ {p}")
    for p in infos:
        print(f"  · {p}")
    print(f"  {len(errors)} error(s), {len(infos)} info")
    return 1 if errors else 0


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    rc = 0
    for arg in sys.argv[1:]:
        rc |= _check_file(Path(arg))
    sys.exit(rc)


if __name__ == "__main__":
    main()
