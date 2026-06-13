# Claims

## Main claim

Force history in contact-rich manipulation should be managed as state with an explicit lifecycle, because stale force history can mislead a policy after contact regimes change.

## V2 narrowed claim

The synthetic task does not establish learned-gate superiority. A hand-coded regime-reset rule reaches 1.000 overall and switch-point accuracy, while the learned forget gate reaches 0.977 overall and 0.723 switch-point accuracy. The safe claim is that reset-aware force-memory lifecycle management matters, not that the proposed gate is uniquely necessary.

## Supported evidence

- Flat transformer: 0.971 overall accuracy, 0.650 switch-point accuracy.
- Learned forget gate: 0.977 overall accuracy, 0.723 switch-point accuracy.
- Regime-reset rule: 1.000 overall accuracy, 1.000 switch-point accuracy.
- Reset rule with 20% regime-boundary flips: 0.878 overall accuracy, 0.842 switch-point accuracy.

## What not to overclaim

- No universal theorem for all manipulation.
- No hardware or full robotics benchmark.
- No claim that the learned gate beats simple reset rules when clean regime boundaries are available.
