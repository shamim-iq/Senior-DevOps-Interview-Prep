# AWS Interview Progress

**Active topic: Phase 1 / AWS.** Started 2026-10-18. Terraform paused by user request with Q12 preserved; no readiness certification implied.

## Assessment agreement

- Ten initial scenario questions, one at a time, calibrated to four years of DevOps / Platform experience. Focus on practical AWS decisions, evidence, safe mitigation and verification.
- Review after Q10. If needed, ask up to five more (Q11–Q15), primarily retesting weaknesses; use remaining slots for important uncovered scope. Maximum 15 total without a new request; fewer follow-ups if sufficient evidence exists.
- Combine related aspects naturally, not as lengthy bundles of separate questions. No answers/hints before an attempt. Create QNN answer files only after evaluation.
- Preserve original attempts/scores. Follow-ups explicitly mark earlier gaps resolved, partially improved or still unresolved, with evidence; unrelated gaps are not reassessed.
- Integrate observability in relevant AWS scenarios and link substantive evidence in ../observability/. Do not add a standalone observability cycle or duplicate scores.
- After each evaluation: concise feedback, score /10 and explicitly subjective answer-specific acceptance estimate; update coverage counts, revision needs and next pending question. Commit locally; push only when asked.

## Metrics

| Metric | Status |
| --- | --- |
| Initial cycle | 4 / 10 evaluated |
| Optional follow-ups | 0 / up to 5; need determined after Q10 |
| Latest question | Q04 evaluated; Q05 deferred (unattempted) |
| Average score | 7.00/10 (28 / 4) |
| Coverage | 9 / 15 aspects sampled; subtopics and mastery remain pending |
| Readiness | Initial evidence: sound diagnosis; restoration and recovery verification need retest |

Prior AWS-related discussions in Terraform, Kubernetes and RAG are context, not automatically credited AWS scores or completed coverage.

## Current position — Q05 deferred

**Deferred by user request on 2026-10-19.** Preserve this question for later; no attempt, score or coverage credit. SQS is not listed in the supplied résumé and the user reports limited depth; treat eventual assessment as introductory learning, not a gap in claimed experience. Do not automatically resume this question until the user asks to revisit it. AWS remains the active topic; no replacement question has been selected. This deferral does not consume an evaluated-question slot or extend the 15-question cap.

A Lambda function consumes order messages from a standard SQS queue and calls a payment service. During a traffic spike, some orders are charged twice, the queue backlog grows and one malformed message fails repeatedly. A teammate proposes increasing Lambda concurrency to its maximum and deleting the troublesome messages. How would you diagnose and safely correct processing, protect the payment service and verify that orders are neither lost nor charged twice?

## Coverage checklist

Check only after substantive attempt and evaluation, with question links. A check means assessed, not mastered; weak subskills stay in revision.

- [x] ✅ VPC routing/NAT/endpoints — [Q04](questions/Q04-s3-endpoint-nat-routing.md); traffic separation understood, route/policy implementation needs retest.
- [x] ✅ Safe network access — [Q01](questions/Q01-alb-unhealthy-targets.md); private isolation assessed, precise SG/NACL rules need retest.
- [x] ✅ EC2 and ALB target health — [Q01](questions/Q01-alb-unhealthy-targets.md); Auto Scaling and AZ resilience depth unassessed.
- [x] ✅ IAM role and least-privilege access — [Q02](questions/Q02-s3-kms-access-denied.md); policy evaluation/identity verification need retest; cross-account depth unassessed.
- [x] ✅ S3 encryption/access — [Q02](questions/Q02-s3-kms-access-denied.md); default encryption needs correction; versioning/lifecycle unassessed.
- [ ] EBS/EFS storage choice, attachment constraints and snapshots.
- [x] ✅ RDS Multi-AZ failover/connectivity — [Q03](questions/Q03-rds-failover-connectivity.md); same-Region topology and recovery proof need retest; Aurora depth unassessed.
- [ ] Route 53, DNS, load balancing, TLS/ACM and CloudFront delivery.
- [ ] CloudWatch metrics/logs/alarms and CloudTrail audit investigation.
- [x] ✅ KMS key access — [Q02](questions/Q02-s3-kms-access-denied.md); key policy/scope need retest; Secrets Manager/rotation unassessed.
- [ ] Lambda/API Gateway: permissions, failures, concurrency and integration.
- [ ] SQS/SNS/EventBridge: delivery failures, retries and safe processing.
- [ ] Container hosting and image delivery: ECS/EKS/ECR service boundaries.
- [x] ✅ Failover versus snapshot recovery — [Q03](questions/Q03-rds-failover-connectivity.md); regional DR, RTO/RPO and restore validation remain incomplete.
- [x] ✅ NAT cost/dependency trade-off — [Q04](questions/Q04-s3-endpoint-nat-routing.md); cost validation, quotas and governance remain unassessed.

## Adaptive coverage plan

Use Q01 for the pending ALB/EC2 incident. Spread Q02–Q10 across identity/security, storage, databases, networking/delivery, serverless/events, containers and resilience/cost. Combine relevant pairs (for example access with storage, or database availability with recovery) while keeping each scenario manageable. Choose exact questions after reviewing each answer; this plan is not coverage credit.

After Q10, report measured strengths, remaining gaps and a realistic AWS-specific verdict. Allocate up to five follow-ups based on the most consequential weaknesses and uncovered essentials. At the cap, report residual gaps instead of automatically extending. This bounded cycle samples important AWS capabilities; it does not establish exhaustive service mastery or overall hiring probability.

## Results

| Question | Score | Strength | Revision |
| --- | --- | --- | --- |
| [Q01](questions/Q01-alb-unhealthy-targets.md) | 7/10 | Private isolation; port/path and app checks | Narrow access checks; rollback; recovery proof |
| [Q02](questions/Q02-s3-kms-access-denied.md) | 7/10 | KMS access diagnosis; success-rate verification | Key policy/scope; denied-operation evidence; actual-role test |
| [Q03](questions/Q03-rds-failover-connectivity.md) | 7/10 | Stable endpoint; DNS cache; standby promotion | Same-Region topology; connection pools; transaction/data checks |
| [Q04](questions/Q04-s3-endpoint-nat-routing.md) | 7/10 | S3/payment traffic separation; outcome monitoring | Gateway routes; access policies; actual-path/cost verification |

## Revision and readiness

- [ ] Q01: verify ALB-to-target rules, select a safe restoration action and prove recovery through target health and real requests.
- [ ] Q02: verify key policy, exact key scope, denial evidence and actual-role read; correct default-encryption assumption. Q01 recovery verification partially improved, not closed.
- [ ] Q03: distinguish AZ availability from regional DR; renew stale sessions; verify transactions/data rather than assuming loss is impossible.
- [ ] Q04: configure gateway endpoint associations/prefix-list routing and scoped access; prove both paths and cost effect.
- [ ] Complete the first ten assessments and interim review.
- [ ] Retest demonstrated weaknesses where needed within the five-follow-up cap.
- [ ] Demonstrate safe diagnosis, mitigation and recovery using concrete evidence.
- [ ] Deliver final verdict at cycle closure with unresolved and unassessed areas explicit.
