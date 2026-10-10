---
number: 28
date: "2026-12-08"
rubric: "Tech (искусственный интеллект)"
category: "tech"
lang: "en"
title: "Homegrown Silicon"
subtitle: "How Huawei builds AI accelerators under sanctions, why Beijing is in no hurry to buy the Nvidia chips it’s now allowed to have, and what self-reliance costs when you count it in megawatts rather than yuan"
meta_description: "Huawei has been on the U.S. Entity List since 2019, and Washington says using its Ascend chips anywhere in the world is risky. Yet DeepSeek V4 ran on Ascend on day one, Huawei promises a new chip every year, and China has been slow to buy the H200s it’s now allowed. A wry essay on tech self-reliance and its price."
excerpt: "How Huawei builds AI accelerators under sanctions, why Beijing is in no hurry to buy the Nvidia chips it’s now allowed to have, and what self-reliance costs when you count it in megawatts rather than yuan"
tag: "Artificial Intelligence"
time: "5 min"
slug: "homegrown-silicon"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/09_Личный_блог_Tech_50_статей.docx"
image: "2026-12-08_homegrown-silicon.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "66dae1b4-2840-47d8-98d9-983ae074e51b"
image_cost: "0.5"
image_logos: "Huawei"
image_prompt: "Photorealistic documentary photo in a bright Chinese engineering lab: a team of young engineers assembles a tall AI computing cabinet, one sliding one of many identical accelerator boards into a densely packed rack while another connects thick bundles of orange optical cables, a long row of identical boards waits on an anti-static bench, the team exchanging satisfied smiles, cool daylight and white LED lighting, wide 16:9 composition with a calm, uncluttered lower-left corner, determined optimistic mood: thousands of ordinary chips taught to work as one. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

To build your own AI chip when you’ve been banned from almost everything, you need:

1.  Lithography equipment nobody will sell you.
2.  High-bandwidth memory nobody will sell you either.
3.  A software stack the whole world has been using for fifteen years. Not yours.
4.  Customers willing to wait while you catch up.
5.  Money and years.
6.  A ban on buying the other guy’s product. Optional, but it really helps.

Item six looks out of place. It’s the most important one.

I understand chips the way the average driver understands an engine: I know where the fluids go, and I can nod knowingly at a strange noise. But in the Huawei Ascend story the engine isn’t the point. The point is how you drive when every gas station has been closed to you.

## It’s called global reach

In May 2019 the U.S. Commerce Department put Huawei on the Entity List. The restrictions were tightened turn by turn after that: American technology, foreign fabs, equipment. In May 2025 came guidance that moved the issue from selling to existing. Using Ascend 910B, 910C or 910D chips anywhere in the world, in Washington’s view, risks violating U.S. export controls, because the chips themselves were likely made in violation of them.

Anywhere in the world. As a marketer, I recognize that. It’s called global reach.

## Eight thousand average chips that get along

Speaking of reach. At Huawei Connect in September 2025 the company published a multi-year roadmap: Ascend 950PR in Q1 2026, 950DT in Q4, then the 960 and 970. The 950 series uses Huawei’s own HBM memory. And an Atlas 950 SuperPoD with 8,192 chips.

Deputy chairman Eric Xu said something you rarely hear at a company’s own conference: a single Huawei chip still trails Nvidia. So the bet is on interconnect, on making many average chips act like one strong one.

If you can’t build one strong chip, build eight thousand average ones and teach them to get along.

## Paying in currencies you didn’t expect

Now the price. Self-reliance is always more expensive; you just pay in currencies you didn’t expect.

You pay in electricity. Many average chips draw more than a few strong ones, so Chinese superclusters are also a question of megawatts.

You pay in engineering time. The world’s AI was written for CUDA, Nvidia’s software platform. Every model and every optimization has to be ported to Ascend, rewritten and tested again.

And you pay in doubt. When DeepSeek V4 came out in April 2026, its technical report said the parallelism scheme had been validated on both Nvidia GPUs and Ascend. The trade press immediately added that this didn’t mean the model was trained entirely on Huawei. The Register also recalled that DeepSeek’s earlier attempt to train on Chinese chips reportedly failed and the company went back to Nvidia.

Still, on V4’s launch day Huawei, Cambricon, Hygon, Moore Threads and several other Chinese chipmakers announced that the model already ran on their hardware. Everyone in formation, everyone reporting for duty.

## Sanctions are Huawei’s best sales team

The most interesting part began when the ban was no longer needed. In January 2026 the U.S. formalized terms for selling Nvidia H200s to China: inspection on U.S. soil and 25% of each sale to the Treasury. Permitted. Go ahead.

China didn’t. In May, after meeting Xi Jinping, President Trump told reporters Beijing had “chose\[n\] not to” approve purchases because it wants to develop its own. Nvidia CEO Jensen Huang said the company’s China share had fallen from about 95% to nearly zero. In its report for the quarter ending in late July, Nvidia disclosed its first H200 sales to Chinese customers: a small number, under 1% of data center revenue.

Sanctions are Huawei’s best sales team. They work for free, seven days a week.

I’ve watched the same scene in negotiations for years. The client says they support domestic suppliers, then quietly asks whether the imported option might still be possible. This time in China there was no one to ask. Item six did its job.

## A challenger pulling its deadlines forward

At Huawei Connect in Shanghai in September 2026, chairman Wang Tao said the Ascend 960DT would be ready in Q1 2027, three quarters ahead of plan, with the 960PR inference chip in Q3. Then the 970 in 2028 and the 980 in 2029. One chip a year, as promised.

A challenger pulling its own deadlines forward is a rare sight. Deadlines usually move the other way. I’d know. I’ve moved a few.

So who wins? I won’t pretend to know. A single Chinese chip is still weaker, as Huawei itself admits. But China now has something it lacked in 2019: a home market that has to buy domestic, and a supplier that has to get better every year.

Self-reliance means paying more, but paying yourself.

I sometimes think the strongest engineering schools grow not where everything is allowed, but where everything is banned and the work still has to be done. That isn’t praise for bans. It’s a sad observation about people: we learn best when no one is waiting for us.

**Sources**

1.  Akin Gump, «Commerce Adds Huawei, Its Non-US Affiliates Worldwide and Others to the Entity List», май 2019 — https://www.akingump.com/en/insights/alerts/commerce-adds-huawei-its-non-us-affiliates-worldwide-and-others (внесение Huawei в Entity List).
2.  Miller & Chevalier, «Key Takeaways: BIS Announcements and Guidance Related to Advanced Computing», май 2025 — https://www.millerchevalier.com/publication/trade-compliance-flash-key-takeaways-bis-announcements-and-guidance-related-advanced (разъяснение BIS от 13.05.2025: Ascend 910B, 910C, 910D, риск использования в любой точке мира).
3.  TrendForce, «Huawei Unveils Ascend 950 with In-House HBM in 2026, Touts SuperPoD to Rival NVIDIA», 18.09.2025 — https://www.trendforce.com/news/2025/09/18/news-huawei-unveils-ascend-950-with-in-house-hbm-in-2026-touts-superpod-to-rival-nvidia/ (дорожная карта 950PR/950DT/960/970, собственная HBM, Atlas 950 на 8192 чипа, признание Эрика Сюя).
4.  The Register, «DeepSeek V4», 24.04.2026 — https://www.theregister.com/2026/04/24/deepseek_v4/ (проверка на Nvidia и Ascend; модель не обязательно обучена на Huawei; прежняя неудачная попытка).
5.  TrendForce, «Huawei Ascend, Cambricon and Hygon Completed Day 0 Adaptation to DeepSeek-V4», 29.04.2026 — https://www.trendforce.com/news/2026/04/29/news-huawei-ascend-cambricon-and-hygon-completed-day-0-adaptation-to-deepseek-v4/ (адаптация в день выхода у китайских производителей).
6.  Tom’s Hardware, «Trump says China is blocking H200 purchases», 15.05.2026 — https://www.tomshardware.com/tech-industry/trump-says-china-is-blocking-h200-purchases (условия января 2026: проверка в США, 25 %; слова Трампа; оценка Хуанга о доле 95 % → почти ноль).
7.  Bloomberg Tax / Bloomberg, «Nvidia Steps Back Into China Market With First H200 Chip Sales», 26.08.2026 — https://news.bloombergtax.com/international-trade/nvidia-steps-back-into-china-market-with-first-h200-chip-sales (небольшие продажи H200, менее 1 % выручки дата-центров).
8.  South China Morning Post, «Huawei quickens AI chip pace, promises next entrant 3 quarters early», 17.09.2026 — https://scmp.com/tech/big-tech/article/3367832/huawei-quickens-ai-chip-pace-promises-next-entrant-3-quarters-early (Ascend 960DT в I кв. 2027, 960PR в III кв. 2027, 970 и 980, ежегодный цикл).
