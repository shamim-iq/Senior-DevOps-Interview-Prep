# Linux Interview Progress

**Active topic: Phase 1 / Linux.** Kubernetes is paused by request; its Q11 remains pending in its own progress file.

| Metric | Current status |
| --- | --- |
| Questions Attempted | 1 / 10 in the first cycle |
| Average Score | 4.5/10 |
| Average Acceptance Probability | 35% — subjective answer-specific estimate |
| Topic Coverage | 1 / 15 aspects assessed (6.7%) |
| Current Strengths | Inode-exhaustion awareness; cautious file deletion |
| Current Weaknesses | df/du interpretation, open-file lifecycle, command precision and recovery validation |
| Readiness Trend | Initial baseline only; insufficient evidence for overall readiness |

## Active Question

Q02 — systemd service startup and permissions; awaiting an answer.

After a deployment, a Linux API fails to start under systemd. The journal reports Permission denied while opening its configured application file. Running the application manually as root succeeds, and a teammate suggests changing the unit to run as root permanently. How would you isolate the cause and restore the service while keeping permissions minimal?

## Coverage Checklist

`[x] ✅` means substantively attempted and evaluated, not mastered. Keep pending and explanation-only aspects unchecked; link completed aspects to evaluated questions.

- [x] ✅ Filesystem capacity, inodes and open/deleted files — Q01; df/du discrepancy and safe recovery need retesting.
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

| Question | Date | Score | Acceptance estimate | Record |
| --- | --- | --- | --- | --- |
| Q01 | 2026-10-04 | 4.5/10 | 35% | [Disk Full / df–du](questions/Q01-disk-full-df-du.md) |

## Retest Queue

- Q01: distinguish blocks/inodes and open deleted files in a fresh scenario; demonstrate evidence-preserving mitigation and validation.
