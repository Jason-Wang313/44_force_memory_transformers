# Force Memory Transformers

Paper 44 in the robotics 60-paper batch.

## Final v3 status

Status: final v3 full-scale manuscript.

Canonical PDF: `C:/Users/wangz/Downloads/44.pdf`

Canonical PDF SHA-256: `34AD3304C4C9C44507D0E4696DE90CB9AC5892F4F27FE045D242BB2ABC241682`

The v3 paper reframes the v2 reset-rule result into a broader force-memory lifecycle study. The final manuscript evaluates stale force memory, missed resets, false resets, switch accuracy, boundary F1, retention calibration, sequence success, and force overshoot across a full deterministic suite.

## Full-scale suite

- Compact condition rows: 221,760.
- Represented reset/split/seed/sequence/corruption/noise/reroll evaluations: 581,188,608,000.
- Factors: 22 manipulation task families, 14 contact phase families, 8 sensor suites, 10 memory policies, 8 reset policies, 9 stresses, 7 splits, 13 seeds, 6 sequence lengths, 5 boundary-corruption rates, 4 force-noise levels, and 30 rerolls.
- Final manuscript length: 25 pages.

## Contents

- `main.tex`: final ICLR-style manuscript source.
- `scripts/run_full_scale_force_memory_suite.py`: deterministic RAM-light full-scale runner.
- `results/full_scale/`: generated aggregate CSVs, validation files, LaTeX tables, and suite README.
- `figures/full_scale/`: generated full-scale figures.
- `scripts/build_pdf.ps1`: canonical PDF build/export wrapper.
- `docs/`: plans, audits, reviewer attacks, novelty decision, and reproducibility records.

## Reproduce

Run the full-scale suite:

```powershell
python scripts/run_full_scale_force_memory_suite.py
```

Build the canonical PDF:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/build_pdf.ps1
```
