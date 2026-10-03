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

## Q03 — HPA / Pending / Cluster Autoscaler — 2026-10-03

Score: 5/10
Interview Acceptance Probability: 40% (subjective estimate for this answer).

✅ Strong
- Correctly identified requests rather than live usage as the central scheduling issue.
- Distinguished requests from limits and gave a more direct, concise answer.

⚠️ Improve
- Compare requests with remaining per-node allocatable capacity, not average usage. A high request does not mean the pod can never schedule.
- Autoscaler investigation was not answered: check logs, eligible group fit/max size, discovery/permissions, and AWS launch activity.
- Specify evidence and the resulting mitigation rather than referring generally to previous commands.
- Explain safe restoration and validation; do not lower requests blindly to make pods fit.

| Evaluation dimension | Assessment |
| --- | --- |
| Technical accuracy | Scheduling principle correct; average-usage/never-schedules wording inaccurate |
| Coverage | Scheduling covered; Autoscaler and recovery sections missing |
| Interview representation | Direct explanation, but incomplete response to the scenario |
| Conciseness | Improved; no lengthy administrative opening |
| Troubleshooting approach | No concrete Autoscaler evidence or decision sequence |
| Senior-level reasoning | Needs distinction between scheduling, scaling and cloud provisioning failures |

Main deduction is missing two central parts of the question, not missing command volume. Autoscaler teaching was requested and is recorded in the answer file; it is not credited as independent knowledge. Queue autoscaling for a later retest and rotate to networking now.

## Q04 — Cross-Namespace NetworkPolicy — 2026-10-03

Score: 6.5/10
Interview Acceptance Probability: 60% (subjective answer-specific estimate).

✅ Strong
- Correct primary hypothesis linked to the recent policy change.
- Understood that Ready endpoints do not guarantee reachability.
- Concise response with sensible exec/connectivity and policy checks.

⚠️ Improve
- Check source egress as well as destination ingress.
- Define the narrow fix: correct namespace/pod selectors and application port, keeping isolation intact.
- Missing ingress permission in one policy is not conclusive: native policies are additive, and unrestricted pods need no explicit allow.
- Test from the affected frontend; ClusterIP failure means DNS alone cannot explain the incident.
- Validate allowed traffic succeeds and intentionally denied traffic stays blocked; confirm application recovery.

| Evaluation dimension | Assessment |
| --- | --- |
| Technical accuracy | Main explanation sound; missing egress and policy-isolation/additive nuance |
| Coverage | Primary cause covered; precise fix and verification incomplete |
| Interview representation | Clear and directly relevant |
| Conciseness | Good; no penalty for short length |
| Troubleshooting approach | Useful starting tools; specify source, policy contents and expected evidence |
| Senior-level reasoning | Needs least-privilege change and positive/negative validation |

Main deductions: omitted source egress, underspecified safe fix, and missing validation. Queue these for a later retest; move to storage for broader coverage.

## Q05 — EBS Multi-Attach — 2026-10-03

Score: 4.5/10
Interview Acceptance Probability: 35% (subjective answer-specific estimate).

✅ Strong
- Correctly identified EBS's AZ restriction.
- Recognized the old-node attachment as relevant.

⚠️ Improve
- Multi-Attach can occur within one AZ; the question did not establish an AZ change. Distinguish attachment conflict from topology mismatch.
- Same-AZ placement does not clear a stale attachment. Verify the old instance cannot write before detachment/recovery.
- Switching a StorageClass provisioner does not migrate an existing EBS volume/data to EFS; EFS requires a deliberate migration and may not suit the application.
- Do not promise zero data loss. Include fencing, normal CSI detachment, integrity validation and tested backups.
- Gather pod/PV/VolumeAttachment and AWS attachment evidence before choosing the fix.

| Evaluation dimension | Assessment |
| --- | --- |
| Technical accuracy | EBS locality correct; attachment/AZ causes conflated and storage migration misunderstood |
| Coverage | Safe recovery, verification and recurrence prevention largely missing |
| Interview representation | Clear explanation but confident unsupported assumptions |
| Conciseness | Focused; repeated AZ explanation could be shorter |
| Troubleshooting approach | No evidence checks to distinguish attachment state from topology |
| Senior-level reasoning | Data-safety safeguards and migration trade-offs are central gaps |

Main deductions are the incorrect proposed recovery and missing writer-safety checks, not lack of command volume. Queue storage safety for spaced retesting; rotate to identity next.
