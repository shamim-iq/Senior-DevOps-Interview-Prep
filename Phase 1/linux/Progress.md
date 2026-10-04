# Linux Interview Progress

**Active topic: Phase 1 / Linux.** Kubernetes is paused by request; its Q11 remains pending in its own progress file.

| Metric | Current status |
| --- | --- |
| Questions Attempted | 0 / 10 in the first cycle |
| Average Score | N/A |
| Average Acceptance Probability | N/A |
| Topic Coverage | 0 / 15 aspects assessed |
| Current Strengths | Not yet assessed |
| Current Weaknesses | Not yet assessed |
| Readiness Trend | Insufficient evidence |

## Active Question

Q01 — Disk-full production incident; awaiting an answer.

A production Linux server hosts an API and a background worker. The API starts returning errors and the worker cannot write files. `df -h` shows the `/var` filesystem at 100%, but `du -xsh /var` accounts for much less space than the filesystem reports as used. A teammate suggests deleting old logs and rebooting the server. How would you investigate the discrepancy and restore service safely while preserving useful diagnostic evidence?

## Coverage Checklist

`[x] ✅` means substantively attempted and evaluated, not mastered. Keep pending and explanation-only aspects unchecked; link completed aspects to evaluated questions.

- [ ] Filesystem capacity, inodes and open/deleted files — Q01 pending.
- [ ] Processes, signals and safe service recovery.
- [ ] CPU, load average and process/thread diagnosis.
- [ ] Memory, swap, OOM and resource limits.
- [ ] Disk I/O latency and storage performance.
- [ ] systemd services, dependencies and journal investigation.
- [ ] Permissions, ownership, ACLs and privilege boundaries.
- [ ] Users, groups, sudo and SSH access troubleshooting.
- [ ] DNS, routing, sockets and connection diagnosis.
- [ ] Firewalls and network access controls.
- [ ] Mounts, filesystem recovery and persistent configuration.
- [ ] Shell scripting, pipelines, exit status and safe automation.
- [ ] Scheduled jobs, cron/systemd timers and execution environments.
- [ ] Log management, rotation and evidence preservation.
- [ ] Host hardening, patching and operational recovery validation.

## Practice Strategy

- Use senior DevOps / Platform / SRE production scenarios, one question at a time, with no hints or answer before the attempt.
- Start with 10 questions; combine related aspects and extend based on uncovered areas and demonstrated weaknesses.
- Prioritize breadth; no more than two consecutive questions centered on one aspect unless requested. Retest weaknesses later with fresh scenarios.
- Apply the compact answer format in root AGENTS.md: essential commands with brief purpose, useful diagrams, evidence-based decisions, safe mitigation and validation.
- After evaluation, create questions/QNN-<topic>.md, append feedback and update metrics/checkmarks. Never create answer files in advance or count pending questions as attempts.
- Keep Linux scores separate from Kubernetes. General communication habits can guide coaching but do not infer Linux competence from Kubernetes results.
- Follow the repository sync workflow. Commit progress locally; push only when explicitly requested.

## Revision and Readiness

- [ ] Complete the first 10 evaluated questions and consolidated review.
- [ ] Assess all planned Linux aspects.
- [ ] Retest recorded weaknesses independently.
- [ ] Demonstrate safe diagnosis, recovery and validation across varied scenarios.

## Evaluation History

No attempts recorded.
