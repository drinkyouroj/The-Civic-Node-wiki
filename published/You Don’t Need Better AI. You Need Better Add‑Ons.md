---
title: "You Don’t Need Better AI. You Need Better Add‑Ons."
source: "https://drinkyouroj.substack.com/p/you-dont-need-better-ai-you-need"
author:
  - "[[Justin Hearn]]"
published: 2025-08-15
created: 2026-04-07
description: "Simple prompt enhancers that make GPT‑5, Claude, Gemini, and friends think first and deliver work you can actually use"
tags:
  - "clippings"
---

[![A chef seasons a robot’s head with tiny checklists.](https://substackcdn.com/image/fetch/$s_!TZWr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8429b1d7-2f43-440e-919c-6e6ba2733887_1248x832.png)](<https://substackcdn.com/image/fetch/$s_!TZWr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8429b1d7-2f43-440e-919c-6e6ba2733887_1248x832.png>)

[Subscribe now](<https://drinkyouroj.substack.com/subscribe?>)

Most people talk to AI like they’re making a wish at a mall fountain. Toss in a vague prompt, hope for a miracle, and act surprised when it spits out soggy pennies. The fix isn’t “get a bigger model.” The fix is add small, targeted instructions that change how the model thinks before it answers. Those tiny instructions are **prompt enhancers** — and they turn default‑mode chatbots into meticulous teammates.

Your high‑performer starter pack begins with a line you’ll use everywhere:

> **“Think carefully about this task and ask me follow‑up questions until you’re 95% confident you can accomplish the task successfully.”**

That single sentence flips the model from “perform now” to “plan first.” Translation: fewer hallucinations, tighter structure, and outputs that don’t read like a group project the night before it’s due.

## What Is a Prompt Enhancer?

A **prompt enhancer** is a short add‑on you tack to the end of your request that shapes _process_ , not just _content_. It tells the model how to plan, what to verify, which audience to target, and how to critique itself before handing you the answer.

Think of your prompt as the recipe and the enhancer as the _mise en place_ — the pre‑work that prevents chaos and burnt onions. Without it, you asked for lasagna and got very confident noodles. With it, you get dinner (labeled leftovers included).

## The Two‑Enhancer Rule (So You Don’t Overcook It)

Stacking five enhancers makes models skittish or weirdly literal. Keep it simple:

  * **1 enhancer** → quick tasks, decent outcomes.

  * **2 enhancers** → important tasks, best quality per minute.

  * **3+** → only for high‑stakes work when you’re fine with extra back‑and‑forth.




If it starts feeling generic, add a **specificity enhancer** : audience, domain, examples, constraints. If it starts feeling timid, remove an enhancer and restate the goal plainly.

## Copy‑Paste Library (Use As Footers On Any Prompt)

### Planning & Quality

  *  _Plan first, answer second._ → “**Plan before answering. Show a brief plan, then the answer.** ”

  *  _Expose hidden assumptions._ → “**List assumptions and flag any that seem risky.** ”

  *  _Offer options, not ultimatums._ → “**Give me three approaches: fast/basic, balanced, gold‑standard.** ”




### Follow‑Ups & Gaps

  *  _Don’t guess — ask._ → “**Ask clarifying questions first; don’t answer until you’ve asked them.** ”

  *  _Request missing inputs._ → “**If information is missing, tell me exactly what you need.** ”




### Style & Scope

  *  _Aim your voice._ → “**Write for [audience], at [grade level], in [tone].** ”

  *  _Keep the signal, trim the fluff._ → “**Limit to 200 words without losing nuance. No filler.** ”

  *  _Ground in context._ → “**Add 2 domain‑specific examples from [industry].** ”




### Verification

  *  _Catch your own bugs._ → “**Before finalizing, critique your answer in 5 bullets.** ”

  *  _Show your uncertainty._ → “**If uncertainty >10%, say what you’re unsure about and how to test it.**”




### Comparison

  *  _Decision framing._ → “**Provide a compare/contrast table with tradeoffs and a recommendation.** ”




### Refinement

  *  _Draft → tighten._ → “**Provide a first draft, then a concise revision with stronger verbs and fewer hedges.** ”

  *  _Review workflow._ → “**Return a checklist I can use to evaluate this output.** ”




### drinkYourOJ’s Favorite

  * **“Think carefully about this task and ask me follow‑up questions until you’re 95% confident you can accomplish the task successfully.”**




> **Pro move:** Put enhancers _after_ the task but _before_ strict constraints (word count; format). Models weight early instructions more.

[Share](<https://drinkyouroj.substack.com/p/you-dont-need-better-ai-you-need?utm_source=substack&utm_medium=email&utm_content=share&action=share>)

## Model‑Agnostic, Model‑Effective

Enhancers are portable — GPT‑5, Claude, Gemini, Mistral, Llama all respond to them. Rough tendencies:

  * **Reasoning‑forward models** love “Plan → Assumptions → Alternatives.”  
Add: “Prioritize accuracy over brevity.”

  * **Summarizer/storyteller models** thrive with audience/voice constraints and tight word limits.  
Add: “No clichés; high‑signal lines only.”

  * **Code‑savvy models** excel when you ask for comments on tradeoffs, tests, and refactors.  
Add: “Propose readability‑first and performance‑first rewrites.”




No sacred lore here. You’re just telling the system how to think before it types.

## Field Guide: Enhancers by Job‑To‑Be‑Done

### 1) Research & Synthesis

> “Summarize the key arguments in [topic] for a smart non‑expert. Extract definitions, claims, evidence, counterarguments, and open questions. **Plan before answering.** List assumptions. If sources are needed, ask for them first. Return a 150‑word abstract and a bulleted outline.”

**Why it works:** You script an analysis pipeline (plan → structure → sanity check) so you get clarity, not vibes.

### 2) Strategy & Decision Memos

> “Draft a 1‑page decision memo on [question]. Include 3 options, pros/cons, risks, costs, and a recommendation with ‘why now.’ **Ask clarifying questions until you’re 95% confident.** Finish with five metrics for ‘how we’ll know this worked.’”

**Why it works:** You force rigor and a scoreboard. The model stops shooting from the hip.

### 3) Product / UX Copy

> “Write in‑app microcopy for [feature]. Audience: [segment]. Voice: [brand traits]. **Provide 3 tone variants** (friendly, direct, playful). **Add a 10‑item UX copy checklist** and rewrite anything that fails.”

**Why it works:** Range + self‑QA beats one bland paragraph.

### 4) Coding & Reviews

> “Write a [language] function that [task]. **Show a brief plan first.** Then code with comments explaining tradeoffs. **Add tests** , and propose two refactors: readability‑first and performance‑first. **Critique your solution** in five bullets.”

**Why it works:** You request design reasoning, not code dump.

### 5) Content Drafting (posts, scripts, emails)

> “Draft a [format] on [topic] for [audience]. Hook → context → three insights → takeaway. **Give two drafts:** one ‘clean’ and one ‘spiky’ with sharper opinions. **Self‑edit the spiky draft** in five bullets.”

**Why it works:** You get range first, polish second.

## Your Always‑On Footer (Steal This)

Paste this under anything that matters:

> “**Plan before answering. List assumptions and ask clarifying questions until you’re 95% confident you can accomplish the task successfully. If information is missing, tell me exactly what you need. Prioritize accuracy over brevity.** ”

It’s coffee, a checklist, and a manager, all in one line.

[Subscribe now](<https://drinkyouroj.substack.com/subscribe?>)

## Troubleshooting: When Outputs Still Feel Mid

  * Too generic? Add audience + domain + examples. Name the vibe: “for solo e‑commerce founders,” “healthcare case studies,” “no corporate euphemisms.”

  * Too verbose? Cap the words and forbid filler: “250 words, no throat‑clearing, no clichés.”

  * Too timid? Remove one enhancer and restate the goal simply. Add: “Make a defensible call.”

  * Too confident? Add the self‑critique enhancer and an uncertainty disclosure.

  * Goes off‑topic? Start with a one‑sentence task summary: “Restate the goal in one line, then proceed.”




LLMs are brilliant, but their default energy is “overachieving intern whose glasses fogged up.” Prompt enhancers are the anti‑fog spray. Without them, you get an earnest monologue about synergy; with them, you get a plan, options, and a recommendation that doesn’t sound like it was coached by a motivational poster.

## Paste‑Ready Examples Using Your Favorite Enhancer

### General Writing

> “Write a 900‑word Substack post explaining how prompt enhancers improve AI outputs for non‑technical readers. Include three real‑world examples and a copy/paste section of enhancers. **Think carefully about this task and ask me follow‑up questions until you’re 95% confident you can accomplish the task successfully.** Plan → Draft → Self‑critique. Keep it tight and funny without being cringe.”

### Marketing Email

> “Write a 150‑word launch email for our new feature that summarizes benefits in three bullets and ends with a single CTA. **Ask clarifying questions** if needed. Provide two tone options and a subject‑line A/B list.”

### Research Brief

> “Synthesize the current landscape on [topic] with the top five claims, what would change my mind, and three unresolved questions. **List assumptions** and **flag uncertainty** over 10%.”

### Code

> “Implement a function that does [task]. **Plan first**. Include tests. **Critique your solution** for readability, performance, and edge cases.”

## CTA — Try This Today

  1. Pick a task you care about.

  2. Add **two** enhancers from the library above.

  3. Make the model restate the goal in one sentence before it starts.

  4. Iterate once with a self‑critique.




Share your results and favorite **prompt enhancers** in the comments!

Thanks for reading! This post is public so feel free to share it.

[Share](<https://drinkyouroj.substack.com/p/you-dont-need-better-ai-you-need?utm_source=substack&utm_medium=email&utm_content=share&action=share>)
