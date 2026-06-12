# Literature Map

## Seed area
The assigned topic sits at the intersection of tactile sequence modeling, force/torque sensing, transformer policies, and contact-rich manipulation. The central recurring design pattern in the literature is to encode tactile or force traces as an observation stream and let attention, diffusion, retrieval, or recurrence discover what matters.

## Main clusters

### 1. Tactile transformers for representation learning
- `Visuo-Tactile Transformers for Manipulation` introduces cross-modal attention between vision and touch for manipulation planning.
- `Transferable Tactile Transformers` scales tactile representation learning across sensors and tasks with a shared trunk and sensor/task adapters.
- Related future work in the sweep expands this line toward multi-sensor pretraining and transfer, but the core assumption remains that tactile history is a feature source, not a structured state with explicit invalidation.

### 2. Tactile memory and retrieval
- `Tactile Retrieval-based Contact-rich Manipulation with a Soft Wrist` and `Tactile Memory with Soft Robot` emphasize storing and retrieving contact experience.
- These works move closer to memory than standard encoders, but retrieval is generally used as a helper to find similar episodes rather than to maintain a formally updated latent state with forgetting tests.

### 3. Action chunking and policy sequence models
- `Action Chunking with Transformers` models action sequences rather than one-step actions.
- This is important because it proves transformers are useful for temporal control, but it does not treat force history as persistent state that can become stale across phase changes.

### 4. Contact-aware diffusion and slow-fast control
- `Reactive Diffusion Policy` shows tactile/force feedback can support reactive control.
- The key assumption is still that the model can react from current observations, while history mainly supplies context. Explicit contact-regime memory is not central.

### 5. World models for manipulation
- The 2026 sweep surfaces a large wave of world-model work for manipulation, including force-guided tactile world models and world-action models.
- This cluster is the strongest hostile prior art because it already treats latent dynamics as a planning object. The open gap is that most world models still prioritize predicting future observations or actions, not deciding when force history should be discarded because it has become invalid.

## Interim interpretation
The best novelty boundary is not a new transformer backbone. It is a mechanism for contact sequences in which force memory is:
- structured as a latent state, not a flat history buffer,
- updated by contact-regime events,
- explicitly tested for staleness before reuse,
- and forgotten when the current phase makes old force evidence misleading.

That makes the paper direction narrower and stronger than generic tactile representation learning.
