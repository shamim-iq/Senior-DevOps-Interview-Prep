# Q02 — Count server errors from logs

**Task:** `count_server_errors(path)` reads UTF-8 lines containing service + integer status. Return per-service 5xx counts; skip blank/malformed/non-5xx lines. Empty file → `{}`; missing file → `FileNotFoundError`. Stream lines; standard library only.

[Your code](../my_codes/Q2.py) — unchanged by evaluator.

| Attempt (2026-10-24) | Score | Acceptance estimate* | Saved version |
| --- | --- | --- | --- |
| Original | 7.5/10 | 70% | `7bbebc9` |
| Coached revision | 10/10 | 95% | `7fa249a` |

*Subjective answer-specific estimates, not hiring probabilities. Original score retained; revision is not an independent retest.*

**Mistakes → fixes**

- Fixed path + `print(services)` → accept `path` and return the dictionary (**−1.5 originally; fixed**).
- `split(" ")` → `split()` handles tabs/repeated spaces (**−1 originally; fixed**).
- Correct throughout: UTF-8 streaming, counting, invalid-number handling and missing-file exception. `strip()` before `split()` and the exists precheck are optional; no deduction.

**Tests:** Original passed example/empty/invalid-boundaries/missing-file; failed whitespace and callable contract. Revision passed all seven categories (including no-errors and Unicode), string/Path arguments and repeated calls. Source unchanged; tests used temporary files. Independent retention and user-authored tests remain to assess.

**Reference solution**

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

**Quick theory / library notes**

- **`split()` vs `split(" ")`?** The former groups whitespace; the latter splits literal spaces and can produce empty fields.
- **Why `with open(...)`?** Closes the file even if an error occurs; `open` raises naturally when the file is missing.
- **`Path`?** Standard-library `pathlib` represents filesystem paths; `open` accepts strings or Path objects.
- **`return` vs `print`?** Return supplies data to the caller; print only displays it.

**Cost:** O(characters read) time; O(distinct error services + longest line) extra memory.
