# Linux Interview Feedback

No answers evaluated yet. Assess technical accuracy, coverage, interview representation, conciseness, troubleshooting approach and senior-level reasoning.

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
