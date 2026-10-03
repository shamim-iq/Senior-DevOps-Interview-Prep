# Kubernetes Interview Feedback

Feedback records actual strengths, mistakes, and improvement areas after each attempt.

Each evaluation covers technical accuracy, coverage, interview representation, conciseness, troubleshooting approach, and senior-level reasoning.

Scores are out of 10. Interview Acceptance Probability is a subjective estimate for the specific answer, not a measured probability or overall hiring probability.

Consolidated feedback will be added after every 10 evaluated questions.

## Q01 — Deployment CrashLoopBackOff — 2026-10-02

Score: 6/10
Interview Acceptance Probability: 55% (subjective estimate for this answer).

✅ Strong
- Good incident ownership, dashboard triage and stakeholder communication.
- Identified logs/events and configuration as useful evidence.
- Understood restart backoff and explicitly prioritized rollback before deep RCA.

⚠️ Improve
- Lead with mitigation; avoid a long administrative preamble or unverified recovery promises.
- Correct command syntax; add previous-container logs, Last State, exit reason and probe checks.
- Do not jump from CrashLoopBackOff to larger nodes. Establish container-limit OOM versus node pressure versus application failure.
- Separate native ConfigMaps/Secrets from AWS-backed retrieval; IRSA trust failure affects STS credential exchange, not generally token issuance.
- Compare healthy/failing ReplicaSets and investigate readiness, Service endpoints and ingress 502 evidence.
- Explain safe GitOps rollback, recovery validation and prevention before redeploying.

| Evaluation dimension | Assessment |
| --- | --- |
| Technical accuracy | Mixed: sound fundamentals with command, resource and identity errors |
| Coverage | Partial: limited routing, probe, validation and prevention detail |
| Interview representation | Responsible ownership; prioritize concrete actions |
| Conciseness | Over-explained incident administration |
| Troubleshooting approach | Useful starting checks; hypotheses need evidence |
| Senior-level reasoning | Good recovery priority; GitOps safeguards and trade-offs missing |

Priority retests: memory limits versus node capacity; later revisit IRSA and GitOps rollback. One answer is insufficient to establish recurring mistakes or overall readiness.

## Q02 — Memory Limit / OOMKilled — 2026-10-03

Score: 6.5/10
Interview Acceptance Probability: 62% (subjective estimate for this answer).

✅ Strong
- Correctly rejected larger nodes as a fix for an unchanged container memory limit.
- Connected traffic, memory demand and repeated restarts; proposed measuring usage before adjusting the limit.
- Included useful pod inspection, previous logs and metrics commands: improvement over Q01.

⚠️ Improve
- OOMKilled does not prove bad YAML; consider leaks, cache growth, concurrency and release regressions.
- Distinguish scheduling requests from enforced limits explicitly.
- Before raising limits, check capacity for all replicas and rollout overhead; apply a controlled GitOps change with rollback available.
- Answer the requested validation/follow-up: no new OOMs, stable peak-load memory, customer recovery, load testing and prevention.
- Lead with the supplied evidence instead of a long observability preamble. Give an update cadence, not an unsupported recovery ETA.
- Inspect Last State, not just Events. Current top may miss peaks; exec/top is optional and may be unavailable in minimal or restarting containers. Include namespaces consistently.

| Evaluation dimension | Assessment |
| --- | --- |
| Technical accuracy | Core diagnosis correct; assumes misconfiguration and leaves request/limit distinction implicit |
| Coverage | Diagnosis and initial fix covered; validation and follow-up largely absent |
| Interview representation | Good ownership; lead with the direct scenario answer |
| Conciseness | Administrative preamble and lower-value commands distract |
| Troubleshooting approach | Improved evidence gathering; alternative hypotheses still limited |
| Senior-level reasoning | Correct node trade-off; change safety and long-term diagnosis need detail |

Emerging repeated gaps across Q01–Q02: unsupported recovery ETA, lengthy opening, narrow hypotheses, and incomplete recovery validation. Retest capacity/scheduling reasoning next; do not treat this assisted correction as proof of broad resource mastery.
