---
title: "The political preferences of LLMs"
type: source
tags: [ai, technology, politics, research]
created: 2026-04-19
updated: 2026-04-19
sources: 16
raw: "raw/The political preferences of LLMs.md"
source_url: "https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0306621"
author: "David Rozado"
published: 2024-07-31
---

[Original source](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0306621)

## Summary
PLOS ONE peer-reviewed paper administering 11 political orientation tests to 24 state-of-the-art conversational LLMs (GPT-3.5, GPT-4, Gemini, Claude, Grok, Llama 2, Mistral, Qwen series). Finding: conversational LLMs consistently score left-of-center across most tests; base (pre-SFT) foundation models cluster near the center or produce incoherent responses. Paper also demonstrates that supervised fine-tuning (SFT) on modestly sized politically-aligned datasets can steer LLMs toward left, right, or depolarizing targets — showing political orientation is a tunable post-training artifact.

## Key Points
- 2,640 tests administered (11 tests × 10 trials × 24 conversational models).
- Political Compass Test: economic axis μ=−3.69, social axis μ=−4.19 (both strongly left).
- Effect size consistent across test instruments; Nolan Test is the only outlier (classifies as centrist).
- Base models (GPT-3 and Llama 2 foundation checkpoints) score near neutral but with high invalid-response rates (~42%).
- Author built LeftWingGPT, RightWingGPT, DepolarizingGPT via OpenAI SFT API with ~30K snippets each — all successfully moved into their target regions.
- Author cannot conclusively determine whether left-lean comes from pretraining corpus or post-training RLHF/SFT.
- Hypothesis: ChatGPT-generated synthetic data used downstream by other labs may have propagated ChatGPT's lean.
- Paper flags selection bias / answer-order vulnerability but argues multi-test design controls for it.
- Funding: Institute for Cultural Evolution (think tank) — flagged as potential conflict.

## Newsletter Angles
- The SFT-as-political-dial finding is the story: political orientation is not emergent, it's trainable with modest data. This changes how we should think about LLM bias audits.
- ICE (Institute for Cultural Evolution) funded this paper and is building DepolarizingGPT — that is itself a politically interested intervention worth examining. Author notes the conflict, doesn't resolve it.
- The "Wikipedia-replacement" framing: if LLMs are displacing neutral-pretense information sources, then consistent tilt across vendors matters politically even if the tilt is modest.
- Connects to [[censorship]] and [[technology]] threads when paired with KOSA/age-verification reporting — platforms are being pressed to moderate content while the underlying AI tools have their own directional priors.

## Entities Mentioned
- David Rozado (author)
- [[OpenAI]] — GPT-3.5, GPT-4
- [[Anthropic]] — Claude
- [[Google]] — Gemini
- [[xAI]] / Twitter — Grok
- [[Meta]] — Llama 2
- [[Mistral AI]]
- [[Alibaba]] — Qwen
- [[Institute for Cultural Evolution]] — funder, Steve McIntosh
- [[LMSYS Chatbot Arena Leaderboard]]
- [[Allsides]] — media bias labels used for fine-tuning data

## Concepts Mentioned
- [[LLM political bias]]
- [[Supervised Fine-Tuning]] (SFT)
- [[Reinforcement Learning from Human Feedback]] (RLHF)
- [[Base model vs. conversational model]]
- [[Political orientation tests]]
- [[Synthetic training data]]

## Quotes
> "When probed with questions/statements with political connotations, most conversational LLMs tend to generate responses that are diagnosed by most political test instruments as manifesting preferences for left-of-center viewpoints."

> "[LLMs] are starting to partially displace these conventional sources. This shift in information sourcing has profound societal implications."

## Notes
Peer-reviewed, methodology fully documented, data available on Zenodo. ICE funding disclosed but the author also built DepolarizingGPT for ICE — reader should note potential motivated framing around "depolarization" as the normative endpoint. Useful as a data point rather than a definitive causal finding. Note this is a substantively different topic from the rest of this ingest batch (LLM bias rather than internet bills); file under "technology / ai" rather than the KOSA cluster.
