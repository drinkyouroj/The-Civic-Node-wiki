---
title: "Claude Mythos Unauthorised Access — BBC"
type: source
tags: [ai, technology, power, cybersecurity]
created: 2026-04-22
updated: 2026-04-22
sources: 3
raw: "raw/Claude Mythos AI unauthorised access claim probed by Anthropic.md"
raw_alt: "raw/Anthropic’s Mythos AI Model Is Being Accessed by Unauthorized Users -….md"
source_url: "https://www.bbc.com/news/articles/cy41zejp9pko"
author: "Joe Tidy"
published: 2026-04-21
---

[Original source](https://www.bbc.com/news/articles/cy41zejp9pko)

## Summary

Anthropic is investigating a Bloomberg report that users in a private forum gained unauthorised access to Claude Mythos — a cyber-security-focused AI model Anthropic has deemed too dangerous to release publicly because of its hacking capabilities. According to Bloomberg, the access was obtained "through one of our third-party vendor environments" — most likely misuse of legitimate vendor permissions rather than an external hack. The group has reportedly been using the model but not for hacking, "because they do not want to be detected." The incident raises questions about whether large AI companies can keep gated frontier models out of unauthorised hands when distribution depends on vendor and contractor access controls.

## Key Points

- Claude Mythos is Anthropic's gated cyber-security model; Anthropic has said it is too powerful to release to the public
- Released to some tech and financial companies to help them secure their own systems against its reported vulnerability-exploitation capabilities
- Access came "through one of our third-party vendor environments" — via a contractor who already had legitimate work access, not external hacking
- Cyber expert Raluca Saceanu (Smarttech247 CEO): "most likely through misuse of access rather than a classic hack"
- No evidence (per Anthropic) that its own systems are affected; no confirmation that malicious actors now hold the model
- Context: OpenAI has a parallel capable cyber-security model, GPT 5.4 Cyber
- UK NCSC head Richard Horne at CyberUK: frontier AI is "rapidly enabling discovery and exploitation of existing vulnerabilities at scale" — urged basics of cyber hygiene
- UK Security Minister Dan Jarvis: AI firms must work with government on "generational endeavour" to secure critical networks
- Structural constraint: all frontier AI is built in the US or China; UK relies on companies like Anthropic for access and has no control over how models are built, trained, or released

## Newsletter Angles

- **Anthropic/Tech-State Conflict**: The breach is a direct stress test of Anthropic's "gated frontier model" posture — the company's case for trust (and its case against DoD demands for weaker guardrails, per [[Statement from Dario Amodei on our discussions with the Department of War]]) rests on its ability to control who can use powerful models. Vendor-permission misuse is the exact failure mode that undermines that argument.
- **AI Sovereignty**: Horne's observation that frontier AI is US/China-only and the UK depends on commercial access recasts the wiki's [[AI Sovereignty]] thread: it's not just about building; it's about gatekeeping, and gatekeeping now has a documented leak.
- **Cybersecurity-as-Monetary-Policy-adjacent**: Frontier AI capable of "discovery and exploitation at scale" against existing vulnerabilities moves cyber from hygiene issue to systemic-risk category.

## Entities Mentioned

- [[Anthropic]] — investigating; maker of Mythos
- [[OpenAI]] — has parallel model (GPT 5.4 Cyber) — relevant context given the wiki's ongoing Anthropic/OpenAI divergence thread

## Concepts Mentioned

- [[Frontier AI]] — the category; relevant to existing [[AI Sovereignty]] and [[AI Liability]] pages

## Quotes

> "We're investigating a report claiming unauthorized access to Claude Mythos Preview through one of our third-party vendor environments." — Anthropic statement

> "When powerful AI tools are accessed or used outside their intended controls, the risk is not just a security incident but the spread of capabilities that could be used for fraud, cyber abuse, or other malicious activity." — Raluca Saceanu, Smarttech247

> "As we have seen in the media in recent days, frontier AI is rapidly enabling discovery and exploitation of existing vulnerabilities at scale." — Richard Horne, NCSC

## Notes

BBC story sources Bloomberg as primary; direct access to the Bloomberg report is paywalled. Anthropic's statement is cautious — "investigating a report" rather than confirming the breach. Bloomberg's claim that the group "has been using the model since it gained access" is unverified independently. The absence of specific timeframe, vendor name, or group identity limits what can be inferred about scale or intent.

> ⚠️ Unverified specifics: the breach duration, the vendor involved, and the identity of the unauthorised group are all reported by Bloomberg without primary documentation in this piece. Treat as reported rather than confirmed.
