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
