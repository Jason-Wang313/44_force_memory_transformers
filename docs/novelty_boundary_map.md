# Novelty Boundary Map

## What is already crowded
- Transformer encoders over tactile histories.
- Diffusion or chunked policies with force feedback.
- Multimodal fusion of vision, touch, and proprioception.
- Memory or retrieval for contact experience.
- World models for robotic manipulation.

## What seems genuinely open
- Treating force history as a structured state with lifecycle management.
- Making stale-contact detection explicit rather than implicit.
- Showing that forgetting old force traces matters for contact-rich control.
- Separating "remember because relevant" from "remember because recent."

## Boundary hypotheses
1. If force history is just another observation stream, the contribution is not novel enough.
2. If memory is only retrieval from similar episodes, prior tactile memory work already covers part of it.
3. If the model only predicts actions better with a bigger transformer, that is a weak move.
4. If the model learns when to forget by a simple heuristic threshold, the mechanism is not strong enough.

## Strongest remaining direction
Build a transformer policy with a force-memory state and a forgetting test that decides whether the latent force memory should be preserved, compressed, or discarded when the contact regime changes.

## Why this survives hostile prior work
- It changes the central mechanism from "encode force sequence" to "manage force state."
- It is testable via phase-shifted contact sequences and ablation on stale-memory reuse.
- It speaks directly to manipulation failure modes, not only representation quality.
