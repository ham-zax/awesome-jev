# Scoring & Ranking

Use this category when Jev assigns a score, probability, relevance signal, or ordering that downstream code uses to prioritize or select items.

## Submission format

```md
- [Name](URL) — Domain: one sentence describing what Jev scores, how results are ordered or thresholded, and what happens next.
```

## Entries

### Relevance, search & selection

- [hearth-jev-rental-search](https://github.com/Nancy-Chauhan/hearth-jev-rental-search) — Housing search: filters multi-source rental listings against user criteria with Jev so only plausible matches advance.
- [jev-resume-screening](https://github.com/nanami-0713/jev-resume-screening) — Recruiting: evaluates a resume against a job description with evidence gates, Score dimensions, and a routing Choice, escalating low-confidence cases to human review.
- [hippo-memory](https://github.com/kitfunso/hippo-memory) — Agent memory: reranks retrieved memories with Jev; the repository reports R@1 improving from 0.41 to 0.62 on a private 300-query developer store.
- [MemSearch Jev reranking](https://github.com/zilliztech/memsearch/blob/main/evaluation/reranking-evaluation.md) — Coding-agent memory: reranks retrieved Markdown chunks with Jev Noul judgments and publishes bilingual evaluation results.
- [Oko](https://github.com/bartlomein/oko) — Developer tooling: shortlists function-level code chunks with ripgrep and BM25, then asks Jev which candidates are relevant before returning excerpts through MCP.
- [grokbot-jev-jobs](https://github.com/mcgalleg/grokbot-jev-jobs) — Job search: scores public job postings against one resume in a daily Vercel cron so only plausible matches surface.

- [citation-verifier](https://github.com/MarissaFamularo/citation-verifier) — Academic publishing: scores whether a cited paper supports the sentence that cites it, with Claude locating candidate evidence and a human retaining the final decision.
- [jev-assist](https://github.com/glud123/jev-assist) — Coding agents: ranks tracked files against a one-line task description with parallel Jev judgments so an agent can start from the most relevant subset.
- [jev-bfs](https://github.com/komikat/jev-bfs) — Search tooling: ranks outgoing Wikipedia links with Jev while Python controls the breadth-first search used to connect two articles.
- [Jev Search](https://github.com/superagents-lab/jev-search) — Web search: scores Search1API result titles and snippets for relevance with Jev, then deduplicates URLs and groups lower-scoring matches separately.
- [jev.nvim](https://github.com/valentynkit/jev.nvim) — Developer tooling: splits a Neovim buffer into functions with Treesitter, scores each function against a natural-language question, and ranks matches in quickfix.
- [jev-reranker](https://github.com/hotchpotch/jev-reranker) — Retrieval and RAG: scores retrieved passages for relevance and evidentiary usefulness with Jev, then sorts and optionally filters them by threshold.
- [Jev Reranker (Rust CLI)](https://github.com/shinpr/jev-reranker) — Retrieval and RAG: provides JSON-in/JSON-out Jev checks for ranking candidates, enforcing evidence thresholds, and extracting source text as separate decisions.
- [jev-semgrep](https://github.com/uehaj/jev-semgrep) — Semantic search: scores source lines against natural-language meanings with Jev and supports combining multiple meanings with AND across languages.
- [nlgrep](https://github.com/YehuiTang0316/jev-nlgrep) — Developer tooling: scores code, documentation, logs, and text against natural-language conditions and returns thresholded matches linked to source lines.
- [jselect](https://github.com/keltokhy/jselect) — Research and retrieval: scores source-linked evidence for relevance with Jev, then applies local diversity selection to fit the chosen evidence within a token budget.
- [jsort](https://github.com/keltokhy/jsort) — Text measurement: turns pairwise Jev judgments under a plain-English criterion into a locally fitted Bradley–Terry ranking.
- [jgrep (kyu1204)](https://github.com/kyu1204/jgrep) — Developer tooling: scores code chunks, diff hunks, or CSV rows against natural-language conditions with Jev and prints grep-style hits above a configurable threshold.

### Quality, priority & measurement

- [Clean Code Judge](https://github.com/frostney/clean-code-review) — Code quality: evaluates pull-request files against 31 Boolean Clean Code smells plus size and nesting signals, then passes the structured verdicts to a writing model for review prose.
- [pagegrade](https://github.com/kitze/pagegrade) — Content quality: scores page sections for clarity, writing quality, and on-page SEO with Jev and reports the results per section.
- [jev-scout](https://github.com/AkashPriyadarshii/jev-scout) — Developer tooling: grounds candidates in GitHub and crates.io, then uses Jev to score architectural fit, maintenance freshness, and license suitability before returning ranked repositories or crates.
- [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) — SEO tooling: uses Jev for semantic intent classification, competitive-gap decisions, and confidence-gated GEO scoring while deterministic Rust code handles local audits and ranking history.
- [JevSlop](https://github.com/TKY-27/JevSlop) — Writing quality: asks Jev for eight Score dimensions on a public note.com article and combines them in TypeScript into a 0–100 slop score.
- [Supercov](https://github.com/supercorp-ai/supercov) — Code quality: asks Jev twelve Boolean-style properties per source file so a coding agent can prioritize which files need attention first.
- [jev-skip](https://github.com/valentynkit/jev-skip) — Media: scores YouTube caption segments for sponsor probability and marks likely sponsor sections on the seek bar before playback reaches them.
- [slop-grader](https://github.com/lukstei/slop-grader) — Writing quality: scores text against configurable rules for style, grammar, and technical-document quality, surfaces line-level findings, and can feed them back to an editing agent.
- [BTK audit studies](https://boringtoolskit.com/blog/seo-audit-cost-2026/) — Content and growth: uses Jev to prioritize “striking-distance” SEO fixes across site audits; the published study reports 1,204 pages judged per run and 4,816 judgments in under three minutes.
