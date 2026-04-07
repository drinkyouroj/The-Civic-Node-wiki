---
title: "Obsidian Was Never the Problem"
source: "https://drinkyouroj.substack.com/p/obsidian-was-never-the-problem"
author:
  - "[[Justin Hearn]]"
published: 2026-04-06
created: 2026-04-06
description: "Every PKM tool fails for the same reason: you’re the maintenance worker. Karpathy’s LLM wiki fixes that."
tags:
  - "clippings"
---
### Every PKM tool fails for the same reason: you’re the maintenance worker. Karpathy’s LLM wiki fixes that.

## The Glitch: Your Second Brain Is Already Dead

The personal knowledge management industry built a billion-dollar business selling solutions to a problem it helped create.

Somewhere on your hard drive, an Obsidian vault exists with nobody tending it. It has folders, probably too many. Inside: a podcast transcript you half-listened to three months ago, a book breakdown you never finished synthesizing, seventeen daily notes from the two weeks you committed, and a folder called “Inbox” containing 214 items. Nobody organized those items. Nobody was going to.

The PKM industry discovered a goldmine around 2020: people would pay for systems to capture information they would never use again. Tiago Forte turned this into a $500 methodology called “Building a Second Brain.” It sold well because what it promised was seductive: notes as an external extension of your memory, accessible on demand.[^1]

The problem is structural, not philosophical. None of these systems failed because the concept was broken. They failed because humans are bad at maintenance. Every one of them hands you the keys and tells you to drive forever. You are the agent. You do the tagging, the linking, the reviewing, the resurface work, the taxonomy maintenance.

Most people can sustain that for eleven days.

![An abandoned study with towering shelves of unused binders and an open laptop showing an empty Obsidian vault, bathed in afternoon light — representing the decay of abandoned PKM systems.](https://substackcdn.com/image/fetch/$s_!Dx3c!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F55b926a8-91f8-433f-a077-896ef618f9ce_1344x768.png)

Every PKM system eventually becomes an archaeology project.

Your second brain outlives the version of you who built it. An artifact in a filing language you no longer remember. The notes are there. The knowledge is inaccessible. The difference between a second brain and a graveyard is whether anything alive is tending it.

## The Source Code: Why Every PKM System Eventually Collapses

Passive systems fail because memory requires an active agent, and humans are terrible at being that agent for themselves.

In 1945, Vannevar Bush published “As We May Think” in The Atlantic and described a device called the Memex: a desk-sized machine that would store records and allow users to navigate them through associative trails rather than rigid indexes.[^2] The key insight was not storage. Storage was already solved. The insight was retrieval through association: knowledge becomes useful only when it connects to other knowledge, and connections require an active process of linking.

Bush imagined someone doing that linking work. A machine, perhaps. We gave humans a machine and told them they were the machine.

What we built instead was a system that stores everything and connects nothing unless you personally draw every connection by hand. Obsidian’s graph view is genuinely beautiful. It is also only as useful as the links you remembered to create, which requires you to already know what connects to what. That is the problem you were trying to solve.

Cognitive overhead compounds fast. Every tag is a promise to maintain a taxonomy. Every folder is a commitment to a worldview you will outgrow in six months. Every Daily Note template requires daily filling-in, which feels manageable until you travel, or have a hard month, and return to a system waiting for a version of you that no longer quite exists.

![An overhead view of a person surrounded by scattered notes and tangled string connections, head in hands, representing the cognitive overload of manual knowledge management.](https://substackcdn.com/image/fetch/$s_!OYwP!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53591b55-5b9d-4cc0-a7a3-5a0ee07bf6fc_1344x768.png)

The maintenance tax compounds daily.

Here’s what nobody admits: note-taking feels productive. Retrieving notes is brutal. It means confronting everything you captured and abandoned. The gap between capture and use is where every PKM system dies: it’s waiting for you to remember something you already forgot.

Andrej Karpathy, former Director of AI at Tesla and early OpenAI researcher, published a gist describing a different architecture for this problem.[^3] He called it an “LLM wiki agent.” The concept reduces to one sentence: instead of you being the maintenance agent for your notes, the LLM is. He’s spent more time thinking about how intelligence actually works than most people spend thinking about anything.

That swap changes everything.

## The Upgrade: Three Files and One Prompt

The Karpathy method does not give you a better note-taking app. What you get instead is a partner who was there the day you learned something and will still be there the day you need it back.

The implementation requires three files.

**CLAUDE.md** is the schema file: the constitution of your second brain. It defines what gets captured, how entries are formatted, what categories exist, and how the LLM should behave in every session. Think of it as the standing operating instructions your agent reads before starting work each day.

**index.md** is the structured knowledge index. Not a flat list of notes, but an active, maintained record of what you know: organized by domain, cross-referenced, and updated by the LLM at the close of every session based on what you discussed.

**log.md** is the session diary. Every conversation gets summarized and committed: what you talked about, what changed in the knowledge base, what the system now knows that it didn’t know before.

![A night-time developer workspace with a code editor showing CLAUDE.md on the left monitor and an Obsidian graph view on the right, with a coffee mug in sharp focus in the foreground.](https://substackcdn.com/image/fetch/$s_!Jf3m!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0028bdc6-5b38-471a-9746-9fc80af34d12_1344x768.png)

Three files. One agent. Zero maintenance anxiety.

The Obsidian implementation takes a single session in Claude Code (not Claude.ai chat). Open your vault directory in the Claude Code CLI, and paste [the Karpathy gist](https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md) alongside this prompt:

> *“You are now my LLM wiki agent. Implement this exact idea file as my complete second brain. Guide me step-by-step: create the CLAUDE.md schema file with full rules, set up index.md and log.md, define folder conventions, and show me the first ingest example. From now on, every interaction follows the schema.”*

Note: Claude Code reads CLAUDE.md because you explicitly provide it as context (either by pasting it directly or through workspace configuration). Once the schema is established, your role shifts to providing raw material.

Claude generates the file structure, defines folder conventions, and walks through a first ingest example. From that session forward, every conversation begins with Claude reading your CLAUDE.md, checking what it already knows, and operating within the schema you defined. You bring the idea from your walk, the article you half-processed, the thing you need to remember. The agent absorbs it, places it in context, relates it to existing knowledge, and logs what changed.

This fulfills the vision Bush articulated in 1945: an agent maintaining associative trails on your behalf, with technology he couldn’t have imagined.

## My Debug: The Moment the System Knew What I’d Forgotten

The system reveals itself not when you build it, but the moment it knows something you forgot you knew.

Growing up working in my father’s frame shop, the thing I loved most was not making frames. It was organizing: samples sorted by color and material, inventory tracked in the Lifesaver POS system, every element in a place that made sense. What eroded the system was maintenance, the entropy. Samples moved and never returned. The system degraded because no single person’s job was to hold it together continuously.

![A before-and-after split of a frame shop: chaotic, dusty workbench on the left; the same space perfectly organized on the right, representing the shift from passive systems to active LLM-maintained organization.](https://substackcdn.com/image/fetch/$s_!Tu2g!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc291a8bc-f247-4e53-a6c0-f6455e0ebbab_1344x768.png)

Entropy is the default. An agent changes the default.

The Karpathy method solved that problem in a way no productivity framework I’ve tried previously managed. The first time Claude surfaced information from a session two weeks prior, context I had given it and completely forgotten, and applied it directly to a new question, the experience was not impressive. It was strange. Something external was tracking continuity that my own memory had dropped.

My brain runs multiple threads simultaneously, processing in parallel, none waiting for the others. That style generates enormous raw material and almost no linear organization. A passive PKM accumulates that material and becomes noise. An active agent absorbs it, organizes it, and returns it in useful form.

The bottleneck in every second brain system was never capture. It was always retrieval, and retrieval requires something alive on the other end. If your notes already contain the insight you need but you cannot reach it, the question worth sitting with is whether you actually know it at all.

[^1]: *[Building a Second Brain](https://www.buildingasecondbrain.com/)*

[^2]: *[Vannevar Bush, “As We May Think,” The Atlantic, July 1945](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/)*

[^3]: *[Andrej Karpathy, LLM wiki agent gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)*