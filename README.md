# Senior DevOps Interview Preparation

Structured preparation for Senior DevOps, Platform Engineer, and SRE interviews, organized across multiple phases.

`Phase 1/` contains the current preparation work. Future phases will be added as sibling directories: `Phase 2/`, `Phase 3/`, and so on.

Each phase may cover Kubernetes, Docker, AWS, Azure, CI/CD pipelines, Terraform, Observability, Linux / Networking, Python automation, RAG, MCP, and Amazon Bedrock.

Within each topic:

- `questions/` — scenario-based interview questions and interview-ready answers.
- `Feedback.md` — knowledge gaps and improvement areas.
- `Progress.md` — interview-readiness tracking.

## Topic roadmap

- [ ] [Kubernetes](Phase%201/kubernetes/Progress.md) — paused; Q11 pending.
- [ ] Docker
- [ ] AWS
- [ ] Azure
- [ ] CI/CD pipelines
- [ ] [Terraform](Phase%201/terraform/Progress.md) — active; 20-question track; 9/20 evaluated; Q10 pending.
- [ ] Observability
- [ ] [Linux / Networking](Phase%201/linux/Progress.md) — paused; Q11 pending.
- [ ] Python
- [ ] [RAG](Phase%201/rag/Progress.md) — paused; Q03 preserved.
- [ ] [MCP](Phase%201/mcp/Progress.md) — cross-topic assessment through RAG; standalone practice later.
- [ ] [Amazon Bedrock](Phase%201/bedrock/Progress.md) — assessed alongside RAG; standalone practice later.

Each topic keeps its own coverage, scores and revision checklist in `Phase N/<topic>/Progress.md`. Completed assessments show ✅; remaining aspects stay unchecked. A topic is complete only after its agreed coverage and revision work are finished. Future phases are not yet scoped, so no overall completion percentage is assigned.

All topics use scored questions, saved answers, feedback, coverage tracking and weakness retests. Python also includes coding exercises covering scripting, files, JSON/YAML, APIs, subprocesses, error handling, logging and testing.

CI/CD questions prioritize GitHub Actions, with Jenkins secondary. Cover workflows, triggers, jobs and runners, build/test stages, artifacts, secrets and OIDC, reusable workflows, security checks, environment approvals, deployment, rollback and troubleshooting. Evaluate answers using the same four-year baseline, topic-specific scores, feedback, coverage checklist and retests as other topics.

The local `Interviews/` directory is the repository root. Keep commits on `main`; push only when explicitly requested.
