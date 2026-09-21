# SDKs, Integrations & Infrastructure

Use this category for software that exposes Jev to another language, framework, runtime, protocol, database, or agent environment rather than defining one application decision of its own.

## Submission format

```md
- [Name](URL) — Integration: one sentence describing the host environment, Jev surface, and the main integration behavior.
```

## Entries

### SDKs & language clients

- [zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai) — Scala: provides a ZIO client and typed DSL for Jev decisions.
- [TypeSafe AI Swift SDK](https://github.com/alterhq/typesafe-sdk-swift) — Swift: provides a dependency-free Swift 6 client for Choice, Score, and probability questions with strict concurrency, configurable authentication, retries, and offline transport tests.
- [laravel-typesafe-jev](https://github.com/Butochnikov/laravel-typesafe-jev) — PHP: integrates Jev with Laravel through typed responses, asynchronous requests, scoped dependency injection, and testing fakes.
- [advocaat](https://github.com/pithings/advocaat) — Data tooling: provides a small type-safe client for asking Jev questions about datasets.
- [jevclient](https://pypi.org/project/jevclient/) — Python: packages an asynchronous Jev client on PyPI.
- [jev (Elixir)](https://github.com/dannote/jev) — Elixir: wraps Jev in a GenServer whose typed answers can be pattern-matched directly by callers.
- [jev-go](https://github.com/Stumble/jev-go) — Go: provides a community SDK for Jev.
- [jev-cli](https://github.com/tumf/jev-cli) — CLI: exposes Jev from a small dependency-free command-line client.
- [ai-python](https://github.com/vercel-labs/ai-python) — Python: carries Jev through the Vercel AI SDK’s evaluation operation and Gateway examples.
- [ruby_decision_model](https://github.com/obie/ruby_decision_model) — Ruby: provides a client abstraction for typed decision models such as Jev.
- [s1_ruby](https://github.com/innocentdiaz/s1_ruby) — Ruby: models System One measurement as a Ruby primitive with a TypeSafe provider and its own specification suite.
- [huncho](https://github.com/edgardcham/huncho) — TypeScript: wraps Jev answers in named decisions with hysteresis thresholds, one-call decision trees, JSONL journaling, replay, and calibration utilities across multiple providers.
- [hunch](https://github.com/carldaws/hunch) — Ruby: turns Jev-backed probability, Choice, and Score questions into idiomatic branching helpers such as `likely?`, `pick`, and `rate`.
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — Python: TypeSafe AI’s official adapter for running Jev-style System One evaluations over OpenAI- and Anthropic-compatible model APIs.
- [jevkit](https://github.com/ariel-frischer/jevkit) — Rust: validates Choice, Score, and probability question sets with offline lint rules before sending the canonical Jev payload and returning confidence-bearing JSON.

### Gateways, MCP & protocol bridges

- [jev-mcp (jkudish)](https://github.com/jkudish/jev-mcp) — MCP: exposes Jev claim verification, content screening, and candidate ranking as standard MCP tools.
- [jev-mcp (blakestone-x)](https://github.com/blakestone-x/jev-mcp) — MCP: exposes classify, score, check, match, and screen operations with confidence-bearing Jev responses.
- [safer-with-jev](https://github.com/andrelandgraf/safer-with-jev) — Cloud infrastructure: proxies Jev decisions through a Neon Function in front of the Neon AI Gateway.
- [Jevbridge](https://github.com/tacticocc/Jevbridge) — Agent protocols: bridges Jev into ACP and MCP clients including Codex, Claude, and Grok.
- [decide-mcp](https://github.com/dakdevs/decide-mcp) — MCP: wraps Jev in a configurable decision server with percentage scores and bias-profile routing.
- [rotom](https://github.com/RyanKung/rotom) — Local gateways: includes Jev in an OpenAI- and Anthropic-compatible gateway’s model catalog and evaluation path.
- [new-api-typesafe-plugin](https://github.com/FFatTiger/new-api-plugin-typesafe) — LLM gateway: adds a native `/v1/systemone` endpoint, synchronous Jev evaluation, and token billing to QuantumNous/new-api.
- [Jev AI](https://jev-ai.pro) — Hosted tooling: provides a public playground and API for Choice, Score, and yes/no Jev questions over pasted text, returning parsed answers with confidence.
- [openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp) — MCP: provides a Python decision gateway and stdio server for reaching Jev through OpenRouter’s decisions endpoint.
- [jev-mcp (burnigtm)](https://github.com/burnigtm/jev-mcp) — MCP: adds Jev tools to Cursor, Codex, and other MCP clients, with a repository-level test suite covering the server.

### Framework & agent integrations

- [eve](https://github.com/vercel/eve) — Agent frameworks: uses `typesafe-ai/jev` as the default model in eve’s experimental evaluation path.
- [AI CLI](https://github.com/vercel-labs/ai-cli) — Developer tooling: lets Vercel’s AI CLI run Jev as the model behind its `evaluate` command.
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — Official tooling: packages installable agent skills that teach coding agents how to structure and call Jev decisions.
- [Smithers](https://github.com/smithersai/smithers) — Agent frameworks: integrates a Jev session checker into a TypeScript workflow framework.
- [skillbox](https://github.com/kitze/skillbox) — Skills infrastructure: adds optional Jev-based recommendations to a self-hosted, versioned skill library.
- [Cline plugins](https://github.com/cline/plugins) — Coding agents: includes a Jev-driven browser plugin in Cline’s official plugin collection.
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) — Web frameworks: adds Hono middleware that uses Jev to route HTTP requests by meaning rather than only by method and path.
- [jev-use](https://github.com/shitianfang/jev-use) — Agent tooling: exposes typed Jev judgments through MCP, a library, and a native Pi extension, rejecting questions that require generation and flagging low-confidence answers as priors.
- [JarvisCore](https://github.com/Prescott-Data/jarviscore-framework) — Agent frameworks: integrates Jev as a decision client separate from the text model for specialist selection and RAG prompt-injection checks.
- [jev-skill-suggester](https://github.com/win4r/jev-skill-suggester) — Coding agents: asks Jev which installed skills are relevant to a request and returns a bounded recommendation set.
- [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) — Agent bridges: connects Jev to Grok Bot as a typed decision layer with usage gates, a skill template, and worked examples.
- [jev-architect](https://github.com/karanb192/jev-architect) — Design tooling: packages guidance and references for designing, evaluating, and delivering Jev decision loops as an agent skill.
- [pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev) — Coding agents: exposes five Jev tools to Pi so narrow semantic judgments stay typed while thresholds, weights, and actions remain under code or user control.
- [jev-judgment](https://github.com/HyunjunJeon/jev-judgment) — Coding agents: packages an agent skill that sends closed coding judgments to Jev instead of a free-form text model.
- [augustus](https://github.com/24601/Augustus) — Agent design: maps Choice, Score, and probability questions onto decision-theory, reranking, and routing patterns, with composition rules and validation gates.
- [pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask) — Coding agents: adds Jev as Pi’s low-overhead decision layer for bounded judgments that do not require generated text.
- [super-jev](https://github.com/Kevthetech143/super-jev) — Decision harness: wraps Jev answers in a small extensible layer that maps typed decisions to bounded application actions.
- [jev-superpowers](https://github.com/AkashPriyadarshii/jev-superpowers) — Coding agents: integrates Jev typed decisions into a structured software-development framework for agent routing, package checks, and completion gates.
- [Atomic](https://github.com/bastani-inc/atomic) — Coding agents: adds Jev as a first-class structured-output provider inside Atomic’s shared decision resolver.
- [jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill) — Coding agents: provides Claude Code and ZCode with Jev-backed classify, screen, score, and compliance-check operations through an installable skill and standalone caller.
- [HA-Jev](https://github.com/AboveColin/HA-Jev) — Home Assistant: turns Jev Choice, Score, and probability answers into sensors, automation actions, and an Assist conversation agent, with configurable confidence and daily token budgets.

### Data & query integrations

- [LlamaIndex Jev](https://github.com/WiktorB2004/llama-index-jev) — Retrieval and RAG: adapts Jev to LlamaIndex for passage scoring and query-engine selection, with the project reporting an nfcorpus nDCG@5 increase from 0.340 to 0.396 in its example.
- [jevql](https://github.com/kylemclaren/jevql) — SQL tooling: provides a psql-shaped CLI plus Go, TypeScript, and Python SDKs that run ordinary Postgres queries before applying Jev filters, sorts, and groups to surviving rows.
- [sqlite-jev](https://github.com/mgaitan/sqlite-jev) — SQLite: exposes Jev Choice, Score, and probability questions as loadable SQL functions and batched virtual-table queries.
- [duckdb-jev](https://github.com/prasanthj/duckdb-jev) — DuckDB: applies Jev decisions directly to structured SQL rows through a native extension with confidence results and bounded concurrency.

