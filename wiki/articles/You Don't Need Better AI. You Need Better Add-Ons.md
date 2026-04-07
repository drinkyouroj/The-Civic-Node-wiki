---
title: "You Don't Need Better AI. You Need Better Add-Ons."
type: article
article_type: nonfiction
tags: ["technology", "ai"]
published: 2025-08-15
created: 2026-04-07
updated: 2026-04-07
source: "published/You Don't Need Better AI. You Need Better Add‑Ons.md"
---

## Argument

The gap between poor and excellent AI outputs is not primarily a function of which model you use — it is a function of prompt engineering. "Prompt enhancers" are short, reusable instruction fragments appended to any prompt that change how a model processes a request (planning, verification, self-critique) rather than what it is asked to produce. A two-enhancer stack is sufficient for most high-stakes tasks; more than three introduces diminishing returns. These enhancers are model-agnostic and portable across GPT-5, Claude, Gemini, and others.

## Structure

Practical guide organized as follows:

1. **Opening framing** — Most people treat AI like a mall fountain wish. The fix is small targeted instructions that change how the model thinks before it answers.
2. **What Is a Prompt Enhancer?** — Defined as an instruction that shapes process rather than content. The recipe/mise-en-place analogy.
3. **The Two-Enhancer Rule** — 1 enhancer for quick tasks; 2 for important tasks; 3+ only for high-stakes work with extra back-and-forth.
4. **Copy-Paste Library** — Organized by category: Planning & Quality, Follow-Ups & Gaps, Style & Scope, Verification, Comparison, Refinement. ~15 specific enhancers with rationale.
5. **Model-Agnostic Notes** — Rough tendencies by model type (reasoning-forward, summarizer/storyteller, code-savvy).
6. **Field Guide by Job-To-Be-Done** — Five worked examples: Research & Synthesis, Strategy & Decision Memos, Product/UX Copy, Coding & Reviews, Content Drafting.
7. **Always-On Footer** — A single paste-ready enhancer stack for any important task.
8. **Troubleshooting** — Diagnostic guide for common failure modes (too generic, too verbose, too timid, too confident, goes off-topic).

## Key Examples

- The flagship enhancer: "Think carefully about this task and ask me follow-up questions until you're 95% confident you can accomplish the task successfully."
- "Plan before answering. Show a brief plan, then the answer." — forces model from perform-now to plan-first.
- "Before finalizing, critique your answer in 5 bullets." — self-QA without a second pass.
- "If uncertainty >10%, say what you're unsure about and how to test it." — explicit uncertainty disclosure.
- Five full worked prompt examples with explanations of why each enhancer combination works for that task type.
- Placement rule: enhancers go after the task but before strict constraints (word count, format) because models weight early instructions more.

## Connections

- [[The Nervous System of AI]] — follow-up piece specifically applying these principles to GPT-5's architecture
- [[Octopus Mode]] — the advanced prompt template introduced in "The Nervous System of AI" is an extension of the principles here

## What It Leaves Open

- Whether the "two-enhancer rule" is empirically validated or a practical heuristic — the piece presents it as established guidance but offers no data.
- How prompting strategies should evolve as models improve their ability to infer intent without explicit instruction — the piece treats current prompting needs as stable.
- No discussion of cost implications: more elaborate prompts consume more tokens, which matters for high-volume applications.
- The piece is model-agnostic by design but notes only "rough tendencies" without rigorous comparison — which enhancers work better on which models is left to reader experimentation.

## Newsletter Context

Foundational practical piece on AI workflow optimization. Preceded "The Nervous System of AI," which applies similar ideas specifically to GPT-5. Pure utility piece — no political or power framing, no personal narrative. Most directly actionable content in the newsletter's AI coverage. Relevant to the AI beat as a demonstration of how the gap between AI capability and AI utility is primarily a human skill problem, not a model problem.
