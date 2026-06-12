# Claims

## Main claim
Explicitly managed force memory improves sequential manipulation when contact regimes change, because stale force history can mislead a policy.

## Supporting claims
- Force history is best treated as state, not just as context.
- A forgetting test can decide whether to preserve, compress, or discard that state.
- The gain is largest in tasks with phase boundaries, repeated contact, or alignment/insertion under uncertainty.

## What we can support
- Synthetic phase-switch experiments.
- Simple contact-rich sequence tasks with adversarial stale-history conditions.
- Ablations against flat-history transformers and memory without forgetting.

## What we should not overclaim
- We do not prove a universal theorem for all manipulation.
- We do not claim the mechanism is sufficient for all tactile learning.
- We do not claim state-of-the-art on a full robotics benchmark without broader experiments.

## Formal-claim status
Likely empirical rather than theorem-driven. If a formal result is included, it should be limited to a toy setting that captures stale-memory failure under regime switches.
