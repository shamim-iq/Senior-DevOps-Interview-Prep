# CI/CD Progress

**Active from 2026-10-25.** GitHub Actions primary, Jenkins secondary. Four-year DevOps/Platform baseline; scenario-based questions, one at a time. Daily Python requirement complete today (Q04/Q05). Kubernetes cycle remains complete; no unrelated pending question replaced.

| Metric | Status |
| --- | --- |
| Evaluated questions | 1 |
| Average score / acceptance estimate | 8.5/10 / 80% (subjective, not hiring probability) |
| Coverage | 2/10 |
| Readiness | Strong first answer; broader CI/CD readiness unassessed |
| Pending | Q02 — promote the tested artifact |

## Coverage

- [x] ✅ Dependencies and conditional gates — Q01; event-trigger breadth remains unassessed.
- [ ] Build/test/security scanning and trustworthy results.
- [ ] Artifact integrity, image tags/digests and promotion.
- [ ] Secrets, OIDC and least-privilege workflow permissions.
- [x] ✅ Environment approvals — Q01; deployment-access security depth remains unassessed.
- [ ] Deployment strategies, rollback and recovery checks.
- [ ] Runners, isolation, supply-chain and untrusted PR security.
- [ ] Concurrency, cancellation, caches and reliable execution.
- [ ] Reusable workflows, matrices and maintenance.
- [ ] Jenkins fundamentals, credentials, agents and pipeline troubleshooting.

Check aspects only after substantive evaluation; coverage is not mastery. Integrate observability into relevant scenarios and link actual evidence. Start with broad high-value coverage; review after ten evaluated questions, adapt to demonstrated gaps. No automatic total question quota or readiness guarantee.

## Pending Q02 — Tested artifact differs from production

GitHub Actions builds an image from commit A, pushes it as latest and tests it successfully in staging. Before production approval, commit B overwrites latest. Production then deploys latest and behaves differently, although every check for A passed. A teammate suggests rebuilding A during the production job. How would you prove what was tested versus deployed, promote the exact approved artifact and make rollback reliable?

## Revision

- [ ] Prove deployment gating with failed/skipped and approval-path tests — Q01.
- [ ] Precisely distinguish dependencies from conditional expressions — Q01.

 Preserve scores/reassessments; use compact answers, focused YAML only when useful, essential commands and actual operation checks. Create canonical question/answer files after attempts only. Commit locally; push only when asked.

## Attempt record

2026-10-25 Q01: 8.5/10, 80% subjective estimate; [evidence](questions/Q01-deployment-check-gates.md). Q02 pending; no future answer revealed.
