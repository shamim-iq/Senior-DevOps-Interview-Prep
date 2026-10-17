# Terraform Interview Progress

**Active topic: Phase 1 / Terraform.** Started 2026-10-15. RAG is paused with Q03 preserved.

## Assessment Agreement

- Exactly 20 scenario-based questions, asked one at a time. Wait for each answer before evaluating or asking the next question. Do not extend beyond Q20 without a new request.
- Use the four-year DevOps / Platform Engineer baseline in AGENTS.md. Include practical evidence interpretation and safe production decisions.
- After each attempt: individual verdict, score out of 10, credited strengths, explained deductions, concise corrected answer and revision needs. Label the required answer-specific acceptance estimate as subjective coaching, not a hiring probability.
- After Q10: interim consolidation. After Q20: final verdict based on all 20 scores, topic evidence, safety, independence, strengths and unresolved gaps. Distinguish coverage from mastery; preserve historical scores and dated retests.
- Adapt remaining scenarios to gaps while maintaining breadth. Retests count within the 20-question limit. No future answers or hints before an attempt.
- Save question/answer files only after attempts. Commit reviewed progress locally; push only when explicitly requested. Follow AGENTS.md for all Git operations.

## Metrics

| Metric | Status |
| --- | --- |
| Evaluated questions | 3 / 20 |
| Average score | Latest per-question: 7.5/10 ((8 + 7 + 7.5) / 3); original attempts: 6.83/10 ((6 + 7 + 7.5) / 3) |
| Individual verdicts | Q01 revised: sound; Q02: recovery gaps; Q03: sound structure, version/isolation gaps |
| Final verdict | Pending Q20 |
| Coverage | 7 / 12 aspects assessed |

## Current Position

Q04 — Resource identity after a list change; awaiting an answer.

Your Terraform configuration creates several production EC2 instances using `count` over a list of service names. You remove the middle service, but the plan proposes replacing or changing instances for services you intended to keep. Why might this happen, and how would you make the change and improve the configuration without unnecessarily recreating the remaining instances?

## Coverage Checklist

Checked means substantively assessed, not mastered. Link evidence after each evaluated attempt.

- [x] ✅ Plan interpretation, resource lifecycle and safe changes — Q01; lifecycle semantics and diagnosis need retesting.
- [x] ✅ State, remote backends, locking and recovery — Q02; stale-lock verification needs retest.
- [ ] Drift and changes made outside Terraform
- [x] ✅ Import and adoption of existing infrastructure — Q02 recovery decision assessed; import was missed, so revision remains.
- [ ] Refactoring, resource addresses and moved blocks
- [x] ✅ Modules, interfaces and versioning — Q03; pinning needs retest; output/interface depth remains.
- [ ] Variables, locals, outputs and type validation
- [ ] Dependencies, data sources and unknown values
- [ ] count, for_each and stable resource identity
- [x] ✅ Providers, aliases, constraints and dependency lock files — Q03 version control attempted; aliases and lock-file handling remain.
- [x] ✅ Environment/account isolation, secrets and access — Q03; explicit backend and role boundaries need retest.
- [x] ✅ CI/CD, tests, policy checks and partial-failure recovery — Q01/Q02 approvals and recovery assessed; tests/policy depth and concurrency remain.

## Individual Results

| Question | Assessed aspects | Score | Verdict | Revision |
| --- | --- | --- | --- | --- |
| [Q01](questions/Q01-unexpected-database-replacement.md) | Plan safety and lifecycle; CI approval discussed | Original 6/10; revised 8/10 (2026-10-17) | Revised after feedback: sound approach | Exact replacement evidence; saved plan; verify result |
| [Q02](questions/Q02-state-lock-interrupted-pipeline.md) | Locking, partial recovery, untracked resources and CI | 7/10 | Good reasoning; recovery safeguards need refinement | Prove stale lock; import; concurrency |
| [Q03](questions/Q03-modules-environment-isolation.md) | Modules, provider versions, environment isolation and secrets | 7.5/10 | Sound design; version/isolation gaps | Pin modules; lock providers; scope backend/roles |

Q01 reassessment is a revision of the same question, not a new numbered question or independent retest. Latest-score average includes revised Q01 (8), Q02 (7) and Q03 (7.5); original baseline includes Q01 (6), Q02 (7) and Q03 (7.5). Coverage means assessed, not mastered; broad checked groups retain untested subtopics.

## Revision and Final Assessment

- [ ] Q01: retest replacement diagnosis, lifecycle semantics and post-apply verification.
- [ ] Q02: verify stale lock, preserve/import untracked resources and enforce CI concurrency.
- [ ] Q03: pin module revisions, distinguish provider locks, and enforce backend/role isolation.
- [ ] Complete 20 evaluated attempts.
- [ ] Consolidate evidence after Q10.
- [ ] Retest demonstrated weaknesses within the agreed 20 questions.
- [ ] After Q20, calculate the actual average and deliver the final Terraform-specific verdict with practical limits and priorities.

Unassessed skills remain N/A. Do not infer overall role readiness from Terraform alone.
