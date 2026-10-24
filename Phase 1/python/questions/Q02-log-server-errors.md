# Q02 — Count server errors from logs

## Scenario

Implement `count_server_errors(path)` reading a UTF-8 log line by line. Valid lines have two whitespace-separated fields: service and integer HTTP code (100–599). Count only 500–599 per service; omit zero-count services. Ignore malformed/blank/non-5xx lines. Return a dictionary, including `{}` for an empty file. Missing files must raise FileNotFoundError. Standard library only.

## Evaluation — 2026-10-24

**7.5/10; answer-specific acceptance estimate 70%** (subjective, not a hiring probability). [Your unchanged code](../my_codes/Q2.py), original attempt preserved in commit `7bbebc9`; SHA256 `9efcd30ea3d1f7d9ade6cdd150d45185f63cb81ee6ccfde054a05a2ef0ec421c`.

**Correct:** UTF-8 context-managed file reading, streaming iteration, dictionary counting, 5xx boundaries, ignoring noninteger/malformed input and explicitly raising FileNotFoundError. Invalid numeric codes are also ignored because none pass the 5xx condition; no extra validation branch is needed for this output contract.

| Your code | Finding and correction |
| --- | --- |
| `file_path = Path("var/logs/server.log")` and `print(services)` | Script is tied to a path instead of accepting `path` in the requested function and returning the dictionary. Deduction 1.5 for the combined interface gap. |
| `line.strip().split(" ")` | Tabs remain unsplit and repeated spaces create empty fields, so valid records are skipped. Use `line.split()` for whitespace-separated fields. Deduction 1.0. |
| `if file_path.exists()` then `open(...)` | Correct missing-file outcome; precheck is optional and can race with file removal. Let open raise naturally. No deduction. |

The path without a leading slash is relative; that is not independently penalized because the requested function should accept its caller's path. No type hints, classes or extra libraries required.

## Verification

Executed the inspected source unchanged using temporary log files and an isolated working directory; no production log access or source edits. No bytecode artifacts created.

| Test | Actual outcome |
| --- | --- |
| Given example | PASS: `{'api': 2, 'worker': 1}` |
| Empty file | PASS: `{}` |
| Blank/malformed, invalid numeric codes and 499/500/599/600 boundaries | PASS |
| Missing file | PASS: FileNotFoundError |
| `api\t500`, `api    502`, `worker 503` | FAIL: only `{'worker': 1}` instead of `{'api': 2, 'worker': 1}` |
| Required callable/return contract | FAIL: no `count_server_errors(path)` function |

## Reference solution — separate from your file

```python
def count_server_errors(path):
    services = {}
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split()
            if len(parts) != 2:
                continue
            service, raw_code = parts
            try:
                code = int(raw_code)
            except ValueError:
                continue
            if 500 <= code <= 599:
                services[service] = services.get(service, 0) + 1
    return services

```

`split()` handles whitespace; `open` naturally raises for missing files; the local dictionary is returned. Time O(number of characters read); auxiliary memory O(distinct error-producing services + longest line). Streaming avoids loading the whole log.

## Follow-up

You can revise Q2.py yourself using these suggestions. Preserve this first score when reassessing. File handling, exception boundaries and dictionary aggregation demonstrated; reusable function contracts and whitespace parsing need retesting. Evaluator tests do not prove user-authored testing skills. Daily Python practice is complete; resume Kubernetes Q12 as requested, with no extra Python question today unless requested.

## Reassessment — 2026-10-24, after feedback

**10/10; subjective answer-specific acceptance estimate 95%.** Original score **7.5/10 (70%)** is preserved. This is a coached revision, not a new exercise or independent retest.

Revised [Q2.py](../my_codes/Q2.py) preserved in commit `7fa249a`; SHA256 `0a2a873f906152bc1f25190fb59295d994c90ed293a3b77f118ea80829fe699a`.

- Function now accepts `path` and returns its dictionary: interface gap resolved in this revision.
- `line.strip().split()` handles tabs and repeated spaces: parsing gap resolved in this revision. `strip()` is redundant but harmless; no deduction.
- Independently tested example, empty, whitespace, boundary/invalid, no-error and Unicode fixtures with both string and Path arguments; all passed. Repeated calls did not share counts. Missing path raised FileNotFoundError from the function as required.
- The main guard catches and prints the exception only for the demonstration; the function itself still raises correctly. The exists precheck remains optional, not an error here.
- User source unchanged during evaluation; temporary fixtures only. No additional fix required. Confirm retained understanding through a later fresh exercise. Return to Kubernetes Q12.
