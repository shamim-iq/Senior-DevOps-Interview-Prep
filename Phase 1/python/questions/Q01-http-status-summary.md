# Q01 — HTTP status summary

## Scenario

Write `summarize_status_codes(codes)` for valid integer HTTP codes 100–599. Return counts for success (200–299), client_error (400–499), server_error (500–599). Ignore other codes; always return all keys, including for empty input. No external packages.

## Evaluation — 2026-10-24

**10/10; answer-specific acceptance estimate 95%** (subjective coaching estimate, not overall hiring probability). First evaluated Python exercise. [User code](../my_codes/Q1.py), preserved in commit `7d00c23`; source SHA256 `42b13b4cf3b947eba03196c6af518f72d8ff0478eaa7cb6248e196f951472fc0`.

| Evidence in your code | Assessment |
| --- | --- |
| Lines 2–4 initialize all counters | Correct zero results even for empty input |
| Lines 6–12 use mutually exclusive ranges | Correct category boundaries; other codes ignored |
| Line 14 returns all three keys | Meets the exact output contract |
| Lines 16–19 demonstrate usage behind main guard | Function can be imported without running the example |

No mistakes found against the stated requirements. Clear O(n) time and O(1) auxiliary space. Type hints/docstring and saved automated tests are optional improvements, not deductions. Invalid-type handling was not required. One foundational task does not establish overall SRE coding readiness.

## Reference solution

Your function is already a suitable reference; no correction is needed. Snapshot of the evaluated function:

```python
def summarize_status_codes(codes):
    success = 0
    client_error = 0
    server_error = 0

    for code in codes:
        if 200 <= code < 300:
            success += 1
        elif 400 <= code < 500:
            client_error += 1
        elif 500 <= code < 600:
            server_error += 1

    return {"success": success, "client_error": client_error, "server_error": server_error}
```

## Verification

Independently executed the inspected function in memory without editing source or generating bytecode. All five cases passed; input lists remained unchanged.

| Input | Expected counts: success, client_error, server_error |
| --- | --- |
| `[200, 201, 404, 500, 200, 503, 301]` | 3, 1, 2 |
| `[]` | 0, 0, 0 |
| `[100, 199, 200, 299, 300, 399, 400, 499, 500, 599]` | 2, 2, 2 |
| `[100, 199, 300, 301, 399]` | 0, 0, 0 |
| `[503, 503, 503]` | 0, 0, 3 |

User-authored automated test coverage remains to be assessed; evaluator tests do not count as that skill. No flowchart needed for this short function.
