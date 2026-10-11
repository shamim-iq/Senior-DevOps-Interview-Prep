# Amazon Bedrock Interview Progress

**Cross-topic assessment planned through RAG.** Standalone practice has not started.

| Metric | Status |
| --- | --- |
| Completed standalone questions | 0 |
| Evaluated cross-topic references | 1 — RAG Q01 |
| Average score | Standalone: N/A; cross-topic Bedrock subscore: 6/10 |
| Readiness | Initial evidence only; service-role and operational precision need retesting |
| Coverage | 2 / 10 aspects assessed (20%) |

## Current Position

Review relevant RAG attempts as they are evaluated. Do not pre-credit planned overlap or start an independent question sequence yet.

## Coverage Checklist

Checked means substantively assessed, not mastered. Explanations alone do not earn a checkmark.

- [x] ✅ Knowledge Bases, data sources and ingestion/sync — RAG Q01; sync trigger unverified.
- [x] ✅ Titan embeddings and OpenSearch vector-store integration — RAG Q01; responsibility boundary needs correction, index details remain.
- [ ] Retrieval and generation APIs and response citations
- [ ] Claude/model choice, inference settings and limits
- [ ] Agents, orchestration and action groups
- [ ] Guardrails, grounding limits and sensitive-data handling
- [ ] IAM roles, resource access and document-level authorization
- [ ] Logging, monitoring, throttling, latency and cost
- [ ] Deployment, change management and recovery
- [ ] Self-healing pipeline: diagnosis, suggested fixes and approval safeguards

## Evidence and Scoring

| Source question | Assessed aspect | Topic-specific result | Gaps / retest |
| --- | --- | --- | --- |
| [RAG Q01](../rag/questions/Q01-bedrock-rag-project.md) | S3 ingestion, Titan/OpenSearch, retrieval/generation role distinction | Bedrock subscore 6/10; 0 standalone attempts | Verify sync trigger/store type; clarify Agent route and Haiku's role |

- Keep the canonical scenario, answer and overall score in the topic where the question was asked.
- After a RAG answer, link its saved question from MCP/Bedrock only where those concepts were substantively attempted and evaluated. Use relative links such as `../rag/questions/Q01-<name>.md` once the file exists.
- Record an explicitly explained topic-specific subscore when enough evidence exists; otherwise record partial evidence without a numeric score. Do not copy the overall RAG score into other topics or count one attempt as several independent questions.
- Keep standalone scores and cross-topic subscores separate in averages. Update checkboxes and counts only from evidence; keep weaknesses pending until independent retesting.
- An absent topic receives no credit or penalty. Mentioning a product name alone is not assessment.

## Practice Strategy

- Use the four-year DevOps / Platform baseline and the same feedback/scoring workflow as existing topics. Ask one question at a time; create question files only after answers.
- Start with the actual résumé project and distinguish personal work, team decisions and conceptual knowledge. Never invent implementation details or assume ownership from a listed tool.
- Later standalone practice should build on linked evidence, assess remaining gaps and avoid treating cross-topic explanations as mastery.
- Keep answers compact with connected explanations, diagrams where useful and only essential commands/API examples with purpose.
- Commit evaluated progress locally; push only when explicitly requested.

## Revision

- [ ] RAG Q01: verify sync mechanism, actual runtime API and serverless access/index responsibilities.
- [ ] RAG Q01: independently explain embedding, retrieval and response-generation services. Agent mention alone does not complete orchestration coverage.

- [ ] Complete initial assessment coverage.
- [ ] Retest demonstrated weaknesses independently.
- [ ] Defend actual project decisions with concrete evidence and trade-offs.

## Résumé Basis

Latest supplied résumé: Ai_DevOps_Shamim_4years.pdf. It lists an internal chatbot using Bedrock Agents, Claude Haiku, Knowledge Bases, S3, Titan Embeddings and OpenSearch; vector-store support, Guardrails and IAM; GitHub/Atlassian MCP usage; and a Bedrock pipeline for diagnosis and suggested fixes. These claims set question scope, not proven competence.
