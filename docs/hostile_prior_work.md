# Hostile Prior Work

This set is intentionally adversarial. Each paper is summarized in terms of what it claims, what it really adds, which assumptions it leans on, and why it weakens the seed novelty.

## 1. Action Chunking with Transformers
- Problem claimed: long-horizon imitation learning for manipulation.
- Actual mechanism: transformer decoder predicts action chunks from a latent policy representation.
- Hidden assumptions: action history is enough context; state changes are visible in the observation stream; no explicit memory invalidation is needed.
- Variables treated as fixed: chunk length, demo distribution, and the observation modality mix.
- Failure modes ignored: stale context after contact regime shifts.
- Makes less novel: any claim that a transformer over history is the main contribution.
- Leaves open: how to know when the past should be forgotten in contact-heavy tasks.

## 2. Visuo-Tactile Transformers for Manipulation
- Problem claimed: joint vision-touch representation learning.
- Actual mechanism: cross-modal transformer attention builds latent heatmaps for planning.
- Hidden assumptions: touch is complementary evidence, not a state variable with lifecycle.
- Variables treated as fixed: sensor calibration and observation alignment.
- Failure modes ignored: regime changes in contact where older force cues become misleading.
- Makes less novel: using transformer fusion alone for tactile manipulation.
- Leaves open: explicit state maintenance and forgetting in force sequences.

## 3. Transferable Tactile Transformers
- Problem claimed: heterogeneity across tactile sensors and tasks.
- Actual mechanism: shared tactile trunk with sensor/task specific branches and pretraining.
- Hidden assumptions: transfer can be solved by representation scaling; the right abstraction is sensor-invariant features.
- Variables treated as fixed: sensor family, dataset composition, and task labels.
- Failure modes ignored: stale history in sequential control.
- Makes less novel: generic claim that tactile transformers are new.
- Leaves open: whether memory should be regime-aware rather than only sensor-invariant.

## 4. Reactive Diffusion Policy
- Problem claimed: slow-fast contact-rich control.
- Actual mechanism: a diffusion policy with a reactive tactile/force loop.
- Hidden assumptions: immediate reaction is enough; history is supportive but not a structured state.
- Variables treated as fixed: control frequency, sensor timing, and policy horizon.
- Failure modes ignored: long contact episodes where stale force context accumulates.
- Makes less novel: using force feedback in a policy head.
- Leaves open: explicit memory gating/forgetting.

## 5. Tactile Retrieval-based Contact-rich Manipulation with a Soft Wrist
- Problem claimed: contact-rich manipulation via tactile memory.
- Actual mechanism: retrieval over tactile episodes, supported by soft hardware and masked token prediction.
- Hidden assumptions: nearest-neighbor style memory is sufficient; retrieved episodes are semantically relevant.
- Variables treated as fixed: the retrieval library and the episode granularity.
- Failure modes ignored: retrieval pollution when the contact regime has changed.
- Makes less novel: the word "memory" itself.
- Leaves open: whether memory should be updated like state and pruned like control.

## 6. Tactile Memory with Soft Robot
- Problem claimed: robust insertion under uncertainty.
- Actual mechanism: masked bidirectional tactile transformer on a soft-wrist system.
- Hidden assumptions: tactile cues are internally consistent enough to reuse across phases.
- Variables treated as fixed: insertion family and perturbation set.
- Failure modes ignored: when tactile cues from earlier phases hurt later decisions.
- Makes less novel: memorization of tactile histories.
- Leaves open: principled forgetting and phase boundary detection.

## 7. T3: Transferable Tactile Transformers
- Problem claimed: sensor/task scaling.
- Actual mechanism: multi-sensor tactile pretraining on FoTa.
- Hidden assumptions: more coverage and a better shared latent solve most of the problem.
- Variables treated as fixed: dataset scale, task ontology, and sensor categories.
- Failure modes ignored: contact regime misalignment during sequential control.
- Makes less novel: tactile foundation-model framing.
- Leaves open: stateful control with explicit invalidation of stale force memory.

## 8. World models for robotic manipulation
- Problem claimed: forecast future observations/actions for planning.
- Actual mechanism: latent dynamics models, often action-conditioned.
- Hidden assumptions: predictive accuracy is the right target; history can be compressed uniformly.
- Variables treated as fixed: future rollout horizon and latent bottleneck size.
- Failure modes ignored: when a memory should be dropped because the latent regime has changed.
- Makes less novel: any claim that "world model" alone is the novelty.
- Leaves open: regime-aware memory with explicit forgetting tests.
