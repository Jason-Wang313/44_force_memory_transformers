# Paper 44 VLA Highlight Hardening Plan

Date: 2026-06-20

## Objective

Harden Paper 44's visible PDF link-box styling so it matches the VLA-v4 role-model PDF's professional red and green boxed callouts while preserving the final 25-page force-memory lifecycle manuscript, its full-scale benchmark, and all scientific claims.

## Current Evidence

- Canonical PDF: `C:/Users/wangz/Downloads/44.pdf`.
- Current page count: 25.
- Current affected link pages: 1, 4, and 7.
- Current link annotations: 16 green citation/link boxes and 1 red internal-reference box.
- Current border state: all 17 link annotations use border `(0, 0, 0)`, so the boxes are invisible.
- Current LaTeX source uses `\usepackage[hidelinks]{hyperref}` in root `main.tex`.
- Current build wrapper is `scripts/build_pdf.ps1`; it builds from the repository root, exports `C:/Users/wangz/Downloads/44.pdf`, and removes local `main.pdf`.
- Current full-scale benchmark remains 221,760 compact condition rows and 581,188,608,000 represented evaluations.

## Role-Model Style Target

Match the VLA-v4 role model's link annotation style:

```tex
\usepackage{hyperref}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

Expected Paper 44 result after rebuild:

- Page count remains 25.
- All 16 citation/link annotations remain green.
- The single internal-reference link annotation remains red.
- All 17 link annotations use visible border `(0, 0, 1)`.
- No benchmark data, tables, figures, claims, or manuscript body text changes.

## Execution Plan

1. Render the affected pre-change pages to `C:/Users/wangz/highlight_box_hardening/tmp/pdfs/paper44_before` for baseline visual comparison.
2. Replace `\usepackage[hidelinks]{hyperref}` in root `main.tex` with plain `\usepackage{hyperref}` plus the VLA-v4 `\hypersetup` block above.
3. Rebuild using `scripts/build_pdf.ps1`, which exports only `C:/Users/wangz/Downloads/44.pdf`, records build metadata, and removes local `main.pdf`.
4. Verify with `pypdf` that the rebuilt PDF has 25 pages, 16 green link annotations, 1 red link annotation, and 17 `(0, 0, 1)` borders.
5. Render affected post-change pages 1, 4, and 7 and visually inspect the boxes for role-model-like color, line weight, alignment, spacing, and legibility.
6. Update README, child status, and tracked audit/readiness metadata with the final hash, size, and visual hardening evidence.
7. Remove Paper 44 temporary render folders after QA while preserving the shared `role_model` render.
8. Commit and push the clean repo before moving to the next paper.

## Non-Goals

- Do not rerun the benchmark.
- Do not pad content or alter the 25-page manuscript.
- Do not revise claims, tables, captions, figures, or body text unless visual QA exposes a layout defect that requires a tiny local fix.

## Final QA Result

- Rebuilt canonical PDF: `C:/Users/wangz/Downloads/44.pdf`.
- Final SHA-256: `368077D70F7BFC6CB5838E247646419435DE7238FEF1439331D8A93FFF8D2DCC`.
- Final size: 358130 bytes.
- Page count remains 25.
- Annotation inventory: 16 green citation/link boxes, 1 red internal-reference box, and 17 visible `(0, 0, 1)` borders.
- Visual QA rendered pages 1, 4, and 7 at 160 dpi. The boxes are thin, aligned, legible, and collision-free, matching the VLA-v4 role-model treatment.
- Local `main.pdf` was removed by the build wrapper after export.
