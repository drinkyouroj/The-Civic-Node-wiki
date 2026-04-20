---
title: "LLM Political Bias"
type: concept
tags: [ai, technology, politics]
created: 2026-04-19
updated: 2026-04-19
sources: 7
---

## Definition
**LLM political bias** refers to the systematic political-orientation tilt observable in the responses of conversational large language models (LLMs) to politically-charged questions. Per [[The political preferences of LLMs — Rozado]] (PLOS ONE, 2024), most state-of-the-art conversational LLMs across providers (OpenAI, Anthropic, Google, xAI, Meta, Mistral, Alibaba) generate responses diagnosed as left-of-center across most political-orientation test instruments. The bias appears post-pretraining — base/foundation models tested separately produce near-center results — and is highly malleable via supervised fine-tuning (SFT) with relatively small amounts (~7-17M tokens) of politically-aligned data.

## Why It Matters for the Newsletter
As LLMs become primary information sources — partially displacing search and Wikipedia — the political tilt of conversational AI becomes a **public information distribution issue** comparable to social-media algorithm bias. Connects directly to the broader Politics / Power / Technology themes: who decides what the default political voice of AI systems is, and how does the answer shift when those systems are deployed in education, customer service, government, and media production?

Crosses unexpectedly with the [[Bad Internet Bills Campaign]] cluster: when LLMs are part of the information layer, the same fights about content moderation political tilt translate directly into fights about LLM RLHF/SFT alignment. The political project that wants to suppress LGBTQ+ content on social platforms via [[KOSA]] is the same project that will (or already does) want to constrain LLM outputs.

## Evidence & Examples
- **Cross-provider homogeneity:** Rozado tested 24 models from ~12 organizations; results were strikingly similar — left of economic center (μ ≈ −3.69 on Political Compass), left of social center (μ ≈ −4.19), Social Democrat / tender-minded on Eysenck. Effect sizes large (d ≈ −2.0 to −2.6).
- **Base models cluster near center:** GPT-3 and Llama 2 base/foundation models — when nudged to select allowed answers — produce results indistinguishable from random selection. Caveats: base models often answer incoherently (only 56% human-rater stance-detection agreement, κ=0.41).
- **Malleability via SFT:** Rozado moved gpt-3.5-turbo to LeftWingGPT, RightWingGPT, DepolarizingGPT positions with 14K-34K text snippets (7-17M tokens) — modest fine-tuning corpus.
- **One outlier instrument:** Nolan Test consistently diagnoses LLMs as politically moderate; flagged as methodological anomaly.
- **Hypothesis (unconfirmed):** ChatGPT-generated synthetic data used in others' fine-tuning may have propagated original ChatGPT left-lean across the field.

## Tensions & Counterarguments
- **Methodological pushback:** Some researchers (Röttger et al., cited in Rozado) argue political-orientation tests are not valid LLM evaluations — the constrained multiple-choice format and response variability make the results "spinning arrow" rather than diagnostic. Rozado's response: 8% coefficient of variation across retakes shows the "arrow" points consistently in one direction.
- **Selection bias in multiple-choice answers:** LLMs have documented preference for certain answer IDs (e.g., "Option A"). Rozado argues the use of multiple test instruments mitigates this confound.
- **Funding caveat:** Rozado's research is funded by the Institute for Cultural Evolution; the broader research program (DepolarizingGPT, Manhattan Institute commentary) has a clear right-of-center political project. The empirical findings here are independently verifiable; the *interpretation* (LLMs as politically captured by progressive cultural elites) is a framing choice. Worth distinguishing data from frame in any newsletter use.
- **Causation vs correlation:** Rozado cannot conclusively determine whether the bias originates in pretraining corpora (with SFT/RLHF making it visible) or in the SFT/RLHF process itself.

## Related Concepts
- [[RLHF]] — Reinforcement Learning from Human Feedback
- [[Supervised Fine-Tuning (SFT)]]
- [[AI Alignment]]
- [[Algorithmic Influence and Media Legitimacy]]
- [[Information Source Displacement]] — LLMs replacing search/Wikipedia
- [[Surveillance Capitalism]]

## Key Sources
- [[The political preferences of LLMs — Rozado]] — primary peer-reviewed source
