# RAG Interview Progress

**Active topic: Phase 1 / RAG.** Linux is paused with Q11 preserved; Kubernetes remains paused.

| Metric | Status |
| --- | --- |
| Completed standalone questions | 0 |
| Evaluated cross-topic references | 0 |
| Average score | N/A — no evaluated evidence |
| Readiness | Unassessed |
| Coverage | 0 / 12 aspects assessed |

## Current Position

Q01 — Résumé project walkthrough; awaiting an answer.

Walk me through the internal RAG chatbot described in your résumé, from a document being added to S3 to a user receiving an answer. Explain where Bedrock Knowledge Bases, Titan Embeddings, OpenSearch, Claude Haiku and Bedrock Agents fit, which parts you personally worked on, and how you would handle a question whose answer is absent from the documents. If a listed component was not part of your actual implementation, say so rather than inventing a role for it.

## Coverage Checklist

Checked means substantively assessed, not mastered. Explanations alone do not earn a checkmark.

- [ ] End-to-end RAG flow and personal project ownership
- [ ] Document ingestion, parsing and metadata
- [ ] Chunking strategy and overlap
- [ ] Embeddings and vector index compatibility
- [ ] Retrieval, filtering, hybrid search and reranking
- [ ] Prompt context, generation and source citations
- [ ] Missing evidence, hallucinations and grounded answers
- [ ] Freshness, updates, deletion and ingestion failures
- [ ] Retrieval versus generation evaluation and test datasets
- [ ] Latency, cost, observability and troubleshooting
- [ ] Document access, sensitive data and prompt injection
- [ ] Agent/tool integration, MCP boundaries and safe actions

## Evidence and Scoring

| Source question | Assessed aspect | Topic-specific result | Gaps / retest |
| --- | --- | --- | --- |
| None yet | — | — | — |

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

- [ ] Complete initial assessment coverage.
- [ ] Retest demonstrated weaknesses independently.
- [ ] Defend actual project decisions with concrete evidence and trade-offs.

## Résumé Basis

Latest supplied résumé: Ai_DevOps_Shamim_4years.pdf. It lists an internal chatbot using Bedrock Agents, Claude Haiku, Knowledge Bases, S3, Titan Embeddings and OpenSearch; vector-store support, Guardrails and IAM; GitHub/Atlassian MCP usage; and a Bedrock pipeline for diagnosis and suggested fixes. These claims set question scope, not proven competence.
