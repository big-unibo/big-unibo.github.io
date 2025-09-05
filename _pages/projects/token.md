---
title: "Token-based system for peer-review"
layout: textlay
excerpt: "A study from the Business Intelligence Group of the University of Bologna about the implementation of a token-based system for peer-review for scientific journal, to address the current problems of long decision times and increased editorial workloads."
sitemap: false
permalink: /token/
---

# Token-based system for peer-review

The peer-review system is facing a critical imbalance: while paper submissions continue to grow, reviewer availability remains stagnant, resulting in longer decision times and increased editorial workloads. Voluntary and reward-based initiatives have proven insufficient in resolving this issue. We propose a token-based mechanism that transforms peer-reviewing from a voluntary activity into a reciprocal obligation. Authors are required to spend tokens earned through reviewing in order to submit papers, ensuring a balanced review-to-submission ratio. Supported by a developed simulator, the token-based model significantly reduces editorial queues and review times, while incentivizing timely and high-quality reviews.

## Survey

From March to April 2025, we opened an [anonymous survey](https://forms.gle/pDZbro8WhbrqDnLfA) among Chief and Associate Editors of the computer science scientific journals, chosen by varying different areas, publishers, and quality of the journals. Out of 100 invitations, we collected 30 answers. The aggregated outcomes are here reported.

(*) Questions marked with an asterisk are open-ended questions, which are here summarized and aggregated.

- Rate your expertise level as Editor of computer science journals, on a scale from 1 (low) to 5 (high).
  - "1": 0 (0.0%)
  - "2": 0 (0.0%)
  - "3": 3 (10.0%)
  - "4": 13 (43.3%)
  - "5": 14 (46.7%)

- How serious do you think the problem of delay in the review process in peer-review journals due to lack of available reviewers is, on a scale from 1 (low) to 5 (high).
  - "1": 0 (0.0%)
  - "2": 0 (0.0%)
  - "3": 3 (10.0%)
  - "4": 8 (26.7%)
  - "5": 19 (63.3%)

- Do you think the problem has been worsening over the last few years?
  - "Yes": 29 (96.7%)
  - "No": 1 (3.3%)

- In your experience, how long does the review process for a journal article take? Consider the time from submission to first-decision, excluding desk-rejects (answer in months).
  - "2": 2 (6.7%)
  - "3": 2 (6.7%)
  - "4": 5 (16.7%)
  - "5": 4 (13.3%)
  - "6": 3 (10.0%)
  - "8": 5 (16.7%)
  - "12": 6 (20.0%)
  - "18": 1 (3.3%)
  - "24": 1 (3.3%)
  - "30": 1 (3.3%)

- How burdensome do you find the search for reviewers, on a scale from 1 (low) to 5 (high).
  - "1": 0 (0%)
  - "2": 0 (0%)
  - "3": 2 (6.7%)
  - "4": 15 (50.0%)
  - "5": 13 (43.3%)

- For each reviewer that accepts your invitation, how many do you contact on average?
  - "2": 5 (16.7%)
  - "3": 10 (13%)
  - "4": 2 (33.3%)
  - "5": 5 (47%)
  - "6": 1 (3.3%)
  - "7": 1 (3.3%)
  - "8": 3 (10.0%)
  - "10": 1 (3.3%)
  - "12": 1 (3.3%)
  - "15": 1 (3.3%)

- Which are the root causes of the problem, in your opinion? (*)
  - "There are too many (low quality) submissions": 5 (16.7%)
  - "There is a lack of good Associate Editors": 1 (3.3%)
  - "There is no compensation/reward for reviews": 3 (10%)
  - "Good reviewers are too busy": 3 (10%)

- How would you rate the effectiveness of a token-based system, where authors can submit papers only if they have done reviews? The basic idea is that 1 token is given to a reviewer for each completed review, and each submission requires N tokens from (any of) the authors (where N is the number of reviews needed for each paper). Vote on a scale from 1 (low) to 5 (high).
  - "1": 9 (30.0%)
  - "2": 2 (6.7%)
  - "3": 10 (33.3%)
  - "4": 8 (26.7%)
  - "5": 1 (3.3%)

- Do you think this system would be ethical? (*)
  - "Yes": 12 (40.0%)
  - "No": 7 (23.3%)
  - "Other": 11 (36.7%)
    - "Junior researchers may be disadvantaged": 7 (23.3%)
    - "It could be subject to unethical exploitation": 3 (10.0%)
    - "The quality of reviews may decrease": 3 (10.0%)

- Do you think this system would be accepted by the community? (*)
  - "Yes": 7 (23.3%)
  - "No": 15 (50.0%)
  - "Maybe/Gradually": 8 (26.7%)

- Do you foresee any potential issues? (*)
  - "The quality of reviews may decrease": 13 (43.3%)
  - "Junior researchers may be disadvantaged": 5 (16.7%)
  - "It could be subject to unethical exploitation": 5 (16.7%)
  - "There could be journal interoperability issues": 5 (16.7%)
  - "The community (or part of it) would oppose it": 3 (10%)
  - "There is a cold-start problem": 2 (6.7%)
  - "There could be DEI-related issues": 1 (3.3%)

- Are you familiar with initiatives like Publons, ReviewerCredits, and Peerage of Science?
  - "Yes": 5 (16.7%)
  - "I have only heard of them": 15 (50.0%)
  - "No": 10 (33.3%)

- If yes, what is your opinion about them? (*)
  - "I don't know enough to judge": 12 (40.0%)
  - "They only partially work": 4 (13.3%)
  - "They don't work": 3 (10.0%)
  - "(no answer)": 11 (36.7%)

## Simulator

For reproducibility, the data and code of the simulator are available at [https://github.com/big-unibo/token-based-peer-review/](https://github.com/big-unibo/token-based-peer-review/).

### Data sources

All statistics used to configure the simulator are retrieved from the following sources:
- The [DBLP computer science bibliography](https://dblp.uni-trier.de/db/), which provides its dataset in XML format at [this link](https://dblp.uni-trier.de/xml/).
- The [Scimago Journal & Country Rank](https://www.scimagojr.com/) website, considering in particular the journals under the [Computer Science area](https://www.scimagojr.com/journalrank.php?area=1700).
- The official websites of more than 700 journals, among those listed by Scimago in the reference above.
- The survey mentioned above.

### Parameters

The simulator provides the following parameters:

- *Number of researchers*: the number of agents in the simulation, which will act as authors and reviewers.
    - Default: 135972. 
    - This is based on DBLP statistics and corresponds to the number of active authors in 2024, divided by the average number of authors per paper; thus, each agent corresponds to a group of researchers.
- *Initial tokens per researcher*: the number of tokens assigned to each agent when the token-based mechanism is activated.
    - Default: 3. 
- *Daily paper generation probability*: the daily probability with which each agent generates a new paper to submit. 
    - Default: 0.023. 
    - This is based on DBLP statistics, so that the same amount of papers submitted in 2024 is generated in the simulation. The number of submitted papers is determined as the number of papers published in 2024 divided by the an acceptance rate of 0.19, which is the average acceptance rate collected from the websites of over 700 journals.
- *Probability of 2 (instead of 3) reviews*: the probability that a paper is submitted to a journal requiring 2 reviews instead of 3.
    - Default: 0.73. 
    - This is based on the average number of reviews declared on the websites of over 700 journals.
- *Probability of accepting invite (Lazy reviewer)*: the probability that a lazy reviewer (i.e., one who does not need tokens) accepts a reviewing invitation.
    - Default: 0.2. 
    - This is based on the average number of invites sent per review declared by the people interviewed in our survey.
- *Probability of accepting invite (Eager reviewer)*: the probability that an eager reviewer (i.e., one who needs tokens to submit a paper) accepts a reviewing invitation.
    - Default: 1.0. 
- *N. of daily invites per needed review*: the number of invites that an editor sends in a day for each review that must be assigned.
    - Default: 1. 
- *N. of days before tokens are enable*: the number of days after which the token-based mechanism is activated; before that, generated papers are automatically submitted.
    - Default: 1825 (5 years). 
    - An initialization period of 3+ years is recommended for the system to stabilize.
- *Enable max n. of yearly reviews per author*: if enabled, reviewers refuse any invitation if they have done *enough* reviews in the previous 365 days.
    - Default: yes. 
    - If enabled, the maximum number of yearly reviews per reviewer varies from 4 to 34; the distribution of this value to the researchers is made in a way to ensure that the yearly demand for reviews is met (considering the default number of researchers with the default probability of paper generation), ensuring the continuity of the system.

### Simulation process

The iterations of the simulation correspond to days. Also, the simulator assumes the existence of a single Publisher Management System (PMS).

Each researcher is associated with a **status**, that determines the probability to accept a review invitation (see parameters above):
- *Eager* if the researcher needs the assignment of new reviews to earn the tokens needed to submit one or more papers.
- *Lazy* if otherwise.

When a review is assigned, the reviewing time is randomly picked based on the histogram of reviewing times declared by the journals' websites that we crawled. This reviewing time can be updated if the reviewer becomes eager for tokens.

Every day, the following operations are carried out.
- For every researcher
    - **Generate papers to submit**
        - Randomly determine whether the author is ready to submit a paper (based on the *Daily paper generation probability*); in such a case, the number of reviewers required (based on the *Probability of 2 (instead of 3) reviews*) is randomly picked and the paper is added to the researcher's queue of papers to submit.
    - **Submit reviews (and earn tokens, if enabled)**
        - If the researcher has papers to review scheduled for the current day, the review is submitted and a token is collected (if tokens are enabled)
    - **Submit papers (and spend tokens, if enabled)**
        - If the researcher has papers to submit, he/she submits them based on the availability of tokens (if tokens are enabled)
    - **Update status (if tokens are enabled)**
        - If more tokens are needed, the researchers anticipates the reviewing time of the assigned reviews that will grant the necessary tokens
        - If more reviews are needed to earn the necessary token, the reviewer becomes *eager*; otherwise he/she remains (or goes back to being) *lazy*
    
- For the PMS
    - **Invite reviewers for submitted papers**
        - Each paper is handled 4 days after its submission
        - For every review needed by the paper, *n* reviewers are randomly invited, where *n* is the *N. of daily invites per needed review*
        - The probability of the reviewer accepting the invite depends on his/her status and his/her number of reviews already accepted in the last 365 days
        - If the review is accepted by an *eager* reviewer, his/her status is possibly set back to *lazy* if this token fullfils his/her need for tokens

