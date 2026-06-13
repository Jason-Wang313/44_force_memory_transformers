# Final Audit

Paper: 44_force_memory_transformers

Decision: workshop-only

Submission-hardening version: v2

## Original positive evidence

- Flat transformer overall accuracy: 0.971.
- Flat transformer switch-point accuracy: 0.650.
- Learned forget gate overall accuracy: 0.977.
- Learned forget gate switch-point accuracy: 0.723.
- Original interpretation: explicit forgetting improves most at contact phase switches.

## V2 reset-rule stress

- Regime-reset rule: 1.000 overall accuracy, 1.000 switch-point accuracy.
- Reset rule with 10% regime-boundary flips: 0.932 overall accuracy, 0.917 switch-point accuracy.
- Reset rule with 20% regime-boundary flips: 0.878 overall accuracy, 0.842 switch-point accuracy.

## Audit judgment

The paper survives as a narrow workshop mechanism note. It supports force-memory lifecycle management, but not learned-gate novelty. The current synthetic task is solved by a hand-coded reset rule when clean regime boundaries are available, and the result depends on reliable boundary signals.

## Artifacts

- Paper source: `main.tex`
- Experiment script: `experiments/force_memory_synth.py`
- Original synthetic results: `docs/synthetic_results.json`
- V2 stress JSON: `docs/v2_reset_stress.json`
- V2 stress CSV: `docs/v2_reset_stress.csv`
- V2 table: `v2_reset_stress_table.tex`
- Build wrapper: `scripts/build_pdf.ps1`

## PDF and repository

- Canonical PDF: `C:/Users/wangz/Downloads/44.pdf`
- Local tracked/generated PDF: removed after build
- Desktop copy: absent
- GitHub URL: `https://github.com/Jason-Wang313/44_force_memory_transformers`
