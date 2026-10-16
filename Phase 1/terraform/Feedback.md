# Terraform Interview Feedback

One question evaluated; original-attempt average 6/10; latest revised-answer average 8/10 (after feedback). Track: 20 questions, one at a time, using the four-year baseline in AGENTS.md.

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
