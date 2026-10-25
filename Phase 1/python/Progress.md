# Python Progress

**Active alongside other topics from 2026-10-24.** One coding attempt before other-topic questions per Asia/Calcutta calendar day. Once evaluated, continue the pending topic question. Writing code is required; running it and sharing output is encouraged. Incorrect attempts still count toward the habit, not mastery.

| Metric | Status |
| --- | --- |
| Evaluated exercises | 5 |
| Average score / acceptance estimate | First attempts: 7.4/10 / 67%; latest per exercise: 8.9/10 / 82% (includes coached Q02/Q03/Q05 revisions; not hiring probability) |
| Coverage | 7 / 10 aspects |
| Interview readiness | Foundation demonstrated; broader coding readiness not yet assessed |
| Pending exercise | Q05 revision pending — original 5/10, latest coached revision 7/10; resolve before CI/CD |
| Return to after warm-up | CI/CD — GitHub Actions primary, Jenkins secondary; after Q05 is resolved |

## Daily ledger

| Date (Asia/Calcutta) | Exercise | Status | Code / execution evidence |
| --- | --- | --- | --- |
| 2026-10-24 | Q01 | Complete — evaluated 10/10 | [Q1.py](my_codes/Q1.py); five independent tests passed; [evaluation](questions/Q01-http-status-summary.md) |
| 2026-10-24 | Q02 | Complete — original 7.5/10; coached revision 10/10 | [Q2.py](my_codes/Q2.py); isolated tests; [evaluation](questions/Q02-log-server-errors.md) |

Q03 evaluated on 2026-10-24: 6.5/10, [code](my_codes/Q3.py), [evaluation](questions/Q03-unhealthy-services-json.md). Original: three valid-input tests failed; invalid JSON passed. Coached revision: 9.5/10, five evaluator test categories passed; user-authored checks still missing. Daily practice remains complete.

**2026-10-25 — Q04 complete:** [code](my_codes/Q4.py), [evaluation](questions/Q04-safe-subprocess.md), 8/10. Independently tested; daily requirement complete despite remaining corrections.

Use the actual attempt date when completed. Retain an unanswered exercise across days. A pending prompt or explanation does not complete the day. Keep execution status explicit: user-reported run, independently tested, or code review only.

## Coverage

- [x] ✅ Core syntax, loops and conditions — Q01.
- [x] ✅ Lists/dictionaries and basic aggregation — Q01; sets and nested structures remain for later practice.
- [x] ✅ Functions and input validation — Q03 function contract and malformed JSON handling; broader validation remains.
- [x] ✅ Files and log processing — Q02; whitespace fixed in coached revision; independent retention pending.
- [x] ✅ JSON parsing — Q03; nested navigation corrected after coaching; independent retention pending. YAML/configuration-specific work remains.
- [ ] HTTP APIs, timeouts and pagination.
- [x] ✅ Subprocesses and exit codes — Q04; narrow exception handling and exact failure contract need revision.
- [x] ✅ Exception handling and file-failure propagation — Q02; structured logging and broader safe failure handling remain to assess.
- [ ] Tests and edge cases.
- [ ] Practical automation combining these skills.

Only mark assessed aspects with [x] ✅ and an evidence link after evaluation. Coverage is not mastery.

## Current position

Q05 assessed on 2026-10-25: 5/10, [code](my_codes/Q5.py), [evaluation](questions/Q05-deployment-gate.md). Success/empty inputs raised AttributeError; invalid JSON passed. User to correct dictionary access, duplicate/completeness handling and Boolean return paths. CI/CD (GitHub Actions primary, Jenkins secondary) follows resolution, as requested. Daily practice already complete; this revision is not a new exercise.

## Revision

- [ ] Correct dictionary access, uniqueness checks and complete Boolean return paths — Q05.

- [ ] Catch specific exceptions and preserve exact failure output — Q04.

- [x] ✅ Fix outer-object/nested-list iteration in coached Q03 revision.
- [ ] Retest nested structures independently.

- [x] ✅ Correct function parameter/return contract in Q02 coached revision, 2026-10-24.
- [x] ✅ Function parameter/return contract demonstrated in fresh Q03; nested iteration corrected in coached revision.
- [x] ✅ Correct whitespace parsing in Q02 coached revision, 2026-10-24.
- [ ] Confirm whitespace parsing independently in a fresh exercise.
- [ ] Demonstrate user-authored tests; evaluator checks alone do not count.

No fixed question quota or readiness percentage is inferred from daily attendance.

## Breadth strategy

Start with fundamentals and file/log processing, then rotate JSON/YAML parsing, HTTP APIs (authentication, timeouts, pagination, retries/backoff), subprocess safety and exit codes, exceptions/logging, tests/mocking and edge cases. Combine these in practical health checks, inventory/reporting and safe automation (dry runs, idempotency, secrets handling). Include functions, modules, environment/CLI input, regex/datetime, sets/nested structures, basic complexity and bounded concurrency where useful. Revisit demonstrated weaknesses without repeating basics indefinitely. Separate demonstrated coverage from remaining subskills; no readiness claim from daily attendance. User-authored tests and independent problem solving must be assessed directly.

Q05 revision 2026-10-25: dictionary access corrected; all-success still returns False due to checking for duplicates immediately after appending. Latest 6/10, 45% subjective estimate; original preserved. CI/CD transition remains pending.

Q05 coached revision 2 (2026-10-25): 7/10, 55% subjective estimate. Failure/duplicate checks improved; final completeness return missing, so success and missing inputs return None. Prior 5/6 scores retained. CI/CD awaits resolution.
