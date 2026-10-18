# Observability Feedback

## Initial cross-topic review — 2026-10-18

Five existing evaluated attempts are linked in [Progress.md](Progress.md) and [the answer index](questions/README.md). No new attempt, retrospective score or independent readiness claim is created.

**Demonstrated strengths:** Linux Q03 recognizes that low CPU does not exclude a bottleneck; Linux Q04 proposes service logs and memory measurements; Linux Q10 identifies the old log-file descriptor and values evidence preservation; Kubernetes Q02 proposes logs and resource measurements.

**Gaps carried forward:** Linux Q03 mixes latency/capacity and lacks task-state proof; Linux Q04 lacks explicit OOM evidence; Linux Q10 lacks confirmation of reopening/new writes. Kubernetes Q08 assumes healthy/Running DNS pods imply overload. Recovery criteria recur as a weakness across these records.

**Status:** These are existing gaps, not newly resolved skills. No observability-specific numeric scores were recorded for these attempts, so the average remains N/A. Broader tracing, alerting and SLO design remain unassessed.

For future relevant attempts, append the canonical link, demonstrated evidence, any explicitly assessed subscore and a recovery verdict against earlier gaps. Retain original topic scores and avoid duplicating questions.

## AWS Q01 — 2026-10-18

[Canonical answer](../aws/questions/Q01-alb-unhealthy-targets.md). No observability subscore assigned. Service-health reasoning partially improved relative to Kubernetes Q08: passing EC2 checks did not prevent investigating application listener/logs and health path. Diagnosis still assumes infrastructure was unchanged without proof. Recovery verification remains unresolved relative to Linux Q03/Q04/Q10: no real-request, target-health or latency/error success criteria. No new coverage aspect completed; four of ten remain sampled.
