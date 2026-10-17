# Terraform Interview Feedback

Ten questions evaluated; original-attempt average 6.60/10; latest per-question average 7.15/10 (includes Q01 and Q04 revisions after feedback). Current track: ten initial questions plus up to five focused follow-ups, one at a time, using the four-year baseline in AGENTS.md.

Record each individual verdict, score, strengths, explained deductions and revision needs after the answer. Consolidate after Q10 and deliver the final evidence-based verdict at the shortened cycle closure (no later than Q15). Preserve scores and history. See Progress.md for the assessment agreement and pending question.

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

## Q04 revised attempt — 2026-10-17

**8/10 — Core identity and migration concepts corrected; replacement behavior and migration verification need precision.** Answer-specific acceptance estimate: **75%**, subjective coaching, not hiring probability. Revision after reading the solution; preserve original 4.5/10. Not a new numbered question or independent retest.

**Response summary:** Identified count indices and trailing-resource risk; proposed stable for_each keys/each.key, keeping resource configuration unchanged and using a moved block to preserve resources. Incorrectly said changing an EC2 instance name can itself recreate it.

**Credit:** Correct cause, stable-key solution and explicit migration awareness. Saying “move” instead of `moved` is a minor terminology slip with no separate penalty.

**Deductions:** 1 for claiming a Name-tag-only change causes recreation; 1 for incomplete migration verification: map every original index to the correct key/instance ID, confirm an address-only plan and separately remove the unwanted service. Previously stated CI approval habits are credited, not penalized again.

**Precision:** The EC2 Name tag normally updates in place. Replacement depends on the changed argument or explicit replacement behavior. A `moved` block maps an old Terraform address to its new address; it is not a general deletion guard and cannot prevent replacement required by other argument changes. Stable keys help only while keys remain unchanged. Retest independently later.

Example mapping (repeat for every existing instance using its verified original identity):

```hcl
moved {
  from = aws_instance.service[2]
  to   = aws_instance.service["notifications"]
}
```

[AWS: tags on existing EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags_Console.html) · [HashiCorp: address migration](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring).

## Q05 — Emergency Security-Group Drift — 2026-10-17

[Canonical answer](questions/Q05-emergency-security-group-drift.md). **7.5/10; subjective acceptance estimate 70%, not hiring probability.**

Credit: correct state/code distinction, required configuration update, plan review and controlled emergency exception. Deductions: 1.5 exact rule/incident and minimum-access decision missing; 0.5 unnecessary refresh-only prerequisite; 0.5 post-change access tests missing. No additional penalty for admin terminology or repeating command names. Next Q06 covers dependency reasoning; retest minimum-access decisions later.

## Q06 — Dependencies and Creation Order — 2026-10-17

[Canonical answer](questions/Q06-dependencies-creation-order.md). **6/10; subjective acceptance estimate 55%, not hiring probability.**

Credit: selective ordering, dependency list syntax, independent parallelism and rejection of routine targeting. Deductions: 2 missing implicit-reference/hidden-dependency distinction; 1 overbroad EC2 network prerequisites; 1 missing actual-error investigation and fresh-deployment verification. No code-volume penalty. Retest these gaps; Q07 covers module input validation.

## Q07 — Module Input Validation — 2026-10-17

[Canonical answer](questions/Q07-module-input-validation.md). **6.5/10; subjective acceptance estimate 60%, not hiring probability.**

Credit: parameterization, environment segregation, OIDC, Python policy checking and approval. Deductions: 2 missing module contract (required inputs, types, value validation, safe defaults); 0.75 validate described as syntax-only; 0.5 guaranteed correctness from separation; 0.25 unstructured plan-log parsing. No separate HCL-omission penalty. Retest the contract with invalid inputs; Q08 covers provider aliases, an untested subtopic despite broad coverage checks.

## Q08 — Provider Aliases and Module Regions — 2026-10-17

[Canonical answer](questions/Q08-provider-alias-module-region.md). **6.5/10; subjective acceptance estimate 60%, not hiring probability.**

Credit: regional configurations, aliases, plan review and CI gates. Deductions: 1.5 missing module provider mapping/inheritance; 1 concrete effective account/region verification; 1 existing-resource protection/migration. No code omission or repeated-gates penalty. Q09 independently retests Q02's untracked-resource recovery gap.

## Q09 — Import an Existing S3 Bucket — 2026-10-17

[Canonical answer](questions/Q09-import-existing-s3-bucket.md). **6/10; subjective answer-specific acceptance estimate 55%, not hiring probability.**

Credit: correct missing-state diagnosis, import over deletion, preserving application data, follow-up plan and controlled CI. Q02 preservation reasoning improved in this independent retest. Deductions: 1.5 replacing the resource block; 1.5 refresh-only cannot perform the import; 1 combined unsupported no-drift assumption and missing exact-object verification. No duplicate syntax penalty. Retest import execution and mapping evidence; Q10 covers provider locks/reproducibility, followed by the interim consolidation.

## Q10 — Provider Locks and Reproducible CI — 2026-10-17

[Canonical answer](questions/Q10-provider-lock-reproducible-ci.md). **8.5/10; subjective answer-specific acceptance estimate 80%, not hiring probability.**

Credit: correct range, ignored lock-file diagnosis, rejection of routine upgrades, branch/release-note review, lower-environment tests and approved promotion. Final “log file” interpreted as lock file; no wording penalty. Deductions: 1 actual local/CI version and resource-plan comparison; 0.5 explicit production re-plan after the fix. No deduction for optional advanced details or repeated approval steps. Q03 provider-lock reasoning improved.

## First-ten review — 2026-10-17

**10/20 assessed. Original attempts: 66/100 = 6.60/10. Latest per-question: 71.5/100 = 7.15/10**, including Q01/Q04 revisions after feedback. Original scores remain intact. Q09 independently improves Q02's preservation decision but not import execution; Q10 demonstrates stronger provider-version reasoning.

**Verdict:** Sound production-safety instincts and useful Terraform knowledge, with uneven execution precision. Stronger in CI approvals, environment organization, state/configuration distinction and controlled upgrades. Not yet consistently independent across the tested troubleshooting scenarios; no overall hiring probability follows from these results.

**Priorities:** Implicit/hidden dependencies (Q06), required inputs/custom validation (Q07), module provider mapping and destination proof (Q08), import versus refresh-only (Q09), and independent stable-address migration (Q04). Q01 lifecycle diagnosis and Q02 stale-lock proof/concurrency still need evidence-based retests.

**Remaining breadth:** Data sources/unknown values, locals/outputs/module interfaces and practical tests/policy controls. Continue to Q20 by interleaving these with the listed retests, combining related aspects without extending the agreed count. Judge concise answers by correct decisions and essential evidence, not command volume. All 12 broad coverage boxes mean attempted, not mastered; retain unresolved revision items.

## Assessment scope revision — 2026-10-17

At the user's request, the original Q20 target is superseded by at most five follow-ups (Q11–Q15), with earlier closure if priority weaknesses are independently resolved. Historical first-ten plans and scores above are retained as history, not current authorization for ten more questions. See Progress.md for the focused mapping and closure criteria. No new attempt or score was recorded for this planning change; unresolved or untested aspects will remain explicit in the final verdict.
