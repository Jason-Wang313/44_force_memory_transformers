# Submission Attack Log

## Attack: hard reset solves the toy

Question: Does the learned gate matter if a clean regime-reset rule reaches perfect toy accuracy?

Result: the v2 stress showed that clean hard reset is stronger in the toy. The v3 suite treats this as a constraint and evaluates lifecycle management under corrupted, delayed, missing, and false reset conditions.

Decision impact: final paper does not claim learned-gate novelty.

## Attack: reset can hurt

Question: Does forgetting always help?

Result: no. Negative controls and false-reset metrics show that premature reset can damage stable contact behavior.

Decision impact: final paper frames the problem as retention/reset balance.

## Attack: overall accuracy hides the mechanism

Question: Can average accuracy obscure stale-memory failures?

Result: yes. The v3 suite reports switch accuracy, stale-memory error, missed resets, false resets, boundary F1, retention calibration, sequence success, and force overshoot.

Decision impact: supports lifecycle metrics beyond overall accuracy.

## Attack: real-robot readiness

Question: Is there hardware or high-fidelity contact evidence?

Result: no. The paper is framed as a full-scale synthetic mechanism study with hardware validation plans and falsification criteria.

Decision impact: limits the claim to representation, metrics, and diagnostics.
