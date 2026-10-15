---
number: 18
date: "2026-11-07"
publish_time: "15:00"
rubric: "Tech (ИИ)"
category: "tech"
lang: "en"
title: "Not in It for the Money"
subtitle: "How a Hangzhou hedge fund built a language model on the side, knocked a few hundred billion off someone else’s stock, and then spent eighteen months acting as if nothing had happened"
meta_description: "DeepSeek grew out of the quant fund High-Flyer, started China’s token price war in 2024, delivered the “DeepSeek moment” in January 2025, and in 2026 shipped V4 for Huawei chips and took outside money for the first time. A wry essay about a company that never meant to scare anyone."
excerpt: "How a Hangzhou hedge fund built a language model on the side, knocked a few hundred billion off someone else’s stock, and then spent eighteen months acting as if nothing had happened"
tag: "Artificial Intelligence"
time: "6 min"
slug: "not-it-for-money"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/09_Личный_блог_Tech_50_статей.docx"
image: "photo.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "7640b0d9-e864-4a7f-b766-fc155d5a6180"
image_cost: "0.5"
image_logos: "DeepSeek"
image_prompt: "Photorealistic candid photo in a modest, quiet research office in Hangzhou on a rainy evening: a small team of young engineers in hoodies and sweaters work at simple desks with monitors showing abstract training curves without numbers, a young woman smiles with quiet satisfaction as a colleague leans over to see her result, stacked boxes of graphics cards in the corner, cups of tea, rain streaks on the window with soft city lights, warm desk lamps, wide 16:9 composition with a calm, uncluttered lower-left corner, calm focused mood of a team that speaks little and is heard by everyone. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

> “It’s not about the money.” — Said by everyone who later made a lot of it

Everybody has written about DeepSeek. I held out, out of laziness, and I’m now proud of it. Eighteen months on, the story has settled like a good pot of tea: the foam is gone and what’s left is worth drinking.

Start with the paradox. The loudest Chinese AI company of recent years ran almost no ads, gave almost no interviews and took no outside investment until 2026. As a marketer, I find this personally offensive. We spend our careers telling clients that nothing sells without noise. DeepSeek sold everything, including other people’s shares, in total silence.

## It began with trading, not AI

It began with trading, not AI. In 2015 Liang Wenfeng co-founded the quant fund High-Flyer in Hangzhou. A quant fund is where the trading is done not by people with fire in their eyes but by algorithms with none. Algorithms need GPUs. By 2021, reportedly, Liang had bought around ten thousand Nvidia A100s, before the US restricted their sale to China.

Foresight or simply a habit of buying in bulk? History is silent. I lean toward bulk. Some people stock up on toilet paper. Some stock up on compute. Only one of those decisions moves markets.

In July 2023 the fund spun its research lab off as a separate company, DeepSeek. The fund paid; there were no outside investors. In 2025 the company had about 160 employees. That’s smaller than the marketing department at many drug companies, although, to be fair, marketing departments don’t train models. They train each other on who to cc.

## Started by a company with no sales team

The first time DeepSeek didn’t mean to scare anyone was May 2024. It released V2 and priced API access at 1 yuan per million input tokens and 2 yuan per million output tokens. Five days later Zhipu cut its price fivefold. ByteDance priced Doubao at 0.8 yuan. Alibaba slashed Qwen-Long by 97%. Four hours after Alibaba, Baidu made two of its models free.

That’s how China’s token price war began. It was started by a company with no sales team.

Some people walk into a room, say nothing, and everyone else starts apologizing.

## A wedding priced as the last toast

In December 2024 came V3, with a number in the technical report that everyone went on to quote: the final training run took 2.788 million H800 GPU hours, about $5.6 million. Jaws dropped. US labs were spending orders of magnitude more.

In fairness, the report says plainly that this covers only the final run, not the research and experiments before it. It’s like quoting the cost of a wedding as the price of the last toast. The toast really was cheap. Everything before it wasn’t.

In September 2025, in a paper in Nature, DeepSeek put the cost of training R1 on top of V3 at $294,000. Nobody gasped this time. People get used to anything, especially other people’s thrift.

In between came January. On January 20, 2025, DeepSeek released R1, an open-weights reasoning model. By January 27 its app had overtaken ChatGPT among free apps on the US App Store, and Nvidia lost about 17% and nearly $600 billion in market value in a single day. Bloomberg called it the largest one-day rout in market history.

A hedge fund is an organization that profits from other people’s volatility. Here it created volatility it apparently made no effort to profit from. Like a firefighter who drops a match in someone else’s warehouse and goes home for tea.

Nobody meant to scare anyone. They just uploaded some files.

## Almost everything, and almost nothing

What changed afterward? Almost everything, and almost nothing.

Everything, because open weights went from a hobbyist quirk to good manners in China. Even Baidu, whose CEO told staff in spring 2024 that open-source models made little sense, released its own a year later. Australia banned DeepSeek on government devices; the US defense budget for 2026 banned it on military and intelligence devices. In February 2026 Anthropic accused DeepSeek, along with Moonshot and MiniMax, of mass-harvesting Claude’s answers through fake accounts. Fame never travels alone. It brings auditors.

Nothing, because the company kept doing what it always did: shipping models. V3.1 in August 2025, V3.2 in December. On April 24, 2026, V4: 1.6 trillion parameters in the larger version, a one-million-token context, open weights and, for the first time, adaptation to Huawei’s Ascend chips. Huawei announced full support the same day, and DeepSeek later made a 75% price cut on its flagship permanent.

Export controls were meant as a fence. DeepSeek read them as a product spec.

## Hand over money and sit quietly

Then, in 2026, the unthinkable. DeepSeek took outside money. According to The Information, its first external round raised more than 50 billion yuan, about $7.4 billion, at a valuation above $50 billion. Liang himself put in about 20 billion yuan, Reuters reported. Tencent and battery maker CATL are named among the backers, and the state AI fund invested directly.

The structure is elegant. Outside investors came in through a partnership managed by Liang. No votes, five-year lock-up. In effect, they were allowed to hand over money and sit quietly. Investors were told, per the Financial Times, that long-term research and open models come before quick commercialization. In July, Bloomberg and the FT reported preparations for an IPO, possibly in 2027.

I’ve helped build a lot of investor decks. A slide that says “profit isn’t our priority and you won’t get a vote” is one I wouldn’t show my own family. DeepSeek showed it to Tencent. Tencent paid.

What moves me in this story isn’t the market cap. It’s the silence. Marketers spend their lives teaching clients to make noise: louder, brighter, more often, billboard at the city gates. And here’s a team that said almost nothing for years and simply published files and papers. Everyone heard them, from Hangzhou to Wall Street.

Not in it for the money. Money, like a cat, comes on its own once you stop calling it.

It stings a little, I admit. All those years teaching people how to speak, only to find that the best salesman is the one who keeps quiet.

**Sources**

1.  Wikipedia, «DeepSeek» — https://en.wikipedia.org/wiki/DeepSeek (основание 17.07.2023, High-Flyer с 2015 г., около 10 000 A100 к 2021 г., около 160 сотрудников, даты R1, V3.1, V3.2, первое место в App Store, запреты в Австралии и по NDAA FY2026; сверено с источниками ниже).
2.  DeepSeek-AI, «DeepSeek-V3 Technical Report», arXiv 2412.19437, 12.2024 — https://arxiv.org/abs/2412.19437 (2,788 млн GPU-часов H800, 5,576 млн долл., только финальный прогон).
3.  KrASIA, «LLM prices hit rock bottom in China as Alibaba Cloud enters the fray», 05.2024 — https://kr-asia.com/llm-prices-hit-rock-bottom-in-china-as-alibaba-cloud-enters-the-fray (V2 6 мая 2024 г.: 1 и 2 юаня; Zhipu, ByteDance 0,8 юаня, Alibaba −97 %, Baidu бесплатно).
4.  Bloomberg, «Nvidia’s $589 Billion DeepSeek Rout Is Largest in Market History», 27.01.2025 — https://www.bloomberg.com/news/articles/2025-01-27/asml-sinks-as-china-ai-startup-triggers-panic-in-tech-stocks
5.  Reuters / CTV News, «China’s DeepSeek says its hit AI model cost just US$294,000 to train», 18.09.2025 — https://www.ctvnews.ca/business/article/chinas-deepseek-says-its-hit-ai-model-cost-just-us294000-to-train/
6.  TechNode, «Open-source models make little sense, says Baidu CEO», 15.04.2024 — https://technode.com/2024/04/15/open-source-models-make-little-sense-says-baidu-ceo/
7.  Reuters / Yahoo, «Factbox: DeepSeek V4», 24.04.2026 — https://tech.yahoo.com/ai/articles/factbox-deepseek-v4-chinese-ai-135916188.html (V4 Pro и Flash, адаптация под Huawei Ascend, заявление Huawei).
8.  NYU Shanghai RITS, «DeepSeek Releases V4: Open-Source 1.6T MoE with 1M Context», 04.2026 — https://rits.shanghai.nyu.edu/ai/deepseek-releases-v4-open-source-1-6t-moe-with-1m-context (1,6 трлн параметров, контекст 1 млн токенов, открытые веса).
9.  Engadget, «DeepSeek permanently reduces the price of its flagship V4 model by 75 percent», 05.2026 — https://engadget.com/2180062/deepseek-permanently-reduces-the-price-of-its-flagship-v4-model-by-75-percent
10. The Decoder, «DeepSeek takes outside money for the first time at a 50 billion valuation», 06.2026 — https://the-decoder.com/deepseek-takes-outside-money-for-the-first-time-at-a-50-billion-valuation/ (50 млрд юаней, оценка выше 50 млрд долл., вклад Ляна около 20 млрд юаней, Tencent, CATL, госфонд, партнёрство без права голоса, пять лет блокировки; ссылки на The Information и Reuters).
11. Trivium China, «DeepSeek reportedly closes USD 7 billion funding round», 16.06.2026 — https://triviumchina.com/2026/06/16/deepseek-reportedly-closes-usd-7-billion-funding-round/
12. W.Media, «DeepSeek explores new funding round as IPO preparations begin», 15.07.2026 — https://w.media/41663-2/ (подготовка к IPO, возможный листинг в 2027 г., позиция для инвесторов по данным FT).
