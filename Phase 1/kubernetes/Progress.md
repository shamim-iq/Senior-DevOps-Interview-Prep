# Kubernetes Interview Progress

**Active again from 2026-10-20.** AWS paused with Q11 preserved. Current agreement: exactly five follow-ups, Q11–Q15, then a consolidated review; further questions require a new request.

| Metric | Current status |
| --- | --- |
| Questions Attempted | 10 initial assessments complete; follow-up cycle 0 / 5 assessed (Q11–Q15) |
| Follow-up average | N/A; no new attempts yet |
| Average Score | 5.85/10 — total 58.5 / 10 |
| Average Acceptance Probability | 51.7% — total 517 / 10; subjective answer-specific estimates |
| Topic Coverage | Q01: deployment failure, incident triage, GitOps; Q02: memory limits/OOM; Q03: request-based scheduling; autoscaling gaps identified; Q04: NetworkPolicy isolation; Q05: EBS/PVC/CSI recovery; Q06: IRSA/ServiceAccount identity; Q07: node maintenance/PDB; Q08: CoreDNS; Q09: ECR image pulls and GitOps; Q10: AKS placement constraints |
| Current Strengths | Incident ownership, previous logs, measuring usage, distinguishing larger nodes from container limits, Helm identity-regression hypothesis and permission restraint |
| Current Weaknesses | Alternative causes, request/limit precision, capacity-aware mitigation, IRSA distinction, storage attachment/migration safety, recovery validation and conciseness |
| Readiness Trend | First five: 5.7; last five: 6.0. Slight improvement across different topics; senior readiness not yet consistent |

## ☑️ Kubernetes Coverage Checklist

**Initial assessment coverage: 12 / 22 aspects (54.5%). Questions completed: 10 / 10 (100% of the first cycle).** These measure different things: one question can assess multiple aspects, and neither percentage is a readiness score.

`[x] ✅` = substantively attempted and evaluated at least once, with question evidence. `[ ]` = not yet assessed sufficiently, including pending questions and concepts only discussed in follow-ups. Checked aspects can still require revision. The overall topic roadmap lives in the [root README](../../README.md).

- [x] ✅ Pod/Deployment troubleshooting and CrashLoopBackOff — Q01; command accuracy and alternative causes need revision.
- [x] ✅ Memory requests/limits and OOMKilled — Q02; capacity safeguards and request semantics need revision.
- [x] ✅ Incident triage and communication — Q01–Q02; shorten opening and avoid unsupported recovery ETAs.
- [x] ✅ ImagePullBackOff — Q09; actual pull identity and event-driven diagnosis need revision.
- [x] ✅ Pending pods and scheduling resources — Q03; per-node allocatable precision needs revision.
- [x] ✅ Taints, tolerations and affinity — Q10; required placement versus permission, label drift and isolation need revision.
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
- [x] ✅ Helm and Argo CD release management — Q01/Q09; Git correction/sync assessed, safe rollout and health validation need revision.
- [ ] Prometheus and EFK/ELK investigation — Q08 did not demonstrate metric/log investigation; tool-specific assessment pending.
- [ ] EKS production architecture and trade-offs — scenario setting used; platform-specific depth pending.
- [ ] AKS production scenarios — pool replacement sampled in Q10; AKS-specific operational depth remains to be assessed.
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
- [x] ✅ Complete the first 10 evaluated questions and consolidated feedback — Q01–Q10, 2026-10-04.
- [ ] Retest outstanding weak areas and record results.
- [x] ✅ Review overall Kubernetes readiness against coverage and retest evidence — cycle-one review completed; readiness not yet established.

## Current Position

**Resumed by user request on 2026-10-20 for five questions, Q11–Q15.** Existing Q11 is retained unchanged.

First 10-question evaluation cycle complete. Further coverage and weakness-driven questioning authorized on 2026-10-04. **Q11 is pending**; do not restart numbering.

See [first-cycle consolidated feedback](Feedback.md#first-cycle-consolidated-feedback--q01q10--2026-10-04). The initial assessment is complete, but topic coverage and revision are not. Prioritize an uncovered observability/SLI-SLO scenario next, then rotate with spaced retests; no future answer file has been created.

### Q11 — Observability and recovery decisions

After a release, a Kubernetes API's p95 latency rises from 200 ms to 2 seconds. All pods are Ready, CPU averages 40%, and the HTTP 5xx rate is unchanged. Users report slow requests. Prometheus/Grafana and centralized application logs are available. How would you isolate the bottleneck, decide whether to roll back, and demonstrate that service performance has recovered?

## Second-Stage Preparation Strategy

**Current agreement — 2026-10-20:** Five follow-up scenarios (Q11–Q15), one at a time, with individual scoring/feedback and explicit recovery comparison. This supersedes the former open-ended Q20/Q30 plan. No question files before attempts; no automatic extension after Q15.

| Slot | Intended focus (adapt unasked scenarios) | Evidence to revisit |
| --- | --- | --- |
| Q11, preserved | Latency investigation, observability and measurable recovery | Q01/Q02/Q08; recurring AWS validation gaps |
| Q12 candidate | HPA metrics and eligible node capacity | Q02/Q03; AWS Q10 scaling/IP distinctions |
| Q13 candidate | Stateful recovery with data and availability safeguards | Q05/Q07; AWS Q08 migration gaps |
| Q14 candidate | Service/request-path isolation and narrow networking | Q04/Q08; readiness/EndpointSlices coverage |
| Q15 candidate | Workload authorization and operational validation | Q06/Q09; AWS Q09 actual identity evidence |

EKS is primary; AKS is secondary where comparisons are relevant. Keep each scenario manageable and avoid adding unrelated questions under subparts. Observability stays integrated; link substantive evidence to its tracking files without duplicating scores. Some uncovered aspects may remain after five: report them honestly rather than marking them complete.

After each answer, map tested earlier gaps to resolved, partially improved or still unresolved with evidence. Untested gaps remain not reassessed. Preserve original scores and distinguish independent retests from answers given after coaching. Four-year baseline applies; do not import the full reference answer as a mandatory scoring checklist.

After Q15, provide a consolidated report: the five individual scores and average, historical and combined averages clearly separated, demonstrated improvements, weakness-recovery matrix, remaining/unassessed aspects, and a Kubernetes-specific readiness verdict. Note that different scenarios and coaching limit score comparisons. No overall hiring-probability claim.

### Coverage Queue — Not Future Question Text

- Observability: Prometheus/Grafana metrics, centralized logs, latency/error SLIs, SLO reasoning and recovery gates.
- Services/Ingress/EndpointSlices and readiness; CNI/network-path troubleshooting.
- HPA metrics and configuration; Cluster Autoscaler diagnosis and capacity constraints.
- Scoped Kubernetes RBAC and ServiceAccounts; Azure workload identity.
- EKS/AKS architecture: availability, cost, upgrades, failure domains and operational trade-offs.

### Priority Retest Queue

- EBS attachment/fencing and migration safety (Q05).
- PDB budget and healthy-capacity restoration (Q07).
- Runtime identity versus image-pull identity; precise trust and validation (Q06/Q09).
- DNS evidence before scaling; NetworkPolicy directions and narrow permissions (Q04/Q08).
- Scheduler requests, pool labels, required affinity versus toleration and node scaling (Q03/Q10).

Use the queue to prioritize within Q11–Q15; remaining items are not authorization to extend the cycle. Add newly observed mistakes without dropping the existing queue. No more than two consecutive questions centered on one aspect unless requested.

### Consistent Evaluation and Readiness Evidence

- Keep evaluating technical accuracy, coverage, communication, conciseness, troubleshooting and senior reasoning. State the dominant deductions: wrong concept, omitted requirement or unsafe decision. Reward correct short answers; command volume earns no credit by itself.
- For targeted retests, record the original question, new question and result. Preserve original scores; distinguish independently demonstrated improvement from an assisted correction.
- Every incident answer should explain the relevant evidence, a safe decision and observable recovery; avoid forcing a checklist into conceptual questions.
- Working practice target (not an employer cutoff): at least 8/10 on five varied recent scenarios, no uncorrected high-risk safety misconceptions, and two independent successful retests per critical weakness.
- Require all agreed assessment aspects covered, plus practical interpretation of commands/logs/manifests and at least one integrated incident and one architecture discussion. Checklist completion alone is not mastery.
- At the Q15 consolidated review, report: remaining aspects, recurring errors, retest results and score movement with its limitations. Do not convert average answer-acceptance estimates into an overall hiring probability.

### Broader Role Readiness

Kubernetes is only the current topic. Before claiming readiness for the overall Senior DevOps / Platform / SRE objective, assess the other agreed topics in their own directories: Docker, AWS, Azure, Terraform, observability, Linux/networking, RAG, MCP and Bedrock. Include CI/CD, security, scripting/automation, incident ownership and project/architecture explanations where relevant to target job descriptions. Topic scope and readiness standards should follow actual job requirements; no company-specific pass probability is inferred from these ten answers.

## Coverage Plan

Across the first 10 questions, assess deployment and pod failures; Services, Ingress, DNS and networking; scheduling; resource management; autoscaling; storage; workload identity and RBAC; maintenance and PDBs; GitOps; and observability in realistic EKS/AKS scenarios. Combine related areas and adapt difficulty to demonstrated performance.

Prioritize unchecked aspects when choosing new questions. Avoid more than two consecutive questions centered on the same aspect unless explicitly requested. Queue weak areas for spaced retesting instead of repeatedly revisiting them immediately. After Q10, prioritize uncovered observability/SLI-SLOs; DNS diagnosis, PDB safety, identity validation, storage safety, autoscaling and NetworkPolicy weaknesses are queued for later retesting. Review coverage after each answer and at each 10-question checkpoint; continue beyond 10 if aspects remain unassessed.

## Session Rules

- Ask one scenario at a time; do not reveal hints or answers before an attempt.
- Before each new question, inspect existing question files and this active-question record to avoid duplicates.
- After each answer: evaluate, provide concise feedback, save the correct answer in questions/QNN-<topic>.md, append feedback, update progress, record the next pending question and wait for the user to continue.
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
| Q09 | 2026-10-04 | 6.5/10 | 60% | [ECR ImagePullBackOff / GitOps](questions/Q09-ecr-imagepull-gitops.md) |
| Q10 | 2026-10-04 | 6/10 | 55% | [AKS Affinity / Taints](questions/Q10-aks-affinity-taints.md) |

## Retesting and Coverage

- Next number: Q11. Prioritize observability/SLI-SLO coverage; the first-cycle consolidation is recorded in Feedback.md.
- Q02 improved the larger-node misconception; revisit requests/limits and safe capacity planning in a different scenario.
- Later: AWS workload identity and native configuration; GitOps rollback safeguards; request-path diagnosis and recovery validation.
- Scheduling assessed in Q03; Autoscaler diagnosis needs a later retest. HPA metrics remain unassessed. CoreDNS was assessed in Q08; hypothesis testing and safe recovery need revision. Maintenance was assessed in Q07; PDB capacity and safe drain reasoning need retesting. Storage was assessed in Q05; safe detachment and migration need retesting. Q04 assessed NetworkPolicy basics; AKS-specific platform depth remains unassessed.
- No mastery percentages inferred from ten answers. Current score movement is descriptive, not proof of overall senior readiness.

## Platform emphasis on resumption — 2026-10-19

Historical preference, now active from 2026-10-20: preserve question history and use EKS as the primary managed platform and AKS secondarily. AWS practice will integrate EKS with related cloud concepts now; later Kubernetes practice should deepen cluster behavior and revisit evidenced gaps without repeating already demonstrated basics. Link relevant AWS attempts when assessed; no automatic coverage credit or copied overall scores. This planning change does not evaluate any skill or alter historical metrics.

## Cross-topic EKS evidence — 2026-10-20

[AWS Q09: IRSA after Helm release](../aws/questions/Q09-eks-irsa-helm-access.md) reinforces ServiceAccount/role mapping and Helm regression diagnosis. Runtime caller proof, precise trust verification and post-fix access tests remain gaps. AWS owns the 7.5/10 overall score; no Kubernetes subscore, new standalone attempt or changed average. Existing Kubernetes question and revision history remain preserved.

## AWS Q10 cross-topic evidence — 2026-10-20

[EKS subnet exhaustion](../aws/questions/Q10-eks-subnet-ip-exhaustion.md): correct capacity constraint and healthy-workload preservation. Free-IP calculation, Calico/prefix modes and VPA semantics need correction; already-bound pod recovery and validation incomplete. AWS owns the 6.5/10 score; no extra Kubernetes attempt, subscore or changed average.
