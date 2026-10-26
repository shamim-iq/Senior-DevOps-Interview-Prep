# Q06 - Failed deployment summary

Task: accept a list of service/status dictionaries; count exact `failed` statuses by service, omit zero-failure services, return {} for empty input, preserve input. Add checks for mixed statuses, repeated failures and empty input.

User code: [Q6.py](../my_codes/Q6.py). Original attempt preserved in the evaluation commit; user file not edited.

## Attempt - 2026-10-26

**6.5/10; 55% subjective answer-specific acceptance estimate, not hiring probability.** Correct loop, exact status filter, dictionary accumulation and final return. Main issue: `res = json.loads(records)` (line 12) parses a string although the contract supplies a list. Independently tested: all five list cases raise TypeError. Diagnostic JSON-string tests: mixed/repeated, empty, no failures and case-sensitive status pass; empty service name fails because `if service` skips it. No user-authored checks present. No input-mutating operations found.

Deductions: 2.5 input-contract failure; 1 missing requested checks. Empty-name filtering is noted without an extra deduction because the intended service naming convention was not explicit. JSON exception handling is unnecessary for this list-input task; adding a TypeError catch would hide rather than fix the mismatch. Source executed in memory after safety inspection; no source changes or generated artifacts.

Original evidence:

```python
try:
    res = json.loads(records)
except json.JSONDecodeError:
    return {}
# inside the loop:
if service:
    result[service] = result.get(service, 0) + 1
```

## Minimal reference

```python
def failed_deployments(records):
    result = {}
    for record in records:
        if record["status"] == "failed":
            service = record["service"]
            result[service] = result.get(service, 0) + 1
    return result
```

`json.loads` converts JSON text into Python objects. This input already contains Python objects. `dict.get(key, 0)` provides a starting count when the service is not present yet.

Revision: user fixes their file and adds checks. Queue a similar aggregation question later for independent retention, as requested; no immediate duplicate exercise. Today's substantive attempt completes the daily habit regardless of score. CI/CD Q03 remains next.
