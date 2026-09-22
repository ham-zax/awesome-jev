# Content Filtering & Moderation

Use this category when Jev filters or moderates user-facing content for abuse, profanity, spoilers, or other policy-defined conditions.

## Submission format

```md
- [Name](URL) — Domain: one sentence describing the content, Jev policy decision, threshold, and moderation action.
```

## Entries

- [jev_antispam_bot](https://github.com/backmeupplz/jev_antispam_bot) — Telegram moderation: checks each message with Jev and routes likely spam into the bot’s moderation path.
- [jev-slop-guard](https://github.com/davertor/jev-slop-guard) — Social feed filtering: classifies X and LinkedIn posts as `slop` or `not_slop`, blurring posts above a user-set threshold while preserving a manual reveal override.

- [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) — Community moderation: scores Discord messages for phishing, spam, and social-engineering signals with Jev and feeds the result into a four-stage escalation policy, while pardoned messages become verified-safe precedent.
- [mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation) — AI assistants: combines a Jev block/no-block decision with a category Choice, aborts the turn at a configured threshold, and fails open behind a deadline and circuit breaker.
- [profanity-checker](https://github.com/4rays/profanity-checker) — Trust and safety: checks text and usernames for literal profanity and disguised variants with two Jev probability questions, then applies the configured threshold in a Cloudflare Worker.

