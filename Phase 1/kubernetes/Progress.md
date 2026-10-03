# Kubernetes Interview Progress

| Metric | Current status |
| --- | --- |
| Questions Attempted | 8 / 10 in the first cycle |
| Average Score | 5.75/10 — (6 + 6.5 + 5 + 6.5 + 4.5 + 7 + 5.5 + 5) / 8 |
| Average Acceptance Probability | 50.25% — (55 + 62 + 40 + 60 + 35 + 65 + 45 + 40) / 8; subjective answer-specific estimates |
| Topic Coverage | Q01: deployment failure, incident triage, GitOps; Q02: memory limits/OOM; Q03: request-based scheduling; autoscaling gaps identified; Q04: NetworkPolicy isolation; Q05: EBS/PVC/CSI recovery; Q06: IRSA/ServiceAccount identity; Q07: node maintenance/PDB; Q08: CoreDNS |
| Current Strengths | Incident ownership, previous logs, measuring usage, distinguishing larger nodes from container limits, Helm identity-regression hypothesis and permission restraint |
| Current Weaknesses | Alternative causes, request/limit precision, capacity-aware mitigation, IRSA distinction, storage attachment/migration safety, recovery validation and conciseness |
| Readiness Trend | 6 → 6.5 → 5 → 6.5 → 4.5 → 7 → 5.5 → 5; evidence-based diagnosis and recovery validation remain recurring gaps |

## ☑️ Kubernetes Coverage Checklist

**Initial assessment coverage: 9 / 22 aspects (40.9%). Questions completed: 8 / 10 (80%).** These measure different things: one question can assess multiple aspects, and neither percentage is a readiness score.

`[x] ✅` = substantively attempted and evaluated at least once, with question evidence. `[ ]` = not yet assessed sufficiently, including pending questions and concepts only discussed in follow-ups. Checked aspects can still require revision. The overall topic roadmap lives in the [root README](../../README.md).

- [x] ✅ Pod/Deployment troubleshooting and CrashLoopBackOff — Q01; command accuracy and alternative causes need revision.
- [x] ✅ Memory requests/limits and OOMKilled — Q02; capacity safeguards and request semantics need revision.
- [x] ✅ Incident triage and communication — Q01–Q02; shorten opening and avoid unsupported recovery ETAs.
- [ ] ImagePullBackOff — not assessed.
- [x] ✅ Pending pods and scheduling resources — Q03; per-node allocatable precision needs revision.
- [ ] Taints, tolerations and affinity — not assessed.
- [ ] Services, Ingress, EndpointSlices and readiness — follow-up explanations given; independent scenario assessment pending.
- [x] ✅ CoreDNS and service discovery — Q08; confirm saturation versus configuration/API issues and validate recovery.
- [x] ✅ NetworkPolicy isolation — Q04; egress, narrow permissions and validation need revision.
- [ ] CNI networking and enforcement troubleshooting — not assessed.
- [ ] HPA behavior and metrics — Q03 touched replica changes; metrics reasoning still requires assessment.
- [ ] Cluster Autoscaler and node capacity — Q03 investigation unanswered; explanation provided, retest pending.
- [x] ✅ PV/PVC and CSI storage troubleshooting — Q05; attachment versus AZ constraints, fencing and migration need revision.
- [ ] RBAC and ServiceAccounts — ServiceAccount linkage sampled in Q06; Kubernetes authorization still needs assessment.
- [x] ✅ IRSA/OIDC — Q06; exact trust conditions and validation need revision.
- [ ] Azure workload identity — not assessed.
- [x] ✅ Node maintenance, upgrades and PDBs — Q07; budget arithmetic, unhealthy replica diagnosis and safe maintenance need revision.
- [ ] Helm and Argo CD release management — rollback mentioned in Q01; broader assessment pending.
- [ ] Prometheus and EFK/ELK investigation — Q08 did not demonstrate metric/log investigation; tool-specific assessment pending.
- [ ] EKS production architecture and trade-offs — scenario setting used; platform-specific depth pending.
- [ ] AKS production scenarios — not assessed.
- [ ] Recovery validation, prevention and SLI/SLO reasoning — gaps identified in Q01–Q02; substantive demonstration pending.

Checklist granularity: CNI/NetworkPolicy were separated in Q04; IRSA/Azure workload identity are separated in Q06 (22 aspects total) so assessing one platform does not imply coverage of another. The first 10 questions may combine aspects. Extend the cycle when needed to assess uncovered areas; do not check boxes merely to meet the question target.

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

Q09 — ImagePullBackOff and GitOps release diagnosis; awaiting an answer.

After a Helm image-tag change is synced by Argo CD to EKS, new API pods enter ImagePullBackOff while old replicas continue serving. Argo CD reports Synced but the application is Degraded. The image is hosted in private Amazon ECR, and the release pipeline reports that its build succeeded. How would you isolate the pull failure and restore a reliable rollout without disrupting the healthy replicas?

## Coverage Plan

Across the first 10 questions, assess deployment and pod failures; Services, Ingress, DNS and networking; scheduling; resource management; autoscaling; storage; workload identity and RBAC; maintenance and PDBs; GitOps; and observability in realistic EKS/AKS scenarios. Combine related areas and adapt difficulty to demonstrated performance.

Prioritize unchecked aspects when choosing new questions. Avoid more than two consecutive questions centered on the same aspect unless explicitly requested. Queue weak areas for spaced retesting instead of repeatedly revisiting them immediately. Q09 moves to image delivery/GitOps; DNS diagnosis, PDB safety, identity validation, storage safety, autoscaling and NetworkPolicy weaknesses are queued for later retesting. Review coverage after each answer and at each 10-question checkpoint; continue beyond 10 if aspects remain unassessed.

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
| Q05 | 2026-10-03 | 4.5/10 | 35% | [EBS Multi-Attach](questions/Q05-ebs-multi-attach.md) |
| Q06 | 2026-10-04 | 7/10 | 65% | [IRSA Trust After Helm](questions/Q06-irsa-trust-after-helm.md) |
| Q07 | 2026-10-04 | 5.5/10 | 45% | [Node Drain / PDB](questions/Q07-node-drain-pdb.md) |
| Q08 | 2026-10-04 | 5/10 | 40% | [CoreDNS SERVFAIL](questions/Q08-coredns-servfail.md) |

## Retesting and Coverage

- Next: ImagePullBackOff, private ECR and Helm/Argo CD release diagnosis (Q09).
- Q02 improved the larger-node misconception; revisit requests/limits and safe capacity planning in a different scenario.
- Later: AWS workload identity and native configuration; GitOps rollback safeguards; request-path diagnosis and recovery validation.
- Scheduling assessed in Q03; Autoscaler diagnosis needs a later retest. HPA metrics remain unassessed. CoreDNS was assessed in Q08; hypothesis testing and safe recovery need revision. Maintenance was assessed in Q07; PDB capacity and safe drain reasoning need retesting. Storage was assessed in Q05; safe detachment and migration need retesting. Q04 assessed NetworkPolicy basics; AKS-specific platform depth remains unassessed.
- No mastery percentages inferred from eight answers. Current score movement is descriptive, not proof of overall senior readiness.
