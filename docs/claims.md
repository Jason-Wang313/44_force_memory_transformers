# Claims

## Core claims

1. Contact force history is not always useful context; stale force memory after phase boundaries can hurt manipulation decisions.
2. Force-memory lifecycle quality should be evaluated separately from backbone capacity and generic sequence accuracy.
3. Useful lifecycle policies balance retention and reset: missed resets cause stale memory, while false resets erase useful contact state.
4. The right metrics include switch accuracy, stale-memory error, missed resets, false resets, boundary F1, retention calibration, sequence success, force overshoot, and lifecycle score.

## Evidence in v3

- Full-scale suite rows: 221,760 compact condition rows.
- Represented evaluations: 581,188,608,000 reset/split/seed/sequence/corruption/noise/reroll checks.
- Flat transformer: lifecycle 0.454, stale-memory error 0.525.
- Full-trace attention: lifecycle 0.458, stale-memory error 0.534.
- Learned forget gate: lifecycle 0.724.
- Hard regime reset: lifecycle 0.739.
- Hysteresis reset: lifecycle 0.741.
- Oracle lifecycle memory: lifecycle 0.796.

## Boundary

The paper is a synthetic mechanism and diagnostic study. It does not claim hardware safety, learned-gate superiority, or a universal tactile policy. Its supported contribution is the evaluation and design frame of force memory as managed contact state with a lifecycle.
