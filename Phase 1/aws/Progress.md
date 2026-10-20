# AWS Interview Progress

**Paused by user request on 2026-10-20 while Kubernetes is active.** Started 2026-10-18. Preserve AWS Q11 and deferred Q05, all scores and outstanding gaps. Terraform also remains paused.

## Assessment agreement

- Ten initial scenario questions, one at a time, calibrated to four years of DevOps / Platform experience. Focus on practical AWS decisions, evidence, safe mitigation and verification.
- Review after ten evaluated attempts. If needed, ask up to five more (Q11–Q15), primarily retesting weaknesses; use remaining slots for important uncovered scope. Maximum 15 total without a new request; fewer follow-ups if sufficient evidence exists.
- Combine related aspects naturally, not as lengthy bundles of separate questions. No answers/hints before an attempt. Create QNN answer files only after evaluation.
- Preserve original attempts/scores. Follow-ups explicitly mark earlier gaps resolved, partially improved or still unresolved, with evidence; unrelated gaps are not reassessed.
- Integrate observability in relevant AWS scenarios and link substantive evidence in ../observability/. Do not add a standalone observability cycle or duplicate scores.
- After each evaluation: concise feedback, score /10 and explicitly subjective answer-specific acceptance estimate; update coverage counts, revision needs and next pending question. Commit locally; push only when asked.

## Metrics

| Metric | Status |
| --- | --- |
| Initial cycle | 9 / 10 evaluated |
| Optional follow-ups | 0 / up to 5; need determined after Q10 |
| Latest question | Q10 evaluated; Q11 pending; Q05 deferred (unattempted) |
| Average score | 7.11/10 (64 / 9) |
| Coverage | 12 / 15 aspects sampled; subtopics and mastery remain pending |
| Readiness | Initial evidence: sound diagnosis; restoration and recovery verification need retest |

Prior AWS-related discussions in Terraform, Kubernetes and RAG are context, not automatically credited AWS scores or completed coverage.

## Current position — Q11 preserved for resumption

A production EKS application uses RDS PostgreSQL and S3 uploads in one AWS Region. The business requires recovery from a Region-wide outage within 60 minutes and at most 15 minutes of lost data. Today, Terraform and Helm are in Git, RDS snapshots are copied to a second Region once nightly, and S3 versioning is enabled only in the primary Region. A teammate says rebuilding EKS from Git guarantees those targets. How would you assess the current plan, choose a practical recovery design and demonstrate that the application and its data can actually recover within the targets?

Q11 will be the tenth actual assessment and trigger the first-cycle review. Q05 remains deferred. Any additional questions remain within the maximum of fifteen assessed attempts.

## Deferred — Q05

**Deferred by user request on 2026-10-19.** Preserve this question for later; no attempt, score or coverage credit. SQS is not listed in the supplied résumé and the user reports limited depth; treat eventual assessment as introductory learning, not a gap in claimed experience. Do not automatically resume this question until the user asks to revisit it. AWS remains active; continue with the current pending scenario while retaining this question. This deferral does not consume an evaluated-question slot or extend the 15-question cap.

A Lambda function consumes order messages from a standard SQS queue and calls a payment service. During a traffic spike, some orders are charged twice, the queue backlog grows and one malformed message fails repeatedly. A teammate proposes increasing Lambda concurrency to its maximum and deleting the troublesome messages. How would you diagnose and safely correct processing, protect the payment service and verify that orders are neither lost nor charged twice?

## Coverage checklist

Check only after substantive attempt and evaluation, with question links. A check means assessed, not mastered; weak subskills stay in revision.

- [x] ✅ VPC routing/NAT/endpoints — [Q04](questions/Q04-s3-endpoint-nat-routing.md); Q10 adds EKS IP exhaustion; subnet/CNI measurement and route/policy implementation need retest.
- [x] ✅ Safe network access — [Q01](questions/Q01-alb-unhealthy-targets.md); private isolation assessed, precise SG/NACL rules need retest.
- [x] ✅ EC2 and ALB target health — [Q01](questions/Q01-alb-unhealthy-targets.md); Auto Scaling and AZ resilience depth unassessed.
- [x] ✅ IAM role and least-privilege access — [Q02](questions/Q02-s3-kms-access-denied.md); Q09 also assesses IRSA/Helm mapping; runtime identity/trust proof need retest; cross-account depth unassessed.
- [x] ✅ S3 encryption/access — [Q02](questions/Q02-s3-kms-access-denied.md); default encryption needs correction; versioning/lifecycle unassessed.
- [x] ✅ EBS/EFS shared storage — [Q08](questions/Q08-efs-shared-uploads.md); safe migration, mounts and cross-instance verification need retest; snapshot depth remains.
- [x] ✅ RDS Multi-AZ failover/connectivity — [Q03](questions/Q03-rds-failover-connectivity.md); same-Region topology and recovery proof need retest; Aurora depth unassessed.
- [x] ✅ CloudFront/private-S3 delivery — [Q06](questions/Q06-cloudfront-private-s3-403.md); origin authorization/cache precision need retest; Route 53/TLS/ACM depth unassessed.
- [ ] CloudWatch metrics/logs/alarms and CloudTrail audit investigation.
- [x] ✅ KMS key access — [Q02](questions/Q02-s3-kms-access-denied.md); key policy/scope need retest; Secrets Manager/rotation unassessed.
- [ ] Lambda/API Gateway: permissions, failures, concurrency and integration.
- [ ] SQS/SNS/EventBridge: delivery failures, retries and safe processing.
- [x] ✅ ECS/Fargate/ECR image delivery — [Q07](questions/Q07-fargate-ecr-image-pull.md); execution role correct, concrete evidence/network/rollout gates need retest; broader container hosting depth remains.
- [x] ✅ Failover versus snapshot recovery — [Q03](questions/Q03-rds-failover-connectivity.md); regional DR, RTO/RPO and restore validation remain incomplete.
- [x] ✅ NAT cost/dependency trade-off — [Q04](questions/Q04-s3-endpoint-nat-routing.md); cost validation, quotas and governance remain unassessed.

## Adaptive coverage plan

Use Q01 for the pending ALB/EC2 incident. Spread Q02–Q10 across identity/security, storage, databases, networking/delivery, serverless/events, containers and resilience/cost. Combine relevant pairs (for example access with storage, or database availability with recovery) while keeping each scenario manageable. Choose exact questions after reviewing each answer; this plan is not coverage credit.

After ten evaluated attempts, report measured strengths, remaining gaps and a realistic AWS-specific verdict. Allocate up to five follow-ups based on the most consequential weaknesses and uncovered essentials. At the cap, report residual gaps instead of automatically extending. This bounded cycle samples important AWS capabilities; it does not establish exhaustive service mastery or overall hiring probability.

## Results

| Question | Score | Strength | Revision |
| --- | --- | --- | --- |
| [Q01](questions/Q01-alb-unhealthy-targets.md) | 7/10 | Private isolation; port/path and app checks | Narrow access checks; rollback; recovery proof |
| [Q02](questions/Q02-s3-kms-access-denied.md) | 7/10 | KMS access diagnosis; success-rate verification | Key policy/scope; denied-operation evidence; actual-role test |
| [Q03](questions/Q03-rds-failover-connectivity.md) | 7/10 | Stable endpoint; DNS cache; standby promotion | Same-Region topology; connection pools; transaction/data checks |
| [Q04](questions/Q04-s3-endpoint-nat-routing.md) | 7/10 | S3/payment traffic separation; outcome monitoring | Gateway routes; access policies; actual-path/cost verification |
| [Q06](questions/Q06-cloudfront-private-s3-403.md) | 7.5/10 | Policy/path diagnosis; actual CloudFront test | OAC/OAI identity; error-cache invalidation; boundary checks |
| [Q07](questions/Q07-fargate-ecr-image-pull.md) | 7.5/10 | Execution-role identity; rollback and staged rollout | Stopped reasons; exact image; network path; health gates |
| [Q08](questions/Q08-efs-shared-uploads.md) | 7/10 | EBS AZ limit; EFS shared-filesystem selection | Safe live-data cutover; mounts/access; cross-instance tests |
| [Q09](questions/Q09-eks-irsa-helm-access.md) | 7.5/10 | IRSA/Helm configuration diagnosis; least privilege | Runtime caller; trust conditions; allowed/denied tests |
| [Q10](questions/Q10-eks-subnet-ip-exhaustion.md) | 6.5/10 | Subnet constraint; preserves healthy pods | Actual IP evidence; prefix/Calico limits; placement and validation |

## Revision and readiness

- [ ] Q01: verify ALB-to-target rules, select a safe restoration action and prove recovery through target health and real requests.
- [ ] Q02: verify key policy, exact key scope, denial evidence and actual-role read; correct default-encryption assumption. Q01 recovery verification partially improved, not closed.
- [ ] Q03: distinguish AZ availability from regional DR; renew stale sessions; verify transactions/data rather than assuming loss is impossible.
- [ ] Q04: configure gateway endpoint associations/prefix-list routing and scoped access; prove both paths and cost effect.
- [ ] Q06: specify origin identity/distribution scope, distinguish error-cache expiry/invalidation and verify content plus private S3 boundary. Actual-path test selection improved.
- [ ] Q07: inspect stopped reasons/exact image, specify pull-network path and validate new-task health/requests. Correct execution-role and mitigation selection demonstrated.
- [ ] Q08: preserve writes during migration, configure mount targets/access and prove consistent files from both instances.
- [ ] Q09: prove actual pod identity, verify issuer/sub/aud and test permitted/denied access after correction.
- [ ] Q10: distinguish pod limits/IP headroom, prefix capacity, Calico modes and HPA/VPA; demonstrate selective rescheduling and application recovery.
- [ ] Complete the first ten assessments and interim review.
- [ ] Retest demonstrated weaknesses where needed within the five-follow-up cap.
- [ ] Demonstrate safe diagnosis, mitigation and recovery using concrete evidence.
- [ ] Deliver final verdict at cycle closure with unresolved and unassessed areas explicit.

## EKS emphasis — 2026-10-19

Prioritize EKS in upcoming unasked AWS scenarios, integrating IAM/workload identity, VPC networking, node capacity, storage, upgrades and operational evidence where naturally relevant. Preserve pending Q08 and deferred Q05. Use remaining initial-cycle slots and any needed follow-ups within the existing maximum of 15 assessed attempts; no extra EKS quota. Do not cram all aspects into one question.

Keep AWS service decisions primary here. When Kubernetes resumes, EKS is the primary managed platform and AKS is secondary, with deeper Kubernetes behavior and platform comparisons. Cross-link substantive attempts between topic progress files without copying scores or counting an answer twice. Do not mark EKS mastered from Q07's ECS evidence. Prior Kubernetes questions guide retests but are not new AWS coverage credit.
