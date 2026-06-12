# Final Audit

1. Chosen thesis: Force memory in contact-rich manipulation should be managed as a structured state with explicit forgetting when contact regimes change.
2. Field assumption broken: More force history is always helpful if you feed it to a transformer or retrieval module.
3. New central mechanism: A force-memory transformer with a learned forgetting gate that can preserve, compress, or discard stale force state.
4. Genuine novelty: The paper shifts the core mechanism from encoding tactile history to lifecycle management of force memory, and shows the failure mode matters at phase switches.
5. Closest hostile prior work: Action Chunking with Transformers, Visuo-Tactile Transformers, Transferable Tactile Transformers, tactile retrieval/memory papers, and reactive diffusion policy.
6. Literature coverage: 1,694-paper landscape matrix; 300-paper ranked skim; 100-paper hostile prior set; detailed hostile and boundary maps in `docs/`.
7. Proof/formal-claim status: No formal theorem; the claim is empirical, supported by a synthetic phase-switch benchmark.
8. Strongest evidence: The synthetic benchmark improved overall accuracy from 0.971 to 0.977 and switch-point accuracy from 0.650 to 0.723 with explicit forgetting.
9. Biggest weaknesses: Evidence is synthetic and narrow; broader real-robot validation is still missing; several cited prior works are represented through accessible abstracts/snippets rather than full-text rereads.
10. Paper-readiness judgment: workshop
11. Exact Downloads PDF path: `C:/Users/wangz/Downloads/44.pdf`
12. GitHub URL: pending push
13. Desktop copy status: pending orchestrator copy

## Notes
- The repo contains a runnable synthetic experiment at `experiments/force_memory_synth.py`.
- The final PDF was built successfully as `main.pdf` and is ready to be copied to the exact Downloads path.
