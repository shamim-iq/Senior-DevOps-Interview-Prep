# CI/CD Feedback

## Q01 — 2026-10-25

**8.5/10; 80% subjective answer-specific estimate.** [Evaluation](questions/Q01-deployment-check-gates.md). Strong dependency diagnosis and production approval reasoning. Clarify deploy needs all three required jobs; success() does not wait for unrelated jobs. Graph useful but deliberately test failed/skipped/all-success and approval paths. Deductions 0.5 precision and 1 verification, no syntax-volume penalty. One answer is insufficient for overall readiness. Prior Kubernetes verification gap persists here as missing negative-path evidence.

## Q02 — 2026-10-25

**6.5/10; 60% subjective estimate.** [Evidence](questions/Q02-tested-artifact-promotion.md). Credit same-image intent, release tags and progressive rollout/metrics. Need digest/immutable handoff, correct GitOps-versus-Rollouts roles and precise rollback recovery. Opening interpreted as rejecting redundant rebuild; no speech penalty. First-two average 7.5/10. Observability signals named but thresholds/verified outcome not demonstrated.
