# Q01 — HTTP status counts

**Task:** Return counts for 2xx, 4xx and 5xx integer codes; ignore others. Always include all three keys, even for empty input. Inputs are valid codes; no external packages.

**2026-10-24: 10/10 · Acceptance estimate 95%** (subjective, not hiring probability).
[Your code / reference solution](../my_codes/Q1.py) · evaluated version: `7d00c23`.

- ✅ Correct ranges, counters, return value and empty-input handling. No fixes needed.
- **Tests:** example, empty, boundaries, ignored and repeated codes passed; input unchanged. Evaluator tests do not establish user-authored testing skill.
- **Cost:** O(n) time, O(1) extra space. Type hints/docstrings are optional.

**Quick theory**

- **Why `elif`?** Each code belongs to at most one counted category.
- **Why initialize counters first?** Empty input still returns every key with zero.
- **Why a main guard?** Example code runs directly, but not when imported.
