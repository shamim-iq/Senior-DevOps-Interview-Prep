# Kubernetes Interview Progress

**Active again from 2026-10-20.** AWS paused with Q11 preserved. Current agreement: exactly five follow-ups, Q11–Q15, then a consolidated review; further questions require a new request.

| Metric | Current status |
| --- | --- |
| Questions Attempted | 10 initial assessments complete; follow-up cycle 1 / 5 assessed (Q11–Q15) |
| Follow-up average | 5.5/10 — Q11 only; four assessments remain |
| Average Score | Historical Q01–Q10: 5.85/10; combined Q01–Q11: 5.82/10 (64 / 11) |
| Average Acceptance Probability | Historical: 51.7%; combined: 51.1% (562 / 11); subjective answer-specific estimates |
| Topic Coverage | Q01: deployment failure, incident triage, GitOps; Q02: memory limits/OOM; Q03: request-based scheduling; autoscaling gaps identified; Q04: NetworkPolicy isolation; Q05: EBS/PVC/CSI recovery; Q06: IRSA/ServiceAccount identity; Q07: node maintenance/PDB; Q08: CoreDNS; Q09: ECR image pulls and GitOps; Q10: AKS placement constraints |
| Current Strengths | Incident ownership, previous logs, measuring usage, distinguishing larger nodes from container limits, Helm identity-regression hypothesis and permission restraint |
| Current Weaknesses | Alternative causes, request/limit precision, capacity-aware mitigation, IRSA distinction, storage attachment/migration safety, recovery validation and conciseness |
| Readiness Trend | First five: 5.7; last five: 6.0. Slight improvement across different topics; senior readiness not yet consistent |

## ☑️ Kubernetes Coverage Checklist

**Assessment coverage: 13 / 22 aspects (59.1%). Questions completed: 10 / 10 (100% of the first cycle).** These measure different things: one question can assess multiple aspects, and neither percentage is a readiness score.

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
- [x] ✅ HPA behavior and metrics — Q11 substantively attempted scaling behavior but HPA/VPA distinction was incorrect; metric interpretation requires Q12 retest.
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

**Resumed by user request on 2026-10-20 for five questions, Q11–Q15.** Q11 has been evaluated; user-requested Q11.1 retry is pending before Q12.

First 10-question evaluation cycle complete. Further coverage and weakness-driven questioning authorized on 2026-10-04. **Q11 assessed; Q11.1 is pending; Q12 is preserved for afterward**; do not restart numbering.

See [first-cycle consolidated feedback](Feedback.md#first-cycle-consolidated-feedback--q01q10--2026-10-04). The initial assessment is complete, but topic coverage and revision are not. Q11 sampled latency reasoning; Q12 now tests scaling and scheduling evidence. No pending-question answer file exists.

### Q11.1 — Targeted latency retry (pending)

User requested this extra retry on 2026-10-20 before Q12. It supplements Q11 rather than replacing its score or consuming a Q12–Q15 slot. Evaluate recovery explicitly; label it a coached retest, since Q11 feedback was already provided. Do not change aggregates until an answer is assessed.

After a new release, an EKS API's p95 rises from 200 ms to 2 seconds. All six pods are Ready, there are no restarts or Pending pods, CPU averages 40%, and request volume and 5xx rate are unchanged. Slow-request logs show much longer database connection-pool waits in the new version; the previous version remains fast under comparable traffic. A teammate suggests adding replicas with VPA. The previous release is compatible with the current database schema.

Explain what p95 means here, which evidence you would follow and what you would verify next, whether the VPA suggestion is correct and how HPA differs, your immediate mitigation/rollback decision, and how you would prove recovery. Keep the response focused; commands are optional if their purpose is clear.

### Q12 — HPA metrics and scheduling capacity (pending)

An EKS API has four replicas. Its HPA targets 60% CPU utilization, but displays `<unknown>/60%` while traffic grows. Metrics Server is healthy and `kubectl top pods` works. The live API container has neither a CPU request nor a CPU limit. During a controlled manual scale to six replicas, two new pods remain Pending with `Insufficient cpu`; node CPU usage is low. A teammate suggests increasing CPU limits and enabling VPA to add replicas. Explain the two failures, the evidence you would check, and how you would restore safe scaling and verify it.

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
- Scheduling assessed in Q03; Autoscaler diagnosis needs a later retest. HPA behavior was attempted in Q11; metrics interpretation is pending Q12. CoreDNS was assessed in Q08; hypothesis testing and safe recovery need revision. Maintenance was assessed in Q07; PDB capacity and safe drain reasoning need retesting. Storage was assessed in Q05; safe detachment and migration need retesting. Q04 assessed NetworkPolicy basics; AKS-specific platform depth remains unassessed.
- No mastery percentages inferred from ten answers. Current score movement is descriptive, not proof of overall senior readiness.

## Platform emphasis on resumption — 2026-10-19

Historical preference, now active from 2026-10-20: preserve question history and use EKS as the primary managed platform and AKS secondarily. AWS practice will integrate EKS with related cloud concepts now; later Kubernetes practice should deepen cluster behavior and revisit evidenced gaps without repeating already demonstrated basics. Link relevant AWS attempts when assessed; no automatic coverage credit or copied overall scores. This planning change does not evaluate any skill or alter historical metrics.

## Cross-topic EKS evidence — 2026-10-20

[AWS Q09: IRSA after Helm release](../aws/questions/Q09-eks-irsa-helm-access.md) reinforces ServiceAccount/role mapping and Helm regression diagnosis. Runtime caller proof, precise trust verification and post-fix access tests remain gaps. AWS owns the 7.5/10 overall score; no Kubernetes subscore, new standalone attempt or changed average. Existing Kubernetes question and revision history remain preserved.

## AWS Q10 cross-topic evidence — 2026-10-20

[EKS subnet exhaustion](../aws/questions/Q10-eks-subnet-ip-exhaustion.md): correct capacity constraint and healthy-workload preservation. Free-IP calculation, Calico/prefix modes and VPA semantics need correction; already-bound pod recovery and validation incomplete. AWS owns the 6.5/10 score; no extra Kubernetes attempt, subscore or changed average.

## Q11 follow-up — 2026-10-20

[Latency investigation](questions/Q11-latency-investigation-recovery.md): **5.5/10; 45% subjective acceptance estimate**. Follow-up 1/5. Recovery observation partially improved; evidence-led diagnosis, rollback decision and HPA/VPA precision remain unresolved. p95 definition needs correction. Tool-specific Prometheus/log searches and full SLI/SLO/recovery criteria remain unchecked; naming dashboards alone does not complete these aspects. No prior weakness marked resolved. Consolidated review after Q15.
