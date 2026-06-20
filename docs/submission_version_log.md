# Submission Version Log

## v1

- Original synthetic phase-switch benchmark showed a learned forget gate improving switch-point accuracy over a flat transformer.

## v2

- Added reset-rule stress.
- Found clean hard reset reaches perfect toy accuracy and corrupted reset signals degrade performance.
- Recorded the result as a narrowing constraint for the next version.

## v3

- Wrote a full-scale execution plan before edits.
- Added `scripts/run_full_scale_force_memory_suite.py`.
- Generated 221,760 compact condition rows representing 581,188,608,000 evaluations.
- Rewrote the manuscript around force-memory lifecycle management.
- Added full-scale tables, figures, reset policies, boundary corruption, stale-memory stress, negative controls, safety, and reproducibility appendices.
- Built and visually checked the 25-page canonical PDF at `C:/Users/wangz/Downloads/44.pdf`.
- Final SHA-256: `368077D70F7BFC6CB5838E247646419435DE7238FEF1439331D8A93FFF8D2DCC`.

## v3 visual hardening

- Rebuilt the same 25-page manuscript with visible VLA-style red/green link boxes.
- Verified affected pages 1, 4, and 7 by PNG render.
