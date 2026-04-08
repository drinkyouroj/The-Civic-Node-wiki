---
title: "The Best Local LLMs To Run On Every Mac (Apple Silicon)"
source: "https://apxml.com/posts/best-local-llm-apple-silicon-mac"
author:
  - "[[Ryan A. on Jul 4]]"
  - "[[2025Guest Author]]"
published:
created: 2026-04-08
description: "List of the best local LLMs for Apple Silicon Macs, optimized for your specific RAM configuration."
tags:
  - "clippings"
---
Running large language models (LLMs) on your local machine is a game-changer. It offers unparalleled privacy, eliminates API costs, and gives you the freedom to experiment without limits. For developers with Apple Silicon Macs, the unified memory architecture provides a unique advantage in efficiently running these powerful AI models.

This guide provides a definitive breakdown of the best LLMs you can run on your specific Mac, from the M1 to the latest M4. We'll look at how your Mac's RAM is the single most important factor and provide you with concrete recommendations to get started immediately.

Note: For the most up-to-date reference, view the [LLM Directory](https://apxml.com/models?modelType=open_weight&selectedGpu=m3_pro_18&runType=inference&quantization=fp16&numGpus=1) and filter by your hardware.

## LLMs and Your Mac's Memory

The ability of your Apple Silicon Mac to run an LLM comes down to one thing: **Unified Memory (RAM)**. Unlike traditional PCs, where the CPU and GPU have separate memory pools, Apple Silicon shares one pool across all components. This is incredibly efficient for AI because the model's weights don't need to be copied between VRAM and RAM, which speeds up inference.

The size of an LLM is measured in billions of parameters. A model's file size is directly related to its parameter count and the precision of its weights (the data type used to store them).

- **FP16 (Base model):** Each parameter takes 16 bits, or 2 bytes. A 7-billion parameter model will require approximately $7B \times 2 \text{ bytes} \approx 14GB$ of RAM. This is often too large for consumer-grade machines.
- **Quantization:** This is the process of reducing the precision of a model's weights. By using fewer bits per parameter, the model becomes smaller and faster, with a manageable trade-off in accuracy. The most common format is **4-bit quantization (Q4)**, where each parameter takes just 4 bits.

A Q4 quantized 7B model only needs about $7B \times 0.5 \text{ bytes} \approx 3.5GB$ of RAM, making it perfect for Macs with less memory. You also need to account for the memory macOS and other applications use, which can be 4-6GB. Therefore, for most users, quantized models are the only practical option.

## How to Run LLMs

The easiest way to get started is with **Ollama**. It's a command-line tool that streamlines the process of downloading, managing, and running LLMs on your Mac.

#### How to Install and Run Ollama

1. **Download and Install:** Head over to the [Ollama website](https://ollama.com/) and download the macOS application. It’s a standard installation process.
2. **Run a Model:** Open your terminal and pull a model. A great starting point is Meta's Llama 3 8B model, a powerful and versatile choice.
	```bash
	ollama run llama3
	```
3. **Start Chatting:** Once the download is complete, you can start interacting with the model directly in your terminal.

Ollama handles all the complexities of model conversion and optimization for Apple Silicon, making it incredibly simple to use.

## The Best LLMs for Every Apple Silicon Mac

Here are the top recommendations based on your Mac's RAM configuration. We've focused on Q4 quantized models, which offer the best balance of performance and memory usage.

### For Macs with 8GB RAM

On an 8GB machine, you're contending with system overhead, leaving you with roughly 3-4GB of usable RAM for the LLM. You'll need to stick to smaller, highly efficient models that deliver impressive performance for their size.

| Mac Configuration | Recommended Models (Q4 Quantized) | Main Use Case | Tokens/Sec |
| --- | --- | --- | --- |
| **M1 (8GB)** | `phi-3:3.8b`, `qwen:4b`, `gemma:2b`, `tinydolphin:latest`, `llama3` (highly compressed quant) | General chat, summarization, light creative writing. | ~18 - 37 |

#### About these models

- **`phi-3:3.8b`**: Microsoft's powerhouse small model. It offers surprisingly strong reasoning and instruction-following for its size.
- **`qwen:4b`**: A fast and competent model from Alibaba Cloud, great for quick questions and general assistance.
- **`gemma:2b`**: Google's lightweight model. It's a solid all-rounder and a great starting point for on-device tasks.
- **`tinydolphin:latest`**: An uncensored fine-tune of Phi-3, excellent for creative writing and brainstorming without guardrails.
- **`llama3`**: The default tag often points to a very small, quantized version of Llama 3 8B that can squeeze into an 8GB system for basic queries.

### For Macs with 16GB - 18GB RAM

This is the sweet spot for many developers. With around 10-12GB of available RAM, you can comfortably run the most popular and powerful 7B to 14B models, which are excellent for coding, complex reasoning, and day-to-day productivity.

| Mac Configuration | Recommended Models (Q4 Quantized) | Main Use Case | Tokens/Sec |
| --- | --- | --- | --- |
| **M1 (16GB)** | `llama3:8b`, `deepseek-coder-v2:16b-lite`, `wizardlm2:7b`, `gemma:7b`, `qwen:14b` | All-purpose chat, advanced coding, RAG applications. | ~26 - 39 |
| **M1 Pro (16GB)** | `llama3:8b`, `deepseek-coder-v2:16b-lite`, `wizardlm2:7b`, `gemma:7b`, `qwen:14b` | Enhanced performance for the same tasks. | ~30 - 46 |
| **M2 Pro (16GB)** | `llama3:8b`, `deepseek-coder-v2:16b-lite`, `wizardlm2:7b`, `gemma:7b`, `qwen:14b` | Faster token generation, smoother experience. | ~30 - 46 |
| **M4 (16GB)** | `llama3:8b`, `deepseek-coder-v2:16b-lite`, `wizardlm2:7b`, `gemma:7b`, `qwen:14b` | Great for high-performance mobile AI tasks. | ~48 - 72 |
| **M3 Pro (18GB)** | `llama3:8b`, `deepseek-coder-v2:16b-lite`, `wizardlm2:7b`, `gemma2:9b`, `qwen:14b` | Excellent performance for demanding workflows. | ~43 - 65 |

#### About these models

- **`llama3:8b`**: The best all-rounder. It excels at reasoning, instruction-following, and general conversation.
- **`deepseek-coder-v2:16b-lite`**: An good coding assistant that outperforms many larger models on programming benchmarks.
- **`wizardlm2:7b`**: A fine-tune from Microsoft known for its exceptional complex reasoning and instruction-following capabilities, often outperforming models of the same size.
- **`gemma:7b` / `gemma2:9b`**: Google's latest open models. They are highly capable, great for multilingual tasks, and offer a strong alternative to Llama 3. The M3 Pro's 18GB can comfortably handle the newer 9B version.
- **`qwen:14b`**: A fantastic multilingual model from Alibaba that can handle larger contexts and more complex instructions.

### For Macs with 24GB - 36GB RAM

With this much memory, you can run powerful Mixture-of-Experts (MoE) models or larger dense models that offer deeper knowledge and more complex understanding. You can also run smaller models with higher quantization (e.g., Q6\_K or Q8\_0) for improved accuracy.

| Mac Configuration | Recommended Models (Q4/Q6 Quantized) | Main Use Case | Tokens/Sec |
| --- | --- | --- | --- |
| **M4 (24GB)** | `mixtral:8x7b`, `gemma2:27b`, `yi:34b`, `qwen:32b`, `llama3:8b-instruct-q8_0` | High-accuracy chat, complex problem-solving, advanced RAG. | ~34 - 52 |
| **M1 Pro (32GB)** | `mixtral:8x7b`, `gemma2:27b`, `yi:34b`, `qwen:32b`, `wizardlm2:13b` | Mixture-of-Experts models, advanced reasoning, research. | ~26 - 40 |
| **M1 Max (32GB)** | `mixtral:8x7b`, `gemma2:27b`, `yi:34b`, `qwen:32b`, `wizardlm2:13b` | Faster performance on MoE and 30B+ models. | ~29 - 44 |
| **M2 Max (32GB)** | `mixtral:8x7b`, `gemma2:27b`, `yi:34b`, `qwen:32b`, `wizardlm2:13b` | Excellent speeds for 30B+ parameter models. | ~31 - 48 |
| **M4 Pro (32GB)** | `mixtral:8x7b`, `gemma2:27b`, `yi:34b`, `qwen:32b`, `wizardlm2:13b` | Future-proofed performance for large models. | ~47 - 72 |
| **M4 (32GB)** | `mixtral:8x7b`, `gemma2:27b`, `yi:34b`, `qwen:32b`, `wizardlm2:13b` | Top-tier performance on the latest base chip. | ~39 - 60 |
| **M3 Pro (36GB)** | `mixtral:8x7b`, `gemma2:27b`, `yi:34b`, `qwen:32b`, `wizardlm2:13b` | Great for running large models smoothly. | ~34 - 52 |
| **M3 Max (36GB)** | `mixtral:8x7b`, `gemma2:27b`, `yi:34b`, `qwen:32b`, `wizardlm2:13b` | Top-tier performance for development and research. | ~47 - 72 |

#### About these models

- **`mixtral:8x7b`**: The classic Mixture-of-Experts (MoE) model. It delivers the knowledge of a 47B model with the speed of a 13B model, making it incredibly efficient.
- **`gemma2:27b`**: Google's 27B model is a performance leader, outperforming many models twice its size on benchmarks and offering fantastic multilingual capabilities.
- **`yi:34b`**: From 01.AI, this model is renowned for its strong bilingual (English/Chinese) capabilities and excellent general reasoning.
- **`qwen:32b`**: A highly capable model for those who need deep knowledge for research or complex multi-step tasks.
- **`wizardlm2:13b`**: The larger version of WizardLM-2 provides even stronger reasoning and is a top choice for complex instruction-following tasks.

### For Macs with 48GB - 64GB RAM

This is where local LLMs start to shine. You have enough memory to run very large models that gets closer to the performance of top proprietary APIs, all with the privacy and speed of local inference.

| Mac Configuration | Recommended Models (Q4/Q6 Quantized) | Main Use Case | Tokens/Sec |
| --- | --- | --- | --- |
| **M3 Max (48GB)** | `llama3:70b`, `wizardlm2:70b`, `gemma2:27b-instruct-q6_K`, `mixtral:8x22b`, `deepseek-coder:67b` | Running top-tier models for demanding applications, local fine-tuning. | ~25 - 33 |
| **M1 Max (64GB)** | `llama3:70b`, `wizardlm2:70b`, `mixtral:8x22b`, `deepseek-coder:67b`, `qwen:72b` | Excellent for research, large-scale coding, and fine-tuning experiments. | ~16 - 22 |
| **M1 Ultra (64GB)** | `llama3:70b-instruct-q6_K`, `wizardlm2:70b`, `mixtral:8x22b-q6_K`, `deepseek-coder:67b`, `qwen:72b` | Higher accuracy with larger models due to better quantization. | ~21 - 28 |
| **M2 Max (64GB)** | `llama3:70b`, `wizardlm2:70b`, `mixtral:8x22b`, `deepseek-coder:67b`, `qwen:72b` | Fast inference speeds on 70B class models. | ~17 - 23 |
| **M2 Ultra (64GB)** | `llama3:70b-instruct-q6_K`, `wizardlm2:70b`, `mixtral:8x22b-q6_K`, `deepseek-coder:67b`, `qwen:72b` | Very fast speeds with high-accuracy quantization. | ~23 - 31 |
| **M3 Max (64GB)** | `llama3:70b-instruct-q6_K`, `wizardlm2:70b`, `mixtral:8x22b-q6_K`, `deepseek-coder:67b`, `qwen:72b` | Unmatched performance for local LLM development. | ~27 - 36 |
| **M4 Pro (64GB)** | `llama3:70b-instruct-q6_K`, `wizardlm2:70b`, `mixtral:8x22b-q6_K`, `deepseek-coder:67b`, `qwen:72b` | Cutting-edge performance for flagship models. | ~26 - 34 |
| **M4 Max (64GB)** | `llama3:70b-instruct-q6_K`, `wizardlm2:70b`, `mixtral:8x22b-q6_K`, `deepseek-coder:67b`, `qwen:72b` | The best performance for this memory tier. | ~30 - 40 |

#### About these models

- **`llama3:70b`**: The gold standard for 70B models. It provides GPT-4 class performance for a wide range of sophisticated tasks.
- **`wizardlm2:70b`**: A direct competitor to Llama 3 70B, excelling at complex, multi-step reasoning and instruction following.
- **`mixtral:8x22b`**: The big brother to the 8x7B MoE. It's a massive model that provides incredible depth of knowledge while remaining efficient to run.
- **`deepseek-coder:67b`**: For specialized, large-scale software engineering tasks, this provides unparalleled code intelligence.
- **`qwen:72b`**: The largest model in the Qwen 1.5 series, offering extensive world knowledge and strong reasoning.

### For Macs with 96GB - 512GB RAM

If you have a Mac with this much memory, then you are at the pinnacle of what consumer hardware can achieve. You can run massive models at high precision, perform in local fine-tuning, and handle multiple models simultaneously.

| Mac Configuration | Recommended Models (Quantized & Full Precision) | Main Use Case | Tokens/Sec |
| --- | --- | --- | --- |
| **M2 Max (96GB)** | `command-r-plus:104b-q4_K_M`, `llama3:70b-q8_0`, `mixtral:8x22b-q6_K`, `deepseek-v2:236b-q2`, `yi-large` | Running the largest models with high-quality quantization. | ~8 - 18 |
| **M3 Max (96GB)** | `command-r-plus:104b-q4_K_M`, `llama3:70b-q8_0`, `mixtral:8x22b-q6_K`, `deepseek-v2:236b-q2`, `yi-large` | State-of-the-art performance for massive models. | ~12 - 27 |
| **M4 Max (96GB)** | `command-r-plus:104b-q4_K_M`, `llama3:70b-q8_0`, `mixtral:8x22b-q6_K`, `deepseek-v2:236b-q2`, `yi-large` | The very latest in high-performance local AI. | ~14 - 30 |
| **M1/M2/M3/M4 Ultra/Max (128GB)** | `llama3:70b` (FP16), `command-r-plus:104b-q6_K`, `mixtral:8x22b` (FP16), `deepseek-v2:236b-q3_K_S`, `yi-large` | Running 70B+ models at full 16-bit precision for maximum quality. | ~20 - 26 |
| **M2 Ultra (192GB)** | `llama3.1:405b-q2_K`, `command-r-plus:104b` (FP16), `deepseek-v2:236b-q4_K_M`, `mixtral:8x22b` (FP16), `llama3:70b` (FP16) | Local fine-tuning of 70B models, running multiple large models simultaneously. | ~14 - 18\*\* |
| **M3 Ultra (256GB)** | `llama3.1:405b-q3_K_M`, `deepseek-v2:236b-q6_K`, `command-r-plus:104b` (FP16), Run `llama3:70b` and `deepseek-coder:67b` at the same time. | Experimenting with frontier-sized models at usable quantization. | ~18 - 19 |
| **M3 Ultra (512GB)** | `llama3.1:405b-q4_K_M`, `deepseek-v2:236b` (FP16), `gemma2:27b` (FP32) | Research and development on the absolute largest open models at high precision. | ~20 - 26 |

#### About these models

- **`command-r-plus:104b`**: From Cohere, this model excels at enterprise-grade RAG and tool use. A Q4 version needs ~60GB of RAM.
- **`llama3:70b` (FP16)**: With 128GB+, you can run the full, unquantized 16-bit version (~140GB RAM) for the best possible quality.
- **`deepseek-v2:236b`**: This MoE has 236B parameters. A Q4 quant requires ~136GB RAM, making it perfect for high-memory systems.
- **`llama3.1:405b`**: The largest open model from Meta. Running this is the ultimate test for a local setup. A Q2 or Q3 quant can fit on 192-256GB systems, while a more usable Q4 fits comfortably in 512 GB systems.
- **`yi-large`**: A proprietary-level dense model from 01.AI with exceptional reasoning and multilingual performance, competitive with GPT-4.

## Conclusion

The era of locally run AI is here, and Apple Silicon is the ideal platform for it. By knowing the role of unified memory and selecting a model that matches your Mac's RAM, you can create incredibly powerful AI features and applications with complete privacy and control. The combination of Ollama and the open-source model ecosystem means there has never been a better time to get started.

As models become more efficient and Apple's hardware continues to evolve, the capabilities of on-device AI will only continue to grow. Start with the recommendations in this guide, experiment, and see what you can build.

Recommended Posts

- [Best Local LLMs to Run On Every Apple Silicon Mac in 2026](https://apxml.com/posts/best-local-llms-apple-silicon-mac)
- [DeepSeek System Requirements Guide For Mac OS (V3, R1, All Variants)](https://apxml.com/posts/deepseek-system-requirements-mac-os-guide)
- [Best Local LLMs for Every NVIDIA RTX 50 Series GPU](https://apxml.com/posts/best-local-llms-for-every-nvidia-rtx-50-series-gpu)
- [Best Local LLMs for Every NVIDIA RTX 40 Series GPU](https://apxml.com/posts/best-local-llm-rtx-40-gpu)
- [GPU Requirements Guide for DeepSeek Models (V3, All Variants)](https://apxml.com/posts/system-requirements-deepseek-models)