# Classification & Routing

Use this category when Jev classifies incoming state or selects a destination, model, tool, handler, or other bounded option.

## Submission format

```md
- [Name](URL) — Domain: one sentence describing the state, typed decision, and downstream action.
```

## Entries

### Model, tool & workflow routing

- [Jevonian](https://github.com/xinyao27/jevonian) — Coding agents: uses one Jev call to select both model route and thinking level from session state, quota health, capabilities, and cache-switch penalties, while deterministic rules handle pinned or disabled routes.

- [jev-router (prismhq)](https://github.com/prismhq/jev-router) — LLM infrastructure: adds a Jev decision step to a LiteLLM router so each request is assigned to one candidate model.
- [jcm-router](https://github.com/adarshmishra07/jcm-router) — Coding agents: uses Jev to choose the Claude model and reasoning effort per message while preserving the main conversation cache.
- [jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router) — Agent infrastructure: selects an agent skill with confidence-aware Jev decisions and declines weak matches instead of forcing a choice.
- [duet-agent](https://github.com/dzhng/duet-agent) — Agent infrastructure: keeps a Jev-backed routing table that decides which model should handle each request.
- [omo-jevlike-router](https://github.com/islee23520/omo-jevlike-router) — Skill routing: uses a frozen Qwen model in a Jev-style single-pass classifier to narrow the skill catalog injected into an agent prompt.
- [flue-jev-demo](https://github.com/matthewp/flue-jev-demo) — Agent routing: inserts a Jev decision step into a Flue agent through Cloudflare AI Gateway.
- [jev-fit](https://jev-fit.com) — Developer tooling: sends a software idea through a fixed Jev rubric that chooses plain code, Jev, or a reasoning LLM, returning “not sure” when confidence is low.

### Content, document & intent classification

- [Diffusion Jev](https://github.com/Hangzhi/diffusion-jev-sglang) — Visual classification: serves a Jev-style DiffusionGemma/SGLang classifier that selects doodle and flower labels from image pixels with typed Choice questions and exposes candidate scores in a drawing playground.
- [AI-decision-maker](https://github.com/zlZayn/AI-decision-maker) — Data cleaning: classifies CSV columns into a fixed 13-type vocabulary and each dataset into one of six scenes with Jev Choice questions before local code applies the writes.
- [jev-table-import-mapper](https://github.com/DuvInc/jev-table-import-mapper) — Data import: maps unmatched CSV columns to destination fields with Jev judgments after an exact-name pass, leaving low-confidence fields unmapped instead of guessing.

- [Notra](https://github.com/usenotra/notra) — Marketing analytics: switches brand-visibility classifiers from an LLM to Jev Boolean decisions behind `NOTRA_JEV_CLASSIFIERS`, using a 0.5 threshold and targeting 300 ms p50.
- [typesafe-jev CV screener](https://github.com/gtaras7/typesafe-jev) — Recruiting: evaluates batches of CVs against an editable policy with typed Jev judgments so candidates can be re-scored when the policy changes.
- [Jev email intent workflow](https://github.com/GiesN/typesafe-jev-workflow) — Back-office automation: asks Jev for an `invoice` or `general` Choice and routes each inbound email to the matching LangGraph handler.
- [DocJev](https://github.com/jerryjliu/docjev) — Document pipelines: classifies documents against natural-language rules or detects sub-document boundaries, with swappable OCR backends and a benchmark harness for the same decisions.
- [Jev Wrapped](https://github.com/gaborishka/jev-wrapped) — Media analysis: classifies Telegram posts by content type and separately scores ad, clickbait, and emotional-pressure signals before aggregating the results into a shareable yearly view.
- [Jev Chat for Twitch](https://github.com/ethanplusai/jev-chat-for-twitch) — Live chat filtering: classifies Twitch messages by intent in batches of 20 and shows only messages matching the viewer’s selected category.

### Triage & operational routing

- [Jev-Mail](https://github.com/vynnlee/jev-mail) — Email productivity: classifies Gmail messages for urgency, importance, and category in Google Apps Script, sending uncertain or suspicious mail to Review without a local daemon.
- [jev-oncall](https://github.com/mingleiw/jev-oncall) — On-call operations: classifies each alert for actionability, severity, owner, and duplication, then code pages, drops, or sends it to human review under fixed thresholds and timeout fallbacks.

- [DiffJury](https://github.com/raihankhan-rk/diffjury) — Code review: uses Jev to classify pull-request risk before assigning the review path or human reviewer.
- [secondlayer](https://github.com/ryanwaits/secondlayer) — Operations: uses Jev decisions in both its Slack gate and fault-triage paths to decide what should proceed or escalate.
- [jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage) — On-call operations: batches collapsed Loki logs into typed Jev questions, then maps the answers in code to suppress, watch, review, notify, or page, sending low-confidence cases to review.
