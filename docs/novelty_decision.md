# Novelty Decision

## Chosen direction

Force Memory Transformers should be framed as a contact-sequence mechanism for force-memory lifecycle management under changing contact regimes.

## Decision after v2 hardening

Workshop-only.

## Reasoning

- The mechanism is more specific than generic tactile transformers.
- The toy supports the claim that stale force history can hurt at phase switches.
- The v2 reset-rule stress shows the learned gate is not the central novelty.
- A hand-coded regime-reset rule solves the synthetic task exactly.
- Reliable phase-boundary signals are a core assumption.
- No real-robot or high-fidelity manipulation benchmark is present.

## Minimal surviving claim

Explicit reset-aware state management is useful for force-memory sequence modeling in this synthetic setting. The current paper does not establish learned-gate superiority over simple reset rules.
