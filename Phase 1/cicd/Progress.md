# CI/CD Progress

**Active from 2026-10-25.** GitHub Actions primary, Jenkins secondary. Four-year DevOps/Platform baseline; scenario-based questions, one at a time. Daily Python requirement complete today (Q04/Q05). Kubernetes cycle remains complete; no unrelated pending question replaced.

| Metric | Status |
| --- | --- |
| Evaluated questions | 0 |
| Average score / acceptance estimate | N/A / N/A |
| Coverage | 0/10 |
| Readiness | Not assessed |
| Pending | Q01 — production deployment bypasses checks |

## Coverage

- [ ] Triggers, job dependencies and conditional gates.
- [ ] Build/test/security scanning and trustworthy results.
- [ ] Artifact integrity, image tags/digests and promotion.
- [ ] Secrets, OIDC and least-privilege workflow permissions.
- [ ] Environment protections, approvals and deployment access.
- [ ] Deployment strategies, rollback and recovery checks.
- [ ] Runners, isolation, supply-chain and untrusted PR security.
- [ ] Concurrency, cancellation, caches and reliable execution.
- [ ] Reusable workflows, matrices and maintenance.
- [ ] Jenkins fundamentals, credentials, agents and pipeline troubleshooting.

Check aspects only after substantive evaluation; coverage is not mastery. Integrate observability into relevant scenarios and link actual evidence. Start with broad high-value coverage; review after ten evaluated questions, adapt to demonstrated gaps. No automatic total question quota or readiness guarantee.

## Pending Q01

A GitHub Actions workflow runs on pushes to main. It has separate build, test, scan and deploy jobs. The deploy job depends only on build. In one run, build succeeds, tests fail and scan is still running when deploy starts updating production. A teammate suggests adding a manual approval as the only fix.

How would you diagnose why deployment started, change the workflow so all required checks must succeed before production deployment, and verify that failed or skipped checks cannot bypass the gate? Explain where approval belongs. A small YAML excerpt is optional; no full workflow required.

## Revision

No evaluated weaknesses yet. Preserve scores/reassessments; use compact answers, focused YAML only when useful, essential commands and actual operation checks. Create canonical question/answer files after attempts only. Commit locally; push only when asked.
