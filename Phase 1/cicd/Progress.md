# CI/CD Progress

**Active from 2026-10-25.** GitHub Actions primary, Jenkins secondary. Four-year DevOps/Platform baseline; scenario-based questions, one at a time. Python Q04/Q05 completion was on 2026-10-25; check the daily ledger before a new question. Kubernetes cycle remains complete.

| Metric | Status |
| --- | --- |
| Evaluated questions | 3 |
| Average score / acceptance estimate | 7.83/10 / 73.3% (subjective, not hiring probability) |
| Coverage | 5/10 |
| Readiness | Controller roles improved in coached retry; artifact proof and recovery verification need independent retest |
| Pending | Q04 — Untrusted pull requests and runner isolation |
| Coached retry | Q02.1: 7/10, 65% subjective estimate; excluded from main-question average |

## Coverage

- [x] ✅ Dependencies and conditional gates — Q01; event-trigger breadth remains unassessed.
- [ ] Build/test/security scanning and trustworthy results.
- [x] ✅ Artifact promotion — Q02; digest pinning/immutability and provenance need revision.
- [x] ✅ Secrets, OIDC and least-privilege workflow permissions — Q03; exact trust matching and allow/deny verification need revision.
- [x] ✅ Environment approvals — Q01; deployment-access security depth remains unassessed.
- [x] ✅ Progressive rollout and rollback — Q02; Argo responsibilities, artifact identity and recovery gates need revision.
- [ ] Runners, isolation, supply-chain and untrusted PR security.
- [ ] Concurrency, cancellation, caches and reliable execution.
- [ ] Reusable workflows, matrices and maintenance.
- [ ] Jenkins fundamentals, credentials, agents and pipeline troubleshooting.

Check aspects only after substantive evaluation; coverage is not mastery. Integrate observability into relevant scenarios and link actual evidence. Start with broad high-value coverage; review after ten evaluated questions, adapt to demonstrated gaps. No automatic total question quota or readiness guarantee.

## Q02.1 — Targeted retry assessed (2026-10-26)

User requested an extra coached retry after Q02. [Evaluation](questions/Q02.1-artifact-promotion-retry.md): 7/10, 65% subjective estimate. CD/Rollouts roles resolved in this coached attempt; artifact identity and lasting rollback partially improved; observable recovery unresolved. Preserve Q02 score and Q03 afterward. Two main-question average remains 7.5/10; all three attempts including this retry: 22/3 = 7.33/10, acceptance estimates 205/3 = 68.3%. These are descriptive coaching aggregates, not hiring probabilities.

Staging tested image tag v2.4.0, recorded digest sha256:AAA (illustrative), from Git commit A. Before production approval, someone repushed v2.4.0 and it now resolves to sha256:BBB. The tested AAA image still exists. Production uses Argo CD plus Argo Rollouts. A teammate says the semantic version and approval are sufficient, and suggests rebuilding A if needed. The previous stable image is sha256:OLD (illustrative).

The retry assessed artifact choice, approval evidence, controller roles and recovery. Digests are illustrative placeholders. No additional main-numbered question consumed.

## Pending Q04 — Untrusted pull requests and runner isolation

A public repository accepts fork pull requests. To run integration tests, a teammate proposes using pull_request_target, checking out the contributor's code and running it on the same self-hosted runner used for production deployments. That runner has access to the internal network. How would you assess this design, run useful PR checks safely and keep production deployment access protected?

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
