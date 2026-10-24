# Q03 — Unhealthy services from JSON

**Task:** Parse a JSON object containing a `services` list; return non-healthy service names in order. Empty list → `[]`; malformed JSON → ValueError/subclass. Assume valid schema after parsing. Include example, healthy, empty and invalid-input checks.

**2026-10-24: 6.5/10 · Acceptance estimate 55%** (subjective, not hiring probability).
[Unchanged user code](../my_codes/Q3.py) · attempt commit `10523fe`.

- ✅ Correct function/return, `json.loads`, status filter, main guard and invalid-JSON handling.
- **Main bug (−3):** `for i in services` iterates the outer dictionary's keys. `i` becomes the string `"services"`; `i["status"]` raises TypeError. Iterate `services["services"]` instead. One root cause, not three separate deductions.
- **Checks (−0.5):** Only example supplied; requested healthy/empty/invalid checks absent. No requirement for a test framework.
- **Observed:** example, healthy and empty inputs all raised TypeError; invalid JSON correctly raised ValueError. Source unchanged. Q02 function-contract gap improved; nested-structure interpretation needs practice.

**Reference solution**

```python
import json

def find_unhealthy_services(json_text):
    data = json.loads(json_text)
    return [item["name"] for item in data["services"]
            if item["status"] != "healthy"]
```

**Quick theory**

- `json.loads(text)` parses a JSON string; `json.load(file)` reads from a file-like object, not an arbitrary Python object.
- JSON object → Python dictionary; JSON array → Python list.
- Dictionary iteration yields keys; access `data["services"]` to get the nested list.
- JSONDecodeError already inherits ValueError, so your conversion is valid but optional.

O(input length + service count) time; parsed input and result use proportional memory. No schema-validation requirement beyond the stated assumptions. Add the requested checks yourself; evaluator tests do not count as your tests.

## Coached revision — 2026-10-24

**9.5/10 · Acceptance estimate 90%** (subjective). Original **6.5/10, 55%** retained; revision saved in `de6f94c`.

- ✅ `for service in services["services"]` fixes nested-list iteration. Example, healthy, empty, order/exact-match and invalid JSON tests now pass; source unchanged.
- Remaining **−0.5**: requested healthy/empty/invalid checks are still absent from your submission. Evaluator tests do not replace user-authored checks.
- Comment clarification only: `json.load()` reads a file-like object; no additional deduction.
- Bug resolved after coaching; independently retest nested structures later. Kubernetes Q12 remains next.
