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

## Q06 — IRSA Trust After Helm — 2026-10-04

Score: 7/10
Interview Acceptance Probability: 65% (subjective estimate for this answer).

✅ Strong
- Plausible Helm/ServiceAccount regression tied to the release.
- Correct role-annotation check and basic temporary-credentials understanding.
- Correctly rejected excessive cluster-admin access; improvement over Q01's identity explanation.

⚠️ Improve
- Inspect the running pod's actual ServiceAccount, not only the list of accounts.
- Compare role trust provider, subject (namespace/name) and audience; the right annotation is necessary but not sufficient.
- State why cluster-admin cannot fix AWS STS authorization: Kubernetes RBAC and IAM are separate.
- Kubernetes issues the token; STS exchanges it for credentials after validating preconfigured trust.
- Describe the narrow Helm/trust correction, any required rollout and verification of role identity plus S3 read.

| Evaluation dimension | Assessment |
| --- | --- |
| Technical accuracy | Mostly correct; token/trust lifecycle needs more precise wording |
| Coverage | Strong likely cause; trust conditions and recovery validation missing |
| Interview representation | Relevant hypothesis and sensible permission restraint |
| Conciseness | Understandable; shorten setup explanation to prioritize incident evidence |
| Troubleshooting approach | Useful annotation check; verify pod-to-role-to-trust chain |
| Senior-level reasoning | Good least-privilege instinct; explicitly separate authorization layers |

Main deductions: missing trust-condition checks and a concrete fix/validation sequence. No deduction for avoiding a long command list. Revisit identity validation later; move to maintenance/PDBs next.

## Q07 — Node Drain / PDB — 2026-10-04

Score: 5.5/10
Interview Acceptance Probability: 45% (subjective estimate for this answer).

✅ Strong
- Connected PDBs with voluntary disruption and rejected outright deletion.
- Planned replacement node capacity, cordon/drain and maintenance communication.

⚠️ Improve
- Lead with the scenario: two Ready minus minAvailable two leaves zero budget for healthy-pod eviction.
- Investigate and restore the third replica, or add genuinely Ready capacity, before weakening protection.
- A maintenance window does not make lower availability safe; loosening a PDB can permit overload or outage.
- New nodes alone do not guarantee application readiness or no latency; validate replacements and customer metrics between drains.
- Use compatible tested versions and release-specific add-on prerequisites rather than an unconditional latest-version sequence.

| Evaluation dimension | Assessment |
| --- | --- |
| Technical accuracy | Basic PDB/drain knowledge correct; mandatory relaxation/no-impact claims incorrect |
| Coverage | Broad upgrade process discussed; actual unready replica and budget diagnosis missed |
| Interview representation | Operational awareness, but answer needs focus on the given blocker |
| Conciseness | Repeats upgrade/capacity points; shorter evidence-first response would improve clarity |
| Troubleshooting approach | No concrete investigation of PDB status or failing replica |
| Senior-level reasoning | Capacity planning is positive; availability trade-offs and stop/verify gates missing |

Main deductions: unsafe default relaxation and missing investigation/validation, not missing command volume. Queue PDB availability reasoning for spaced retesting; rotate to DNS/observability.

## Q08 — CoreDNS SERVFAIL — 2026-10-04

Score: 5/10
Interview Acceptance Probability: 40% (subjective estimate for this answer).

✅ Strong
- Understood Service-name resolution and why direct ClusterIP requests bypass DNS.
- Identified scaling as a plausible mitigation if CoreDNS is overloaded.

⚠️ Improve
- Running does not prove health or overload. SERVFAIL needs investigation, not an automatic scale-up conclusion.
- Reproduce the failing query and compare logs/metrics; consider Corefile changes, API/RBAC errors and resolver-path differences.
- CoreDNS can forward external queries; it does not redirect application HTTP requests.
- Use precise dataplane terminology: IPv4 is an address family; Service forwarding may use kube-proxy or another implementation.
- Explain controlled mitigation and DNS/application validation during representative traffic.

| Evaluation dimension | Assessment |
| --- | --- |
| Technical accuracy | Basic DNS role correct; pod-phase inference and DNS/dataplane wording inaccurate |
| Coverage | One potential fix; isolation and validation missing |
| Interview representation | Understandable analogy; lead with the supplied evidence |
| Conciseness | Reasonably concise; shorten generic DNS explanation |
| Troubleshooting approach | Assumed saturation without logs, queries or resource evidence |
| Senior-level reasoning | Needs alternative causes and controlled recovery checks |

Main deductions: unsupported diagnosis and omitted isolation/validation, not missing command volume. Queue DNS evidence gathering for a later retest; rotate to image delivery/GitOps.

## Q09 — ECR ImagePullBackOff / GitOps — 2026-10-04

Score: 6.5/10
Interview Acceptance Probability: 60% (subjective answer-specific estimate).

✅ Strong
- Identified wrong image references and pull authorization as plausible causes.
- Distinguished pipeline success from successful runtime rollout.
- Proposed correcting Git and syncing Argo CD, including a manual sync alternative.

⚠️ Improve
- Check actual pod pull events before selecting a cause; verify image publication rather than assume a successful build means it was pushed.
- Normal EC2 EKS pulls use the node role; Fargate uses the execution role. Runtime IRSA annotation is not the default pull identity. Explicit newer per-pod pull setups use a separate mechanism.
- Explain Synced versus Healthy explicitly; auto-sync is conditional on configuration.
- Preserve healthy replicas, use a known-good revert when appropriate, and verify new pods plus customer requests.

| Evaluation dimension | Assessment |
| --- | --- |
| Technical accuracy | Tag and permission hypotheses sound; default pull identity confused with runtime IRSA |
| Coverage | Includes recovery through Git; event evidence, networking and serving-capacity validation limited |
| Interview representation | Logical release narrative; lead with the actual error |
| Conciseness | Some repetition of tag/permissions; focus on decisions |
| Troubleshooting approach | Checks proposed but no exact-event branching or actual pull-principal confirmation |
| Senior-level reasoning | GitOps repair is good; protect old replicas and verify the new rollout |

Main deductions: identity assumption and incomplete safe-rollout validation. Complete resubmitted answer evaluated once; no penalty for the interrupted message. Move to scheduling constraints/AKS for Q10; consolidate feedback after its evaluation, not before.

## Q10 — AKS Affinity / Taints — 2026-10-04

Score: 6/10
Interview Acceptance Probability: 55% (subjective estimate for this answer).

✅ Strong
- Rejected removing placement restrictions and tolerating everything.
- Identified affinity/tolerations as relevant and retained the dedicated payments-pool objective.

⚠️ Improve
- Start with the supplied affinity/taint errors, not an assumed resource shortage.
- Compare replacement-node labels with required affinity; a changed/missing label is a key hypothesis after pool replacement.
- Tolerations permit placement; required affinity/nodeSelector confines it. Keep intentional payments/system taints, and remove only an evidenced configuration mistake.
- Scheduling isolation does not provide network isolation. VM size, not machine image, determines CPU/memory.
- Persist pool/workload configuration and verify actual placement, readiness and customer recovery.

| Evaluation dimension | Assessment |
| --- | --- |
| Technical accuracy | Relevant controls recognized; isolation layers and VM image/capacity confused |
| Coverage | Broad fix proposed; label comparison, exact constraint and verification missing |
| Interview representation | Good rejection of unsafe advice; focus first on scenario evidence |
| Conciseness | Repeats capacity reasoning that is secondary to the reported errors |
| Troubleshooting approach | Needs direct comparison of pod constraints and replacement-pool metadata |
| Senior-level reasoning | Good isolation intent; precise enforcement and persistence need detail |

Main deductions: imprecise isolation/placement explanation and missing evidence/validation, not missing command count.

## First Cycle Consolidated Feedback — Q01–Q10 — 2026-10-04

**Completed:** 10 evaluated questions. **Average:** 5.85/10. **Average answer-acceptance estimate:** 51.7% (subjective; not hiring probability).

| Area | Evidence-based assessment |
| --- | --- |
| Relative strengths | Incident ownership and mitigation intent (Q01–Q02); recognizing risky permission/placement proposals (Q06/Q10); restoring desired state through Git (Q09). No domain is yet proven mastered. |
| Moderate areas | Container-limit reasoning after feedback (Q02), request-based scheduling (Q03), NetworkPolicy hypothesis (Q04), IRSA setup (Q06), image-tag diagnosis (Q09), placement controls (Q10). Correct starting ideas need fuller investigation. |
| Weak areas | Safe EBS recovery/migration (Q05); Autoscaler diagnosis (Q03); PDB availability trade-offs (Q07); evidence-led DNS diagnosis (Q08); runtime IAM versus image-pull identity (Q09). |
| Recurring mistakes | Jumping from a symptom to a single assumed cause; blurring control layers; underspecified safe changes; rarely demonstrating customer-facing validation. Unsupported no-impact/zero-loss claims occurred in Q05/Q07. |
| Communication quality | Understandable operational narrative; Q03/Q04 were more direct. Several answers spend too long on generic setup or repeat the same point. Lead with the provided evidence, then action and verification. |
| Technical depth | Familiar with many components, but exact enforcement boundaries and failure-stage reasoning remain uneven. Essential commands should show what evidence changes the decision, not pad the answer. |
| Overall Kubernetes readiness | Developing foundation; not yet consistently ready for senior production-troubleshooting interviews based on these attempts. Coverage and retest gaps remain, so completing 10 questions is not topic completion. |

### Priority Revision Topics

1. Safe mitigation and explicit recovery checks in every scenario: fix -> observe -> verify customer outcome.
2. EBS writer fencing, stale attachment versus AZ mismatch, migration/restore realities (Q05).
3. Identity boundaries: Kubernetes RBAC, IRSA trust, image-pull credentials (Q06/Q09).
4. Scheduling/Autoscaler/PDB: requested capacity, eligible node groups, healthy-replica budget (Q03/Q07/Q10).
5. Network diagnosis: ingress plus egress, DNS logs/metrics, readiness versus connectivity (Q04/Q08).

### Trend and Next Coverage

- Scores: 6, 6.5, 5, 6.5, 4.5, 7, 5.5, 5, 6.5, 6. First five average 5.7; last five average 6.0. Small descriptive improvement across different topics, not proof of mastery.
- Strongest answer: Q06 (7). Lowest: Q05 (4.5). No old scores changed.
- Continue broad coverage before concentrated repetition: observability/SLI-SLOs, HPA metrics, CNI, scoped RBAC, Azure workload identity, deeper Service/Ingress and platform architecture.
- Interleave fresh coverage with spaced retests of the priorities above. Follow-up explanations count as learning, not new scored attempts.

## Cross-topic follow-up — AWS Q09, 2026-10-20

[IRSA/Helm evidence](../aws/questions/Q09-eks-irsa-helm-access.md): configuration mapping and least-privilege reasoning reinforced. Actual pod identity, issuer/sub/aud checks and access verification remain unproven. No separate Kubernetes score; prior Q06 score retained.

## AWS Q10 cross-topic evidence — 2026-10-20

[EKS subnet exhaustion](../aws/questions/Q10-eks-subnet-ip-exhaustion.md): correct capacity constraint and healthy-workload preservation. Free-IP calculation, Calico/prefix modes and VPA semantics need correction; already-bound pod recovery and validation incomplete. AWS owns the 6.5/10 score; no extra Kubernetes attempt, subscore or changed average.

## Five-question follow-up agreement — 2026-10-20

Resume Q11–Q15, with individual feedback after every answer and a consolidated improvement/readiness/weakness-recovery review after all five. Historical baseline: 58.5/100, average 5.85/10; keep scores unchanged. Report the new five-question average separately and explain limitations when comparing different scenarios/calibration. No new scores or mastery claims arise from this planning change. EKS primary, AKS secondary; cross-topic AWS evidence guides retests without double-counting attempts. No automatic extension beyond Q15.

## Q11 — 2026-10-20: latency investigation

**5.5/10; acceptance estimate 45%** (subjective, answer-specific). [Answer and deduction details](questions/Q11-latency-investigation-recovery.md). Credit workload localization, dependency consideration, logs and explicit p95 recovery observation. Deduct for incorrect p95/HPA/VPA concepts, weak evidence prioritization, missing rollback decision and incomplete recovery criteria. No extra deduction for command count or incidental syntax.

Recovery versus earlier attempts: Q01/Q02/Q08 recovery observation **partially improved**; Q08 diagnosis-before-scaling **unresolved**; AWS Q10 HPA/VPA distinction **unresolved**; Q01/Q09 rollback decision **unresolved**. Storage/identity/PDB not reassessed. Follow-up 1/5; full readiness and weakness-recovery verdict after Q15.

## Q11.1 coached retry — 2026-10-20

**6.5/10; 55% subjective answer acceptance estimate.** [Attempt, corrections and deduction details](questions/Q11.1-latency-targeted-retry.md). Clear rollback-first mitigation improved. Percentile threshold understood but wrong population (pods instead of requests); HPA/VPA roles mostly corrected but HPA not supported as the incident fix. Pool-wait evidence and concrete recovery criteria remain gaps. RollingUpdate is not generally discouraged. Rollback gap resolved for this coached attempt only; no independent mastery claim. Original Q11 5.5 retained, primary cycle 1/5, Q12 pending.

## Q12 — 2026-10-24

**7/10; 65% subjective estimate.** [Evaluation](questions/Q12-hpa-requests-scheduling.md). HPA/VPA misconception resolved in this attempt. Right-sizing and node scaling reasoning partially improved; HPA uses requests, not limits. Low node usage does not show unallocated requested capacity. Autoscaler readiness/eligibility and measurable recovery remain gaps. Question's missing whole-pod request context acknowledged without penalty. Follow-up 2/5; Q13 pending.

## Q13 — 2026-10-24

**8/10; 75% subjective estimate.** [Evaluation](questions/Q13-stateful-ebs-recovery.md). Credit safe intent, supported out-of-service recovery, CSI and attachment checks. Deduct shutdown-versus-NotReady condition (1), data/single-writer validation before writes (0.75), safe rejoin/taint cleanup (0.25). Q05 storage gaps significantly but partially improved; Q11/Q12 verification partially improved. PDB/cross-AZ migration not tested. Clarified question history preserved; no penalty for user challenging its premise. Three of five follow-ups assessed; Q14 pending.

## Q14 — 2026-10-24

**6.5/10; 60% subjective estimate.** [Details](questions/Q14-service-networkpolicy.md). Credit security restraint, working-DNS recognition and both-side policy awareness. Gaps: exact narrow ingress/egress rules, same-namespace exemption misconception, DNS-only recovery test, port mapping explanation. Q04/Q08 partially improved; customer-operation verification unresolved. Latest complete answer supersedes interrupted partial submission. Four of five follow-ups complete, Q15 pending.

## Q15 — 2026-10-24

**6.5/10; 60% subjective estimate.** [Evaluation](questions/Q15-rbac-irsa-boundaries.md). Credit least privilege and Helm/SA checks. Scope, runtime identity/image-pull inference and actual allowed/denied verification remain gaps. Ambiguous role wording not treated as an explicit IAM-for-ConfigMaps claim. Five follow-ups complete.

## Five-follow-up consolidated review — 2026-10-24

| Question | Score | Main finding |
| --- | --- | --- |
| Q11 latency | 5.5 | Broad hypotheses; percentile/scaling errors and missing rollback |
| Q12 autoscaling | 7 | HPA/VPA corrected; requests/limits/capacity precision incomplete |
| Q13 storage | 8 | Strong recovery mechanism; shutdown and data-safety prerequisites need precision |
| Q14 networking | 6.5 | Security intent correct; policy scope and HTTP verification gaps |
| Q15 authorization | 6.5 | Configuration checks useful; runtime identity and authorization boundaries incomplete |

**Initial Q01–Q10 average: 5.85/10. Follow-ups Q11–Q15: 6.7/10 (33.5/5). Combined 15 main questions: 6.13/10 (92/15).** Q11.1 coached retry 6.5 is separate; including it gives 98.5/16 = 6.16. Different scenarios and intervening coaching limit direct comparison; movement is descriptive, not proof of a fixed skill gain. Subjective acceptance averages: follow-ups 61%, combined main 54.8%, all attempts 54.81%; none are hiring probabilities.

| Gap | Recovery evidence | Current status |
| --- | --- | --- |
| HPA versus VPA | Q12 correctly separates replicas and resources | Corrected in this attempt; not all autoscaling mastered |
| Safe rollback | Q11.1 chooses known-good rollback | Improved after coaching; independent retention not established |
| Storage recovery | Q13 rejects reckless detach; names supported mechanism and attachment checks | Significant partial improvement; strict shutdown/data gate remains |
| Requests versus limits and scheduling | Q12 right-sizing intent, but denominator/allocated capacity omitted | Partially recovered |
| NetworkPolicy | Q14 preserves isolation, considers both sides | Partially recovered; exact peer/port scope and same-namespace reasoning need work |
| Workload authorization | Q15 ServiceAccount/Helm/annotation checks | Partially recovered; runtime caller, cross-namespace RBAC, image-pull distinction unresolved |
| Evidence-led latency investigation | Q11/Q11.1 general causes versus supplied pool evidence | Unresolved; p95 request population needs fresh proof |
| Recovery validation | Q13 attachment checks; Q14 DNS-only; Q15 vague in-container checks | Recurring unresolved gap: test the actual operation plus forbidden access where relevant |
| PDB arithmetic, cross-AZ recovery, other uncovered areas | Not independently revisited in this cycle | Not reassessed; preserve earlier gaps |

**Readiness verdict:** Better production-safety judgment and troubleshooting vocabulary; not yet consistently interview-ready for deep Kubernetes production scenarios at the four-year baseline. Can explain common approaches, but follow-up questions expose control-boundary and verification gaps. Highest-value revision: request-based capacity, identity/authorization boundaries, actual-path tests, shutdown/single-writer guarantees. A concise evidence → decision → operation test answer is more valuable than extra component names. No claim about overall role or company-specific hiring odds.

**Coverage:** 16/22 aspects sampled, not mastered. Six unchecked broad aspects: CNI troubleshooting, Azure workload identity, tool-specific Prometheus/log investigation, EKS architecture trade-offs, deeper AKS operations, complete recovery/SLI-SLO reasoning. Ingress, PDB and selected subskills also remain incomplete despite checked parent areas. AWS-linked work is evidence, not a duplicate Kubernetes score. Prioritize important remaining weaknesses; do not chase obscure commands to fill checkboxes.

**Agreement fulfilled:** Five main follow-ups plus requested Q11.1 retry complete. No Q16 scheduled or automatically authorized. Further targeted retests/practice only on user request; keep pending questions in other topics intact.

## Clarification reassessment — 2026-10-24

**Revised Q15: 7/10; subjective acceptance estimate 65%. Original 6.5/10 (60%) preserved.** This records a clarification, not a new question or independent retest.

The candidate explicitly distinguishes Kubernetes Role/RoleBinding/ServiceAccount authorization from IAM for AWS APIs. Credit correct API-group/verb scoping and intent to restrict access to the required ConfigMap. The original answer already mentioned RoleBinding; do not characterize the candidate as claiming IAM grants ConfigMap access. Remove 0.5 of the original combined 1-point deduction for boundary ambiguity.

Remaining deductions: exact target-namespace binding placement/subject not stated (0.5); image-pull inference/runtime identity proof (1); S3 prefix/action scope (0.75); concrete allowed/denied operation verification (0.75). Role and RoleBinding should be in shared, with subject reporter in analytics; for a named ConfigMap read, use the core API group, configmaps resource, get verb and resourceNames as appropriate. This precision is separate from knowing RBAC versus IAM.

Recovery remarks updated: **conceptual RBAC/IAM distinction demonstrated in clarification**; exact cross-namespace binding and runtime proof remain incomplete. IAM can govern application calls to ECR APIs, but successful image pulling still does not establish runtime IRSA identity. Other gaps are unchanged.

### Revised consolidated metrics

Latest Q11–Q15 scores: 5.5, 7, 8, 6.5, **7** → **6.8/10** (34/5). Original-assessment average remains 6.7. Latest-per-main-question average: 92.5/15 = **6.17/10**; original 92/15 = 6.13 preserved. Q11.1 remains separate; using latest Q15 plus Q11.1 gives 99/16 = 6.19 (not an extra Q15 attempt). Latest acceptance estimates: follow-ups 62%, main 827/15 = 55.13%, including Q11.1 882/16 = 55.13%; subjective, not hiring probabilities.

Readiness review adjustment: credit RBAC versus IAM conceptual understanding; do not list it as an unresolved misconception. Runtime identity, image-pull distinction, binding placement, S3 scope and real-operation verification remain revision priorities. No new question authorized.
