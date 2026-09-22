# Adaptive & Realtime UI

Use this category when Jev directly changes what a user sees or can do in a live interface, and the interface itself is the clearest way to browse the project.

## Submission format

```md
- [Name](URL) — Domain: one sentence describing the live UI state, Jev decision, and visible interaction change.
```

## Entries

### Browser & feed adaptation

- [Tab Sorter](https://github.com/AstonyCat/jev-tab-grouper) — Browser tooling: groups Chrome tabs by user-defined criteria with one Jev Choice per tab, preserving manual groups and sending unmatched tabs to a fixed fallback bucket.
- [Feed Lens](https://github.com/SkywalkerDarren/feed-lens) — Social media: annotates Weibo, Threads, and X posts in a Chrome extension using Jev judgments against user-defined topic and expression labels.
- [unclutter](https://github.com/kitze/unclutter) — Browser tooling: classifies page elements as clutter with Jev and removes matches under reusable template rules.
- [typesafe-adblock](https://github.com/realZachi/typesafe-adblock) — Browser tooling: evaluates DOM elements with Jev to decide which ones should be treated as ads and removed.
- [sift](https://github.com/bohutang/sift) — Social feeds: classifies X posts into substance, humour, chit-chat, promotion, junk, or AI-written content with Jev.
- [PlotVeil](https://github.com/Dearest/plotveil) — Spoiler protection: evaluates YouTube comments for concrete plot revelations with Jev, keeps uncertain comments covered, and applies stricter thresholds to protected titles.

### Generated & interactive interfaces

- [json-render](https://github.com/vercel-labs/json-render) — Generative UI: uses Jev in the compose path to select which components and actions should appear in a generated interface.
- [jev-canvas](https://github.com/gaborishka/jev-canvas) — Multimodal UI: combines partial voice transcripts and webcam pointing with eight Jev decisions before code updates a tldraw canvas.
- [DWIM](https://github.com/rohit9mehta/dwim) — Desktop productivity: scores the frontmost macOS app’s menu items against a plain-language command and executes the top safe match when it clears a threshold.
- [SemanticSpace](https://semanticspace.dev/) — Semantic mapping: places phrases in two dimensions by using their Jev relationship scores to two user-selected concepts as coordinates.
