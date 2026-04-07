---
title: "Therapy in a Trustless World"
type: article
article_type: nonfiction
tags:
  - mental-health
  - technology
  - ai
published: 2025-09-02
created: 2026-04-07
updated: 2026-04-07
source: "published/Therapy in a Trustless World.md"
---

## Argument
The mental health tech industry has replicated the structural exploitation of other vulnerable-consumer markets: BetterHelp sold therapy session data to Facebook and Snapchat; Cerebral, MDLIVE, and Talkspace (collectively $1B+ raised) harvest intimate psychological data for insurance companies, employers, and advertisers. The solution is decentralized AI therapy running locally on edge nodes (the piece uses Datagram's infrastructure as the example), where therapeutic conversations never leave the user's device. The author has been his own clinical trial for a year — first GPT (uploaded everything to OpenAI servers), then local Ollama/Qwen3 models (zero data exposure). The tension: local AI therapy requires technical knowledge that puts it out of reach for the 99% who most need it.

## Structure
The piece is structured as a response to four explicit questions about a DePIN use case:
1. **What is your use case?** Decentralized AI mental health app; AI inference on Datagram nodes; no data leaves the device.
2. **What makes it unexpected?** Blockchain infrastructure for psychological sovereignty rather than financial transactions or supply chain.
3. **How does Datagram's infrastructure enable it?** Node-based LLAMA inference locally; secure one-time encrypted tunnels for any necessary data sharing; cost-efficient scaling on idle compute.
4. **Why is it necessary?** Personal testimony: a year of AI therapy (GPT then Ollama/Qwen3); the "vulnerability monetization paradox"; Cerebral breach exposed 3.1 million users' psychological blueprints; anxiety disorders are not irrational response to surveillance capitalism.

## Key Examples
- FTC banned BetterHelp from sharing user therapy data with Facebook and Snapchat for targeted advertising — confirmed, not hypothetical.
- Cerebral data breach: 3.1 million users had psychological blueprints exposed.
- Cerebral, MDLIVE, Talkspace collectively raised over $1 billion while monetizing intimate psychological data.
- AIDS crisis parallel: pharmaceutical companies exploiting desperate patients; vulnerability itself as a business model.
- Author's personal protocol: GPT phase required uploading intimate psychological details to OpenAI servers; switched to local Qwen3 via Ollama — same therapeutic benefit, zero data exposure, but requires command-line competence that 99% of users lack.
- Nearly 40% of adults report persistent anxiety symptoms (APA Stress in America 2024).

## Connections
- [[DePIN]] — Datagram's infrastructure as the technical solution; this is the most specific DePIN application piece in the newsletter
- [[AI Therapy]] — the author as personal test case; pairs directly with the AI therapist's neurodivergence detection in "My Autism Self-Assessment Scores"
- [[When Minds Break]] — establishes the stakes: AI that amplifies delusion vs. AI that provides genuine grounding
- [[Surveillance Capitalism]] — the business model the piece argues against; vulnerability monetization as its most extractive form
- [[BetterHelp]] — entity; confirmed FTC action makes this a documented case, not just a claim

## What It Leaves Open
- The Datagram/DePIN technical solution is presented as a use-case pitch, not a working product — what would actual implementation look like, and what are the regulatory obstacles?
- Local AI models can be personalized, but does personalization without any external grounding create a risk of echo-chamber therapy?
- Can local AI therapy handle crisis situations (active suicidality, psychosis) or only maintenance/support?
- The technical accessibility gap is named but not solved: what would a consumer-friendly version actually look like?
- No engagement with insurance, licensing, or liability questions that would accompany any formal mental health application.

## Newsletter Context
This is the piece where the personal and the analytical strands most explicitly converge: the author's own psychiatric system failures (documented across the personal pieces) become the motivating use case for a specific technical architecture. The "I've been my own clinical trial" framing is the newsletter's signature move — personal catastrophe as analytical access, but here with a concrete product proposal attached. The tension between "this works for me" and "this requires technical skills most people don't have" is left productively unresolved.
