# CI/CD Feedback

## Q02.1 coached retry - 2026-10-26

**7/10; 65% subjective answer-specific estimate.** [Evidence](questions/Q02.1-artifact-promotion-retry.md). CD/Rollouts roles resolved in this coached attempt. Digest use and Git alignment partially improved; commit-ID tagging is not digest identity. Deductions: 1 artifact selection/commit-tag equivalence; 1 missing approval/test/manifest/runtime evidence chain; 1 missing recovery verification. Abort/undo is credited; clarify that abort does not inherently cause a GitOps redeployment loop. No wording/spelling penalties. Q02 remains 6.5/10; main-question average 7.5/10. Recovery signals unresolved; independent mastery not established. Q03 preserved.

## Q01 — 2026-10-25

**8.5/10; 80% subjective answer-specific estimate.** [Evaluation](questions/Q01-deployment-check-gates.md). Strong dependency diagnosis and production approval reasoning. Clarify deploy needs all three required jobs; success() does not wait for unrelated jobs. Graph useful but deliberately test failed/skipped/all-success and approval paths. Deductions 0.5 precision and 1 verification, no syntax-volume penalty. One answer is insufficient for overall readiness. Prior Kubernetes verification gap persists here as missing negative-path evidence.

## Q02 — 2026-10-25

**6.5/10; 60% subjective estimate.** [Evidence](questions/Q02-tested-artifact-promotion.md). Credit same-image intent, release tags and progressive rollout/metrics. Need digest/immutable handoff, correct GitOps-versus-Rollouts roles and precise rollback recovery. Opening interpreted as rejecting redundant rebuild; no speech penalty. First-two average 7.5/10. Observability signals named but thresholds/verified outcome not demonstrated.

## Q03 — 2026-10-26

**8.5/10; 80% subjective answer-specific estimate.** [Evidence](questions/Q03-oidc-deployment-identity.md). Credit precise repository/environment intent, id-token permission, role ARN and CloudTrail. Deduct 0.75 for incomplete trust/resource boundary diagnosis and 0.75 for verification limited to retry/audit logs. No separate deduction for token terminology. Previous verification weakness partially improved through named audit evidence, not yet recovered through operation/denial tests. Main average 7.83/10; Q04 pending.
