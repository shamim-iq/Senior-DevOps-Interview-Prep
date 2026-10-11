# Linux Interview Progress

**Active topic: Phase 1 / Linux.** Kubernetes is paused by request; its Q11 remains pending in its own progress file.

| Metric | Current status |
| --- | --- |
| Questions Attempted | 10 / 10 — first cycle complete |
| Average Score | 6.45/10 — 64.5 / 10; historical scores unchanged |
| Average Acceptance Probability | 59.5% — subjective answer-specific estimates, not hiring probability |
| Topic Coverage | 13 / 15 aspects assessed (86.7%); scripting remains deferred |
| Current Strengths | Inode awareness, cautious deletion, least-privilege intent and path-permission investigation |
| Current Weaknesses | df/du and load-state interpretation, latency versus capacity, precise access scope and recovery validation |
| Readiness Trend | Useful diagnostic starting points; narrow mitigation, precise evidence interpretation and recovery validation remain recurring gaps. Overall readiness not established |

## Active Question

First-cycle review completed in Feedback.md. Q11 — Host patching and safe recovery; pending for the next practice turn.

Two Linux servers behind a load balancer run a production API. A kernel security update requires a reboot. A teammate suggests upgrading and rebooting both immediately. How would you prepare, patch and reboot safely, preserve a recovery path, and verify success before proceeding to the second host? Include essential Linux checks; no scripting required.

The unanswered shell-pipeline Q08 was replaced at the user's request on 2026-10-10. No attempt or score was recorded for it. Keep current questions focused on Linux administration and troubleshooting; defer shell scripting until the user asks to resume it. Diagnostic Linux commands remain in scope.

## Coverage Checklist

`[x] ✅` means substantively attempted and evaluated, not mastered. Keep pending and explanation-only aspects unchecked; link completed aspects to evaluated questions.

- [x] ✅ Filesystem capacity, inodes and open/deleted files — Q01; df/du discrepancy and safe recovery need retesting.
- [x] ✅ Processes, signals and safe service recovery — Q08; managed shutdown and partial-job recovery need retesting.
- [x] ✅ CPU, load average and process/thread diagnosis — Q03; task-state interpretation needs retesting, thread-level depth remains.
- [x] ✅ Memory, swap, OOM and resource limits — Q04; termination evidence and host-versus-service limits need retesting.
- [x] ✅ Disk I/O latency and storage performance — Q03; latency versus capacity and metric interpretation need retesting.
- [x] ✅ systemd services, dependencies and journal investigation — Q02 startup/journal assessed; dependency-specific diagnosis remains for later sampling.
- [x] ✅ Permissions, ownership, ACLs and privilege boundaries — Q02 identity/path permissions assessed; ACL-specific diagnosis remains for later sampling.
- [x] ✅ Users, groups, sudo and SSH access troubleshooting — Q09 SSH assessed; key custody and permission checks need retesting, sudo depth remains.
- [x] ✅ DNS, routing, sockets and connection diagnosis — Q05 sockets/private routing assessed; DNS-specific diagnosis remains for later sampling.
- [x] ✅ Firewalls and network access controls — Q05; source-scoped rules and private routing need retesting.
- [x] ✅ Mounts, filesystem recovery and persistent configuration — Q07; preservation, recovery and persistent mount safeguards need retesting.
- [ ] Shell scripting, pipelines, exit status and safe automation.
- [x] ✅ Scheduled jobs, cron/systemd timers and execution environments — Q06 cron assessed; environment differences need retesting, timers remain for later sampling.
- [x] ✅ Log management, rotation and evidence preservation — Q10; open-file reasoning correct, safe reopening and validation need retesting.
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

- [x] ✅ Complete the first 10 evaluated questions and consolidated review — Q01–Q10, 2026-10-11; see Feedback.md.
- [ ] Assess all planned Linux aspects.
- [ ] Retest recorded weaknesses independently.
- [ ] Demonstrate safe diagnosis, recovery and validation across varied scenarios.

## Evaluation History

| Question | Date | Score | Acceptance estimate | Record |
| --- | --- | --- | --- | --- |
| Q01 | 2026-10-04 | 4.5/10 | 35% | [Disk Full / df–du](questions/Q01-disk-full-df-du.md) |
| Q02 | 2026-10-04 | 7.5/10 | 70% | [systemd / Permissions](questions/Q02-systemd-permissions.md) |
| Q03 | 2026-10-05 | 6.5/10 | 60% | [High Load / Moderate CPU](questions/Q03-high-load-low-cpu.md) |
| Q04 | 2026-10-05 | 7/10 | 65% | [Memory / Process Termination](questions/Q04-memory-process-termination.md) |
| Q05 | 2026-10-06 | 6.5/10 | 60% | [API Private Connectivity](questions/Q05-api-private-connectivity.md) |
| Q06 | 2026-10-07 | 6/10 | 55% | [Cron Backup / Environment](questions/Q06-cron-backup-environment.md) |
| Q07 | 2026-10-10 | 6/10 | 55% | [Missing /data Mount](questions/Q07-missing-data-mount.md) |
| Q08 | 2026-10-10 | 7/10 | 65% | [Stalled Worker / Signals](questions/Q08-stalled-worker-signals.md) |
| Q09 | 2026-10-10 | 6.5/10 | 60% | [SSH Public-Key Access](questions/Q09-ssh-publickey-access.md) |
| Q10 | 2026-10-11 | 7/10 | 70% | [Log Rotation / Open File](questions/Q10-logrotate-open-file.md) |

Supplementary boot-process explanation: 8/10 conversational understanding check after reading the guide (2026-10-11); excluded from numbered attempts and averages.

## Next-Cycle Strategy

Cover host hardening/patching first, then alternate fresh DNS/ACL/sudo/timer scenarios with the retest queue. Checked broad areas still contain untested subtopics. Keep scripting deferred. Reassess after each answer and at the next ten-question checkpoint; coverage alone does not establish readiness.

## Retest Queue

- Q10: confirm open log descriptors, use supported reopen/rotation configuration and demonstrate successful writes through a subsequent rotation.

- Q09: demonstrate client-owned key recovery, account/key permissions, safe configuration validation and fresh-session verification.

- Q08: demonstrate managed-worker stop/restart safeguards, evidence-based resource changes and verification of partially processed jobs.

- Q07: stop writers, confirm filesystem identity/mount state, preserve and reconcile both datasets, configure startup safeguards and verify recovery.

- Q06: reproduce cron environment, distinguish scheduler logs from script output, scope backup permissions and demonstrate scheduled backup/restore validation.

- Q05: interpret loopback/private binding, scope firewall rules to approved clients, preserve private routing and verify client access/isolation.

- Q04: prove termination cause, distinguish host pressure from service limits, and validate mitigation through a representative traffic spike.

- Q03: interpret runnable/D-state evidence and I/O measurements; distinguish capacity from latency, choose a targeted mitigation and verify service recovery.

- Q01: distinguish blocks/inodes and open deleted files in a fresh scenario; demonstrate evidence-preserving mitigation and validation.
- Q02: independently scope file access and demonstrate restart/recovery validation. Evaluation uses the four-year baseline; advanced optional details are not required for full credit.
