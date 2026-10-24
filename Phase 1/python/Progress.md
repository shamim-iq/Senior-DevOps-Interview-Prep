# Python Progress

**Active alongside other topics from 2026-10-24.** One coding attempt before other-topic questions per Asia/Calcutta calendar day. Once evaluated, continue the pending topic question. Writing code is required; running it and sharing output is encouraged. Incorrect attempts still count toward the habit, not mastery.

| Metric | Status |
| --- | --- |
| Evaluated exercises | 2 |
| Average score / acceptance estimate | First attempts: 8.75/10 / 82.5%; latest per exercise: 10/10 / 95% (includes coached Q02 revision; not hiring probability) |
| Coverage | 4 / 10 aspects |
| Interview readiness | Foundation demonstrated; broader coding readiness not yet assessed |
| Pending exercise | Q03 — unhealthy services from JSON; extra requested on 2026-10-24 |
| Return to after warm-up | Kubernetes Q12 — HPA metrics and scheduling capacity |

## Daily ledger

| Date (Asia/Calcutta) | Exercise | Status | Code / execution evidence |
| --- | --- | --- | --- |
| 2026-10-24 | Q01 | Complete — evaluated 10/10 | [Q1.py](my_codes/Q1.py); five independent tests passed; [evaluation](questions/Q01-http-status-summary.md) |
| 2026-10-24 | Q02 | Complete — original 7.5/10; coached revision 10/10 | [Q2.py](my_codes/Q2.py); isolated tests; [evaluation](questions/Q02-log-server-errors.md) |

Q03 is pending as an extra exercise requested on 2026-10-24; no completed attempt recorded yet.

Use the actual attempt date when completed. Retain an unanswered exercise across days. A pending prompt or explanation does not complete the day. Keep execution status explicit: user-reported run, independently tested, or code review only.

## Coverage

- [x] ✅ Core syntax, loops and conditions — Q01.
- [x] ✅ Lists/dictionaries and basic aggregation — Q01; sets and nested structures remain for later practice.
- [ ] Functions and input validation.
- [x] ✅ Files and log processing — Q02; whitespace fixed in coached revision; independent retention pending.
- [ ] JSON/YAML and configuration handling.
- [ ] HTTP APIs, timeouts and pagination.
- [ ] Subprocesses and exit codes.
- [x] ✅ Exception handling and file-failure propagation — Q02; structured logging and broader safe failure handling remain to assess.
- [ ] Tests and edge cases.
- [ ] Practical automation combining these skills.

Only mark assessed aspects with [x] ✅ and an evidence link after evaluation. Coverage is not mastery.

## Current position

Q01 and Q02 evaluated; daily requirement already complete. User explicitly requested one more Python exercise on 2026-10-24. Q03 is now pending in [my_codes/Q3.py](my_codes/Q3.py). After its evaluation return to the preserved Kubernetes Q12. No new scores or coverage credit until an attempt is assessed.

## Pending Q03

Q03 — Find unhealthy services in JSON

Write find_unhealthy_services(json_text). The input is a JSON string containing
an object with a services list. Each entry is an object with a string name
and a string status. Assume this structure is valid when the JSON parses.
Return names whose status is not exactly "healthy", in input order.
An empty services list returns []. Invalid JSON must raise ValueError
(or a subclass), not silently return []. Use only the standard library.
Do not read files, make network calls, or change the input.

Example input:
{"services": [{"name": "api", "status": "healthy"}, {"name": "worker", "status": "degraded"}, {"name": "scheduler", "status": "down"}]}
Expected result: ["worker", "scheduler"]

Write your function here. Add checks for the example, all-healthy services,
an empty services list, and invalid JSON. Keep any demonstration under the
main guard so importing the module does not run it. No solution supplied.

## Revision

- [x] ✅ Correct function parameter/return contract in Q02 coached revision, 2026-10-24.
- [ ] Confirm function-contract understanding in a fresh exercise.
- [x] ✅ Correct whitespace parsing in Q02 coached revision, 2026-10-24.
- [ ] Confirm whitespace parsing independently in a fresh exercise.
- [ ] Demonstrate user-authored tests; evaluator checks alone do not count.

No fixed question quota or readiness percentage is inferred from daily attendance.

## Breadth strategy

Start with fundamentals and file/log processing, then rotate JSON/YAML parsing, HTTP APIs (authentication, timeouts, pagination, retries/backoff), subprocess safety and exit codes, exceptions/logging, tests/mocking and edge cases. Combine these in practical health checks, inventory/reporting and safe automation (dry runs, idempotency, secrets handling). Include functions, modules, environment/CLI input, regex/datetime, sets/nested structures, basic complexity and bounded concurrency where useful. Revisit demonstrated weaknesses without repeating basics indefinitely. Separate demonstrated coverage from remaining subskills; no readiness claim from daily attendance. User-authored tests and independent problem solving must be assessed directly.
