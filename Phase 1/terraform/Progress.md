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
| Evaluated questions | 2 / 20 |
| Average score | Latest per-question: 7.5/10 ((8 + 7) / 2); original attempts: 6.5/10 ((6 + 7) / 2) |
| Individual verdicts | Q01 revised: sound approach; Q02: good reasoning, recovery safeguards need refinement |
| Final verdict | Pending Q20 |
| Coverage | 4 / 12 aspects assessed |

## Current Position

Q03 — Reusable modules across environments; awaiting an answer.

Your team has copied Terraform configurations for dev, QA and production. Fixes are applied inconsistently, and a shared module update recently changed production unexpectedly. How would you organize reusable modules and environment configuration, control module versions and roll out changes safely without mixing state or credentials?

## Coverage Checklist

Checked means substantively assessed, not mastered. Link evidence after each evaluated attempt.

- [x] ✅ Plan interpretation, resource lifecycle and safe changes — Q01; lifecycle semantics and diagnosis need retesting.
- [x] ✅ State, remote backends, locking and recovery — Q02; stale-lock verification needs retest.
- [ ] Drift and changes made outside Terraform
- [x] ✅ Import and adoption of existing infrastructure — Q02 recovery decision assessed; import was missed, so revision remains.
- [ ] Refactoring, resource addresses and moved blocks
- [ ] Modules, interfaces and versioning
- [ ] Variables, locals, outputs and type validation
- [ ] Dependencies, data sources and unknown values
- [ ] count, for_each and stable resource identity
- [ ] Providers, aliases, constraints and dependency lock files
- [ ] Environment/account isolation, secrets and access
- [x] ✅ CI/CD, tests, policy checks and partial-failure recovery — Q01/Q02 approvals and recovery assessed; tests/policy depth and concurrency remain.

## Individual Results

| Question | Assessed aspects | Score | Verdict | Revision |
| --- | --- | --- | --- | --- |
| [Q01](questions/Q01-unexpected-database-replacement.md) | Plan safety and lifecycle; CI approval discussed | Original 6/10; revised 8/10 (2026-10-17) | Revised after feedback: sound approach | Exact replacement evidence; saved plan; verify result |
| [Q02](questions/Q02-state-lock-interrupted-pipeline.md) | Locking, partial recovery, untracked resources and CI | 7/10 | Good reasoning; recovery safeguards need refinement | Prove stale lock; import; concurrency |

Q01 reassessment is a revision of the same question, not a new numbered question or independent retest. Latest-score average includes revised Q01 (8) and Q02 (7); original baseline includes Q01 (6) and Q02 (7). Coverage means assessed, not mastered; broad checked groups retain untested subtopics.

## Revision and Final Assessment

- [ ] Q01: retest replacement diagnosis, lifecycle semantics and post-apply verification.
- [ ] Q02: verify stale lock, preserve/import untracked resources and enforce CI concurrency.
- [ ] Complete 20 evaluated attempts.
- [ ] Consolidate evidence after Q10.
- [ ] Retest demonstrated weaknesses within the agreed 20 questions.
- [ ] After Q20, calculate the actual average and deliver the final Terraform-specific verdict with practical limits and priorities.

Unassessed skills remain N/A. Do not infer overall role readiness from Terraform alone.
