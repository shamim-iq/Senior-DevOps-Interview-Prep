# Kubernetes Interview Progress

**Active again from 2026-10-20.** AWS paused with Q11 preserved. Current agreement: exactly five follow-ups, Q11–Q15, then a consolidated review; further questions require a new request.

| Metric | Current status |
| --- | --- |
| Questions Attempted | 10 initial assessments complete; follow-up cycle 4 / 5 assessed (Q11–Q15) |
| Follow-up average | 6.75/10 — Q11 5.5, Q12 7, Q13 8, Q14 6.5; one remains; Q11.1 excluded |
| Average Score | Historical Q01–Q10: 5.85/10; combined Q01–Q14: 6.11/10 (85.5 / 14); Q11.1 excluded |
| Average Acceptance Probability | Historical: 51.7%; combined: 54.43% (762 / 14); Q11.1 excluded; subjective answer-specific estimates |
| Topic Coverage | Q01: deployment failure, incident triage, GitOps; Q02: memory limits/OOM; Q03: request-based scheduling; autoscaling gaps identified; Q04: NetworkPolicy isolation; Q05: EBS/PVC/CSI recovery; Q06: IRSA/ServiceAccount identity; Q07: node maintenance/PDB; Q08: CoreDNS; Q09: ECR image pulls and GitOps; Q10: AKS placement constraints |
| Current Strengths | Incident ownership, previous logs, measuring usage, distinguishing larger nodes from container limits, Helm identity-regression hypothesis and permission restraint |
| Current Weaknesses | Alternative causes, request/limit precision, capacity-aware mitigation, IRSA distinction, storage attachment/migration safety, recovery validation and conciseness |
| Readiness Trend | First five: 5.7; last five: 6.0. Slight improvement across different topics; senior readiness not yet consistent |

## ☑️ Kubernetes Coverage Checklist

**Assessment coverage: 15 / 22 aspects (68.2%). Questions completed: 10 / 10 (100% of the first cycle).** These measure different things: one question can assess multiple aspects, and neither percentage is a readiness score.

`[x] ✅` = substantively attempted and evaluated at least once, with question evidence. `[ ]` = not yet assessed sufficiently, including pending questions and concepts only discussed in follow-ups. Checked aspects can still require revision. The overall topic roadmap lives in the [root README](../../README.md).

- [x] ✅ Pod/Deployment troubleshooting and CrashLoopBackOff — Q01; command accuracy and alternative causes need revision.
- [x] ✅ Memory requests/limits and OOMKilled — Q02; capacity safeguards and request semantics need revision.
- [x] ✅ Incident triage and communication — Q01–Q02; shorten opening and avoid unsupported recovery ETAs.
- [x] ✅ ImagePullBackOff — Q09; actual pull identity and event-driven diagnosis need revision.
- [x] ✅ Pending pods and scheduling resources — Q03; per-node allocatable precision needs revision.
- [x] ✅ Taints, tolerations and affinity — Q10; required placement versus permission, label drift and isolation need revision.
- [x] ✅ Service mapping/readiness/reachability — Q14; Ingress-specific depth still unassessed, recovery test needs revision.
- [x] ✅ CoreDNS and service discovery — Q08; confirm saturation versus configuration/API issues and validate recovery.
- [x] ✅ NetworkPolicy isolation — Q04; egress, narrow permissions and validation need revision.
- [ ] CNI networking and enforcement troubleshooting — not assessed.
- [x] ✅ HPA behavior and metrics — Q11 substantively attempted scaling behavior but HPA/VPA distinction was incorrect; Q12 distinguishes HPA/VPA; request denominator still needs revision.
- [x] ✅ Cluster Autoscaler and node capacity — Q12 attempted; matching capacity, configured status and expansion constraints need retest.
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

**Resumed by user request on 2026-10-20 for five questions, Q11–Q15.** Q11 has been evaluated; Q11.1 coached retry and Q12 assessed; Q15 is pending.

First 10-question evaluation cycle complete. Further coverage and weakness-driven questioning authorized on 2026-10-04. **Q11, Q11.1 and Q12 assessed; Q15 is pending**; do not restart numbering.

See [first-cycle consolidated feedback](Feedback.md#first-cycle-consolidated-feedback--q01q10--2026-10-04). The initial assessment is complete, but topic coverage and revision are not. Q11 sampled latency reasoning; Q12 now tests scaling and scheduling evidence. No pending-question answer file exists.

### Q11.1 — Coached retry assessed, 2026-10-20

[Targeted retry](questions/Q11.1-latency-targeted-retry.md): **6.5/10; 55% subjective acceptance estimate**. Rollback decision resolved in this coached attempt; p95 population, scaling choice, pool-specific diagnosis and recovery criteria still need practice. Prior Q11 score preserved. This supplementary retry is excluded from historical/first-attempt and five-scenario averages above; follow-up completion remains 1/5. Across all 12 attempts including this retry: 70.5/12 = 5.88/10; acceptance estimates 617/12 = 51.4%. These descriptive aggregates are not hiring probabilities. Q12–Q15 remain available, with consolidated review after Q15.

### Q15 — Separate Kubernetes and AWS authorization (pending)

An EKS reporting pod uses ServiceAccount reporter in namespace analytics. After a Helm release it gets Kubernetes `Forbidden` when reading ConfigMaps in namespace shared, and AWS `AccessDenied` when reading one S3 prefix. Image pulling works. A teammate suggests binding cluster-admin to reporter and adding S3 permissions to every worker node role. The workload uses IRSA. How would you identify its actual identities, restore only the required permissions in both systems, and verify permitted and denied access from the workload?

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

## Q12 — 2026-10-24

[HPA requests and capacity](questions/Q12-hpa-requests-scheduling.md): **7/10, 65% subjective acceptance estimate**. HPA/VPA distinction corrected; request/limit denominator, reserved capacity and verification remain gaps. Follow-up 2/5; Q13 pending. Whole-pod request premise clarification recorded without penalty. Initial 10 average remains 5.85; main 12 average 5.92; including coached Q11.1, 13 attempts total 77.5/13 = 5.96 (acceptance 682/13 = 52.46%). Historical snapshots above remain dated history, not current totals.

## Q13 — 2026-10-24

[Stateful EBS recovery](questions/Q13-stateful-ebs-recovery.md): **8/10; 75% subjective estimate**. Storage recovery significantly improved; verify shutdown (not merely NotReady) and data/single-writer safety before writes. Concrete attachment/events improve verification. Coverage unchanged at 14/22; no new aspect inferred. Follow-up 3/5; Q14 pending. Main follow-up average 6.83; main 13-question average 6.08. Including coached Q11.1: 85.5/14 = 6.11; acceptance estimates 757/14 = 54.07%. Older totals are historical snapshots. Full readiness review after Q15.

## Q14 — 2026-10-24

[Service/NetworkPolicy](questions/Q14-service-networkpolicy.md): **6.5/10; 60% subjective estimate**. Q04 security intent and both-side awareness partly improved; narrow rules, same-namespace semantics and application-level verification remain gaps. Main follow-up 4/5 average 6.75; main 14 average 6.11. Including coached Q11.1: 92/15 = 6.13; acceptance 817/15 = 54.47%. Coverage 15/22; Ingress not inferred. Q15 pending. Previous totals are historical snapshots.
