# Agent & Action Control

Use this category when a Jev decision directly changes an active loop: what to do next, whether to continue, when to escalate, or what context remains available.

## Submission format

```md
- [Name](URL) — Domain: one sentence describing the loop state, Jev decision, and action taken by code.
```

## Entries

### Browser, desktop & software actions

- [jev-mobile](https://github.com/Friedjof/jev-mobile) — Mobile control: uses Jev inside a structured Android control loop alongside Mobile MCP to choose each bounded action.
- [GUI JEV Harness](https://github.com/ZihuaEvan/GUI_JEV) — Computer use: recursively selects screenshot grid regions with Jev Choice questions, using local probability and margin gates to descend or refuse without clicking.

- [jev-social](https://github.com/socai-io/jev-social) — Social media research: asks Jev to choose the next socai CLI operation and target on Instagram, TikTok, or LinkedIn, rejecting malformed or low-confidence choices before execution.
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) — Browser automation: uses Jev to choose the next browser action and target element, invoking a text model only when the step requires generated text.
- [jev-agent-browser](https://github.com/forvela/jev-agent-browser) — Browser agents: runs bounded delegated tasks through a Jev action loop, validates each browser action through agent-browser, and returns ambiguous or stuck states to the parent agent.
- [fastbrowse](https://github.com/agent-labs-dev/fastbrowse) — Browser agents: lets an LLM read and plan while Jev selects the next action from the current page state.
- [Jev Browser](https://github.com/jkudish/jev-browser) — Browser automation: drives browser steps with Jev action selection instead of asking a text-generation model to choose every interaction.
- [BrowserClaw](https://github.com/GoldenLoaf24h/browserclaw) — Browser automation: combines a Jev action loop with a pruned Chrome DOM representation and dispatches the selected interactions through CDP against the active profile.
- [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome) — Browser automation: uses a Jev Choice for each operation/element pair plus separate goal-complete and stuck checks, calling a small text model only for typed text.
- [Yappy](https://yappy.biz/jev/) — Computer use: selects one accessibility-tree operation and target per step with Jev, executing only validated high-confidence choices and escalating uncertain or ineffective actions to a full LLM agent.

### Loop & lifecycle control

- [JevLoop](https://github.com/parkavenue9639/jevloop) — Agent runtimes: selects tools and targets with Jev Choice decisions, escalating uncertain steps to an LLM while a shared kernel enforces isolated execution.

- [dsh-auto-mode](https://git.allen-software.com/allenh1/dsh-auto-mode) — Coding agents: evaluates unresolved questions at the end of a DeepSeek Harness turn and returns control to the agent only when both the selected choice and autonomy-safety checks clear configured thresholds.
- [wakegate](https://github.com/shitianfang/wakegate) — Long-running agents: asks Jev whether a sleeping agent should wake for a timer or event, while deterministic rules always wake for user messages, bare timers, repeated skips, errors, and timeouts.
- [JevLoop](https://github.com/zjunlp/JevLoop) — Agent runtimes: uses Jev to choose the next tool, score call risk, and decide whether authorization is required, with code enforcing the final action policy.
- [DataJev](https://github.com/zzz1YAO/DataJev) — Data analysis agents: reads compressed analysis state and asks Jev whether to continue, change direction, verify a finding, or stop and synthesize.

### Context control

- [jev-compaction](https://github.com/Waxmell114514/jev-compaction) — Context management: scores transcript segments with Jev, keeping selected lines verbatim and moving low-scoring material behind expandable pointers instead of deleting it.


### Physical & multimodal control

- [robo-harness](https://github.com/grmkris/robo-harness) — Robotics: selects bounded SO-101 joint movements from typed candidate actions with Jev under an explicit spend budget.

