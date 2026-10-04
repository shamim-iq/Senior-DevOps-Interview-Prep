# Linux Interview Progress

**Active topic: Phase 1 / Linux.** Kubernetes is paused by request; its Q11 remains pending in its own progress file.

| Metric | Current status |
| --- | --- |
| Questions Attempted | 2 / 10 in the first cycle |
| Average Score | 6/10 — (4.5 + 7.5) / 2; historical Q01 unchanged |
| Average Acceptance Probability | 52.5% — subjective answer-specific estimates, not hiring probability |
| Topic Coverage | 3 / 15 aspects assessed (20%) |
| Current Strengths | Inode awareness, cautious deletion, least-privilege intent and path-permission investigation |
| Current Weaknesses | df/du interpretation, open-file lifecycle, precise access scope and recovery validation |
| Readiness Trend | Q02 demonstrates useful diagnosis; two different scenarios and a scoring calibration do not establish a readiness trend |

## Active Question

Q03 — CPU / load investigation; awaiting an answer.

An API on an 8-vCPU Linux server becomes slow. Load averages are 18, 16 and 12, but overall CPU utilization is only about 35%. A teammate recommends adding CPUs immediately. How would you identify the bottleneck, choose a safe mitigation and verify recovery? Include the essential commands and what you would look for.

## Coverage Checklist

`[x] ✅` means substantively attempted and evaluated, not mastered. Keep pending and explanation-only aspects unchecked; link completed aspects to evaluated questions.

- [x] ✅ Filesystem capacity, inodes and open/deleted files — Q01; df/du discrepancy and safe recovery need retesting.
- [ ] Processes, signals and safe service recovery.
- [ ] CPU, load average and process/thread diagnosis.
- [ ] Memory, swap, OOM and resource limits.
- [ ] Disk I/O latency and storage performance.
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

## Retest Queue

- Q01: distinguish blocks/inodes and open deleted files in a fresh scenario; demonstrate evidence-preserving mitigation and validation.
- Q02: independently scope file access and demonstrate restart/recovery validation. Evaluation uses the four-year baseline; advanced optional details are not required for full credit.
