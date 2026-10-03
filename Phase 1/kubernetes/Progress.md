# Kubernetes Interview Progress

| Metric | Current status |
| --- | --- |
| Questions Attempted | 2 / 10 in the first cycle |
| Average Score | 6.25/10 — (6 + 6.5) / 2 |
| Average Acceptance Probability | 58.5% — (55 + 62) / 2; subjective answer-specific estimates |
| Topic Coverage | Q01: deployment failure, incident triage, GitOps; Q02: memory limits/OOM and resource diagnosis; identity sampled |
| Current Strengths | Incident ownership, previous logs, measuring usage, distinguishing larger nodes from container limits |
| Current Weaknesses | Alternative causes, request/limit precision, capacity-aware mitigation, IRSA distinction, recovery validation and conciseness |
| Readiness Trend | 6 → 6.5; modest improvement after feedback, insufficient evidence for overall readiness |

## Active Question

Q03 — HPA, Pending pods and node autoscaling; awaiting an answer. Extends resource reasoning into scheduling and capacity.

During peak traffic, an EKS API's CPU-based HPA raises desired replicas from 4 to 10. Four pods remain Running and six stay Pending. Pending-pod events report Insufficient cpu, although node dashboards show only about 35% CPU usage. Cluster Autoscaler is installed, but no new nodes appear and latency is rising. How would you explain the discrepancy, investigate why capacity is not increasing, and restore service safely?

## Coverage Plan

Across the first 10 questions, assess deployment and pod failures; Services, Ingress, DNS and networking; scheduling; resource management; autoscaling; storage; workload identity and RBAC; maintenance and PDBs; GitOps; and observability in realistic EKS/AKS scenarios. Combine related areas and adapt difficulty to demonstrated performance.

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

## Retesting and Coverage

- Next: scheduling requests versus measured usage, HPA and Cluster Autoscaler (Q03).
- Q02 improved the larger-node misconception; revisit requests/limits and safe capacity planning in a different scenario.
- Later: AWS workload identity and native configuration; GitOps rollback safeguards; request-path diagnosis and recovery validation.
- Scheduling and autoscaling are pending assessment. Storage, maintenance, NetworkPolicy/CoreDNS and AKS remain unassessed.
- No topic-level percentages inferred from two answers. Current score movement is descriptive, not proof of overall senior readiness.
