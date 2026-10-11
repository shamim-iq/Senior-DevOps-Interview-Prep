# Q10 — Rotation Leaves the Old Log Growing

## 🎯 Scenario

An API has daily log rotation, but the new file stays empty and the renamed old log keeps growing. A teammate proposes hourly truncation. Diagnose, preserve evidence, fix rotation and verify.

## ✅ Interview-Ready Answer

> The process likely still holds the old file open: renaming a log does not redirect its existing file descriptor. I would confirm the owner with lsof and inspect rotation settings and the new file's permissions. After preserving needed logs, I would use the application's documented log-reopen action and configure rotation to invoke it. A controlled restart is a fallback if reopening is unsupported. I would generate a safe request and confirm fresh entries in the new file, no continued writes to the old one, and healthy service behavior through the next rotation.

## 🔄 Flow

```text
Old log still growing → confirm open file → inspect rotation + permissions
                              ↓
Preserve evidence → supported reopen → verify new log + next rotation
```

## 🛠️ Essential Commands

Examples only, not executed. Replace PID and filenames with actual values.

| Command | Purpose |
| --- | --- |
| `ls -lh /var/log/myapi/` | Compare sizes and ownership. Useful, but does not identify which file the process has open. |
| `sudo lsof -p <pid>` | Find the worker's open log and confirm whether it is the renamed file; check other workers if needed. |
| `cat /etc/logrotate.d/myapi` | Inspect matching paths, retention, new-file owner/mode and the configured post-rotation action. |
| `sudo logrotate -d /etc/logrotate.conf` | Debug the effective configuration without rotating files or updating state. |
| `tail -n 20 /var/log/myapi/app.log` | After a safe request, confirm fresh expected entries in the new log. |

## 🔧 Fix → Verify

- Preserve required incident logs to approved storage with space available. Retain evidence, but do not let unrestricted growth fill the disk; use retention/compression after the application closes the old file.
- Use the application's documented reopen command/signal, or reload only if it actually reopens logs. There is no universal safe signal for every application. Configure that supported action after rotation (postrotate); no scripting exercise is required here.
- Check that the new file's owner/mode allow the application to write. If reopening is unsupported, plan a controlled restart with service-impact checks.
- Confirm lsof now shows the new file, a known request produces a new entry, the old log stops growing, and API health remains normal. Observe the next scheduled rotation or a controlled test outside risky production activity.
- Daily rotation controls timing, not a strict maximum file size. If growth is excessive, align size-based policy and scheduler frequency with actual volume.

💡 `copytruncate` is an alternative when reopening is unavailable, but writes between copying and truncation can be lost. It needs an explicit trade-off decision; it is not equivalent to blindly truncating all logs hourly.

## Attempt — 2026-10-11

Candidate rejected evidence-destroying truncation, correctly explained the old open file descriptor and the need to redirect logging to a new file. Supplied ls -lh only; did not demonstrate open-file confirmation, a supported reopen/configuration fix or successful-write/service verification.

**Score: 7/10 — four-year baseline.** Subjective answer-specific acceptance estimate: 70%, not hiring probability.

Credit: correct central mechanism, concise reasoning and evidence-preservation intent. Deductions: 1 for missing open-file/configuration confirmation, 1 for unspecified safe reopen/prevention mechanism, 1 for missing observable verification. No penalty for brevity or not listing advanced tools; ls alone cannot prove the fix.

## Reference

[logrotate: debug mode, postrotate, create and copytruncate](https://man7.org/linux/man-pages/man8/logrotate.8.html)
