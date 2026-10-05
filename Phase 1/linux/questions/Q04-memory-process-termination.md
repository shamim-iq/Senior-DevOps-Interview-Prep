# Question 04 — Memory Pressure / Process Termination

## 🎯 Scenario

A systemd-managed API disappears under traffic spikes and restarts automatically. Free memory was low before failure and looks normal afterward. A teammate suggests dropping caches every minute. Establish the cause, mitigate safely and verify recovery.

## ✅ Interview-Ready Answer

> I would correlate the service's exit and restart time with kernel logs before declaring OOM. Low free memory alone is insufficient: I would inspect available memory, swap activity and the service's memory limit. Restarting frees the old process's memory, so current readings cannot disprove earlier exhaustion. If confirmed, I would reduce excess concurrency or roll back a memory regression, then right-size memory or distribute traffic based on the measured cause. I would verify stable memory, no further kills/restarts and normal API latency under comparable traffic. I would not schedule cache drops or tune swap blindly.

## 🔄 Flow

```text
Process disappeared → service exit evidence + kernel logs
                               ↓
            Host OOM / service limit / other termination?
                               ↓
              Target confirmed cause → verify under load
```

## 🔍 Essential Commands

Study examples only; replace service and time window with the actual incident values.

| Command | Why / evidence |
| --- | --- |
| `sudo systemctl status <service>` | Check service state and reported exit reason; current success may follow a restart. |
| `sudo journalctl -u <service> --since "30 minutes ago"` | Correlate termination and restart timestamps, signals and application errors. |
| `sudo journalctl -k --since "30 minutes ago"` | Look for OOM-killer messages and the killed process/cgroup at the incident time. SIGKILL alone does not prove OOM. |
| `free -h` | Focus on `available`, not merely `free`; inspect swap totals/usage. |
| `vmstat 1` | Observe repeated `si/so` swap activity and waits; current samples must be correlated with pre-failure monitoring. |
| `ps aux --sort=-%mem` | Identify current memory-heavy processes; the killed process's old usage is no longer present. |
| `sudo systemctl show <service> -p MemoryCurrent -p MemoryHigh -p MemoryMax` | Check service memory use and configured limits; a service limit can be reached while host RAM remains available. Parent limits may also apply. |

## 🛠️ Mitigation → Validation

- For confirmed host pressure: reduce nonessential workers/concurrency, distribute traffic to healthy instances where supported, or add RAM with an operational plan. Adding RAM is **vertical scaling**; adding instances is **horizontal scaling**.
- For a service memory limit: adjust only with sufficient host headroom and measured demand. Extra host RAM alone does not raise a fixed service limit.
- For a release regression/leak: consider safe rollback, bound application concurrency/cache and work with developers using historical memory trends and incident evidence.
- Swap may help selected workloads but can worsen latency; changing swappiness neither creates swap nor fixes a leak. Validate active swap, workload behavior and I/O impact before tuning.
- Validate through representative traffic spikes: no new OOM records or unexpected restarts, stable memory/headroom and acceptable API latency/errors. Persist the proven fix in configuration and alert before pressure becomes critical.

## 🧠 Key Points / Further Coaching

- Kernel page cache is different from an application's own cache. Linux reclaims reclaimable kernel caches as needed; it cannot automatically clear arbitrary application heap caches. Regular drop_caches can add I/O and CPU work.
- Low free RAM alone is normal on a caching system; available memory estimates usable headroom including reclaimable memory.
- If kernel OOM evidence is absent, investigate other causes such as application crashes, service timeouts, administrative kills or systemd-oomd if enabled. Do not label every restart OOM. Detailed oomd/cgroup event commands are optional follow-up, not required command volume.

## 📌 Takeaway

**Prove the termination cause, distinguish host pressure from service limits, and demonstrate recovery under the traffic that triggered it.**

## Attempt — 2026-10-05

Candidate rejected cache dropping, proposed service status/journal, htop, vmstat, free and memory-sorted ps. Suggested adding RAM (called horizontal scaling), conditional swappiness tuning and developer optimization. Did not explicitly establish OOM through kernel evidence, distinguish available memory/service limits or define recovery validation.

**Score: 7/10 — four-year baseline.** Subjective answer-specific acceptance estimate: 65%, not a hiring prediction.

Credit: sound investigation sequence, appropriate common tools, rejection of routine cache drops and conditional rather than automatic tuning. Deductions: 1 for incomplete termination proof; 0.75 for insufficient host/limit and swap safeguards; 0.75 for missing recovery verification; 0.5 combined for cache/free-memory/scaling terminology. No deduction for omitted advanced commands.

## References

- [Kernel cache reclamation and swappiness](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/vm.html)
- [systemd memory resource controls](https://man7.org/linux/man-pages/man5/systemd.resource-control.5.html)
