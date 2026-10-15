# Terraform Interview Progress

**Active topic: Phase 1 / Terraform.** Started 2026-10-15. RAG is paused with Q03 preserved.

## Assessment Agreement

- Exactly 20 scenario-based questions, asked one at a time. Wait for each answer before evaluating or asking the next question. Do not extend beyond Q20 without a new request.
- Use the four-year DevOps / Platform Engineer baseline in AGENTS.md. Include practical evidence interpretation and safe production decisions.
- After each attempt: individual verdict, score out of 10, credited strengths, explained deductions, concise corrected answer and revision needs. Label the required answer-specific acceptance estimate as subjective coaching, not a hiring probability.
- After Q10: interim consolidation. After Q20: final verdict based on all 20 scores, topic evidence, safety, independence, strengths and unresolved gaps. Distinguish coverage from mastery; preserve historical scores and dated retests.
- Adapt remaining scenarios to gaps while maintaining breadth. Retests count within the 20-question limit. No future answers or hints before an attempt.
- Save question/answer files only after attempts. Commit reviewed progress locally; push only when explicitly requested. Follow AGENTS.override.md for all Git operations.

## Metrics

| Metric | Status |
| --- | --- |
| Evaluated questions | 0 / 20 |
| Average score | N/A |
| Individual verdicts | None yet |
| Final verdict | Pending Q20 |
| Coverage | 0 / 12 aspects assessed |

## Current Position

Q01 — Unexpected production replacement; awaiting an answer.

You change a tag in Terraform for a production AWS environment. The CI plan unexpectedly shows that an existing database will be destroyed and recreated, even though you intended no database change. How would you investigate the plan, decide whether it is safe to proceed, and deliver the intended change without risking production data?

## Coverage Checklist

Checked means substantively assessed, not mastered. Link evidence after each evaluated attempt.

- [ ] Plan interpretation, resource lifecycle and safe changes
- [ ] State, remote backends, locking and recovery
- [ ] Drift and changes made outside Terraform
- [ ] Import and adoption of existing infrastructure
- [ ] Refactoring, resource addresses and moved blocks
- [ ] Modules, interfaces and versioning
- [ ] Variables, locals, outputs and type validation
- [ ] Dependencies, data sources and unknown values
- [ ] count, for_each and stable resource identity
- [ ] Providers, aliases, constraints and dependency lock files
- [ ] Environment/account isolation, secrets and access
- [ ] CI/CD, tests, policy checks and partial-failure recovery

## Individual Results

| Question | Assessed aspects | Score | Verdict | Revision |
| --- | --- | --- | --- | --- |
| None evaluated | — | N/A | N/A | N/A |

## Revision and Final Assessment

- [ ] Complete 20 evaluated attempts.
- [ ] Consolidate evidence after Q10.
- [ ] Retest demonstrated weaknesses within the agreed 20 questions.
- [ ] After Q20, calculate the actual average and deliver the final Terraform-specific verdict with practical limits and priorities.

Unassessed skills remain N/A. Do not infer overall role readiness from Terraform alone.
