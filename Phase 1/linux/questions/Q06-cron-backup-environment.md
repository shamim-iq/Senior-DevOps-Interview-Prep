# Question 06 — Manual Backup Works / Cron Fails

## 🎯 Scenario

A backup script works manually but its nightly cron job produces no backup. The server is running at the scheduled time. A teammate suggests root's crontab. Diagnose, fix safely and verify scheduled backups.

## ✅ Interview-Ready Answer

> I would confirm the schedule, job owner and whether cron launched the command. Then I would inspect captured script errors and compare the manual and scheduled user, environment, working directory and interpreter. I would use absolute paths, explicit required configuration and only the backup account's necessary permissions. I would verify a real scheduled run, successful exit and a fresh usable backup, including a restore test in an isolated destination. Moving to root is not a substitute for diagnosis.

## 🔄 Flow

```text
Correct schedule + daemon running?
               ↓
Was the job launched? → inspect script stderr / exit status
               ↓
Compare identity + environment + paths + access
               ↓
Minimal fix → scheduled run → verify backup + test restore
```

## 🔍 Essential Commands

Illustrative only; no backup or production commands executed. Replace placeholders with actual values.

| Command | Why |
| --- | --- |
| `sudo crontab -u <backup-user> -l` | Check the correct user's schedule and command. Also inspect /etc/crontab or /etc/cron.d if the job lives there; system entries include a user field. |
| `sudo systemctl status cron` | Check the scheduler; some distributions call the service crond. Verify schedule/timezone as well as host uptime. |
| `sudo journalctl -u cron --since "24 hours ago"` | Check scheduler evidence where logged to the journal. Syslog/cron log location depends on configuration. A launch record is not proof of successful backup. |
| `namei -l /opt/backup/backup.py` | Inspect path access; also check source-read and destination-write access as the backup user. |

For a controlled test, use the cron account, intended interpreter, working directory and minimal environment. Example **executes a backup**, so first ensure a safe destination and no overlapping run:

```sh
sudo -u <backup-user> env -i HOME=<home> PATH=/usr/bin:/bin /bin/sh -c 'cd /opt/backup && /opt/backup/venv/bin/python /opt/backup/backup.py'
```

Supply actual required configuration securely. This approximates a minimal cron environment; inspect the actual job settings rather than assuming every installation uses these values. A plain sudo -u test does not reproduce all cron differences.

## 🛠️ Fix and Verify

- Use absolute interpreter/script/data paths and an explicit working directory. Cron does not normally load interactive shell setup or activate a virtual environment. Ensure required credentials/configuration are available securely.
- Grant only required access through a dedicated backup group, ownership or targeted ACL. A broad developers group may grant unrelated access. Individual ownership/ACL permissions are valid; groups are not universally mandatory.
- Example user-crontab command, **configuration change**; the protected log must already be writable by the backup account:

```cron
0 2 * * * cd /opt/backup && /opt/backup/venv/bin/python /opt/backup/backup.py >> /var/log/backup/job.log 2>&1
```

- Capture stdout/stderr, propagate failures with nonzero exit status and alert on failed or missing backups. Avoid secrets in logs. Cron may mail output if configured; syslog does not automatically contain script errors.
- Verify an actual scheduled execution, exit status, fresh backup timestamp/size and successful restore to an isolated destination. A created file alone does not establish recoverability.

## 🧠 Key Points

- `python script.py` needs Python execution permission and script read/path access; the script itself need not have its execute bit set. Direct execution has different requirements.
- Root can be justified for narrowly controlled privileged backups, but should not be a blind workaround. Protect privileged scripts against modification by less-trusted users.
- Users may have personal crontabs; not every account has one configured.

## Attempt — 2026-10-07

Interpreted the opening as rejecting moving the job to root (not literally removing it). Candidate identified a user-permission mismatch, listed crontabs, proposed running Python as the cron user, adding that account to dev, and reading syslog. No penalty for the opening wording slip. Missing: cron environment/path comparison, captured script output, schedule/daemon checks and backup validation.

**Score: 6/10 — four-year baseline.** Subjective answer-specific acceptance estimate: 55%, not hiring probability.

Credit: plausible identity hypothesis, useful crontab inspection and user-based reproduction, least-privilege intent. Deductions: 1.5 for incomplete cron-environment/scheduling investigation; 1 for broad group remediation without demonstrated access need; 1 for missing scheduled-run and backup verification; 0.5 combined for script-permission and logging assumptions. Advanced tools are not required.

## References

- [Cron environment and entry format](https://manpages.debian.org/testing/cron/crontab.5.en.html)
- [Cron output handling](https://manpages.ubuntu.com/manpages/stonking/man8/crond.8.html)
