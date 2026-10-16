# Terraform Interview Feedback

One attempt evaluated; average 6/10. Track: 20 questions, one at a time, using the four-year baseline in AGENTS.md.

Record each individual verdict, score, strengths, explained deductions and revision needs after the answer. Consolidate after Q10 and deliver the final evidence-based verdict after Q20. Preserve scores and history. See Progress.md for the assessment agreement and pending question.

## Q01 — Unexpected Database Replacement — 2026-10-17

[Question and corrected answer](questions/Q01-unexpected-database-replacement.md)

**6/10. Verdict:** Good production caution; diagnosis and lifecycle semantics need correction. Subjective answer-specific acceptance estimate: 55%, not hiring probability.

Credit: recognized data-loss risk, fresh plan review, validate and approval-gated CI. The expanded response is evaluated as one attempt. `ignore_changes` skips the requested tag update and does not block replacement from other causes.

Deductions: 2 lifecycle misconception/unsupported certainty; 1.5 missing root-cause inspection; 0.5 missing post-apply checks. No separate penalty for optional safeguards or command completeness. Retest the actual replacement diff, intended in-place update and recovery verification. Next: Q02 remote state locking; revisit lifecycle later within the 20 questions.
