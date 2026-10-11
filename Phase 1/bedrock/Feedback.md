# Amazon Bedrock Interview Feedback

Use the four-year baseline in AGENTS.md. One cross-topic answer evaluated; no standalone answers.

## Cross-Topic Evidence — RAG Q01 — 2026-10-11

[Canonical RAG question](../rag/questions/Q01-bedrock-rag-project.md)

**Bedrock subscore: 6/10**, kept separate from the RAG overall score and standalone averages.

✅ Correctly named S3, Knowledge Bases, Titan V2 and OpenSearch in ingestion; understood managed infrastructure.

Corrections: establish the actual ingestion trigger; distinguish the embedding model/vector search from Haiku response generation; identify whether the CLI invokes an Agent or direct KB API; retain responsibility for collection access, index/data configuration and costs.

Deductions: 1.5 retrieval/generation service roles; 1 sync precision; 1 serverless responsibility boundary; 0.5 incomplete invocation path. Do not assume the user's automatic sync is absent or a particular model version/store configuration without evidence. Only two broad aspects are checked; other mentioned services remain unassessed or partially sampled.

Record strengths, essential corrections, optional coaching, explained scores and retests after each substantive attempt. Preserve previous evaluations. For cross-topic evidence, link the canonical question and evaluate only this topic's demonstrated concepts; do not duplicate the whole answer or its overall score.

Consolidate after each ten standalone questions, or during the RAG checkpoint for cross-topic evidence. Do not infer hiring probability or readiness from coverage alone.
