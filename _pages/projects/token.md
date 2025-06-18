---
title: "Token-based system for peer-review"
layout: textlay
excerpt: "A study from the Business Intelligence Group of the University of Bologna about the implementation of a token-based system for peer-review for scientific journal, to address the current problems of long decision times and increased editorial workloads."
sitemap: false
permalink: /token/
---

# Token-based system for peer-review

The peer-review system is facing a critical imbalance: while paper submissions continue to grow, reviewer availability remains stagnant, resulting in longer decision times and increased editorial workloads. Voluntary and reward-based initiatives have proven insufficient in resolving this issue. We propose a token-based mechanism that transforms peer-reviewing from a voluntary activity into a reciprocal obligation. Authors are required to spend tokens earned through reviewing in order to submit papers, ensuring a balanced review-to-submission ratio. Supported by a developed simulator, the token-based model significantly reduces editorial queues and review times, while incentivizing timely and high-quality reviews.

## Simulator

For reproducibility, the data and code of the simulator are available at <https://github.com/big-unibo/token-based-peer-review/>.

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