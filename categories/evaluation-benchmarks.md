# Evaluation & Benchmarks

Use this category for Jev-based evaluators and for measured studies that compare, benchmark, or stress-test Jev on a defined task.

## Submission format

```md
- [Name](URL) — Evaluation: one sentence naming the task, comparison or metric, and what the study or evaluator measures.
```

## Entries

### Jev as evaluator

- [Jev Web Analyzer](https://github.com/replynodes/jev-web-analyzer) — Product evaluation: converts a public SaaS landing page to Markdown, asks Jev ten bounded questions about first-visit comprehension, and returns inspectable findings for the first change to consider.
- [minutes](https://github.com/silverstein/minutes) — Meeting software: uses Jev in the live-voice path to run bounded evaluations inside a local-first transcription application.
- [LegalForecast-MTD](https://github.com/johnhughes3/LegalForecastBench) — Legal evaluation: asks Jev to forecast federal motion-to-dismiss rulings from the judge’s written record and scores the resulting probabilities with claim-defendant micro-Brier metrics.

### Benchmarks & comparative studies

- [Jev Playground](https://github.com/hegargarcia/jev-playground) — Model comparison: evaluates Jev, Luna, Haiku, and Gemini on validated legal-move selection in explicit-state games, tracking decision quality and consistency across sequences.
- [Jev vs Mistral and Gemini for event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation) — Event discovery: compares Jev with Mistral Small and Gemini Flash-Lite on the same local-event validation task.
- [jev-research-eval](https://github.com/jgridifier/jev-research-eval) — Browser-agent evaluation: packages quality-controlled Jev Ultrafast research-browser cases with a suite runner and report generator for reproducible comparison.
- [Jev judge call vs dimension scores](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/) — Model evaluation: compares one direct Jev judgment per row with 12–14 Jev-scored dimensions plus locally fitted weights across three classification tasks.
- [Jev Pong](https://github.com/ably-labs/jev-pong) — Model comparison: advances a Pong simulation one step per model decision to compare Jev with LLMs through Vercel AI Gateway.
- [Jev reranking is not a free win](https://x.com/GoSailGlobal/status/2100877682972258619) — Retrieval evaluation: reports a run over 33,047 catalog entries, 164 real queries, and 9,831 graded pairs in which Jev-only reranking did not beat vector retrieval.
- [An early-access test of TypeSafe's Jev](https://lindfors.no/blog/a-first-look-at-typesafes-jev/) — Independent evaluation: measures early-access Jev judgments for calibration and cost per decision on the author’s test set.
- [WindTunnel](https://github.com/nekuda-ai/WindTunnel) — Browser-agent benchmark: compares WebMCP with other browser-agent interfaces and includes a Jev configuration among the measured systems.
- [jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval) — Third-party evaluation: compares Jev, GPT-4o-mini, and Claude Sonnet 4.5 under the same conditions on one judgment task.
- [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) — Ranking evaluation: tests whether Jev probabilities are suitable SQL sort keys using inversion, ordinality, calibration, wording-invariance, and tie checks across 20 Newsgroups and Amazon ESCI data.
- [jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) — Spam evaluation: measures zero-shot Jev Boolean spam classification against TF-IDF baselines on the same labeled data.
- [Can Jev Be a Better Agent Evaluator?](https://www.langchain.com/blog/jev-agent-evals-langsmith) — Agent evaluation: LangChain compares Jev with LLM judges on accuracy, repeatability, latency, and cost for online agent evaluation.

