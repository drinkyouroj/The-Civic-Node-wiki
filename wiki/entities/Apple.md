---
title: "Apple"
type: entity
entity_type: organization
tags: [technology, antitrust, power]
created: 2026-04-07
updated: 2026-04-07
sources: 8
---

## Overview
Apple Inc. is the US-based technology company behind the iPhone, iOS, and the App Store. It has become a central target of global antitrust enforcement due to its control over iOS app distribution — a walled garden that generates significant revenue through mandatory developer commissions of up to 30%.

## Apple Silicon & Local AI

Apple Silicon's unified memory architecture — a single memory pool shared by CPU and GPU — has emerged as a significant advantage for local LLM inference. Unlike traditional PC hardware where model weights must be copied between system RAM and discrete VRAM over a PCIe bottleneck, Apple Silicon accesses weights directly at full memory bandwidth. As of early 2026, a 512GB Mac Studio (M3/M4 Ultra) can run DeepSeek R1 (671B parameters) at Q4 quantization locally — frontier reasoning on consumer hardware. See [[On-Device AI]].

## Key Facts
- iOS App Store charges commissions up to 30%; reduced to 15% for developers earning <$1M/year (from end of 2020)
- UK Competition Appeal Tribunal ruled Apple abused market power over iOS app distribution and in-app payments, October 2015–end 2020 [[Apple Loses UK Antitrust Lawsuit Over App Store Fees]]
- UK class action seeks up to £1.5 billion in damages; damages trial scheduled November 2025
- EU Digital Markets Act complaint filed by civil rights groups (Article 19, Society for Civil Rights) over €1M standby letter of credit requirement for App Store developers [[Apple Hit with EU Antitrust Complaint Over App Store Policies]]
- DMA penalties can be up to 10% of global annual revenue
- Apple will appeal UK CAT ruling

## Newsletter Relevance
Apple's App Store litigation is the clearest current example of the Platform Antitrust battle: a company using monopoly control over a technical platform (iOS distribution) to extract rents from developers, who pass costs to consumers. Multiple jurisdictions (UK, EU, US) are attacking this structure simultaneously, each using different legal theories. The outcome will set the terms for how digital platform monopolies are regulated globally.

## Connections
- [[Digital Markets Act]] — EU regulation Apple is accused of violating
- [[European Commission]] — EU antitrust regulator pursuing Apple
- [[UK Competition Appeal Tribunal]] — found Apple abused market power
- [[Platform Antitrust]] — the central concept organizing Apple's legal challenges
- [[Tech-State Conflict]] — Apple's ongoing legal battles with multiple state regulators
- [[OpenAI]] — competing in adjacent markets (AI assistants)

## Source Appearances
- [[Apple Loses UK Antitrust Lawsuit Over App Store Fees]] — found liable for App Store monopoly abuse
- [[Apple Hit with EU Antitrust Complaint Over App Store Policies]] — DMA complaint over SBLC requirement
- [[Best Local LLMs for Every Apple Silicon Mac — 2025 Guide]] — unified memory architecture as enabling hardware for on-device AI
- [[Best Local LLMs for Every Apple Silicon Mac — 2026 Guide]] — frontier models (DeepSeek R1 671B) now runnable on Mac Studio; the accidental AI infrastructure moat

## Open Questions
- Will the UK appeal succeed? On what legal grounds?
- What is the status of parallel US DOJ antitrust proceedings against Apple?
- Does the SBLC requirement survive DMA scrutiny, or will Apple modify it?
- How does Apple's AI strategy (Apple Intelligence) interact with antitrust concerns about platform bundling?
