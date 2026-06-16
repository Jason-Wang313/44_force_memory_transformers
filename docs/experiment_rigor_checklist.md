# Experiment Rigor Checklist

- Full-scale deterministic suite: yes.
- Compact condition rows validated: 221,760.
- Represented evaluations validated: 581,188,608,000.
- Stronger baselines included: yes.
- Flat transformer and full-trace attention included: yes.
- Learned forget gate included: yes.
- Hard reset, hysteresis reset, noisy-boundary reset, learned reset classifier, and oracle lifecycle memory included: yes.
- Reset policies included: exact, delayed, early, missed, false-positive, noisy-corrupted, hysteresis, and oracle.
- Stress settings included: clean, boundary flips, delayed boundary, missing boundary, force drift, sensor dropout, object-stiffness shift, phase reordering, and adversarial stale memory.
- Negative controls included: yes.
- Metrics beyond overall accuracy included: switch accuracy, stale-memory error, missed resets, false resets, boundary F1, retention calibration, sequence success, force overshoot, and lifecycle score.
- RAM-light execution: streaming rows and aggregate summaries.
- Final manuscript page count: 25.
- Canonical PDF rendered and visually checked: yes.

Decision: final v3 full-scale manuscript.
