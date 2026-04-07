---
title: "Building a DAO Framework: Interview with Aragon's CTO | Aragon Resource Library"
source: "https://www.aragon.org/how-to/building-a-dao-framework-interview-with-aragons-cto"
link_text: "Aragon Network - Building a DAO Framework"
domain: "aragon.org"
published: "2020-12-22"
fetched: 2026-04-07
tags: ["clippings"]
---

# Building the Aragon OSx DAO Framework: Interview with Aragon's CTO

How do you adapt and evolve your DAO once it’s deployed on an immutable blockchain?

That’s the question our engineering team at Aragon has been working on. We interviewed Carlos, Aragon’s CTO, to gain insight into the building blocks of Aragon OSx, DAO plugins, and how our modular framework enables adaptable DAOs.

## Architecture of Aragon OSx


**The Aragon OSx DAO framework is made of two main parts: the core contracts and the framework contracts. The core contracts run each DAO and the framework contracts run all the connections, such as the factories, registry, and plugin manager.**

The core contracts are very simple. They make up the DAO Vault, which is where assets are stored, and the DAO’s permission manager, determining which addresses have permissions to execute which action within the DAO.

“Simplicity is one the biggest features you can have in a smart contract,” said Carlos. Simplicity can help make a contract more secure because there is less potential for bugs and hidden exploits.

The simplicity of the core contracts means there’s less immutable logic, so it’s easier for DAOs to adapt their organization as it evolves through time.

**“If you force logic into it, you have that logic forever,” said Carlos. “That’s why you need a very lean contract that holds your funds and doesn’t do anything. Everything else is programmable and based on your needs through plugins.”**

Think of the architecture as a stack, with the protocol on the bottom and plugins on the top.

**Protocol:**base layer, contains very simple contracts that interact with the blockchain.**Plugin manager:**manages the plugins by allowing the base layer to grant or revoke permission to the plugins or other wallet addresses.**Plugins:**external contracts that can extend the logic of the base layer, but be “unplugged” by revoking permission.

## Plugin manager

**The plugin manager is where you add logic into your DAO. Plugins are connections to other contracts that can integrate with DAOs built on Aragon.** For example, a DAO might want to use NFT voting. In that case, they would grant permission to the NFT voting plugin via the permission manager.

“Once you have the vault that holds the treasury, and the logic that is able to execute anything on governance plugins, you need to tie them together. That’s where the permission management comes in. You can set the permissions from different contracts to the vault.”

For example, X contract can execute Y if Z happens. But how does the contract know that Z happened? In these cases, you might want to use an oracle.

An oracle is software that tells contracts on the blockchain things that the contract couldn’t “know” itself. For example, a contract couldn’t know if it’s Tuesday. If there’s a plugin that only sends funds on Tuesday, the oracle tells the contract if it’s Tuesday or not.

“Permission management with oracles that check parameters, like guardians, allows programmable flows into your main contract,” said Carlos. “That’s one of the biggest features we have.”

Carlos gave some more details on how the plugin manager works on a technical level. “Basically, this is a modifier,” he said. “When you program the plugin, you set the permissions it needs in bytecode. Whenever you want to use that permission you just call a function.” Then, when you call the function, it calls a modifier to ask if that address has permission. When the modifier answers “yes,” the function executes.

## Adapting with DAO Plugins

Typically, when you want to change a contract deployed to the blockchain, you need to upgrade the entire contract. This is cumbersome and can open up security risks because you need to move your treasury.

But the new Aragon protocol is built to solve this problem. Instead of deploying an entirely new DAO, simply grant permission to the new plugin that gives you the adaptations you need.

“You’re almost never going to upgrade the DAO vault. It’s very simple. But you will want to upgrade the next layer—governance—from time to time. Maybe every few months or every year.”

That’s why the logic is separated away from the DAO itself. **The logic is in the plugins, which are not deployed in the core contract.**

**This means DAOs can adapt, even on an immutable blockchain.**

For example, maybe you want to start your DAO as a multisig. Say you have a small DAO of just five people, and everyone is a signer on the multisig. You have a pass rate and quorum of three out of five of the signers.

Once your DAO grows to 20 people, a pass rate and quorum of three is probably not sufficient anymore. Typically, if you want to upgrade this DAO to a new type of voting, you would have to deploy a new DAO contract and migrate your treasury there.

**In our new protocol, you’ll simply unplug the multisig voting plugin by revoking permission in the plugin manager, and then grant permission to the ERC-20 plugin to adapt your governance.**

This system is highly composable and grows with the changing needs of your DAO and the ecosystem as a whole. If a new governance model becomes popular, you can simply develop a new plugin to apply that model to your organization without needing to start over from scratch. Our protocol enables organizations we can’t yet imagine today.

**With the new protocol, “You have full mutability of your DAO without having to upgrade your contracts.”**

## What can be built on top


On top of this stack, developers can build apps, or UIs that the end user interacts with. We built one UI, the Aragon App, but anyone can build a UI for their own use cases.

“Our app will do the most basic core things a DAO needs, but do them well,” said Carlos. “We’ll ensure those basics have the best user experience and the most human-centric design possible.”

For reaching beyond the basics, other interfaces could be built on top. For example, UIs for specific verticals could be built. With the simple, modular underlying system, the sky is the limit for building on top.

“You start with something very simple and based on modularity, and you end up having a composable system that can grow with other systems as well,” said Carlos.

## Permission management system

Carlos has a lot of ideas for how the permission management system could be used, including social media profiles, account abstraction, and more advanced governance systems.

“Governance plugins are the first thing that comes to your mind when building a DAO,” he said. “You can have delegated governance, normal on-chain voting with ERC-20s, NFT voting, and you can even go into more creative stuff, like what we’re doing at Aragon ZK Research.”

You can also make it easier to post on blockchain-based social networks like Lens as a DAO, by using a plugin that posts when it receives enough approval.

“You can do a lot of magic in these governance plugins. You can integrate Snapshot and Lens profiles to cross-post proposals on social media,” he said.

Another avenue is making payments easier and more automatic. “You could also integrate payment streaming, like through Superfluid.”

A new avenue to explore is using a DAO as a smart wallet. Account abstraction is the customizability of your crypto wallet to make it safer and more convenient to use, so you or your DAO can better manage your assets.

“You can have your own personal DAO that belongs to you,” he said. For example, you could program logic into a plugin that allows you to make transactions under a certain dollar amount with just your hot wallet, and then if you have a transaction over $10,000, it requires a signature from your cold wallet. This makes a lot of sense in terms of security. Nowadays, security is one of the biggest topics we have to think about.”

But the possibilities go beyond just these examples. We compiled a list of 20 dApps you can build on Aragon OSx, so you can find more inspiration!

## Open-source plugins

“Anyone can build plugins,” said Carlos. “You don’t need an API, you don’t need to get authorized, you don't even need to give your email.” Building on Aragon is entirely permissionless.

Carlos said the engineering team was careful to ensure that plugins are easy to develop. “As long as you know a bit of Solidity, you’re good to go,” he said. But if you don’t want to code a plugin from scratch, you can fork the existing plugins. Simply erase what you don’t want, add a few new lines of code, and you have your own plugin!

“The way the system is designed is that you can use them as Legos,” he said. “Even if you don’t know how to build something from the ground up, you can use pieces from different plugins.”

## Join us to build the DAOs of the future

The protocol was designed to enable organizations that we can’t yet imagine today.

“Anything can be a DAO,” said Juliette, Developer Advocate at Aragon, in the interview with Carlos. “As long as you're working to achieve a common mission with a group of people, you'll need resources. And then, you need to *organize* those resources. Essentially, that's the DAO.”

The fact that anything can be a DAO makes us incredibly excited. But, converting the world’s organizations into DAOs is a massive task, and we know we can’t do it alone!

“We’re building one interface, but that doesn’t mean that we cover 100% of the use cases,” said Carlos. “So, we need help. This isn’t only on us—we need more minds working on this very same problem. That’s the cool thing about this core protocol. It allows anyone to build anything on top of it.”

**To learn more, you can listen to the full interview here:**

Want to build with us? Check out our developer docs or reach out to have your custom DAO built by our team.
