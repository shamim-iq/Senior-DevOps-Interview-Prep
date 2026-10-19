# AWS Interview Feedback

Started 2026-10-18. Five evaluated AWS attempts; average 7.10/10. Q05 remains deferred. Readiness evidence is preliminary.

Evaluate at the four-year DevOps / Platform baseline. Credit correct reasoning; separate material errors, omissions, minor slips and optional advanced coaching. Do not penalize concise answers for irrelevant command omissions.

For each attempt, record the canonical question link, actual answer summary, score, credited strengths, explained deductions, subjective answer-specific acceptance estimate and revision needs. Preserve history and clearly distinguish coached revisions from independent retests.

For follow-ups, compare with the original gaps using resolved, partially improved or still unresolved, citing evidence. Mark unrelated areas not reassessed. Cross-link observability evidence where substantively assessed without duplicating the overall AWS score.

Consolidate after Q10; use up to five targeted follow-ups if needed. Maximum 15 questions, then a final evidence-based verdict with remaining limitations.

## Q01 — ALB Unhealthy Targets — 2026-10-18

[Canonical answer](questions/Q01-alb-unhealthy-targets.md). **7/10; subjective answer-specific acceptance estimate 65%, not hiring probability.**

Credit: private isolation, deployment correlation, port/path mismatch, target health and application investigation. Deductions: 1 missing concrete restoration, 1 missing recovery criteria, 1 combined unsupported exclusion of infrastructure and omitted narrow ALB/instance access check. No penalty for concise Linux commands, opening transcription ambiguity or unspecified 503 origin. Record observability evidence without duplicating this score. Q02 rotates to IAM/S3/KMS access diagnosis.

## Q02 — S3/KMS AccessDenied — 2026-10-18

[Canonical answer](questions/Q02-s3-kms-access-denied.md). **7/10; subjective acceptance estimate 65%, not hiring probability.** Correct KMS authorization diagnosis, rejection of excessive access and retrieval-success monitoring. Deductions: 1 key policy; 1 combined denial evidence/actual-role test; 0.5 default-encryption misconception; 0.5 exact-key scope. Role/profile terminology clarified without separate penalty.

Recovery: Q01 missing action resolved in this scenario; verification partially improved through retrieval success but identity-specific proof remains. Networking/rollback gaps not reassessed. Q03 rotates to RDS failover and application recovery.

## Q03 — RDS Failover Connectivity — 2026-10-18

[Canonical answer](questions/Q03-rds-failover-connectivity.md). **7/10; subjective acceptance estimate 65%, not hiring probability.** Credit endpoint/DNS diagnosis, standby promotion and dashboard verification. Deductions: 1 incorrect DR-Region location; 1 incomplete runtime cache/pool reconnection; 1 combined unconditional data-safety claim and missing transaction/data verification. No additional terminology/tooling penalty.

Recovery: Q01 mitigation and Q01/Q02 verification partially improved, with explicit cache action and app-health observation; concrete pool/transaction recovery remains. IAM/KMS and ALB-specific gaps not reassessed. Q04 covers private networking/endpoints and NAT cost/reliability.

## Q04 — S3 Endpoint and NAT — 2026-10-19

[Canonical answer](questions/Q04-s3-endpoint-nat-routing.md). **7/10; subjective acceptance estimate 65%, not hiring probability.** Credit traffic separation, retained payment egress, S3 private access and monitoring both outcomes. Deductions: 1.5 gateway selection/concrete routing; 1 access checks; 0.5 direct operation/path/cost verification. Advanced NAT resilience is coaching, not a further penalty.

Recovery: verification remains partially improved; previous concrete-network/access checks still unresolved. Other gaps not reassessed. Q05 rotates to Lambda/SQS processing and safe retries.

## Q06 — CloudFront Private S3 403 — 2026-10-19

[Canonical answer](questions/Q06-cloudfront-private-s3-403.md). **7.5/10; subjective acceptance estimate 70%, not hiring probability.** Credit policy/path diagnosis, private bucket and actual browser test via CloudFront. Deductions: 1.5 specific origin identity/permission scope; 0.5 cache precision; 0.5 content/assets and access-boundary verification. No command or advanced-feature penalty.

Recovery: actual-path test selection resolved in this scenario relative to dashboard-only answers; full recovery proof and exact policy evaluation partially improved. Other gaps not reassessed. Fifth evaluated attempt; Q05 unassessed. Q07 rotates to ECS/Fargate image delivery.
