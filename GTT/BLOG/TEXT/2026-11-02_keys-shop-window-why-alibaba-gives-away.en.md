---
number: 2
date: "2026-11-02"
lang: "en"
title: "Keys to the Shop Window: Why Alibaba Gives Away Qwen, and How It Reached the Taobao Checkout"
seo_title: "Alibaba’s Qwen for Business: Apache 2.0 Open Models, Alibaba Cloud, Agentic Shopping in the Qwen App, and What to Ask in Hangzhou (as of October 2026)"
meta_description: "Why Alibaba open-sources its Qwen models, how Alibaba Cloud makes money from them, what the 2026 Apsara Conference revealed, how the Qwen app learned to order and pay through Taobao and Alipay, and what that means for manufacturers and sellers."
slug: "keys-shop-window-why-alibaba-gives-away"
source: "CONTROL/SOURCES/2026-10-10_тексты-ноябрь-декабрь/08_Блог_Global_Tech_Tour_66_статей.docx"
image: "2026-11-02_keys-shop-window-why-alibaba-gives-away.jpg"
image_status: "на согласовании"
image_model: "gpt_image_2_5 medium 1k 16:9"
image_job: "8b5f900a-aaaa-499c-aa83-e904452c068b"
image_cost: "0.5"
image_logos: "Alibaba"
image_prompt: "Photorealistic candid photo in a bright modern apartment in Hangzhou: a smiling young Chinese woman sits on a sofa holding her smartphone with a blurred chat on the screen, while at the open front door a courier in a plain jacket hands her husband a parcel, he laughs and holds it up to show her, warm afternoon light, wide 16:9 composition with the main subject in the center-right and a calm, uncluttered lower-left corner, delighted everyday mood of an AI assistant that orders and pays by itself. Realistic materials, natural colors. No text, no letters, no logos, no watermarks."
---

In business, “free” rarely travels alone. It comes with a contract, an appendix to the contract, and someone who calls a month later to check that everything is to your satisfaction. So when China’s biggest technology company spends years giving away its language models, an executive’s first question is the right one: where is the till?

There is a till. Two of them, in fact.

### What exactly is being given away

In August 2023 [Alibaba](/en/companies/alibaba) released Qwen-7B as open source, with commercial use allowed, the first of China’s tech giants to do so. Since then giving models away has become a system. The Qwen3 family, released at the end of April 2025, came under the Apache 2.0 licence, one of the most permissive there is: models from 0.6 billion to 235 billion parameters that you can build into your own products and sell.

By August 2026, the company says, more than 460 Qwen models had been released openly, downloaded more than 3 billion times, with over 300,000 derivative models built on top. For an independent benchmark, Hugging Face reports about 2 billion Qwen downloads on its platform in the first seven months of 2026, against 418 million for Google and 227 million for Meta.

The practical point for business: Qwen is not one model but a size range, like a line of machine tools. A small one can run on your own server and keep data inside your walls. A large one is easier to rent in the cloud. The choice depends on the task, not on who topped the latest leaderboard.

A model is downloaded once. It runs every day, and the question is whose hardware it runs on.

### Till number one: the cloud

Alibaba has answered the “where is the till” question in public. In February 2025 it pledged at least 380 billion yuan for cloud and AI infrastructure over three years. In August 2026 it reported AI and compute cloud revenue of $7.1 billion for the quarter, up 45% year on year.

Omdia puts China’s AI cloud market at 56.7 billion yuan in 2025, with Alibaba Cloud holding 38.1%, almost twice its nearest rival, [ByteDance](/en/companies/bytedance)’s Volcano Engine. Open models work for the cloud the way free samples work at a wholesale fair: you try it at home, you like it, and when you need volume you come back to rent capacity.

The Apsara Conference, which Alibaba holds in Hangzhou every autumn, showed on 22 September 2026 how seriously this is meant. The flagship Qwen3.8-Max has 2.4 trillion parameters; Qwen 4 is in training, with no date or licence terms announced; models of 5–10 trillion parameters are planned; Alibaba’s own Zhenwu V900 AI chip is due for mass production in Q1 2027; and the target is 20 gigawatts of Alibaba Cloud data-centre capacity by 2032. CEO Eddie Wu also said the open-weight Qwen-27B had become the most popular model among developers worldwide, and that Alibaba will keep releasing models for local deployment.

Twenty gigawatts is roughly twenty large power stations. A free model is very expensive for someone. Just not for the person who downloaded it.

### Till number two: the Taobao shop window

The second till matters more to anyone who sells. On 17 November 2025 Alibaba opened a public beta of the Qwen app, and on 15 January 2026 it plugged in its own ecosystem: Taobao, the instant-delivery service Taobao Instant Commerce, Alipay, the travel platform [Fliggy](/en/companies/fliggy) and Amap maps. At the launch, the in-chat assistant ordered 40 milk teas from a local chain and paid through Alipay, with the user required to confirm. The same update let the assistant book flights and hotels, call restaurants and process up to a hundred documents at once.

QuestMobile counted 167 million monthly active users for Qwen in May 2026. In August the app introduced paid tiers for its office assistant; basic access stayed free.

For manufacturers and sellers, this changes a familiar pattern. Shoppers used to search, scroll, read reviews and compare for themselves. Now an assistant sits between them and the shelf, searching, comparing and sometimes paying on their behalf. You will be selling not only to the customer but to the customer’s assistant. And the assistant, unlike the customer, is unmoved by nice packaging. It reads the specifications.

Machines will read the label. Product descriptions will have to work for people and machines at once.

### How to approach model choice (a rough guide)

This is general logic, not advice for a specific project.

1.  Data must not leave the building: look at small and mid-sized open models on your own servers.
2.  You need top accuracy on hard tasks: the flagship via a cloud API.
3.  The task is high-volume and simple (tagging, classification, drafts): the smallest model that copes. It is often enough.
4.  Before launch, check the licence of the specific version. Terms can differ between models and generations.
5.  Budget for moving to the next version. It will come sooner than you think.

### What to look at in Hangzhou

Hangzhou is the city where you can see Qwen from both sides of the till. On one side, Alibaba and its cloud. On the other, thousands of Zhejiang sellers, manufacturers and service firms trading through Taobao and Tmall and already living in a market where shoppers have AI helpers.

For an executive, the most useful conversations are with people deploying models themselves: a manufacturer running a small model on its own server, an integrator building Qwen-based tools for factories, a seller who rewrote product listings for AI search. We do not promise meetings with any specific company, but such conversations are possible in China, and the questions are worth preparing in advance.

A few to start with. Which Qwen version do you run, and why that one? On your own servers or in the cloud? What did it cost to move from the previous version? Have sales changed since shoppers got AI assistants, and how did you measure it?

### The bottom line

Alibaba does not give models away out of generosity, and does not pretend to. The model is the key, the cloud is the premises, and Taobao is the shop window, which now has a new kind of visitor. It never gets tired, never gets distracted and always reads the small print.

We could all learn to read it as carefully. Starting with the licence.
