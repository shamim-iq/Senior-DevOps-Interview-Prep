# RAG Interview Progress

**Active topic: Phase 1 / RAG.** Linux is paused with Q11 preserved; Kubernetes remains paused.

| Metric | Status |
| --- | --- |
| Completed standalone questions | 2 / 10 in first cycle |
| Evaluated cross-topic references | 0 |
| Average score | 6.75/10 |
| Readiness | Early baseline; diagnostic isolation and validation need retesting |
| Coverage | 4 / 12 aspects assessed (33.3%) |

## Current Position

Q03 - Document-level authorization; awaiting an answer.

Your internal Bedrock RAG chatbot indexes general engineering runbooks and restricted incident reports. An engineer who cannot access a restricted report in S3 receives details from it in a chatbot answer. How would you investigate the leak, contain it safely, enforce each user's document permissions throughout retrieval and generation, and verify the fix?

## Coverage Checklist

Checked means substantively assessed, not mastered. Explanations alone do not earn a checkmark.

- [x] ✅ End-to-end RAG flow and personal project ownership — Q01; roles need correction, ownership details remain self-reported.
- [ ] Document ingestion, parsing and metadata
- [x] ✅ Chunking strategy and overlap - Q02; diagnostic validation remains weak.
- [ ] Embeddings and vector index compatibility
- [x] ✅ Retrieval, filtering, hybrid search and reranking — Q01/Q02 retrieval and search trade-offs assessed; filtering depth and cost claims need retesting.
- [ ] Prompt context, generation and source citations
- [x] ✅ Missing evidence, hallucinations and grounded answers — Q01 attempted; abstention guarantees need retesting.
- [ ] Freshness, updates, deletion and ingestion failures
- [ ] Retrieval versus generation evaluation and test datasets
- [ ] Latency, cost, observability and troubleshooting
- [ ] Document access, sensitive data and prompt injection
- [ ] Agent/tool integration, MCP boundaries and safe actions

## Evidence and Scoring

| Source question | Assessed aspect | Topic-specific result | Gaps / retest |
| --- | --- | --- | --- |
| [Q01](questions/Q01-bedrock-rag-project.md) | Pipeline, retrieval/reranking, missing evidence | 6.5/10 overall; acceptance estimate 60% (subjective) | Separate retrieval/generation; confirm sync; test abstention |
| [Q02](questions/Q02-chunking-retrieval-quality.md) | Chunking, overlap, search trade-offs and metadata | 7/10; acceptance estimate 65% (subjective) | Trace evidence; controlled before/after validation |

- Keep the canonical scenario, answer and overall score in the topic where the question was asked.
- After a RAG answer, link its saved question from MCP/Bedrock only where those concepts were substantively attempted and evaluated. Use relative links such as `../rag/questions/Q01-<name>.md` once the file exists.
- Record an explicitly explained topic-specific subscore when enough evidence exists; otherwise record partial evidence without a numeric score. Do not copy the overall RAG score into other topics or count one attempt as several independent questions.
- Keep standalone scores and cross-topic subscores separate in averages. Update checkboxes and counts only from evidence; keep weaknesses pending until independent retesting.
- An absent topic receives no credit or penalty. Mentioning a product name alone is not assessment.

## Practice Strategy

- Use the four-year DevOps / Platform baseline and the same feedback/scoring workflow as existing topics. Ask one question at a time; create question files only after answers.
- Start with the actual résumé project and distinguish personal work, team decisions and conceptual knowledge. Never invent implementation details or assume ownership from a listed tool.
- Cover core RAG and Bedrock throughout the first cycle; include MCP where realistic, without forcing it into every pipeline. Rotate coverage and retest gaps later. Review after ten RAG questions.
- Keep answers compact with connected explanations, diagrams where useful and only essential commands/API examples with purpose.
- Commit evaluated progress locally; push only when explicitly requested.

## Revision

- [ ] Q02: trace source, parsed text, chunks, retrieval and generation; validate fixed evidence/answer tests.
- [ ] Q02: qualify dense/hybrid quality and cost claims; measure chunking trade-offs.

- [ ] Q01: independently distinguish embedding, retrieval, reranking, generation and Agent roles.
- [ ] Q01: verify actual sync mechanism and serverless responsibilities; test missing-evidence behavior.

- [ ] Complete initial assessment coverage.
- [ ] Retest demonstrated weaknesses independently.
- [ ] Defend actual project decisions with concrete evidence and trade-offs.

## Résumé Basis

Latest supplied résumé: Ai_DevOps_Shamim_4years.pdf. It lists an internal chatbot using Bedrock Agents, Claude Haiku, Knowledge Bases, S3, Titan Embeddings and OpenSearch; vector-store support, Guardrails and IAM; GitHub/Atlassian MCP usage; and a Bedrock pipeline for diagnosis and suggested fixes. These claims set question scope, not proven competence.
