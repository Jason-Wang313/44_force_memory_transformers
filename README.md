# Force Memory Transformers

Paper 44 in the robotics 60-paper batch.

## V2 hardening decision

Decision: workshop-only.

The v2 reset-rule stress narrows the claim. A hand-coded regime-reset rule reaches 1.000 overall and switch-point accuracy, outperforming the learned forget gate at 0.977 overall and 0.723 switch accuracy. With corrupted reset signals, the rule drops to 0.932/0.917 at 10% flips and 0.878/0.842 at 20% flips. The paper is therefore a mechanism note about force-memory lifecycle management, not learned-gate novelty.

Canonical PDF: `C:/Users/wangz/Downloads/44.pdf`

## Contents

- `main.tex`: ICLR-style source with the v2 hardening note.
- `v2_reset_stress_table.tex`: v2 reset-rule stress table included in the paper.
- `docs/synthetic_results.json`: original synthetic transformer results.
- `docs/v2_reset_stress.json` and `docs/v2_reset_stress.csv`: v2 reset-rule stress results.
- `experiments/force_memory_synth.py`: regenerates original and v2 synthetic results.
- `figures/force_memory_synth.png`: original synthetic evidence figure.
- `scripts/build_pdf.ps1`: canonical PDF build wrapper.

## Reproduce

Run the experiment:

```powershell
python experiments/force_memory_synth.py
```

Build the canonical PDF:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build_pdf.ps1
```
