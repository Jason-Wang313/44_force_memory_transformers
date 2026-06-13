# Reviewer Attacks

1. This is just a transformer over force history.
2. This is close to tactile memory or retrieval.
3. The gains come from extra parameters.
4. The task is synthetic and too simple.
5. Forgetting is obvious.
6. This could be solved by better data.
7. This is just a world model.
8. The novelty is incremental.
9. A hand-coded reset rule solves the toy.
10. The method depends on reliable regime-boundary signals.

## V2 outcome

Attacks 9 and 10 define the final boundary. The regime-reset rule reaches 1.000 accuracy, so the paper should not claim learned-gate novelty. Boundary corruption also matters: reset performance falls to 0.878 overall and 0.842 at switch points under 20% regime-boundary flips.
