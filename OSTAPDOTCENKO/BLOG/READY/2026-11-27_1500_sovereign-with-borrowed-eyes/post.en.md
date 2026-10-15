---
number: 32
date: "2026-11-27"
publish_time: "15:00"
rubric: "Tech (искусственный интеллект)"
category: "tech"
lang: "en"
title: "Sovereign, With Borrowed Eyes"
subtitle: "Korea and Japan are building their own AI so they don’t depend on America or China. The hardest part turns out to be agreeing on what “their own” means"
meta_description: "Korea’s national AI model contest, where Naver was dropped over a component from China’s Qwen and Upstage had to clear itself of resembling a Zhipu model; Japan’s $2.65 billion Sakana AI and the trillion-yen Noetra project. A wry essay on a sovereignty measured against China."
excerpt: "Korea and Japan are building their own AI so they don’t depend on America or China. The hardest part turns out to be agreeing on what “their own” means"
tag: "Artificial Intelligence"
time: "6 min"
slug: "sovereign-with-borrowed-eyes"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/09_Личный_блог_Tech_50_статей.docx"
image: "photo.jpg"
image_status: "утверждено"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "1ec208d9-3fe0-4bed-9d78-013f797703f8"
image_cost: "0.5"
image_logos: ""
image_prompt: "Photorealistic photo on two adjacent apartment balconies in Seoul at dusk: one neighbour leans over the low partition to hand a pair of binoculars to the other, both laughing, potted plants and drying laundry on the balconies, the Han River, its bridges and the city lights spreading out before them under a violet sky, wide 16:9 composition with a calm, uncluttered lower-left corner, warm friendly mood: everyone borrows eyes from a neighbour, then learns to see on their own. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

“Is the model yours?” “It’s ours.” “All of it?” “Our brain. Our architecture. Our training.” “And the eyes?” “The eyes… we borrowed from the neighbors. Good eyes. Open source. Everyone uses them.” “Then it’s not yours.”

That’s not a joke. Translated into plain language, it’s what happened at South Korea’s Ministry of Science and ICT in January 2026. And it’s the best way I know to start talking about sovereign AI in Asia.

In 2025, Korea launched a national contest for a homegrown foundation model that could compete with American and Chinese ones. Five teams were picked: Naver Cloud, SK Telecom, LG AI Research, NC AI and the startup Upstage. The state supplied GPUs, deadlines and elimination rounds. Think reality TV, except the prize isn’t a car but national pride.

## Eyes borrowed from the neighbors

After round one, in January 2026, two teams were out: Naver Cloud and NC AI. Naver’s exit made headlines. Its model scored well on performance and usability, but it used a pretrained vision encoder with weights from Alibaba’s open-source Qwen. The encoder is, roughly speaking, the model’s eyes: the part that turns an image into something a machine understands.

The ministry was blunt. Using someone else’s pretrained weights fails the independence test; at minimum, weights must be reset and trained from scratch. Second Vice Minister Ryu Je-myung said exactly that. Naver replied that its architecture and engine were its own and the encoder could be swapped. Researchers pointed out that reusing open components is standard practice everywhere. The press mentioned, carefully, a “China factor.”

Sovereignty means you can do everything yourself. Which is exactly why nobody does.

## The worst suspicion is Qwen inside

Two weeks earlier, Korea had staged another scene. On January 1, 2026, the head of a small AI company posted that Upstage’s Solar Open 100B looked suspiciously like a model from China’s Zhipu, citing a 96.8% similarity in one layer’s weights. Upstage didn’t argue in the comments. It offered a public review with outside experts, livestreamed on YouTube, and promised to open its code. The next day, the accuser apologized: similar layers, he conceded, don’t prove copying.

Accused on New Year’s Day, cleared on January 2. Some families take longer to finish the holiday leftovers.

But notice the yardstick. Not American models. Chinese ones. In 2026, the worst suspicion an Asian AI developer can face is: “Is that Qwen in there?”

## Borrowed eyes forbidden, borrowed muscles fine

The contest moved on. In February, Motif Technologies took a vacant slot. In August 2026, the ministry announced round two: LG AI Research with K-EXAONE 2.0, SK Telecom with A.X K2 and Upstage with Solar Open2 advanced. Motif was cut, even though Artificial Analysis ranked its model in the global top ten; the ministry cited weaker real-world applicability. Finalists were promised about 1,000 Nvidia B200 chips for the second half of the year, with round three set for the second half of 2026 and its rules still under discussion.

Note that sovereign AI is trained on American chips. Borrowed eyes are forbidden; borrowed muscles are fine. Eyes, apparently, are closer to the soul.

## Quietly, politely and with fish

Now Japan, where sovereignty is done the Japanese way: quietly, politely and with fish.

Sakana AI was founded in Tokyo in 2023 by former Google researchers David Ha, Llion Jones and Ren Ito. “Sakana” means fish: the idea is that a school of small models can outsmart one big one. In November 2025, it raised 20 billion yen at a $2.65 billion valuation, with banking group MUFG among the investors. It builds models that learn from small datasets and are tuned to Japanese language and culture, mostly for finance for now, with industry and government next.

So while China builds big models and Korea checks whose eyes they have, Japan is betting on a school of minnows. Very Japanese. In a country of vending machines on every corner, gigantism was never the national sport.

Meanwhile, the Japanese state went big. In summer 2026, the trade and industry ministry handed a five-year project to a consortium called Noetra: up to one trillion yen, about 44 companies, with SoftBank, Sony, NEC and Honda at the core. The plan: a model strong in Japanese in fiscal 2026, a model that handles text, images, video and sound by 2028, and AI that runs robots and vehicles by 2030. The goal is stated without diplomacy: depend on neither American nor Chinese AI.

Japan’s second AI Basic Plan, adopted in July 2026, calls this an “open approach to AI sovereignty”: no dependence on any particular vendor or country.

Open sovereignty. I’ve thought about that phrase a lot. I think it means you own the door but don’t install a lock. So the neighbors won’t be offended.

## All this fuss is a compliment

Seen from China, all this fuss is a compliment. Five years ago, sovereign AI meant “not depending on America.” Now it means “not depending on America or China,” with the second half said a little louder. Chinese open models have become so good and so accessible that the neighbors have to check whether one has moved in.

The best ad a product can get is a competitor’s rule banning it.

Still, history gets the last word here, not ministries. Japanese writing is half Chinese characters. Koreans wrote in Chinese script for many centuries before King Sejong gave them their own alphabet, and hanja still lives in Korean dictionaries. The sovereign languages that sovereign AI is now learning grew out of someone else’s characters.

And that’s fine. They became their own. It took a few centuries, but they did.

Everyone borrows eyes. Learning to see is up to you.

**Sources**

1.  The Korea Herald, «Open-source use, China-linked concerns fuel reputational risks in national AI race», 20.01.2026 — https://www.koreaherald.com/article/10658913 (пять команд, выбывание Naver Cloud из-за визуального энкодера и весов Qwen, позиция министерства и замминистра Рю Чжэ Мёна, критика экспертов, «китайский фактор»).
2.  The Korea Times, «LG AI Research, SK Telecom, Upstage survive next cut in national AI model project», 18.08.2026 — https://www.koreatimes.co.kr/business/tech-science/20260818/lg-ai-research-sk-telecom-upstage-survive-next-cut-in-national-ai-model-project (выбывание Naver Cloud и NC AI в январе, Motif в феврале, итоги второго этапа, K-EXAONE 2.0, A.X K2, Solar Open2, Motif 3 — 10-е место по AAII, около 1000 B200).
3.  Venture Square, «업스테이지 ‘AI 표절 논란’ 종결», 04.01.2026 — https://www.venturesquare.net/1030519/ (обвинение 1 января, 96,8 %, публичная проверка, извинение 2 января).
4.  TechCrunch, «Sakana AI raises $135M Series B at a $2.65B valuation to continue building AI models for Japan», 17.11.2025 — https://techcrunch.com/2025/11/17/sakana-ai-raises-135m-series-b-at-a-2-65b-valuation-to-continue-building-ai-models-for-japan (основатели, 20 млрд иен, MUFG, японский язык и культура, финансовый сектор).
5.  TechCrunch, 19.07.2026 — https://techcrunch.com/?p=3144105 (Noetra: до 1 трлн иен за пять лет, около 44 компаний, SoftBank, Sony, NEC, Honda, этапы 2026–2028–2030, цель не зависеть от американского и китайского ИИ).
6.  Let’s Data Science, «Japan Targets Sovereign AI Model and 10 Million Robots», 01.07.2026 — https://letsdatascience.com/news/japan-targets-sovereign-ai-model-and-10-million-robots-83b74c54 (решение METI о проекте Noetra, первый транш 387,3 млрд иен).
7.  MLex, «Japan adopts second AI basic plan, targets agentic AI and sovereignty», 14.07.2026 — https://www.mlex.com/mlex/artificial-intelligence/articles/2500643/japan-adopts-second-ai-basic-plan-targets-agentic-ai-and-sovereignty («открытый подход к суверенитету», без зависимости от отдельных поставщиков и стран).
