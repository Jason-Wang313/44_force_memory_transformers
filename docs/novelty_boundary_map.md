# Novelty Boundary Map

## What is already crowded

- Transformer encoders over tactile histories.
- Diffusion or chunked policies with force feedback.
- Multimodal fusion of vision, touch, and proprioception.
- Memory or retrieval for contact experience.
- World models for robotic manipulation.

## What remains open

- Treating force history as a structured state with lifecycle management.
- Making stale-contact invalidation explicit.
- Separating "remember because relevant" from "remember because recent."
- Estimating reliable contact-regime boundaries from real sensing.

## V2 boundary update

The synthetic task is too easy for an oracle reset mechanism. The novelty cannot be the learned forgetting gate itself; it must be the robotics framing that force-memory state needs lifecycle events. A future stronger paper must compare learned gates against explicit reset rules under noisy, latent, or ambiguous contact-boundary signals.
