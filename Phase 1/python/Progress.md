# Python Progress

**Active alongside other topics from 2026-10-24.** One coding attempt before other-topic questions per Asia/Calcutta calendar day. Once evaluated, continue the pending topic question. Writing code is required; running it and sharing output is encouraged. Incorrect attempts still count toward the habit, not mastery.

| Metric | Status |
| --- | --- |
| Evaluated exercises | 1 |
| Average score / acceptance estimate | 10/10 / 95% (one task; subjective, not hiring probability) |
| Coverage | 2 / 10 aspects |
| Interview readiness | Foundation demonstrated; broader coding readiness not yet assessed |
| Pending exercise | Q02 — count server errors from a file; user-requested extra today |
| Return to after warm-up | Kubernetes Q12 — HPA metrics and scheduling capacity |

## Daily ledger

| Date (Asia/Calcutta) | Exercise | Status | Code / execution evidence |
| --- | --- | --- | --- |
| 2026-10-24 | Q01 | Complete — evaluated 10/10 | [Q1.py](my_codes/Q1.py); five independent tests passed; [evaluation](questions/Q01-http-status-summary.md) |
| 2026-10-24 | Q02 | Pending — optional extra explicitly requested | [Q2.py](my_codes/Q2.py); prompt only |

Use the actual attempt date when completed. Retain an unanswered exercise across days. A pending prompt or explanation does not complete the day. Keep execution status explicit: user-reported run, independently tested, or code review only.

## Coverage

- [x] ✅ Core syntax, loops and conditions — Q01.
- [x] ✅ Lists/dictionaries and basic aggregation — Q01; sets and nested structures remain for later practice.
- [ ] Functions and input validation.
- [ ] Files and log processing.
- [ ] JSON/YAML and configuration handling.
- [ ] HTTP APIs, timeouts and pagination.
- [ ] Subprocesses and exit codes.
- [ ] Exceptions, logging and safe failure handling.
- [ ] Tests and edge cases.
- [ ] Practical automation combining these skills.

Only mark assessed aspects with [x] ✅ and an evidence link after evaluation. Coverage is not mastery.

## Pending Q02 — Count server errors from a file

Q02 — Count server errors from a log file

Write count_server_errors(path). Read a UTF-8 text file whose nonblank lines
contain two whitespace-separated fields: SERVICE STATUS_CODE.
Return a dictionary counting 500–599 responses per service. Include only
services with at least one such response. Ignore blank lines, malformed lines
(wrong field count, non-integer code or code outside 100–599), and non-5xx codes.
An empty file returns {}. A missing file must raise FileNotFoundError rather
than returning an empty result. Use standard library only and process the file
line by line without loading the entire file at once.

Example contents:
api 200
api 500
worker 503
api 502
bad-line
worker unknown

Expected: {"api": 2, "worker": 1}
Share or save your code here, plus any test output. No solution supplied.

User requested a second exercise before returning to other topics. Evaluate [my_codes/Q2.py](my_codes/Q2.py) unchanged, then resume Kubernetes Q12; do not automatically add Q03 today.

## Revision

No demonstrated weaknesses yet. Build the revision queue from evaluated code; rotate fundamentals, practical tasks and spaced retests. No fixed interview-question quota or readiness percentage is inferred from daily attendance.

## Breadth strategy

Start with fundamentals and file/log processing, then rotate JSON/YAML parsing, HTTP APIs (authentication, timeouts, pagination, retries/backoff), subprocess safety and exit codes, exceptions/logging, tests/mocking and edge cases. Combine these in practical health checks, inventory/reporting and safe automation (dry runs, idempotency, secrets handling). Include functions, modules, environment/CLI input, regex/datetime, sets/nested structures, basic complexity and bounded concurrency where useful. Revisit demonstrated weaknesses without repeating basics indefinitely. Separate demonstrated coverage from remaining subskills; no readiness claim from daily attendance. User-authored tests and independent problem solving must be assessed directly.
