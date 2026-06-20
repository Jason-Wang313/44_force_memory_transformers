# Final Audit

Paper: 44_force_memory_transformers

Status: final v3 full-scale manuscript

## V2 lesson retained

The earlier reset-rule stress showed that a clean hand-coded reset can beat a learned forget gate in the small toy. The final paper keeps that lesson and makes lifecycle quality, boundary corruption, stale memory, missed resets, false resets, and force overshoot central metrics.

## V3 contribution

The final paper tests force-memory lifecycle management at scale. Flat and full-trace memory retain stale evidence. Learned gates help, but hard and hysteresis reset remain strong. Oracle lifecycle memory estimates headroom.

## Key artifacts

- Paper source: `main.tex`
- Full-scale runner: `scripts/run_full_scale_force_memory_suite.py`
- Full-scale outputs: `results/full_scale/`
- Figures: `figures/full_scale/`
- Build wrapper: `scripts/build_pdf.ps1`
- Build status: `data/build_status.json`

## Final PDF

- Canonical PDF: `C:/Users/wangz/Downloads/44.pdf`
- Pages: 25.
- File bytes: 358130.
- SHA-256: `368077D70F7BFC6CB5838E247646419435DE7238FEF1439331D8A93FFF8D2DCC`
- Local tracked/generated PDF: removed after build.
- Render QA: canonical Downloads PDF rendered to PNG pages and contact sheet under `tmp/pdfs/` before cleanup.
- VLA-style link-box QA: affected pages 1, 4, and 7 rendered at 160 dpi; verified 16 green citation boxes, 1 red internal-reference box, and 17 visible `(0, 0, 1)` borders with no visual collisions.

## Repository

GitHub URL: `https://github.com/Jason-Wang313/44_force_memory_transformers`
