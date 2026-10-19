# Observability Progress

**Integrated practice only — 2026-10-18.** Assess observability within Kubernetes, Linux, AWS, CI/CD, Terraform, RAG and other relevant scenarios. No separate topic cycle, standalone question quota or automatic switch to Observability.

## Metrics

| Metric | Status |
| --- | --- |
| Linked evaluated attempts | 9 attempts indexed; not new questions |
| Standalone questions | 0; none planned |
| Observability-specific average | N/A — historical overall topic scores are not observability subscores |
| Coverage | 4 / 10 aspects substantively sampled; coverage is not mastery |
| Readiness | Partial evidence; metric interpretation and recovery verification need retesting |

## Coverage

- [x] ✅ Host resource metrics and bottleneck interpretation — Linux Q03/Q04.
- [x] ✅ Container resource metrics and restart investigation — Kubernetes Q02.
- [x] ✅ Service-health diagnosis versus process/pod status — Kubernetes Q08 / AWS Q01.
- [x] ✅ Log rotation, continuity and evidence preservation — Linux Q10.
- [ ] Central log collection, searching, retention and sensitive-data handling.
- [ ] Distributed tracing and correlation between logs, metrics and traces.
- [ ] SLIs, SLOs and error budgets.
- [ ] Actionable alerts, thresholds, routing and alert noise.
- [ ] Instrumentation, dashboards, metric labels/cardinality and telemetry cost.
- [ ] Concrete recovery criteria and verification under representative traffic.

## Evidence map

| Canonical answer | Observability evidence from actual attempt | Remaining gap |
| --- | --- | --- |
| [Linux Q03](../linux/questions/Q03-high-load-low-cpu.md) | vmstat/I/O investigation; rejected CPU-only diagnosis | Task-state evidence; latency versus capacity; recovery criteria |
| [Linux Q04](../linux/questions/Q04-memory-process-termination.md) | Service logs and memory measurements | Prove termination cause; available memory/limits; recovery checks |
| [Linux Q10](../linux/questions/Q10-logrotate-open-file.md) | Old file-descriptor reasoning and evidence preservation | Confirm open file, supported reopening and successful new writes |
| [Kubernetes Q02](../kubernetes/questions/Q02-memory-limit-oomkilled.md) | Peak memory, restart logs and resource metrics | Establish cause from evidence rather than assuming bad limits; verify stability |
| [Kubernetes Q08](../kubernetes/questions/Q08-coredns-servfail.md) | DNS failure/health reasoning substantively assessed | Running pods do not prove successful queries or overload; isolate and verify |
| [AWS Q01](../aws/questions/Q01-alb-unhealthy-targets.md) | App listener/logs and health-path diagnosis despite passing EC2 checks | Concrete recovery metrics/requests absent; deployment correlation is not proof |
| [AWS Q02](../aws/questions/Q02-s3-kms-access-denied.md) | Retrieval-success monitoring after access fix | Actual-role read and denial evidence missing; recovery partially improved |
| [AWS Q03](../aws/questions/Q03-rds-failover-connectivity.md) | App-level monitoring and DNS lookup | Real transactions, exact error/latency criteria and data checks remain missing |
| [AWS Q04](../aws/questions/Q04-s3-endpoint-nat-routing.md) | Separate payment success and upload failures | Direct path testing and NAT cost/byte evidence missing |

This is an initial evidence index, not an exhaustive remapping of every answer. Reference answers contain coaching that must not be counted as candidate-demonstrated skill.

## Ongoing workflow

- Ask one scenario in the active topic; include observability only where operationally relevant. Do not add a separate question quota or extend Terraform's current five-follow-up cap.
- Keep the canonical answer and overall score in its original topic. Add links here and in questions/README.md after a substantive attempt; do not duplicate answers or count an attempt twice.
- Update Feedback.md with the demonstrated observability strengths/gaps. Record a clearly justified observability subscore only if explicitly assessed; otherwise leave it N/A. Never copy an overall Linux/Kubernetes score into this average.
- Mark coverage only after an attempt and evaluation. Retest weaknesses through future topic scenarios, recording resolved, partially improved or unresolved with evidence; explanations alone do not close gaps.
- Keep the user's current topic/pending question unchanged. No standalone Observability practice unless requested later.

## Revision

- [ ] Distinguish measured evidence from hypotheses; interpret task states, latency, memory and service health correctly.
- [ ] Use specific before/after signals to prove recovery.
- [ ] Confirm logging continuity without losing required evidence.
- [ ] Cover the remaining unchecked aspects naturally through other topics.
