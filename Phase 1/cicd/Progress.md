# CI/CD Progress

**Active from 2026-10-25.** GitHub Actions primary, Jenkins secondary. Four-year DevOps/Platform baseline; scenario-based questions, one at a time. Python Q04/Q05 completion was on 2026-10-25; check the daily ledger before a new question. Kubernetes cycle remains complete.

| Metric | Status |
| --- | --- |
| Evaluated questions | 5 |
| Average score / acceptance estimate | 7.9/10 / 74% (subjective, not hiring probability) |
| Coverage | 7/10 |
| Readiness | Controller roles improved in coached retry; artifact proof and recovery verification need independent retest |
| Pending | Q06 — Reusable workflows and matrix failure handling |
| Coached retry | Q02.1: 7/10, 65% subjective estimate; excluded from main-question average |

## Coverage

- [x] ✅ Dependencies and conditional gates — Q01; event-trigger breadth remains unassessed.
- [ ] Build/test/security scanning and trustworthy results.
- [x] ✅ Artifact promotion — Q02; digest pinning/immutability and provenance need revision.
- [x] ✅ Secrets, OIDC and least-privilege workflow permissions — Q03; exact trust matching and allow/deny verification need revision.
- [x] ✅ Environment approvals — Q01; deployment-access security depth remains unassessed.
- [x] ✅ Progressive rollout and rollback — Q02; Argo responsibilities, artifact identity and recovery gates need revision.
- [x] ✅ Runners and untrusted PR security — Q04; explicit isolation needs revision; broader supply-chain controls remain unassessed.
- [x] ✅ Concurrency and cancellation — Q05; stale-run checks and migration failure recovery need revision; caches remain unassessed.
- [ ] Reusable workflows, matrices and maintenance.
- [ ] Jenkins fundamentals, credentials, agents and pipeline troubleshooting.

Check aspects only after substantive evaluation; coverage is not mastery. Integrate observability into relevant scenarios and link actual evidence. Start with broad high-value coverage; review after ten evaluated questions, adapt to demonstrated gaps. No automatic total question quota or readiness guarantee.

## Q02.1 — Targeted retry assessed (2026-10-26)

User requested an extra coached retry after Q02. [Evaluation](questions/Q02.1-artifact-promotion-retry.md): 7/10, 65% subjective estimate. CD/Rollouts roles resolved in this coached attempt; artifact identity and lasting rollback partially improved; observable recovery unresolved. Preserve Q02 score and Q03 afterward. Two main-question average remains 7.5/10; all three attempts including this retry: 22/3 = 7.33/10, acceptance estimates 205/3 = 68.3%. These are descriptive coaching aggregates, not hiring probabilities.

Staging tested image tag v2.4.0, recorded digest sha256:AAA (illustrative), from Git commit A. Before production approval, someone repushed v2.4.0 and it now resolves to sha256:BBB. The tested AAA image still exists. Production uses Argo CD plus Argo Rollouts. A teammate says the semantic version and approval are sufficient, and suggests rebuilding A if needed. The previous stable image is sha256:OLD (illustrative).

The retry assessed artifact choice, approval evidence, controller roles and recovery. Digests are illustrative placeholders. No additional main-numbered question consumed.

## Pending Q06 — Reusable workflows and matrix failure handling

Your team copied the same GitHub Actions test workflow into twelve service repositories, and fixes now differ across copies. Tests run for Python 3.11 and 3.12 in a matrix. The 3.12 test fails, but deployment still proceeds because that failure is tolerated. A teammate suggests removing 3.12 from the matrix and maintaining the copies manually. How would you share the workflow while preserving service-specific inputs, make required matrix failures block deployment, and roll out shared workflow changes safely?

## Revision

- [ ] Demonstrate immutable artifact promotion and tested/running identity comparison — Q02.
- [ ] Separate Argo CD and Argo Rollouts duties; prove rollback recovery — Q02.

Q02.1: duties correctly distinguished after coaching; independent retest and recovery proof remain pending.

- [ ] Prove deployment gating with failed/skipped and approval-path tests — Q01.
- [ ] Precisely distinguish dependencies from conditional expressions — Q01.

 Preserve scores/reassessments; use compact answers, focused YAML only when useful, essential commands and actual operation checks. Create canonical question/answer files after attempts only. Commit locally; push only when asked.

## Attempt record

2026-10-25 Q01: 8.5/10, 80% subjective estimate; [evidence](questions/Q01-deployment-check-gates.md). Q02 pending; no future answer revealed.

2026-10-25 Q02: 6.5/10, 60% subjective estimate; [evidence](questions/Q02-tested-artifact-promotion.md). Q03 pending.

## Q03 — 2026-10-26

**8.5/10, 80% subjective estimate.** [Evidence](questions/Q03-oidc-deployment-identity.md). Strong least-privilege identity diagnosis; exact trust boundary and positive/negative verification remain revision items. Main-question average: 23.5/3 = 7.83/10; acceptance 220/3 = 73.3%. Including coached Q02.1: 30.5/4 = 7.625/10 and 285/4 = 71.25%. Earlier aggregates above describe their historical checkpoints. Coverage 5/10; Q04 pending. Python Q06 already evaluated on 2026-10-26.

- [ ] Retest trust-versus-permission boundaries and actual subject/audience matching — Q03.
- [ ] Verify runtime identity, required operation and denied contexts — Q03.

## Q04 — 2026-10-26

**8/10, 75% subjective estimate.** [Evidence](questions/Q04-untrusted-pr-runner-isolation.md). Sound safe design direction; clarify privileged execution mechanism, actual runner isolation and merged-only trigger. Main average 31.5/4 = 7.875/10; acceptance 295/4 = 73.75%. Including coached Q02.1: 38.5/5 = 7.7/10 and 360/5 = 72%. Earlier aggregates are historical checkpoints. Coverage 6/10; Q05 pending.

- [ ] Retest isolated execution boundaries and merged-only deployment triggers — Q04.

## Q05 — 2026-10-26

**8/10, 75% subjective estimate.** [Evidence](questions/Q05-deployment-concurrency.md). Correct concurrency group and active-migration protection. Remaining gaps: stale candidate checks, partially failed migration handling, and actual version/health evidence. Main average 39.5/5 = 7.9/10; acceptance 370/5 = 74%. Including coached Q02.1: 46.5/6 = 7.75/10 and 435/6 = 72.5%. Prior aggregates remain historical. Coverage 7/10; Q06 pending. Queue-feature detail is coaching, not a deduction.

- [ ] Retest release freshness, failed migration recovery and runtime version/health verification — Q05.
