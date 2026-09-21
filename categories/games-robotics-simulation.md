# Games, Robotics & Simulation

Use this category for Jev decisions inside games, embodied-control experiments, robotics simulations, and other interactive environments where the domain is the clearest browsing signal.

## Submission format

```md
- [Name](URL) — Domain: one sentence describing the environment state, Jev decision, and how the simulator or game applies it.
```

## Entries

### Games & puzzles

- [typesafe-mario](https://github.com/fhshaik/typesafe-mario) — Gaming: reads structured Super Mario Bros. emulator state and uses Jev to choose each action from emulator-derived features.
- [tsai-sc](https://github.com/phyous/tsai-sc) — Gaming: controls original StarCraft shareware through keyboard and mouse while recording Jev action probabilities for each decision.
- [jev-plays-pokemon](https://github.com/milanboers/jev-plays-pokemon) — Gaming: turns Pokémon Red state into typed Jev questions each turn and lets deterministic code translate the answers into moves.
- [PlayJev](https://github.com/OmniJev/PlayJev) — Gaming research: uses an open 0.8B vision-language decision model to score the legal moves shown in a game frame, passing low-confidence steps to search across ten browser games.
- [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) — Gaming: keeps route planning and arithmetic deterministic while Jev handles branch decisions in Pokémon Red and scores battle faint predictions against emulator RAM state.
- [Soupbase](https://github.com/spoonnotfound/soupbase) — Puzzle solving: uses Jev Choices to answer lateral-thinking questions and assess proposed solutions, with code requiring factual support, explanation quality, and sufficient confidence before marking a puzzle solved.
- [jev-torneo-animales](https://github.com/hectorlcastro09/jev-torneo-animales) — Gaming: runs a winner-stays-on animal tournament where Jev chooses each matchup winner under land, water, or air rules, batching speculative challenger decisions and discarding unused answers after an upset.
- [2048 × Jev](https://github.com/ARCJ137442/jev-2048) — Gaming: asks Jev to choose among four legal 2048 directions each turn and pauses for human review when confidence falls below the user’s threshold.

### Robotics & autonomy

- [jev-drone](https://github.com/RomanSlack/jev-drone) — Robotics simulation: places a Jev decision model in the camera-only MuJoCo drone control loop at 2.5 Hz.
- [typesafe-jev-drone-demo](https://github.com/kxzk/typesafe-jev-drone-demo) — Simulation: uses a Python Jev backend to choose navigation decisions for a drone rendered in Three.js.
- [jev-reflex-autonomy-lab](https://github.com/khordoo/jev-reflex-autonomy-lab) — Drone autonomy: gives Jev the fast reflex layer for multiple simulated drones while an optional slower strategy layer supplies higher-level guidance.
- [RoboJEV](https://github.com/lykycy123/RoboJEV) — Robotics simulation: uses two Jev Choice stages over structured state to select intent and Cartesian/gripper commands for a Franka Panda in MuJoCo, while physics independently checks task success.

### Interactive simulations

- [typesafe-playground](https://github.com/kavehmz/typesafe-playground) — Interactive demos: collects small Jev experiments that expose the decision process directly, from support-message routing to steering a car in a 3D scene.
- [Jevtown](https://github.com/gaborishka/jevtown) — Audience simulation: scores a post against thousands of deterministic personas with batched Jev questions, applies moderation gates, and expands to larger reaction waves only while the previous wave remains net-positive.

