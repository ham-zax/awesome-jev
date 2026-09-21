# Agent & Action Control

Use this category when a Jev decision directly changes an active loop: what to do next, whether to continue, when to escalate, or what context remains available.

## Submission format

```md
- [Name](URL) — Domain: one sentence describing the loop state, Jev decision, and action taken by code.
```

## Entries

### Browser, desktop & software actions

- [jev-social](https://github.com/socai-io/jev-social) — Social media research: asks Jev to choose the next socai CLI operation and target on Instagram, TikTok, or LinkedIn, rejecting malformed or low-confidence choices before execution.
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) — Browser automation: uses Jev to choose the next browser action and target element, invoking a text model only when the step requires generated text.
- [jev-agent-browser](https://github.com/forvela/jev-agent-browser) — Browser agents: runs bounded delegated tasks through a Jev action loop, validates each browser action through agent-browser, and returns ambiguous or stuck states to the parent agent.
- [fastbrowse](https://github.com/agent-labs-dev/fastbrowse) — Browser agents: lets an LLM read and plan while Jev selects the next action from the current page state.
- [Jev Browser](https://github.com/jkudish/jev-browser) — Browser automation: drives browser steps with Jev action selection instead of asking a text-generation model to choose every interaction.
- [public-browser](https://github.com/Silbercue/public-browser) — Browser automation: lets Claude Code and Cursor control an existing Chrome profile through a Jev action loop; the project reports lower token use and cost than its comparison path.
- [BrowserClaw](https://github.com/GoldenLoaf24h/browserclaw) — Browser automation: combines a Jev action loop with a pruned Chrome DOM representation and dispatches the selected interactions through CDP against the active profile.
- [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome) — Browser automation: uses a Jev Choice for each operation/element pair plus separate goal-complete and stuck checks, calling a small text model only for typed text.
- [jev-desktop](https://github.com/yikangy873-gif/jev-desktop) — Computer use: inserts Jev into Codex Computer Use to select among bounded desktop actions at each step.
- [Yappy](https://yappy.biz/jev/) — Computer use: selects one accessibility-tree operation and target per step with Jev, executing only validated high-confidence choices and escalating uncertain or ineffective actions to a full LLM agent.

### Loop & lifecycle control

- [dsh-auto-mode](https://git.allen-software.com/allenh1/dsh-auto-mode) — Coding agents: evaluates unresolved questions at the end of a DeepSeek Harness turn and returns control to the agent only when both the selected choice and autonomy-safety checks clear configured thresholds.
- [wakegate](https://github.com/shitianfang/wakegate) — Long-running agents: asks Jev whether a sleeping agent should wake for a timer or event, while deterministic rules always wake for user messages, bare timers, repeated skips, errors, and timeouts.
- [JevLoop](https://github.com/zjunlp/JevLoop) — Agent runtimes: uses Jev to choose the next tool, score call risk, and decide whether authorization is required, with code enforcing the final action policy.
- [DataJev](https://github.com/zzz1YAO/DataJev) — Data analysis agents: reads compressed analysis state and asks Jev whether to continue, change direction, verify a finding, or stop and synthesize.

### Context control

- [yoshi](https://github.com/compozy/yoshi) — Context management: uses Jev to decide which Claude Code or Codex conversation history is still needed before pruning.
- [pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction) — Context management: keeps conversation text verbatim while Jev removes stale tool history, falling back to Pi summarization only when pruning cannot free enough space.
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Context management: scores Claude Code tool calls and results for continued relevance with Jev and prunes low-value history instead of generating a compaction summary.
- [fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction) — Context management: ports Jev-guided pruning to Codex, preserving selected context verbatim across compaction rather than replacing it with a generated summary.
- [jev-pruner](https://github.com/tamaratran/jev-pruner) — Context management: uses Jev to trim long Bash output before it enters Claude Code’s context window.

### Physical & multimodal control

- [robo-harness](https://github.com/grmkris/robo-harness) — Robotics: selects bounded SO-101 joint movements from typed candidate actions with Jev under an explicit spend budget.
- [jev-canvas](https://github.com/gaborishka/jev-canvas) — Multimodal UI: combines partial voice transcripts and webcam pointing with eight Jev decisions covering command intent, completeness, action, shape, colour, target, placement, and size before code updates a tldraw canvas.

