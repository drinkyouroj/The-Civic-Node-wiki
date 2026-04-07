---
title: "Helium's Dirty Secret - POC Hacking Explained | HNT News | Helium Network Blog"
source: "https://hntnews.org/poc-hacking-explained/"
link_text: "HNT News, “Helium’s Dirty Secret - POC Hacking Explained”"
domain: "hntnews.org"
author: "Hans"
published: "2021-01-12"
fetched: 2026-04-07
tags: ["clippings"]
---

## Hackers Are Costing Helium Miners Tens of Thousands of HNT a Month

Bad actors possibly numbering in the hundreds have falsely asserted their locations so that they can steal money from legitimate miners and users. This is known as a Proof of Coverage Hacking Ring. It’s a relatively simple exploit and unfortunately may become a serious problem as the network grows.

### What Is Proof of Coverage Hacking?

When a miner is started up for the first time, it is required by the blockchain to assert their location on a map. Once that location has been made it cannot be changed without paying a reassert fee. The way the Helium Blockchain verifies the miner location is by relying on other miners to verify the location. They do this by having the original miner send a signal known as a beacon, if the other miners in the area can hear the signal over wireless then they verify the location, and the miners are rewarded. This is known as a POC reward. This reward incentivizes the growth of the network.

Hackers have gotten around this by purchasing a handful of miners and falsely asserting their locations in the same geographic area, but at greater distances than the minimum allowed for rewards, which is about 800ft. There are a few other things that they do to obfuscate their true location, but I don’t want to go into detail on how that’s done because it will just perpetuate the problem. Instead of the beacon traveling over a long distance, it only travels a few feet, guaranteeing a reward without having to actually offer coverage.

### Is There Any Easy Way to Determine if a Miner is Legit?

Yes, as of now, there are some clear signs, although the best way to determine is to do a site inspection and do a signal scan of the area. The quick and dirty method is to use the Helium Coverage Map. Currently, these hackers are actually easy for a trained eye to see on the map. Oftentimes, these hackers place the miners in an evenly spaced way that is apparent. Before showing a Hacking Network, I want to show you what a **legitimate mining network** looks like:

Above is a snapshot from mappers.helium.com that I took. I personally verified the wireless coverage of these miners over the past few days so I can attest to their legitimacy.

Think about it, how does any good idea spread? You know how it goes. One guy buys a miner, then he tells his neighbor next door and they buy one…. Then he tells his brother who lives in the neighborhood across the street….. So you get this organic growth that isn’t perfectly separated…. But that’s not how these hacking networks look.

### Example of a POC Hacking Network

Now for the fakers. Currently, a lot of the hacking networks have these features, but I do think that will change as more people catch on to their methods and they modify their techniques.

Notice how the dots are evenly spaced? That’s not how Miner placement works out. It’s too perfect. Another dead giveaway is the witnesses:

Witnesses are the colored links who vet the purple miner who sent out the beacon to assert it’s location. This rarely happens in the real world. Notice how it looks different from a real-world example of miners?

Now, I wouldn’t just publicly call out a Miner Network for cheating unless I had proof. Before writing this article, I was extremely suspicious of this network. I really wanted to go see if this network was fake or if I was being paranoid, but it was too far of a drive. In a stroke of good fortune, I randomly had a job that required me to drive through this area – so I went and wirelessly sniffed this network with a wireless mapper. After crawling for hours, **I didn’t get one ping**, and I crawled over every single one of those Miners. Here are their names:

- Wide Graphite Orca
- Bubbly Slate Crane
- Blurry Linen Reindeer
- Fierce Mulberry Osprey
- Able Sky Pangolin
- Shiny Peach Swallow
- Long Chartreuse Panda

The miners mentioned above are siphoning HNT from legitimate users to the tune of thousands of HNT (~1.3 USD) and unfortunately, there are many more.

Unfortunately, Wireless Mapping the Helium Network is the only surefire way to determine if hacking has occurred and it is a time-consuming, expensive, and tedious process. There are quite a few other Miners that I seriously suspect may be hacking but I have not yet have had time to crawl. I would REALLY love it if someone in the Georgia area crawls the Gainesville, GA, and Augusta, GA areas to determine if these are hackers or not. Just look at the map:

That’s just too perfect. I’m willing to bet money that this is a fake. If my hunch is correct, this particular network is stealing thousands of HNT coins each month.

### These Hackers Aren’t Stealing From Me So Who Cares?

Well, actually they are, to the tunes of 10’s of thousands of dollars a month. Imagine HNT earnings as a huge pie that miners earn each month, with the size of each slice determined by how large of an area is covered by said miner. The size of the pie does not grow as more miners enter the network – in fact it diminishes. The blockchain rewards users by doing these Proof of Coverage challenges. So if a cheater network falsely grabs a large piece of the pie, even though they are in effect providing zero wireless coverage in return for that slice, they are robbing those miners who are providing wireless coverage.

“

-A Helium MapperYes, It’s Quite Upsetting.”

The saddest part for me is when I go and drive by and map a lone wolf Miner, like this guy:

This poor lone wolf is currently making 7.7 HNT per month, yet they’re providing literally acres of coverage in a highly trafficked area. They are the real heroes…….

*Meanwhile Cons like Blurry Linen Reindeer*

Whom I personally mapped and found them offering zero benefit to users nor offering wireless coverage, are making 182 HNT per month on a bed of lies. And that’s just ONE miner in the hacking ring.

### What Can We Do?

Firstly, we need more people to sniff out these networks. There are quite a few out there. I suggest looking for the signs that I mentioned above and see if you see anything amiss and if it’s not too far please go check them out. Check out the Discord forum for more information, there is even a tab for Helium Mapping. You can build a Wireless Mapper for pretty cheap right now by building a Cubecell HTCC-AB02S. There’s a clone for sale on Amazon for 30 bucks right now. Jas Williams has some excellent firmware available that you can use. The whole process takes some time – you have to setup an account on Helium and modify some config files for it to work, but if you are reading this article (this ain’t exactly People Magazine) you probably have the skills to do it.

Next, it’s important that the Helium team are made aware that POC hacking is a huge problem. And it is a problem that will not go away unless significant fixes are made to the blockchain. It’s just too easy to pull off. It’s much harder to actually build out the network and offer wireless coverage than it is to hack the network.

Think about it…… what’s easier? Buying a few miners and falsely asserting them in a room somewhere and then profiting thousands OR installing antennas, convincing neighbors, and renting out tower space?

### What is Helium Doing?

Well, I think that many of the engineers there recognize that this is a serious problem. That’s exactly why HIP 19 was enacted. HIP 19 requires hardware vendors to lock down the miners and hardcodes the key into the Miner’s Memory. Helium also shut down the DIY miner program as a result of this (I assume anyway). Other HIPS have been passed that did slow down some of the profits too, but it’s been over a month since they passed and many of these illegitimate miners are earning more than legitimate ones.

I personally think that these steps do not go far enough. Even if miners are locked down, people can still do this hack. That’s why additional steps need to be introduced.

### The People’s Network Must Prevail

I want to be clear that I am not knocking Helium. I am actually one of its biggest cheerleaders. It has the chance to become a great example of the blockchain solving a real-world problem instead of just being a “store of value” like so many other cryptocurrencies. But’s it’s important to not over-evangelize the network or turn away from issues that it may face along the way.

The Helium Network has a hard road ahead of it. Bitcoin and other cryptocurrencies have the good fortune of living in a digital fortress, protected by highly structured rules and unbreakable encryption algorithms. Helium does not have that luxury, it must occupy the often messy analog world to deliver on its promise. And I guess that really gets to the fundamental question, can humans build a trustless system built on top of the messy real world? I guess we’re about to find out.

*A Response From a Helium Engineer*

*After this blog was published a Helium Engineer made a response on Reddit. I feel like it’s important to share it here:*
