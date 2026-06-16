# Reviewer Attacks

1. A hard reset rule already solves the toy.
2. This is just a transformer variant.
3. Overall accuracy hides boundary failures.
4. Reset can hurt stable contact phases.
5. Boundary labels may be corrupted or delayed.
6. Stale force memory is synthetic.
7. Hardware force safety is not proven.
8. Sensor quality may dominate memory design.

## v3 response

Attack 1 is accepted and built into the final design. The final paper includes hard reset, hysteresis reset, noisy-boundary reset, learned reset classifier, and oracle lifecycle memory.

Attacks 3, 4, and 5 are addressed with lifecycle metrics, negative controls, and boundary-corruption stresses.

Attacks 6 and 7 remain limitations. The paper is explicit that the suite is synthetic and diagnostic. The hardware validation and falsification sections specify what future robot evidence must test.
