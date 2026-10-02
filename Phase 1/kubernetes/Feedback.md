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
