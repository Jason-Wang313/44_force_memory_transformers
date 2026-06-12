# Reviewer Attacks

1. "This is just a transformer over force history."
- Response: the central mechanism is explicit force-memory management and forgetting, not sequence encoding.

2. "This is close to tactile memory / retrieval."
- Response: retrieval alone does not manage state lifecycle or stale-contact invalidation.

3. "The gains come from extra parameters."
- Response: the key ablation must hold capacity roughly fixed and isolate forgetting.

4. "The task is synthetic and too simple."
- Response: synthetic tests are used to expose the failure mode cleanly; the paper should be honest that broader real-robot validation is limited.

5. "Forgetting is obvious."
- Response: it is only obvious in hindsight; the paper must demonstrate that naive retention hurts and that the forgetting test is what fixes it.

6. "This could be solved by better data."
- Response: better data helps, but the mechanism specifically addresses stale force evidence under regime shift.

7. "This is just a world model."
- Response: world models predict futures; this work manages contact-memory validity.

8. "The novelty is incremental."
- Response: the paper should clearly separate encoding, retrieval, and lifecycle management, and show the latter is the missing piece.
