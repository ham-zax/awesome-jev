# Data Labeling & Curation

Use this category when Jev annotates, filters, links, deduplicates, or triages records at scale.

## Submission format

```md
- [Name](URL) — Domain: one sentence describing the records, Jev label or match decision, and how the result is stored or reviewed.
```

## Entries

- [jevgrep (allebee)](https://github.com/allebee/jevgrep) — Log triage: filters text streams, including live `tail -f` output, by asking Jev one Noul per line and printing only lines above a caller-set probability threshold.

- [jev-align (Sutro)](https://github.com/sutro-sh/jev-align) — Dataset engineering: evaluates CSV, Parquet, and JSONL rows with typed Jev questions, sends ambiguous and audit samples to humans, and uses accepted corrections to refine the saved definition with GEPA.
- [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) — Dataset engineering: screens synthetic JSONL and Parquet rows with Jev probability checks and streams accepted records and rejections to separate outputs.
- [typeful-triage](https://github.com/cephalization/jev-triage) — Open-source maintenance: labels issues by kind, severity, urgency, duplication, and next step with Jev, while preserving human corrections as context for later runs.
- [jlink](https://github.com/keltokhy/jlink) — Research data: evaluates record pairs against a plain-English match rule with Jev and combines those pair judgments with local candidate blocking and match resolution.
- [jgrep](https://github.com/keltokhy/jgrep) — Data filtering: filters text, structured records, functions, and diff hunks against plain-English conditions using Jev probability judgments.
