# CI/CD Progress

**Active from 2026-10-25.** GitHub Actions primary, Jenkins secondary. Four-year DevOps/Platform baseline; scenario-based questions, one at a time. Daily Python requirement complete today (Q04/Q05). Kubernetes cycle remains complete; no unrelated pending question replaced.

| Metric | Status |
| --- | --- |
| Evaluated questions | 2 |
| Average score / acceptance estimate | 7.5/10 / 70% (subjective, not hiring probability) |
| Coverage | 4/10 |
| Readiness | Strong first answer; broader CI/CD readiness unassessed |
| Pending | Q02.1 — targeted artifact/release retry; Q03 preserved afterward |

## Coverage

- [x] ✅ Dependencies and conditional gates — Q01; event-trigger breadth remains unassessed.
- [ ] Build/test/security scanning and trustworthy results.
- [x] ✅ Artifact promotion — Q02; digest pinning/immutability and provenance need revision.
- [ ] Secrets, OIDC and least-privilege workflow permissions.
- [x] ✅ Environment approvals — Q01; deployment-access security depth remains unassessed.
- [x] ✅ Progressive rollout and rollback — Q02; Argo responsibilities, artifact identity and recovery gates need revision.
- [ ] Runners, isolation, supply-chain and untrusted PR security.
- [ ] Concurrency, cancellation, caches and reliable execution.
- [ ] Reusable workflows, matrices and maintenance.
- [ ] Jenkins fundamentals, credentials, agents and pipeline troubleshooting.

Check aspects only after substantive evaluation; coverage is not mastery. Integrate observability into relevant scenarios and link actual evidence. Start with broad high-value coverage; review after ten evaluated questions, adapt to demonstrated gaps. No automatic total question quota or readiness guarantee.

## Pending Q02.1 — Targeted retry (2026-10-25)

User requested an extra coached retry after Q02; preserve Q02 score and keep Q03 afterward. Evaluate demonstrated recovery separately, not as independent mastery or a new main-numbered question. No retry score until attempted.

Staging tested image tag v2.4.0, recorded digest sha256:AAA (illustrative), from Git commit A. Before production approval, someone repushed v2.4.0 and it now resolves to sha256:BBB. The tested AAA image still exists. Production uses Argo CD plus Argo Rollouts. A teammate says the semantic version and approval are sufficient, and suggests rebuilding A if needed. The previous stable image is sha256:OLD (illustrative).

Explain exactly which artifact production should run, what evidence/configuration would ensure that identity survives approval, which Argo component handles Git synchronization versus traffic promotion, and what you would do and verify if the new release increases errors. Treat digests as placeholders, not valid real hashes. No answer supplied before the attempt.

## Pending Q03 — OIDC deployment identity

A GitHub Actions production job used stored AWS access keys. You migrate it to OIDC, but assuming the deployment role fails with AccessDenied. The job references the production GitHub environment. A teammate suggests restoring long-lived administrator keys or allowing every GitHub repository to assume the role. How would you identify the failing trust/permission boundary, scope access to this repository and deployment context, and verify it safely?

## Revision

- [ ] Demonstrate immutable artifact promotion and tested/running identity comparison — Q02.
- [ ] Separate Argo CD and Argo Rollouts duties; prove rollback recovery — Q02.

- [ ] Prove deployment gating with failed/skipped and approval-path tests — Q01.
- [ ] Precisely distinguish dependencies from conditional expressions — Q01.

 Preserve scores/reassessments; use compact answers, focused YAML only when useful, essential commands and actual operation checks. Create canonical question/answer files after attempts only. Commit locally; push only when asked.

## Attempt record

2026-10-25 Q01: 8.5/10, 80% subjective estimate; [evidence](questions/Q01-deployment-check-gates.md). Q02 pending; no future answer revealed.

2026-10-25 Q02: 6.5/10, 60% subjective estimate; [evidence](questions/Q02-tested-artifact-promotion.md). Q03 pending.
