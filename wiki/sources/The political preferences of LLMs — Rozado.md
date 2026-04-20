---
title: "The political preferences of LLMs"
type: source
tags: [ai, technology, politics, foundational]
created: 2026-04-19
updated: 2026-04-19
sources: 15
raw: "raw/The political preferences of LLMs.md"
source_url: "https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0306621"
author: "David Rozado"
published: 2024-07-31
---

[Original source](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0306621)

## Summary
PLOS ONE peer-reviewed study (Rozado, July 2024) administering 11 political-orientation tests to 24 state-of-the-art conversational LLMs (closed and open source: GPT-3.5, GPT-4, Gemini, Claude, Grok, Llama 2, Mistral, Qwen) across 2,640 test administrations. **Finding:** Most conversational LLMs produce responses diagnosed as left-of-center across most tests. Five base/foundation models tested separately produce near-center results (though base models often answer incoherently, complicating interpretation). The bias appears post-pretraining — i.e., introduced (or amplified) by SFT/RLHF. Rozado then demonstrates that fine-tuning with ~7-17M tokens of politically-labeled data can move a model anywhere in the political spectrum (LeftWingGPT, RightWingGPT, DepolarizingGPT).

## Key Points
- **24 conversational LLMs, 11 tests, 2,640 total administrations.** Stance detection automated via gpt-3.5-turbo with 93% human-rater agreement (κ=0.91) on conversational models.
- **Political Compass Test:** mean −3.69 economic, −4.19 social. Effect sizes large (d ≈ −2.0 to −2.6).
- **Eysenck's Political Test:** Models lean Social Democrat / tender-minded.
- **iSideWith (US):** Models cluster with Democratic and Green parties; significantly distant from Libertarian and Republican parties.
- **Nolan Test outlier:** Diagnoses LLMs as politically moderate — only test that disagrees. Methodological flag.
- **Base models:** GPT-3 series, Llama 2 series — when prompted with prefixes/suffixes to nudge them into selecting allowed answers, results cluster near political center, indistinguishable from random selection. **Caveat:** Base models often produce incoherent answers; only 56% human-stance-detector agreement (κ=0.41).
- **Fine-tuning experiment:** With 14K-34K text snippets (7-17M tokens), Rozado moved gpt-3.5-turbo to LeftWingGPT, RightWingGPT, DepolarizingGPT positions. Demonstrates that political alignment is highly malleable post-pretraining.
- **Implications section:** Rozado argues this matters because LLMs are "starting to partially displace" search engines and Wikipedia as primary information sources — political bias becomes a public-information distribution issue.
- **Hypothesis (unconfirmed):** ChatGPT-generated synthetic data used in others' fine-tuning may have propagated original ChatGPT left-lean across the field.
- **Funding:** Institute for Cultural Evolution; Steve McIntosh consulted on the DepolarizingGPT data — disclosed as conflict-of-interest.

## Newsletter Angles
- **AI / Politics:** Direct evidence that conversational AI models, regardless of producer, share a measurable political tilt — a fact-based foundation for any piece on AI as a political-information infrastructure.
- **Editorial hook:** "Twenty-four LLMs from a dozen organizations. Eleven tests. One direction." The cross-model homogeneity is the story — it's not OpenAI-specific or Anthropic-specific.
- **Pairs unexpectedly with the [[Bad Internet Bills]] cluster:** When LLMs become primary information sources, the same questions about platform political tilt that drive KOSA (right-wing concerns about LGBTQ+ content in feeds) translate directly to AI alignment. The political fight over content moderation is about to become the political fight over LLM RLHF.
- **Skepticism flag:** Rozado is funded by Institute for Cultural Evolution, a think tank with its own political project (DepolarizingGPT). The methodology is solid; the framing of "LLMs as ideologically captured" carries motivated framing. Worth citing the data, contextualizing the politics.

## Entities Mentioned
- [[David Rozado]] — author
- [[Institute for Cultural Evolution]] — funder; conflict disclosed
- [[Steve McIntosh]] — ICE think tank; *Developmental Politics* author
- [[OpenAI]] — GPT-3.5, GPT-4 tested
- [[Anthropic]] — Claude tested
- [[Google]] — Gemini tested
- [[xAI]] / [[Twitter]] — Grok tested
- [[Meta]] — Llama 2 tested
- [[Mistral AI]] — tested
- [[Alibaba]] — Qwen tested

## Concepts Mentioned
- [[LLM Political Bias]]
- [[RLHF]] — Reinforcement Learning from Human Feedback
- [[Supervised Fine-Tuning (SFT)]]
- [[AI Alignment]]
- [[Information Source Displacement]] — LLMs replacing search/Wikipedia

## Quotes
> "When probed with questions/statements with political connotations, most conversational LLMs tend to generate responses that are diagnosed by most political test instruments as manifesting preferences for left-of-center viewpoints."

> "If political biases are being introduced in LLMs post-pretraining, the consistent political leanings observed in our analysis for conversational LLMs may be an unintentional byproduct of annotators' instructions or dominant cultural norms and behaviors."

## Notes
Peer-reviewed (PLOS ONE), July 2024. Methodology is sound: 11 instruments, 10 retakes per model, automated + human-validated stance detection, coefficient-of-variation analysis.

**Funding caveat:** Rozado's broader research program (DepolarizingGPT, Manhattan Institute commentary, etc.) has a clear right-of-center political project. The empirical findings here are independently verifiable; the *interpretation* (LLMs as politically captured by progressive cultural elites) is a framing choice. Any newsletter use should distinguish data from frame.

Cited as a foundational reference for the AI-as-political-infrastructure question. Connects to the broader "information source as power" thread running through this wiki ([[Algorithmic Influence and Media Legitimacy]], [[A systematic review of echo chamber research]], etc.).
