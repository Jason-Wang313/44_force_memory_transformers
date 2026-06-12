# Novelty Decision

## Chosen direction
`Force Memory Transformers` should be framed as a contact-sequence policy that maintains a structured force memory and explicitly forgets stale force state when the current contact regime no longer matches.

## Why this is the strongest idea
- It is more specific than "tactile transformers."
- It breaks a real assumption: that all force history should be retained uniformly.
- It is naturally robotic: contact regimes change during insertion, sliding, regrasping, and alignment.
- It can be evaluated with both synthetic and real manipulation sequences.

## Rejected alternatives
- Bigger backbone: too weak and already crowded.
- Better dataset only: useful but not the mechanism.
- Pure retrieval memory: already close to existing tactile memory work.
- Generic world model: too broad unless tied to force-memory lifecycle.
- LLM planner: outside the contact-sequence mechanism.

## Core claim boundary
The paper should claim that explicit forgetting is not a cosmetic tweak; it changes control quality because stale force evidence can actively mislead sequential manipulation when contact phases switch.

## Evidence requirement
At minimum:
- a contact-sequence benchmark or synthetic task with phase switches,
- comparisons against flat force-history transformers and retrieval-style memory,
- forgetting ablations showing when the memory should be dropped,
- adversarial tests where stale force history is intentionally misleading.
