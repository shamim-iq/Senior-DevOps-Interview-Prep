# Question 02 — systemd Startup / Permission Denied

## 🎯 Scenario

After deployment, an API fails under systemd with Permission denied opening its configured application file. Manual startup as root succeeds. A teammate proposes running the service permanently as root. Diagnose and recover with minimal permissions.

## ✅ Interview-Ready Answer

> I would keep the service unprivileged, check its journal for the exact failing path and operation, and inspect the unit's configured user and groups. I would check permissions along that path and grant only the necessary access through the intended application group or targeted ownership/permissions. After a controlled service restart, I would verify startup, the failed file operation and an API request. If ordinary permissions are correct, I would investigate service restrictions and security-policy denials rather than broaden access blindly.

## 🔄 Investigation Flow

```text
Journal: exact file + operation
             ↓
Unit identity → path permissions → narrowly scoped correction
             ↓
Controlled restart → clean journal + successful API/file operation
```

## 🔍 Essential Commands

Examples only, not executed. Replace placeholders with the actual service, service account and failing path.

| Command | Purpose |
| --- | --- |
| `sudo systemctl status <service>` | Check failure state and recent messages. |
| `sudo journalctl -u <service> -n 50 --no-pager` | Find the exact denied operation/path; it need not be a log file. |
| `sudo systemctl cat <service>` | Inspect unit and overrides for User, Group, ExecStart and restrictions; the operator running systemctl is not necessarily the service identity. |
| `id <api-user>` | Check account groups against the path's owning group. |
| `namei -l <failing-path>` | Show permissions/ownership of each component; assess these against the service identity. This does not check every ACL or security policy. |

Directories need search (`x`) permission along the path. Reading a config needs file read permission; writing an existing log needs file write permission; creating a file needs write and search on its parent. `ls -l` shows permissions, not log contents.

### 🛠️ Mitigate and Verify

If an existing, narrowly scoped application group already has the required access, this is one possible **state-changing** fix:

```sh
sudo usermod -aG <app-file-group> <api-user>
sudo systemctl restart <service>
sudo systemctl status <service>
sudo journalctl -u <service> --since "5 minutes ago" --no-pager
```

Inspect what else that group can access first. Group membership does not grant permissions the group lacks on the path. Correct only the affected ownership/mode/ACL when that is the actual regression; avoid broad privileged groups or recursive permission changes. Restarting lets the new process receive updated groups; coordinate disruption. Run daemon-reload before restart only if unit configuration changed.

Verify a real API request and the formerly failing file operation, then correct deployment file ownership/permissions so the next release preserves the fix.

## 🧠 Additional Coaching

- Running a command as the service user is useful, but starting a second API can have side effects. Prefer a safe access test; a manual run does not reproduce systemd's full environment, sandbox or explicitly configured groups.
- If access bits look correct, examine ACLs, SELinux/AppArmor denials and systemd path restrictions. Do not disable protections wholesale. These are conditional follow-ups, not mandatory command lists for this answer.

## Attempt — 2026-10-04

Candidate rejected permanent root access; proposed status/journal checks, reproducing as the API user, inspecting the log path using namei, and adding the account to a group with all permissions.

**Score: 7.5/10 — four-year experience baseline.** Subjective answer-specific acceptance estimate: 70%; not a hiring prediction.

Strong diagnosis direction and useful commands. Deductions: 1 point for insufficiently scoped group remediation; 1 point for missing restart/recovery verification; 0.5 for not explicitly confirming unit identity and the actual failing path. No deduction for omitted advanced policy commands. Original Q01 score remains unchanged.

## References

- [systemd execution identity, groups and restrictions](https://github.com/systemd/systemd/blob/main/man/systemd.exec.xml)
- [namei path inspection](https://www.man7.org/linux/man-pages/man1/namei.1.html)
