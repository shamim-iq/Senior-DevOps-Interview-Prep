# RAG Interview Feedback

Use the four-year baseline in AGENTS.md. One answer evaluated.

## Q01 — Bedrock RAG Project — 2026-10-11

[Canonical question and corrected explanation](questions/Q01-bedrock-rag-project.md)

**Overall score: 6.5/10.** Subjective answer-specific acceptance estimate: 60%, not hiring probability.

✅ Correct two-flow model, embedding/vector-store concept, top-K retrieval and optional reranking. Candidate reports whole-setup implementation; request concrete configuration examples rather than infer or dismiss ownership.

| Dimension | Assessment |
| --- | --- |
| Accuracy | Haiku generation versus retrieval is the main correction; separate chunking from embedding |
| Coverage | Named project components; Agent invocation path and implementation evidence need clarification |
| Representation | Structured explanation, but distinguish deployed features from general design options |
| Conciseness | Avoid repeating the two-flow overview; use one ingestion and one query explanation |
| Troubleshooting | Inspect sync job and retrieved chunks independently from generated output |
| Operational reasoning | Serverless still requires access, data and cost ownership; refusal must be tested |

Deductions: 1.5 retrieval/generation role confusion; 0.75 unsupported automatic-sync certainty; 0.5 serverless responsibility; 0.75 assumed missing-evidence refusal. Automatic sync may exist in this deployment; its mechanism is unverified, not declared absent. No penalty for omitted MCP or advanced commands. Bedrock has its own linked subscore; MCP has no assessed evidence yet.

Next: chunking/retrieval-quality scenario, then spaced retests of Q01 gaps.

Record strengths, essential corrections, optional coaching, explained scores and retests after each substantive attempt. Preserve previous evaluations. For cross-topic evidence, link the canonical question and evaluate only this topic's demonstrated concepts; do not duplicate the whole answer or its overall score.

Consolidate after each ten standalone questions, or during the RAG checkpoint for cross-topic evidence. Do not infer hiring probability or readiness from coverage alone.

## Q02 - Chunking and Retrieval Quality - 2026-10-12

[Canonical question and corrected answer](questions/Q02-chunking-retrieval-quality.md)

**Score: 7/10.** Answer-specific acceptance estimate: 65% (subjective, not hiring probability).

Strengths: context-loss reasoning, splitting alternatives, overlap, size/cost trade-offs and metadata. Omissions: source-to-model evidence inspection and a controlled test measuring retrieval recall, mandatory warning completeness, source support, latency and cost. Qualify dense/hybrid superiority and hybrid cost claims; cosine is index-dependent. Semantic splitting need not use a generative LLM.

Deductions: 1 diagnostic isolation; 1.5 controlled validation; 0.5 retrieval generalizations. No spelling deductions or penalty for optional tools. Next: Q03 document-level authorization; retain Q01/Q02 gaps for spaced retesting. Average: (6.5 + 7) / 2 = 6.75/10.
