# Linux Interview Progress

**Active topic: Phase 1 / Linux.** Kubernetes is paused by request; its Q11 remains pending in its own progress file.

| Metric | Current status |
| --- | --- |
| Questions Attempted | 3 / 10 in the first cycle |
| Average Score | 6.17/10 — 18.5 / 3; historical scores unchanged |
| Average Acceptance Probability | 55% — subjective answer-specific estimates, not hiring probability |
| Topic Coverage | 5 / 15 aspects assessed (33.3%) |
| Current Strengths | Inode awareness, cautious deletion, least-privilege intent and path-permission investigation |
| Current Weaknesses | df/du and load-state interpretation, latency versus capacity, precise access scope and recovery validation |
| Readiness Trend | Useful diagnostic starting points; evidence-to-mitigation and validation need practice. Three scenarios do not establish overall readiness |

## Active Question

Q04 — Memory / unexpected process termination; awaiting an answer.

A Linux API managed by systemd disappears during traffic spikes and is restarted automatically. Monitoring just before failure shows little free memory, while memory appears normal after restart. A teammate suggests dropping caches every minute. How would you establish why the process was terminated, choose a safe mitigation and verify recovery? Include the essential commands and evidence you would look for.

## Coverage Checklist

`[x] ✅` means substantively attempted and evaluated, not mastered. Keep pending and explanation-only aspects unchecked; link completed aspects to evaluated questions.

- [x] ✅ Filesystem capacity, inodes and open/deleted files — Q01; df/du discrepancy and safe recovery need retesting.
- [ ] Processes, signals and safe service recovery.
- [x] ✅ CPU, load average and process/thread diagnosis — Q03; task-state interpretation needs retesting, thread-level depth remains.
- [ ] Memory, swap, OOM and resource limits.
- [x] ✅ Disk I/O latency and storage performance — Q03; latency versus capacity and metric interpretation need retesting.
- [x] ✅ systemd services, dependencies and journal investigation — Q02 startup/journal assessed; dependency-specific diagnosis remains for later sampling.
- [x] ✅ Permissions, ownership, ACLs and privilege boundaries — Q02 identity/path permissions assessed; ACL-specific diagnosis remains for later sampling.
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

| Question | Date | Score | Acceptance estimate | Record |
| --- | --- | --- | --- | --- |
| Q01 | 2026-10-04 | 4.5/10 | 35% | [Disk Full / df–du](questions/Q01-disk-full-df-du.md) |
| Q02 | 2026-10-04 | 7.5/10 | 70% | [systemd / Permissions](questions/Q02-systemd-permissions.md) |
| Q03 | 2026-10-05 | 6.5/10 | 60% | [High Load / Moderate CPU](questions/Q03-high-load-low-cpu.md) |

## Retest Queue

- Q03: interpret runnable/D-state evidence and I/O measurements; distinguish capacity from latency, choose a targeted mitigation and verify service recovery.

- Q01: distinguish blocks/inodes and open deleted files in a fresh scenario; demonstrate evidence-preserving mitigation and validation.
- Q02: independently scope file access and demonstrate restart/recovery validation. Evaluation uses the four-year baseline; advanced optional details are not required for full credit.
