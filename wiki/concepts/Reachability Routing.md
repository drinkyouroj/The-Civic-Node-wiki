---
title: "Reachability Routing"
type: concept
tags: [legal, jurisdictional-asymmetry, civil-litigation, power]
created: 2026-04-17
updated: 2026-04-18
sources: 13
---

## Definition

The structural tendency of civil legal systems to route liability and process toward the defendant who is reachable — served, jurisdictionally available, asset-holding, identifiable — rather than toward the actor who was the proximate cause of the harm. When those diverge (anonymous foreign actors, encrypted actors, judgment-proof actors, platform intermediaries shielded by immunity), the system does not stop. It reassigns the liability to whoever is nearest.

This is not a malfunction. It is the default behavior of a system designed around the assumption that a defendant can always be compelled to appear, and that the proximate cause of any harm will be coextensive with that compellable party.

## Why It Matters for the Newsletter

The Civic Node's core editorial thesis — that structural outcomes are the unnoticed shape of ordinary systems running normally — finds a clean instance here. Civil litigation is frequently discussed as if it assigns liability to fault. It does not. It assigns liability to *reachable fault*. When the mismatch between proximate cause and reachable defendant gets wide enough (as in cross-border digital harm), the system's routing becomes visible in a way that the ordinary case obscures.

This concept anchors the [[You Can't Sue the Catfish]] article and generalizes to a wider pattern: SLAPP suits against the loud party rather than the original speaker, fraud suits against the local bank rather than the originating crypto wallet, deepfake injuries routed against the distributing platform rather than the originating foreign actor, and — pre-digital — the landlord sued rather than the absentee management company.

## Evidence & Examples

- **[[Doe v. Bonnell (1-25-cv-20757)]]** — the generating case. Proximate cause: anonymous UK catfisher [[Solo (Ben Conway)]]. Reachable defendant: [[Steven K. Bonnell II]], Miami Beach. The case proceeds against the latter because the former cannot be served.
- **Platform immunity as reachability distortion.** Section 230 in US law treats platforms as unreachable for third-party content. This pushes liability back down onto individual users even when the platform's design is the proximate cause of scale.
- **Crypto fraud civil recovery.** Plaintiffs routinely sue exchanges, KYC providers, and downstream recipients because the originating wallet is pseudonymous. The money that *can* be reached gets clawed back; the money in the actual fraudster's control does not.
- **Deepfake and NCII statutes generally.** Written for an ex posting publicly. Do not have an operational concept of an anonymous foreign third-party mediating every interaction.

## Tensions & Counterarguments

- **"Someone has to pay."** The plaintiff's injury is real. If the reachable party is even partially culpable, why not route liability to them? This is a legitimate response. The counter is that *partial* culpability does not map cleanly to *full* liability, and the current routing treats the two as interchangeable.
- **Deterrent theory.** Even if the reachable defendant was not the proximate cause, holding them liable deters the broader pattern (platforms tighten controls, public figures treat intimate media with more care). This is coherent. It is also an admission that the civil system is doing deterrence work on the wrong actor.
- **Reachability is a gradient, not a binary.** Civil process *can* reach foreign witnesses via the Hague Convention and letters rogatory; in [[Doe v. Bonnell (1-25-cv-20757)]], plaintiff has in fact filed a letter rogatory attempt directed at Solo in the UK (see [[Doe v Bonnell continuance motion (ECF 227)]]). The more precise claim is that the mechanism is slow, expensive, jurisdictionally fragile, and evidentially thin — such that the reachable defendant absorbs practical liability before the unreachable mechanism completes. Reachability routing is about *practical* reachability, not legal impossibility.
- **The reachable defendant may actually be liable.** The Doe v. Bonnell complaint alleges a written admission ("fairly close to me"), pattern evidence with 15+ women, and evidence destruction. Reachability routing does not require the reachable party to be innocent — only that the unreachable party generates no liability in proportion to their actual causal contribution, regardless of the reachable party's own culpability.

## Related Concepts

- [[Jurisdictional Asymmetry]] — the structural condition that produces reachability routing
- [[Catfishing as Legal Gap]] — the statutory-design failure that makes reachability routing particularly brutal in NCII cases
- [[Toothless Transparency Laws]] — adjacent pattern in which accountability mechanisms exist but cannot reach the actors they nominally target
- [[Institutional Gaslighting]] — pattern where system failure is reframed as system success

## Key Sources

- [[Doe v Bonnell complaint (ECF 1)]]
- [[Doe v Bonnell continuance motion (ECF 227)]]
- [[Rose deposition — Doe v Bonnell]]
- [[Doe v. Bonnell (1-25-cv-20757)]]
- [[Doe v Bonnell ECF132 — Motion to Dismiss (Abby Subpoena History)]] — fullest articulation of the jurisdictional asymmetry in the case; Bonnell is reachable, Solo is not
- [[Doe v Bonnell ECF139 — Plaintiff Opposition to MTD (False Minor Footnote)]] — Discord CDN reachability theory; Plaintiff's attempt to bridge the April 2022 pre-statute gap via continuous disclosure
- [[Doe v Bonnell ECF210 — Motion for Summary Judgment]] — most complete legal synthesis; shows how reachability routing and catfishing interact in the post-discovery record
- [[Doe v Bonnell ECF216 — Plaintiff Rule 56(d) Motion to Defer MSJ]] — Hague Convention request to depose Göransson in Sweden; practical example of how expensive and slow it is to reach unreachable witnesses even via legitimate process
- [[Doe v Bonnell ECF235 — Bonnell Opposition to Trial Continuance]] — system's practical verdict as of April 2026: the reachable defendant proceeds to trial while the proximate cause is unserved and undeposed
