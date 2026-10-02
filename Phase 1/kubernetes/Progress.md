# Kubernetes Interview Progress

| Metric | Current status |
| --- | --- |
| Questions Attempted | 1 / 10 in the first cycle |
| Average Score | 6/10 |
| Average Acceptance Probability | 55% — subjective answer-specific estimate |
| Topic Coverage | Q01: deployment failure, incident triage, GitOps; resource and identity reasoning sampled |
| Current Strengths | Incident ownership, logs/events awareness, mitigation priority |
| Current Weaknesses | Command precision, evidence-based resource diagnosis, IRSA distinction, recovery validation |
| Readiness Trend | Initial baseline only; overall readiness not yet established |

## Active Question

Q02 — Resource troubleshooting; awaiting an answer. Chosen to test the Q01 assumption that larger nodes solve crashing containers.

An EKS API container repeatedly restarts during peak traffic. Its last termination reason is OOMKilled, its memory request is 256Mi, and its memory limit is 512Mi. Historical metrics show memory rising toward 512Mi before each restart, while the node has several GiB of available memory and no MemoryPressure condition. A teammate proposes moving the workload to a larger node. How would you assess that proposal and choose, validate, and follow up on a safe production fix?

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

## Retesting and Coverage

- Next: container memory limits versus node capacity (Q02).
- Later: AWS workload identity and native configuration; GitOps rollback safeguards; request-path diagnosis and recovery validation.
- Scheduling, autoscaling, storage, maintenance, NetworkPolicy/CoreDNS and AKS remain unassessed.
- No topic-level percentages or readiness trend inferred from a single answer.
