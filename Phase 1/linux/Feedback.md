# Linux Interview Feedback

## Q04 — Memory / Process Termination — 2026-10-05

**Score: 7/10.** Subjective answer-specific acceptance estimate: 65%, not a hiring prediction. Four-year baseline; prior scores unchanged.

✅ Sound log-first investigation, useful common memory tools, rejection of routine cache drops and developer collaboration. Swappiness was proposed conditionally, not as an automatic fix.

| Dimension | Assessment |
| --- | --- |
| Technical accuracy | Good direction; distinguish kernel/application cache, available/free memory and vertical/horizontal scaling |
| Coverage | Kernel termination evidence, service limits and recovery checks missing |
| Interview representation | Clear diagnostic sequence |
| Conciseness | Relevant and reasonably compact |
| Troubleshooting | Current memory readings cannot prove the earlier cause; correlate historical evidence |
| Operational reasoning | Capacity/optimization sensible; bound swap tuning and validate under representative load |

Deductions: 1 termination proof, 0.75 mitigation safeguards, 0.75 validation, 0.5 combined terminology/metric precision. No advanced-command penalty. Retest host versus service-limit OOM later; rotate to network connectivity next.

## Q03 — High Load / Moderate CPU — 2026-10-05

**Score: 6.5/10.** Subjective answer-specific acceptance estimate: 60%, not a hiring prediction. Four-year baseline.

✅ Correctly avoided assuming CPU saturation; chose vmstat r/b/wa and iostat, considered dependencies and sought approval before deletion.

| Dimension | Assessment |
| --- | --- |
| Technical accuracy | Good initial hypothesis; distinguish runnable/D-state load from ordinary socket sleep |
| Coverage | Useful host investigation; concrete recovery criteria missing |
| Interview representation | Explain observed metrics before choosing a fix |
| Conciseness | Filesystem-choice discussion distracts from current evidence |
| Troubleshooting | Separate I/O latency from free blocks/inodes; ping does not test DB queries |
| Operational reasoning | Cautious cleanup is positive; target demonstrated bottleneck and validate |

Deductions: 1 load/task-state distinction, 1 latency/capacity conflation, 1 mitigation/validation gap, 0.5 DB verification limits. No deduction for omitted advanced tools. Retest with measured output later; rotate to memory for breadth. Q01 and Q02 scores unchanged.

Evaluate against the four-year DevOps / Platform baseline in AGENTS.md. Preserve historical scores and distinguish essential corrections from optional advanced coaching.

Record actual strengths and gaps after each answer, a score out of 10 and a subjective answer-specific Interview Acceptance Probability. Do not interpret this as hiring probability. Preserve history and consolidate feedback every 10 evaluated questions.

## Q01 — Disk Full / df–du Discrepancy — 2026-10-04

Score: 4.5/10
Interview Acceptance Probability: 35% (subjective estimate).

✅ Strong
- Recognized inode exhaustion as a genuine cause of failed file creation.
- Proposed assessing file importance before deletion.
- Recalled XFS dynamic inode allocation versus ext4 inode provisioning.

⚠️ Improve
- Address the supplied block-usage discrepancy; investigate open deleted files with lsof.
- Use df -i for inode availability, not du -i.
- Do not assume /var/apps is a standard application-log directory.
- Filesystem migration is not the immediate recovery; diagnose first and consider targeted reopen/restart rather than host reboot.
- Preserve evidence and validate space, writes and application health after mitigation.

| Dimension | Assessment |
| --- | --- |
| Technical accuracy | Valid inode concept; incorrect command and assumed path |
| Coverage | Missed central df/du clue and requested evidence-preserving recovery |
| Interview representation | Clear hypothesis but not tied to supplied measurements |
| Conciseness | Reasonably concise; filesystem preference distracts from incident |
| Troubleshooting approach | Needs block/inode distinction and open-file evidence |
| Senior reasoning | Cautious deletion is positive; targeted mitigation and validation missing |

Main deductions concern the missed diagnostic clue and recovery plan, not command volume. Retest open-file lifecycle later; move to service startup/permissions for breadth.

## Q02 — systemd / Permissions — 2026-10-04

**Score: 7.5/10.** Subjective answer-specific acceptance estimate: 70%, not a hiring prediction. Four-year baseline; Q01 unchanged.

✅ Correctly rejected unnecessary root privileges, used status/journal investigation, proposed testing the service identity and checked parent-path permissions with namei.

Essential corrections: confirm User/Group from the unit, use the actual denied file path rather than assume logs, grant only required application-group access, restart appropriately after group changes and verify the API/file operation. ls lists metadata, not log contents.

| Dimension | Assessment |
| --- | --- |
| Technical accuracy | Sound core approach; group access must be checked and scoped |
| Coverage | Diagnosis present; recovery validation omitted |
| Interview representation | Clear and relevant; distinguish operator from service identity |
| Conciseness | Good; useful commands without excessive detail |
| Troubleshooting | Strong path-level check; use the journal's exact path |
| Operational reasoning | Least-privilege intent sound; complete mitigation and verification |

Deductions: 1 for remediation scope, 1 for omitted restart/validation, 0.5 for identity/path precision. No penalty for not listing ACL, SELinux/AppArmor or systemd sandbox commands; those are conditional coaching. Retest minimal access and recovery later; rotate to CPU/load next.
