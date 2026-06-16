# Reproducibility Checklist

- Full-scale suite command: `python scripts/run_full_scale_force_memory_suite.py`
- PDF build command: `powershell -NoProfile -ExecutionPolicy Bypass -File scripts/build_pdf.ps1`
- Canonical PDF location: `C:/Users/wangz/Downloads/44.pdf`
- Canonical SHA-256: `34AD3304C4C9C44507D0E4696DE90CB9AC5892F4F27FE045D242BB2ABC241682`
- Local generated paper PDF retained in repo: no.
- Full-scale validation: `results/full_scale/experiment_validation.json`
- Final artifact validation: `results/full_scale/validation.json`
- Main aggregate CSV: `results/full_scale/condition_metrics.csv`
- Summary CSVs: policy, reset, stress, sensor, task, phase, corruption, policy-stress, regime, and negative controls.
- Paper tables: `results/full_scale/table_*.tex`
- Paper figures: `figures/full_scale/*.pdf`
- Visual QA: canonical Downloads PDF rendered to PNG pages and checked before final cleanup.
