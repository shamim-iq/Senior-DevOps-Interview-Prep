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
| Evaluated questions | 9 / 20 |
| Average score | Latest per-question: 7.00/10 (63 / 9); original attempts: 6.39/10 (57.5 / 9) |
| Individual verdicts | Q01 revised: sound; Q02: recovery gaps; Q03: version/isolation gaps; Q04 revised: core concepts sound; Q05: state/code sound; Q06: dependency gaps; Q07: input-contract gaps; Q08: provider mapping and migration gaps; Q09: import execution gaps |
| Final verdict | Pending Q20 |
| Coverage | 12 / 12 broad aspects attempted; mastery and remaining subtopics pending |

## Current Position

Q10 — Provider versions and reproducible CI plans; awaiting an answer.

The same Terraform commit produces a no-change plan on your laptop but proposes production changes in a fresh CI runner. Both target the correct backend and account. The AWS provider constraint is `~> 5.0`; `.terraform.lock.hcl` is ignored by Git, and CI runs `terraform init -upgrade` on every deployment. A teammate suggests approving CI's plan because the configuration has not changed. How would you investigate the difference, restore reproducible deployments and safely introduce future provider upgrades? Include the essential commands or configuration.

## Coverage Checklist

Checked means substantively assessed, not mastered. Link evidence after each evaluated attempt.

- [x] ✅ Plan interpretation, resource lifecycle and safe changes — Q01; lifecycle semantics and diagnosis need retesting.
- [x] ✅ State, remote backends, locking and recovery — Q02; stale-lock verification needs retest.
- [x] ✅ Drift and changes made outside Terraform — Q05; least-privilege investigation and verification need retest.
- [x] ✅ Import and adoption of existing infrastructure — [Q09](questions/Q09-import-existing-s3-bucket.md) retests Q02; preservation improved, import mechanics/verification remain.
- [x] ✅ Refactoring, resource addresses and moved blocks — Q04 revised: mapping understood; independent retest required.
- [x] ✅ Modules, interfaces and versioning — Q03; pinning needs retest; output/interface depth remains.
- [x] ✅ Variables, locals, outputs and type validation — Q07 input design attempted; required inputs/validation need retest; locals/outputs depth remains.
- [x] ✅ Dependencies, data sources and unknown values — Q06 ordering attempted; implicit references need retest; data-source and unknown-value depth remains.
- [x] ✅ count, for_each and stable resource identity — Q04 revised: index shift and stable keys understood; independent retest pending.
- [x] ✅ Providers, aliases, constraints and dependency lock files — Q03/Q08 version control and aliases attempted; module mapping and lock-file handling need retest.
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
| [Q06](questions/Q06-dependencies-creation-order.md) | Dependency ordering and investigation | 6/10 | Selective ordering understood; implicit dependencies missed | References; hidden dependencies; fresh test |
| [Q07](questions/Q07-module-input-validation.md) | Input contracts, environment inputs and plan policy | 6.5/10 | Useful pipeline controls; module validation missing | Required inputs; types; validation; plan JSON |
| [Q08](questions/Q08-provider-alias-module-region.md) | Regional aliases and module provider selection | 6.5/10 | Alias concept correct; module/recovery details missing | Provider map; identity checks; preserve deployed resources |
| [Q09](questions/Q09-import-existing-s3-bucket.md) | Existing-resource import; Q02 recovery retest | 6/10 | Preservation improved; execution incorrect | Keep resource; normal import plan/apply; verify mapping |

Q01 and Q04 reassessments revise the same questions after feedback; neither is a new numbered question or independent retest. Latest-score average: 63 / 9 = 7.00/10 (rounded). Original-attempt average: 57.5 / 9 = 6.39/10 (rounded). Coverage means assessed, not mastered; untested subtopics and independent retests remain pending.

## Revision and Final Assessment

- [ ] Q01: retest replacement diagnosis, lifecycle semantics and post-apply verification.
- [ ] Q02: verify stale lock, preserve/import untracked resources and enforce CI concurrency.
- [ ] Q03: pin module revisions, distinguish provider locks, and enforce backend/role isolation.
- [ ] Q04: retest index shifting, stable keys and address migration with actual instance IDs.
- [ ] Q05: investigate and minimize emergency access; explain optional refresh-only; verify allowed/denied traffic.
- [ ] Q06: retest implicit references, hidden dependencies and fresh-environment verification.
- [ ] Q07: require critical inputs, validate values and verify structured production policy.
- [ ] Q08: map module providers, verify destinations and preserve resources across regional changes.
- [ ] Q09: retain resource configuration, import through normal plan/apply and verify identity/differences; Q02 preservation decision improved.
- [ ] Complete 20 evaluated attempts.
- [ ] Consolidate evidence after Q10.
- [ ] Retest demonstrated weaknesses within the agreed 20 questions.
- [ ] After Q20, calculate the actual average and deliver the final Terraform-specific verdict with practical limits and priorities.

Unassessed skills remain N/A. Do not infer overall role readiness from Terraform alone.
