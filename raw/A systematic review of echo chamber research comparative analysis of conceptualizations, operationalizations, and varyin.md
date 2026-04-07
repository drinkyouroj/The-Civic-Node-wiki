---
title: "A systematic review of echo chamber research: comparative analysis of conceptualizations, operationalizations, and varying outcomes - Journal of Computational Social Science"
source: "https://link.springer.com/article/10.1007/s42001-025-00381-z"
link_text: "Journal of Computational Social Science, “A systematic review of echo chamber research” (2025)"
domain: "link.springer.com"
author: "Hartmann; David; Wang; Sonja Mei; Pohlmann; Lena; Berendt; Bettina"
published: "2025-04-07"
fetched: 2026-04-07
tags: ["clippings"]
---

## Abstract

This systematic review synthesizes research on echo chambers and filter bubbles to explore the reasons behind dissent regarding their existence, antecedents, and effects. It provides a taxonomy of conceptualizations and operationalizations, analyzing how measurement approaches and contextual factors influence outcomes. The review of 129 studies identifies variations in measurement approaches, as well as regional, political, cultural, and platform-specific biases, as key factors contributing to the lack of consensus. Studies based on homophily and computational social science methods often support the echo chamber hypothesis, while research on content exposure and broader media environments, such as surveys, tends to challenge it. Group behavior, cultural influences, instant messaging platforms, and short video platforms remain underexplored. The strong geographic focus on the United States further highlights the need for studies in multi-party systems and regions beyond the Global North. Future research should prioritize cross-platform studies, continuous algorithmic audits, and investigations into the causal links between polarization, fragmentation, and echo chambers to advance the field. This review also provides recommendations for using the EU’s Digital Services Act to enhance research in this area and conduct studies outside the US in multi-party systems. By addressing these gaps, this review contributes to a more comprehensive understanding of echo chambers, their measurement, and their societal impacts.

### Similar content being viewed by others

## 1 Introduction

The impact of social media on public discussions and democratic processes has been a hot topic for more than a decade. It remains relevant with elections taking place in more than 50 countries in the year 2024 (including the United States, India, and the EU), and the introduction of EU regulation on very large online platforms (see the Digital Services Act [1]). The emerging shift to the political right, along with declining trust in democratic institutions and science, raises concerns that the advent of social media platforms may have contributed to these phenomena [2,3,4].

Many believe that the constructs *echo chamber* and *filter bubble* can explain the decline in democratic exchange, as they cause social media users to become polarized (e.g., [2, 5]) and radicalized (e.g., [6]). *Echo chambers*—a term first introduced by Sunstein [7] who repeatedly emphasized the dangers of echo chambers—are frequently defined similarly as “environments in which the opinion, political leaning, or belief of users about a topic gets reinforced due to repeated interactions with peers or sources having similar tendencies and attitudes” [8]. In the context of social media, this involves the interchangeably used but differing concept of filter bubbles. *Filter bubbles*—coined by Pariser [9]—are created by personalized recommendation systems that expose users to content similar to their beliefs. These algorithms rank and moderate content to provide users with a personalized universe of information [9]. Similarly to previous research, we will use the term echo chamber to describe both Sunstein’s construct of an echo chamber and Pariser’s filter bubble. This is due to the similarity in conceptualization and the fact that Sunstein included algorithms in the characterization of echo chambers in later work (see e.g., [10]).

The public discussion around both of these theoretical constructs [11, 12] underscores the need for exposure to diverse viewpoints, which, according to Habermas [13] and Dahlgren [14], is crucial for the public ability to influence politics through a critical exchange of ideas and for consensus-building in democracies. The fear regarding echo chambers on social media arises from users having a vast range of media environments to choose from on the internet. Thus, users can choose to be exposed to conversations with like-minded users and content that reflects their existing preferences or beliefs [11, 12]. According to the *echo chamber hypothesis* [15],Footnote 1 echo chambers in social networks lead to the fragmentation of increasingly polarized groups, which can profoundly impact public debate. There is a growing fear that echo chambers have led or could lead to an epistemological crisis and seriously threaten democratic societies [18].

However, there is conflicting evidence on the existence and effects of echo chambers. Thus, the motivation for conducting this review is the fact that empirical research—especially regarding computation social science—on echo chambers remains inconclusive. The review will address the following research questions:

-
1.
How does academic literature characterize echo chambers in social networks, including their antecedents and effects?

-
2.
How are echo chambers measured (conceptualization and operationalization)?

-
3.
How can the varying outcomes in echo chamber research be explained?


The systematic review offers an overview of antecedents, properties (like existence), and effects of echo chambers in social networks based on research published until December 31st, 2023. We reviewed 129 peer-reviewed studies. From an initial set of 1,706 studies, we selected these 129 studies based on criteria explained in Sect. 3.4. We identify a taxonomy of conceptualizations and operationalizations of echo chambers and determine antecedents and effects that organize existing work and support future studies. This analysis aims to highlight certain assumptions and choices in the research design of echo chambers. We find that studies differ in (1) outcomes, (2) focus, (3) construct conceptualization and (4) operationalization, and (5) granularity.

Like Jacobs and Wallach [19] in the case of fairness, we propose to use measurement modeling from the quantitative social sciences [20] to discuss the echo chamber construct and to compare conceptualizations and operationalizations of echo chambers. We argue that employing measurement modeling can help clarify how research defines and measures the concept of an “echo chamber” and how this is linked to the differences we observe in research outcomes.

Furthermore, we argue that a broader perspective on antecedents, properties, and effects of echo chambers as a concept is essential to understanding the sociotechnical structure and mechanisms of social media. We understand social media and recommendation technologies as sociotechnical systems embedded in a complex, dynamic political and social system that may have multiple feedback loops. A multi-perspective and multi-granular (individual level, structural level) approach to the topic is crucial to promote the understanding of these structures and their reproduction by such systems. This distinguishes this review from existing reviews on echo chambers [15, 21], echo chamber detection [22], filter bubbles [23], and social media [4].

Our review identifies variations in measurement approaches, and regional, political, cultural, and platform-specific biases as key factors contributing to the lack of consensus. Studies based on homophily and computational social science methods often support the echo chamber hypothesis, while research on content exposure that analyzes broader media environments tends to challenge it.

## 2 Related work and contribution

In 2021, Terren and Borge [15] conducted a systematic review to explore the existence of echo chambers in social networks. Similar to this systematic review, it aimed to provide a better overview of the current research (up to January 2020) and identify differences in research approaches. The authors examined 55 studies related to the existence of echo chambers in social networks. They found that differences in research design impacted whether the studies concluded that echo chambers exist in social networks. In particular, different data sets on which the research was conducted produced different results. Trace data clearly showed the existence of echo chambers, whereas self-reported data from survey studies did not [15]. While Terren and Borge [15] sorted existing echo chamber literature by data set and foci, referring to foci such as interaction-centric studies and content-centered studies; they only provided a summary of studies that explicitly referred to the echo chamber hypothesis. In contrast, the present study provides a more comprehensive analysis of echo chambers and social media, including antecedents, properties, and effects of echo chambers and their measurement.

Furthermore, non-systematic literature reviews on echo chambers, filter bubbles, and thematically related phenomena exist. Arguedas et al. [21] examined social science evidence of online echo chambers’ existence, antecedents, and effects. They found no evidence for the echo chamber hypothesis and presented a mixed picture of how news and media affect polarization. Kitchens et al. [24] outlined several potential reasons for the divergent and conflicting findings related to echo chambers. However, their method was a trace data analysis, not a review study.

Lorenz-Spreen et al. [4] analyzed nearly 500 articles on the impact of digital media on democracy, including examining echo chambers. Findings are mixed: while social media platforms are shown to diversify news consumption, they also contribute to the formation and confirmation of ideologically similar social groups. They suggest a link between the increased knowledge through digital media and the rise of homophilic social structures, which may relate to the spread of hate speech and anti-outgroup sentiments. The systematic review of Interian et al. [25] examined network polarization measures of 78 studies and identified the most used ones in research on online social data.

In summary, variations in research design have played a critical role in shaping conclusions about the existence of echo chambers in social networks. Differences in datasets used across studies have led to inconsistent results, with much of the evidence relying on data collected in 2020. Key open questions include the need for updated evidence on the antecedents, existence, and effects of echo chambers up to December 31, 2023, a comprehensive review of how echo chambers are measured, and an analysis of how measurement approaches influence research outcomes beyond the choice of datasets. Our work builds on these findings, incorporates evidence published in recent years, and provides novel insights into echo chamber research.

Furthermore, this review expands the scope of analysis by examining diverse conceptualizations and measurement methods of echo chamber phenomena, highlighting their impact on research conclusions. By advancing the theoretical understanding of echo chambers, refining measurement practices, and situating their study within broader methodological frameworks, this work contributes meaningfully to the field. Importantly, it offers actionable recommendations for both research and policy, underscoring the need for precision in measuring echo chambers to improve our understanding of their dynamics and implications.

## 3 Method

We follow the *PRISMA 2020* [26] guideline to present a transparent account of how we conducted our systematic review. A systematic review following the PRISMA 2020 guideline involves the following elements [27, 28]: (1) a definition of research questions (see below), a strategy regarding the search for relevant literature to answer these questions (Sect. 3.1), explicit criteria for inclusion and exclusion of research literature (Sect. 3.4.3), synthesis of evidence that can be derived from the literature (Appendix), and a summary of the results presented in a structured manner (Sect. 4).

To allow for reproducibility, we make all steps of the reviewing process explicit and describe them in detail. Our research questions are conceptual questions and methodology questions, as we are both interested in how echo chambers are conceptualized and what methods have been used to study them, to find how the varying outcomes in the literature emerge [29].

We use standardized methods for search, evaluation, and selection of studies reduce subjective influences [30]. The search strategy is discussed in more detail in Sect. 3.1. It includes keywords and scientific databases we identified as relevant to the search, which we lay out in Sect. 3.2. The criteria for inclusion and exclusion of papers are presented in Sect. 3.5. The PRISMA 2020 flow diagram is depicted in Fig. 1.

### 3.1 Search protocol

While formulating the search string, we aimed to reduce the number of irrelevant results. Some searches, such as “echo chamber” as a keyword, produced too many results. Other terms, such as “echo chamber hypothesis” or “existence” were too limiting and returned only a few results. Keywords were refined iteratively. Two main groups of keywords that identified broad and relevant research were merged, reducing irrelevant results. The first group included the keywords “echo chamber” and “filter bubble”. The keywords of group one are presented in Fig. 2.

To keep the review focused, terms like “selective exposure”, “content exposure”, “recommendation algorithms” were not included. Using these keywords for searches resulted in more than 10,000 results.

The second group of keywords, presented in Fig. 3, exclusively contained all keywords related to social media platforms. After careful consideration regarding the inclusion of publications not written in English, we decided to remove these studies from the corpus. This was done to improve transparency of our analysis and synthesis, as not all readers can read German. Nonetheless, we want to emphasize the importance of publications written in other languages and have added citations for those studies excluded due to not being written in English. The second group included names of the most used social media platforms as of April 2024 [31]. This inclusion guaranteed that individual studies on specific platforms were taken into account. To avoid a search query that was too restricted, keywords were searched for in both titles and abstracts.

### 3.2 Databases

After reviewing the most-used databases for computer science [32] and social science, the following databases were chosen: Web of Science, Scopus, ACM, IEEE, Google Scholar, and DBLP.

Although Google Scholar does not have a main search system to compile research, it offers extensive coverage and serves as a comprehensive collection of scientific knowledge, including a large amount of grey literature - which refers to literature outside traditional publishing sources, such as dissertations, reports, and pre-prints [33]. This can help counteract publication bias [34]. While we only include peer-reviewed literature in our review, adding Google Scholar articles has expanded our sources.

Search precision for systematic searches in Google Scholar is much lower than one percent [35]. For our query, Google Scholar returned 20,000 results. Therefore, Google Scholar was only used as a supplemental database, and its search query results were trimmed to 300 results (an amount deemed relevant for systematic reviews according to Haddaway et al. [34]).

### 3.3 Search results

Database searches yielded a total of 1,706 results. Each source’s bibliographic information and abstract were downloaded into a single Citavi library.Footnote 2 Citavi was used to remove duplicates during the inclusion and exclusion process and to code papers in the screening phase. 514 duplicates were removed. Furthermore, only peer-reviewed work was included as justified in Sect. 3.4. This selection resulted in 1,051 unique publications that were then screened for eligibility.

### 3.4 Identification and screening scope

#### 3.4.1 Peer-reviewed work and publication bias

We want to briefly discuss potential biases that can occur in systematic reviews and how they apply to this one. The likelihood of publication bias is one of the possible drawbacks of systematic reviews [30]. Publication bias refers to the tendency of researchers, reviewers, and editors to submit or accept articles for publication based on the direction or intensity of the study findings.

Consequently, journals may tend to prioritize publishing data with substantial or positive findings, skewing the balance in favor of such results [36]. This bias can influence systematic reviews, which often include only peer-reviewed papers to manage research volume and reduce potential small-study biases. However, retrieving unpublished data to address this issue is time-consuming, labor-intensive, and may not always yield reliable information.

While accessing unpublished data can supplement the review of published literature, it remains ineffective in fully mitigating publication bias [36]. Given this bias, it is plausible that studies presenting negative findings related to the echo chamber hypothesis or its effects face greater challenges in achieving publication compared to studies with positive results. In this context, our work makes a deliberate effort to emphasize and include negative results, contributing to a more balanced understanding of the topic.

#### 3.4.2 Other potential biases in systematic reviews

Location bias refers to the publication of research findings in journals with varying accessibility to researchers and levels of indexing in standard databases. For this review, accessibility bias occured, since we found 11 studies that were inaccessible to us during the screening phase. While these studies have a low citation count, we recognize that their exclusion could still introduce bias and potentially overlook valuable perspectives.

Language bias occurs when research findings are published in a specific language based on the type and direction of the results. In this review, we only used English keywords and included studies written in English for transparency and reproducibility reasons. This means that studies relating to certain countries might be excluded from our corpus and there could be results relating to non-English speaking countries and the Global South that are not included in our analysis. Outcome reporting bias involves selectively reporting some outcomes while omitting others based on the kind and direction of the findings [37]. Due to the large amount of studies, we cannot discuss each in detail. By compiling the outcomes of studies in a table in the “Appendix” we aim to give an overview of the studies’ diverse methodologies, results, and conceptualizations.

#### 3.4.3 Inclusion and exclusion criteria

Exclusion criteria were applied in the search for evidence; the inclusion criteria were the negations of the exclusion criteria. Our exclusion criteria (C1-C3) are presented in Table 1. Criterion C1 is based on our research questions. Due to the difficulty of comparing qualitative and quantitative research, we only included papers that use quantitative methods with observational data, surveys, mixed methods, and experiments (see C2). While we discussed the existence of echo chambers in different media, such as television or newspapers, our focus is on echo chambers in social media to allow for comparisons between studies, as formulated in C3.

### 3.5 Screening of search results

The identification of studies and the screening process in the PRISMA 2020 format can be seen in Fig. 1. During the screening process, the eligibility criteria were applied in a hierarchical cascade method, with each source being verified first against C1, then against C2, and then against C3. A total of 1,051 studies were screened based on title, excluding 655 studies that did not meet the three criteria. Most papers were excluded based on criterion C1. During the first screening round, we decided if an article was eligible based on its title. This step was conducted through one coder (the first author) who flagged articles to be discussed with a second coder (the second author) to discuss whether an exclusion is warranted. In this phase, only clearly out-of-scope articles, like articles on physical echo chambers, were excluded. In the subsequent screening round, articles were excluded based on their abstract. To calculate Inter-coder reliability (ICR), 20 % of articles were coded by a third coder (the third author) who was unfamiliar with the previous discussions [38, 39]. The agreement between the coding conducted by the first author and the third author—student researcher—was moderate, and differences were then discussed. After the adjustment, the value for Cohens’ \(\kappa\) was 0.62 [40], meaning a substantial agreement.

### 3.6 Analysis and synthesis

The final full-text coding followed an inductive approach to content analysis, as research on echo chambers is dispersed and inconclusive [41]. Codes were established without a preconceived theoretical framework and then grouped into categories concerning conceptualizations and operationalizations of echo chambers, as well as findings concerning antecedents, properties, and effects [42]. An example of a code that was inductively formed is “Focus and Granularity” (see 2) for all codes and subcodes). During the coding process, it became apparent that there are significant differences between studies in regards to these two aspects. Some studies look at specific groups, others focus on individuals and their behaviourial patterns. Some studies are focused on one platform, others focus on multiple platforms. We wanted to highlight these differences since platform design can influence the behavior of users [43]. Other codes were also formed based on the intention to highlight similarities and differences (e.g. type of data used). A short version of the codebook is presented in Table 2.

After the codebook was established through an initial coding round and discussions between the first author and second author, the third coder independently coded 19 random studies (roughly a 15 % sample [39]). Here, ICR was substantial (Cohen’s \(\kappa = 0.66\)Footnote 3). We used MAXQDA for coding.Footnote 4

Cohen’s \(\kappa\) is a statistic used to measure the level of agreement between two coders while accounting for the agreement that could occur by chance. For our study, it was calculated by comparing the primary codes assigned by the first and third coder to a subset of the articles, focusing on the categories of antecedents, existence, and effects. The observed agreement was then adjusted to reflect the likelihood of random agreement, resulting in a Cohen’s \(\kappa\) value of 0.66, indicating substantial agreement.

Conducting a meta-analysis would not have been possible on the included papers, as research designs across identified studies are not similar [44]. To organize the results of our synthesis, we instead follow a narrative synthesis approach with bibliometric features, which is suitable to show relationships in and between quantitative studies using diverse methodologies and different conceptualizations to identify factors that can explain differences [44, 45].

We discuss these relationships by giving an overview of the type of data and datasets used and the context of the studies, such as the country. We group studies by conceptualization, methodology, and outcome.

## 4 Results

In this section, we start by giving a brief corpus overview and then present the results of our analysis in sections corresponding to the research questions.

The 129 studies included in the systematic review were all published between 2014 and 2023, as Fig. 4a illustrates. The year of publication was not restricted in the search query for this review. The distribution of the identified studies across different publication sources demonstrates the interdisciplinarity of this topic but also represents the need to systemize operationalizations (see Table 5 in the “Appendix”).

In this review, conceptualizations refer to the theoretical frameworks that define and explain the phenomenon. These include homophily, which describes the tendency of individuals to associate with like-minded others, content exposure, which examines the diversity or narrowness of information individuals encounter, and user behavior versus group behavior, which distinguishes between individual-level dynamics and collective patterns within online communities.

Operationalizations, meanwhile, are the methods employed to measure and analyze these conceptual frameworks. Common approaches include computational social science (CSS) methods, such as network analyses and algorithmic modeling, which leverage large-scale digital data; surveys, which capture self-reported behaviors and attitudes; experiments, which create controlled environments to test causal effects; and mixed-method studies, which combine qualitative and quantitative approaches to provide a more comprehensive understanding.

### 4.1 Evidence supporting the existence, antecedents, and effects of echo chambers in social networks (RQ1)

#### 4.1.1 Existence of echo chambers

In the following, we discuss evidence for the echo chamber hypothesis, mixed results, and counter-evidence. We will include findings on specific platforms. Figure 4b presents an overview of platforms when specific platforms were researched in a study. Looking at which platforms are studied shows that some platforms are studied in many publications, while other platforms appear only in a few. This is related to available APIs—we will come back to this in the discussion—and leads to the fact that not the most popular platforms [46] were studied; instead most studies analyzed Twitter/X or Facebook, although Facebook is only in the top 10 of platforms with the most users on social media.

Overall, the range of outcomes in echo chamber research points to a divergence of outcomes regarding the existence of echo chambers, how pronounced the phenomenon is in various communities or platforms, and what consequences its presence has. Despite contesting results, the overall findings support the echo chamber hypothesis.

##### 4.1.1.1 Evidence supporting echo chamber hypothesis

A significant body of research (\(n= 76\)) demonstrates attitude-based homophily in social media. This means that in these studies, clusters of users around shared values, attributes, or beliefs were identified. This phenomenon is particularly pronounced in segregated networks, such as “scientific” vs. “conspiracy” communities [47,48,49,50], and among groups divided by *political affiliation*, such as Democrats and Republicans. Studies examining major political events, including the 2015 Polish elections [51], the impeachment of Brazilian President Dilma Rousseff [52], and the 2016 U.S. elections [53], also support the echo chamber hypothesis, showing pronounced clustering in user interactions.

On Facebook, research highlights the prevalence of homophilic news consumption patterns. Users often consume partisan content, reinforcing existing beliefs [24, 54]. For example, Cinelli et al. [17] found that Facebook facilitates the formation of segregated communities with limited exposure to cross-cutting content, especially compared to Reddit.

Twitter/X studies similarly document echo chambers, particularly in retweet networks. Polarization often arises during contentious events, such as elections, where users amplify content from ideologically aligned sources [55, 56]. Figure 5 displays the outcomes for each platform and demonstrates that most research for Facebook and Twitter/X supports the echo chamber hypothesis on these platforms.

##### 4.1.1.2 Mixed results

Several studies (\(n = 27\)) documented mixed results, meaning they found segregated communities or tendencies for echo chambers, but only under certain circumstances, assumptions, or partially in specific communities. Such studies found segregated communities in the Catalan parliamentary relations network on Twitter/X but not in the retweet network [57], on specific political events where users tend to group themselves around authority hubs but only for these events [56], in the Hungarian Twitter/X follower-followee network but not in the Polish one [58], and in the Subreddit on the Men’s Rights Movement Online [59] but not in all Subreddits [24, 60,61,62].

*Platform design* plays a significant role in shaping echo chamber tendencies. For example, Reddit’s customizable recommendation algorithms encourage exposure to diverse viewpoints, reducing echo chamber effects compared to Facebook [17, 61, 63]. However, echo chambers were partially observed in specific Subreddits [59], as mentioned previously.

Comparative studies, such as Kitchens et al. [24], found that Facebook users tend to consume more partisan news than Reddit users, who encounter greater content diversity. Twitter/X occupies a middle ground, with users showing limited changes in exposure to opposing views over time. Nikolov et al. [54] also observe that content bias varies by platform, suggesting the impact of platform design on echo chamber formation.

In our corpus, only a few studies examined short video platforms like Instagram and TikTok, likely due to barriers such as limited access to APIs and the complexities involved in analyzing video content. However, a study by Gao et al. [64] analyzed platforms such as Douyin, TikTok, and Bilibili, demonstrating how feed algorithms foster selective exposure and homophily, ultimately contributing to echo chamber formation, while also highlighting that cultural differences can correlate with the development of echo chambers and their influence is not equivalently likely for each community and culture.

Another important dimension is *user behavior*, particularly how engagement and media consumption habits influence the formation of echo chambers. User engagement has been found to correlate positively with echo chambers and political affiliation. The survey by Dubois et al. [65] found that political involvement and media variety reduce the risk of being in an echo chamber. They find that the amount of media a person consumes is anti-proportional to their chance of being trapped in an echo chamber, which contradicts findings by CSS studies [48, 50, 66, 67] that find that engagement and echo chambers are positively correlated. Greater media diversity reduces the likelihood of echo chamber formation, as studies such as Boulianne et al. [16], Dubois et al. [65], Jones-Jang and Chung [68], Burnett et al. [69], found only minimal indication of echo chambers when examining the complete multi-media environment. Many studies found a small echo chamber effect for Republicans, but none for Democrats before and in the aftermath of the 2016 U.S. election [70,71,72,73].

##### 4.1.1.3 Counter-evidence

In contrast, 26 studies provide little to no support for the echo chamber hypothesis. On Facebook, Beam et al. [74] found that users exposed to newsfeeds experienced depolarization over time, suggesting that social media could reduce rather than reinforce ideological segregation. Similarly, Eady et al. [72] and Barbera et al. [75] observed significant ideological overlap among the most liberal and conservative users, contradicting the assumption of rigid polarization.

In general, studies examining the broader media environment including newspapers and TV do not find substantial evidence for echo chambers. For instance, Nordbrandt [76], Nyhan et al. [77] observed that while social media usage does not directly influence affective polarization—the individuals’ sympathy or antipathy toward specific political parties—prior patterns of social media engagement can shape this relationship. Similarly, Dubois and Blank [12] demonstrated that users with more diverse media consumption habits are less likely to become trapped in echo chambers, as varied exposure to information promotes openness to differing viewpoints and, again, politically engaged users are particularly resilient to echo chambers, with their media choices further mitigating risks of ideological isolation. Supporting this, Bail et al. [2] further challenge the polarization assumption, showing that social media use can increase exposure to non-partisan content.

Reddit and Weibo present unique counter-evidence. On Reddit, studies find minimal evidence of echo chambers due to platform features encouraging cross-cutting exposure [17, 61, 63]. On Weibo, Wang et al. [78] observed that retweeting mechanisms promote polarization, while commenting fosters consensus, highlighting the importance of interaction types in shaping polarization dynamics. Cross-platform comparisons further highlight the influence of platform characteristics on echo chamber formation. For example, Masip et al. [55] showed that Twitter/X users are exposed to more diverse viewpoints than Facebook users.

#### 4.1.2 Antecedents

This section examines the antecedents of echo chambers, i.e. what leads to the formation of echo chambers, focusing on group and user behavior, content moderation and recommender systems, as well as polarization and fragmentation. These factors were most present in the corpus as potential contributors to the formation and persistence of echo chambers.

##### 4.1.2.1 Group behavior

Certain group behaviors and attributes contribute to the emergence of echo chambers. Behaviors such as avoidance, unfriending, and discreditation are mechanisms that reinforce group cohesion by excluding opposing views. Studies operationalize these behaviors through concepts like the spiral of silence (i.e., the theory that people fear isolation and, therefore, fear speaking out against mass media opinions) and affective polarization (i.e., people’s emotions become more positive towards members of their own party or own community than opposing groups). Although group behaviors play a role in echo chamber formation, few studies have investigated them comprehensively or as antecedents of the construct.

*Avoidance and Discreditation*: Neely [71] found that political leanings and perceived credibility influence avoidance behaviors, particularly among Republicans, during the 2020 U.S. elections. Avoidance often manifested in politically motivated unfriending, driven by discreditation of opposing views. Similarly, Lin et al. [79] demonstrated that cross-cutting discussions can paradoxically heighten affective polarization through unfriending, with this effect exacerbated by exposure to incivility on social media.

*Self-Censorship:* Some studies such as Burnett et al. [69], Powers et al. [80] applied the spiral of silence theory to social media, suggesting that platform dynamics might invert traditional silencing mechanisms. This inversion allows a vocal minority to overshadow the silent majority, particularly in ideologically polarized contexts. Burnett et al. [69] highlights significant ideological differences in self-censorship practices and fears of isolation, showing how political identity influences individuals’ willingness to engage in public discourse which is as we have demonstrated correlated to echo chamber formation. Accordingly, Powers et al. [80] observed that college students avoid expressing political opinions online to protect their civic identity, reflecting a strategic approach to maintain social harmony in ideologically congruent networks.

*Counter-Evidence:* Contrarily, Beam et al. [74] reported that exposure to counter-attitudinal news on Facebook could promote depolarization, challenging assumptions about affective polarization.

Although group behaviors play a role in echo chamber formation, few studies have investigated them comprehensively or as antecedents of the phenomenon.

##### 4.1.2.2 User attributes and behavior

Selective exposure, demographics, emotions, and personality traits have been identified as key factors in echo chamber formation that we summarize under the category of user attributes and behaviour. Although selective exposure is the most studied and affirmed contributing factor among these user behaviours, it remains unclear how selective exposure and recommendation systems interact with each other, given that previous studies have focused on one or the other. Interestingly, despite the tendency for selective exposure, many users still consume a variety of content through diverse media channels [12]. This can even amplify the echo chamber effect since exposure to counter-opinions may reinforce one’s opinion when combined with avoidance and discreditation as described before [81]. Consequently, some studies analyzed demographics, emotions, and personality traits as antecedents of echo chambers.

*Selective Exposure:* Users often choose content that aligns with their existing opinions, reinforcing confirmation biases. However, as Dubois et al. [65] notes, exposure to diverse media and political engagement can counteract this tendency, reducing echo chamber risks.

*Demographics and Personalization:* Bodo et al. [82] highlighted that younger and less educated users are more susceptible to personalized content, potentially limiting exposure to diverse viewpoints. Conversely, political interest and efficacy are associated with a reduced likelihood of being in echo chambers [83].

*Personality Traits:* Studies found that traits such as openness to experience and extraversion correlate with greater exposure to diverse viewpoints, while introversion and conscientiousness are linked to like-minded discussions [84, 85].

These findings suggest that while user behavior and individual attributes play significant roles in echo chamber formation, they also offer pathways to mitigate such effects through active engagement and media diversity.

##### 4.1.2.3 Content moderation and recommendation systems

recommendation systems and content moderation are frequently cited as primary drivers of echo chambers due to their role in shaping user content exposure.

*Platform-Specific Differences:* Studies comparing Reddit and YouTube demonstrate stark differences. Findings show that Reddit’s customizable algorithms reduce echo chambers by encouraging diverse exposure [63], while YouTube’s recommendations amplify far-right content, fostering echo chambers [60, 86].

*Algorithmic Effects: *Hilbert et al. [87] emphasized the influence of initial network creation by recommendation systems, which can embed users in echo chambers depending on their initial interactions.

*Limited Research on Moderation:* Despite the critical role of content moderation, few studies have explored its relationship with echo chambers due to restricted access to platform data about how content moderation works and how content is deleted and recommended [88].

While evidence suggests that recommendation algorithms significantly influence echo chambers, gaps remain in understanding the interplay between moderation practices and echo chamber dynamics.

##### 4.1.2.4 Polarization and fragmentation

The relationship between societal polarization, fragmentation, and echo chambers is complex and often correlational rather than causal.

*Offline-Online Interaction:* Bright [89] found that offline political success correlates with detachment (isolation of political actors) in online networks, suggesting that online fragmentation is not solely a product of digital interactions but also reflects offline political dynamics.

*Geographic and Community Influences:* Bastos et al. [90] demonstrated that Brexit-related echo chambers had strong geographic and offline community influences, highlighting the interplay between online and offline environments. Aligning with Mahrt [91] that demanded more research on cultural context and polarization, novel research [61, 64, 92] finds that culture or demographics drive polarization and echo chambers.

These findings emphasize the need to account for offline contexts when studying echo chambers and suggest that future research should integrate online and offline dynamics to better understand these relationships.

#### 4.1.3 Effects of echo chambers

This section synthesizes the documented effects of echo chambers, focusing on their role in polarization, the spread of misinformation, and their potential to amplify extremism.

##### 4.1.3.1 Polarization and fragmentation of the public sphere

Nearly a third of the included studies in the corpus identify polarization as an effect associated with echo chambers. Polarization, a phenomenon where individuals with similar beliefs converge more strongly while those with opposing views diverge further, has been central to these studies [25]. Researchers predominantly operationalized polarization through political leaning metrics, calculating the distance between the mean political leanings of opposing communities. Additional measures include:

*Affective polarization:* which captures the degree of emotional divides between groups, such as hostility or negative sentiments toward opposing ideologies [4] was studied by many studies that focused on group or user behavior.

*Bimodality coefficients and homophily:* assessing the clustering of users based on shared characteristics or beliefs. Many studies demonstrated that shared partisanship increases the likelihood of social tie formation on platforms like Twitter, reinforcing homophily (e.g., [93,94,95]). Similarly, studies of vaccine debates on Facebook reveal how polarized communities emerge around pro- and anti-vaccine content, driven by selective exposure [49], which is similar in climate change debates [94] and in “science” and “conspiracy” communities [96]. However, these communities might have been polarized from the beginning.

*Challenge avoidance and reinforcement seeking:* Both are cognitive mechanisms that explain the persistence of polarized behavior. Studies (e.g., [97, 98]) found that these mechanisms, paired with peer influence, promote the formation of tightly clustered subgroups within echo chambers. Reinforcement-seeking amplifies group coherence by encouraging users to engage with content that aligns with their preexisting beliefs, while challenge avoidance leads users to ignore dissenting information, deepening polarization.

*Counter-Evidence:* Nordbrandt [76] challenged the assumption that social media drives societal polarization, instead proposing that existing polarization shapes social media usage patterns. This finding aligns with findings by Monti et al. [61], Gao et al. [64], and Grusauskaite et al. [92] who find that culture or demographics drive polarization. Furthermore, Nyhan et al. [77] found that although exposure to like-minded content is prevalent on Facebook, reducing such exposure during the 2020 US presidential election had no measurable effect on polarization in beliefs or attitudes.

On the other hand, fragmentation, measured through the size and density of communities across entire platforms, has been comparatively understudied. While fragmentation reflects the structural segmentation of networks into isolated clusters, it has not received the same analytical attention as polarization.

Despite diverse operationalizations, the majority of results are consistent with the echo chamber hypothesis: echo chambers contribute to both polarization and societal fragmentation. However, novel studies from 2023 also highlight that polarization may stem from other factors, such as traditional media, cultural differences, demographics, or other offline influences, complicating the attribution of causality solely to social media.

While the relationship between polarization and echo chambers has been widely explored, the causal direction of this association remains unclear, as most studies focus on echo chambers increasing polarization and fragmentation—aligning with the echo chamber hypothesis—and use correlational methods. However, the study by Nyhan et al. [77] demonstrates using a randomized controlled experiment that reducing exposure to like-minded sources may not significantly alter polarization, further questioning the causal role of echo chambers in driving societal divides. Strategies to mitigate polarization, such as algorithmic interventions or promoting diverse interactions, are discussed by Interian et al. [25] as potential recommendations for addressing these issues [25].

##### 4.1.3.2 Spread of and belief in misinformation

Echo chambers are closely tied to the belief in and spread of misinformation. Twenty-three studies in the corpus address this connection, with seven focusing explicitly on misinformation in the context of echo chambers.

*Homophily and Content Distribution:* Del Vicario et al. [48] found that users on Facebook cluster around two types of pages, "conspiracy" and "scientific," selectively consuming and distributing content aligned with a single narrative while ignoring conflicting information. The authors argue that homophily is a key driver of content dissemination and that polarization within these communities exacerbates the spread of misinformation. Notably, the first two hours of an information cascade are critical for developing opinion clusters.

*Influential Users and Information Cascades:* Specific hub nodes play a pivotal role in spreading misinformation within networks and shaping echo chambers [99]. For example, Choi et al. [100] found that a small number of highly connected users are responsible for a significant portion of misinformation spread, with 10% of hub communities generating 36% of retweets of false information. These findings highlight the importance of early cascades and densely connected nodes in amplifying misinformation.

*Polarized Consumption:* Schmidt et al. [66] analyzed anti-vaccination communities and found that users tend to exclusively consume and share polarized content, either supporting or opposing vaccinations. This behavior has gained heightened attention since the COVID-19 pandemic, generating substantial research on echo chambers and misinformation.

In summary, misinformation is intricately linked to echo chambers, with highly connected and influential users driving both phenomena. Research emphasizes the importance of focusing on these nodes when studying the spread of false information.

##### 4.1.3.3 Potential for increasing populism and extremism

14 studies in the corpus investigate the relationship between echo chambers and extremism, examining how homophily and algorithmic amplification contribute to radicalization.

*Algorithmic Influence and Weak Ties:* Wolfowicz et al. [101] analyzed trace data from ego-centric networks on Twitter/X and found that recommendation algorithms often suggest accounts aligned with users’ ideological profiles. While these weak ties expose users to radical ideas, the lack of reciprocal connections may limit deeper engagement. Similarly, Torregrosa et al. [6] observed that network relevance is associated with extremist content, highlighting the role of user connections in spreading radical ideologies.

*Homophily and Political Ideologies:* Boutyline and Willer [73] found that conservatives in the U.S. are more homophilic than liberals on Twitter/X, with conservative homophily rates 3.8 times higher. This structural advantage makes conservative groups more prone to echo chambers and potential radicalization. Homophily appears to facilitate mobilization within politically extreme groups.

*Selective Communication:* Bright [89] found that individuals with radical beliefs tend to limit their interactions to like-minded individuals, avoiding discussions with those holding opposing or more moderate views. This selective communication reinforces echo chambers by deepening ideological isolation.

*Platform-Specific Differences:* Whittaker et al. [60] used sock puppet accounts to study recommendation systems across platforms. They found that YouTube amplifies extreme and fringe content through algorithmic recommendations, while Reddit and Gab do not exhibit the same patterns. The findings underscore the need for policy interventions to address algorithmic amplification of extremism.

*Counter-evidence:* Not all studies support this connection. Boulianne et al. [16] found no evidence that social media increases support for right-wing populism, suggesting that online behavior often reflects existing offline communities rather than driving polarization or radicalization.

### 4.2 Measurement of echo chambers (RQ2)

From the perspective of measurement modeling, “echo chamber” is a theoretical construct. It describes a phenomenon observed in online and offline communities that cannot be directly measured. Instead, researchers rely on measurable proxies that serve as indirect indicators of echo chambers. Conceptualization involves defining the theoretical construct of an echo chamber in terms of measurable concepts, while operationalization is the process of translating these concepts into concrete, observable measures [19].

In the following sections, we provide an overview of the various conceptualizations and operationalizations of echo chambers in the literature. We distinguish operationalization into two components: the method of measurement (e.g., network analysis, sentiment analysis, or surveys) and the granularity of measurement (e.g., individual behaviors, group dynamics, or platform-wide patterns). Granularity acts as a link between conceptualization and operationalization, shaping how abstract concepts about echo chambers are transformed into specific, observable phenomena.

#### 4.2.1 Conceptualizations

We identified four key concepts integral to echo chamber conceptualizations: (1) *homophily*, (2) *content exposure*, (3) *individual user behaviors*, such as selective exposure, confirmation bias or fear, and (4) *group behaviors*, including exclusion of outsiders and collective unfriending. Another dimension in the definition and then measurement of echo chambers is the granularity of the echo chamber, meaning how granular we define and measure echo chambers. We will explore how these concepts intersect with theoretical frameworks, providing an overview of the predominant conceptualizations within the corpus.

Although both echo chamber and filter bubble as concepts were established due to concern that social media and other information-gathering platforms could influence people’s decisions about what they consume, what they think, and how they interact, the study field has conceptualized them in different ways. According to Pariser [9], personalization technology is the underlying mechanism of echo chambers, and he contends that this technology will show users information that confirms their own opinions at the expense of information that challenges them. The isolation of the individual has negative effects, as it leads to epistemic bubbles where personal ideas go unchallenged and untested [102]. This is why many studies put more focus on the content that an individual sees through their news feed curated by recommendation systems. We call this conceptualization *content exposure*.

Both in 2001 [7] and then again in 2017 [10], Sunstein emphasized that technology has the potential to increase fragmentation on a larger scale, with people no longer living separately but rather forming groups where those with similar ideological preferences associate exclusively with one another. Studies that focus on groups, interactions, and communication between users relate to the phenomenon of individuals selecting like-minded people as communication partners and information sources [103]. This conceptualization of echo chambers that focuses more on the social structures than on media and information diet is captured by the term *homophily*. A term frequently used in the context of echo chambers is selective exposure, which is said to be one of the main antecedents and mechanisms driving echo chambers. This is based on the many choices of media environments on the Internet. Users of social media platforms can choose to be exposed to conversations with like-minded users and content that reflects their thinking, thus reinforcing their existing preferences or beliefs [11, 12]. This tendency is accompanied by the avoidance of cognitive dissonance through avoiding challenging information and is also known under the term *confirmation bias*. Selective exposure and other user-specific behaviors or attributes partially conceptualized by the corpus literature. These user attributes that are linked to echo chambers include—besides selective exposure—personality traits (e.g., [16]), fear of isolation and anger (e.g, [104]), openness (e.g., [84]), and reflectiveness (e.g., [93]).

Recent philosophical debates on social epistemology have built on the work of Jamieson and Hall [105] and approach the understanding of echo chambers differently, as they strictly separate them from epistemic bubbles. Nguyen [102] argues that an echo chamber is “a social epistemic structure in which other relevant voices have been actively discredited”, meaning that people who do not share the opinions of that group are discredited as sources of information in general. The overall structure of echo chambers in his account is built on creating a substantial trust imbalance between members and non-members so outsiders are no longer taken seriously [102]. However, such an echo chamber conceptualization is hardly reflected in the corpus, although there is research that examines particular *group behavior* and presents it as echo chamber-specific.

#### 4.2.2 Granularity of measurement

Granularity is an essential dimension of an echo chamber operationalization. How granular are echo chambers analyzed, and from what perspective? After analysis of studies, we differentiate between *single-user*, *group*, *platform*, *cross-platform*, and *holistic*. While single-user studies examine whether echo chambers originate from single individuals and how the individual influences echo chambers, group studies examine specific groups on specific platforms. Platform studies generally examine an entire platform to see whether it has an affinity for echo chambers or whether echo chambers occur there. In contrast, cross-platform studies compare platforms regarding their tendency for echo chambers. Holistic studies look at the entire media diet of users, i.e., not only certain social media but also newspapers, television, and other media simultaneously.

Most studies examined specific groups or communities on platforms, such as climate change deniers (e.g., [94]), vaccination opponents and advocates (e.g., [49]), and Trump supporters (e.g., [16]). However, few papers looked at the specific group behavior of these groups but mainly examined homophily over time and information flow to the group as opposed to outside the group. Some research conceptualizing specific user behavior also looked at specific users on platforms and how their behavior can create echo chambers. Some papers examined entire platforms and whether they correlate with echo chambers.

Only seven studies compared platforms in cross-platform studies with CSS methods. However, if specific platforms were researched, CSS was usually utilized. This is the case as surveys mostly observed the whole media diet but not one particular platform.

#### 4.2.3 Operationalization and methods

##### 4.2.3.1 Data-driven computational social science

In the following, the general procedure of echo chamber detection and evaluation via data-driven CSS methods or Social Data Analysis (SDA),Footnote 5 used in 85 studies, will be presented.

*General Procedure*. In general, most CSS studies used a form of social network analysis and followed this procedure:

-
1.
Gathering social media data through an API or scraping

-
2.
Building an undirected graph from this data

-
3.
Transforming the undirected graph into a bipartite graph

-
4.
Calculating network attributes from this bipartite graph

-
5.
Using community detection algorithms to detect clusters of homophilic relationships or use latent space models to find higher order dependencies between users

-
6.
Using a specific metric to determine a threshold

*t*which indicates whether there is an echo chamber/multiple echo chambers

*Content-considering and Interaction Data Sets*. The underlying data sets can be classified into API and scraping data, crowdsourced or donated data, and tracking data. The latter also includes sock puppet studies—bots that impersonate users to analyze platforms or algorithmic systems from the user’s perspective [106]. They also differ in their central research focus and granularity. API and scraping studies are predominantly platform-centered, while data donations and tracking data are mainly user-centered [107]. In the case of this corpus of echo chamber research, most of the data sets were API-gathered data sets (Facebook API, and the Twitter/X API back when it still offered free academic access). Some used scraping or tracking via plugins (e.g., Bing toolbar, YouGov). Most data sets were collected from digital traces of users collected on specific platforms, not donated by users.

We find another distinction between the underlying observational trace data sets for echo chamber research: purely structural data (interaction-based) and content-considering data sets. The former data sets consist of interactions between users such as ‘likes’, ‘posts’, ‘comments’,‘friendship’, ‘shares’, etc.; the latter use the content of ‘posts’ and ‘comments’ to gain insights into the users political leaning, polarization, radicalism or other attributes.

The size of the data sets varied by platform and by study as Fig. 7 in the “Appendix” shows. Data consisted of posts, comments, likes, and other digital traces. Different amounts of users and data were used for the analysis, with interaction-based methods having the advantage that larger data sets could often be examined, whereas content-considering data sets either had to be labeled, cleaned or had to apply resource-intensive Machine Learning (ML) algorithms to make sense of their data. The differences by platform could be related to the platforms’ API access restrictions. Studies that included data donated by users included additional information to the traces, but were smaller in size.Footnote 6 Data gathering periods differ among studies as well, and most of the studies look at a certain event, such as an election to investigate emerging echo chambers around that event. There were also works that examined longer time spans. An overview of interaction-based data sets and content considering data sets can be seen in Table 3.

Based on these two types of data sets, the general procedure was to build a graph for every time-dependent sample as social networks are dynamic networks [142] and use interaction (structural data sets) or semantic networks (content-considering data sets)Footnote 7. In the identified studies, nodes often represent users and edges denote interactions between users and interaction of users with content such as posts or hyperlinks to news pages (e.g., [108]). Thus, users can be connected in a graph through edges if they are friends (e.g., [136]) or have shared content. At the same time, the user is connected to posts or news pages that they have shared, thus also creating a semantic network. Each user can be characterized by a vector of node attributes,Footnote 8 such as demographic information, interests, or activity patterns. The edges can be weighted by the strength of the social tie between users, such as the frequency, intensity of interactions, or a friendship tie.

*User-Attribute Estimation*. Some of the content-considering data sets first transformed the network into a weighted, undirected network by computing the pairwise similarities between nodes of the same type (e.g., similarity between users based on their shared interactions with content or friendship ties). They estimated the user attributes like political leaning by calculating ideology scores or political preferenceFootnote 9 based on the users attributes with an ideology score ranging from -1 (conservative) to 1 (liberal) (e.g., [73]), by shared news pages which were sorted by their political affiliation (e.g., [108, 129]), averaging over user’s produced content scores with the number of posts ranging as well from \(-1\) to 1 (e.g., [17]) or by their shared content by using sentiment analysis (e.g., [127]).

These user-attribute estimation techniques are, as their name suggests, used to estimate user attributes, such as political leaning, based on the content they consume, share, or interact with. They enable the analysis of interactions between specific groups of attributes. User leaning was also estimated by activity in specific groups (e.g., [59, 127, 143]), by semantics in the posts (e.g., [94, 99, 113]), calculation of political slant of visited websites by the user [124], shared news URLs with news outlets leaning score (e.g., [8, 96, 129]).

*Two-Mode and Bipartite Graphs*. Some content-considering studies incorporate a second set of nodes to represent content items (e.g., posts, articles), creating bipartite graphs where users are connected to the content they interact with. From these, unipartite projections or multiple bipartite graphs are derived to study user-to-user connections or user-content dynamics [94, 96]. Polarization and homophily measures are frequently calculated on these networks to assess ideological clustering.

*Community Detection*. The next methodological step for most of the social data methods was to use a community detection algorithm. The Louvain algorithm,Footnote 10 Leiden algorithmFootnote 11 (e.g., [99]), random walk modelling (e.g., [108, 127]), greedy algorithms (e.g., [94]), latent space modelsFootnote 12(e.g., [8, 100]), flow stability (e.g., [146]) or hierarchical clustering algorithms (e.g., [90]) are used in most cases of the included studies to detect communities in the bipartite graph.Footnote 13

*CSS Metrics*. In the context of the bipartite graph *B*, these algorithms are used to detect communities of users who are more likely to interact with content items within their community than with content items outside their community. These communities can be interpreted as echo chambers, where users are exposed to information that reinforces their existing beliefs and opinions, if these communities are communities of like-minded people with similar attributes. To asses the similarity between different users in communities, different metrics are used.

To detect and analyze echo chambers, a variety of metrics are employed, categorized into interaction-based metrics, content-considering metrics, homophily and polarization measures, and modularity measures. These metrics differ by data type, granularity, and approach (connectionist vs. positional) [142].

*Interaction-based methods*. These metrics rely heavily on centrality measures to identify influential users and assess the structural dynamics of networks:

*Degree Centrality:* Nodes with a high in-degree, such as accounts receiving frequent retweets, signify prominence within the network [6, 56].

*Eigenvector Centrality:* Highlights nodes connected to influential accounts, portraying their authority within the network [6, 111].

*Closeness Centrality:* Identifies nodes with the shortest paths to all others, indicating their ability to disseminate information effectively [6].

*Betweenness Centrality:* Measures nodes acting as bridges, facilitating the flow of information and potentially mitigating misinformation [6].

Centrality measures identify influential nodes, such as disseminators (high closeness centrality) or bridges (high betweenness centrality), offering insights into individual roles within echo chambers [6, 111]. While these metrics provide user-level insights, they do not directly capture broader interaction patterns or group dynamics.

*Content-Considering Metrics*. They estimate user attributes, such as political leanings, or analyze cross-cutting content exposure to understand how individuals engage with ideologically similar or diverse content. Metrics like polarity scores measure the distance between users based on their attributes when group membership is unavailable (e.g., [73, 100]). For example: Bakshy et al. [129], Choi et al. [100], and Brugnoli et al. [97] used polarity scores to assess user ideological alignment. Del Vicario et al. [48] and Flaxman et al. [134] demonstrated that content-considering methods effectively detect echo chambers formed through selective content exposure.

*Homophily and Polarization Metrics*. These are used interchangeably in many studies to evaluate the similarity between users within echo chambers.

*Node-Level Homophily:* Focuses on individual tendencies to connect with similar users (e.g., [73, 99]).

*Group-Level Homophily:* Aggregates the homophily of individual group members to assess group polarization [25].

*Network-Level Homophily:* Measures the overall homophily of a network to understand the systemic tendencies for like-minded clustering [99, 117].

*EI-Index:* Calculates relative homophily, capturing the balance between in-group and out-group ties [86, 114].

While the measures can also indirectly represent structural trends in a network, homophily studies the propensity for people to connect with those who share their qualities or traits and does not directly capture the structural organization of these groups. This is why it is often combined with community detection. Homophily measures highlight user preferences and shared characteristics, directly linking echo chambers to ideological or demographic alignment [25, 73]. Homophily measures, particularly ideological homophily (e.g., [73, 117]) and demographic homophily (e.g., [147]), are crucial for analyzing echo chambers with CSS research. The strong association of homophily and polarization measures used in the corpus, especially in connection to conceptualizations of echo chambers as homophily demonstrates the importance and advantages of using homophily measures in CSS echo chamber research.

*Modularity Measures*. Modularity measures the organization and segregation of communities within a network, providing insights into the structural presence of echo chambers. Modularity captures larger structural trends, assessing how communities form and segregate [111]. For example, Kratzke [111] used modularity to analyze community dynamics, complementing user-level centrality measures.

##### 4.2.3.2 Surveys

Out of all the analyzed studies, 20 were surveys. Most of these surveys were longitudinal, meaning they collected data over a period of time, whereas a few were cross-sectional, meaning data was collected at one point in time. About half of the surveys were conducted in the USA (a total of 8), and only 5 of these studies addressed the echo chamber hypothesis directly. The rest of the studies examined elective exposure of social media users, news consumption and sharing behavior, extremism, and voting patterns. As Fig. 6a demonstrates, most survey studies conceptualized echo chambers with content exposure. These studies mostly researched how much cross-cutting content users self-report via their media usage. User behavior survey studies researched specific user behavior that is associated with echo chambers.

In both cross-sectional and longitudinal studies, some surveys were conducted around election periods. This means that panels were usually surveyed before and after the elections or a three-wave panel was used. In cross-sectional studies, participants were surveyed either shortly before or after an election. The longitudinal studies are all panels that were either built around elections or drawn from existing panels such as household panels (e.g., [69]), panels about migration (e.g., [148]) or social media and internet panels (e.g., [76]).

Out of all survey studies, 17 looked at general social media usage or the whole media diet, while only two looked at specific platforms. Masip et al. [55] analyzed social media usage on Facebook, Instagram, and Twitter/X, focusing on news-sharing behavior in Spain. Similarly, Beam et al. [74] examined news polarization on Facebook before and after the 2016 U.S. elections. Interestingly, both studies found no echo chambers or polarization through social media, contrary to homophily studies.

18 surveys that focused on content exposure have examined the entire media landscape and compared the content exposure of social media with other media outlets. Dubois and Blank [12], for instance, studied the use of other media and found that social media is only one part of the users’ media diet and argued that echo chamber research has to include a wide variety of media usage.

Some survey studies (\(n = 14\)) examine the role of user attitudes in shaping online behavior and mitigating the effects of echo chambers. For example, the study by Dubois et al. [65] examines the effects of fact-checking, political interest, and opinion leadership on individuals’ exposure to different viewpoints and their susceptibility to echo chamber effects. Similarly, studies by Koivula et al. [67] and Zerback and Kobilke [148] examine the role of political activity, extreme attitudes, and interpersonal communication in reinforcing or counteracting echo chambers in online communities. Studies by Chan et al. [83], Boulianne et al. [16], and Neely [71] explore how factors like internal political efficacy, personality, and social network structures influence individuals’ interactions with political content and their susceptibility to echo chamber effects. The focus is placed on user behavior and thus also conceptualized and operationalized by investigating how specific user attributes, such as political interest, change content exposure. There is little focus here on the social environment of the users but instead on what content they are exposed to with certain behaviors or specific attributes, such as fear of isolation or personality traits.

Survey research involves a broad set of measures like political engagement, media consumption, and specific topics like climate change, misinformation, COVID-19, vaccines, news dissemination, and other forms of media use such as TV and newspapers. The studies use between 5 and 41 items to gather data from a participant pool of 198 to 11,052 individuals.

Control variables are mainly demographics and political ideology. To evaluate the broader societal implications of echo chamber behavior, researchers use dependent variables that we group into four categories: (1) political engagement and behavior, (2) media consumption and exposure, (3) homophily and polarization measures, (4) trust in specific information and misinformation sharing. Political engagement and behavior measures include political engagement (e.g., following political news, expressing political views), social media behavior and impact (e.g., reliance on Facebook, unfriending/unfollowing due to political posts) polarization, satisfaction with democracy, political ideology, party affiliation, and affective polarization, news consumption habits (e.g., interest in hard news, news trust).

Media consumption and exposure metrics include exposure to various news sources (e.g., news websites, TV news) and engagement with news, social media usage and attitudes, perception of the public sphere, universal news access, and privacy concerns. Homophily and other echo chamber measures include like-minded discussion, perceived viewpoint diversity exposure, and cognitive attitude extremityFootnote 14.

Trust in information and misinformation measures include trust in news sources, traditional media use for COVID-19, and vaccine hesitancy.

##### 4.2.3.3 Experiments

Ten experiments are part of the corpus. Such experiments include observing test subjects while they follow a bot that shares certain types of political content, experiments with their own newsfeeds or self-constructed platforms, or even sock puppet studies, in which bots generate online content and collect what content they encounter. Most experiments focus on user behavior (e.g., [93]), recommendation systems’ influence on echo chamber creation (mostly through sock puppet studies like e.g., Minh Pham et al. [5], Whittaker et al. [60]), on extremism and misinformation (e.g., [101]). Like surveys, these experiments used operationalizations that isolated the effects of echo chambers by controlling for variables like demographics and political ideology.

Figure 6b demonstrates that most experimental studies find echo chambers. These findings point mostly to individual behavior like selective exposure, extremism, and anger. Data sets for experiments vary from 102 to 1,652 users. They can be categorized into (1) sock puppet data, (2) user-centric data, and (3) trace data experiments. Sock puppet experiments (Minh Pham et al. [5], Whittaker et al. [60], Mosleh et al. [93]) used bots that mimic user behavior on Twitter/X, YouTube, and Weibo. In contrast to trace data, bots enable real-world experiments on platforms which comes with the advantage of controlled experiments but is limited to a certain number of bots and has to be ethically evaluated. Sock puppet studies used measures like the directed clustering coefficient, connection density, strong and weak co-partisanship and counter-partisanship,Footnote 15 social attentiveness, attitude consistency, algorithmic polarization, and extremist media index. User-centric data sets were used, e.g., in an eye-tracking study by Suelflow et al. [150] which used measures like political affiliation, affective polarization, perceived polarization, contact with immigrants, and political interest. Trace data experiments like the experiment by Bail et al. [81] measure the change of affiliation after the experiment through a survey.

##### 4.2.3.4 Mixed methods

Six of the included studies used a mixed methods approach. The main idea of mixed methods approaches is to have different perspectives and granularities in echo chamber research and platform research. Most mixed methods approaches studied a particular platform; some did a cross-platform analysis (e.g., [24]). Most mixed method studies focused either on user behavior, recommendation systems’ influence on echo chamber creation (mainly through sock puppet studies), or extremism and misinformation.

Most link survey data with trace data, and some link experiments or surveys with trace data. As Fig. 6b suggests, mixed methods approaches have mixed results. Here again, studies using homophily as a conceptualization tend to have affirming results on the echo chamber hypothesis, and studies using context exposure tend to have negative findings. All but two mixed method studies used trace data and analyzed user groups ranging from 2,000 to 42,600 users (e.g., [84]). The other two studies mixed impression data with surveys (e.g., [87]).

The survey and trace data linking approaches used categories of accounts: media elite, political elite, and non-elite (Eady et al. [72]), distinct news sites, slant dispersion, reverse Gini index, audience variety, mean slan, cross-cutting proportion (Kitchens et al. [24]), Big Five Personality Traits (Matz [84]), and a combination of cognitive reflection and co-follower network (Mosleh et al. [93]). The two studies that combined impression data and surveys used attitude polarization, anger, and emotional valence (Hilbert et al. [87]).

### 4.3 Varying outcomes in echo chamber research (RQ3)

This section aims to answer RQ3, namely: “How can the varying outcomes in echo chamber research be explained?”. Synthesizing the results from our first two research questions yields five dimensions where echo chamber studies diverge, providing a framework to examine the causes of conflicting outcomes in this field systematically. Specifically, echo chamber studies vary across dimensions of (1) focus, (2) construct conceptualization, (3) operationalization, (4) granularity, and finally in (5) outcomes.

In the following, we will give an extended overview of how studies vary across these dimensions and outcomes, analyze the relationship between outcomes and measurement, and discuss how geographical and contextual factors may influence research approaches and variations in findings.

#### 4.3.1 Varying research, varying outcomes

Firstly, the echo chamber construct is controversial, and researchers claim that it was ill-defined from the beginning and that researchers should either abandon or conceptualize it properly [91]. This is largely because the concept does not represent any observable outcome since “echo chambers” describe a state of absence, namely the absence of an idealized model of a deliberative public sphere such as the Habermasian democratic model [24, 114].

In addition, studies on echo chambers in social networks have been carried out by researchers from various fields—such as computer science, sociology, political science, law, media, and communication science—using differing methods and thus different *operationalizations* of the echo chamber construct. Some studies have conducted a network analysis based on data from social networks [17], while others have interviewed Twitter/X users after they were exposed to the contents of a social media bot [2].

The difficulties in operationalizing extend to the *granularity* of echo chamber detection as they can occur on individual users, groups, or entire platforms [111] and related to the research decision to analyze specific groups or platforms, data utilized in the empirical research is subject to sampling bias even if there are attempts to counteract these differences [12, 24].

Previous studies may have analyzed mainly active users and used scarce or incomplete data sets to support their conclusions. This fact may have led to misleading results, as the periphery of networks appears to be essential for the average behavior of social networks [124]. Studies analyzed online platforms either independently (one specific platform) or in aggregate (all of social media), which may make it difficult to determine the link between social aspects, technological characteristics, and information-limiting contexts [24].

If only one medium (e.g., one platform or one online newspaper) is analyzed, this may not provide relevant information on how political information moves across offline and online media [12]. Moreover, demographics differ across platforms [151, 152].

Echo chamber research in our corpus also differs in *focus*. Some research studies are primarily concerned with the echo chamber hypothesis, while others focus on the antecedents, properties, and effects of echo chambers.

Finally, studies differ in *outcomes*. Although the majority of studies has found evidence for echo chambers on platforms such as Facebook (e.g., [66]), there is still a substantial amount of studies that had mixed findings, and one-fourth of studies that focused on the echo chamber hypothesis have not identified evidence for echo chambers (e.g., [74, 129]).

Echo chambers are also repeatedly associated with the spread of misinformation, which poses the risk of poor political decisions or the formation of opinions based on falsehoods [48, 100, 153]. However, scientific findings have also been contrasting with the echo chamber hypothesis. Some studies indicate that social media networks are similar to real-life interpersonal networks (e.g., [12, 90]), thus downplaying the asserted impact of social media or that social networks do not change the political discourse excessively (e.g., [75, 114, 154]).

Some studies claim that echo chambers have no significant impact (e.g., [12]), do not contribute to polarization (e.g., [77]), or do not demonstrate increased exposure to dissimilar opinions through social media (e.g., [81]). According to some studies, societal polarization is not a phenomenon attributable exclusively to social media, but to other forms of media like radio and TV as well (e.g, Jamieson and Hall [105], Muise et al. [135]). Other studies find that cultural and demographic factors are more important than structural (e.g., [61, 92]).

#### 4.3.2 Relationship between outcomes and measurement

Our analysis culminates in the analysis of factors contributing to the varying outcomes in echo chamber research, with measurement playing a central role. Outcomes are closely linked to how echo chambers are conceptualized and operationalized. We start by examining the relationships between conceptualization, method, and granularity, followed by an analysis of how these elements influence outcomes. Conceptualization and operationalization are interconnected. Figure 6a shows that conceptualizations often align with specific methods. For instance, studies using CSS methods typically conceptualize echo chambers as attribute-based homophilic structures, whereas surveys and experimental studies focus on content exposure and user behavior.

The granularity of measurement varies depending on the method. Survey studies often assess exposure across broader media environments, encompassing both social media and traditional media. In contrast, CSS studies focus more narrowly on structural aspects of specific communities or platforms. These methodological differences shape the outcomes of the studies.

Differences in definitions of echo chambers-whether based on homophily, content exposure, or selective exposure-translate into distinct methodological choices, which in turn shape findings. Figure 6b illustrates a clear relationship between methods and outcomes. Studies employing CSS methods are more likely to identify echo chambers, while surveys and experiments tend to produce mixed or less conclusive results.

Studies that challenge the echo chamber hypothesis often conceptualize echo chambers in terms of content exposure and emphasize the availability of cross-cutting content. These studies argue that users are exposed to diverse media sources beyond social networks, challenging the notion of isolated filter bubbles. However, they also find that echo chambers can still emerge under specific conditions, such as heightened political interest, selective exposure tendencies, or high user activity. Surveys and experiments in this area focus on individual-level behaviors and demographics, often reporting modest or mixed effects. These findings suggest that individual traits mediate the formation of echo chambers.

CSS studies, by contrast, frequently provide evidence supporting the echo chamber hypothesis. These studies focus on network analysis and trace data to examine homophily, showing how like-minded individuals cluster within networks and how these clusters contribute to polarization. The methodological emphasis on interaction patterns within platforms highlights structural aspects of echo chambers, such as clustering and information reinforcement. However, these approaches may overlook broader user experiences, leaving gaps in understanding how individuals engage with the wider media environment.

The relationship between methodology and outcomes is consistent. CSS studies often support the existence of echo chambers, while surveys and experiments, with their emphasis on content exposure and user perceptions, are more likely to report mixed results. This reflects how methodological choices shape the specific aspects of echo chambers that are studied. Furthermore, conceptualization and methodology are closely aligned. Studies that focus on network-based homophily tend to use CSS methods, while those examining user-level exposure typically rely on surveys or experiments. These interconnections demonstrate how conceptual frameworks and methodological approaches influence the outcomes of echo chamber research.

#### 4.3.3 Measurement factors and challenges

The diverse measurements used in echo chamber research reveal different approaches’ strengths and limitations. Each conceptualization and operationalization offers advantages for measurement while also presenting specific challenges. This section explores these factors, focusing on their implications for measuring and understanding echo chambers.

##### 4.3.3.1 Computational social science

CSS methods allow researchers to unobtrusively observe behavioral choices in natural social media environments. This approach minimizes social desirability bias and measurement error [75] and is relatively accessible, particularly for European researchers under the upcoming Digital Services Act (DSA). However, API restrictions have made access more challenging in recent years.

CSS methods are particularly effective at analyzing large-scale networks and identifying patterns of homophily, polarization, and content exposure. For example, researchers can use network metrics like degree centrality and betweenness centrality to analyze the structural components of social networks. Techniques like latent space models enable the estimation of ideological positions from behavioral data, although these approaches are not without limitations. Latent models can be biased by parameter choices and assumptions and may fall into circular reasoning, such as inferring political positions from network structures and then using those positions to explain the same structures [155]. While content-based methods offer higher accuracy [48], they require substantial labeled training data, which is often unavailable or costly to generate. These methods are also less effective for novel situations, such as the Russia-Ukraine war, where labeled data is scarce [111].

Bots pose another significant challenge for CSS studies. While Gallwitz and Kreil [156] argue that the role of social bots is overstated, other studies suggest that bots disproportionately benefit certain political groups, such as right-wing parties [157]. For instance, when Twitter/X deleted millions of bots in 2017, radical right European MPs experienced the greatest loss of followers [158]. Machine learning-based bot detection, as proposed by Rusche [110], and implemented by Choi et al. [100] and Gaumont et al. [120], offers a way to mitigate this issue.

Causal inference remains one of the most significant challenges in CSS. Observational data can identify associations but cannot establish causality. For example, polarization on social media may reflect broader societal polarization rather than causing it [159]. Longitudinal data can help address this issue by disentangling network influence from selection effects, and some studies have shown that longitudinal approaches can approximate results from randomized experiments [160].

##### 4.3.3.2 Surveys

Survey methods provide insights into users’ broader media diets and individual-level behaviors, capturing information beyond the scope of social media platforms. These methods are particularly useful for studying exposure to cross-cutting content. Longitudinal surveys, in particular, can track changes over time and help distinguish network effects from selection biases.

However, surveys face limitations in measuring homophily. Self-reported data often captures perceived rather than actual homophily, which can lead to underestimation of polarization [73]. Survey studies also suffer from smaller sample sizes, measurement errors, and social desirability biases, where respondents may overreport “positive” behaviors, such as exposure to diverse viewpoints, and underreport politically charged or “negative” activities [15]. Additionally, survey respondents may struggle to recall specific instances of content exposure, further complicating data collection [12].

##### 4.3.3.3 Experiments

Experiments provide a robust framework for identifying causality by allowing researchers to manipulate network structures or content exposure. For example, randomized experiments can isolate the effects of polarization and information flow on individual behavior [161]. Crowdsourcing platforms and sock puppet studies offer tools for quasi-experimental research. These methods can be cost-effective and scalable, but ethical concerns and the complexity of real-world social networks limit their use in echo chamber studies. However, more recent studies as conducted by Nyhan et al. [77] are positive examples of how experiments can significantly contribute to echo chamber research. They conducted a large-scale, randomized field experiment with estimated treatment effects to directly evaluate whether reducing exposure to like-minded content can causally impact polarization.

##### 4.3.3.4 Common measurement challenges

Several challenges cut across all methodological approaches. Selection bias is a persistent issue, particularly in CSS studies. Highly active and ideologically driven users are often overrepresented in trace data, which can skew findings [110]. For instance, Aruguete et al. [108] show that ideological congruence and issue salience correlate with political engagement, leading users on both ends of the political spectrum to disproportionately share ideologically aligned content. This overrepresentation of ideologues may amplify observed polarization and limit the generalizability of findings.

Another common issue is the “no interference assumption” in causal inference frameworks, which assumes that one individual’s treatment does not affect another’s outcome [159]. This assumption often fails in highly interconnected social networks, where individuals influence one another across various ties. Although recent advancements have sought to extend causal frameworks to account for interference, they remain underutilized. Cluster-based approaches offer a partial solution but are difficult to implement in highly connected networks like social media.

Lastly, there are inconsistencies in how echo chambers are operationalized and measured across studies. Dependent variables, such as exposure to opposing viewpoints or clustering within networks, vary widely. These inconsistencies complicate comparisons across methods and highlight the importance of aligning conceptual frameworks with empirical approaches.

#### 4.3.4 Geographical and contextual factors

In the following, we briefly analyze other factors such as regional factors, political system factors, demographics, and platform characteristics that could influence research outcomes. We want to compare studies’ demographics and political environments, as Kitchens et al. [24] claimed that most research that confirms the echo chamber hypothesis has been conducted in the United States.

Table 4 presents the distribution of countries in the corpus. This summarization includes studies with participants from these countries or CSS studies that used trace data from these populations. The table demonstrates that the majority of studies, namely 54, were conducted in the US. The other most studied countries are all European countries. Only four studies were conducted in China, two studies in Japan, and another two in Brazil. There is a lack of research, particularly about countries outside the Global North. This may be due to non-English publications, limited funding, or limited data access. This will probably only change with publicly accessible data and increased research funding.

Concurrent with previous research, we find that most studies affirming the echo chamber hypothesis are conducted in the United States or use data concerning the United States population and are not representative of other regions. We find that more studies from the US and UK affirm the echo chamber hypothesis and less from countries such as Germany, France, and the Netherlands.

This presents a tendency for echo chambers to be mostly demonstrated in countries or discourse spaces that are already highly fragmented. That is, in countries that have two-party systems and are considered divided or in polarized groups, such as conspiracy and science or vaccination and anti-vaccination. It is necessary to determine whether there is a reverse causality fallacy present in this context and whether fragmentation in society ultimately leads to the formation of echo chambers in social networks.

Figure 4b illustrates the social media platforms analyzed in the reviewed studies, where specific platforms were identified. Importantly, this distribution does not reflect the actual usage patterns of social media platforms globally. Among the top 10 most popular platforms, only Facebook and YouTube were addressed in the included studies [46]. Research on platforms such as Instagram, WhatsApp, Telegram, TikTok, and WeChat is notably absent, largely due to challenges in data accessibility. These platforms lack open APIs, introducing a significant data accessibility bias.

This gap is particularly concerning given the varying user demographics and interaction patterns across platforms. For instance, TikTok, which relies on algorithm-driven content delivery, features interactions that are fundamentally different from platforms like Twitter/X, where users can follow one another back. Such differences not only shape how information spreads but also influence user engagement and community dynamics. Neglecting these variations risks oversimplifying the complexity of online ecosystems.

Moreover, certain platforms like Telegram have emerged as critical spaces for misinformation, including content related to COVID-19 [162] and disinformation about the Russian invasion of Ukraine [163]. Similarly, TikTok’s growing role in shaping public discourse and its distinct interaction model remain significantly underexplored.

Additionally, while instant messaging services like WhatsApp and Telegram are often excluded from the definition of social networks, their importance in information sharing is undeniable and growing. A significant portion of content sharing occurs through private channels such as instant messengers or email rather than public social networks [164].

## 5 Discussion and limitations

Our systematic review demonstrates that differing conceptualizations and operationalizations of echo chambers significantly shape research outcomes. In the following, we outline research recommendations for echo chamber studies based on our findings and the limitations of our review.

Future research should focus on (1) proposing unified conceptual and operational frameworks to standardize the study of echo chambers, (2) expanding research on group behavior and finding ways to integrate social and cultural context into measurements of echo chambers, (3) addressing gaps in causal evidence through longitudinal studies, experiments, or quasi- experimental designs, (4) investigating cross-platform dynamics, including less-studied platforms like Instagram, TikTok, instant messengers, and decentralized networks, and (5) researching the relationship between content moderation and echo chambers, not solely focusing on the recommendation systems in the moderation process.

The field urgently needs standardized frameworks for both conceptualizations and operationalizations. The current diversity in how echo chambers are defined—whether as homophily, selective exposure, or content exposure—and the wide range of methodologies used make it challenging to synthesize evidence. This review contributes to a more nuanced understanding of the echo chamber construct by categorizing and systematically measuring these varying approaches.

However, to achieve meaningful progress in understanding phenomena such as polarization, it is crucial to develop a unified perspective that integrates these differing views while distinguishing between structural and behavioral (individual or group) elements. To bridge this gap, researchers should adopt measurement modeling techniques to systematically link theoretical constructs with empirical data, ensuring coherence between what is being studied and how it is being measured.

While the corpus predominantly reflects these four established conceptualizations, some approaches remain underexplored. For instance, trust imbalances as the foundational structure of echo chambers [102] have yet to be extensively operationalized in empirical studies. Similarly, Mahrt [91] argues for broader integration of social and cultural contexts into echo chamber research, emphasizing that fragmentation is often context-specific rather than universal. These perspectives call for re-conceptualizing echo chambers as embedded within wider societal dynamics rather than solely as digital phenomena. We recommend expanding operationalizations on group behavior and integrating context-specific measurement into research.

Researchers should establish transparency in reporting such measurement decisions and potential limitations. This will allow others to replicate findings and assess the robustness of conclusions, which should be done regularly. Validations of operationalization should accompany this. By addressing these issues and promoting interdisciplinary collaboration, the field can progress toward a standardized framework that captures the complex dynamics of echo chambers while accommodating their multifaceted nature.

The current limitations in echo chamber research design highlight the need for more comprehensive and interdisciplinary approaches. One issue is the focus on single platforms, which restricts the generalizability of findings and overlooks cross-platform dynamics. Future research should prioritize cross-platform studies that examine how users navigate diverse media ecosystems, integrating insights from platforms like Facebook, Twitter/X, Reddit, TikTok, and instant messengers. These studies could explore how platform-specific affordances, such as recommendation systems, influence echo chamber formation and how cross-cutting content from one platform may counteract clustering effects on another.

Another critical gap lies in capturing broader contextual factors. CSS methods are effective for identifying patterns and relationships within networks but often fail to account for the social, cultural, and political contexts that shape these networks. Combining CSS with surveys can address this gap, providing both behavioral data and self-reported insights into user motivations and experiences. For instance, surveys could explore how individuals perceive their exposure to diverse viewpoints, while CSS could validate these perceptions through trace data. Mixed-methods approaches, which combine trace data, surveys, and experiments, offer a promising pathway to uncovering the nuanced mechanisms driving echo chambers.

Randomized experiments, while challenging due to ethical and logistical constraints, are important methods for establishing causality. Innovative approaches, such as ethically designed simulations or controlled interventions (e.g., “sock puppet” accounts), should be explored to assess the impact of recommendation systems on polarization, misinformation, and selective exposure. Such experiments would help understand the interplay between homophily and selective exposure, which may be more critical than the overemphasized issue of content exposure or filter bubbles.

Causal inference remains a significant challenge in this field. While many studies identify associations, few establish causal relationships, such as whether echo chambers amplify polarization or whether pre-existing polarization fosters echo chambers. Future research should use longitudinal designs, instrumental variable approaches, and quasi-experimental methods to address this gap.

Finally, addressing granularity requires designing studies that account for different levels of analysis, from individual users to platform-wide phenomena. Researchers should integrate multi-level data to examine how individual behaviors aggregate into group dynamics and how these, in turn, influence platform-wide trends. By explicitly linking findings across these levels, studies can provide a more holistic understanding of echo chambers and their societal impacts.

There is a lack of research about countries outside the US and outside the Global North. This may be due to the limits of literature searches in systematic reviews or the difficult data situation. This will probably only change with publicly accessible data. The DSA [1] could lead to more studies focusing on EU countries, but similar regulatory efforts are needed to ensure broader applicability beyond the Global North.

In the following, we will briefly lay out the limitations of our work, although most limitations of systematic reviews have already been addressed in this study. For instance, ICR was discussed in Sect. 3. Although the ICR falls within a reasonable range, there is room for improvement. The initial agreement between the first and third coders was moderate. While considered substantial by some standards, this highlights areas for enhancing the clarity and consistency of the coding process. This moderate agreement could stem from differences in the interpretation of the codebook or the inherent complexity of the coding task. To address this, disagreements were thoroughly discussed, and the codebook was refined during the process. These efforts improved consistency, resulting in a Cohen’s \(\kappa\) value of 0.66. Nonetheless, future studies could benefit from additional coder training or iterative testing of the codebook before formal coding begins.

It is worth noting that most systematic reviews do not measure or report ICR, nor do they provide transparency in how their coding processes are executed [165]. This study has aimed to counteract this common issue by employing measures such as publishing the codebook, detailing the derivation of code variables, and calculating ICR. These steps enhance the reproducibility and reliability of the findings.

The possible biases that can occur in systematic reviews are the already mentioned publication bias, time lag bias, multiple (duplicate) publication bias, location bias, citation bias, language bias, and the outcome reporting bias [37] in Sects. 3.4.1 and 3.4.2, these biases and their potential to occur in this work were discussed.

## 6 Policy recommendations

Based on our findings, the following section will explore implications and recommendations for policies.

The findings highlight the necessity of platform-level interventions that empower users with greater customization options and control over recommendations. Adjustable recommender systems like those tested on Reddit allow users to customize content diversity, reducing algorithmic reinforcement of homogeneous content and introducing contrasting perspectives. Regulatory policies should mandate their implementation to ensure users can meaningfully adjust their content exposure.

One major criticism of social media studies is their limited attention to algorithmic filtering changes. Although a few studies have conducted continuous audits to examine how algorithms evolve (e.g., [147, 166]), most research fails to address these dynamic shifts adequately. The inaccessibility of platform algorithms and their inherent complexity—often requiring live observation to understand their real-world effects—presents significant challenges.

This reinforces the need for continuous algorithmic auditing, as the EU DSA emphasizes, which grants vetted researchers access to platform data and enables recommendation system audits [88]. Institutionalizing live observation and ongoing audits in various regional and political contexts are necessary to create transparency and accountability and provide deeper insights into how recommender systems reinforce or mitigate echo chambers in these contexts.

Policies should enable standardized researcher data access across platforms to create the possibility for cross-platform research. Integrating user data from multiple platforms, combined with survey, trace, and experimental data, would offer a more comprehensive understanding of how algorithmic filtering influences exposure to content across the digital ecosystem. Policies and standardization of social media data and data access should enable this. Whether the DSA will shape such a standardized data ecosystem for vetted researchers remains to be seen.

Our findings demonstrated that we not only need more European research on echo chambers but also more data from outside the Global North. Thus, policies such as the DSA Art. 40 and systematic audits should be enabled outside the Global North to understand better how regional and political contexts shape the echo chamber phenomenon and its dynamics with polarization, misinformation, and extremism.

## 7 Conclusion

We conducted a systematic review of 129 studies investigating the antecedents, characteristics, and effects of echo chambers on social media. Our analysis focused on how echo chambers are conceptualized and operationalized, using a measurement modeling perspective. The review demonstrated that varying conceptualizations and operationalizations often lead to divergent findings.

Specifically, studies that conceptualized echo chambers through the lens of homophily and employed data-driven CSS methods tended to support the echo chamber hypothesis and its link to polarization effects on social media. In contrast, studies utilizing content exposure analyses and surveys, which examined the broader spectrum of media exposure, often refuted the echo chamber hypothesis.

Notably, most of these studies were conducted in the context of the United States, highlighting a critical gap in understanding echo chambers within non-two-party political systems. To advance this field, future research should prioritize cross-platform analyses, incorporate continuous audits of algorithmic filtering, and examine the causal dynamics between polarization, fragmentation, and the formation of online echo chambers.

Additionally, research should strive for greater transparency in conceptualizing and operationalizing echo chambers. A more nuanced and granular approach to defining echo chambers is essential for advancing our understanding of this complex phenomenon.

See Fig. 7.

## Notes

Data-driven CSS methods and SDA will be used interchangeably in the following.

Graph is represented by \(G= (V,E)\) with a node set \(V = \{v_1,\dots ,v_n \}\) and edge set \(E \subseteq V \times V\).

For a user

*u*in*V*this vector is denoted by \(u_i = (x_{1,\dots , j})^T\)Calculated through: \(f: (x_{1,\dots , j})^T \rightarrow \{-1, \dots , 1\}\)

The Louvain algorithm is a greedy agglomerative cluster algorithm that optimizes a modularity score by iteratively merging nodes into communities that maximize the increase in modularity. The modularity score measures the degree to which nodes within a community are more densely connected than nodes outside the community [144].

The Leiden algorithm is an extension of the Louvain algorithm that improves its community quality and scalability by employing a refinement step that further partitions communities into sub-communities [144].

Assumes that nodes in the network belong to one of K latent communities and that the probability of an edge between two nodes depends on their community membership [145]. In latent space models, the goal is to learn a low-dimensional embedding of the nodes in the network, where nodes that are close in the latent space are likely to have similar connectivity patterns.

Let \(A = \{A_1,\dots ,A_q\}\) be a set of node groups defined over

*V*, that is, each \(A_i \subseteq V\) for any \(i = 1,\dots , q\). Then \(A_i\) is a community of*G*based on some node and edge attributes.

## References

European Commission: Regulation (EU) 2022/2065 of the European Parliament and of the Council of 19 October 2022 on a Single Market For Digital Services and amending Directive 2000/31/EC (Digital Services Act) (Text with EEA relevance). Legislative Body: EP, CONSIL (2022). http://data.europa.eu/eli/reg/2022/2065/oj/eng Accessed 19 June 2024.

Bail, C. A., Argyle, L. P., Brown, T. W., Bumpus, J. P., Chen, H., Hunzaker, M. B. F., Lee, J., Mann, M., Merhout, F., & Volfovsky, A. (2018). Exposure to opposing views on social media can increase political polarization.

*Proceedings of the National Academy of Sciences of the United States of America,**115*(37), 9216–9221.Quattrociocchi, W. (2017). Social and political challenges: Western democracy in crisis? In

*Global Risks Report 2017*.Lorenz-Spreen, P., Oswald, L., Lewandowsky, S., & Hertwig, R. (2023). A systematic review of worldwide causal and correlational evidence on digital media and democracy.

*Nature Human Behaviour,**7*(1), 74–101. https://doi.org/10.1038/s41562-022-01460-1Minh Pham, T., Kondor, I., Hanel, R., & Thurner, S. (2020). The effect of social balance on social fragmentation.

*Journal of the Royal Society Interface,**17*(172), 7–52.Torregrosa, J., Panizo-Lledot, A., Bello-Orgaz, G., & Camacho, D. (2020). Analyzing the relationship between relevance and extremist discourse in an alt-right network on twitter.

*Social Network Analysis and Mining**10*(1).Sunstein, C. (2001). Republic.com. Princeton University Press

Cinelli, M., Brugnoli, E., Schmidt, A. L., Zollo, F., Quattrociocchi, W., & Scala, A. (2020). Selective exposure shapes the facebook news diet. PLOS ONE

*15*(3).Pariser, E. (2011).

*The filter bubble: What the internet is hiding from you*. The Penguin Group.Sunstein, C. (2017).

*Republic: Divided democracy in the age of social media*. Princeton University Press.Van Aelst, P., Strömbäck, J., Aalberg, T., Esser, F., De Vreese, C., Matthes, J., Hopmann, D., Salgado, S., Hubé, N., & Stępińska, A. (2017). Political communication in a high-choice media environment: a challenge for democracy?

*Annals of the International Communication Association**41*(1), 3–27.Dubois, E., & Blank, G. (2018). The echo chamber is overstated: the moderating effect of political interest and diverse media.

*Information Communication & Society**21*(5, SI), 729–745 https://doi.org/10.1080/1369118X.2018.1428656Habermas, J. (2010). Hat die demokratie noch eine epistemische dimension? Ach Europa

*Kleine Politische Schriften 11*(pp. 138–191). Suhrkamp Verlag AG.Dahlgren, P. (2005). The internet, public spheres, and political communication: Dispersion and deliberation.

*Political Communication,**22*(2), 147–162.Terren, L., & Borge, R. (2021). Echo chambers on social media: A systematic review of the literature.

*Review of Communication Research,**9*, 99–118. https://doi.org/10.12840/ISSN.2255-4165.028Boulianne, S., Koc-Michalska, K., & Bimber, B. (2020). Right-wing populism, social media and echo chambers in western democracies.

*New Media & Society,**22*(4), 683–699. https://doi.org/10.1177/1461444819893983Cinelli, M., Morales, G.D.F., Galeazzi, A., Quattrociocchi, W., & Starnini, M. (2021). The echo chamber effect on social media.

*Proceedings of the National Academy of Sciences of the United States of America**118*(9).Benkler, Y., Faris, R., & Roberts, H. (2018).

*Network propaganda: Manipulation, disinformation, and radicalization in American politics*. Oxford University Press.Jacobs, A. Z., & Wallach, H. (2021). Measurement and fairness. In: Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency. FAccT ’21, pp. 375–385. Association for Computing Machinery, New York, NY, USA. https://doi.org/10.1145/3442188.3445901.

Jackman, S. (2008). Measurement. In

*The Oxford handbook of political methodology*. Oxford University Press. https://doi.org/10.1093/oxfordhb/9780199286546.003.0006.Arguedas, A. R., Robertson, C., Fletcher, R., & Nielsen, R. K. (2022). Echo chambers, filter bubbles, and polarisation: A literature review. Reuter Institute for the Study of Journalism. Accessed 10 March 2022.

Mahmoudi, A., Jemielniak, D., & Ciechanowski, L. (2024). Echo chambers in online social networks: A systematic literature review.

*IEEE Access,**12*, 9594–9620. https://doi.org/10.1109/ACCESS.2024.3353054Michiels, L., Leysen, J., Smets, A., & Goethals, B. What are filter bubbles really? a review of the conceptual and empirical work. In

*Adjunct Proceedings of the 30th ACM conference on user modeling, adaptation and personalization*(pp. 274–279). ACM. https://doi.org/10.1145/3511047.3538028. Accessed 29 January 2025.Kitchens, B., Johnson, S. L., & Gray, P. (2020). Understanding echo chambers and filter bubbles: The impact of social media on diversification and partisan shifts in news consumption.

*MIS Quarterly,**44*(4), 1619–1649.Interian, R., Marzo, R. G., Mendoza, I., & Ribeiro, C. C. Network polarization, filter bubbles, and echo chambers: an annotated review of measures and reduction methods.

*International Transactions in Operational Research*. https://doi.org/10.1111/itor.13224.Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., … Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews.

*Systematic Reviews,**18*(3), 1003583.Gough, D. (2007). Weight of evidence: A framework for the appraisal of the quality and relevance of evidence.

*Research Papers in Education,**22*(2), 213–228.Grant, M. J., & Booth, A. (2009). A typology of reviews: An analysis of 14 review types and associated methodologies.

*Health Information & Libraries Journal,**26*(2), 91–108.Booth, A., Papaioannou, D., & Sutton, A. (2012). Systematic approaches to a successful literature review.

Biondi-Zoccai, G., Lotrionte, M., Landoni, G., & Modena, M. G. (2011). The rough guide to systematic reviews and meta-analyses.

*HSR Proceedings in Intensive Care and Cardiovascular Anesthesia,**3*(3), 161–173.We Are Social, DataReportal, Meltwater: Most Popular Social Networks Worldwide as of April 2024, Ranked by Number of Monthly Active Users (in millions) [Graph]. In Statista. Retrieved April 25, 2024, from https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/ (2024).

Silva, R., & Neiva, F. (2016). Systematic literature review in computer science—A practical guide. https://doi.org/10.13140/RG.2.2.35453.87524

Mahood, Q., Van Eerd, D., & Irvin, E. (2014). Searching for grey literature for systematic reviews: Challenges and benefits.

*Research Synthesis Methods,**5*(3), 221–234.Haddaway, N. R., Collins, A. M., Coughlin, D., & Kirk, S. (2015). The role of google scholar in evidence reviews and its applicability to grey literature searching.

*PLoS ONE,**10*(9), 0138237.Boeker, M., Vach, W., & Motschall, E. (2013). Google scholar as replacement for systematic literature searches: Good relative recall and precision are not enough.

*BMC Medical Research Methodology,**13*(1), 131. https://doi.org/10.1186/1471-2288-13-131Dickersin, K. (1990). The existence of publication bias and risk factors for its occurrence.

*JAMA: The Journal of the American Medical Association,**263*, 1385–9. https://doi.org/10.1001/jama.263.10.1385Drucker, A. M., Fleming, P., & Chan, A.-W. (2016). Research techniques made simple: Assessing risk of bias in systematic reviews.

*Journal of Investigative Dermatology,**136*(11), 109–114. https://doi.org/10.1016/j.jid.2016.08.021Lombard, M., Snyder-Duch, J., & Bracken, C. C. (2006). Content analysis in mass communication: Assessment and reporting of intercoder reliability.

*Human Communication Research,**28*(4), 587–604. https://doi.org/10.1111/j.1468-2958.2002.tb00826.xO’Connor, C., & Joffe, H. (2020). Intercoder reliability in qualitative research: Debates and practical guidelines.

*International Journal of Qualitative Methods,**19*, 1609406919899220. https://doi.org/10.1177/1609406919899220Cohen, J. (1960). A coefficient of agreement for nominal scales.

*Educational and Psychological Measurement,**20*(1), 37–46.Elo, S., & Kyngäs, H. (2008). The qualitative content analysis process.

*Journal of Advanced Nursing,**62*(1), 107–115.Hsieh, H.-F., & Shannon, S. E. (2005). Three approaches to qualitative content analysis.

*Qualitative Health Research,**15*(9), 1277–1288.Olteanu, A., Castillo, C., Diaz, F., & Kıcıman, E. (2019). Social data: Biases, methodological pitfalls, and ethical boundaries.

*Frontiers in Big Data,**2*, 13.Siddaway, A. P., Wood, A. M., & Hedges, L. V. (2019). How to do a systematic review: A best practice guide for conducting and reporting narrative reviews, meta-analyses, and meta-syntheses.

*Annual Review of Psychology,**70*(1), 747–770.Popay, J., Roberts, H., Sowden, A., Petticrew, M., Arai, L., Rodgers, M., Britten, N., Roen, K., Duffy, S., et al. (2006). Guidance on the conduct of narrative synthesis in systematic reviews.

*A Product from the ESRC Methods Programme Version,**1*(1), 92.We Are Social, Hootsuite, DataReportal.: Most popular social networks worldwide as of November 2024, ranked by number of monthly active users (in millions). publisher: Statista (2024). https://www.statista.com/statistics/272014/global-social-networks-ranked-by-number-of-users/. Accessed 06 April 2022.

Bessi, A., Zollo, F., Del Vicario, M., Puliga, M., Scala, A., Caldarelli, G., Uzzi, B., & Quattrociocchi, W. (2016). Users polarization on facebook and youtube.

*PLOS ONE**11*(8).Del Vicario, M., Bessi, A., Zollo, F., Petroni, F., Scala, A., Caldarelli, G., Stanley, H. E., & Quattrociocchi, W. (2016). The spreading of misinformation online.

*Proceedings of the National Academy of Sciences of the United States of America,**113*(3), 554–559.Schmidt, A. L., Zollo, F., Scala, A., Betsch, C., & Quattrociocchi, W. (2018). Polarization of the vaccination debate on facebook.

*Vaccine,**36*(25), 3606–3612. https://doi.org/10.1016/j.vaccine.2018.05.040Zollo, F., Bessi, A., Del Vicario, M., Scala, A., Caldarelli, G., Shekhtman, L., Havlin, S., & Quattrociocchi, W. (2017). Debunking in a world of tribes.

*PLOS ONE**12*(7).Batorski, D., & Grzywinska, I. (2018). Three dimensions of the public sphere on facebook.

*Information, Communication & Society,**21*(3), 356–374. https://doi.org/10.1080/1369118X.2017.1281329Cota, W., Ferreira, S. C., Pastor-Satorras, R., & Starnini, M. (2019). Quantifying echo chamber effects in information spreading over political communication networks.

*EPJ Data Science**8*(1).Guo, L., Rohde, J. A., & Wu, H. D. (2020). Who is responsible for twitter’s echo chamber problem? Evidence from 2016 us election networks.

*Information, Communication & Society,**23*(2), 234–251. https://doi.org/10.1080/1369118X.2018.1499793Nikolov, D., Lalmas, M., Flammini, A., & Menczer, F. (2019). Quantifying biases in online information exposure.

*Journal of the Association for Information Science and Technology,**70*(3), 218–229. https://doi.org/10.1002/asi.24121Masip, P., Suau, J., & Ruiz-Caballero, C. (2020). Incidental exposure to non-like-minded news through social media: Opposing voices in echo-chambers’ news feeds.

*Media and Communication,**8*(4), 53–62.Guarino, S., Trino, N., Celestini, A., Chessa, A., & Riotta, G. (2020). Characterizing networks of propaganda on twitter: a case study.

*Applied Network Science**5*(1).Del Valle, M. E., & Borge Bravo, R. (2018). Echo chambers in parliamentary twitter networks: The catalan case.

*International Journal of Communication,**12*, 1715–1735.Matuszewski, P. (2019). Selective exposure on polish political and news media facebook pages.

*Polish Sociological Review,**206*, 177–197. https://doi.org/10.26412/psr206.04Rafail, P., & Freitas, I. (2019). Grievance articulation and community reactions in the men’s rights movement online.

*Social Media + Society**5*(2). https://doi.org/10.1177/2056305119841387Whittaker, J., Looney, S., Reed, A., & Votta, F. (2021). Recommender systems and the amplification of extremist content.

*Internet Policy Review**10*(3).Monti, C., D’Ignazi, J., Starnini, M., & Morales, G. D. F. (2023). Evidence of demographic rather than ideological segregation in news discussion on reddit. In: Proceedings of the ACM Web Conference 2023 (WWW ’23) (pp. 1–10). ACM, New York, NY, USA. https://doi.org/10.1145/3543507.3583468

Treen, K., Williams, H., O’Neill, S., & Coan, T. G. (2022). Discussion of climate change on reddit: Polarized discourse or deliberative debate?

*Environmental Communication,**16*(5), 680–698. https://doi.org/10.1080/17524032.2022.2050776Morales, G. D. F., Monti, C., & Starnini, M. (2021). No echo in the chambers of political interactions on reddit.

*Scientific Reports**11*(1).Gao, Y., Liu, F., & Gao, L. (2023). Echo chamber effects on short video platforms.

*Scientific Reports,**13*, 6282. https://doi.org/10.1038/s41598-023-33370-1Dubois, E., Minaeian, S., Paquet-Labelle, A., & Beaudry, S. (2020). Who to trust on social media: How opinion leaders and seekers avoid disinformation and echo chambers.

*Social Media + Society**6*(2). https://doi.org/10.1177/2056305120913993Schmidt, A. L., Peruzzi, A., Scala, A., Cinelli, M., Pomerantsev, P., Applebaum, A., Gaston, S., Fusi, N., Peterson, Z., Severgnini, G., Cesco, A. F., Casati, D., Novak, P. K., Stanley, H. E., Zollo, F., & Quattrociocchi, W. (2020). Measuring social response to different journalistic techniques on facebook.

*Humanities & Social Sciences Communications,**7*(1), 17.Koivula, A., Kaakinen, M., Oksanen, A., & Rasanen, P. (2019). The role of political activity in the formation of online identity bubbles.

*Policy and Internet,**11*(4), 396–417.Jones-Jang, S. M., & Chung, M. (2022). Can we blame social media for polarization? Counter-evidence against filter bubble claims during the covid-19 pandemic.

*New Media & Society*, 14614448221099591Burnett, A., Knighton, D., & Wilson, C. (2022). The self-censoring majority: How political identity and ideology impacts willingness to self-censor and fear of isolation in the united states.

*Social Media + Society**8*(3).Justwan, F., Baumgaertner, B., Carlisle, J. E., Clark, A. K., & Clark, M. (2018). Social media echo chambers and satisfaction with democracy among democrats and republicans in the aftermath of the 2016 us elections.

*Journal of Elections Public Opinion and Parties,**28*(4), 424–442.Neely, S. R. (2021). Politically motivated avoidance in social networks: A study of facebook and the 2020 presidential election.

*Social Media + Society**7*(4). https://doi.org/10.1177/20563051211055438Eady, G., Nagler, J., Guess, A., Zilinsky, J., & Tucker, J. A. (2019). How many people live in political bubbles on social media? evidence from linked survey and twitter data.

*SAGE OPEN**9*(1). https://doi.org/10.1177/2158244019832705Boutyline, A., & Willer, R. (2017). The social structure of political echo chambers: Variation in ideological homophily in online networks.

*Political Psychology,**38*(3), 551–569. https://doi.org/10.1111/pops.12337Beam, M. A., Hutchens, M. J., & Hmielowski, J. D. (2018). Facebook news and (de)polarization: Reinforcing spirals in the 2016 us election.

*Information, Communication & Society,**21*(7), 940–958. https://doi.org/10.1080/1369118X.2018.1444783Barbera, P., Jost, J. T., Nagler, J., Tucker, J. A., & Bonneau, R. (2015). Tweeting from left to right: Is online political communication more than an echo chamber?

*Psychological Science,**26*(10), 1531–1542. https://doi.org/10.1177/0956797615594620Nordbrandt, M. (2019). Affective polarization in the digital age: Testing the direction of the relationship between social media and users’ feelings for out-group parties.

*New Media & Society*. https://doi.org/10.1177/14614448211044393Nyhan, B., Settle, J., Thorson, E., et al. (2023). Like-minded sources on facebook are prevalent but not polarizing.

*Nature,**620*, 137–144. https://doi.org/10.1038/s41586-023-06297-wWang, X., Sirianni, A. D., Tang, S., Zheng, Z., & Fu, F. (2020). Public discourse and social network echo chambers driven by socio-cognitive biases.

*Physical Review X**10*(4). https://doi.org/10.1103/PhysRevX.10.041042Lin, H., Wang, Y., Lee, J., & Kim, Y. (2023). The effects of disagreement and unfriending on political polarization: A moderated-mediation model of cross-cutting discussion on affective polarization via unfriending contingent upon exposure to incivility.

*Journal of Computer-Mediated Communication,**28*(4), 022. https://doi.org/10.1093/jcmc/zmad022Powers, E., Koliska, M., & Guha, P. (2019). “Shouting matches and echo chambers”: Perceived identity threats and political self-censorship on social media.

*International Journal of Communication,**13*, 3630–3649.Bail, C. A., Argyle, L. P., Brown, T. W., Bumpus, J. P., Chen, H., Hunzaker, M. F., Lee, J., Mann, M., Merhout, F., & Volfovsky, A. (2018). Exposure to opposing views on social media can increase political polarization.

*Proceedings of the National Academy of Sciences,**115*(37), 9216–9221.Bodo, B., Helberger, N., Eskens, S., & Moller, J. (2019). Interested in diversity: The role of user attitudes, algorithmic feedback loops, and policy in news personalization.

*Digital Jorunalism,**7*(2), 206–229. https://doi.org/10.1080/21670811.2018.1521292Chan, M., Chen, H.-T., & Lee, F. L. F. (2019). Examining the roles of political social network and internal efficacy on social media news engagement: A comparative study of six asian countries.

*International Journal of Press-Politics,**24*(2), 127–145. https://doi.org/10.1177/1940161218814480Matz, S. C. (2021). Personal echo chambers: Openness-to-experience is linked to higher levels of psychological interest diversity in large-scale behavioral data.

*Journal of Personality and Social Psychology,**121*(6), 1284–1300.Boulianne, S., & Koc-Michalska, K. (2022). The role of personality in political talk and like-minded discussion.

*International Journal of Press-Politics,**27*(1), 285–310. https://doi.org/10.1177/1940161221994096Kaiser, J., & Rauchfleisch, A. (2020). Birds of a feather get recommended together: Algorithmic homophily in youtube’s channel recommendations in the United States and Germany.

*Social Media + Society**6*(4). https://doi.org/10.1177/2056305120969914Hilbert, M., Ahmed, S., Cho, J., Liu, B., & Luu, J. (2018). Communicating with algorithms: A transfer entropy analysis of emotions-based escapes from online echo chambers.

*Communication Methods and Measures,**12*(4), 260–275. https://doi.org/10.1080/19312458.2018.1479843Hartmann, D., Pereira, J. R. L., Streitbörger, C., & Berendt, B. (2024). Addressing the regulatory gap: Moving towards an EU AI audit ecosystem beyond the AIA by including civil society.

Bright, J. (2018). Explaining the emergence of political fragmentation on social media: The role of ideology and extremism.

*Journal of Computer-Mediated Communication,**23*(1), 17–33.Bastos, M., Mercea, D., & Baronchelli, A. (2018). The geographic embedding of online echo chambers: Evidence from the Brexit campaign.

*PLOS ONE**13*(11).Mahrt, M. (2019). Beyond Filter Bubbles and Echo Chambers: The Integrative Potential of the Internet. Digital Communication Research

*5*, 246. Digital Communications Research, Berlin. https://doi.org/10.17174/dcr.v5.0Grusauskaite, K., Carbone, L., Harambam, J., & Aupers, S. (2024). Debating (in) echo chambers: How culture shapes communication in conspiracy theory networks on youtube.

*New Media & Society,**26*(12), 7037–7057. https://doi.org/10.1177/14614448231162585Mosleh, M., Pennycook, G., Arechar, A. A., & Rand, D. G. (2021). Cognitive reflection correlates with behavior on twitter.

*Nature Communications**12*(1).Cann, T. J. B., Weaver, I. S., & Williams, H. T. P. (2021). Ideological biases in social sharing of online information about climate change.

*PLOS ONE**16*(4).Guerrero-Sole, F. (2018). Interactive behavior in political discussions on twitter: Politicians, media, and citizens’ patterns of interaction in the 2015 and 2016 electoral campaigns in spain.

*Social Media + Society**4*(4). https://doi.org/10.1177/2056305118808776Del Vicario, M., Zollo, F., Caldarelli, G., Scala, A., & Quattrociocchi, W. (2017). Mapping social dynamics on facebook: The brexit debate.

*Social Networks,**50*, 6–16.Brugnoli, E., Cinelli, M., Quattrociocchi, W., & Scala, A. (2019). Recursive patterns in online echo chambers.

*Scientific Reports**9*.Del Vicario, M., Vivaldo, G., Bessi, A., Zollo, F., Scala, A., Caldarelli, G., & Quattrociocchi, W. (2016). Echo chambers: Emotional contagion and group polarization on facebook.

*Scientific Reports**6*. https://doi.org/10.1038/srep37825Asatani, K., Yamano, H., Sakaki, T., & Sakata, I. (2021). Dense and influential core promotion of daily viral information spread in political echo chambers.

*Scientific Reports**11*(1).Choi, D., Chun, S., Oh, H., Han, J., & Kwon, T. (2020). Rumor propagation is amplified by echo chambers in social media.

*Scientific Reports,**10*(1), 310.Wolfowicz, M., Weisburd, D., & Hasisi, B. (2023). Examining the interactive effects of the filter bubble and the echo chamber on radicalization.

*Journal of Experimental Criminology*.Nguyen, C. T. (2020). Echo chambers and epistemic bubbles.

*Episteme,**17*(2), 141–161.McPherson, M., Smith-Lovin, L., & Cook, J. M. (2001). Birds of a feather: Homophily in social networks.

*Annual Review of Sociology,**27*(1), 415–444.Wollebaek, D., Karlsen, R., Steen-Johnsen, K., & Enjolras, B. (2019). Anger, fear, and echo chambers: The emotional basis for online behavior.

*Social Media + Society**5*(2). https://doi.org/10.1177/2056305119829859Jamieson, K., & Hall, C. (2008).

*Echo chamber: Rush limbaugh and the conservative media establishment*. Oxford University Press.Sandvig, C., Hamilton, K., Karahalios, K., & Langbort, C. (2014).

*Auditing algorithms: Research methods for detecting discrimination on internet platforms*. Data and Discrimination: Converting Critical Concerns into Productive Inquiry.Ohme, J., Araujo, T., Boeschoten, L., Freelon, D., Ram, N., Reeves, B. B., & Robinson, T. N. (2023). Digital trace data collection for social media effects research: Apis, data donation, and (screen) tracking.

*Communication Methods and Measures*1–18.Aruguete, N., Calvo, E., & Ventura, T. (2023). News by popular demand: Ideological congruence, issue salience, and media reputation in news sharing(1).

*International Journal of Press-Politics*. https://doi.org/10.1177/19401612211057068Wieringa, M., van Geenen, D., Schafer, M. T., & Gorzeman, L. (2018). Political topic-communities and their framing practices in the dutch twittersphere.

*Internet Policy Review**7*(2).Rusche, F. (2022). Few voices, strong echo: Measuring follower homogeneity of politicians’ twitter accounts.

*New Media & Society*, 14614448221099860. https://doi.org/10.1177/14614448221099860Kratzke, N. (2023). How to find orchestrated trolls? a case study on identifying polarized twitter echo chambers.

*Computers**12*(3). https://doi.org/10.3390/computers12030057Hagen, L., Fox, A., O’Leary, H., Dyson, D., Walker, K., Lengacher, C. A., & Hernandez, R. (2022). The role of influential actors in fostering the polarized covid-19 vaccine discourse on twitter: Mixed methods of machine learning and inductive coding.

*JMIR Infodemiology,**2*(1), 34231–34231. https://doi.org/10.2196/34231Colleoni, E., Rozza, A., & Arvidsson, A. (2014). Echo chamber or public sphere? predicting political orientation and measuring political homophily in twitter using big data.

*Journal of Communication,**64*(2), 317–332.Bruns, A. (2017). Echo chamber? what echo chamber? reviewing the evidence. In

*6th Biennial future of journalism conference (FOJ17)*.Matuszewski, P., & Szabo, G. (2019). Are echo chambers based on partisanship? Twitter and political polarity in poland and hungary.

*Social Media + Society**5*(2). https://doi.org/10.1177/2056305119837671Del Valle, M. E., Broersma, M., & Ponsioen, A. (2022). Political interaction beyond party lines: Communication ties and party polarization in parliamentary twitter networks.

*Social Science Computer Review*. https://doi.org/10.1177/0894439320987569Enjolras, B., & Salway, A. (2022). Homophily and polarization on political twitter during the 2017 Norwegian election.

*Social Network Analysis and Mining,**13*(1), 10. https://doi.org/10.1007/s13278-022-01018-zFurman, I., & Tunc, A. (2020). The end of the habermassian ideal? Political communication on twitter during the 2017 Turkish constitutional referendum.

*Policy and Internet,**12*(3), 311–331. https://doi.org/10.1002/poi3.218Radicioni, T., Saracco, F., Pavan, E., & Squartini, T. (2021). Analysing twitter semantic networks: The case of 2018 Italian elections.

*Scientific Reports**11*(1).Gaumont, N., Panahi, M., & Chavalarias, D. (2018). Reconstruction of the socio-semantic dynamics of political activist twitter networks-method and application to the 2017 French presidential election.

*PLOS ONE**13*(9).Radicioni, T., Squartini, T., Pavan, E., & Saracco, F. (2021). Networked partisanship and framing: A socio-semantic network analysis of the Italian debate on migration.

*PLOS ONE**16*(8).Ceron, A., & Splendore, S. (2019). ‘Cheap talk’? second screening and the irrelevance of tv political debates.

*Journalism,**20*(8), 1108–1123. https://doi.org/10.1177/1464884919845443Samantray, A., & Pin, P. (2019). Credibility of climate change denial in social media.

*Palgrave Communications**5*.Shore, J., Baek, J., & Dellarocas, C. (2018). Network structure and patterns of information diversity on twitter.

*Management Information Systems Quarterly,**42*(3), 849–972.Flamino, J., Galeazzi, A., Feldman, S., Macy, M. W., Cross, B., Zhou, Z., Serafino, M., Bovet, A., Makse, H. A., & Szymanski, B. K. (2023). Political polarization of news media and influencers on twitter in the 2016 and 2020 us presidential elections.

*Nature Human Behaviour*. https://doi.org/10.1038/s41562-023-01550-8Tyagi, A., Uyheng, J., & Carley, K. M. (2021). Heated conversations in a warming world: affective polarization in online climate change discourse follows real-world climate anomalies.

*Social Network Analysis and Mining**11*(1).Bessi, A., Zollo, F., Del Vicario, M., Scala, A., Caldarelli, G., & Quattrociocchi, W. (2015). Trend of narratives in the age of misinformation.

*PLOS ONE**10*(8).Zollo, F., Novak, P.K., Del Vicario, M., Bessi, A., Mozetic, I., Scala, A., Caldarelli, G., & Quattrociocchi, W. (2015). Emotional dynamics in the age of misinformation.

*PLOS ONE**10*(9).Bakshy, E., Messing, S., & Adamic, L. A. (2015). Political science. exposure to ideologically diverse news and opinion on facebook.

*Science (New York, N.Y.)**348*(6239), 1130–1132. https://doi.org/10.1126/science.aaa1160Etta, G., Cinelli, M., Galeazzi, A., Valensise, C. M., Quattrociocchi, W., & Conti, M. (2022). Comparing the impact of social media regulations on news consumption.

*IEEE Transactions on Computational Social Systems*. https://doi.org/10.1109/TCSS.2022.3171391Bessi, A. (2016). Personality traits and echo chambers on facebook.

*Computers in Human Behavior,**65*, 319–324. https://doi.org/10.1016/j.chb.2016.08.016Goel, V., Sahnan, D., Dutta, S., Bandhakavi, A., & Chakraborty, T. (2023). Hatemongers ride on echo chambers to escalate hate speech diffusion.

*PNAS Nexus**2*(3).Fletcher, R., Kalogeropoulos, A., & Nielsen, R. K. (2021). More diverse, more politically varied: How social media, search engines and aggregators shape news repertoires in the united kingdom.

*New Media & Society*. https://doi.org/10.1177/14614448211027393Flaxman, S., Goel, S., & Rao, J. M. (2016). Filter bubbles, echo chambers, and online news consumption.

*Public Opinion Quarterly,**80*, 298–320.Muise, D., Hosseinmardi, H., Howland, B., Mobius, M., Rothschild, D., & Watts, D. J. (2022). Quantifying partisan news diets in web and tv audiences.

*Science Advances,**8*(28), 0083. https://doi.org/10.1126/sciadv.abn0083Urman, A. (2019). News consumption of Russian Vkontakte users: Polarization and news avoidance.

*International Journal of Communication,**13*, 5158–5182.Bond, R. M., & Sweitzer, M. D. (2022). Political homophily in a large-scale online communication network.

*Communication Research,**49*(1), 93–115. https://doi.org/10.1177/0093650218813655Roth, C., Mazieres, A., & Menezes, T. (2020). Tubes and bubbles topological confinement of youtube recommendations.

*PLOS ONE**15*(4).Lima, L., Reis, J. C. S., Melo, P., Murai, F., Araújo, L., Vikatos, P., & Benevenuto, F. (2018). Inside the right-leaning echo chambers: Characterizing gab, an unmoderated social system. In

*Proceedings of the 2018 IEEE/ACM international conference on advances in social networks analysis and mining. ASONAM ’18*(pp. 515–522). IEEE Press.Wang, D., & Qian, Y. (2021). Echo chamber effect in rumor rebuttal discussions about covid-19 in china: Social media content and network analysis study.

*Journal of Medical Internet Research*. https://doi.org/10.2196/27009Wang, D., Zhou, Y., & Ma, F. (2022). Opinion leaders and structural hole spanners influencing echo chambers in discussions about covid-19 vaccines on social media in china: Network analysis.

*Journal of Medical Internet Research,**24*(11), 40701. https://doi.org/10.2196/40701Light, R., & Moody, J. (2021). 16network basics: Points, lines, and positions. In

*The Oxford handbook of social networks*. Oxford University Press. https://doi.org/10.1093/oxfordhb/9780190251765.013.2Cinelli, M., Pelicon, A., Mozetic, I., Quattrociocchi, W., Novak, P. K., & Zollo, F. (2021). Dynamics of online hate and misinformation.

*Scientific Reports**11*(1).Traag, V. A., Waltman, L., & Eck, N. J. (2019). From Louvain to Leiden: Guaranteeing well-connected communities.

*Scientific Reports,**9*(1), 5233.Kim, B., Lee, K., Xue, L., & Niu, X. (2017). A review of dynamic network models with latent variables.

*Statistics Surveys**12*. https://doi.org/10.1214/18-SS121Bovet, A., & Grindrod, P. (2022). Organization and evolution of the UK far-right network on telegram.

*Applied Network Science**7*(1). https://doi.org/10.1007/s41109-022-00513-8Srba, I., Moro, R., Tomlein, M., Pecher, B., Simko, J., Stefancova, E., Kompan, M., Hrckova, A., Podrouzek, J., Gavornik, A., & Bielikova, M. (2023). Auditing youtube’s recommendation algorithm for misinformation filter bubbles.

*ACM Transactions on Recommender Systems**1*(1).Zerback, T., & Kobilke, L. (2022). The role of affective and cognitive attitude extremity in perceived viewpoint diversity exposure.

*New Media & Society*, 14614448221117484. https://doi.org/10.1177/14614448221117484Mosleh, M., Martel, C., Eckles, D., & Rand, D. G. (2021). Shared partisanship dramatically increases social tie formation in a twitter field experiment.

*Proceedings of the National Academy of Sciences of the United States of America**118*(7).Suelflow, M., Schaefer, S., & Winter, S. (2019). Selective attention in the news feed: An eye-tracking study on the perception and selection of political news posts on facebook.

*New Media & Society,**21*(1), 168–190. https://doi.org/10.1177/1461444818791520Mellon, J., & Prosser, C. (2017). Twitter and facebook are not representative of the general population: Political attitudes and demographics of british social media users.

*Research & Politics,**4*(3), 205316801772000.Center, P. R. (2021). Social Media Fact Sheet. https://www.pewresearch.org/internet/fact-sheet/social-media/

Jasny, L., Waggle, J., & Fisher, D. R. (2015).

*An empirical examination of echo chambers in US climate policy networks,**5*(8), 782–786.Guess, A., Lyons, B., Nyhan, B., & Reifler, J. (2018). Avoiding the echo chamber about echo chambers: Why selective exposure to like-minded political news is less prevalent than you think.

Barbera, P. (2013). Birds of the same feather tweet together: Bayesian ideal point estimation using twitter data.

*SSRN Electronic Journal**23*. https://doi.org/10.2139/ssrn.2108098Gallwitz, F., & Kreil, M. (2021). The rise and fall of ’social bot’ research. SSRN.

Neudert, L., Kollanyi, B., & Howard, P. N. (2017). Junk news and bots during the German parliamentary election: What are German voters sharing over twitter?.

Silva, B. C., & Proksch, S.-O. (2021). Fake it ‘til you make it: A natural experiment to identify European politicians’ benefit from twitter bots.

*American Political Science Review,**115*(1), 316–322.VanderWeele, T. J., & Weihua, A. (2014). Social networks and causal inference. Handbooks of sociology and social research. In

*Handbook of Causal Analysis for Social Research*(pp. 353–374). Springer.Frank, K. A., & Xu, R. (2021). Causal inference for social network analysis. In

*The Oxford handbook of social networks*. Oxford University Press. https://doi.org/10.1093/oxfordhb/9780190251765.013.21Brashears, M. E., & Gladstone, E. (2021). Social network experiments. In

*The Oxford handbook of social networks*. Oxford University Press. https://doi.org/10.1093/oxfordhb/9780190251765.013.12Walther, S., & Mccoy, A. (2021). Us extremism on telegram: Fueling disinformation, conspiracy theories, and accelerationism.

*Perspectives on Terrorism**15*.Stokel-Walker, C. (2022). How to fight disinformation.

*New Scientist,**253*(3378), 8. https://doi.org/10.1016/S0262-4079(22)00458-4Madrigal, A. (2012). Dark social: We have the whole history of the web wrong.

*The Atlantic**12*.Belur, J., Tompson, L., Thornton, A., & Simon, M. (2021). Interrater reliability in systematic review methodology: Exploring variation in coder decision-making.

*Sociological Methods & Research,**50*(2), 837–865.Tomlein, M., Pecher, B., Simko, J., Srba, I., Moro, R., Stefancova, E., Kompan, M., Hrckova, A., Podrouzek, J., & Bielikova, M. (2021). An audit of misinformation filter bubbles on youtube: Bubble bursting and recent behavior changes. In

*Fifteenth ACM conference on recommender systems*(pp. 1–11). Association for Computing Machinery, New York, NY, USA. https://doi.org/10.1145/3460231.3474241Ackermann, K., & Stadelmann-Steffen, I. (2022). Voting in the echo chamber? patterns of political online activities and voting behavior in Switzerland.

*Swiss Political Science Review,**28*(2), 377–400.Auxier, B. E., & Vitak, J. (2019). Factors motivating customization and echo chamber creation within digital news environments.

*Social Media + Society**5*(2). https://doi.org/10.1177/2056305119847506Bodrunova, S. S., Blekanov, I. S., & Tarasov, N. (2023). Echo chambers on Russian twitter. In G. Meiselwitz (Ed.),

*Social computing and social media: Applications in communication, social communities, and e-services. Lecture notes in computer science*(Vol. 14025, pp. 167–182). Springer. https://doi.org/10.1007/978-3-031-35801-0_13Cargnino, M., & Neubaum, G. (2022). Is it better to strike a balance? how exposure to congruent and incongruent opinion climates on social networking sites impacts users’ processing and selection of information.

*New Media & Society*, 14614448221083914.Cargnino, M., Neubaum, G., & Winter, S. (2023). We’re a good match: Selective political friending on social networking sites.

*Communications,**48*(2), 202–225.Cheng, Z., Marcos-Marne, H., & Zúñiga, H. (2023). Birds of a feather get angrier together: Social media news use and social media political homophily as antecedents of political anger.

*Political Behavior*, 1–17.De Lima-Santos, M. F., & Ceron, W. (2023). Disinformation echo chambers on facebook. In

*Fighting fake facts*(pp. 61–90). MDPI, Basel. Chap. 4. https://doi.org/10.3390/books978-3-0365-1347-8-4Ebeling, R., Nobre, J., & Becker, K. (2023). A multi-dimensional framework to analyze group behavior based on political polarization.

*Expert Systems with Applications,**233*, 120768. https://doi.org/10.1016/j.eswa.2023.120768Enjolras, B. (2023). Does relational polarization entail ideological polarization? the case of the 2017 Norwegian election campaign on twitter.

*International Journal of Communication,**17*, 2394–2421.Erickson, J., Yan, B., & Huang, J. (2023). Bridging echo chambers? Understanding political partisanship through semantic network analysis.

*Social Media + Society**9*(3). https://doi.org/10.1177/20563051231186368Hada, R., Ebrahimi Fard, A., Shugars, S., Bianchi, F., Rossini, P., Hovy, D., Tromble, R., & Tintarev, N. (2023). Beyond digital “echo chambers;;: The role of viewpoint diversity in political discussion. In

*Proceedings of the sixteenth ACM international conference on web search and data mining. WSDM ’23*(pp. 33–41). Association for Computing Machinery, New York, NY, USA. https://doi.org/10.1145/3539597.3570487Hong, S., & Kim, S. H. (2016). Political polarization on twitter: Implications for the use of social media in digital governments.

*Government Information Quarterly,**33*(4), 777–782. https://doi.org/10.1016/j.giq.2016.04.007Liu, R., Greene, K. T., Liu, R., Mandic, M., Valentino, B.A., Vosoughi, S., & Subrahmanian, V. S. (2021). Using impression data to improve models of online social influence.

*Scientific Reports**11*(1).Ludwig, K., Grote, A., Iana, A., Alam, M., Paulheim, H., Sack, H., Weinhardt, C., & Müller, P. (2023). Divided by the algorithm? the (limited) effects of content-and sentiment-based news recommendation on affective, ideological, and perceived polarization.

*Social Science Computer Review,**41*(6), 2188–2210.Min, Y., Jiang, T., Jin, C., Li, Q., & Jin, X. (2019). Endogenetic structure of filter bubble in social networks.

*Royal Society Open Science**6*(11).Mirlohi, A., Mahdavimoghaddam, J., Jovanovic, J., Al-Obeidat, F.N., Khani, M., Ghorbani, A. A., & Bagheri, E. (2022). Social alignment contagion in online social networks.

*IEEE Transactions on Computational Social Systems*.Shmargad, Y., & Klar, S. (2019). How partisan online environments shape communication with political outgroups.

*International Journal of Communication,**13*, 2287–2313.Tsai, W.-H.S., Tao, W., Chuan, C.-H., & Hong, C. (2020). Echo chambers and social mediators in public advocacy issue networks.

*Public Relations Review,**46*(1), 101882. https://doi.org/10.1016/j.pubrev.2020.101882Turetsky, K. M., & Riddle, T. A. (2018). Porous chambers, echoes of valence and stereotypes: A network analysis of online news coverage interconnectedness following a nationally polarizing race-related event.

*Social Psychological and Personality Science,**9*(2), 163–175.Vaccari, C., Valeriani, A., Barbera, P., Jost, J. T., Nagler, J., & Tucker, J. A. (2016). Of echo chambers and contrarian clubs: Exposure to political disagreement among German and Italian users of twitter.

*Social Media + Society**2*(3). https://doi.org/10.1177/2056305116664221Villa, G., Pasi, G., & Viviani, M. (2021). Echo chamber detection and analysis a topology- and content-based approach in the covid-19 scenario.

*Social Network Analysis and Mining**11*(1).Williams, H. T. P., McMurray, J. R., Kurz, T., & Hugo Lambert, F. (2015). Network analysis reveals open forums and echo chambers in social media discussions of climate change.

*Global Environmental Change,**32*, 126–138. https://doi.org/10.1016/j.gloenvcha.2015.03.006

## Funding

Open Access funding enabled and organized by Projekt DEAL.

## Author information

### Authors and Affiliations

### Corresponding author

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Appendix

### Appendix

### 1.1 A: Users and data points of platforms in corpus literature

### 1.2 B: Publication sources in corpus literature

See Table 5.

### 1.3 C: Table of results

References | Country | Method | Focus | Platform | Result |
|---|---|---|---|---|---|
Ackermann and Stadelmann-Steffen [167] | Swiss | Surveys | Elections and EC | Social Media in General | Mixed |
Aruguete et al. [108] | Argentina, Brasil, US | CSS | News sharing behavior | Positive | |
Asatani et al. [99] | Japan | CSS | EC hypothesis | Positive | |
Auxier and Vitak [168] | US | Surveys | Cognitive states, emotions, personality traits | Social Media in General, mobile news applications | Mixed |
Bail et al. [81] | US | Experiment | EC hypothesis | Negative | |
Bakshy et al. [129] | US | CSS | EC hypothesis | Positive | |
Barbera et al. [75] | US | CSS | EC hypothesis | Mixed | |
Bastos et al. [90] | UK | CSS | Geographic embedding of Echo Chambers | Positive | |
Batorski and Grzywinska [51] | Poland | CSS | EC hypothesis | Positive | |
Beam et al. [74] | US | Surveys | EC hypothesis | Negative | |
Bessi [131] | US | CSS | Cognitive associations with EC | Positive | |
Bessi et al. [47] | US | CSS | EC hypothesis | Facebook, Youtube | Positive |
Bessi et al. [127] | Italy | CSS | Misinformation | Positive | |
Bodo et al. [82] | Netherlands | Surveys | News sharing and consuming | Social Media in General | Positive |
Bond and Sweitzer [137] | US | CSS | EC hypothesis | Positive | |
Boulianne and Koc-Michalska [85] | France, UK, US | Surveys | Extremism, radicalization and echo chambers | Social Media in General | Negative |
Boulianne et al. [16] | France, UK, US | Surveys | Cognitive states, emotions, personality traites | Social Media in General | Negative |
Boutyline and Willer [73] | US | CSS | EC hypothesis | Positive | |
Bovet and Grindrod [146] | UK | CSS | Extremism and echo chambers | Telegram | Mixed |
Bright [89] | EU | CSS | EC hypothesis | Mixed | |
Brugnoli et al. [97] | Italy | CSS | EC hypothesis | Positive | |
Bruns [114] | Australia | CSS | EC hypothesis | Negative | |
Bodrunova et al. [169] | Russia | CSS | EC Hypothesis | Positive | |
Burnett et al. [69] | US | Surveys | News sharing and consuming | Social Media in General | Negative |
Cann et al. [94] | US, UK | CSS | Climate change and echo chambers | Positive | |
Cargnino and Neubaum [170] | Germany | Experiment | Cognitive states, emotions, personality traites | Negative | |
Cargnino et al. [171] | Germany | Experiment | Echo chamber hypothesis | Social Media in General | Positive |
Ceron and Splendore [122] | Italy | CSS | TV, social media and echo chambers | Positive | |
Chan et al. [83] | Taiwan, Japan, Korea | Surveys | News sharing and consuming | Social Media in General | Mixed |
Cheng et al. [172] | US | Surveys | Cognitive states, emotions, personality traites | Social Media in General | Negative |
Choi et al. [100] | US | CSS | Misinformation | Positive | |
Cinelli et al. [8] | EU | CSS | EC hypothesis | Positive | |
Cinelli et al. [17] | US | CSS | Recommender systems | Twitter, Facebook, Reddit | Mixed |
Cinelli et al. [143] | Italy | CSS | Misinformation | YouTube | Positive |
Colleoni et al. [113] | US | CSS | EC hypothesis | Mixed | |
Cota et al. [52] | Brasli | CSS | EC hypothesis | Positive | |
Del Valle and Borge Bravo [57] | Spain | CSS | Parliamentary discussions and echo chambers | Positive | |
Del Valle et al. [116] | Netherlands | CSS | Parliamentary discussions and echo chambers | Negative | |
De Lima-Santos and Ceron [173] | Brazil | CSS | Covid-19 vaccines and EC | Positive | |
Del Vicario et al. [48] | US | CSS | Misinformation | Positive | |
Del Vicario et al. [98] | US | CSS | Emotions and echo chambers | Positive | |
Del Vicario et al. [96] | UK | CSS | EC hypothesis | Positive | |
Dubois and Blank [12] | UK | Surveys | EC hypothesis | Social Media in General | Negative |
Dubois et al. [65] | France | Surveys | EC hypothesis | Social Media in General | Mixed |
Ebeling et al. [174] | Brazil | Mixed Methods | Covid-19 vaccines and EC | Positive | |
Eady et al. [72] | US | Mixed Methods | EC hypothesis | Negative | |
Enjolras [175] | Norway | CSS | Elections and EC | Mixed | |
Enjolras and Salway [117] | Norway | CSS | Echo chamber hypothesis | Mixed | |
Erickson et al. [176] | USA | CSS | Elections and EC | Positive | |
Etta et al. [130] | US | CSS | EC hypothesis | Twitter, Gab | Positive |
Flamino et al. [125] | US | CSS | EC hypothesis | Mixed | |
Flaxman et al. [134] | US | CSS | EC hypothesis | Browser | Mixed |
Fletcher et al. [133] | UK | CSS | News sharing behavior | Browser | Mixed |
Furman and Tunc [118] | Turkey | CSS | EC hypothesis | Negative | |
Gao et al. [64] | China | CSS | EC hypothesis | Douyin, TikTok, Bilibili | Positive |
Gaumont et al. [120] | France | CSS | Opinion dynamics | Positive | |
Goel et al. [132] | US | CSS | Echo chamber hypothesis | Reddit, Twitter, Gab | Mixed |
Grusauskaite et al. [92] | - | Mixed-Methods | Extremism, radicalization, and EC | YouTube | Positive |
Guarino et al. [56] | Italy | CSS | EC hypothesis | Positive | |
Guerrero-Sole [95] | Spain | CSS | EC hypothesis | Positive | |
Guo et al. [53] | US | CSS | EC hypothesis | Mixed | |
Hada et al. [177] | - | CSS | Extremism, radicalization, and EC | Positive | |
Hagen et al. [112] | US | Mixed Methods | Vaccines, misinformation, and echo chambers | Mixed | |
Hilbert et al. [87] | US | Mixed Methods | Recommender systems and EC | YouTube | Positive |
Hong and Kim [178] | USA | CSS | Parliament representations and EC | Positive | |
Jones-Jang and Chung [68] | US | Surveys | Vaccines, misinformation and echo chambers | Social Media in General | Negative |
Justwan et al. [70] | US | Surveys | Cognitive states, emotions, personality traites | Social Media in General | Negative |
Kaiser and Rauchfleisch [86] | Germany, US | CSS | Recommender systems and EC | YouTube | Positive |
Kitchens et al. [24] | - | Mixed Methods | EC hypothesis | Facebook, Twitter, Reddit | Mixed |
Koivula et al. [67] | Finland | Surveys | News sharing and consuming | Social Media in General | Positive |
Kratzke [111] | Germany | CSS | EC hypothesis | Positive | |
Lima et al. [139] | US | CSS | EC hypothesis | Gab | Positive |
Liu et al. [179] | US | Experiment | Recommender systems and EC | Self-constructed platform | Positive |
Ludwig et al. [180] | Germany | Experiment | Recommender systems and EC | Social Media in General | Negative |
Masip et al. [55] | Spain | Surveys | EC hypothesis | Facebook, Twitter, Instagram | Negative |
Matuszewski and Szabo [115] | Poland | CSS | EC hypothesis | Positive | |
Matuszewski [58] | Poland, Hungary | CSS | EC hypothesis | Negative | |
Matz [84] | US | Mixed Methods | Cognitive states, emotions, personality traites | Mixed | |
Min et al. [181] | China | Experiment | EC hypothesis | Positive | |
Mirlohi et al. [182] | - | CSS | News sharing behavior | Twitter, Forsquare | Mixed |
Monti et al. [61] | US | CSS | EC hypothesis | Negative | |
Morales et al. [63] | US | CSS | EC hypothesis | Negative | |
Mosleh et al. [93] | US | Experiment | EC hypothesis | Positive | |
Mosleh et al. [149] | US | Mixed Methods | Cognitive states, emotions, personality traites | Mixed | |
Muise et al. [135] | US | CSS | TV, social media and echo chambers | Browser | Mixed |
Neely [71] | US | Surveys | Elections and EC | Mixed | |
Nikolov et al. [54] | US | CSS | Elections and EC | Social Media in General | Positive |
Nordbrandt [76] | Netherlands | Surveys | EC hypothesis | Social Media in General | Negative |
Nyhan et al. [77] | US | Experiment | Cognitive states, emotions, personality traites | Negative | |
Powers et al. [80] | US | Surveys | Elections and EC | Social Media in General | Negative |
Radicioni et al. [119] | Italy | CSS | TV, social media and echo chambers | Mixed | |
Radicioni et al. [121] | Italy | CSS | EC hypothesis | Mixed | |
Rafail and Freitas [59] | US | CSS | EC hypothesis | Positive | |
Roth et al. [138] | EU | CSS | EC hypothesis | YouTube | Mixed |
Rusche [110] | Germany | CSS | EC hypothesis | Mixed | |
Samantray and Pin [123] | - | CSS | Climate change | Mixed | |
Schmidt et al. 2020 | Italy | CSS | EC hypothesis | Positive | |
Schmidt et al. [49] | Italy | CSS | COVID-19, vaccines and echo chambers | Positive | |
Shmargad and Klar [183] | US | Experiment | News sharing behavior | Social Media in General | Positive |
Shore et al. [124] | US | CSS | EC hypothesis | Mixed | |
Srba et al. [147] | - | CSS | Misinformation | YouTube | Mixed |
Suelflow et al. [150] | US | Experiment | Recommender systems and EC | Positive | |
Sun et al. 2022 | US | CSS | Covid-19 vaccines and EC | YouTube | Mixed |
Tomlein et al. [166] | - | CSS | Misinformation | YouTube | Mixed |
Torregrosa et al. [6] | US | CSS | Extremism and echo chambers | Positive | |
Treen et al. 2022 | US | CSS | Climate change and EC | Mixed | |
Tsai et al. [184] | - | CSS | Boycotts and EC | Positive | |
Turetsky and Riddle [185] | US | CSS | News sharing behavior | Social Media in General | Negative |
Tyagi et al. [126] | US | CSS | Climate chance and echo chambers | Positive | |
Urman [136] | Russia | CSS | EC hypothesis | Vkontakte | Positive |
Vaccari et al. [186] | Italy, Germany | Surveys | EC hypothesis | Positive | |
Villa et al. [187] | EU | CSS | Covid-19 vaccines and EC | Positive | |
Wang and Qian [140] | China | CSS | Vaccines, misinformation and echo chambers | Positive | |
Wang et al. [141] | China | CSS | EC hypothesis | Positive | |
Wang et al. [78] | China | CSS | Misinformation | Negative | |
Williams et al. [188] | - | CSS | Climate Change and EC | Positive | |
Whittaker et al. [60] | - | Experiment | Extremism | YouTube, Gab, Reddit | Mixed |
Wieringa et al. [109] | Netherlands | CSS | EC hypothesis | Positive | |
Wolfowicz et al. [101] | Israel, Palestine | Mixed Methods | Extremism | Mixed | |
Wollebaek et al. [104] | Norway | Surveys | Cognitive states, emotions, personality traites | Social Media in General | Mixed |
Zerback and Kobilke [148] | Germany | Surveys | Extremism, radicalization and echo chambers | Social Media in General | Mixed |
Zollo et al. [50] | US | CSS | EC hypothesis | Positive | |
Zollo et al. [128] | US | CSS | Emotions and echo chambers | Positive |

### 1.4 D: Platform-specific aggregated tables

## Rights and permissions

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

## About this article

### Cite this article

Hartmann, D., Wang, S.M., Pohlmann, L. *et al.* A systematic review of echo chamber research: comparative analysis of conceptualizations, operationalizations, and varying outcomes.
*J Comput Soc Sc* **8**, 52 (2025). https://doi.org/10.1007/s42001-025-00381-z

Received:

Accepted:

Published:

Version of record:

DOI: https://doi.org/10.1007/s42001-025-00381-z
