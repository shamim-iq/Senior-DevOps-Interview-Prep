# Terraform Interview Progress

**Active topic: Phase 1 / Terraform.** Started 2026-10-15. RAG is paused with Q03 preserved.

## Assessment Agreement

- Revised by user request on 2026-10-17: ten initial questions plus at most five focused follow-up scenarios (Q11–Q15), asked one at a time. Stop earlier if independent answers sufficiently address the priority gaps. Do not add questions beyond this cap without a new request.
- Use the four-year DevOps / Platform Engineer baseline in AGENTS.md. Include practical evidence interpretation and safe production decisions.
- Recovery tracking requested 2026-10-18: for each follow-up, explicitly map the assessed gap to its original question and label it resolved, partially improved, or still unresolved, citing evidence from the new answer. Mark gaps outside the scenario as not reassessed. Preserve original scores; close revision checkboxes only when independent evidence supports resolution.
- After each attempt: individual verdict, score out of 10, credited strengths, explained deductions, concise corrected answer and revision needs. Label the required answer-specific acceptance estimate as subjective coaching, not a hiring probability.
- After Q10: interim consolidation. At the end of the shortened follow-up cycle: final verdict based on actual attempts, topic evidence, safety, independence, strengths and unresolved gaps. Distinguish coverage from mastery; preserve historical scores and dated retests.
- Adapt remaining scenarios to gaps while maintaining breadth. Retests count within the five-question follow-up cap; do not disguise extra questions as lengthy multipart scenarios. No future answers or hints before an attempt.
- Save question/answer files only after attempts. Commit reviewed progress locally; push only when explicitly requested. Follow AGENTS.md for all Git operations.

## Metrics

| Metric | Status |
| --- | --- |
| Evaluated questions | 11 completed; 1 / up to 5 focused follow-ups assessed |
| Average score | Latest per-question: 7.27/10 (80 / 11); original attempts: 6.77/10 (74.5 / 11) |
| Individual verdicts | Q01 revised: sound; Q02: recovery gaps; Q03: version/isolation gaps; Q04 revised: core concepts sound; Q05: state/code sound; Q06: dependency gaps; Q07: input-contract gaps; Q08: provider mapping and migration gaps; Q09: import execution gaps; Q10: strong version-control reasoning; Q11: correct deferred-read diagnosis |
| Final verdict | After focused follow-ups; no later than Q15 |
| Coverage | 12 / 12 broad aspects attempted; mastery and remaining subtopics pending |

## Current Position

Q12 — Interrupted apply and safe recovery; awaiting an answer.

A production CI apply lost its runner connection. A retry reports a state lock. AWS shows a newly created S3 bucket containing application data, but the correct backend's state does not list it; its resource block is still in Git. The old runner's status is initially uncertain. How would you establish whether recovery can safely proceed and bring the bucket under Terraform management without deleting data? Include the essential commands or a short configuration excerpt and how you would verify the result.

## Coverage Checklist

Checked means substantively assessed, not mastered. Link evidence after each evaluated attempt.

- [x] ✅ Plan interpretation, resource lifecycle and safe changes — Q01; lifecycle semantics and diagnosis need retesting.
- [x] ✅ State, remote backends, locking and recovery — Q02; stale-lock verification needs retest.
- [x] ✅ Drift and changes made outside Terraform — Q05; least-privilege investigation and verification need retest.
- [x] ✅ Import and adoption of existing infrastructure — [Q09](questions/Q09-import-existing-s3-bucket.md) retests Q02; preservation improved, import mechanics/verification remain.
- [x] ✅ Refactoring, resource addresses and moved blocks — Q04 revised: mapping understood; independent retest required.
- [x] ✅ Modules, interfaces and versioning — Q03; pinning needs retest; output/interface depth remains.
- [x] ✅ Variables, locals, outputs and type validation — Q07 input design attempted; required inputs/validation need retest; locals/outputs depth remains.
- [x] ✅ Dependencies, data sources and unknown values — Q06/Q11 assessed; deferred lookup and broad-dependency diagnosis improved; implicit-reference/hidden-dependency precision remains.
- [x] ✅ count, for_each and stable resource identity — Q04 revised: index shift and stable keys understood; independent retest pending.
- [x] ✅ Providers, aliases, constraints and dependency lock files — Q03/Q08 version control and aliases attempted; [Q10](questions/Q10-provider-lock-reproducible-ci.md) demonstrates sound provider locking/upgrades; module mapping and concrete evidence interpretation remain.
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
| [Q10](questions/Q10-provider-lock-reproducible-ci.md) | Provider locks, constraints and controlled upgrades | 8.5/10 | Strong diagnosis and upgrade strategy | Compare actual versions/plan changes; regenerate production plan |
| [Q11](questions/Q11-data-source-deferred-read.md) | Deferred reads, unknown values and replacement | 8.5/10 | Correct cause and fix | Conditional deferral; exact plan/connectivity evidence |

Q01 and Q04 reassessments revise the same questions after feedback; neither is a new numbered question or independent retest. Latest-score average: 80 / 11 = 7.27/10 (rounded). Original-attempt average: 74.5 / 11 = 6.77/10 (rounded). Coverage means assessed, not mastered; untested subtopics and independent retests remain pending.

## Revision and Final Assessment

- [ ] Q01: retest replacement diagnosis, lifecycle semantics and post-apply verification.
- [ ] Q02: verify stale lock, preserve/import untracked resources and enforce CI concurrency.
- [ ] Q03: pin module revisions and enforce backend/role isolation; provider locking improved in Q10.
- [ ] Q04: retest index shifting, stable keys and address migration with actual instance IDs.
- [ ] Q05: investigate and minimize emergency access; explain optional refresh-only; verify allowed/denied traffic.
- [ ] Q06: retest implicit references, hidden dependencies and fresh-environment verification.
- [ ] Q07: require critical inputs, validate values and verify structured production policy.
- [ ] Q08: map module providers, verify destinations and preserve resources across regional changes.
- [ ] Q09: retain resource configuration, import through normal plan/apply and verify identity/differences; Q02 preservation decision improved.
- [ ] Complete the shortened follow-up cycle (at most five additional scenarios).
- [x] ✅ Consolidate evidence after Q10 — see Feedback.md first-ten review.
- [ ] Retest demonstrated weaknesses within the shortened follow-up cycle.
- [ ] At cycle closure, calculate the actual average and deliver the final Terraform-specific verdict with practical limits and priorities.

Unassessed skills remain N/A. Do not infer overall role readiness from Terraform alone.

## Focused follow-up strategy — revised 2026-10-17

User superseded the original 20-question plan with at most five additional questions. Preserve Q01–Q10 scores; Q11 assessed, Q12 pending. These are compact scenarios, not five bundles of separate interviews.

| Slot | Focus | Earlier evidence |
| --- | --- | --- |
| Q11 (assessed 8.5/10) | Dependency reasoning, unknown values and replacement-plan evidence | Q01/Q06 |
| Q12 (pending) | Interrupted apply: lock ownership, import and recovery verification | Q02/Q09 |
| Q13 candidate | Stable identity and safe address migration | Q04 |
| Q14 candidate | Module input contract and a meaningful production validation check | Q07; Q03 interfaces |
| Q15 candidate | Module provider mapping and effective account/region isolation | Q03/Q08 |

Adapt unasked slots to demonstrated gaps. Incorporate related lifecycle, drift, outputs or pipeline safeguards only when naturally relevant; do not force every remaining subtopic into each scenario. No repeated general safety discussion is required when already demonstrated.

After each answer, distinguish independently corrected gaps from coached understanding and remaining uncertainty. Stop before five only if priority gaps have sufficient independent evidence of correct diagnosis, safe execution and verification. A score alone is not proof of closure. At the cap, deliver the verdict even if weaknesses remain; report them honestly rather than adding questions automatically. Untested breadth stays unassessed and unresolved revision boxes remain unchecked. No mastery or hiring guarantee follows from finishing this cycle.

## Weakness recovery — Q11, 2026-10-18

- [x] ✅ Q06 broad-dependency misuse resolved in Q11's independent-lookup scenario; [evidence](questions/Q11-data-source-deferred-read.md).
- [x] ✅ Q01 replacement-cause reasoning resolved in this scenario: unknown VPC ID and replacement-sensitive endpoint identified.
- [ ] Q06 implicit-reference/hidden-dependency distinction: partially improved, not fully demonstrated. Original EC2/fresh-environment gap not reassessed.
- [ ] Q01/Q06 verification: partially improved through re-planning; exact plan criteria and post-change connectivity remain.
- Other prior gaps, including lifecycle semantics: not reassessed. Original scores and composite revision items remain unchanged.
