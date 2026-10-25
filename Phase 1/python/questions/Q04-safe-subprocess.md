# Q04 — Safe diagnostic command

**Task:** Run an argument list without shell=True; return success/returncode/stdout/stderr with stripped text. Preserve nonzero exit output; timeout → None/empty stdout/"timeout"; missing executable → None/empty stdout/"command not found". Other exceptions must propagate. Add four main-guard checks.

**2026-10-25: 8/10 · Acceptance estimate 75%** (subjective, not hiring probability).
[Unchanged user code](../my_codes/Q4.py) · original commit `efd6654`.

- ✅ Argument-list execution (shell=False by default), captured text, actual return code, output trimming and timeout handling.
- **−1:** `except Exception` swallows unrelated failures such as PermissionError and mislabels them. Catch FileNotFoundError only; other failures should propagate.
- **−0.5:** Missing executable must return exactly `"command not found"`; your output includes OS error text.
- **−0.5:** Only a success call is supplied, with no print/assert; requested nonzero/timeout/missing checks are absent.
- **Tests:** success, nonzero and timeout passed. Missing-executable exact output failed; injected PermissionError was swallowed. Evaluator tests used harmless local commands/mock and left source unchanged.

**Focused correction** — replace only the broad exception handler yourself:

```python
except FileNotFoundError:
    return {
        "success": False,
        "returncode": None,
        "stdout": "",
        "stderr": "command not found"
    }
```

**Quick theory**

- `capture_output=True`: collect stdout/stderr instead of displaying them.
- `text=True`: return strings rather than bytes.
- Nonzero exit is a result here; `check=True` would instead raise CalledProcessError.
- Specific exceptions preserve useful failure distinctions. TimeoutExpired handles timeout; FileNotFoundError handles missing executable.

Add visible checks/assertions for all four requested outcomes. No need to change the working success/nonzero/timeout paths. Broader subprocess automation still needs practice; daily coding attempt is complete.
