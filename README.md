# Senior DevOps Interview Preparation

Structured preparation for Senior DevOps, Platform Engineer, and SRE interviews, organized across multiple phases.

`Phase 1/` contains the current preparation work. Future phases will be added as sibling directories: `Phase 2/`, `Phase 3/`, and so on.

Each phase may cover Kubernetes, Docker, AWS, Azure, CI/CD pipelines, Terraform, Observability, Linux / Networking, Python automation, RAG, MCP, and Amazon Bedrock.

Within each topic:

- `questions/` — scenario-based interview questions and interview-ready answers.
- `Feedback.md` — knowledge gaps and improvement areas.
- `Progress.md` — interview-readiness tracking.

## Topic roadmap

- [ ] [Kubernetes](Phase%201/kubernetes/Progress.md) — Q11–Q15 follow-up cycle complete; consolidated review recorded; important gaps remain; no new question scheduled.
- [ ] Docker
- [ ] [AWS](Phase%201/aws/Progress.md) — paused; 9/10 initial questions evaluated; up to 5 targeted follow-ups if needed; Q11 pending; Q05 (SQS/Lambda) deferred.
- [ ] Azure
- [ ] [CI/CD pipelines](Phase%201/cicd/Progress.md) — active; GitHub Actions primary, Jenkins secondary; Q01–Q02 assessed, Q03 pending.
- [ ] [Terraform](Phase%201/terraform/Progress.md) — paused; 11 evaluated; 1 of up to 5 focused follow-ups assessed; Q12 pending.
- [Observability](Phase%201/observability/Progress.md) — integrated into other topics; linked evidence, no standalone assessment cycle.
- [ ] [Linux / Networking](Phase%201/linux/Progress.md) — paused; Q11 pending.
- [ ] [Python](Phase%201/python/Progress.md) — Q01–Q05 assessed; Q05 core logic resolved; CI/CD next.
- [ ] [RAG](Phase%201/rag/Progress.md) — paused; Q03 preserved.
- [ ] [MCP](Phase%201/mcp/Progress.md) — cross-topic assessment through RAG; standalone practice later.
- [ ] [Amazon Bedrock](Phase%201/bedrock/Progress.md) — assessed alongside RAG; standalone practice later.

Each topic keeps its own coverage, scores and revision checklist in `Phase N/<topic>/Progress.md`. Completed assessments show ✅; remaining aspects stay unchecked. A topic is complete only after its agreed coverage and revision work are finished. Future phases are not yet scoped, so no overall completion percentage is assigned.

Observability stays on the roadmap as integrated coverage, not a separate completion item. Its directory tracks linked answers, feedback and coverage from other topics without duplicating questions or overall scores.

All assessed topics use scored questions, saved answers, feedback, coverage tracking and weakness retests. Python also includes coding exercises covering scripting, files, JSON/YAML, APIs, subprocesses, error handling, logging and testing.

AWS scenarios emphasize EKS alongside related cloud services. When Kubernetes resumes, EKS is the primary managed platform and AKS is secondary; relevant answers are cross-linked without duplicate scores.

CI/CD questions prioritize GitHub Actions, with Jenkins secondary. Cover workflows, triggers, jobs and runners, build/test stages, artifacts, secrets and OIDC, reusable workflows, security checks, environment approvals, deployment, rollback and troubleshooting. Evaluate answers using the same four-year baseline, topic-specific scores, feedback, coverage checklist and retests as other topics.

The local `Interviews/` directory is the repository root. Keep commits on `main`; push only when explicitly requested.

Before other-topic practice each day, complete one Python coding attempt and review (Asia/Calcutta date). This is once per day across all topics, with code and any execution output recorded in Python progress. Then resume the existing topic question; Kubernetes follow-up cycle is complete; choose the next topic when ready.
