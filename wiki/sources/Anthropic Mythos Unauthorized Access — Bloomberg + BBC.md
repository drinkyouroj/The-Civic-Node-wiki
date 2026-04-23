---
title: "Anthropic Mythos Unauthorized Access — Bloomberg + BBC"
type: source
tags: [ai, technology, power, infrastructure, cybersecurity]
created: 2026-04-23
updated: 2026-04-23
sources: 6
raw: "raw/Anthropic’s Mythos AI Model Is Being Accessed by Unauthorized Users -….md"
raw_alt: "raw/Claude Mythos AI unauthorised access claim probed by Anthropic.md"
source_url: "https://archive.ph/tV1NJ"
author: "Carmen Arroyo, Rachel Metz, Natasha Mascarenhas (Bloomberg); Joe Tidy (BBC)"
published: 2026-04-21
---

[Bloomberg original](https://archive.ph/tV1NJ) · [BBC coverage](https://www.bbc.com/news/articles/cy41zejp9pko)

## Summary
A small group of users in a private Discord forum gained unauthorized access to Anthropic's Claude Mythos model — the cyber-security-capable frontier system Anthropic has refused to release publicly because it can identify and exploit vulnerabilities "in every major operating system and every major web browser." The group accessed Mythos on the same day Anthropic's limited Project Glasswing partner testing began (initial partners include Apple, Amazon, Cisco). Access was obtained via a third-party vendor contractor's credentials combined with open-source sleuthing — details exposed in a March 2026 Mercor data breach revealed Anthropic's model URL format. Anthropic is investigating.

## Key Points
- The group claims access "to a slew of other unreleased Anthropic AI models" beyond Mythos, per the Bloomberg source.
- They report using Mythos for "simple websites" rather than exploits — an intentional choice to avoid detection, not a capability ceiling.
- Attack vector was compound: legitimate contractor access + OSINT-style URL guessing based on the [[Mercor]] breach leak. Not a "classic hack" per cyber-security executive Raluca Saceanu.
- UK NCSC head Richard Horne used the incident to argue frontier AI is "rapidly enabling discovery and exploitation of existing vulnerabilities at scale."
- Anthropic's statement confines the incident to "one of our third-party vendor environments" — quiet deflection toward [[Supply Chain Risk]] framing.
- Project Glasswing and Amazon Bedrock partner-testing distribution is the exact model governance structure the UK relies on, since all frontier labs are US/China-based. The leak exposes the structural fragility.

## Newsletter Angles
- **Power & Infrastructure**: A company that says its model is too dangerous to release can't keep it out of a Discord server. The "safety-by-partner-testing" governance model just had its first documented failure. Pairs with the existing [[AI Safety]] / [[Frontier AI]] concept pages and the [[Help Desk for the Singularity]] fiction arc.
- **Technology & State**: UK Security Minister Dan Jarvis's "generational endeavour" rhetoric plus NCSC framing show governments now treating frontier-model access as national-security infrastructure they do not control. Links to [[The Department of Defense's Conflict With Anthropic and Deal With OpenAI Are a Call for Congress To Act]] and the [[Anthropic vs White House]] thread.

## Entities Mentioned
- [[Anthropic]] — builder; investigating breach
- [[Mercor]] — AI training startup; March 2026 breach exposed model URL format
- Richard Horne — UK NCSC head
- Dan Jarvis — UK Security Minister
- [[Apple]], [[Amazon]], [[Cisco]] — Project Glasswing partners
- [[OpenAI]] — mentioned for its parallel GPT 5.4 Cyber product

## Concepts Mentioned
- [[Frontier AI]] — Mythos as capability frontier
- [[AI Safety]] — access control as the governance frontier
- Project Glasswing — Anthropic's partner-testing program name
- Supply chain risk in model access

## Quotes
> "We're investigating a report claiming unauthorized access to Claude Mythos Preview through one of our third-party vendor environments." — Anthropic statement

> "When powerful AI tools are accessed or used outside their intended controls, the risk is not just a security incident but the spread of capabilities that could be used for fraud, cyber abuse, or other malicious activity." — Raluca Saceanu, Smarttech247

> "Frontier AI is rapidly enabling discovery and exploitation of existing vulnerabilities at scale, illustrating how quickly it will expose where fundamentals of cyber-security are still to be addressed." — Richard Horne, UK NCSC

## Notes
Two independent outlets (Bloomberg originating, BBC following) — corroborated. The Bloomberg piece's source "corroborated the account with screenshots and a live demonstration," which is stronger evidence than the usual anonymous-source AI scoop. The user's comment that they chose mundane tasks "to avoid detection by Anthropic" implies the company's misuse-detection pipeline relies on prompt-content signals, not auth-layer verification — a governance tell.
