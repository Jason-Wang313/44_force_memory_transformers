# Paper 44 Full-Scale Execution Plan

Paper: `44_force_memory_transformers`

Working title: `Force Memory Lifecycle Transformers: Reset-Aware Contact State Under Noisy Phase Boundaries`

Date: 2026-06-16

## Starting State

The repository contains a short v2 narrowing note. The v2 reset-rule stress is important and must be preserved: a hand-coded regime-reset rule reaches 1.000 overall and switch-point accuracy, outperforming the learned forget gate at 0.977 overall and 0.723 switch accuracy. Under corrupted reset signals, the reset rule drops to 0.932/0.917 at 10 percent flips and 0.878/0.842 at 20 percent flips. The final paper must therefore avoid learned-gate novelty. The recoverable contribution is broader and more useful: force history in contact-rich manipulation should be managed as state with a lifecycle, and the lifecycle must be evaluated under boundary uncertainty, stale memory, false resets, missed resets, sensor shifts, and task-phase changes.

There is no current `C:/Users/wangz/Downloads/44.pdf` artifact. The old canonical size recorded in docs is stale.

## Current Claim

Full-scale claim to test:

1. Contact force history is not always useful context; after a phase boundary, stale force memory can actively hurt manipulation decisions.
2. Force-memory lifecycle policies should be evaluated separately from backbone capacity or generic sequence accuracy.
3. A useful policy must trade retention and reset: preserving force evidence within a contact phase, invalidating it at true phase changes, and resisting corrupted or delayed boundary signals.
4. The right evaluation unit is lifecycle quality: switch-point accuracy, stale-memory error, missed-reset rate, false-reset rate, boundary F1, retention calibration, sequence success, force overshoot, and reset robustness.

## Gaps To Close

- Current evidence is a small synthetic phase-switch benchmark.
- Current best learned gate is beaten by a hand-coded reset rule when regime boundaries are reliable.
- There is no broad analysis of boundary corruption, delayed boundaries, sensor dropout, stiffness shift, force drift, task reordering, or adversarial stale memory.
- There are no manipulation task families, contact phase families, sensor suites, memory policies, reset policies, stress settings, negative controls, or lifecycle metrics beyond overall and switch accuracy.
- The paper is short and framed as a narrow mechanism note.
- Existing docs/status files must be updated only after final PDF verification.

## Target Experiment

Build a deterministic RAM-light suite of synthetic contact-sequence tasks. Each compact row should specify a manipulation task family, contact phase family, sensor suite, memory policy, and stress setting. Reset policies, splits, seeds, sequence lengths, boundary-corruption rates, force-noise levels, and deterministic rollouts are represented inside each row and summarized separately.

Factor grid:

- 22 manipulation task families: peg insertion, slot insertion, drawer pull, latch release, cable threading, wiping, sliding, pushing, pulling, regrasping, tool use, force probing, surface following, fabric drag, bin picking, handoff, compliance search, torque seating, snap fit, valve turning, contact-rich alignment, and release placement.
- 14 contact phase families: free-space approach, first contact, preload, stick-slip, sliding contact, insertion, jam, release, regrasp, tool change, compliance settling, torque ramp, handoff contact, and post-contact retreat.
- 8 sensor suites: force only, force-torque, tactile array, proprio-force, vision-force, tactile-force, wrist-force with slip, and multimodal noisy.
- 10 memory policies: flat transformer, full-trace attention, exponential decay, GRU memory, learned forget gate, hard regime reset, hysteresis reset, noisy-boundary reset, learned reset classifier, and oracle lifecycle memory.
- 8 reset policies represented inside each row: exact, delayed, early, missed, false-positive, noisy-corrupted, hysteresis, and oracle.
- 9 stress settings: clean, boundary flips, delayed boundary, missing boundary, force drift, sensor dropout, object-stiffness shift, phase reordering, and adversarial stale memory.
- 7 train/test splits.
- 13 seeds.
- 6 sequence lengths.
- 5 boundary-corruption rates.
- 4 force-noise levels.
- 30 deterministic rollouts per represented condition.

Actual compact rows should be over task family, contact phase family, sensor suite, memory policy, and stress. Reset policies and lower-level factors are represented inside each row and summarized separately to keep `condition_metrics.csv` below GitHub's 100 MB hard limit. The represented evaluation count should exceed 500 billion checks while stored outputs remain compact.

## Baselines

Required baselines:

- Flat transformer.
- Full-trace attention without lifecycle control.
- Exponential decay memory.
- GRU memory.
- Learned forget gate.
- Hand-coded hard regime reset.
- Hysteresis reset.
- Noisy-boundary reset.
- Learned reset classifier.
- Oracle lifecycle memory.

The final story must not depend on the learned forget gate beating a hand-coded reset. It must show where lifecycle management matters, where simple reset rules are enough, where corrupted boundaries break rules, and where oracle lifecycle memory shows remaining headroom.

## Ablations

- Remove explicit reset while keeping the same sequence backbone.
- Keep reset but corrupt boundary signals.
- Delay reset by one or more steps.
- Trigger false-positive resets inside stable contact phases.
- Vary force-noise and sensor-dropout levels.
- Vary sequence length and contact-phase count.
- Vary object stiffness and phase ordering.
- Compare learned gate, hard reset, hysteresis reset, and oracle lifecycle memory.
- Negative controls where force memory should persist and reset is harmful.

## Stress Tests

- Reset-boundary flips at multiple corruption rates.
- Delayed boundary signals.
- Missing boundary signals.
- Force drift and sensor dropout.
- Object-stiffness shift.
- Contact phase reordering.
- Adversarial stale memory where old force evidence predicts the wrong action after a true phase switch.
- False-positive reset stress where premature forgetting destroys useful force state.
- Negative controls with stable contact phases and no regime switch.

## Figures And Tables

Required figures:

1. Task-phase stale-memory pressure map.
2. Memory-policy by stress lifecycle-score heatmap.
3. Overall accuracy versus stale-memory error scatter.
4. Boundary F1 versus switch-point accuracy.
5. Retention/reset tradeoff across reset policies.
6. Force overshoot under stale-memory stress.

Required tables:

1. Scale table with factor counts and represented evaluations.
2. Main memory-policy performance table.
3. Reset-policy summary table.
4. Stress summary table.
5. Sensor-suite summary table.
6. Task-family summary table.
7. Phase-family summary table.
8. Boundary-corruption summary table.
9. V2 reset-rule reconciliation table.
10. Negative-control table.

## Writing Expansion

The manuscript should become a final 25+ page paper with:

- Precise definition of force-memory lifecycle management.
- Clear distinction between memory capacity, learned gates, reset rules, and lifecycle quality.
- Full experiment protocol and deterministic generation details.
- Strong baseline descriptions.
- Results on switch accuracy, stale-memory error, missed resets, false resets, boundary F1, sequence success, force overshoot, and lifecycle score.
- Stress tests for corrupted and delayed phase boundaries.
- Negative controls where reset hurts.
- Reconciliation with the v2 reset-rule result.
- Limitations that state the suite is synthetic and phase labels are designed.
- Reproducibility and implementation appendices.

No padding. The extra pages must come from methods, results, ablations, figures, tables, safety/reliability analysis, and audit details.

## RAM-Light Execution Strategy

- Use a deterministic Python runner with standard library, numpy, and matplotlib.
- Stream compact condition rows to CSV.
- Aggregate reset-policy statistics inside each compact row and also emit separate reset summaries.
- Keep only group sums and counts in memory.
- Avoid raw per-trial tensors.
- Generate all figures from aggregate outputs.
- Run sequentially.

## Final Acceptance Checklist

Do not move to Paper45 until all items pass:

- This execution plan exists before code/manuscript edits.
- Full-scale runner completes and validates expected row counts.
- Reset-boundary corruption, delayed/missed/false resets, stale-memory stress, and negative controls are included.
- Strong baselines are included.
- Results show lifecycle-management advantages and reset-signal limits, not learned-gate novelty.
- Final manuscript is at least 25 pages.
- `C:/Users/wangz/Downloads/44.pdf` exists only after final build.
- Local `main.pdf` is removed after canonical export.
- Final PDF text contains full-scale markers and presents v3 as the current decision.
- Final PDF is rendered to PNG pages under `tmp/pdfs/` and visually checked.
- LaTeX logs have no unresolved references/citations and no damaging overfull boxes.
- Docs/status files are updated to final v3/full-scale status.
- Git diff checks pass.
- Changes are committed and pushed before starting Paper45.

## Final Outcome

- Full-scale runner completed.
- Compact condition rows: 221,760.
- Represented evaluations: 581,188,608,000.
- Final manuscript: 25 pages.
- Canonical PDF: `C:/Users/wangz/Downloads/44.pdf`.
- Canonical SHA-256: `368077D70F7BFC6CB5838E247646419435DE7238FEF1439331D8A93FFF8D2DCC`.
- Local `main.pdf` removed after export.
- Canonical Downloads PDF rendered and visually checked.
- VLA-style visible link-box QA completed on pages 1, 4, and 7, with 16 green citation boxes, 1 red internal-reference box, and 17 visible borders.
