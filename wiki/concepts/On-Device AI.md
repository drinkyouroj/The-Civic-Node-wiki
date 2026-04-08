---
title: "On-Device AI"
type: concept
tags: [technology, ai, privacy, hardware]
created: 2026-04-08
updated: 2026-04-08
sources: 2
---

## Definition

On-device AI (also called local AI or local LLM inference) is the practice of running AI models directly on personal or on-premises hardware rather than sending data to a cloud provider's API. The defining characteristic is that data never leaves the device. As of early 2026, this is viable at frontier scale on consumer hardware — a 512GB Apple Silicon Mac can run DeepSeek R1 (671B parameters) at Q4 quantization locally.

## Why It Matters for the Newsletter

Three converging stories make on-device AI analytically important:

1. **Privacy as competitive moat**: Legal, medical, financial, and journalistic use cases where data confidentiality is legally or professionally required can now run frontier-capable models without cloud exposure. This wasn't true before 2025.
2. **AI Sovereignty at the individual level**: [[AI Sovereignty]] has been framed primarily as a nation-state concern (who controls the compute infrastructure). On-device AI extends the sovereignty frame down to the individual user and the small team. You don't need to trust OpenAI, Anthropic, or any government with your queries.
3. **Economics of inference**: API costs at scale are significant. A team running heavy LLM workloads can amortize a $14–16k Mac Studio against annual API costs in months. The "build vs. buy" calculus for AI inference shifted materially in 2025–2026.

## How It Works

Local LLM inference depends on three variables:

- **Model size**: measured in billions of parameters (7B, 14B, 70B, 671B)
- **Quantization**: the compression technique that reduces memory footprint at the cost of some accuracy. Q4 (4-bit) is the practical standard — reduces RAM requirement by ~4x vs. FP16 (16-bit). Q8 and FP16 are higher quality but require more RAM.
- **Hardware memory**: Apple Silicon's unified memory (CPU and GPU share one pool) is structurally advantaged — no PCIe bottleneck copying weights between system RAM and VRAM. This gives Macs a meaningful inference throughput advantage over comparably-priced PC hardware.

**The 60% Rule**: model weights should not exceed 60% of available RAM. The remaining headroom is consumed by macOS overhead and the KV Cache (which stores context and grows with conversation length).

**Practical runtime**: [[Ollama]] is the lowest-friction tool — one command downloads, converts, and optimizes a model for Apple Silicon.

## RAM Tier Benchmarks (as of early 2026)

| RAM | Practical ceiling | Example models |
|---|---|---|
| 8GB | ~3.8B (Q4) | Phi-4 Mini, Gemma 2B |
| 16–18GB | ~14B (Q4) | Qwen2.5-14B, Llama 3 8B |
| 24–36GB | ~32B (Q4) or ~14B (Q8) | Qwen3-Coder 32B, Mixtral 8x7B |
| 48–64GB | ~70B (Q4) | Llama 3.1 70B, DeepSeek Coder 67B |
| 96–128GB | ~105B (Q4) or 70B (FP16) | Command R+ 104B |
| 256–512GB | 405B (Q4) or 671B (Q4) | Llama 3.1 405B, DeepSeek R1 671B |

## Tensions & Counterarguments

- **Quality vs. convenience trade-off**: Q4 quantization degrades model quality vs. API-served FP16/BF16. For most tasks the gap is unnoticeable; for precision reasoning tasks it matters.
- **Maintenance overhead**: Running local models means managing updates, storage, and version compatibility — costs that API providers absorb.
- **The 60% rule bites**: Long conversations exhaust KV Cache headroom. Cloud APIs have effectively unlimited context; local inference has a hard RAM ceiling.
- **Speed ceiling**: Tokens per second on even high-end Apple Silicon (40–70 tok/s for 70B models) is slower than GPU cluster inference. Acceptable for most uses; constraining for latency-sensitive applications.

## Related Concepts

- [[AI Sovereignty]] — on-device AI as the individual/team-level expression of AI sovereignty
- [[Quantization]] — the compression technique that makes on-device frontier models viable
- [[Tech-State Conflict]] — data sovereignty questions that motivate local inference in regulated industries
- [[Surveillance Capitalism]] — on-device AI as a structural escape from data-extraction business models

## Key Sources

- [[Best Local LLMs for Every Apple Silicon Mac — 2025 Guide]] — foundational reference; unified memory explainer, Q4 quantization, Ollama setup
- [[Best Local LLMs for Every Apple Silicon Mac — 2026 Guide]] — updated with frontier models (DeepSeek R1, Phi-4 Mini, Qwen3); adds 60% rule, Flash Attention, thermal management

## Open Questions

- At what point does on-device inference quality become indistinguishable from cloud inference for professional use cases?
- How does Apple's Neural Engine roadmap (M5, M6) extend the frontier accessible on consumer hardware?
- Does the local inference movement fragment the AI ecosystem (different users running different model versions) in ways that matter for interoperability?
- What happens to API providers (OpenAI, Anthropic) if the on-device quality gap closes? Is local inference an existential threat or a niche?
