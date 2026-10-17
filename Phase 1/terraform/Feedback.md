# Terraform Interview Feedback

Four questions evaluated; original-attempt average 6.25/10; latest per-question average 6.75/10 (includes Q01 revision after feedback). Track: 20 questions, one at a time, using the four-year baseline in AGENTS.md.

Record each individual verdict, score, strengths, explained deductions and revision needs after the answer. Consolidate after Q10 and deliver the final evidence-based verdict after Q20. Preserve scores and history. See Progress.md for the assessment agreement and pending question.

## Q01 — Unexpected Database Replacement — 2026-10-17

[Question and corrected answer](questions/Q01-unexpected-database-replacement.md)

**6/10. Verdict:** Good production caution; diagnosis and lifecycle semantics need correction. Subjective answer-specific acceptance estimate: 55%, not hiring probability.

Credit: recognized data-loss risk, fresh plan review, validate and approval-gated CI. The expanded response is evaluated as one attempt. `ignore_changes` skips the requested tag update and does not block replacement from other causes.

Deductions: 2 lifecycle misconception/unsupported certainty; 1.5 missing root-cause inspection; 0.5 missing post-apply checks. No separate penalty for optional safeguards or command completeness. Retest the actual replacement diff, intended in-place update and recovery verification. Next: Q02 remote state locking; revisit lifecycle later within the 20 questions.

## Q01 revised attempt — 2026-10-17

**8/10 — Sound production approach with limited operational gaps.** Answer-specific acceptance estimate: **75%**, subjective coaching only, not hiring probability. Requested reassessment after feedback; original 6/10 remains unchanged. This is a revision of Q01, not a new numbered question or independent retest.

**Revised response summary:** Inspect the CI plan/logs for intended versus unintended changes; recognize that another attribute may trigger replacement; correct Terraform configuration; add `prevent_destroy` as extra protection; review a fresh plan and approve apply through CI.

**Credit:** Corrected the central lifecycle misconception and now investigates before fixing. Sensible use of an additional safeguard and approval-gated execution. No penalty for omitting an exhaustive command list.

**Remaining deductions:** 1 point for keeping the diagnosis generic rather than identifying the exact replacement attribute/address and tracing its input; 0.5 for not explicitly ensuring apply uses the reviewed saved plan; 0.5 for omitting verification of database identity/health and the actual tag after apply.

**Clarification:** `prevent_destroy = true` rejects a destructive plan; it does not convert replacement into an in-place update. It requires the rule to remain in configuration and does not protect against deletion outside Terraform. Independently retest later to confirm retention.

## Q02 — State Lock and Interrupted Apply — 2026-10-17

[Canonical answer](questions/Q02-state-lock-interrupted-pipeline.md). **7/10; subjective answer-specific acceptance 65%, not hiring probability.**

Credit: waits for active owner, rejects lock bypass, understands partial apply and reconciliation, knows S3 locking and refresh-only. Deductions: 1 stale-lock/no-writer proof missing; 1 deletion-first recovery without import; 0.5 CI concurrency prevention missing; 0.5 admin-only and complete-CloudTrail claims. User qualified deletion as safe; no indiscriminate-deletion penalty. Retest stale-lock evidence, import and concurrency. Next Q03 rotates to modules/environment management; no new question answered yet.

## Q03 — Modules and Environment Isolation — 2026-10-17

[Canonical answer](questions/Q03-modules-environment-isolation.md). **7.5/10; subjective acceptance estimate 70%, not hiring probability.**

Credit: directory roots, shared modules/inputs, protected state, OIDC/Secrets Manager, progressive testing and production approvals. Deductions: 1 module pinning/promotion missing; 0.75 explicit backend/role isolation missing; 0.5 provider constraints/lock controls; 0.25 CLI/file secret-injection caveats. No penalty for optional tooling. Retest these gaps; Q04 rotates to resource identity and safe refactoring.

## Q04 — Count and Stable Resource Identity — 2026-10-17

[Canonical answer](questions/Q04-count-stable-resource-identity.md). **4.5/10; subjective acceptance estimate 35%, not hiring probability.**

Credit: count/list-length understanding, dependency awareness, plan review and production caution. Main gap: numeric index shifting, not necessarily downstream dependencies. Deductions: 2.5 wrong central diagnosis; 2 combined stable-key/address-migration omission; 1 lifecycle limits and compulsory-protection claim. No terminology or repeated-command penalty. Retest with instance-ID mapping later; Q05 rotates to drift and desired-state decisions.
