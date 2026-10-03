# Kubernetes Interview Progress

| Metric | Current status |
| --- | --- |
| Questions Attempted | 4 / 10 in the first cycle |
| Average Score | 6/10 — (6 + 6.5 + 5 + 6.5) / 4 |
| Average Acceptance Probability | 54.25% — (55 + 62 + 40 + 60) / 4; subjective answer-specific estimates |
| Topic Coverage | Q01: deployment failure, incident triage, GitOps; Q02: memory limits/OOM; Q03: request-based scheduling; autoscaling gaps identified; Q04: NetworkPolicy isolation; identity sampled |
| Current Strengths | Incident ownership, previous logs, measuring usage, distinguishing larger nodes from container limits |
| Current Weaknesses | Alternative causes, request/limit precision, capacity-aware mitigation, IRSA distinction, recovery validation and conciseness |
| Readiness Trend | 6 → 6.5 → 5 → 6.5; clearer communication, but safe fixes and validation remain recurring gaps |

## ☑️ Kubernetes Coverage Checklist

**Initial assessment coverage: 5 / 21 aspects (23.8%). Questions completed: 4 / 10 (40%).** These measure different things: one question can assess multiple aspects, and neither percentage is a readiness score.

`[x] ✅` = substantively attempted and evaluated at least once, with question evidence. `[ ]` = not yet assessed sufficiently, including pending questions and concepts only discussed in follow-ups. Checked aspects can still require revision. The overall topic roadmap lives in the [root README](../../README.md).

- [x] ✅ Pod/Deployment troubleshooting and CrashLoopBackOff — Q01; command accuracy and alternative causes need revision.
- [x] ✅ Memory requests/limits and OOMKilled — Q02; capacity safeguards and request semantics need revision.
- [x] ✅ Incident triage and communication — Q01–Q02; shorten opening and avoid unsupported recovery ETAs.
- [ ] ImagePullBackOff — not assessed.
- [x] ✅ Pending pods and scheduling resources — Q03; per-node allocatable precision needs revision.
- [ ] Taints, tolerations and affinity — not assessed.
- [ ] Services, Ingress, EndpointSlices and readiness — follow-up explanations given; independent scenario assessment pending.
- [ ] CoreDNS and service discovery — not assessed.
- [x] ✅ NetworkPolicy isolation — Q04; egress, narrow permissions and validation need revision.
- [ ] CNI networking and enforcement troubleshooting — not assessed.
- [ ] HPA behavior and metrics — Q03 touched replica changes; metrics reasoning still requires assessment.
- [ ] Cluster Autoscaler and node capacity — Q03 investigation unanswered; explanation provided, retest pending.
- [ ] PV/PVC and CSI storage troubleshooting — not assessed.
- [ ] RBAC and ServiceAccounts — not assessed.
- [ ] IRSA/OIDC and Azure workload identity — misconception sampled in Q01; dedicated assessment pending.
- [ ] Node maintenance, upgrades and PDBs — not assessed.
- [ ] Helm and Argo CD release management — rollback mentioned in Q01; broader assessment pending.
- [ ] Prometheus and EFK/ELK investigation — generic dashboard/log usage only; tool-specific assessment pending.
- [ ] EKS production architecture and trade-offs — scenario setting used; platform-specific depth pending.
- [ ] AKS production scenarios — not assessed.
- [ ] Recovery validation, prevention and SLI/SLO reasoning — gaps identified in Q01–Q02; substantive demonstration pending.

CNI and NetworkPolicy are tracked separately from Q04 onward (21 aspects rather than 20) so policy assessment does not imply CNI coverage. The first 10 questions may combine aspects. Extend the cycle when needed to assess uncovered areas; do not check boxes merely to meet the question target.

## 🔁 Revision and Readiness Activities

These boxes mean the activity has been completed with recorded evidence, not merely discussed.

- [ ] Demonstrate accurate, concise essential commands in a fresh scenario.
- [ ] Explain requests versus limits and capacity implications independently.
- [ ] Consider alternative causes before selecting an infrastructure change.
- [ ] Demonstrate safe mitigation, rollback and measurable recovery validation.
- [ ] Correct workload-identity misconceptions in a fresh scenario.
- [ ] Deliver concise answers with realistic stakeholder updates.
- [ ] Complete the first 10 evaluated questions and consolidated feedback.
- [ ] Retest outstanding weak areas and record results.
- [ ] Review overall Kubernetes readiness against coverage and retest evidence.

## Active Question

Q05 — Persistent storage and CSI; awaiting an answer. Rotate to storage after networking.

An EKS StatefulSet uses an EBS-backed PersistentVolume. After a node failure, a replacement pod is scheduled on another node but remains ContainerCreating. Its PVC is Bound, and pod events report a Multi-Attach error for the volume. The application stores customer data. How would you investigate and restore service without risking data corruption, and what would you improve to reduce recurrence?

## Coverage Plan

Across the first 10 questions, assess deployment and pod failures; Services, Ingress, DNS and networking; scheduling; resource management; autoscaling; storage; workload identity and RBAC; maintenance and PDBs; GitOps; and observability in realistic EKS/AKS scenarios. Combine related areas and adapt difficulty to demonstrated performance.

Prioritize unchecked aspects when choosing new questions. Avoid more than two consecutive questions centered on the same aspect unless explicitly requested. Queue weak areas for spaced retesting instead of repeatedly revisiting them immediately. Q05 moves to storage; autoscaling and NetworkPolicy weaknesses are queued for later retesting. Review coverage after each answer and at each 10-question checkpoint; continue beyond 10 if aspects remain unassessed.

## Session Rules

- Ask one scenario at a time; do not reveal hints or answers before an attempt.
- Before each new question, inspect existing question files and this active-question record to avoid duplicates.
- After each answer: evaluate, provide concise feedback, save the correct answer in questions/QNN-<topic>.md, append feedback, update progress, then ask the next question.
- Question files use: Question, 🎯 Scenario, ✅ Interview-Ready Answer, 🔍 Troubleshooting / Reasoning Flow, 🧠 Key Points, 🔄 Diagram (if useful), and 📌 Senior-Level Takeaway.
- Preserve previous answers and scores; keep numbering sequential.
- Derive all performance metrics from actual evaluated answers. Unassessed topics remain N/A.
- After each 10 questions, consolidate strong/moderate/weak areas, recurring mistakes, communication, technical depth, revision priorities, and readiness.

## Evaluation History

| Question | Date | Score | Acceptance estimate | Record |
| --- | --- | --- | --- | --- |
| Q01 | 2026-10-02 | 6/10 | 55% | [Deployment CrashLoopBackOff](questions/Q01-deployment-crashloop.md) |
| Q02 | 2026-10-03 | 6.5/10 | 62% | [Memory Limit / OOMKilled](questions/Q02-memory-limit-oomkilled.md) |
| Q03 | 2026-10-03 | 5/10 | 40% | [HPA / Pending / Autoscaler](questions/Q03-hpa-pending-autoscaler.md) |
| Q04 | 2026-10-03 | 6.5/10 | 60% | [Cross-Namespace NetworkPolicy](questions/Q04-networkpolicy-cross-namespace.md) |

## Retesting and Coverage

- Next: EBS persistent storage and CSI attachment recovery (Q05).
- Q02 improved the larger-node misconception; revisit requests/limits and safe capacity planning in a different scenario.
- Later: AWS workload identity and native configuration; GitOps rollback safeguards; request-path diagnosis and recovery validation.
- Scheduling assessed in Q03; Autoscaler diagnosis needs a later retest. HPA metrics, storage, maintenance and CoreDNS remain unassessed. Q04 assessed NetworkPolicy basics; AKS-specific platform depth remains unassessed.
- No mastery percentages inferred from four answers. Current score movement is descriptive, not proof of overall senior readiness.
