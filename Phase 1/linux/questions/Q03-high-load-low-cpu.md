# Question 03 — High Load / Moderate CPU

## 🎯 Scenario

An API on an 8-vCPU Linux host is slow. Load averages are 18, 16, 12; overall CPU utilization is 35%. A teammate suggests adding CPUs. Diagnose, mitigate safely and verify recovery.

## ✅ Interview-Ready Answer

> High load alone does not prove CPU saturation. Linux load includes runnable tasks and tasks in uninterruptible sleep, often waiting for I/O. I would sample vmstat, check per-core activity and process states, and use extended iostat output to confirm storage latency/queues. I would identify the responsible workload or failing storage before reducing nonessential I/O, correcting a regression or addressing storage limits. I would verify API latency/errors and current wait/queue metrics recover; load averages will settle gradually. A slow database can explain API latency, but ordinary socket waits do not automatically explain high Linux load.

## 🔄 Flow

```text
High load + slow API
         ↓
Sample runnable tasks / blocked tasks / per-core activity
         ↓
CPU pressure? → confirm busy cores and workload constraints
I/O pressure? → confirm device latency/queues and affected tasks
Neither?     → examine application/dependency latency and timing
         ↓
Targeted mitigation → verify API and bottleneck metrics
```

## 🔍 Essential Commands

Study examples only; not executed on a server.

| Command | Why / evidence |
| --- | --- |
| `vmstat 1` | Compare `r` runnable tasks, `b` blocked tasks, `wa` CPU I/O-wait and `si/so` swap activity over several samples. The first CPU/I/O report summarizes since boot. `wa` is not disk-capacity usage or proof of one failing device. |
| `top` | Press `1` for individual CPUs; check process state and consumption. An overall average can hide a busy core. |
| `ps -eo pid,stat,comm,wchan:32` | Identify `D` state tasks and their wait locations; CPU-sorted output alone can miss blocked processes. |
| `iostat -xz 1` | Check device `await`/read-write latency, queue size (`aqu-sz`) and activity against baseline. Ignore the first since-boot report. `%util` alone does not establish saturation on parallel storage. |

### 🛠️ Mitigation and Verification

- Confirm the culprit before acting. For a competing backup/batch job, coordinate pausing or reducing its concurrency. For storage faults or IOPS/throughput limits, repair the path or adjust proven constraints. Roll back a correlated application regression where safe.
- If capacity errors are present, check `df -h <path>` and `df -i <path>`; clean only approved disposable data and preserve evidence. These checks answer a different question from I/O latency. Full blocks/inodes often cause write failures rather than proving sustained blocked-task load.
- If database calls are slow, inspect request/query timings and dependency health. `ping <hostname>` only tests ICMP, not database-port access or query performance; an ICMP failure can also reflect filtering. Test the application's real dependency path safely.
- Verify API p95 latency/error rate, throughput and relevant queue/I/O measurements return to baseline under comparable traffic. Current indicators may recover before the 1/5/15-minute load averages.

## 🧠 Key Corrections

- Linux load counts runnable and uninterruptible tasks; ordinary interruptible socket sleep does not count. Network filesystems can involve uninterruptible waits, so distinguish them from routine database socket waits.
- `iostat` reports I/O performance, not free filesystem space. A filesystem can have ample free space and still serve I/O slowly.
- XFS is not a universal incident fix or automatically preferable because it is popular. Filesystem selection is planned work; revisit the inode-capacity explanation in Q01 only when evidence supports it.

## 📌 Takeaway

**Separate host load, storage performance, capacity and application latency; choose a fix from evidence and prove recovery.**

## Attempt — 2026-10-05

Candidate correctly rejected CPU-only reasoning; proposed vmstat r/b/wa, iostat, ps CPU/memory sorting, uptime and htop. Considered inode exhaustion, cautious cleanup, XFS and database latency with ping. Did not distinguish ordinary socket sleep from load-counted states, mislabeled iostat as a capacity check, or provide explicit recovery criteria.

**Score: 6.5/10, four-year baseline.** Subjective answer-specific acceptance estimate: 60%, not hiring probability.

Deductions: 1 point for attributing high load to ordinary dependency waits without task-state evidence; 1 for mixing storage latency with capacity/inodes and filesystem selection; 1 for insufficiently specific evidence-driven mitigation and missing validation; 0.5 for treating ping as a database-health check. Correct vmstat reasoning and careful deletion receive credit; no deduction for missing advanced tools.

## References

- [Linux load definition](https://man7.org/linux/man-pages/man1/uptime.1.html)
- [vmstat fields and sampling](https://man7.org/linux/man-pages/man8/vmstat.8.html)
- [iostat performance metrics](https://www.man7.org/linux/man-pages/man1/iostat.1.html)
