# Python Feedback

## Q01 — 2026-10-24

**10/10; 95% subjective answer-specific acceptance estimate.** [Evaluation](questions/Q01-http-status-summary.md) · [unchanged user code](my_codes/Q1.py).

Correct ranges, readable loop/counters, complete output and empty-input behavior. Five independent cases passed. No demonstrated defects; optional docstring/type hints do not affect score. File I/O, failures, APIs and other advanced skills remain unassessed. No overall readiness claim from one exercise.

Next: user-requested extra Q02 today; return to Kubernetes Q12 after its evaluation. Daily habit already completed by Q01.

## Q02 — 2026-10-24

**7.5/10; 70% subjective acceptance estimate.** [Evaluation and separate reference solution](questions/Q02-log-server-errors.md) · [unchanged code](my_codes/Q2.py). Correct streaming UTF-8 file handling, counting and malformed-input exception handling. Missing callable/return contract (1.5 deduction); literal-space splitting skips valid whitespace records (1.0). Four runtime cases passed, whitespace case failed, required-function check failed. Revise independently; no source correction performed. First-two average 8.75/10, descriptive only; practical breadth still unassessed. Return to Kubernetes Q12 now.

## Q02 coached revision — 2026-10-24

Reassessed **10/10; 95% subjective estimate**, original 7.5/10 retained. [Evidence](questions/Q02-log-server-errors.md#reassessment--2026-10-24-after-feedback). Function interface and whitespace handling both corrected; all seven test categories passed. No source edits by evaluator. Both flaws resolved in this revision; independent retention remains to be tested. First-attempt average remains 8.75/10; latest-per-exercise average 10/10 includes coaching and is not overall readiness.

## Q03 — 2026-10-24

**6.5/10; 55% subjective estimate.** [Evaluation](questions/Q03-unhealthy-services-json.md). Correct function/JSON parsing/error handling, but outer-dictionary iteration crashes all valid cases (−3); requested edge-case checks absent (−0.5). Q02 function contract improved in a fresh task. Nested JSON/list access and self-testing need revision. Source preserved; return to Kubernetes Q12.

## Q03 coached revision — 2026-10-24

**9.5/10; 90% subjective estimate**, original 6.5 preserved. [Details](questions/Q03-unhealthy-services-json.md). Corrected nested-list iteration; five evaluator test categories pass. Missing requested user checks retain a 0.5 deduction. Independent nested-structure retention remains pending. Code unchanged by evaluator.

## Q04 — 2026-10-25

**8/10; 75% subjective estimate.** [Evaluation](questions/Q04-safe-subprocess.md). Correct subprocess capture, timeout and exit handling. Broad exception catch swallows unrelated failures (−1), missing-file output differs (−0.5), requested checks absent (−0.5). Three runtime outcomes passed; missing-output and exception-propagation checks failed. Tests-writing gap persists. Source unchanged. Daily practice complete; next topic awaits user choice.

## Q05 — 2026-10-25

**5/10; 40% subjective estimate.** [Details](questions/Q05-deployment-gate.md). Dict attribute access blocks valid inputs; duplicate/order handling and list-length completeness reasoning are incorrect; some paths return None. Invalid JSON passes. Requested tests missing. Q03 dictionary navigation remains an independent-retest weakness. Preserve source; resolve Q05 before CI/CD as requested.
