# Interview preparation workflow

## Hard rule: push only when asked

- Only push when the user explicitly asks for a push. Completing a question, recording progress, committing, or resuming a session does not authorize a push.
- This rule supersedes earlier automatic-push instructions. A previous push request does not authorize future pushes.
- Keep changes local until a push is requested, and report their local/unpushed status accurately. Fetching and safe pull/rebase synchronization remain part of the session workflow.

## Repository layout

- This checkout corresponds to the local `interviews/` directory. Keep `README.md`, `Phase 1/`, and future `Phase 2/`, `Phase 3/`, etc. directly at its root; do not nest another `interviews/` directory.
- Expected origin: `https://github.com/shamim-iq/Senior-DevOps-Interview-Prep.git`. Primary branch: `main`.
- Preserve existing topic folders, questions, answers, scores, feedback, and progress.

## Before resuming preparation

1. Run `git status`, `git branch --show-current`, and `git remote -v`. Verify the checkout root, branch, origin, and local changes. Do not blindly replace an unexpected remote or rename an existing branch.
2. Always run `git fetch origin`. After fetching, inspect `git status --short --branch` and `git log --oneline --left-right HEAD...origin/main` to determine ahead/behind state.
3. Inspect any local changes, including untracked files. Commit valid local work or safely stash it (including untracked files when needed) before synchronization. Do not overwrite work. Restore any stash after synchronization, verify its contents, and retain it until restoration is confirmed.
4. When safe, synchronize the local `main` branch with `git pull --rebase origin main`. If on another branch, inspect its work before safely returning to main. If synchronization fails, report the blocker rather than continuing from potentially stale progress.
5. If conflicts occur, pause normal preparation, inspect every conflicting file, and reconcile both systems' progress logically. Never blindly choose one side. Preserve distinct attempts and historical scores; resolve numbering collisions without deleting either question. Ask for clarification if the records cannot be reconciled reliably. Continue the rebase only after checking the resolution.
6. Review Markdown throughout every `Phase */` directory, including topic-level `Feedback.md`, `Progress.md`, and `questions/*.md`. These synchronized files are the source of truth.
7. Reconstruct the current phase, started topics, completed questions, latest question number, pending question, actual average scores, strengths, weaknesses, retest areas, and readiness. Unassessed metrics remain N/A. If summaries disagree with question records, inspect and reconcile the discrepancy without inventing results.
8. Resume a pending question or choose the next sequential question from the synchronized history. Do not restart at Q01 if previous progress exists. Adapt difficulty and topics to actual performance and check for duplicates before asking.

Never use `git reset --hard`, `git clean -fd`, or force-push unless the user explicitly authorizes it.

## Interview practice

- Ask one scenario-based question at a time, suited to approximately four years of DevOps / Platform experience targeting senior and SRE roles. Wait for the answer; do not reveal hints or the correct answer beforehand.
- Evaluate technical accuracy, coverage, interview representation, conciseness, troubleshooting approach, and senior-level reasoning. Give concise feedback, a score out of 10, and an answer-specific Interview Acceptance Probability. The percentage is a subjective estimate, not overall hiring probability.
- Create `questions/QNN-<topic>.md` only after an attempt, with the scenario, concise interview-ready answer, troubleshooting/reasoning flow, key points, an ASCII diagram if useful, and senior-level takeaways.
- Append actual feedback and update progress from evaluated attempts. Preserve prior scores and answers. Consolidate feedback after each 10 questions; adapt future questions to demonstrated gaps.
- Record the next pending question in progress so another system can resume it without duplication.

## After recording progress

1. Inspect `git status` and the changes. Fetch again and inspect incoming history before committing; if concurrent progress exists, protect local work and reconcile it using the same safe workflow above.
2. Stage the reviewed repository changes with `git add .` and commit with an accurate message, for example `Update Kubernetes interview progress - Q06`. Use the actual topic and question number. Do not make empty commits.
3. Stop after local recording/committing unless the user explicitly requests a push. Report pending local changes or unpushed commits.
4. Only when a push is requested, run `git pull --rebase origin main` again before pushing. Resolve any conflicts by preserving both histories and recheck affected records, numbering, and aggregates.
5. For that requested push, run `git push origin main`. If rejected because the remote advanced, fetch, inspect, rebase, validate, and retry without force-pushing.
6. Verify the final status and, if a push was requested and performed, the remote commit. Report any synchronization or push failure accurately; do not claim progress was saved remotely when it was not.

Apply this workflow to future phases and topics as well as Kubernetes. Future changes require explicit commits and pushes; Git does not automatically synchronize files.
