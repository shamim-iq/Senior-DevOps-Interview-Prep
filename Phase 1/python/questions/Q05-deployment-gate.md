# Q05 — Deployment gate

**Task:** Parse jobs JSON. Return True only if build/test/scan each appear once with exact success status. Ignore other names; missing/duplicate/failed/empty → False. Invalid JSON raises ValueError/subclass. Add requested checks.

**2026-10-25: 5/10 · Acceptance estimate 40%** (subjective).
[Unchanged user code](../my_codes/Q5.py) · attempt `d4b745c`.

- ✅ Parsing/error handler, required-name filtering and success comparison show relevant understanding.
- **−2:** Parsed objects are dictionaries: `report.jobs` / `job.name` / `job.status` must use key access. Success and empty tests both raised AttributeError; invalid JSON passed. Count this as one root cause.
- **−2:** Duplicate branch comes after the success branch, so successful duplicates bypass it. List length cannot prove all three unique required jobs exist. By inspection, after key-access correction, build/build/test successes would wrongly pass; failed build followed by successful build/test/scan could also pass.
- **−0.5:** More than three appended successes fall through and return None, not False.
- **−0.5:** Only happy-path example provided; requested edge checks absent.

**Reference solution**

```python
import json

def can_deploy(report_json):
    required = {"build", "test", "scan"}
    seen = set()
    for job in json.loads(report_json)["jobs"]:
        name = job["name"]
        if name not in required:
            continue
        if name in seen or job["status"] != "success":
            return False
        seen.add(name)
    return seen == required
```

**Theory:** JSON objects become dictionaries; bracket notation accesses keys. A set tracks distinct names; duplicate detection must happen before accepting a repeated job. JSONDecodeError already subclasses ValueError. All normal paths must return a Boolean. O(input length + jobs) time; required/seen sets are bounded to three names, plus parsed input memory.

**Recovery:** Q03 nested-key access is not yet retained independently. Fix source yourself, then test success, failure-before-success duplicate, successful duplicate, missing/empty, unrelated failures and invalid JSON. No real deployment executed. CI/CD begins after Q05 is resolved, per user request.

## Coached revision — 2026-10-25

**6/10; acceptance estimate 45%** (subjective). Original 5/10 preserved; revision commit `dca5bdd`.

- ✅ Dictionary key access corrected; valid inputs no longer crash. Empty input and malformed JSON behave correctly.
- **Remaining logic gap (−3.5):** First success is appended, then the next independent if immediately sees that same name and returns False. All valid-schema inputs therefore return False, including all-success. Reject cases passing do not demonstrate correct duplicate logic. The former >3/None issue is no longer reachable, so its original deduction does not carry forward.
- **Checks (−0.5):** Still only one printed example, not the requested edge-case checks.
- Tests: all-success and unrelated-failure inputs incorrectly False; missing/empty/duplicate/failed inputs False; invalid JSON raises ValueError. Source unchanged.

**Trace:** first build/success → append build → build now in valid_jobs → return False. Validate duplicate/non-success required jobs before appending; ignore unrelated jobs, then verify all required names were collected. Merely switching the second if to elif would still fail to reject a failed occurrence followed by a successful duplicate. Retest both acceptance and rejection paths. CI/CD waits for resolution as requested.

## Coached revision 2 — 2026-10-25

**7/10; acceptance estimate 55%** (subjective). Earlier scores 5 and 6 retained; source commit `cf0bf97`.

- Improved: ignores unrelated jobs, rejects failed required jobs immediately, checks duplicates before appending.
- **−2.5:** No final completeness check/return. All-success, unrelated-extra and missing-job tests return None. Empty, duplicate, failed and invalid-JSON cases pass.
- **−0.5:** Requested user-authored edge checks still absent.
- Add a final return after the loop to confirm exactly the three required unique names. With current successful-duplicate rejection and specified two-field records, `return len(valid_jobs) == 3` completes the basic contract; name-based tracking is clearer and remains correct if extra metadata differs. Source unchanged; still awaiting correction before CI/CD.

## Coached revision 3 — 2026-10-25

**9.5/10; acceptance estimate 90%** (subjective). Earlier 5/6/7 scores retained; source `79d7c1e`.

- ✅ Final Boolean return fixes completion. Independently tested 4,681 ordered combinations of 0–4 two-field jobs (required/unrelated names and success/failed statuses); all matched the specification. Invalid JSON raised ValueError. Source unchanged.
- **−0.5 remains:** requested user-authored edge-case checks absent; example print only. Evaluator checks do not replace these.
- Whole-dictionary comparison works for the illustrated two-field schema. Tracking names is clearer and robust if reports later include varying metadata; extra metadata was not imposed as a new scoring requirement.
- Core exercise resolved after coaching; independent retention not yet demonstrated. CI/CD is next, GitHub Actions primary and Jenkins secondary. No more Python question today unless requested.
