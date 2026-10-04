# Question 01 — Disk Full but du Shows Less Usage

## 🎯 Scenario

A Linux API and worker fail to write files. `df -h` shows `/var` at 100%, but `du -xsh /var` accounts for much less usage. A teammate suggests deleting logs and rebooting. Investigate and recover safely while preserving evidence.

## ✅ Interview-Ready Answer

> I would confirm filesystem block and inode usage, then compare the same filesystem with a privileged du scan. The large df/du gap suggests deleted files still held open, which I would check with lsof. After recording the owning process and preserving essential evidence outside the full filesystem, I would use a supported log reopen or controlled service restart to release the file. I would verify reclaimed space, successful application writes and stable service health, then fix rotation/retention and alerting.

## 🔄 Diagram

```text
Writes fail -> check blocks AND inodes
                         |
            df usage much larger than du?
                         |
             Check deleted-but-open files
                 /                  \
               Found               Not found
                 |                    |
       Identify owner; preserve    Verify scan permissions,
       evidence; close safely      mount scope and hidden data
                 \                  /
           Verify space + application recovery
```

## 🔍 Troubleshooting / Reasoning Flow

### ① Establish what is exhausted

```sh
df -h /var
df -i /var
sudo du -xsh /var
sudo lsof +L1
```

| Command | Why / evidence |
| --- | --- |
| `df -h` | Check filesystem block usage and mount. 100% here is not the inode percentage. |
| `df -i` | Check inode usage/free inodes. Inode exhaustion can prevent file creation even when blocks are free. |
| `du -xsh` | Count reachable files on the same filesystem; sudo avoids permission-related undercounting. Inspect errors. |
| `lsof +L1` | Find open files with zero links; correlate device/path, process, PID and size with `/var`. Large open deleted files remain allocated but are absent from du's directory scan. |

Study examples only; none executed on a production server. lsof may need installation/privileges. Other discrepancies include files hidden beneath mounts and filesystem accounting; do not assume every difference is a deleted log.

### ② Recover with the smallest disruption

- Record affected filesystem, process/PID and relevant logs. Preserve required evidence to an approved separate filesystem or remote destination, not the full `/var`.
- For a deleted log held open, use the application's documented log-reopen/rotation action; a reload does not universally reopen logs. If needed, gracefully restart only the owning service after checking traffic/worker impact.
- Stop excessive growth or pause nonessential writers when appropriate. Remove only confirmed disposable files under retention rules; deleting a file still open may not free its blocks.
- If inodes are actually exhausted, identify the directory generating many small files and remove approved expired files. Reopening a deleted file and deleting thousands of small files address different causes.
- Avoid blanket reboot, blind truncation, force-killing processes or filesystem conversion as the first response. Emergency space expansion may help if supported, but still address the cause.

### ③ Validate and prevent

Repeat `df -h /var` and `df -i /var`; confirm the large deleted file is no longer held open. Verify application writes, API errors, worker progress and stable usage after recovery.

Fix log rotation with the required reopen behavior, retention and centralized collection. Alert on both blocks and inodes. `/var/apps` is not a universal log location: use service configuration; logs may be in `/var/log`, the journal or application-specific paths.

## 🧠 Key Points

- `df` counts filesystem allocations; `du` walks named files. Removing a filename does not release an open file's storage until its final reference is closed.
- On GNU/Linux use **`df -i`**, not `du -i`, for available inodes. `du --inodes` counts inode usage under directories, not filesystem free inodes.
- XFS dynamically allocates inodes; ext4 normally provisions inode tables when created (filesystem growth can add more). XFS still has capacity constraints. Selecting or migrating a filesystem is planned engineering, not a guaranteed incident fix.

## 📌 Senior-Level Takeaway

**Distinguish block exhaustion, inode exhaustion and open-file retention before cleaning up; preserve evidence and release only what is safe.**

## Attempt Record — 2026-10-04

Candidate response summary (paraphrased): Assumed `/var/apps` stores logs; identified inode exhaustion despite free storage; proposed assessing and deleting unneeded files, using `du -i` to check inodes, and preferring XFS for dynamic inode allocation over ext4. Did not explain the supplied df/du gap, identify open deleted files, or specify targeted recovery and validation.

Score: 4.5/10. Interview Acceptance Probability: 35% (subjective answer-specific estimate).

## References

- [GNU Coreutils: filesystem usage](https://www.gnu.org/software/coreutils/manual/coreutils.html#df-invocation)
- [Red Hat: deleted open files retain disk space](https://access.redhat.com/solutions/2316)
- [Filesystem allocation differences](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_file_systems/overview-of-available-file-systems_managing-file-systems)
