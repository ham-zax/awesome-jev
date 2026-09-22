# Guides, Analysis & Community

Use this category for tutorials, explainers, technical analyses, public discussions, directories, case reports, and demo collections that help readers understand Jev or the surrounding System One pattern.

## Submission format

```md
- [Name or title](URL) — Source: one sentence explaining what the resource teaches, demonstrates, measures, or argues.
```

## Entries

### Tutorials & explainers

- [Jev by Example](https://github.com/ReallyArtificial/jev-by-example) — Agent development: runnable JavaScript lessons cover memory reconciliation, recovery proposals, handoff checks, and explicit application policies around Jev decisions.
- [Search with Jev and Milvus](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) — Search engineering: nine runnable notebooks combine Milvus retrieval with Jev judgments for ranking, filtering, routing, and stopping.
- [jev-usecases](https://github.com/kenhuangus/jev-usecases) — Reference harnesses: collects production-shaped examples built around confidence-gated Jev decision logic.
- [A deep dive into Jev](https://flaviocopes.com/jev/) — Blog: explains the System One model, typed decision interface, and how Jev differs from general text-generation models.
- [Jev Tutorial](https://www.jev-tutorial.org/) — Site: multilingual implementation guide covering Choice, Score, Noul, Python SDK calls, thresholds, deterministic fallbacks, and human escalation.
- [Jev vs GPT-6 Astra: when to use each](https://vercel.com/i/jev-vs-gpt-6-astra) — Guide: compares when to use Jev versus a frontier generative model and links several Jev use cases.

- [Jev 中文解读](https://x.com/dotey/status/2100109937237987823) — X (Chinese): explains Jev to Chinese readers as a calibrated typed-decision layer rather than a text-generation model.
- [WTF is Jev, ELI5](https://x.com/mvanhorn/status/2100761338918363550) — X: introduces Jev with the “AI multiple choice, not AI essay writing” analogy and explains the basic System One interface.
- [Full Jev tutorial](https://x.com/moritzkremb/status/2100715237267660873) — X: walks through the API and then builds voice-controlled browsing, memory, and YouTube-preprocessing examples.
- [WTF is Jev, and the 9 things people are building with it](https://x.com/mvanhorn/status/2100788572316139655) — X: combines a plain-language Jev explainer with nine early application patterns.
- [Jev is a really smart switch statement](https://x.com/NathanFlurry/status/2100036101809619314) — X: frames Jev as a fast learned branching primitive that complements rather than replaces general-purpose text models.
- [Arbitrary classification as a type-safe primitive](https://x.com/cocktailpeanut/status/2100277062309179521) — X: argues that the useful abstraction is runtime-defined, typed classification rather than classification as a one-off model task.
- [深入解读 Jev 模型：毫秒级判定与工程边界](https://github.com/kuhung/understanding-jev) — GitHub (Chinese): examines Jev’s decision-model interface, latency characteristics, and practical engineering boundaries.
- [TypeSafe AI's Jev Is Not an LLM - and That May Be the Point](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/) — News analysis: explains why refusing to generate free-form text can be an advantage for bounded software decisions and inference cost.
- [Ask HN: What do you think of Noul, a new decision primitive](https://news.ycombinator.com/item?id=49760225) — Hacker News: discusses `Noul`, the probability-of-true answer shape, as a software primitive that could outlive any one Jev implementation.
- [jev-cookbook](https://github.com/nexibeo/jev-cookbook) — GitHub: provides 15 runnable Node recipes for routing tickets, filing documents, categorizing transactions, labeling Gmail, and escalating low-confidence Jev decisions.
- [typesafe-jev-examples](https://github.com/rajivkuriakose/typesafe-jev-examples) — GitHub: packages worked ticket-triage and reranking examples with sample data and a Makefile, runnable through OpenRouter.
- [Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev) — LangChain: walks through adding Jev to an agent harness as a bounded decision layer and connects the design to LangChain’s later evaluator work.

### Technical analysis & critique

- [JEV captcha arbitrage](https://x.com/kenonews/status/2101656436136661163) — X: analyzes CAPTCHA-solving economics using Jev’s per-decision pricing against marketplace payouts.
- [Replacing an agentic classification loop with Jev](https://blog.r6i.it/typesafe-jev-vs-agentic-loop.html) — Blog: replaces an agentic classification loop with one Jev call and reports a 7× speedup.
- [Jev and the System One Model (Latent Space)](https://www.latent.space/p/jev) — Podcast: Diogo Almeida discusses RLCD, reliability, inference economics, and System One models.
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — Documentation: TypeSafe’s page on model jaggedness for the Jev 1.13 release.
- [Jev cannot emit an invalid output, but where is the reliability curve?](https://www.reddit.com/r/ArtificialInteligence/comments/1wm873q/typesafes_jev_cannot_emit_an_invalid_output_but/) — Reddit: questions whether Jev’s calibration claims are backed by published ECE or reliability curves while accepting its typed-output guarantee.
- [Why I couldn't build Jev at OpenAI](https://www.youtube.com/watch?v=cFx9Z3ZXca0) — Video: Diogo Almeida explains the design motivation behind System One models and why the work became a separate company.
- [TypeSafe's Jev Can't See. I Made It Guess What I Drew Anyway](https://mikulskibartosz.name/typesafe-jev-guess-what-i-drew) — Blog: explores what Jev can infer from textual descriptions of drawings despite lacking direct image input.

- [MLP on Qwen 4B mimicking Jev](https://x.com/justALEXWORTEGA/status/2100341039986798930) — X: reports an experiment in which a small MLP over Qwen 4B reproduces Jev-like decision behavior.
- [Running a local Typesafe Jev](https://x.com/wmoto_ai/status/2100454049359577516) — X (Japanese): documents an attempt to reproduce the Jev interaction pattern locally and notes remaining speed limitations.
- [Jev is the fish at the poker table](https://backnotprop.com/blog/jev-poker/) — Blog: uses poker as a stress test for where a fast decision model helps and where open-ended reasoning still matters.
- [Jev is about to change the AI economy](https://thefinancialengineer.substack.com/p/typesafes-jev-is-about-to-change) — Substack: argues that cheap calibrated decisions could shift inference spend away from general-purpose generation in bounded workflows.
- [This is a terrible compaction strategy](https://x.com/theo/status/2100762304862384257) — X: critiques Jev-based context pruning on the grounds that compaction requires reconstruction rather than simple relevance filtering.
- [It is the inference technique, not the training](https://x.com/anderslie/status/2100388704644919662) — X: argues that Jev’s speed is primarily an inference-interface effect and that similar APIs can be built over open-weight models.
- [Jev's Architecture Unmasked](https://x.com/iwashi86/status/2100713337436930288) — X (Japanese): summarizes an inference-time investigation based on many API calls and proposes a hypothesis for Jev’s parallel decision mechanism.
- [Five open Jev replicas worth trying](https://x.com/xiaomovps/status/2100923960493818177) — X (Chinese): surveys five open System One-style models and notes which ones are practical on consumer hardware.
- [Chinese notes after a day with Jev](https://x.com/jiayuan_jy/status/2100876273061102006) — X (Chinese): offers a skeptical early assessment, treating Jev as a fast general classifier while questioning its behavior on knowledge-heavy tasks.
- [Has anyone tried Jev as a relevance filter for RAG?](https://reddit.com/r/AI_Agents/comments/1wjpgbx/has_anyone_tried_jev_as_a_relevance/) — Reddit: discusses using Jev as a retrieval relevance filter and reranker, including the limitations suggested by early negative reranking results.
- [Jev is just a classifier, and that is fine](https://x.com/bojie_li/status/2100688989006475580) — X (Chinese): argues that Jev is best understood as a representation/classification model and ties its latency to one prefill plus parallel answer scoring.
- [One 50 ms pass versus 23 turns](https://x.com/be_arsh/status/2101026864341164110) — X: contrasts a specialist form-filling System One model with a multi-turn LLM agent to illustrate the latency trade-off between bounded scoring and iterative generation.

### Demos & implementation reports

- [Spike: Jev as a judgement layer to cut model cost](https://github.com/open-orcha/orcha/issues/253) — Issue: proposes moving agent judgment into Jev to reduce model cost inside a multi-agent orchestration platform.

- [Model router built with Jev](https://x.com/ephraimduncan/status/2100454070536351824) — X: demonstrates a request router that asks Jev which model should receive each prompt.
- [Jev as an AI agent safety monitor](https://x.com/isNickMa/status/2100566407524344225) — X: reports using Jev to check agent actions before execution and compares attack catches, false blocks, and latency.
- [Rethinking security engineering with Jev](https://x.com/Kostastsale/status/2100362415187833048) — X: proposes moving bounded security-engineering judgments from chat models to typed Jev decisions.
- [Ask Jev anything, it will judge](https://x.com/waynesutton/status/2100487878992388279) — X: demonstrates a Convex-backed public app that returns Jev judgments rather than generated prose.
- [First Jev use case in a Mac app](https://x.com/malekoo/status/2100439840575684910) — X: describes a shipped Mac application that sends setup and troubleshooting judgments to Jev when no language model is loaded.
- [Jev "playing" Minecraft (r/accelerate)](https://reddit.com/r/accelerate/comments/1whk9oy/new_typesafe_ai_jev_model_playing_minecraft_wip/) — Reddit: shows a work-in-progress Minecraft controller using Jev for fast structured behavior decisions.
- [Jev for instant compaction](https://x.com/tamarajtran/status/2100694549362553153) — X: proposes replacing generated context summaries with Jev relevance decisions over existing conversation material.
- [Reviewing unnecessary tool calls with Jev](https://x.com/altryne/status/2100739055923425589) — X: demonstrates a Claude plugin that asks Jev to flag redundant tool calls after the fact.
- [jev(): a PostgreSQL extension for natural-language queries](https://x.com/iam_zachi/status/2100679300756435135) — X: demonstrates a PostgreSQL `jev()` predicate for natural-language row filtering without a prebuilt search index.
- [A DuckDB extension for row classification](https://x.com/hamiltonulmer/status/2100370557405667768) — X: demonstrates applying Jev to CSV, Parquet, and DuckDB rows and reports timing for a thousand-row classification run.
- [An on-chain trading bot where Jev decides](https://x.com/jarrodwatts/status/2100356151468585346) — X: demonstrates a Monad trading bot that turns live price state into Jev buy/sell decisions and places the resulting orders.
- [Jev broke our WebMCP benchmark](https://x.com/0xidanlevin/status/2100937437325205568) — X: reports a WebMCP benchmark configuration combining Jev with a small text model and compares its task success and model cost with a computer-use baseline.
- [Stagehand plus Jev browser control](https://x.com/kylejeong/status/2100622054945095934) — X: demonstrates browser control by sending an accessibility tree plus candidate actions to Jev for each step.
- [Introducing CUA-S1](https://x.com/trycua/status/2101014004927729737) — X: announces a family of open specialist System One models for computer use, starting with form filling.
- [When a designer gets access to Jev](https://x.com/heystefan_/status/2101369117496521042) — X: demonstrates narrowing a large icon set from a natural-language phrase with Jev and discusses mismatches in the reply thread.
- [LangChain is already using Jev inside its harness](https://x.com/dongxi_nlp/status/2100813094951748074) — X (Chinese): interprets LangChain’s adoption as evidence that Jev fits fixed harness roles such as agent and model routing.
- [Early experimentation using Jev to rethink harness UX](https://www.elvex.com/blog/early-experimentation-using-jev-to-rethink-harness-ux) — Elvex: describes using Jev as a callable harness tool for search, approvals, and context and reports a bulk expense-categorization experiment.
- [jev-experiments](https://github.com/dabit3/jev-experiments) — GitHub: collects 22 latency-focused Jev demos with per-project notes across shell guards, log monitoring, search, reranking, and voice turn-taking.

### Launch & ecosystem signals

- [Jev is now available to everyone, no waitlist](https://x.com/typesafeai/status/2101786156572823624) — X: TypeSafe announces Jev general availability and removal of the waitlist.
- [TypeSafe pauses Jev signups](https://x.com/typesafeai/status/2102281508950307159) — X: TypeSafe reports pausing new Jev signups after general availability to protect service quality.
- [Jev is on Workers AI as typesafe/jev](https://www.reddit.com/r/CloudFlare/comments/1wmjsj2/typesafes_jev_the_decisiononly_model_is_on/) — Reddit: reports Jev availability on Cloudflare Workers AI as `typesafe/jev`.

- [Introducing System One Models and Jev (Hacker News)](https://news.ycombinator.com/item?id=49717558) — Hacker News: launch discussion covering whether typed decisions can replace LLM calls for classification, routing, and verification.
- [Launch thread by Diogo Almeida](https://x.com/CompleteSkeptic/status/2099925682726002904) — X: TypeSafe’s founder introduces Jev and argues for RLCD-trained decision models as a separate path from conversational models.
- [TypeSafe AI releases Jev (r/singularity)](https://reddit.com/r/singularity/comments/1whop6b/typesafe_ai_releases_ai_model_called_jev_rather/) — Reddit: community launch discussion framing Jev around bounded, lower-cost software decisions rather than chat.
- [Jev on OpenRouter](https://x.com/OpenRouter/status/2100744709589316009) — X: announces Jev availability through OpenRouter.
- [Jev on Cloudflare AI Gateway](https://x.com/CloudflareDev/status/2100688880798159254) — X: announces Jev support in Cloudflare AI Gateway for use from Workers and other gateway clients.
- [An internal Jev study session with 50+ engineers](https://x.com/LayerX_tech/status/2100887864594895154) — X (Japanese): shares material from a company-wide Jev study session, providing an early signal of organizational evaluation.
- [Can we have Jev in Devin?](https://reddit.com/r/DevinAI/comments/1wjtmwi/can_we_have_jev_in_devin/) — Reddit: asks for a Jev-style decision layer inside Devin, illustrating user demand for typed decisions in another coding-agent environment.
- [X is all over it, Reddit is not](https://x.com/0xBOYD/status/2100619702003208701) — X: compares Jev discussion volume across platforms and cautions that ecosystem impressions depend strongly on where builders are posting.

### Directories, roundups & field notes

- [Awesome TypeSafe Jev](https://github.com/AbdelStark/awesome-typesafe-jev) — Curated list: source-backed collection of Jev SDKs, live demos, and implementation examples.
- [60 Jev use cases in Chinese](https://x.com/yaojingang/status/2101867443820113982) — X (Chinese): rounds up sixty Jev use cases and organizes them around classification, scoring, and selection.
- [A Jev index rebuilt every four hours](https://x.com/LinearUncle/status/2102423502414618729) — X (Chinese): describes a multilingual index that scrapes X every four hours and reports more than 5,380 Jev-related posts.

- [Awesome Jev by TypeSafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe) — GitHub: curates Jev use cases, patterns, prompts, starter code, and a video walkthrough of eight example projects.
- [19 open-source Jev projects](https://x.com/GoSailGlobal/status/2100859307671855113) — X (Chinese): rounds up 19 early open-source Jev projects and summarizes the kinds of applications appearing after launch.
- [Awesome Jev by 0xLogicrw](https://x.com/0xLogicrw/status/2100478725393686556) — X (Chinese): links a hand-checked Jev project list that later expanded into a larger navigation site.
- [Jev repository roundup (Japanese)](https://x.com/studio_yebisu/status/2100686990090047569) — X (Japanese): surveys practical Jev repositories and highlights computer use and automated trading among the early clusters.
- [Six things I'll still use Jev for](https://x.com/isaac_flath/status/2100623016644223175) — X: records six Jev use cases the author expects to keep after extended hands-on use.
- [All the coolest Jev projects on X](https://x.com/moritzkremb/status/2100895894287839255) — X: curates a launch-window thread of notable Jev builds across several application patterns.
- [I reviewed 287 open-source Jev projects](https://reddit.com/r/LLMDevs/comments/1wko2e5/i_reviewed_287_opensource_jev_projects_here_are/) — Reddit: reports a manual review of 287 Jev repositories and narrows them to a smaller set that clearly explains how the model is used.
- [Made with Jev](https://madewithjev.com) — Directory: indexes Jev builds, guides, and posts and links to several free Jev-powered tools.

