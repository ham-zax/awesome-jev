# Calibration & Model Research

Use this category for confidence calibration, threshold selection, open Jev-style models, reproduction work, training recipes, and local deployment research.

## Submission format

```md
- [Name](URL) — Research: one sentence describing the model, calibration method, training or deployment approach, and any measured result worth preserving.
```

## Entries

### Calibration & measurement

- [jevcal](https://github.com/abhixhek/jevcal) — Calibration tooling: fits a confidence threshold to a target accuracy on labeled data, checks it on a held-out split, reports remaining escalation traffic, and can fail CI when a model update breaks the locked threshold.
- [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) — Calibration study: evaluates Jev on 900 rule-generated support tickets plus three public benchmarks, publishing raw responses, ECE, a temperature refit, and per-answer-type calibration direction.
- [ASSAY-001](https://github.com/jourdanlabs/assay-001) — Calibration study: pre-registers a Jev calibration and type-safety check on Banking77 and CLINC150, then publishes the split verdict, run logs, and a separate [write-up](https://donttrustme.ai/assay-001.html).
- [jev-acento](https://github.com/marcosmartinez/jev-acento) — Language calibration: runs a pre-registered paired audit over 3,200 human-labeled Spanish items to measure how Spanish `state` and `instructions` affect accuracy and ECE.
- [poorjev](https://github.com/rupeshpoojary9/poorjev) — Local reproduction: implements Jev-style Choice, Score, and probability questions on zero-shot NLI models, then calibrates confidence with temperature scaling and conformal abstention for offline use.

### Open models & reproductions

- [Visual-JEV](https://github.com/jiangxiluning/Visual-Jev) — Open model: adapts a Qwen3.5-4B-based Jev-style model for direct multimodal image input instead of converting visual state to text first.
- [OpenDecision](https://github.com/deepanwadhwa/OpenDecision) — Open alternative: provides a local Jev-style engine for Choice, Noul, and Score questions over structured state and documents.

- [decider](https://github.com/Mapika/decider) — Open model: fine-tunes Qwen3.5-2B into a one-pass typed decision model that emits calibrated probabilities.
- [openjev](https://github.com/zhihz/openjev) — Open research: provides a local Jev-inspired model for bilingual probability questions over context, questions, and candidate answers.
- [Parallel Constrained Decoding (Qwen2.5-1B-RLCD)](https://huggingface.co/spaces/drinkmoonshine/parallel-constrained-decoding) — Open research: demonstrates RLCD-trained parallel constrained decoding on Qwen2.5-1B as an open System One-style alternative.
- [NanoJev](https://github.com/TianyuCodings/NanoJev) — Open model: packages a 0.6B parallel decision model with training code, weights, and data, returning full probability distributions without autoregressive answer generation.
- [open-alternative-jev](https://github.com/ikermoel/open-alternative-jev) — Local model: runs a Jev-shaped decision interface on a user-controlled GPU.
- [mini-jev](https://github.com/r-ms/mini-jev) — Local reproduction: maps Jev’s typed-decision interface onto a local language model.
- [Laya](https://github.com/NandhaKishorM/laya) — Open model: serves Choice, Score, and probability questions with a non-autoregressive RLCD-trained model published on PyPI and Hugging Face.
- [Jev-compatible public API](https://x.com/ekzhang1/status/2100651678110515383) — Open research: exposes a public Jev-shaped API backed by an open Qwen3.6-35B-A3B model for testing the same typed-decision interface.
- [kev](https://github.com/jaredpalmer/kev) — Trainable reproduction: builds a small Jev-like decision model on Qwen2.5-0.5B that can train and run on a MacBook and ships its research runs and evaluation scripts.
- [jev-local](https://github.com/us/jev-local) — Local reproduction: serves a Jev-compatible `POST /v1/systemone` endpoint from open weights and validates drop-in compatibility with the official SDK plus temperature-fitted calibration.
- [LitJev](https://github.com/zhengxuyu/litjev) — Local reproduction: turns Qwen models into a Jev-shaped `/v1/systemone` service for Choice, Score, and probability questions without training or generated answer text.
- [CUA-S1-FORMS](https://huggingface.co/cua-ai/cua-s1-forms) — Specialist model: scores FILL, CHECK, CLICK, and SKIP for form fields in one parallel pass; its authors report 99.7% on their form-filling evaluation versus 83.6% for Jev on the same setup.
- [von](https://github.com/wfzyx/von) — Open model: implements a 395M non-autoregressive System One model for typed questions with calibrated probabilities and reports sub-15 ms inference.
- [minojev](https://github.com/zeredy879/minojev) — Open model: trains a 547k-parameter decision model from scratch on CPU for runtime-defined Choice, Boolean, and Score questions, with committed datasets, predictions, and ECE results.
- [openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) — Open model: publishes a calibrated 151M non-autoregressive decision engine and its test suite; the repository reports stronger benchmark results than both TypeSafe Jev and Laya.

### Training & deployment tooling

- [jevlike](https://github.com/vinnylarouge/jevlike) — Training library: trains compact models that score a changing list of text options and return one probability per option in a single pass.
- [jevbetter](https://github.com/olanotolu/jevbetter) — Model architecture: extends the one-pass option scorer with hashed n-gram encoding, rival-aware attention, and gated prediction heads.
- [jevlike-esp32](https://github.com/david-cermak/jevlike-esp32) — Edge deployment: exports a jevlike scorer to ESP32 firmware with a C inference path and host-side verification.
- [JevForge](https://github.com/zwliJay/jev-forge) — Training stack: combines auditable data construction, Qwen3.5-0.8B training, fixed Mind2Web/OOD evaluation, local serving, and a preliminary RLCD baseline.
- [Luce](https://github.com/scienthoon/luce) — Training recipe: turns a natural-language decision task into teacher-generated data, then trains a LoRA plus decision head on Qwen3-4B-Base and reports accuracy/ECE alongside Jev on matched test items.
- [laya-mlx](https://github.com/mizorewww/laya-mlx) — Local runtime: ports Laya checkpoints to MLX for Apple Silicon and reports single-digit to low-teens millisecond end-to-end decision latency without PyTorch or a cloud API.

### Experiments

- [jevinci](https://github.com/achimala/jevinci) — Creative experiment: asks Jev to predict image pixel colours in parallel and uses confidence to control rendered stroke width.

