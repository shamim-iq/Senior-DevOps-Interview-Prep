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
| Evaluated questions | 5 / 20 |
| Average score | Latest per-question: 7.6/10 ((8 + 7 + 7.5 + 8 + 7.5) / 5); original attempts: 6.5/10 ((6 + 7 + 7.5 + 4.5 + 7.5) / 5) |
| Individual verdicts | Q01 revised: sound; Q02: recovery gaps; Q03: version/isolation gaps; Q04 revised: core concepts sound; Q05: state/code sound, access-validation gaps |
| Final verdict | Pending Q20 |
| Coverage | 10 / 12 aspects assessed |

## Current Position

Q06 — Dependencies and values known after apply; awaiting an answer.

A configuration creates a VPC, subnets and EC2 instances. On a clean environment, instance creation fails because the expected network dependency is not ready. A teammate proposes adding depends_on to every resource and using targeted applies in a fixed sequence. How would you investigate the dependency graph, connect resources correctly and decide when an explicit dependency is actually needed?

## Coverage Checklist

Checked means substantively assessed, not mastered. Link evidence after each evaluated attempt.

- [x] ✅ Plan interpretation, resource lifecycle and safe changes — Q01; lifecycle semantics and diagnosis need retesting.
- [x] ✅ State, remote backends, locking and recovery — Q02; stale-lock verification needs retest.
- [x] ✅ Drift and changes made outside Terraform — Q05; least-privilege investigation and verification need retest.
- [x] ✅ Import and adoption of existing infrastructure — Q02 recovery decision assessed; import was missed, so revision remains.
- [x] ✅ Refactoring, resource addresses and moved blocks — Q04 revised: mapping understood; independent retest required.
- [x] ✅ Modules, interfaces and versioning — Q03; pinning needs retest; output/interface depth remains.
- [ ] Variables, locals, outputs and type validation
- [ ] Dependencies, data sources and unknown values
- [x] ✅ count, for_each and stable resource identity — Q04 revised: index shift and stable keys understood; independent retest pending.
- [x] ✅ Providers, aliases, constraints and dependency lock files — Q03 version control attempted; aliases and lock-file handling remain.
- [x] ✅ Environment/account isolation, secrets and access — Q03; explicit backend and role boundaries need retest.
- [x] ✅ CI/CD, tests, policy checks and partial-failure recovery — Q01/Q02 approvals and recovery assessed; tests/policy depth and concurrency remain.

## Individual Results

| Question | Assessed aspects | Score | Verdict | Revision |
| --- | --- | --- | --- | --- |
| [Q01](questions/Q01-unexpected-database-replacement.md) | Plan safety and lifecycle; CI approval discussed | Original 6/10; revised 8/10 (2026-10-17) | Revised after feedback: sound approach | Exact replacement evidence; saved plan; verify result |
| [Q02](questions/Q02-state-lock-interrupted-pipeline.md) | Locking, partial recovery, untracked resources and CI | 7/10 | Good reasoning; recovery safeguards need refinement | Prove stale lock; import; concurrency |
| [Q03](questions/Q03-modules-environment-isolation.md) | Modules, provider versions, environment isolation and secrets | 7.5/10 | Sound design; version/isolation gaps | Pin modules; lock providers; scope backend/roles |
| [Q04](questions/Q04-count-stable-resource-identity.md) | Count identity and safe refactoring | Original 4.5/10; revised 8/10 (2026-10-17) | Core identity/migration corrected after feedback | Tag updates; mapping validation; independent retest |
| [Q05](questions/Q05-emergency-security-group-drift.md) | Drift, desired configuration and emergency access | 7.5/10 | Correct state/code distinction | Minimum access; optional refresh; verify traffic |

Q01 and Q04 reassessments revise the same questions after feedback; neither is a new numbered question or independent retest. Latest-score average: (8 + 7 + 7.5 + 8 + 7.5) / 5 = 7.6/10. Original-attempt average: (6 + 7 + 7.5 + 4.5 + 7.5) / 5 = 6.5/10. Coverage means assessed, not mastered; untested subtopics and independent retests remain pending.

## Revision and Final Assessment

- [ ] Q01: retest replacement diagnosis, lifecycle semantics and post-apply verification.
- [ ] Q02: verify stale lock, preserve/import untracked resources and enforce CI concurrency.
- [ ] Q03: pin module revisions, distinguish provider locks, and enforce backend/role isolation.
- [ ] Q04: retest index shifting, stable keys and address migration with actual instance IDs.
- [ ] Q05: investigate and minimize emergency access; explain optional refresh-only; verify allowed/denied traffic.
- [ ] Complete 20 evaluated attempts.
- [ ] Consolidate evidence after Q10.
- [ ] Retest demonstrated weaknesses within the agreed 20 questions.
- [ ] After Q20, calculate the actual average and deliver the final Terraform-specific verdict with practical limits and priorities.

Unassessed skills remain N/A. Do not infer overall role readiness from Terraform alone.
