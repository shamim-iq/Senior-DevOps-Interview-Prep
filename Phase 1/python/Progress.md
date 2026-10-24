# Python Progress

**Active alongside other topics from 2026-10-24.** One coding attempt before other-topic questions per Asia/Calcutta calendar day. Once evaluated, continue the pending topic question. Writing code is required; running it and sharing output is encouraged. Incorrect attempts still count toward the habit, not mastery.

| Metric | Status |
| --- | --- |
| Evaluated exercises | 3 |
| Average score / acceptance estimate | First attempts: 8/10 / 73.3%; latest per exercise: 9.83/10 / 93.3% (includes coached Q02/Q03 revisions; not hiring probability) |
| Coverage | 6 / 10 aspects |
| Interview readiness | Foundation demonstrated; broader coding readiness not yet assessed |
| Pending exercise | None; Q03 evaluated, return to Kubernetes Q12 |
| Return to after warm-up | Kubernetes follow-up cycle complete; next topic awaits user choice |

## Daily ledger

| Date (Asia/Calcutta) | Exercise | Status | Code / execution evidence |
| --- | --- | --- | --- |
| 2026-10-24 | Q01 | Complete — evaluated 10/10 | [Q1.py](my_codes/Q1.py); five independent tests passed; [evaluation](questions/Q01-http-status-summary.md) |
| 2026-10-24 | Q02 | Complete — original 7.5/10; coached revision 10/10 | [Q2.py](my_codes/Q2.py); isolated tests; [evaluation](questions/Q02-log-server-errors.md) |

Q03 evaluated on 2026-10-24: 6.5/10, [code](my_codes/Q3.py), [evaluation](questions/Q03-unhealthy-services-json.md). Original: three valid-input tests failed; invalid JSON passed. Coached revision: 9.5/10, five evaluator test categories passed; user-authored checks still missing. Daily practice remains complete.

Use the actual attempt date when completed. Retain an unanswered exercise across days. A pending prompt or explanation does not complete the day. Keep execution status explicit: user-reported run, independently tested, or code review only.

## Coverage

- [x] ✅ Core syntax, loops and conditions — Q01.
- [x] ✅ Lists/dictionaries and basic aggregation — Q01; sets and nested structures remain for later practice.
- [x] ✅ Functions and input validation — Q03 function contract and malformed JSON handling; broader validation remains.
- [x] ✅ Files and log processing — Q02; whitespace fixed in coached revision; independent retention pending.
- [x] ✅ JSON parsing — Q03; nested navigation corrected after coaching; independent retention pending. YAML/configuration-specific work remains.
- [ ] HTTP APIs, timeouts and pagination.
- [ ] Subprocesses and exit codes.
- [x] ✅ Exception handling and file-failure propagation — Q02; structured logging and broader safe failure handling remain to assess.
- [ ] Tests and edge cases.
- [ ] Practical automation combining these skills.

Only mark assessed aspects with [x] ✅ and an evidence link after evaluation. Coverage is not mastery.

## Current position

Q01–Q03 evaluated; Q02 includes a preserved coached reassessment. User-requested extra Python exercise is complete. Kubernetes follow-up cycle is complete; do not ask another Python exercise today unless requested. Q03 correction is for the user to make; no source edits by evaluator.

## Revision

- [x] ✅ Fix outer-object/nested-list iteration in coached Q03 revision.
- [ ] Retest nested structures independently.

- [x] ✅ Correct function parameter/return contract in Q02 coached revision, 2026-10-24.
- [x] ✅ Function parameter/return contract demonstrated in fresh Q03; internal logic still needs correction.
- [x] ✅ Correct whitespace parsing in Q02 coached revision, 2026-10-24.
- [ ] Confirm whitespace parsing independently in a fresh exercise.
- [ ] Demonstrate user-authored tests; evaluator checks alone do not count.

No fixed question quota or readiness percentage is inferred from daily attendance.

## Breadth strategy

Start with fundamentals and file/log processing, then rotate JSON/YAML parsing, HTTP APIs (authentication, timeouts, pagination, retries/backoff), subprocess safety and exit codes, exceptions/logging, tests/mocking and edge cases. Combine these in practical health checks, inventory/reporting and safe automation (dry runs, idempotency, secrets handling). Include functions, modules, environment/CLI input, regex/datetime, sets/nested structures, basic complexity and bounded concurrency where useful. Revisit demonstrated weaknesses without repeating basics indefinitely. Separate demonstrated coverage from remaining subskills; no readiness claim from daily attendance. User-authored tests and independent problem solving must be assessed directly.
