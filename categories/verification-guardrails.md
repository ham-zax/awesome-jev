# Verification & Guardrails

Use this category when Jev verifies evidence, checks a rule, or gates an action or output before it proceeds.

## Submission format

```md
- [Name](URL) — Domain: one sentence describing what Jev checks, the gate or threshold, and the resulting action.
```

## Entries

### Agent permissions & execution gates

- [pi-jev](https://github.com/y0usaf/pi-jev) — Agent safety: checks potentially risky Pi tool calls with Jev before allowing execution.
- [jev-guard](https://github.com/leepokai/jev-guard) — Agent security: screens prompts and proposed actions for Claude Code, Codex, Pi, and ACP agents, using Jev to decide when to block.
- [opencompany](https://github.com/useopencompany/opencompany) — Agent workspace: routes workspace approvals through a typed Jev review before actions proceed.
- [fx](https://github.com/vercel-labs/fx) — Coding agents: provides a `typesafe_permission_reviewer` so permission decisions can be made by Jev instead of a text-generation model.
- [pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) — Agent safety: checks each side-effecting Pi tool call against the user’s stated request before execution.
- [jev-axi](https://github.com/shiftynick/jev-axi) — Agent safety: scores shell commands for destructiveness, exfiltration, remote execution, and security weakening, while handling routine commands locally and sending ambiguous cases to Jev.
- [pi-verdict](https://github.com/jesset/pi-verdict) — Agent safety: combines deterministic rules with a Jev `allow / ask / deny` Choice for gray-zone tool calls, escalating `ask` to the user and denying on errors or timeouts.
- [hermes-jev-approvals](https://github.com/anpicasso/hermes-jev-approvals) — Agent approvals: places Jev in front of Hermes Agent command approvals; the project reports 8.7× faster decisions and 4.4× fewer user prompts in its proof of concept.
- [jev-engineering](https://github.com/eugeniughelbur/jev-engineering) — Agent safety: applies deterministic rules first, then a typed Jev check for remaining tool calls, and publishes a rerunnable 300-call injection evaluation of the gate.
- [Reflex](https://github.com/kaustav1996/reflex) — Coding agents: checks each state-changing Pi tool call with five Jev risk questions plus a risk Score, then maps the result to allow, ask, or block under user-configured policy.

### Code, change & completion verification

- [is-malicious](https://github.com/luantak/is-malicious) — Software supply-chain security: asks Jev whether source and build-file chunks look malicious, escalates suspicious chunks for a second pass, and reports implicated files and lines before execution.
- [jev-review](https://github.com/devagrawal09/jev-review) — Software engineering: runs code changes through staged Jev review gates before they advance in the workflow.
- [OpenWork](https://github.com/different-ai/openwork) — Engineering workflow: uses Jev as a typed verification judge in its eval testkit so agent-produced work can be gated without a free-form reviewer.
- [Foreman](https://github.com/thruwire/foreman) — Software factories: asks Jev whether a Codex worker’s implementation is complete, whether its tests are sufficient, and whether human review is required.
- [stanley-code](https://github.com/devagrawal09/stanley-code) — Coding agents: routes a natural-language code-check request to a bounded workflow, gathers limited evidence, asks fixed-choice Jev questions, and lets deterministic code apply the thresholds and produce the findings.
- [jev-git](https://github.com/AkashPriyadarshii/jev-git) — Developer tooling: screens staged diffs for secrets and destructive commands with Jev in pre-commit and pre-push hooks.
- [Hunch](https://github.com/Kelbie/hunch) — Code review: evaluates plain-English project rules against code with Jev and assigns one label to each finding.
- [Abide](https://github.com/coldteadotai/abide) — Agent supervision: checks every coding-agent edit for rule violations with Jev and records the flagged edits for human review.
- [jev-pref](https://github.com/doeixd/jev-pref) — Code review: turns preferences from `AGENTS.md` into rules that Jev evaluates against diff hunks, staged files, or pull requests, separating blocking `fix_now` findings from advisory ones.
- [jev-commit](https://github.com/valentynkit/jev-commit) — Git tooling: checks whether a commit message matches the staged diff, flags debug leftovers and unmentioned work, and blocks only when a credential is detected.
- [Blink](https://blink.review) — Code review: gives coding agents a CLI that runs a Jev diff check after changes instead of invoking a text-model reviewer.
- [jev-harness](https://github.com/ismaelsoilet/jev-harness) — Coding agents: combines typed Jev decisions with deterministic control logic to gate execution, triage failures, and stop repeated circular attempts.
- [limpet](https://github.com/noplan-inc/limpet) — Coding agents: uses Jev in a Stop hook to check plain-language completion rules before an agent is allowed to finish.
- [jev-belay](https://github.com/valentynkit/jev-belay) — Coding agents: runs a four-question Jev completion check only when files changed without a later passing verification, and fails open if the check itself errors.

### Content & quality checks

- [Sniff Test](https://github.com/DanRWilloughby/snifftest) — Writing quality: evaluates each paragraph against ten Boolean style rules at a 0.7 threshold, with CLI, pre-commit, GitHub Action, and Claude Code integrations.
- [taste-lint](https://github.com/mblode/taste-lint) — UI and writing quality: applies Jev probabilities to semantic style rules for interface copy, prose, and agent instructions while keeping measurable rules local and allowing active findings to fail a run.
