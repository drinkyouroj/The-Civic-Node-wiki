---
title: "Preventable Cyber Attack Impacts Io.net"
source: "https://cryptodaily.co.uk/2024/05/preventable-cyber-attack-impacts-ionet"
link_text: "Crypto Daily, “Preventable Cyber Attack Impacts Io.net” (May 2024)"
domain: "cryptodaily.co.uk"
author: "Crypto Daily"
published: "2024-05-05"
fetched: 2026-04-07
tags: ["clippings"]
---

Despite promising that the aftermath of the cyber attack early last Thursday wouldn’t knock their development plans off course, decentralized computing provider io.net has postponed the launch of its $IO token. The company’s CEO Ahmad Shadid tweeted that it would take “about two weeks” to get back on track.

In the cyber attack on the Solana-based decentralized computing project io.net, almost two million fake GPUs were used to mimic the signals sent by genuine GPUs, thus fooling the network into recognizing them as legitimate. This led to incentive program rewards being spent on fake servers and revealed misinformation regarding the actual number of machines in the network. This unfortunate and insidious breach shines a sobering light on the vulnerability of traditional Decentralized Public Infrastructure Network (DePIN) systems. While the specifics of its architecture exacerbate the vulnerability of io.net, this incident underscores the overall security problems of DePIN systems in general.

One company that had foreseen this problem from the outset is the Web3 cloud computing solution Super Protocol. An active NVIDIA partner, the company leverages Trusted Execution Environments (TEEs) - secure computational environments within CPUs or GPUs, that isolate code execution and data processing from the rest of the device. TEEs are impossible to fake, because they are manufactured with unextractable embedded private keys. Unlike unprotected virtual machines, with which hundreds of thousands of fake servers can be inserted into the network undetected, TEE technology supports an attestation process that enables verification of the authenticity and soundness of the execution environment. Thus, TEEs protect the execution environment from outside influences, and guarantee its soundness and configuration, even if the OS or hardware environments are compromised.

Self-sovereign computing is the future of DePIN.

## How Private Keys work


Private keys are generated randomly or pseudorandomly, using cryptography software, which provides the key with a high level of complexity and entropy, making it hack-resistant.


The TEE is manufactured with the private key physically embedded into it, using a special technology called “hardware root of trust” - it is programmed into the one-time programmable memory of the device (eFuses is used in mobile devices). This key cannot be changed, extracted, or copied, even after a device reset.

Importantly, the private key never leaves the TEE. The public key, signed using the Certificate Authority’s (CA’s) private key, which builds a chain of trust back to the CA, is exchanged and distributed; but the private key remains protected inside the TEE, isolating code execution from whatever might be going on outside the shielded environment.


“TEEs are a fortified island of safety amid the raging and predator-filled sea of Web3.” NukriBasharuli, Founder and CEO, Super Protocol


## How Private Keys are manufactured

Processors being made in factories have dark currents, and numerous other absolutely randomparameters. In the area where the TEE is programmed, a function reads these parameters, and generates a random number. After this function is performed, the connection is calcinated to make the private key unextractable (it won’t work otherwise, as the TEE will remain accessible). The key cannot be stolen or cloned without separating the chip into quanta, while also not harming its parameters, which is impossible.

## What's next

The future of DePIN is self-sovereign computing. Super Protocol continues to develop Web3 Cloud solutions with verifiable computation governed by smart contracts and a marketplace for AI solutions and data providers, as well as multi-party data collaboration. One off-shoot possibility that Super Protocol is already in talks with several DePINs about, is the development of Super Domain technology, which would hybridize computational networks by dividing them into nodes managed by Super Domains.

*Disclaimer: This article is provided for informational purposes only. It is not offered or intended to be used as legal, tax, investment, financial, or other advice.*
