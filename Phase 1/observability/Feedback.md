# Observability Feedback

## Initial cross-topic review — 2026-10-18

Five existing evaluated attempts are linked in [Progress.md](Progress.md) and [the answer index](questions/README.md). No new attempt, retrospective score or independent readiness claim is created.

**Demonstrated strengths:** Linux Q03 recognizes that low CPU does not exclude a bottleneck; Linux Q04 proposes service logs and memory measurements; Linux Q10 identifies the old log-file descriptor and values evidence preservation; Kubernetes Q02 proposes logs and resource measurements.

**Gaps carried forward:** Linux Q03 mixes latency/capacity and lacks task-state proof; Linux Q04 lacks explicit OOM evidence; Linux Q10 lacks confirmation of reopening/new writes. Kubernetes Q08 assumes healthy/Running DNS pods imply overload. Recovery criteria recur as a weakness across these records.

**Status:** These are existing gaps, not newly resolved skills. No observability-specific numeric scores were recorded for these attempts, so the average remains N/A. Broader tracing, alerting and SLO design remain unassessed.

For future relevant attempts, append the canonical link, demonstrated evidence, any explicitly assessed subscore and a recovery verdict against earlier gaps. Retain original topic scores and avoid duplicating questions.

## AWS Q01 — 2026-10-18

[Canonical answer](../aws/questions/Q01-alb-unhealthy-targets.md). No observability subscore assigned. Service-health reasoning partially improved relative to Kubernetes Q08: passing EC2 checks did not prevent investigating application listener/logs and health path. Diagnosis still assumes infrastructure was unchanged without proof. Recovery verification remains unresolved relative to Linux Q03/Q04/Q10: no real-request, target-health or latency/error success criteria. No new coverage aspect completed; four of ten remain sampled.

## AWS Q02 — 2026-10-18

[Answer](../aws/questions/Q02-s3-kms-access-denied.md): recovery verification partially improved from AWS Q01 through explicit retrieval-success monitoring. Exact-role/object testing and denial evidence remain missing. No separate subscore; coverage stays 4/10, with full recovery verification unchecked.

## AWS Q03 — 2026-10-18

[Answer](../aws/questions/Q03-rds-failover-connectivity.md): application dashboards and DNS checks provide partial recovery evidence; concrete transactions and error/latency acceptance criteria remain absent. Verification remains partially improved, not resolved. No separate subscore or new coverage check.

## AWS Q04 — 2026-10-19

[Answer](../aws/questions/Q04-s3-endpoint-nat-routing.md): names payment success and upload failures as recovery signals. Verification remains partially improved: direct tests from app subnets and route/cost evidence absent. No separate subscore or new coverage check; 4/10 aspects remain sampled.
