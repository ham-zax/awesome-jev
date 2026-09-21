# Classification & Routing

Use this category when Jev classifies incoming state or selects a destination, model, tool, handler, or other bounded option.

## Submission format

```md
- [Name](URL) — Domain: one sentence describing the state, typed decision, and downstream action.
```

## Entries

### Model, tool & workflow routing

- [jev-router](https://github.com/gargpratyush/jev-router) — Developer tooling: asks Jev to choose the least-expensive capable model for each Claude Code task before forwarding the request.
- [jev-router (prismhq)](https://github.com/prismhq/jev-router) — LLM infrastructure: adds a Jev decision step to a LiteLLM router so each request is assigned to one candidate model.
- [pi-jev-router](https://github.com/mejiasd3v/pi-jev-router) — Coding agents: routes each Pi request to a model through a Jev decision exposed via Vercel AI Gateway.
- [jcm-router](https://github.com/adarshmishra07/jcm-router) — Coding agents: uses Jev to choose the Claude model and reasoning effort per message while preserving the main conversation cache.
- [Jev Auto Router](https://github.com/miniLV/Jev-Auto-Router) — Coding agents: asks Jev to choose one host-available model/effort pair per Codex call, then records whether independent verification still passes.
- [jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router) — Agent infrastructure: selects an agent skill with confidence-aware Jev decisions and declines weak matches instead of forcing a choice.
- [duet-agent](https://github.com/dzhng/duet-agent) — Agent infrastructure: keeps a Jev-backed routing table that decides which model should handle each request.
- [json-render](https://github.com/vercel-labs/json-render) — Generative UI: uses Jev in the compose path to select which components and actions should appear in a generated interface.
- [omo-jevlike-router](https://github.com/islee23520/omo-jevlike-router) — Skill routing: uses a frozen Qwen model in a Jev-style single-pass classifier to narrow the skill catalog injected into an agent prompt.
- [flue-jev-demo](https://github.com/matthewp/flue-jev-demo) — Agent routing: inserts a Jev decision step into a Flue agent through Cloudflare AI Gateway.
- [jev-fit](https://jev-fit.com) — Developer tooling: sends a software idea through a fixed Jev rubric that chooses plain code, Jev, or a reasoning LLM, returning “not sure” when confidence is low.
- [jev-skill-router](https://github.com/shimo4228/jev-skill-router) — Coding agents: evaluates whether Claude Code needs a skill, chooses from installed candidates with Jev, and defaults to shadow mode unless configured to inject the suggestion.
- [pi-jev (TheoOliveira)](https://github.com/TheoOliveira/pi-jev) — Coding agents: adds Jev-backed semantic tool routing and typed decision calls to the Pi coding agent.
- [pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router) — Coding agents: routes Pi work through typed Jev decisions instead of leaving the selection to free-form generation.

### Content, document & intent classification

- [Notra](https://github.com/usenotra/notra) — Marketing analytics: switches brand-visibility classifiers from an LLM to Jev Boolean decisions behind `NOTRA_JEV_CLASSIFIERS`, using a 0.5 threshold and targeting 300 ms p50.
- [typesafe-jev CV screener](https://github.com/gtaras7/typesafe-jev) — Recruiting: evaluates batches of CVs against an editable policy with typed Jev judgments so candidates can be re-scored when the policy changes.
- [Jev email intent workflow](https://github.com/GiesN/typesafe-jev-workflow) — Back-office automation: asks Jev for an `invoice` or `general` Choice and routes each inbound email to the matching LangGraph handler.
- [unclutter](https://github.com/kitze/unclutter) — Browser tooling: classifies page elements as clutter with Jev and removes matches under reusable template rules.
- [typesafe-adblock](https://github.com/realZachi/typesafe-adblock) — Browser tooling: evaluates DOM elements with Jev to decide which ones should be treated as ads and removed.
- [sift](https://github.com/bohutang/sift) — Social feeds: classifies X posts into substance, humour, chit-chat, promotion, junk, or AI-written content with Jev.
- [DocJev](https://github.com/jerryjliu/docjev) — Document pipelines: classifies documents against natural-language rules or detects sub-document boundaries, with swappable OCR backends and a benchmark harness for the same decisions.
- [Jev Wrapped](https://github.com/gaborishka/jev-wrapped) — Media analysis: classifies Telegram posts by content type and separately scores ad, clickbait, and emotional-pressure signals before aggregating the results into a shareable yearly view.
- [Jev Chat for Twitch](https://github.com/ethanplusai/jev-chat-for-twitch) — Live chat filtering: classifies Twitch messages by intent in batches of 20 and shows only messages matching the viewer’s selected category.

### Triage & operational routing

- [DiffJury](https://github.com/raihankhan-rk/diffjury) — Code review: uses Jev to classify pull-request risk before assigning the review path or human reviewer.
- [secondlayer](https://github.com/ryanwaits/secondlayer) — Operations: uses Jev decisions in both its Slack gate and fault-triage paths to decide what should proceed or escalate.
- [jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage) — On-call operations: batches collapsed Loki logs into typed Jev questions, then maps the answers in code to suppress, watch, review, notify, or page, sending low-confidence cases to review.
