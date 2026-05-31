---
title: "The Bill of Rights Ends at the Contractor's Door"
source: "https://drinkyouroj.substack.com/p/the-bill-of-rights-ends-at-the-contractors-door"
author:
  - "[[Justin Hearn]]"
published: 2026-05-28
created: 2026-05-31
description: "Surveillance, speech, biometrics, health data — four domains where the government's constitutional limits come with a vendor workaround."
tags:
  - "clippings"
---
Atlanta’s [open-records response](https://atlpresscollective.com/2025/11/13/atlanta-police-flock-immigration-searches/), released in late 2025, contained two things. The first was a statement: APD (Atlanta Police Department) had not assisted federal immigration enforcement that year. The second was an audit showing 3,254 Border Patrol searches of APD cameras and 3,383 immigration-keyword searches by external agencies, all while the city’s sanctuary policy was in effect.

Both are accurate. The statement governs what Atlanta officers did. The audit documents what the private network answered when federal agencies asked. The Fourth Amendment covers one of those things. The vendor contract covers the other.

![A hand in a formal dark suit cuff reaches across an open doorway to pass a plain manila folder to an unmarked dress-shirt-sleeved hand on the other side. The light is warm amber on the formal side and cold fluorescent on the vendor side. The folder is bisected by the temperature change exactly at the threshold.](https://substackcdn.com/image/fetch/$s_!Iq_w!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16808177-ee59-47fe-871e-e67f6d41917f_2688x1520.png)

The handoff happens at the door. The Constitution doesn’t follow the folder.

## The Glitch: The audit said 3,254 searches. The ordinance said none.

An ATF intelligence specialist named Keya Chavies ran three searches tagged “ERO assist” using APD-issued Flock credentials. Chavies was a federal employee, not an Atlanta officer. Atlanta’s sanctuary policy governs Atlanta officers; it says nothing about what a federal agent can do with Atlanta’s account.

That’s how Flock’s “National Lookup” feature works. Enabling it to query other agencies’ cameras also enables every other agency on the network to query yours. By design. Bend, Oregon Police Captain Brian Beekman discovered this three weeks after his department signed on in June 2025: “What we didn’t know is that National Lookup is a reciprocal sharing feature — when you turn that on, yes, you can query outside your state, but that actually turns on the ability for other agencies in the country to query information from your agency.”

In those three weeks, [federal agencies ran 279 immigration queries](https://www.bendsource.com/news/localnews/federal-immigration-officials-made-279-queries-into-bends-flock-safety-data-in-its-first-three-weeks/) into Bend’s cameras. CBP (Customs and Border Protection) made 118 of them. Flock CEO Garrett Langley had [previously denied the company had federal contracts](https://www.npr.org/2026/02/17/nx-s1-5612825/flock-contracts-canceled-immigration-survillance-concerns); he later acknowledged the company had “inadvertently provided inaccurate information” about its relationship with federal agencies. The inaccuracy covered exactly the period when CBP and HSI (Homeland Security Investigations) pilot programs were running. [Pierce County, Georgia ran four searches](https://atlpresscollective.com/2025/11/13/atlanta-police-flock-immigration-searches/) tagged “Border Patrol Assist” on September 15, one month after Flock announced those pilots had ended.

The Ventura County Sheriff’s Office [disabled National Lookup in June 2023](https://www.cbsnews.com/losangeles/news/flock-license-plate-readers-shared-data-with-out-of-state-federal-agencies/) specifically to comply with California law. Something reactivated it. Without departmental approval or knowledge, federal and out-of-state agencies queried their cameras 364,000 times. Flock said the cause was impossible to determine due to technical logging limitations. The department’s own investigation found no one on their staff had done it. The [Gibbs Mura class action](https://www.classlawgroup.com/flock-safety-license-plate-reader-cameras-lawsuit), filed in San Francisco Superior Court, documented the same architecture at a larger department: SFPD cameras accessed by outside agencies [1.6 million times](https://sfist.com/2026/02/28/lawsuit-says-flock-allowed-out-of-state-agencies-access-to-sfpd-database-1-6-million-times/) in seven months.

The Fourth Amendment requires a warrant for government search of private property. Flock’s cameras record public spaces; the database is privately held. No warrant is required for a government agency to query a private company’s database of recordings of public spaces. A sanctuary ordinance governs what one city’s officers may do; it governs nothing about what any of the [roughly 4,500 credentialed agencies](https://atlpresscollective.com/2025/11/13/atlanta-police-flock-immigration-searches/) on the Flock network may query from that city’s cameras.

Atlanta is one node. There are [4,500 agencies](https://atlpresscollective.com/2025/11/13/atlanta-police-flock-immigration-searches/) on this network. What’s the constitutional limit on any of it?

## The Source Code: How a constitutional limit stops at the vendor contract

Three major protections share the same architecture. The First Amendment prohibits government from ordering speech removed. The Fourth Amendment prohibits warrantless government searches. HIPAA (the Health Insurance Portability and Accountability Act, the federal statute protecting patient health records) governs what counts as protected health information and who can access it. Each one governs what government actors can do directly. The constitutional text is silent on what a private intermediary does when contracted to perform equivalent functions.

CISA (the Cybersecurity and Infrastructure Security Agency, created in 2018 to protect critical infrastructure from cybersecurity threats) ran a program it internally called “ [switchboarding](https://judiciary.house.gov/sites/evo-subsites/republicans-judiciary.house.gov/files/evo-media-document/cisa-staff-report6-26-23.pdf) “: flagging social media content to platforms that acted on it under their own content policies. Director Jen Easterly [defined the information environment](https://judiciary.house.gov/sites/evo-subsites/republicans-judiciary.house.gov/files/evo-media-document/cisa-staff-report6-26-23.pdf) as “cognitive infrastructure” within CISA’s mandate. That framing made content moderation a federal cybersecurity function. The First Amendment prohibits CISA from issuing the removal order. Switchboarding assigned that job to the platform.

Murthy v. Missouri reached the [Supreme Court in June 2024](https://en.wikipedia.org/wiki/Murthy_v._Missouri#Supreme_Court). Barrett’s majority dismissed on standing: plaintiffs couldn’t show that specific platform actions were traceable to government pressure. The constitutional question went unaddressed. The [March 2026 settlement](https://en.wikipedia.org/wiki/Murthy_v._Missouri#Supreme_Court) bars three federal entities from jawboning (informal government pressure on private entities to act in ways it can’t legally compel) for 10 years. It names CISA, the Surgeon General, and the CDC. Every other agency with regulatory leverage over those same platforms keeps the same instrument.

Congress can’t compel disclosure of children’s biometric data directly. Nineteen states have [passed online ID-check laws](https://www.badinternetbills.com/) requiring residents to hand over a driver’s license or a face scan to access age-gated sites, including adult content; the federal [SCREEN Act](https://www.congress.gov/bill/119th-congress/senate-bill/737/text) would extend this nationally. Under each law, the verification vendor holds the biometric database.

National security letters bypass judicial review. Subpoenas require a judge’s sign-off; NSLs don’t. They can reach that database without the warrant the Fourth Amendment would require if government collected the data directly. What that database looks like when it fails: the Tea app breach produced selfies and driver’s licenses on 4chan, with address data [used to pinpoint home locations](https://www.techpolicy.press/age-verification-is-locking-trans-people-out-of-the-internet/).

When therapy session data gets relabeled as a behavioral interest category of users who seek therapy, it exits the HIPAA framework. That relabeling is how therapy records become advertising raw material. BetterHelp made that move; the FTC confirmed it and forced [$7.8 million in consumer refunds](https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-ban-betterhelp-revealing-consumers-data-including-sensitive-mental-health-information-facebook). HIPAA covers the intake questionnaire. The targeting category assembled from it carries no equivalent protection.

The First Amendment prohibits the order. CISA placed the call. The Fourth Amendment requires the warrant. Flock accepted the query. Congress can’t compel the biometric. The verification vendor holds it. HIPAA protects the record. BetterHelp sold the category.

In each case, the constitutional protection was written to govern one party. The government contracted a different party to do the equivalent work.

## The Upgrade: The class action is real. The constitutional fix isn’t.

The [Gibbs Mura amended complaint](https://www.classlawgroup.com/flock-safety-license-plate-reader-cameras-lawsuit) (filed April 3, 2026) grounds the Flock claims in California Civil Code § 1798.90.55(b), the state statute prohibiting ALPR (automated license plate reader) data sharing with out-of-state and federal agencies. The damages floor is $2,500 per violation. At 1.6 million SFPD accesses alone, that’s $4 billion in statutory exposure. [Oregon SB 1516](https://olis.oregonlegislature.gov/liz/2026R1/Downloads/MeasureDocument/SB1516/Enrolled), signed March 31, 2026, restricts Flock data sharing to Oregon agencies and requires public audit reports every 30 days. These are real remedies. They also apply within one state each.

No federal court has held that a government-contracted private intermediary must comply with the constitutional limits that would apply if government performed the function directly. Murthy v. Missouri was dismissed on standing; the constitutional question is unresolved. No legislation at any level currently treats vendor contracts as equivalent to government action for constitutional purposes.

You can settle with CISA. You can cancel Flock. You can challenge the age verification law. The architecture keeps running. The March 2026 settlement names CISA, the Surgeon General, and the CDC; any agency with equivalent regulatory leverage over platforms inherits the same playbook. Ventura County disabled National Lookup in full compliance with state law. Something reactivated it. Each fix stops at the case it was written for.

Right now, the only accountability tool that works is an open-records request. APD’s audit showing 3,383 external immigration searches existed before anyone published a story about it; it became visible because someone asked for it. The Ventura County audit showing 364,000 unauthorized accesses came from the department’s own audit after they discovered the reactivation. Both required someone to ask for the data. Neither required a constitutional doctrine that doesn’t exist yet.

“Follow the vendor” is the working instrument: in any domain where a constitutional right is supposed to limit government action, ask who holds the database and what they require to share it.

## My Debug: I wrote two pieces before the pattern became visible.

“ [The Jawboning Papers](https://drinkyouroj.substack.com/p/the-jawboning-papers) “ ran in October 2025: CISA as censorship mechanism, First Amendment, speech beat. “ [Atlanta Passed a Sanctuary Resolution. The Vendor Contract Didn’t.](https://drinkyouroj.substack.com/p/atlanta-passed-a-sanctuary-resolution)“ ran in April 2026, immigration beat.

Turns out I was covering the same story from two different angles and didn’t notice.

Speech journalists cover CISA. Immigration journalists cover Flock. Child safety journalists cover age verification. Health privacy journalists cover BetterHelp. The pattern that spans all four doesn’t have a beat. Nobody owns it. Each individual piece contains the structural connection to the others (a private vendor doing the work, constitutional limit intact on paper, government one contract away), but making that connection is nobody’s job.

Anyone who builds or contracts infrastructure knows this gap. Policies and contracts live in separate documents. A sanctuary resolution doesn’t talk to the API. A terms-of-service prohibition doesn’t talk to a national security letter. Passing another resolution can’t reach what the contract already promises.

On April 20, 2026, the Atlanta City Council passed [two resolutions opposing ICE detention and requiring new APD guidelines](https://www.atlantanewsfirst.com/2026/04/21/atlanta-council-passes-resolutions-opposing-ice-detention-facilities-setting-police-guidelines/). The city has now passed a sanctuary designation, terminated an ICE detention contract, published an open-records response confirming the audit numbers, and added two more resolutions to the stack. Neither of the April resolutions mentions Flock Safety. Neither touches the vendor contract.

The cameras are still on. The next agency querying them doesn’t need to read any of those documents.

---

*Next Friday: another contract the buyers didn't read. On May 27, 78,000 Samsung workers ratified a ten-year claim on 10.5% of the chip division's operating profit. Every hyperscaler PPA priced against that division was priced before the capture went permanent.*