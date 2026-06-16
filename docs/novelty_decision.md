# Novelty Decision

## Chosen direction

Force-memory lifecycle management: preserve useful contact force state inside a phase and invalidate stale evidence at true contact phase boundaries.

## Final decision

Final v3 full-scale manuscript.

## Reasoning

- The paper no longer depends on a learned forget gate beating a hard reset rule.
- Strong reset-rule and memory baselines are included.
- The measured contribution is lifecycle quality: stale-memory reduction, switch accuracy, reset precision/recall, retention calibration, force overshoot, and sequence success.
- The full-scale suite covers task families, phase families, sensor suites, policies, reset policies, stresses, splits, seeds, sequence lengths, corruption rates, force-noise levels, and rerolls.

## What we are not claiming

- Not a hardware-validated manipulation policy.
- Not learned-gate novelty.
- Not a universal tactile transformer.
- Not proof that every contact task needs explicit reset.

## Supported claim

In contact-rich sequence regimes where force evidence can become stale after phase changes, policies should manage force memory as lifecycle state and report reset/retention errors rather than relying only on overall accuracy.
