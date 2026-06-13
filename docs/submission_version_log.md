# Submission Version Log

## v1

- Original synthetic benchmark reported flat transformer accuracy 0.971 overall and 0.650 at switch points.
- Learned forget gate improved to 0.977 overall and 0.723 at switch points.

## v2

- Added reset-rule stress to `experiments/force_memory_synth.py`.
- Found that a hand-coded regime-reset rule reaches 1.000 overall and switch-point accuracy.
- Added corrupted-boundary stress for 10% and 20% regime flips.
- Updated paper and docs to mark the repo workshop-only.
- Canonical PDF target remains `C:/Users/wangz/Downloads/44.pdf`.
